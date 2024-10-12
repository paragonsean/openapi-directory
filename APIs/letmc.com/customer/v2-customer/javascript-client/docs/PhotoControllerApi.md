# AgentOsApiV2CustomerLoginCallGroup.PhotoControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**photoControllerGetPhotoDownload**](PhotoControllerApi.md#photoControllerGetPhotoDownload) | **GET** /v2/customer/{shortName}/photo/download | Downloads the photo of a property given the photo ID.



## photoControllerGetPhotoDownload

> Object photoControllerGetPhotoDownload(shortName, token, photoID, opts)

Downloads the photo of a property given the photo ID.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.PhotoControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let photoID = "photoID_example"; // String | The unique ID of the photo on the property
let opts = {
  'width': 56, // Number | An optional parameter specifying the image width
  'height': 56 // Number | An optional parameter specifying the image height
};
apiInstance.photoControllerGetPhotoDownload(shortName, token, photoID, opts, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **photoID** | **String**| The unique ID of the photo on the property | 
 **width** | **Number**| An optional parameter specifying the image width | [optional] 
 **height** | **Number**| An optional parameter specifying the image height | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

