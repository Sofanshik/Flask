from flask import Flask, render_template, request, abort

from file_py.IntSorted import q_sort
from file_py.Sortedmy import sorte_my

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def first_index():
    #if request.method == "POST":
        #print("!" * 100)
        #print(request.form)
        #print("!" * 100)
        #user_data = request.form
        #numbers = user_data['numbers']
        #la = []
        #for num in numbers.split(','):
            #a = int(num)
            #la.append(a)
        #result = sorte_my(la)
        #return render_template('tests.html', result=result)
    return render_template('tests.html')


@app.route('/Choose.html')
def second_index():
    return render_template('Choose.html')

@app.route('/SS.html', methods=['GET', 'POST'])
def third_index():
    if request.method == "POST":
        print("!" * 100)
        print(request.form)
        print("!" * 100)
        user_data = request.form
        numbers = user_data['numbers']
        la = []
        for num in numbers.split(','):
            a = int(num)
            la.append(a)
        result = sorte_my(la)
        return render_template('SS.html', result=result)
    return render_template('SS.html')

@app.route('/IntS.html', methods=['GET', 'POST'])
def fours_index():
    if request.method == "POST":
        print("!" * 100)
        print(request.form)
        print("!" * 100)
        user_data = request.form
        numbers = user_data['numbers']
        la = []
        for num in numbers.split(','):
            a = int(num)
            la.append(a)
        result = sorte_my(la)
        return render_template('IntS.html', result=result)
    return render_template('IntS.html')

@app.route('/MyS.html', methods=['GET', 'POST'])
def fifth_index():
    if request.method == "POST":
        print("!" * 100)
        print(request.form)
        print("!" * 100)
        user_data = request.form
        numbers = user_data['numbers']
        la = []
        for num in numbers.split(','):
            a = int(num)
            la.append(a)
        result = sorte_my(la)
        return render_template('/MyS.html', result=result)
    return render_template('/MyS.html')

@app.route('/user/<name>')
@app.route('/user/')

def user(name=None):
    if name is None:
        name = request.args.get('name')

    if name:
        return render_template('tests.html', name=name)

    else:
        abort(404)
if __name__ == '__main__':
    app.run(debug=True)
