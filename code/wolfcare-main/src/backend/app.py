#from werkzeug.exceptions import HTTPException
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from src.backend.utils import *

# Flask application configuration
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def empty():
    """
    Empty function which sends a json when we start the application.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    return jsonify({"status": 200, "data": {}, "message": "Backend working"})

@app.route('/addDoctor', methods=['POST'])
def app_addDoctor():
    """
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Information about the Doctor getting added.
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        firstname = data['firstname']
        lastname = data['lastname']
        primaryspecialty = data['primaryspecialty']
        secondaryspecialty = data['secondaryspecialty']
        type = data['type']
        degree = data['degree']
        phone = data['phone']
        email = data['email']
        gender = data['gender']
        yoe = data['yoe']
        approvalstatus = data['approvalstatus'] 
        isactive = data['isactive']
        userid = data['userid']
        status, msg = addDoctor(firstname, lastname, primaryspecialty, secondaryspecialty,
                                type, degree, phone, email, gender, yoe, approvalstatus, isactive, userid)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/updateDoctor', methods=['PUT'])
def app_updateDoctor():
    """
    Updating doctor info already exisiting.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Updated doctor info 
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'PUT':
        data = json.loads(request.data)

        status, msg = updateDoctorInfo(data)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})

@app.route('/getDoctorInfo', methods=['GET'])
def app_getDoctorInfo():
    """
    Gets information of the doctor based on the id.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    id : int
        ID doctor id.
    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information, message in accordance with the status.
    """

    if request.method == 'GET':

        id = request.args.get('id')
        status, data = getDoctorDetails(id)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Records found"})
        else:
            return jsonify({"status": 400, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/addHospital', methods=['POST'])
def app_addHospital():
    """
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Information about the Hospital getting added.
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        type = data['type']
        addressline1 = data['addressline1']
        addressline2 = data['addressline2']
        city = data['city']
        state = data['state']
        country = data['country']
        zipcode = data['zipcode']
        phone = data['phone']
        email = data['email']    
        approvalstatus = data['approvalstatus']
        isactive = data['isactive']
       
        status, msg = addHospital(name, type, addressline1, addressline2, city,
                                  state, country, zipcode, phone, email, approvalstatus, isactive)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/updateHospital', methods=['PUT'])
def app_updateHospital():
    """
    Updating Hospital info already exisiting.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Updated doctor info 
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'PUT':
        data = json.loads(request.data)

        status, msg = updateHospitalInfo(data)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/getHospitalInfo', methods=['GET'])
def app_getHospitalInfo():
    """
    Gets information of the hospital based on the id.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    id : int
        ID hospital id.
    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information, message in accordance with the status.
    """

    if request.method == 'GET':

        id = request.args.get('id')
        status, data = getHospitalDetails(id)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Records found"})
        else:
            return jsonify({"status": 400, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/addAffiliation', methods=['POST'])
def app_addAffiliation():
    """
    Affiliation is created between an existing doctor and hospital\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Information about the affiliation which is getting created.
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        doctorid = data['doctorid']
        hospitalid = data['hospitalid']
        appointmentschedule = data['appointmentschedule']
        status, msg = addAffiliation(doctorid, hospitalid, appointmentschedule)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/addAppointment', methods=['POST'])
def app_addAppointment():
    """
    Appoitnment is created for a user with a doctor in a hospital on a particular date and timeslot\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Information about the appointment which is getting created.
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        userid = data['userid']
        doctorid = data['doctorid']
        hospitalid = data['hospitalid']
        date = data['date']
        timeslot = data['timeslot']
        status, msg = addAppointment(
            userid, doctorid, hospitalid, date, timeslot)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/updateAppointment', methods=['PUT'])
def app_updateAppointment():
    """
    Updating Appointment info already exisiting.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Updated appointment info 
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'PUT':
        data = json.loads(request.data)

        status, msg = updateAppointmentInfo(data)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})

#updateAffiliation(data)


@app.route('/updateAffiliation', methods=['PUT'])
def app_updateAffiliation():
    """
    Updating an affiliation already exisiting.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    data : json
        Updated appointment schedule or isactive status
    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'PUT':
        data = json.loads(request.data)

        status, msg = updateAffiliation(data)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/getAfiiliationByDoctor', methods=['GET'])
def app_getAfiiliationByDoctor():
    """
    Gets information for all the hospitals affiliated to a doctor.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    id : int
        ID doctor id.
    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information, message in accordance with the status.
    """

    if request.method == 'GET':

        id = request.args.get('id')
        status, data = getAfiiliationByDoctor(id)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Records found"})
        else:
            return jsonify({"status": 200, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/getAfiiliationByHospital', methods=['GET'])
def app_getAfiiliationByHospital():
    """
    Gets information for all the doctors affiliated to a hospital.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    id : int
        ID hospital id.
    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information, message in accordance with the status.
    """

    if request.method == 'GET':

        id = request.args.get('id')
        status, data = getAfiiliationByHospital(id)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Records found"})
        else:
            return jsonify({"status": 200, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})

#getDoctorSearch


@app.route('/getDoctorSearch', methods=['GET'])
def app_getDoctorSearch():
    """
    Gives back all doctors that match keyword as firstname, lastname, primaryspecialty or secondaryspecialty.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    id : int
        Keyword to search doctor.
    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information, message in accordance with the status.
    """

    if request.method == 'GET':

        keyword = request.args.get('keyword')
        status, data = getDoctorSearch(keyword)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Records found"})
        else:
            return jsonify({"status": 200, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})

#getHospitalSearch


@app.route('/getHospitalSearch', methods=['GET'])
def app_getHospitalSearch():
    """
    Gives back all hospitals that match keyword as name or address.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.
    Parameters
    ----------
    id : int
        Keyword to search hospital.
    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information, message in accordance with the status.
    """

    if request.method == 'GET':

        keyword = request.args.get('keyword')
        status, data = getHospitalSearch(keyword)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Records found"})
        else:
            return jsonify({"status": 200, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)
