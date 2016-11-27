$(document).ready(function() {
    var drop = $('.files');

    drop[0].ondragover = function () {
        drop.addClass('active');

        return false;
    };

    drop[0].ondragleave = function () {
        drop.removeClass('active');

        return false;
    };

    drop[0].ondrop = function (event) {
        event.preventDefault();

        // Design
        drop.removeClass('active');
        drop.addClass('progress');

        // Get file
        var file = event.dataTransfer.files[0];
        var formData = new FormData()
        formData.append('file', file)

        // Make request
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload');
        xhr.onreadystatechange = stateChange;
        xhr.setRequestHeader('X-FILE-NAME', file.name);
        xhr.send(formData)
    };

    function stateChange(event) {
        if (event.target.readyState == 4) {
            drop.removeClass('progress');

            if (event.target.status == 200) {
                drop.addClass('success');
                drop.find('span').html('<i class="fa fa-icons fa-check-circle"></i>')
            } else {
                drop.addClass('failed');
                drop.find('span').html('<i class="fa fa-icons fa-times-circle"></i>')
            }
        }
    }
});