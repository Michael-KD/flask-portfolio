function AlertIt(noteId) {
    //let noteId = $('#my-data').data();
    console.log(noteId);
    var answer = confirm ("Please click on OK to delete your note.")
    if (answer)
    window.location=`/delete/${noteId}`;
}