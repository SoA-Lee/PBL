<!DOCTYPE html>
<html>

        <head>
<style>

        #btn1{
                border-bottom-left-radius: 5px;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                margin-right:-4px;
                padding:5px;
        }
        #btn2{
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                margin-left:-3px;
                color: #6495ED;
                border: 3px solid #6495ED;
                padding: 5px;
        }
        #hr{
                height: 1px;
                background: #bbb;
                background-image: -webkit-linear-gradient(left, #eee, #777, #eee);
                background-image: -moz-linear-gradient(left, #eee, #777, #eee);
                background-image: -ms-linear-gradient(left, #eee, #777, #eee);
                background-image: -o-linear-gradient(left, #eee, #777, #eee);
        }
</style>
        </head>
       <body>
        <div style="text-align: center; position: absolute; top:300px; left: 35%" >
        <img src="/bannerimage/twitter_header_photo_2.png" alt="My Image" style="width: 50%; height: auto;"> </p>
        <label for="upfile" style="font-size: 30px; color: #6495ED; font-style: italic||bold;" >업로드 결과
        </label>
        </p>
        </p>
        <hr style="border: solid 2px grey;">
        </p>
     
<?php 
$db_conn = mysqli_connect("10.1.3.5","root", "rootpass", "cloudbread");

if(isset($_FILES['upfile']) && $_FILES['upfile']['name'] != "") {

    $file = $_FILES['upfile'];

    $upload_directory = './';

    $ext_str = "hwp,xls,doc,xlsx,docx,pdf,jpg,gif,png,txt,ppt,pptx";

    $allowed_extensions = explode(',', $ext_str);



    $max_file_size = 5242880;

    $ext = substr($file['name'], strrpos($file['name'], '.') + 1);



    // 확장자 체크

    if(!in_array($ext, $allowed_extensions)) {

        echo "업로드할 수 없는 확장자 입니다.";

    }



    // 파일 크기 체크

    if($file['size'] >= $max_file_size) {

        echo "5MB 까지만 업로드 가능합니다.";

    }



    $path = md5(microtime()) . '.' . $ext;

    if(move_uploaded_file($file['tmp_name'], $upload_directory.$path)) {

        $query = "INSERT INTO upload_file (file_id, name_orig, name_save, reg_time) VALUES(?,?,?,now())";

        $file_id = md5(uniqid(rand(), true));

        $name_orig = $file['name'];

        $name_save = $path;



        $stmt = mysqli_prepare($db_conn, $query);

        $bind = mysqli_stmt_bind_param($stmt, "sss", $file_id, $name_orig, $name_save);

        $exec = mysqli_stmt_execute($stmt);



        mysqli_stmt_close($stmt);



        echo"<h3>파일 업로드 성공</h3>";

        echo '<a href="file_list.php">업로드 파일 목록</a>';



    }

} else {

    echo "<h3>파일이 업로드 되지 않았습니다.</h3>";

    echo '<a href="javascript:history.go(-1);">이전 페이지</a>';

}



mysqli_close($db_conn);

?>

        </div>
</div>

        </body>

</html>