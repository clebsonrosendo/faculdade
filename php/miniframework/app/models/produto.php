<?php 

    namespace app\models;

    use mf\model\Model;

    class Produto extends Model{

        public function getProdutos() {

            $query = "select id, descricao, preco from tb_produtos";
            return $this->db->query($query)->fetchAll();
        }
    }



?>