import dialogflow_v2 as dialogflow
import uuid
session_client = dialogflow.SessionsClient()
project_id="myprojectomega-261417"
session_id = str(uuid.uuid4())
language_code = 'en-US'

session = session_client.session_path(project_id, session_id)
text_input = dialogflow.types.TextInput(
            text='hi', language_code=language_code)

query_input = dialogflow.types.QueryInput(text=text_input)

response = session_client.detect_intent(
            session=session, query_input=query_input)
            
    



1) timeout = session_client._method_configs["DetectIntent"].timeout

2) Attributes of timeout object :
_deadline = 600
_initial = 20.0
_maximum = 20.0
_multiplier = 1.0


import dialogflow_v2 as dialogflow
session_client = dialogflow.SessionsClient()

session
