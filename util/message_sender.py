import pywhatkit
from datetime import datetime

class WhatsAppMessageSender:
    """
    Constructor method for the WhatsAppMessageSender class

    params:
        counter: The total number of rows drived from the excel sheet read
    returns:
        None
    """
    def __init__(self, counter):
        self.counter = counter

    """
    Method which checks if the message being sent is last of the batch.

    params:
        self.counter: The total number of messages to be sent
    returns:
        True/ False 
    """
    def __is_last_message(self):
        print("Checking if the message is a last one or not.")
        return self.counter - 1 == 0

    """
    Method to formulate the message body, dynamically embeds @loan_amount,
    @interest_rate, @contact_number into @message.

    params:
        loan_amount: The total loan amount of the customer
        interest_rate: The interest rate applied on the loan
        contact_number: The contact number of the customer
        message: The actual message to be sent to the customer

    returns:
        message: Message text embedded with the other params values provided
    """
    def __formulate_message_body(self, loan_amount, interest_rate, contact_number, message):
        print("Formulating the message body.")

        #TODO: Modify the message body logic
        return message

    """
    Method to send the WhatsApp message to the customer.

    params:
        loan_amount: The total loan amount of the customer
        interest_rate: The interest rate applied on the loan
        contact_number: The contact number of the customer
        message: The actual message to be sent to the customer

    returns:
        None
    """
    def send_message(self, customer):
        print("Sending message...")

        #TODO: Change the variables based on actual data being provided
        loan_amount = customer["Loan_Amount"]
        interest_rate = customer["Interest_Rate"]
        contact_number = customer["Contact"]
        message = customer["Message"]
        
        # Current hour
        scheduled_hour = (datetime.now().hour)%24

        # Current minute
        scheduled_minute = datetime.now().minute

        
        # If the current minute is closer to the end of an hour,
        # the message is scheduled to deliver in the next hour.
        if (scheduled_minute + 2) >= 60:
                scheduled_hour = scheduled_hour + 1
        if not self.__is_last_message():
            scheduled_minute = (scheduled_minute + 2)%60

        # Adding extra buffer time for scheduling the last message since
        # there is an issue that the last message is not getting delivered.
        else:
           scheduled_minute = (scheduled_minute + 4)%60
        
        # Send message to customer
        try:
            contact_number = str(contact_number)
            if "+91" not in contact_number:
                print("Adding extension code to the contact number.")
                contact_number = "+91" + contact_number

            pywhatkit.sendwhatmsg(
                contact_number,
                self.__formulate_message_body(loan_amount, interest_rate, contact_number, message),
                scheduled_hour,
                scheduled_minute
            )

            print("Message is being delivered to the customer...")
        except Exception as e:
            print(str(e))

        self.counter = self.counter - 1

        # Close the tabs once done