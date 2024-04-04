<?php 

    namespace app\controllers;

    // Recursos framework
    use mf\model\Container;
    use mf\controller\Action;

    // Os models
    use app\models\Produto;
    use app\models\Info;

    class IndexController extends Action {

        public function index() {

            $produto = Container::getModel('produto');
            $produtos = $produto->getProdutos();

            // Instância de visualização
            $this->view->dados = $produtos;
            $this->render('index', 'layout1');
        }

        public function sobreNos() {
            
            $info = Container::getModel('info');
            $informacoes = $info->getInfo();

            // Instância de visualização
            $this->view->dados = $informacoes;
            $this->render('sobreNos', 'layout1');
        }

    }

?>