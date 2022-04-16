from plyer import notification

def notify(title_, message_):
    notification.notify(
            title = title_,
            message= message_ ,

            # displaying time
            timeout=5
)
