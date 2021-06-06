<?php
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true');
header("Content-Type: application/json;charset=utf-8");
if(isset($_GET["school"]) && isset($_GET["id"]) && isset($_GET["username"])){

    $school = $_GET["school"];
    $username = $_GET["username"];
    $identity = $_GET["id"];

    $res = 0;
    $key = array();

    exec("/usr/bin/python /var/www/html/sk.py ".$school." ".$username." ".$identity, $key, $res);

    if($res != 0){
            $result = '{"result":"fail", "sk":"fail", "pk":"fail", "id":"fail"}';
            echo $result;
    }

    else{
            //$result = '{"result":"success", "sk":"'.$key[0].'", "pk":"'.$key[1].'", "id":"'.$key[2].'"}';
            $result = '   sk:'.$key[0].'   pk:'.$key[1].'   id:'.$key[2];
            echo $result;
    }

}

?>
