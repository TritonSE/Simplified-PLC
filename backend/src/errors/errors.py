"""
This file contains the generic error class type which contains error messages that we might
need in development. Every time a new feature is added BE SURE TO ADD PROPER ERROR MESSAGES
to the corresponding error class it falls under
"""


class CustomError(Exception):
    """
    This is the base class for all error types. All errors will be divided into
    different groups based on error type and will have its own respective class
    in a separate file
    """

    def __init__(self, code: int, status: int, message: str) -> None:
        """
        This is the generic constructor for errors

        Args:
            code: This is the code that identifies each error
            status: This is the error status when sending error response
                Check out https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
            message: This is the message that informs users of what went wrong
        """
        super().__init__(message)
        self.code = code
        self.status = status
        self.message = message
        self.context: list[str] = []

    def add_context(self, message: str) -> list[str]:
        """
        This function allows you to add context to error messages
        such as stack traces

        Args:
            message: Message to be added
        """
        self.context.append(message)
        return self.context

    def display_message(self, client_facing: bool) -> str:
        """
        This method will display the error message
        based on whether its client facing or not

        Args:
            client_facing: determines whether the message is client facing
        """
        if client_facing:
            return self.message

        context = "\n" + "\n\n".join(self.context) if self.context else ""
        return f"Error: Type {type(self).__name__}, Code {self.code}, Context: {context}"
