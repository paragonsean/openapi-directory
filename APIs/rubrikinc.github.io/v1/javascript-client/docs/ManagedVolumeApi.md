# RubrikRestApi.ManagedVolumeApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createManagedVolumeGenerateScriptJob**](ManagedVolumeApi.md#createManagedVolumeGenerateScriptJob) | **POST** /managed_volume/snapshot/export/{id}/script | Generate and download unified view script



## createManagedVolumeGenerateScriptJob

> AsyncRequestStatus createManagedVolumeGenerateScriptJob(id)

Generate and download unified view script

Start an asynchronous job to generate and download a script to unify export paths across channels in managed volume export.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ManagedVolumeApi();
let id = "id_example"; // String | ID of snapshot export.
apiInstance.createManagedVolumeGenerateScriptJob(id, (error, data, response) => {
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
 **id** | **String**| ID of snapshot export. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

