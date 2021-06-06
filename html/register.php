<?php
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true'); 
header("Content-Type: application/json;charset=utf-8"); 
if(isset($_GET["username"]) && isset($_GET["password"])){
    $username = $_GET["username"];
    $password = $_GET["password"];

    $fn = array();
    $data = scandir('./users/');
    foreach($data as $value){
        if($value != '.' && $value != '..'){
            $tmp = explode('.', $value);
            $fn[] = $tmp[0];
        }
    }

    if(in_array($username, $fn)){
        $error = "username has been registered";
        $result = '{"result":"fail", "reason":"'.$error.'"}';
        echo $result;
    }

    else{
        $key = "";
        $res = 0;
        $fp = fopen('/var/www/html/users/'.$username, 'w');
        fclose($fp);
        exec("/usr/bin/python /var/www/html/python_api/register.py ".$username." ".$password, $key, $res);
        if($res != 0){
            $error = "unable to register";
            $result = '{"result":"fail", "reason":"'.$error.'"}';
            echo $result;
        }
        else if($key[0] !='success'){

        }
        else{
            $result = '{"result":"success"}';
            echo $result;
        }
    }
}
?>
