# BusinessUnits.BusinessUnitApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID**](BusinessUnitApi.md#getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID) | **GET** /business-units/v3/business-units/user/{userId} | Get Business Units for a user



## getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID

> CollectionResponsePublicBusinessUnitNoPaging getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID(userId, opts)

Get Business Units for a user

Get Business Units identified by &#x60;userId&#x60;. The &#x60;userId&#x60; refers to the user’s ID.

### Example

```javascript
import BusinessUnits from 'business_units';
let defaultClient = BusinessUnits.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new BusinessUnits.BusinessUnitApi();
let userId = "userId_example"; // String | Identifier of user to retrieve.
let opts = {
  'properties': ["null"], // [String] | The names of properties to optionally include in the response body. The only valid value is `logoMetadata`.
  'name': ["null"] // [String] | The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned.
};
apiInstance.getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID(userId, opts, (error, data, response) => {
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
 **userId** | **String**| Identifier of user to retrieve. | 
 **properties** | [**[String]**](String.md)| The names of properties to optionally include in the response body. The only valid value is &#x60;logoMetadata&#x60;. | [optional] 
 **name** | [**[String]**](String.md)| The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned. | [optional] 

### Return type

[**CollectionResponsePublicBusinessUnitNoPaging**](CollectionResponsePublicBusinessUnitNoPaging.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

