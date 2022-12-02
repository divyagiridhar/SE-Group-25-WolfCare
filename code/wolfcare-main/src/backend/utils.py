import mysql.connector
from src.backend.dbconfig import constants
import datetime

try:
    connection = mysql.connector.connect(
        host=constants["host"], user=constants["user"], password=constants["password"], database=constants["database"])
except:
    pass

def addDoctor(firstname, lastname, primaryspecialty, secondaryspecialty, type, degree, phone, email, gender, yoe, approvalstatus, isactive, userid):
    """
    Inserts doctor info into the database.

    Parameters
    ----------
    firstname : string
        First name of the doctor.
    lastname : string
        Last name of the doctor.
    primaryspecialty : string
        Primary specialty of the doctor. For eg. Dermatology, Neurology etc.
    secondaryspecialty : string
        Secondary specialty of the doctor, other than primaryspecialty. This can be NULL. For eg. Dermatology, Neurology etc.
    type : string
        Type of the doctor. For eg. Prescriber, Non Prescriber.
    degree : int
        Degree owned by the doctor. For eg. MBBS, MD etc.
    phone : string
        Contact number of the doctor. 
    email : string
        Email id of the doctor. 
    gender : string
        Gender of the doctor. For eg. Male, Female etc.
    yoe : string
        Years of experience of the doctor.
    approvalstatus : string
        Whether the doctor is approved by the admin. At time of registeration it will be False.
    isactive : string
        Whether the doctor is currently working or not. 
    userid : int
        ID of the doctor (Doctor also an user)


    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        cursor = connection.cursor(dictionary=True)
        mysql_insert_query = """INSERT INTO doctors (firstname, lastname, primaryspecialty, secondaryspecialty, type, degree, phone, email, gender, yoe, approvalstatus, isactive, lastmoddate, userid)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        record = (firstname, lastname, primaryspecialty, secondaryspecialty, type, degree,
                  phone, email, gender, yoe, approvalstatus, isactive, lastmoddate, int(userid))
        cursor.execute(mysql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into doctors table")
        msg = "Record inserted successfully into doctors table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to insert into doctors table {}".format(error))
        msg = "Failed to insert into doctors table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in addDoctor: {}".format(e))
        msg = "Failed to insert into doctors table {}".format(e)
        return False, msg


def updateDoctorInfo(data):
    """
    Updates doctor information in the database.
    
    Parameters
    ----------
    data : json
        Updated Doctor information.
        
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """
    
    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        cursor = connection.cursor(dictionary=True)
        mysql_update_query = """UPDATE doctors set firstname = %s, lastname = %s, primaryspecialty = %s, secondaryspecialty = %s, type = %s, degree = %s, phone = %s, email = %s, gender = %s, yoe = %s, approvalstatus = %s, isactive = %s, lastmoddate = %s WHERE doctorid = %s """

        input_data = (str(data['firstname']), str(data['lastname']), str(data['primaryspecialty']), str(data['secondaryspecialty']), str(data['type']), str(data['degree']), str(data['phone']), str(data['email']), str(data['gender']), str(data['yoe']), str(data['approvalstatus']), str(data['isactive']), lastmoddate, int(data['doctorid']))
        
        cursor.execute(mysql_update_query, input_data)
        connection.commit()

        print("Record updated successfully into doctors table")
        msg = "Record updated successfully into doctors table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update table {}".format(error))
        msg = "Failed to update table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in updateDoctorInfo: {}".format(e))
        msg = "Failed to update table {}".format(e)
        return False, msg

    
def getDoctorDetails(doctorid):
    """
    Get details of the doctor with the given doctorid.

    Parameters
    ----------
    doctorid : int
        ID of the doctor.

    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is the list of info of doctor.
    """
    
    try:
        cursor = connection.cursor(dictionary=True)
        finalData = []
        cursor.execute(
            'SELECT doc.doctorid, doc.firstname, doc.lastname, doc.primaryspecialty, doc.secondaryspecialty, doc.type, doc.degree, doc.phone, doc.email, doc.gender, doc.yoe, doc.approvalstatus, doc.isactive, doc.lastmoddate, doc.userid FROM doctors doc WHERE doc.doctorid = %s', (int(doctorid),))
        
        data = cursor.fetchall()
        for record in data:
            finalData.append({"doctorid": record["doctorid"], "firstname": record["firstname"], "lastname": record["lastname"], "primaryspecialty": record["primaryspecialty"], "secondaryspecialty": record["secondaryspecialty"],  "type": record["type"], "degree": record["degree"], "phone": record["phone"], "email": record["email"], "gender": record["gender"], "yoe": record["yoe"], "approvalstatus": record["approvalstatus"], "isactive": record["isactive"], "lastmoddate": record["lastmoddate"], "userid":record["userid"]})
        cursor.close()
        return True, finalData
    except mysql.connector.Error as error:
        print("Failed to get data {}".format(error))
        msg = "Failed to get data {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getDoctorInfo: {}".format(e))
        msg = "Failed to get data {}".format(e)
        return False, msg


def addHospital(name, type, addressline1, addressline2, city, state, country, zipcode, phone, email, approvalstatus, isactive):
    """
    Inserts doctor info into the database.

    Parameters
    ----------
    name : string
        Name of the hospital
    type : string
        Type of hospital
    addressline1 : string
        address of hospital
    addressline2 : string
        address of hospital
    city : string
        City of the hospital
    state : string
        State of the hospital
    country : string
        State of the hospital
    zipcode : string
        Zip code of the hospital
    phone : string
        Contact number of the hospital. 
    email : string
        Email id of the hospital. 
    approvalstatus : string
        Whether the hospital is approved by the admin. At time of registeration it will be False.
    isactive : string
        Whether the hospital is currently working or not. 


    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        cursor = connection.cursor(dictionary=True)
        mysql_insert_query = """INSERT INTO hospitals (name, type, addressline1, addressline2, city, state, country, zipcode, phone, email, approvalstatus, isactive, lastmoddate)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        record = (name, type, addressline1, addressline2, city, state, country,
                  zipcode, phone, email, approvalstatus, isactive, lastmoddate)
        cursor.execute(mysql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into hospitals table")
        msg = "Record inserted successfully into hospitals table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to insert into hospitals table {}".format(error))
        msg = "Failed to insert into hospitals table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in addHospital: {}".format(e))
        msg = "Failed to insert into hospitals table {}".format(e)
        return False, msg


def updateHospitalInfo(data):
    """
    Updates hospital information in the database.
    
    Parameters
    ----------
    data : json
        Updated Hospital information.
        
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        cursor = connection.cursor(dictionary=True)
        
        mysql_update_query = """UPDATE hospitals set name = %s, type = %s, addressline1 = %s, addressline2 = %s, city = %s, state = %s, country = %s, zipcode = %s, phone = %s, email = %s, approvalstatus = %s, isactive = %s, lastmoddate = %s  WHERE hospitalid = %s """

        input_data = (str(data['name']), str(data['type']), str(data['addressline1']), str(data['addressline2']), str(data['city']), str(data['state']), str(data['country']), str(data['zipcode']), str(data['phone']), str(data['email']), str(data['approvalstatus']), str(data['isactive']), lastmoddate, int(data['hospitalid']))

        cursor.execute(mysql_update_query, input_data)
        connection.commit()

        print("Record updated successfully into hospitals table")
        msg = "Record updated successfully into hospitals table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update table {}".format(error))
        msg = "Failed to update table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in updateHospitalInfo: {}".format(e))
        msg = "Failed to update table {}".format(e)
        return False, msg


def getHospitalDetails(hospitalid):
    """
    Get details of the hospital with the given hospitalid.
    
    Parameters
    ----------
    hospitalid : int
        ID of the hospital.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a list of info of hospital.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        finalData = []
        cursor.execute(
            'SELECT hosp.hospitalid, hosp.name, hosp.type, hosp.addressline1, hosp.addressline2, hosp.city, hosp.state, hosp.country, hosp.zipcode, hosp.phone, hosp.email, hosp.approvalstatus, hosp.isactive, hosp.lastmoddate FROM hospitals hosp where hosp.hospitalid = %s', (int(hospitalid),))
        data = cursor.fetchall()
        for record in data:
            finalData.append({"hospitalid": record["hospitalid"], "name": record["name"], "type": record["type"], "addressline1": record["addressline1"],
                              "addressline2": record["addressline2"], "city": record["city"], "state": record["state"], "country": record["country"], "zipcode": record["zipcode"], "phone": record["phone"], "email": record["email"], "approvalstatus": record["approvalstatus"], "isactive": record["isactive"], "lastmoddate": record["lastmoddate"]})
        cursor.close()
        return True, finalData
    except mysql.connector.Error as error:
        print("Failed to get data {}".format(error))
        msg = "Failed to get data {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getHospitalSearch: {}".format(e))
        msg = "Failed to get data {}".format(e)
        return False, msg


def getAfiiliationByDoctor(ID):
    """
    Gets all affiliated hospitals of a doctor given their ID. 
    Parameters
    ----------
    ID : int
        ID of an doctor.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a list of all data.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        finalData = []
        cursor.execute(
            'SELECT affil.affiliationid, affil.hospitalid, affil.appointmentschedule, hosp.name, hosp.type, hosp.addressline1, hosp.addressline2, hosp.city, hosp.state, hosp.country, hosp.zipcode, hosp.phone, hosp.email FROM affiliation affil inner join hospitals hosp on affil.hospitalid = hosp.hospitalid where affil.isactive = "TRUE" and hosp.approvalstatus = "TRUE" and affil.doctorid = %s', (int(ID),))
        data = cursor.fetchall()
        print(data)
        for record in data:
            finalData.append({"affiliationid": record["affiliationid"], "hospitalid": record["hospitalid"], "appointmentschedule": record["appointmentschedule"], "name": record["name"],
                              "addressline1": record["addressline1"], "addressline2": record["addressline2"], "city": record["city"], "state": record["state"],
                              "country": record["country"], "zipcode": record["zipcode"], "phone": record["phone"], "email": record["email"]})
        cursor.close()
        return True, finalData
    except mysql.connector.Error as error:
        print("Failed to get data {}".format(error))
        msg = "Failed to get data {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getAfiiliationByDoctor: {}".format(e))
        msg = "Failed to get data {}".format(e)
        return False, msg


def getAfiiliationByHospital(ID):
    """
    Gets all affiliated doctors of a hospital given their ID. 
    Parameters
    ----------
    ID : int
        ID of an hospital.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a list of all data.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        finalData = []
        cursor.execute(
            'SELECT affil.affiliationid, affil.doctorid, affil.appointmentschedule, doc.firstname, doc.lastname, doc.primaryspecality, doc.secondaryspecialty, doc.type, doc.degree, doc.phone, doc.email, doc.gender, doc.yoe FROM affiliation affil inner join doctors doc on affil.doctorid = doc.doctorid where affil.isactive = "TRUE" and doc.approvalstatus = "TRUE" and affil.hospitalid = %s', (int(ID),))
        data = cursor.fetchall()
        print(data)
        for record in data:
            finalData.append({"affiliationid": record["affiliationid"], "doctorid": record["doctorid"], "appointmentschedule": record["appointmentschedule"], "firstname": record["firstname"],
                              "lastname": record["lastname"], "primaryspecality": record["primaryspecality"], "secondaryspecialty": record["secondaryspecialty"], "type": record["type"],
                              "degree": record["degree"], "phone": record["phone"], "email": record["email"], "gender": record["gender"], "yoe": record["yoe"]})
        cursor.close()
        return True, finalData
    except mysql.connector.Error as error:
        print("Failed to get data {}".format(error))
        msg = "Failed to get data {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getAfiiliationByHospital: {}".format(e))
        msg = "Failed to get data {}".format(e)
        return False, msg


def addAffiliation(doctorid, hospitalid, appointmentschedule):
    """
    For future check if the doctorid and hospitalid are valid from the database
    Parameters
    ----------
    doctorid : string
        Id of the doctor.
    hospitalid : string
        Id of the hospital.
    appointmentschedule : string
        schedule sent as a json inside string
    Returns
    ----------
    bool
        Checks if the user got added to the database or not.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        isactive = "TRUE"
        print(doctorid, hospitalid, appointmentschedule, isactive, lastmoddate)
        cursor = connection.cursor(dictionary=True)
        sql_insert_query = "INSERT INTO affiliation (doctorid, hospitalid, appointmentschedule, isactive, lastmoddate) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql_insert_query, (doctorid, hospitalid,
                                          appointmentschedule, isactive, lastmoddate))
        connection.commit()
        cursor.close()
        return True, "bla bal"
    except mysql.connector.Error as error:
        print("some error occurred in addAffiliation: {}".format(error))
        print(error)
        return False,  str(error)
    except Exception as e:
        print("some error occurred in addAffiliation: {}".format(e))
        return False,  str(e)


def updateAffiliation(data):
    """
    Updates an affiliation in the database.
    Parameters
    ----------
    data : json
        Updated affilfiation information.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        cursor = connection.cursor(dictionary=True)
        mysql_update_query = """UPDATE affiliation set appointmentschedule = %s, isactive=%s, lastmoddate=%s WHERE affiliationid = %s """

        input_data = (str(data['appointmentschedule']), str(
            data['isactive']), lastmoddate, int(data['affiliationid']))
        cursor.execute(mysql_update_query, input_data)
        connection.commit()

        print("Record updated successfully into affiliation table")
        msg = "Record updated successfully into affiliation table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update table {}".format(error))
        msg = "Failed to update table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in updateAffiliation: {}".format(e))
        msg = "Failed to update table {}".format(e)
        return False, msg


def getDoctorSearch(keyword):
    """
    Searches for doctor by firstname, lastname, primaryspecialty, secondaryspecialty
    Parameters
    ----------
    keyword : string
        keyword for search.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a list of all data.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        finalData = []
        cursor.execute(
            'SELECT doc.doctorid, doc.firstname, doc.lastname, doc.primaryspecialty, doc.secondaryspecialty FROM doctors doc where doc.firstname = %s or doc.lastname = %s or doc.primaryspecialty = %s or doc.secondaryspecialty= %s', (str(keyword), str(keyword), str(keyword), str(keyword)))
        data = cursor.fetchall()
        for record in data:
            finalData.append({"doctorid": record["doctorid"], "firstname": record["firstname"], "lastname": record["lastname"],
                              "primaryspecialty": record["primaryspecialty"], "secondaryspecialty": record["secondaryspecialty"]})
        cursor.close()
        return True, finalData
    except mysql.connector.Error as error:
        print("Failed to get data {}".format(error))
        msg = "Failed to get data {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getDoctorSearch: {}".format(e))
        msg = "Failed to get data {}".format(e)
        return False, msg


def getHospitalSearch(keyword):
    """
    Searches for hospital by name, address
    Parameters
    ----------
    keyword : string
        keyword for search.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a list of all data.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        finalData = []
        cursor.execute(
            'SELECT hosp.hospitalid, hosp.name, hosp.addressline1, hosp.addressline2, hosp.city, hosp.state, hosp.zipcode FROM hospitals hosp where hosp.name = %s or hosp.addressline1 = %s or hosp.addressline2 = %s or hosp.city= %s or hosp.state = %s or hosp.zipcode= %s', (str(keyword), str(keyword), str(keyword), str(keyword), str(keyword), str(keyword)))
        data = cursor.fetchall()
        for record in data:
            finalData.append({"hospitalid": record["hospitalid"], "name": record["name"], "addressline1": record["addressline1"],
                              "addressline2": record["addressline2"], "city": record["city"], "state": record["state"]})
        cursor.close()
        return True, finalData
    except mysql.connector.Error as error:
        print("Failed to get data {}".format(error))
        msg = "Failed to get data {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getHospitalSearch: {}".format(e))
        msg = "Failed to get data {}".format(e)
        return False, msg


def addAppointment(userid, doctorid, hospitalid, date, timeslot):
    """
    For future check if the doctorid and hospitalid are valid from the database
    Parameters
    ----------
    userid : string
        Id of the doctor.
    doctorid : string
        Id of the doctor.
    hospitalid : string
        Id of the hospital.
    date : string
        appoitnment date
    timeslot : string
        appoitnment timeslot
    Returns
    ----------
    bool
        Checks if the appointment got added to the database or not.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        isactive = "TRUE"
        cursor = connection.cursor(dictionary=True)
        sql_insert_query = "INSERT INTO appointment (userid, doctorid, hospitalid, date, timeslot, isactive, lastmoddate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_insert_query, (userid, doctorid,
                                          hospitalid, date, timeslot, isactive, lastmoddate))
        connection.commit()
        cursor.close()
        return True, "Record added successsfully"
    except mysql.connector.Error as error:
        print("some error occurred in addAppointment: {}".format(error))
        print(error)
        return False, error
    except Exception as e:
        print("some error occurred in addAppointment: {}".format(e))
        return False, e


def updateAppointmentInfo(data):
    """
    Updates Appointment information in the database.
    
    Parameters
    ----------
    data : json
        Updated Appointment information.
        
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """

    try:
        lastmoddate = str(datetime.datetime.today()).split()[0]
        cursor = connection.cursor(dictionary=True)

        mysql_update_query = """UPDATE appointment set userid = %s, doctorid = %s, hospitalid = %s, date = %s, timeslot = %s, isactive = %s, lastmoddate = %s WHERE appointmentid = %s """

        input_data = (int(data['userid']), int(data['doctorid']), int(data['hospitalid']), str(data['date']), str(data['timeslot']), str(data['isactive']), lastmoddate, int(data['appointmentid']))

        cursor.execute(mysql_update_query, input_data)
        connection.commit()

        print("Record updated successfully into appointment table")
        msg = "Record updated successfully into appointment table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update table {}".format(error))
        msg = "Failed to update table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in updateHospitalInfo: {}".format(e))
        msg = "Failed to update table {}".format(e)
        return False, msg

def updateHospitalStatus(data):
    """
    Admin sets hospital status to TRUE.
    Parameters
    ----------
    data : json
        Contains hospitalid which is needed to change the status.
    Returns
    ----------
    tuple
        Returns a tuple which contains a bool(checking database staus) and a message for the approval of the status.
    """

    try:
        now = datetime.datetime.now()
        formattedDate = now.strftime("%Y%m%d")
        cursor = connection.cursor(dictionary=True)
        mysqlUpdateQuery = "UPDATE hospitals set approvalstatus = %s, lastmoddate = %s where hospitalid = %s"
        inputData = ("TRUE",
                     formattedDate, int(data['hospitalid']))
        cursor.execute(mysqlUpdateQuery, inputData)
        connection.commit()
        msg = "Status Approved"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update into hospitals table {}".format(error))
        msg = "Failed to update into hospitals table {}".format(error)
        return False, msg

    except Exception as e:
        print("Failed to update into hospitals table {}".format(e))
        msg = "Failed to update into hospitals table {}".format(e)
        return False, msg


def updateDoctorStatus(data):
    """
    Admin sets doctors status to TRUE.
    Parameters
    ----------
    data : json
        Contains doctorid which is needed to change the status.
    Returns
    ----------
    tuple
        Returns a tuple which contains a bool(checking database staus) and a message for the approval of the status.
    """

    try:
        now = datetime.datetime.now()
        formattedDate = now.strftime("%Y%m%d")
        cursor = connection.cursor(dictionary=True)
        mysqlUpdateQuery = "UPDATE doctors set approvalstatus = %s, lastmoddate = %s where doctorid = %s"
        inputData = ("TRUE",
                     formattedDate, int(data['doctorid']))
        cursor.execute(mysqlUpdateQuery, inputData)
        connection.commit()
        msg = "Status Approved"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update into doctors table {}".format(error))
        msg = "Failed to update into doctors table {}".format(error)
        return False, msg

    except Exception as e:
        print("Failed to update into doctors table {}".format(e))
        msg = "Failed to update into doctors table {}".format(e)
        return False, msg


def getUnapprovedDoctors():
    """
    Gets all the unapproved doctors.
    Parameters
    ----------
    None
    Returns
    ----------
    tuple
        Returns a tuple which contains a bool(checking database staus) and a list of unapproved doctors.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "Select * FROM doctors WHERE approvalstatus = %s", ("FALSE",))
        unapprovedDoctors = cursor.fetchall()
        finalData = []
        for record in unapprovedDoctors:
            finalData.append(record)

        cursor.close()
        return True, finalData

    except mysql.connector.Error as error:
        print("Failed to get unapproved Doctors {}".format(error))
        msg = "Failed to get unapproved Doctors {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getunapprovedDoctors: {}".format(e))
        msg = "Failed to get unapproved Doctors {}".format(e)
        return False, msg


def getUnapprovedHospitals():
    """
    Gets all the unapproved hospitals.
    Parameters
    ----------
    None
    Returns
    ----------
    tuple
        Returns a tuple which contains a bool(checking database staus) and a list of unapproved hospitals.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "Select * FROM hospitals WHERE approvalstatus = %s", ("FALSE",))
        unapprovedHospitals = cursor.fetchall()
        finalData = []
        for record in unapprovedHospitals:
            finalData.append(record)

        cursor.close()
        return True, finalData

    except mysql.connector.Error as error:
        print("Failed to get unapproved Hospitals {}".format(error))
        msg = "Failed to get unapproved Hospitals {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in getunapprovedHospitals: {}".format(e))
        msg = "Failed to get unapproved Hospitals {}".format(e)
        return False, msg


def checkDuplicateEmail(email):
    """
    Checks if an email is present twice in the database.
    Parameters
    ----------
    email : string
        Email of the user.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) is a check to see if there are two users with the same email. The second element is a status code of whether there is a database error or not.  
    """

    try:
        cursor = connection.cursor(dictionary=True)
        sqlSelectQuery = "SELECT * FROM Users where email = %s"
        cursor.execute(sqlSelectQuery, (email,))
        record = cursor.fetchall()
        print(email)
        if record:
            return True, 1
        else:
            return False, 1

    except mysql.connector.Error as error:
        print(error)
        return (False, 0)

    except Exception as e:
        print("some error occurred in checkDuplicateEmail: {}".format(e))
        return (False, 0)


def addUser(data):
    """
    Adds an user into the database
    Parameters
    ----------
    data : json
        Information about the user who is going to be added.
    Returns
    ----------
    bool
        Checks if the user got added to the database or not.
    """

    try:
        username = str(data["username"])
        firstname = str(data["firstname"])
        lastname = str(data["lastname"])
        usertype = str(data["usertype"])
        gender = str(data["gender"])
        email = str(data["email"])
        password = str(data["password"])
        phone = str(data["phone"])
        isactive = "TRUE"
        now = datetime.datetime.now()
        formattedDate = now.strftime("%Y%m%d")
        cursor = connection.cursor(dictionary=True)
        sqlInsertQuery = "INSERT INTO users (username, firstname, lastname, usertype, gender, email, password, phone, isactive, lastmoddate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sqlInsertQuery, (username, firstname, lastname,
                                        usertype, gender, email, password, phone, isactive, formattedDate))

        connection.commit()
        cursor.close()
        return True

    except mysql.connector.Error as error:
        print(error)
        return False

    except Exception as e:
        print("some error occurred in addUser: {}".format(e))
        return False


def loginCheck(email, password):
    """
    Checks if the password and email are matching in the database and returns the user
    Parameters
    ----------
    email : string
        Email of the user.
    password : string
        Password of the user.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) is a check to see if there is a user present with matching password and email. The second element is a status code of whether there is a database error or not.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT userid, username, email, usertype, phone, isactive FROM users WHERE email= %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return user, 1
        else:
            return [], 1

    except mysql.connector.Error as error:
        print(error)
        return False, 0

    except Exception as e:
        print("some error occurred in loginCheck: {}".format(e))
        return False, 0


def getUserProfileByID(ID):
    """
    Get the user information given his ID.
    Parameters
    ----------
    ID : int
        ID of the user.
    Returns
    ----------
    list
        Returns a list containing the information of an user given his id.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            'SELECT username, email, firstname, lastname, gender, password, phone, isactive FROM users where userid = %s', (int(ID),))
        user = cursor.fetchone()

        cursor.close()
        return user

    except mysql.connector.Error as error:
        print(error)
        return []

    except Exception as e:
        print("some error occurred in getUserProfileByID: {}".format(e))
        return []


def updateUserProfile(data):
    """
    Updates an user in the database.
    Parameters
    ----------
    data : json
        Updated user information.
    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) checks to see if the database operations worked correctly. The second element is a message about the same.
    """

    try:
        now = datetime.datetime.now()
        formattedDate = now.strftime("%Y%m%d")
        cursor = connection.cursor(dictionary=True)
        sqlUpdateQuery = "UPDATE users set username = %s, email = %s, firstname = %s, lastname = %s, gender = %s, password = %s, phone = %s, isactive = %s, lastmoddate = %s WHERE userid = %s"
        inputData = (str(data['username']), str(data['email']),
                     str(data["firstname"]), str(data["lastname"]), str(data["gender"]), str(
                         data["password"]), str(data["phone"]), str(data["isactive"]), formattedDate, int(data["userid"]))
        cursor.execute(sqlUpdateQuery, inputData)
        connection.commit()

        print("Record updated successfully into users table")
        msg = "Record updated successfully into users table"
        cursor.close()
        return True, msg

    except mysql.connector.Error as error:
        print("Failed to update table {}".format(error))
        msg = "Failed to update table {}".format(error)
        return False, msg

    except Exception as e:
        print("some error occurred in updateUserProfile: {}".format(e))
        msg = "Failed to update table {}".format(e)
        return False, msg
