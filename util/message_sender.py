import pywhatkit
from datetime import datetime

class WhatsAppMessageSender:

    # The hour value during which the message is sent
    _scheduled_hour = 0
    # The minute value at which the message is sent 
    _scheduled_minute = 0

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
    def is_last_message(self):
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
    def formulate_message_body(self, loan_amount, interest_rate, contact_number, message):
        pass

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
    def send_message(self, loan_amount, interest_rate, contact_number, message):

        # Current hour
        _scheduled_hour = (datetime.now().hour)%24

        # Current minute
        _scheduled_minute = datetime.now().minute

        
        # If the current minute is closer to the end of an hour,
        # the message is scheduled to deliver in the next hour.
        if (_scheduled_minute + 2) >= 60:
                _scheduled_hour = _scheduled_hour + 1
        if not self.is_last_message():
            _scheduled_minute = (_scheduled_minute + 2)%60

        # Adding extra buffer time for scheduling the last message since
        # there is an issue that the last message is not getting delivered.
        else:
            _scheduled_minute = (_scheduled_minute + 4)%60
        
        # Send message to customer
        try:
            pywhatkit.sendwhatmsg(
                f"{contact_number}",
                f"{self.formulate_message_body(loan_amount, interest_rate, contact_number, message)}",
                _scheduled_hour,
                _scheduled_minute
            )
        except Exception:
            pass

        self.counter = self.counter - 1

        # Close the tabs once done