from flask import Flask, render_template, request

from app.database import query_db
from app.plot import plot_wells

well_app = Flask(__name__) 


@well_app.route('/')
def root():
    return render_template('index.html')

@well_app.route('/plot')
def plot():
    depth = request.args.get('depth_min', 500)
    gradient = request.args.get('grad_min', 0.05)
    
    data = query_db(depth, gradient)
    chart = plot_wells(data)
    
    return render_template('plot.html', chart=chart)


if __name__ == '__main__':
    well_app.run(port=8123, debug=True)
    