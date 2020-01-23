### The method_configs is used in the detectIntent requests
self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )
        
interface_config = client_config["interfaces"][self._INTERFACE_NAME]
                 = 
        {
            "retry_codes": 
            {
                "idempotent": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
                "non_idempotent": [],
            },
            "retry_params": 
            {
                "default": 
                {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 20000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 20000,
                    "total_timeout_millis": 600000,
                }
            },
            "methods": 
            {
                "DetectIntent": 
                {
                    "timeout_millis": 220000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default",
                },
                "StreamingDetectIntent": {
                    "timeout_millis": 220000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default",
                },
            }
        }



def parse_method_configs(interface_config):
"""Creates default retry and timeout objects for each method in a gapic
    interface config."""
