from util.data_reader import CustomerDataReader
from util.message_sender import WhatsAppMessageSender

if __name__ == "__main__":

    customer_data = None
    try:
        customer_data = CustomerDataReader("./resource/customers.xlsx").read_customer_data()
    except Exception as e:
        print(str(e))
        print("Kindly run the application again.")
        pass

    message_sender = WhatsAppMessageSender(len(customer_data))
    for _, customer in customer_data.iterrows():
        try:
            message_sender.send_message(customer)
            pass
        except Exception as e:
            print(str(e))