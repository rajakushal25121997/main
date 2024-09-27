document.getElementById("upload-pdf-btn").addEventListener("click", async function() {
    let fileInput = document.getElementById("file");
    let formData = new FormData();
    
    if (fileInput.files.length > 0) {
        formData.append("file", fileInput.files[0]);
        document.getElementById("upload-pdf-btn").innerHTML='Matching Data....'
        try {
            const response = await fetch("/upload-pdf/", {
                method: "POST",
                body: formData
            });

            if (response.ok) {
                let output=''
                const data = await response.json();
                document.getElementById("response-output").innerHTML = `${data.profiles}`;
                for(let i=0; i<data.profiles.length;i++){
                    job_profile=data.profiles[i]['Job Title']
                    job_skills=data.profiles[i]['Skill Set Required']
                    job_experience=data.profiles[i]['Total Experience Required']
                    job_location=data.profiles[i]['Location']
                    output +=   "<div class='card'>"+
                                    "<div class='container'>"+
                                    "<h4><b>Job Profile : "+job_profile+"</b></h4>"+
                                    "<p>Experience : "+job_experience+"</p>"+
                                    "<p>Location : "+job_location+"</p>"+
                                    "<p>Skills : "+job_skills+"</p>"+
                                    "</div>"+
                                "</div>"
                }
                document.getElementById("response-output").innerHTML = output;
                document.getElementById("upload-pdf-btn").innerHTML='Match Data'
                output=''
                
            } else {
                document.getElementById("response-output").innerHTML = "Error uploading PDF";
            }
        } catch (error) {
            console.error("Error:", error);
            document.getElementById("upload-pdf-btn").innerHTML='Match Data'
            document.getElementById("response-output").innerHTML = "An error occurred";
        }
    } else {
        document.getElementById("load-urls-btn").innerHTML='Match Data'
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
    document.getElementById("load-urls-btn").innerHTML='Data Loading.....'
    try {
        const response = await fetch("/load-urls/", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById("response-output").innerHTML = `URLs Loaded: ${data.status}`;
            document.getElementById('pdf-upload-form').style.display='block';
            document.getElementById("load-urls-btn").innerHTML='Load Data'
        } else {
            document.getElementById("response-output").innerHTML = "Error loading URLs";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("load-urls-btn").innerHTML='Load Data'
        document.getElementById("response-output").innerHTML = "An error occurred";
    }
});
