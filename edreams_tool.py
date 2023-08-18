from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from instagrapi import Client

class InstagramSendInputSchema(BaseModel):
    tool_input: str = Field(...)

class InstagramSendTool(BaseTool):
    name = "Instagram Send Tool"
    description = "Tool for sending messages on Instagram"
    args_schema = InstagramSendInputSchema

    def _execute(self, input_data: InstagramSendInputSchema):
        message = input_data.tool_input

        instagram_username = self.get_tool_config('INSTAGRAM_USERNAME')
        instagram_password = self.get_tool_config('INSTAGRAM_PASSWORD')
        target_username = self.get_tool_config('INSTAGRAM_TARGET_USERNAME')

        # Crear cliente y realizar login
        cl = Client()
        cl.login(instagram_username, instagram_password)

        # Enviar mensaje
        try:
            result = cl.direct_send(message, user_ids=[target_username])
            thread_id = result.thread_id
            thread = cl.direct_thread(thread_id)
            # Store last_message_id, thread_id, last_sent_message, and last_sent_timestamp as instance variables
            self.last_message_id = thread.messages[0].id
            self.thread_id = result.thread_id
            self.last_sent_message = message
            self.last_sent_timestamp = thread.messages[0].timestamp
            return "Message sent successfully"
        except Exception as e:
            return f"Error sending message: {e}"

