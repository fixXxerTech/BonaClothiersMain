// This is a javasript function to preview image upload before form submition
// ---------------------------------------------------------------------------

document.getElementById("StyleImage").addEventListener("change", readFile, false);

function readFile() {
  if (this.files && this.files[0]) {
    var FR= new FileReader();
    FR.onload = function(e) {
      document.getElementById("StyleImagePreview").src = e.target.result;
      document.getElementById("StyleImagePreview").style.width = "200px";

    };
    FR.readAsDataURL( this.files[0] );
  }
}