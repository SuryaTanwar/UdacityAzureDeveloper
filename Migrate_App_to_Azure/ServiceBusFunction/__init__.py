import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):
    # I diidn't use new school formating <f"string and {value}"> because logging has issues with it
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    message = msg.get_body().decode('utf-8')

    #  NOTE:sendmail function
    def send_email(db_email, db_firstname, db_lastname, db_subject, db_message):
        # Sendgrid mail details
        from_email = 'forsurya02@gmail.com'
        to_emails = db_email
        subject = f"Hello {db_firstname}, You have got a notification"
        html_content = f" Hello {db_firstname} {db_lastname}, We created a topic to inform you about {db_subject}. More details below: <br> \n \n  {db_message}"



        message = Mail(
            from_email = from_email,
            to_emails= to_emails,
            subject = subject,
            html_content = html_content)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            logging.info(response.status_code)
            logging.info(response.body)
            logging.info(response.headers)
        except Exception as e:
            logging.error(str(e))

    #  NOTE:sendmail function ends


    # TODO: Get connection to database
    
    conn = psycopg2.connect(
            host="techconf-postgres-db-server.postgres.database.azure.com",
            database="techconfdb",
            user="postgresAdmin@techconf-postgres-db-server",
            password="single123@")

    notification_sql = f"SELECT message,subject FROM public.notification WHERE id={message}" 
    attendees_sql = f"SELECT first_name, last_name, email FROM public.attendee ORDER BY id ASC"

    try:
        # TODO: Get notification message and subject from database using the notification_id
        notification_msg_subj_date_tuple = None
        with conn.cursor() as cur:
            cur.execute(notification_sql)
            notification_msg_subj_date_tuple = cur.fetchone()
        db_message, db_subject = notification_msg_subj_date_tuple

        # TODO: Get attendees email and name
        attendee_fname_lname_email_tuple = None
        with conn.cursor() as cur:
            cur.execute(attendees_sql)
            attendee_fname_lname_email_tuple = cur.fetchall()


        # TODO: Loop through each attendee and send an email with a personalized subject
        for db_tuples in attendee_fname_lname_email_tuple:
            db_firstname, db_lastname, db_email = db_tuples
            send_email(db_email, db_firstname, db_lastname, db_subject, db_message)

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        update_notification_sql = "UPDATE public.notification SET status=%s, completed_date=%s WHERE id=%s"
        with conn.cursor() as cur:
            cur.execute(update_notification_sql, (f"Notified {len(attendee_fname_lname_email_tuple)} attendees", datetime.utcnow(), message ))
            conn.commit()



    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # TODO: Close connection
        conn.close()
        