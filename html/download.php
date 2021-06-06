<?php
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true');
header("Content-Type: application/json;charset=utf-8");
if(isset($_GET["data"])){
    $fn = array();
    $data = scandir('/var/www/html/resources/');
    foreach($data as $value){
        if($value != '.' && $value != '..' && $value != 'index'){
            $fn[] = $value;
        }
    }

    $file = array();
    foreach($fn as $value){
        $tmp_path = '/var/www/html/download.php?file='.$value;
        $fp_attr = fopen($tmp_path.'/attr', 'r');
        $attr = fread($fp_attr, 4096);

        $tmp = '{"name":"'.$value.', "attr":"'.$attr.'", "path":"'.$tmp_path.'"}';
        $file[] = $tmp;
    }

    $num = count($file);
    $res = '{"num":"'.$num.'", "filename":[';
    foreach($file as $value){
        $res = $res.$value.', ';
    }
    $res = substr($res, 0, strlen($res)-2);
    $res = $res.']}';
    echo $res;
}
?>
