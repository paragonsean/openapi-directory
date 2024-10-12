# OpenPolicyAgentOpaRestApi.ConfigAPIApi

All URIs are relative to *http://openpolicy.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConfig**](ConfigAPIApi.md#getConfig) | **GET** /v1/config | Get configurations



## getConfig

> Model200SingleResult getConfig(opts)

Get configurations

This API endpoint responds with active configuration (result response)  --- **Note** The &#x60;credentials&#x60; field in the &#x60;services&#x60; configuration and  The &#x60;private_key&#x60; and &#x60;key&#x60; fields in the &#x60;keys&#x60; configuration will be omitted from the API response  ---

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.ConfigAPIApi();
let opts = {
  'pretty': true // Boolean | If true, response will be in a human-readable format.
};
apiInstance.getConfig(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 

### Return type

[**Model200SingleResult**](Model200SingleResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

