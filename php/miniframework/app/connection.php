<?php 

    namespace app;

    class Connection {

        public static function getDB() {
            try {

                $conn = new \PDO(
                    "mysql:host=localhost;dbname=mvc;charset=utf8",
                    "root",
                    "root"
                );

                return $conn;
            } catch(\PDOException $e) {
                print_r($e);
            }
        }
    }


?>