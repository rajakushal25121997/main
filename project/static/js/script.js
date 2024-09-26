document.getElementById("upload-pdf-btn").addEventListener("click", async function() {
    let fileInput = document.getElementById("file");
    let formData = new FormData();

    if (fileInput.files.length > 0) {
        formData.append("file", fileInput.files[0]);

        try {
            const response = await fetch("/upload-pdf/", {
                method: "POST",
                body: formData
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById("response-output").innerHTML = `PDF Uploaded: ${data.filename}`;
            } else {
                document.getElementById("response-output").innerHTML = "Error uploading PDF";
            }
        } catch (error) {
            console.error("Error:", error);
            document.getElementById("response-output").innerHTML = "An error occurred";
        }
    } else {
        document.getElementById("response-output").innerHTML = "Please select a file.";
    }
});

document.getElementById("load-urls-btn").addEventListener("click", async function() {
    let urlInput = document.getElementById("urls").value;

    if (urlInput.trim() === "") {
        document.getElementById("response-output").innerHTML = "Please enter URLs.";
        return;
    }

    let formData = new FormData();
    formData.append("urls", urlInput);

    try {
        const response = await fetch("/load-urls/", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById("response-output").innerHTML = `URLs Loaded: ${data.urls.join(", ")}`;
        } else {
            document.getElementById("response-output").innerHTML = "Error loading URLs";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("response-output").innerHTML = "An error occurred";
    }
});
