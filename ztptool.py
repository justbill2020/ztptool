<!doctype html>
<html lang="en">
  <head>
    <script type="text/javascript" src="/eel.js"></script>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/icons.css">

        <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
          body {
  padding-top: 5rem;
}
.starter-template {
  padding-top: 1rem;
  padding-bottom: 1rem;
}
    </style>

    <title>ZTP Tool</title>
  </head>


<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">ZTP Tool Help</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>ZTP Tool v1.0.6-alpha</p>
        <p>Supports:<ul>
        <li>FortiManager 6.2.1</li>
        <li>FortiManager 6.2.2</li>
        <li>Future versions of FortiManager 6.2 should also work</li>
      </ul></p>
        <p>ZTP Tool is created by Tim Morris.</p>
        <p>Please report any issues at <a href="https://github.com/tmorris-ftnt/ztptool/issues">https://github.com/tmorris-ftnt/ztptool/issues</a>.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>


  <body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
  <a class="navbar-brand" href="#">ZTP Tool</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarsExampleDefault">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="ztptool.html">Import Devices <span class="sr-only">(current)</span></a>
      </li>
            <li class="nav-item active">
        <a class="nav-link" href="#" onclick="eel.getsettings_adom()">Import ADOM<span class="sr-only">(current)</span></a>
      </li>

    </ul>
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
  Help
</button>
  </div>
</nav>

<main role="main" class="container">
<div id="mainpage">

</div>
</main><!-- /.container -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="js/jquery-3.4.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>

<script>
var dosya_path = "/";
async function getFolder() {
var dosya_path = await eel.btn_getxlsxfile()();
	if (dosya_path) {
		console.log(dosya_path);
        document.getElementById("filepath").innerHTML = dosya_path;
	}
}

var dosya_path = "/";
async function getFileADOM() {
var dosya_path = await eel.btn_getjsonfile()();
	if (dosya_path) {
		console.log(dosya_path);
        document.getElementById("filepath").innerHTML = dosya_path;
	}
}

function processxlsx(fp) {
  if (fp === "/") {
    alert("Please Select an xlsx file first.")
  } else {
    eel.btn_checkxlsx(fp,document.getElementById('fmgip').value,document.getElementById('fmgusername').value,document.getElementById('fmgpassword').value,document.getElementById('fmgadom').value)
  }
}

function processadom(fp) {
  if (fp === "/") {
    alert("Please Select an json file first.")
  } else {
    eel.btn_checkadom(fp,document.getElementById('fmgip').value,document.getElementById('fmgusername').value,document.getElementById('fmgpassword').value,document.getElementById('fmgadom').value,document.getElementById('fmgadomdesc').value)
  }
}


eel.expose(pageupdate);
function pageupdate(msg) {
  document.getElementById("mainpage").innerHTML = msg;
}



$( document ).ready(function() {
    eel.getsettings_devices()
});

</script>

</html>
