from datetime import datetime
def generate_preprocessing(connection,from_date,to_date):
    cursor = connection.cursor()
    cursor.execute("delete from preprocessing_transaction")
    query = "SELECT d.document_no, GROUP_CONCAT(DISTINCT i.label SEPARATOR ',') as item FROM  sales_transaction as d "
    query = query + " INNER JOIN item i on d.item_no = i.no WHERE posting_date BETWEEN '"+ str(from_date) +"' and '"+ str(to_date) +"' GROUP BY d.document_no "
    insert_query = "insert into preprocessing_transaction(document_no,item) " + query
    cursor.execute(insert_query)
    return cursor.rowcount


