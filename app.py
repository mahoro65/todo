from flask import Flask,render_template,request,redirect,url_for



#app instance from the flask class
app = Flask(__name__,template_folder='templates')


# storing a particular value into a variable.
tasks = [] #variable is task that will store

@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)

#teplta fo
@app.route('/add',methods=['post','Get'])
def create_new_task():
    task = request.form.get('task') #we pass in the on in the template 'index'
    tasks.append(task)#adds the variable to the list 
    return redirect(url_for('home'))#redirecting to the home page


@app.route('/delete/<int:index>')#instance to help us delete the particular index
def delete_task(index):#using the parameter index for indexing
    if 0 <= index <len(tasks):#checking if the valid range of indice for the task list and also less than the length of our task variable
        del tasks[index]
        return redirect(url_for('home'))#redirecting to the home page

    

if __name__== '__main__':
    app.run(debug=True)
    
