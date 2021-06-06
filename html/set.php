<?php
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true');
header("Content-Type: application/json;charset=utf-8");
if(isset($_POST["attr"])){
    mkdir('/var/www/html/error');
    $attr = $_POST["attr"];
    $attr_file = fopen('/var/www/html/tmp_key_attr/key_attr.txt', "w") or mkdir('/var/www/html/error');
    fwrite($attr_file, $attr);
    fclose($attr_file);
    echo '{"result":"success"}';
}

?>
