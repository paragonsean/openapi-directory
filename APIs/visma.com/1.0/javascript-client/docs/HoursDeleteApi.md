# SeveraPublicRestApiDocumentation.HoursDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntriesDeleteTimeEntry**](HoursDeleteApi.md#timeEntriesDeleteTimeEntry) | **DELETE** /v1/timeentries/{guid} | Deletes a time entry.
[**workHoursDeleteWorkHour**](HoursDeleteApi.md#workHoursDeleteWorkHour) | **DELETE** /v1/workhours/{guid} | Deletes a work hour.



## timeEntriesDeleteTimeEntry

> timeEntriesDeleteTimeEntry(guid)

Deletes a time entry.

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the time entry.
apiInstance.timeEntriesDeleteTimeEntry(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the time entry. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursDeleteWorkHour

> workHoursDeleteWorkHour(guid)

Deletes a work hour.

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.HoursDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the work hour.
apiInstance.workHoursDeleteWorkHour(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the work hour. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

