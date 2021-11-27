<style>
  #btn1{
          border-top-left-radius: 5px;
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
          color: #454545;
          border: 3px solid #454545;
          padding: 5px;
  }
  #hr{
          height: 2px;
          background: #bbb;
          background-image: -webkit-linear-gradient(left, #eee, #777, #eee);
          background-image: -moz-linear-gradient(left, #eee, #777, #eee);
          background-image: -ms-linear-gradient(left, #eee, #777, #eee);
          background-image: -o-linear-gradient(left, #eee, #777, #eee);
  }
</style>

<!--<div style="text-align: center; position: absolute; top:300px; left: 40%;" > -->

<form name="uploadForm" id="uploadForm" method="post" action="/upload_process.php"

enctype="multipart/form-data" onsubmit="return formSubmit(this);">

<div>
  <img src="/bannerimage/twitter_header_photo_2.png" style="width: 100%; height: auto;" alt="logo">
  <div style="text-align: center; position: absolute; top: 540px; left: 39%;" >
    <label for="upfile" style="font-size: 30px; color: #454545; font-style: italic;"> <strong>동영상을 업로드해주세요.</strong>
  </label>
  </p>
  </p>
  <hr style="border: solid 2px grey;">
  </p>
  </p>
  <input id="btn1" style="left: 40%;" type="file" name="upfile" id="upfile" color="blue" />
  </p>
  <input id="btn2"  type="submit" value="upload" />
</div>

</form>
</div>