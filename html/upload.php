<?php
/*
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true');
header("Content-Type: application/json;charset=utf-8");
*/

$error = " ";
$ret = 0;

if(isset($_POST["attr"])){
    $attr = $_POST["attr"];
    $attr_file = fopen('/var/www/html/tmp_key_attr/key_attr.txt', "w") or mkdir('/var/www/html/error');
    fwrite($attr_file, $attr);
    fclose($attr_file);
}

else{
    $ret = 1;
    $error = "attr error";
}

$fp = $_FILES['uploadfile'];
if ($fp["error"] > 0){
    $ret = $fp["error"];
} 

else {

    	$tmp_name = $fp["tmp_name"];
    	$file_array = explode('.', $fp['name']);
    	$path_name = $file_array[0];
        $attr_name = $file_array[1];
    	if(is_uploaded_file($tmp_name)){
            $file_path_tmp = '/var/www/html/resources/'.$path_name;
            $file_path1 = $file_path_tmp;
            $num = 0;

            while(is_dir($file_path1)){
                $num = $num + 1;
                $file_path1 = $file_path_tmp.(string)$num;
            }

            mkdir($file_path1);
            $key = '';
            $res = 0;
            $file_path = $file_path1.'/cfile';
            $fp = fopen($file_path);
            fclose($fp);

            $attr_path = $file_path1.'/back';
            $ap = fopen($attr_path, 'w');
            fwrite($ap, $attr_name);
            fclose($ap);
            exec('/usr/bin/python encrypt.py '.$tmp_name.' '.$file_path, $key, $res);
            exec('cp /var/www/html/tmp_key_attr/key_attr.txt '.$file_path1.'/attr');
            if($res != 0){
                $ret =  1;
                $error = "unable to preservation";
            }
        }
}

if($ret == 0){
    echo "<script>alert('Upload success!')</script>";
}
else {
    echo "<script>alert('Error: ".$error."')</script>";
}
header("Location: index.html");
?>
