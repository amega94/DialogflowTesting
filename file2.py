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

    retry_codes_map = {
        name: retry_codes
        for name, retry_codes in six.iteritems(interface_config.get("retry_codes", {}))
    }
              # Grab all of the retry params
    retry_params_map = {
        name: retry_params
        for name, retry_params in six.iteritems(
            interface_config.get("retry_params", {})
        )
    }

# retry_codes_map = {'non_idempotent': [], 'idempotent': ['DEADLINE_EXCEEDED', 'UNAVAILABLE']}
# retry_params_map = {'default': {'rpc_timeout_multiplier': 1.0, 'max_rpc_timeout_millis': 20000, 'initial_retry_delay_millis': 100, 'retry_delay_multiplier': 1.3, 'total_timeout_millis': 600000, 'initial_rpc_timeout_millis': 20000, 'max_retry_delay_millis': 6000
#0}}

#My Modifications to test the code
for method_name, method_params in six.iteritems(
        interface_config.get("methods", {})
    ):
    
    print(method_name)
    print(method_params)
    retry_params_name = method_params.get("retry_params_name")
    print("thanks", retry_params_name)

'''
STDOUT

DetectIntent                                                                                                                                                                                                                                      
{'retry_codes_name': 'non_idempotent', 'timeout_millis': 220000, 'retry_params_name': 'default'}                                                                                                                                                  
thanks default                                                                                                                                                                                                                                    
StreamingDetectIntent                                                                                                                                                                                                                             
{'retry_codes_name': 'non_idempotent', 'timeout_millis': 220000, 'retry_params_name': 'default'}                                                                                                                                                  
thanks default

Therefore we can conclude that we enter the if sttmnt for the 2 occassions and execute the following code.

retry_params = retry_params_map[retry_params_name]
retry_ = _retry_from_retry_config(
                retry_params, retry_codes_map[method_params["retry_codes_name"]]
            )
timeout_ = _timeout_from_retry_config(retry_params)
            

'''
    
    retry_params = retry_params_map[retry_params_name]
    print(retry_params,'Number 1')
    print(retry_codes_map[method_params["retry_codes_name"]],'Number 2')
        #retry_ = _retry_from_retry_config(
        #        retry_params, retry_codes_map[method_params["retry_codes_name"]]
        #    )
        #timeout_ = _timeout_from_retry_config(retry_params)


{'max_rpc_timeout_millis': 20000, 'rpc_timeout_multiplier': 1.0, 'total_timeout_millis': 600000, 'retry_delay_multiplier': 1.3, 'initial_retry_delay_millis': 100, 'max_retry_delay_millis': 60000, 'initial_rpc_timeout_millis': 20000} Number 1 
[] Number 2                                                                                                                                                                                                                                       
{'max_rpc_timeout_millis': 20000, 'rpc_timeout_multiplier': 1.0, 'total_timeout_millis': 600000, 'retry_delay_multiplier': 1.3, 'initial_retry_delay_millis': 100, 'max_retry_delay_millis': 60000, 'initial_rpc_timeout_millis': 20000} Number 1 
[] Number 2                                                                                                                                                                                                                                       
               

