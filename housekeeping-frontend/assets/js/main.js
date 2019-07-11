function addAsset(event) {
    event.preventDefault();
    var assetName = $('#assetName').val();
    console.log(assetName);
    var data = {
        assetName
    }
    $.post("http://127.0.0.1:8000/add-asset/", data, function(data, status){
        alert("Data: " + data + "\nStatus: " + status);        
    });
    setTimeout(function(){ getAssets(); }, 1000);
    return false;
}

function addWorker(event) {
    event.preventDefault();
    var workerName = $('#workerName').val();
    console.log(workerName);
    var data = {
        workerName
    }
    $.post("http://127.0.0.1:8000/add-worker/", data, function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
    return false;
}

function addTask(event) {
    event.preventDefault();
    var taskName = $('#taskName').val();
    var frequency = $('#taskFrequency').val();
    
    var data = {
        taskName,
        frequency
    }

    $.post("http://127.0.0.1:8000/add-task/", data, function(data,status) {
        console.log(data);
    })

    return false;
}

function getAssets() {
    $.get("http://127.0.0.1:8000/assets/all/", function(data, status){
        // alert("Data: " + data + "\nStatus: " + status);
        console.log(data)
        var assets = "<ul>";
        for(var i in data.assets) {
            assets += `
                <li class="assetName">
                    `+ data.assets[i].asset_name +`
                </li>
            `
        }
        assets += "</ul>";
        $('#assets').html(assets)
    });
}

function populateAllocateTask() {

    var assets, workers, tasks;
    // Could've cached this but short on time
    $.get("http://127.0.0.1:8000/assets/all/", function(data, status){
       
        assets = data.assets;
        
        $.get("http://127.0.0.1:8000/workers/all/", function(data, status){
            workers = data.workers;
        });
        
        $.get("http://127.0.0.1:8000/tasks/all/", function(data, status){

            tasks = data.tasks;
            console.log(assets,workers,tasks)

            var assetHtml = "<select class='selectClass' id='allocateAsset'>";
            for(var i in assets) {
                assetHtml += "<option value='" + assets[i].id + "'> " + assets[i].asset_name + " </option>"
            }
            assetHtml += "</select>";
            $('#selectAssets').html(assetHtml);

            var workerHtml = "<select class='selectClass' id='allocateWorker'>";
            for(var i in workers) {
                workerHtml += "<option value='" + workers[i].id + "'> " + workers[i].worker_name + " </option>"
            }
            workerHtml += "</select>";
            $('#selectWorkers').html(workerHtml);
            
            var taskHtml = "<select class='selectClass' id='allocateTask'>";
            for(var i in tasks) {
                taskHtml += "<option value='" + tasks[i].id + "'> " + tasks[i].task_name + " </option>"
            }
            taskHtml += "</select>";
            $('#selectTasks').html(taskHtml);

        });
    });
}

function populateWorkers() {
    $.get("http://127.0.0.1:8000/workers/all/", function(data, status){
        workers = data.workers;

        var workerHtml = "<select class='selectClass' id='workerSelect'>";
        for(var i in workers) {
            workerHtml += "<option value='" + workers[i].id + "'> " + workers[i].worker_name + " </option>"
        }
        workerHtml += "</select>";
        $('#workerSelect12').html(workerHtml);

    });
}

function getWorkerTasks(event) {
    event.preventDefault();
    var workerSelect = $('#workerSelect').val();
    $.get('http://127.0.0.1:8000/get-tasks-for-worker/' + workerSelect + '/', function(data,status) {
        var allocatedTasks = data.allocatedTasks;
        taskHtml = "<div>";
        for(var i in allocatedTasks) {
            taskHtml += `
                taskId: `+ allocatedTasks[i].task +`<br>
                workerId: `+ allocatedTasks[i].worker +`<br>
                assetId: `+ allocatedTasks[i].asset +`<br>
                Task to be performed by: `+allocatedTasks[i].task_to_be_performed_by +`<br><br>
            `
        }
        taskHtml += "</div>";
        console.log(taskHtml)
        $('#allocatedTasks_').html(taskHtml);
    } )
    return false;
}

function allocateTask_(event) {
    console.log("asdasd");
    event.preventDefault();

    var assetId = $('#allocateAsset').val();
    var workerId = $('#allocateWorker').val();
    var taskId = $('#allocateTask').val();
    var taskToBePerformedBy = $('#taskToBePerformedBy').val();

    var data = {
        assetId,
        workerId,
        taskId,
        taskToBePerformedBy
    }

    console.log(data);
    $.post("http://127.0.0.1:8000/allocate-task/", data, function(data,status) {
        alert(status);
    })
    return false;
}

$( document ).ready(function() {
    getAssets();
    populateAllocateTask();
    populateWorkers();
});
