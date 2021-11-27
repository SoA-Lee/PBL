<div style="text-align: center; color: #6495ED; position: absolute; top:150px; left: 36%" >
<img src="./images/koren_image.jfif" alt="My Image" style="width: 50%; height: auto;">
<h1>FILE List</h1>
<hr style="border: solid 2px grey;">
</div>

<table style="margin-left: auto; margin-right: auto; margin-top: 330px" width= "60%" height= "100px" border= "1"  cellpadding="10px" style= "text-align : center; border-collapse: collapse; ">
<tr>

        <th bgcolor="#6495ED">파일 아이디</th>

        <th bgcolor="#6495ED">원래 파일명</th>

        <th bgcolor="#6495ED">저장된 파일명</th>

</tr>

<?php

$db_conn = mysqli_connect("116.89.189.14", "root", "rootpass", "cloudbread");

$query = "SELECT file_id, name_orig, name_save FROM upload_file ORDER BY reg_time DESC";

$stmt = mysqli_prepare($db_conn, $query);

$exec = mysqli_stmt_execute($stmt);

$result = mysqli_stmt_get_result($stmt);

while($row = mysqli_fetch_assoc($result)) {

?>

<tr>

  <td><?= $row['file_id'] ?></td>

  <td><a href="download.php?file_id=<?= $row['file_id'] ?>" target="_blank"><?= $row['name_orig'] ?></a></td>

  <td><?= $row['name_save'] ?></td>

</tr>

<?php

}



mysqli_free_result($result);

mysqli_stmt_close($stmt);

mysqli_close($db_conn);

?>

</table>