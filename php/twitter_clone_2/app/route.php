<?php

    namespace app;

    use mf\init\Bootstrap;
    
    class Route extends Bootstrap {

        // Incio das rotas
        protected function initRoutes() {

            $routes['home'] = array(
                'route' => '/',
                'controller' => 'indexController',
                'action' => 'index'
            );

            $routes['inscreverse'] = array(
                'route' => '/inscreverse',
                'controller' => 'indexController',
                'action' => 'inscreverse'
            );

            $routes['registrar'] = array(
                'route' => '/registrar',
                'controller' => 'indexController',
                'action' => 'registrar'
            );

            $routes['autenticar'] = array(
                'route' => '/autenticar',
                'controller' => 'AuthController',
                'action' => 'autenticar'
            );

            $routes['sair'] = array(
                'route' => '/sair',
                'controller' => 'AuthController',
                'action' => 'sair'
            );

            $routes['timeline'] = array(
                'route' => '/timeline',
                'controller' => 'AppController',
                'action' => 'timeline'
            );

            $routes['tweet'] = array(
                'route' => '/tweet',
                'controller' => 'AppController',
                'action' => 'tweet'
            );

            $routes['quem_seguir'] = array(
                'route' => '/quem_seguir',
                'controller' => 'AppController',
                'action' => 'quemSeguir'
            );

            $routes['acao'] = array(
                'route' => '/acao',
                'controller' => 'AppController',
                'action' => 'acao'
            );



            $this->setRoutes($routes);
        }
       
    }
