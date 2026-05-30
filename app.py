from flask import Flask , request , jsonify
from models.task import Task

#__name__ = '__main__'  
app = Flask(__name__)

#CRUD 
# Create, read, Update and Delete #
tasks = []
task_id_control = 1  
total_tasks = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description',''))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    global total_tasks
    tasks_list = [tasks.to_dict() for tasks in tasks]
    output ={
        "tasks": tasks_list,
        "total_tasks": len(tasks_list) 
    }
    return jsonify (output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task=None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({'message': 'Não foi possível encontrar a atividade'}),404
    

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task=None
    for t in tasks:
        if t.id == id:
            task = t 
    
    print(task)
    
    if task == None:
        return jsonify({'message': 'Não foi possível encontrar a atividade'}),404    
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    print(task)

    return jsonify(task.to_dict(),{'message': 'tarefa atualiza com sucesso'})   


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
       if t.id == id:
           task = t
           tasks.remove(t)
           return jsonify(task.to_dict(),{'message': 'Tarefa deleta com sucesso'})   
    
    return jsonify({'message': 'Não foi possível encontrar a atividade'}),404


if __name__ == '__main__':
    app.run(debug=True)