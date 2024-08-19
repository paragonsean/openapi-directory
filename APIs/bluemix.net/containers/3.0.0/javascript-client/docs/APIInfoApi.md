# IbmContainersApi.APIInfoApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containersMessagesGet**](APIInfoApi.md#containersMessagesGet) | **GET** /containers/messages | List messages for the user
[**containersVersionGet**](APIInfoApi.md#containersVersionGet) | **GET** /containers/version | List latest API version



## containersMessagesGet

> ContainersMessagesGet200Response containersMessagesGet(xAuthToken, xAuthProjectId)

List messages for the user

This endpoint retrieves all IBM Containers system messages for the user.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.APIInfoApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. To retrieve your space ID, run `cf space <space_name> --guid` and replace `<space_name>` with the name of the space where you want to create or work with your container. 
apiInstance.containersMessagesGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. To retrieve your space ID, run &#x60;cf space &lt;space_name&gt; --guid&#x60; and replace &#x60;&lt;space_name&gt;&#x60; with the name of the space where you want to create or work with your container.  | 

### Return type

[**ContainersMessagesGet200Response**](ContainersMessagesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersVersionGet

> ContainersVersionGetInfo containersVersionGet()

List latest API version

This endpoint retrieves a list of all microservices that are used in the IBM Containers service with their current build version. This method does not require authentication.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.APIInfoApi();
apiInstance.containersVersionGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ContainersVersionGetInfo**](ContainersVersionGetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

