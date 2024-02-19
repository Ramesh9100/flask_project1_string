from flask import Flask

FAI=Flask(__name__)
@FAI.route('/stringResponse')
def stringResponse():
    return 'Hai This is First View Of Flask Project'


@FAI.route('/secondString')
def secondString():
    return 'Hai This is Second View Of Flask Project'

if __name__=='__main__':
    FAI.run(debug=True)
