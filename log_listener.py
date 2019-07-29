import sqlite3
from sqlite3 import Error

sm_list = []

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return None    

# def get_recv_data(gatewayID, numfailedSM, timestamp, sm_list):
#     conn = create_connection("db\smartgw_log.db")
#     with conn:
#         recvlog = (gatewayID,numfailedSM,timestamp)
#         lrlogid = store_recv_log(conn,recvlog)
#         for sm in sm_list:
#             smFailedlog = (sm,timestamp,lrlogid)
#             resultId = store_smFailed_log(conn,smFailedlog)
#             print(resultId)

def get_data(gatewayID, numAnomalydata, timestamp, sm_list, tag):
    conn = create_connection("./db/smartgw_log.db")
    with conn:
        dnnlog = (gatewayID,numAnomalydata,timestamp)
        dnnlogid = store_dnn_log(conn,dnnlog)
        for sm in sm_list:
            if tag == "anomaly":
                anlomalylog = (sm,timestamp,dnnlogid)
                resultId = store_Anomaly_log(conn,anlomalylog)
                print(resultId)
            elif tag == "smfailed":
                smFailedlog = (sm,timestamp,lrlogid)
                resultId = store_smFailed_log(conn,smFailedlog)
                print(resultId)
            else:
                print("The tag is null or not exist .")

def store_recv_log(conn, recvlog):
    """
    Create a new LoRa Receiver Log into the LoRa_Receiver_Log table
    :param conn:
    :param recvlog:
    :return: LRLogId
    """
    sql = ''' INSERT INTO LoRa_Receiver_Log(GatewayID,NumFailedSM,timestamp)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, recvlog)
    return cur.lastrowid

def store_smFailed_log(conn, smFailedlog):
    """
    Added Failed SM ID into the Failed_SM_Log table
    :param conn:
    :param smFailedlog:
    :return: FSMLogId
    """
    sql = ''' INSERT INTO Failed_SM_Log(SMId,timestamp,LRLogId)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, smFailedlog)
    return cur.lastrowid

def store_dnn_log(conn, dnnlog):
    """
    Create a new DNN Log into the DNN_Log table
    :param conn:
    :param dnnlog:
    :return: DnnLogId
    """
    sql = ''' INSERT INTO DNN_Log(GatewayID,NumAnomalyData,timestamp)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, dnnlog)
    return cur.lastrowid

def store_Anomaly_log(conn, anlomalylog):
    """
    Added SM ID with anomaly data into the Anomaly_Log table
    :param conn:
    :param anlomalylog:
    :return: AnlomalyId
    """
    #maybe next can classify what kind of anomaly (hacked, thief, or etc)

    sql = ''' INSERT INTO Anomaly_Log(SMId,timestamp,DnnLogId)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, anlomalylog)
    return cur.lastrowid
