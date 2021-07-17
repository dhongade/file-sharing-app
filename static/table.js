function slugify(name) {
    if (!name) {
        return "";
    }
    return name.replace(' ', '-').replace('*', '-');
}


const dropZone = document.querySelector(".drop-zone");
const browsbtn = document.querySelector(".browsbtn");
const fileInput = document.querySelector("#fileInput");


// dropzone event
dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();

    if (!dropZone.classList.contains("dragged")) {
        dropZone.classList.add("dragged");
    }
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragged");
})

dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragged");
    const files = e.dataTransfer.files;
    console.table(files);

    if (files.length) {
        fileInput.files = files;

    }
});

// browsbtn click event
browsbtn.addEventListener("click", () => {
    fileInput.click();
})

//share btn click event
$('.btn-share-file').on('click', function () {
    const $this = $(this);

    $('#shareModal').modal();

    const fileId = $this.attr("data-file-id");
    const fileName = $this.attr('data-file-name');
    const fileNameSlugified = fileName;

    const permalink = 'http://localhost:5000' + '/download/' + fileId + '/' + fileNameSlugified;

    $('#shareModal .share-link').html(permalink);
});


//**************copy tp clipboard******************* */
function copytoclipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
}
//********************/******************************** */ */

//***************delete btn***************** */

$('.delete').on('click', function () {
    const $this = $(this);

    const fileId = $this.attr("data-file-id");
    window.location.href = "/table/" + fileId;
});
