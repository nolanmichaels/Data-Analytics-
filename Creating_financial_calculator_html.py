from flask import Flask,request

from Final_Project_HTML import calc_splashHTML, calc1HTML, calc1resultHTML, calc2HTML, calc2resultHTML, calc3HTML, calc3resultHTML, calcErrorHTML1, calcErrorHTML2,calcErrorHTML3

from Final_Project_HTML import homeHTML

app = Flask(__name__)

def try_float(num):

    """
    Checks whether a value can be converted into a float. If a Value Error is thrown
    returns false. If no error is thrown, retruns true.
    """
    try:
         float(num)
    except ValueError:
        return False
    else:
        return True


@app.route('/')
def homepage():
    return homeHTML

@app.route('/calc_home')
def calculator_landing_page():
    return calc_splashHTML

@app.route('/calc1')
def calc1():
    return calc1HTML

@app.route('/calc1result')
def calc1result():
    # references HTML input forms from calc1HTML and stores text values as strings
    FV = request.args.get('FV')
    ROR = request.args.get('ROR')
    NOP = request.args.get('NOP')
    
    # input validation to check if field values follow required conditions
    # assigns float value to field variables and calculates present value based on user inputs and stores 
    ## in PV variable 
    if try_float(FV)==True and try_float(ROR)==True and try_float(NOP)==True:
        FV = float(request.args.get('FV'))
        ROR = float(request.args.get('ROR'))
        NOP = float(request.args.get('NOP'))
        PV = FV*(1/(1+ROR)**NOP)
        
        #returns calc1resultHTML page and fills fields with variables calculated above
        return calc1resultHTML.format(FV_field=FV,ROR_field=ROR,NOP_field=NOP, PV_field=PV)
    else:
        return calcErrorHTML1

@app.route('/calc2')
def calc2():
    return calc2HTML

@app.route('/calc2result')
def calc2result():
    # references HTML input forms from calc2HTML and stores text values as strings
    IA = request.args.get('IA')
    NOY = request.args.get('NOY')
    IR = request.args.get('IR')

    # input validation to check if field values follow required conditions
    # assigns float value to field variables and calculates present value based on user inputs
    if try_float(IA)==True and try_float(NOY)==True and try_float(IR)==True:
        IA = float(request.args.get('IA'))
        NOY = float(request.args.get('NOY'))
        IR = float(request.args.get('IR'))
        FV = IA * (1+(IR*NOY))
         
        #returns calc1resultHTML page and fills fields with variables calculated above
        return calc2resultHTML.format(IA_field=IA,NOY_field=NOY,IR_field=IR,FV_field=FV)
    
    else: 
        return calcErrorHTML2


@app.route('/calc3')
def calc3():
    return calc3HTML

@app.route('/calc3result')
def calc3result():
    # references HTML input forms  from calc3HMTL and stores text values as strings
    IAMT = request.args.get('IAMT')
    NY = request.args.get('NY')
    IRT = request.args.get('IRT')
    
    # input validation to check if field values follow required conditions
    # assigns float value to field variables and calculates present value based on user inputs
    if try_float(IAMT)==True and try_float(NY)==True and try_float(IRT)==True:
        IAMT = float(request.args.get('IAMT'))
        NY = float(request.args.get('NY'))
        IRT = float(request.args.get('IRT'))
        CI = IAMT * (1+IRT)**NY

         #returns calc1resultHTML page and fills fields with variables calculated above
        return calc3resultHTML.format(IAMT_field=IAMT,NY_field=NY,IRT_field=IRT,CI_field=CI)
    
    else: 
        return calcErrorHTML3

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)


