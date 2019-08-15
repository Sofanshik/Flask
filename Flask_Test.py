from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def first_index():
    return render_template('tests.html')

@app.route('/Choose.html')
def second_index():
    return render_template('Choose.html')

@app.route('/SS.html')
def third_index():
    return render_template('SS.html')

@app.route('/IntS.html')
def fours_index():
    return render_template('IntS.html')

@app.route('/MyS.html')
def fifth_index():
    return render_template('MyS.html')

@app.route('/IntSorted.py')
def sorte():
    return render_template('IntSorted.py')

@app.route('/Sorted.py')
def sor():
    return render_template('Sorted.py')

@app.route('/Sortedmy.py')
def sote():
    return render_template('Sortedmy.py')


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
