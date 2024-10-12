# AgentOsApiV2CustomerLoginCallGroup.PropertyControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**propertyControllerGetPropertiesPhotos**](PropertyControllerApi.md#propertyControllerGetPropertiesPhotos) | **GET** /v2/customer/{shortName}/property/{propertyID}/photos | A collection showing all the photos linked to a specific block, property or room



## propertyControllerGetPropertiesPhotos

> LandlordPhotoModelResults propertyControllerGetPropertiesPhotos(shortName, token, propertyID, offset, count)

A collection showing all the photos linked to a specific block, property or room

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.PropertyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let propertyID = "propertyID_example"; // String | The unique ID of the Property
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.propertyControllerGetPropertiesPhotos(shortName, token, propertyID, offset, count, (error, data, response) => {
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
 **propertyID** | **String**| The unique ID of the Property | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**LandlordPhotoModelResults**](LandlordPhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

