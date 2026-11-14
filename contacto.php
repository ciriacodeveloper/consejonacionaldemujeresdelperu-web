<?php
/**
 * Formulario de contacto — Consejo Nacional de Mujeres del Perú
 * Recibe el POST del formulario, valida los campos y envía el mensaje por correo.
 */
declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$DESTINO     = 'cnmp031923@gmail.com';
$REMITENTE   = 'noreply@consejonacionaldemujeresdelperu.com';
$ASUNTOS     = [
    'afiliacion'   => 'Solicitud de afiliación',
    'voluntariado' => 'Colaboración en una comisión',
    'asociacion'   => 'Afiliación de una asociación',
    'filial'       => 'Constitución de una filial regional',
    'alianza'      => 'Propuesta de alianza institucional',
    'prensa'       => 'Prensa y comunicaciones',
    'consulta'     => 'Consulta general',
];

function responder(bool $ok, string $mensaje, int $codigo = 200): void {
    http_response_code($codigo);
    echo json_encode(['ok' => $ok, 'message' => $mensaje], JSON_UNESCAPED_UNICODE);
    exit;
}
function campo(string $k, int $max = 500): string {
    $v = isset($_POST[$k]) ? trim((string) $_POST[$k]) : '';
    $v = str_replace(["\r", "\n"], ' ', $v);
    return mb_substr($v, 0, $max);
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    responder(false, 'Método no permitido.', 405);
}
// Honeypot: los bots suelen rellenar este campo oculto.
if (!empty($_POST['sitio_web'])) {
    responder(true, 'Gracias, recibimos tu mensaje.');
}

$nombre   = campo('nombre', 120);
$email    = campo('email', 160);
$telefono = campo('telefono', 40);
$asunto   = campo('asunto', 30);
$mensaje  = isset($_POST['mensaje']) ? trim((string) $_POST['mensaje']) : '';
$mensaje  = mb_substr($mensaje, 0, 4000);

if ($nombre === '' || mb_strlen($nombre) < 3) {
    responder(false, 'Por favor, indica tu nombre.', 422);
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    responder(false, 'Por favor, indica un correo electrónico válido.', 422);
}
if (!isset($ASUNTOS[$asunto])) {
    responder(false, 'Por favor, selecciona el motivo de tu mensaje.', 422);
}
if (mb_strlen($mensaje) < 10) {
    responder(false, 'Cuéntanos un poco más en tu mensaje (mínimo 10 caracteres).', 422);
}
if (empty($_POST['privacidad'])) {
    responder(false, 'Debes autorizar el tratamiento de tus datos para enviar el mensaje.', 422);
}

$titulo = '[Web CNMP] ' . $ASUNTOS[$asunto] . ' - ' . $nombre;
$cuerpo = "Nuevo mensaje desde el formulario de contacto del sitio web.\n\n"
    . "Nombre:   {$nombre}\n"
    . "Correo:   {$email}\n"
    . "Teléfono: " . ($telefono !== '' ? $telefono : '-') . "\n"
    . "Motivo:   {$ASUNTOS[$asunto]}\n"
    . "Fecha:    " . date('d/m/Y H:i') . "\n"
    . "IP:       " . ($_SERVER['REMOTE_ADDR'] ?? '-') . "\n\n"
    . "Mensaje:\n" . wordwrap($mensaje, 90, "\n", true) . "\n";

$cabeceras = "From: Consejo Nacional de Mujeres del Perú <{$REMITENTE}>\r\n"
    . "Reply-To: {$nombre} <{$email}>\r\n"
    . "MIME-Version: 1.0\r\n"
    . "Content-Type: text/plain; charset=UTF-8\r\n"
    . "Content-Transfer-Encoding: 8bit\r\n";

$enviado = @mail($DESTINO, '=?UTF-8?B?' . base64_encode($titulo) . '?=', $cuerpo, $cabeceras, '-f ' . $REMITENTE);

if ($enviado) {
    responder(true, 'Gracias, ' . explode(' ', $nombre)[0] . '. Recibimos tu mensaje y te responderemos pronto.');
}
responder(false, 'No pudimos enviar el mensaje en este momento. Escríbenos a ' . $DESTINO . '.', 500);
