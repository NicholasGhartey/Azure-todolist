from application import app, db
from application.models import Tasks



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/create/task')
def add():
    new_task = Tasks(description="New Task")
    db.session.add(new_task)
    db.session.commit()
    return f"Task with id {new_task.id} added to database"


@app.route('/read/allTasks')
def read_tasks():
    all_tasks = Tasks.query.all()
    
    tasks_dict = {"tasks": []}

    for task in all_tasks:
        tasks_dict["tasks"].append({"description": task.description, "completed": task.completed})

    return tasks_dict


@app.route('/update/task/<int:id>/<new_description>')
def update(id, new_description):
    task = Tasks.query.get(id)
    task.description = (new_description)
    db.session.commit()
    return f"Task {id} updated to {new_description}"

    

@app.route('/delete/task/<int:id>')
def delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} removed"

 
 
@app.route('/completed/task/<int:id>')
def completed(id):
    task = Tasks.query.get(id) 
    task.completed = True 
    db.session.commit() 
    return f"Task {id} completed!"




@app.route('/incomplete/task/<int:id>')
def incomplete(id):
    task = Tasks.query.get(id) 
    task.completed = False 
    db.session.commit() 
    return f"Task {id} incomplete!"



