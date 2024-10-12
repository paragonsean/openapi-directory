# BungieNetApi.AppApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appGetApplicationApiUsage**](AppApi.md#appGetApplicationApiUsage) | **GET** /App/ApiUsage/{applicationId}/ | 
[**appGetBungieApplications**](AppApi.md#appGetBungieApplications) | **GET** /App/FirstParty/ | 



## appGetApplicationApiUsage

> AppGetApplicationApiUsage200Response appGetApplicationApiUsage(applicationId, opts)



Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.AppApi();
let applicationId = 56; // Number | ID of the application to get usage statistics.
let opts = {
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | End time for query. Goes to now if not specified.
  'start': new Date("2013-10-20T19:20:30+01:00") // Date | Start time for query. Goes to 24 hours ago if not specified.
};
apiInstance.appGetApplicationApiUsage(applicationId, opts, (error, data, response) => {
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
 **applicationId** | **Number**| ID of the application to get usage statistics. | 
 **end** | **Date**| End time for query. Goes to now if not specified. | [optional] 
 **start** | **Date**| Start time for query. Goes to 24 hours ago if not specified. | [optional] 

### Return type

[**AppGetApplicationApiUsage200Response**](AppGetApplicationApiUsage200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appGetBungieApplications

> AppGetBungieApplications200Response appGetBungieApplications()



Get list of applications created by Bungie.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.AppApi();
apiInstance.appGetBungieApplications((error, data, response) => {
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

[**AppGetBungieApplications200Response**](AppGetBungieApplications200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

