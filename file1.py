from dialogflow_v2beta1.gapic import sessions_client_config

class SessionsClient

# The name of the interface for this client. This is the key used to
# find the method configuration in the client_config dictionary.

_INTERFACE_NAME = "google.cloud.dialogflow.v2beta1.Sessions"

client_config (dict): DEPRECATED. A dictionary of call options for each method. 
If not specified, the default configuration is used.

client_config = {
    "interfaces": {
        "google.cloud.dialogflow.v2beta1.Sessions": {
            "retry_codes": {
                "idempotent": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
                "non_idempotent": [],
            },
            "retry_params": {
                "default": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 20000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 20000,
                    "total_timeout_millis": 600000,
                }
            },
            "methods": {
                "DetectIntent": {
                    "timeout_millis": 220000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default",
                },
                "StreamingDetectIntent": {
                    "timeout_millis": 220000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default",
                },
            },
        }
    }
}


    
