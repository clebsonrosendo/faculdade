<?php

use Slim\Http\Response;

require '../vendor/autoload.php';

$app = new \Slim\App;

// Definindo rotas
$app->get('/postagens', function() {
    echo 'Lista de postagens';
});

// Definindo rotas com parâmetros {} opcionais []
$app->get('/usuarios[/{ano}[/{mes}]]', function($request, $response) {
    $ano = $request->getAttribute('ano');
    $mes = $request->getAttribute('mes');
});

// Definindo rotas com qualquer tipo de parâmetro
$app->get('/usuarios[/{itens:.*}]', function($request, $response) {
    $itens = $request->getAttribute('itens');
});

// Nomear rotas 
$app->get('/blog/postagens/{id}', function($request, $response) { 
    echo "Exemplo de rota nomeada";
});


$app->run(); 

?>