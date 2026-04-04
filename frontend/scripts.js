```javascript
document.addEventListener('DOMContentLoaded', function() {
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    addTaskBtn.addEventListener('click', function() {
        const title = prompt('Enter task title:');
        const description = prompt('Enter task description:');

        if (title && description) {
            fetch('http://localhost:5000/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title, description: description })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(task => {
                const taskItem = document.createElement('div');
                taskItem.textContent = task.title;
                taskItem.classList.add('task'); // Add a class for styling
                taskItem.setAttribute('data-id', task.id); // Store the task ID
                taskList.appendChild(taskItem);
            })
            .catch(error => {
                console.error('Error creating task:', error);
                alert('Failed to create task. Check console for details.');
            });
        }
    });

    // Fetch tasks from the API
    fetch('http://localhost:5000/tasks')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(tasks => {
            taskList.innerHTML = '';
            tasks.forEach(task => {
                const taskItem = document.createElement('div');
                taskItem.textContent = task.title;
                taskItem.classList.add('task'); // Add a class for styling
                taskItem.setAttribute('data-id', task.id); // Store the task ID
                taskList.appendChild(taskItem);
            });
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
            alert('Failed to fetch tasks. Check console for details.');
        });

    // Mark tasks as complete
    taskList.addEventListener('click', function(event) {
        if (event.target.classList.contains('task')) {
            const taskId = event.target.getAttribute('data-id');
            fetch(`http://localhost:5000/tasks/${taskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id: taskId, completed: !event.target.classList.contains('completed') })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(updatedTask => {
                event.target.classList.toggle('completed');
            })
            .catch(error => {
                console.error('Error updating task:', error);
                alert('Failed to update task. Check console for details.');
            });
        }
    });
});
```