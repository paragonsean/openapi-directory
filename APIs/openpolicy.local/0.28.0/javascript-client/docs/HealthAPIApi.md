# OpenPolicyAgentOpaRestApi.HealthAPIApi

All URIs are relative to *http://openpolicy.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHealth**](HealthAPIApi.md#getHealth) | **GET** /health | Health



## getHealth

> getHealth(opts)

Health

This API endpoint verifies that the server is operational.  The response from the server is either 200 or 500: - **200** - OPA service is healthy. If &#x60;bundles&#x60; is true, then all configured bundles have been activated. If &#x60;plugins&#x60; is true, then all plugins are in an &#39;OK&#39; state. - **500** - OPA service is *not* healthy. If &#x60;bundles&#x60; is true, at least one of configured bundles has not yet been activated. If &#x60;plugins&#x60; is true, at least one plugins is in a &#39;not OK&#39; state.  --- **Note** This check is only for initial bundle activation. Subsequent downloads will not affect the health check.  Use the **status** endpoint (in the (management API)[management.html]) for more fine-grained bundle status monitoring.  ---

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.HealthAPIApi();
let opts = {
  'bundles': true, // Boolean | Reports on bundle activation status (useful for 'ready' checks at startup).  This includes any discovery bundles or bundles defined in the loaded discovery configuration.
  'plugins': false // Boolean | Reports on plugin status
};
apiInstance.getHealth(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundles** | **Boolean**| Reports on bundle activation status (useful for &#39;ready&#39; checks at startup).  This includes any discovery bundles or bundles defined in the loaded discovery configuration. | [optional] 
 **plugins** | **Boolean**| Reports on plugin status | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

