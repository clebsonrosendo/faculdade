<?php 

    namespace app\models;

    use mf\model\Model;

    class Info extends Model {

        public function getInfo() {

            $query = "select titulo, descricao from tb_info";
            return $this->db->query($query)->fetchAll();
        }
    }



?>