# SeveraPublicRestApiDocumentation.ActivitiesDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activitiesDeleteActivity**](ActivitiesDeleteApi.md#activitiesDeleteActivity) | **DELETE** /v1/activities/{guid} | Delete an activity
[**activitiesDeleteExceptions**](ActivitiesDeleteApi.md#activitiesDeleteExceptions) | **DELETE** /v1/activities/{guid}/exceptions | Resets exceptions from a recurring activity.
[**activityParticipantsDeleteActivityParticipant**](ActivitiesDeleteApi.md#activityParticipantsDeleteActivityParticipant) | **DELETE** /v1/activities/{activityGuid}/activityparticipants/{activityParticipantGuid} | Delete activity participant.



## activitiesDeleteActivity

> activitiesDeleteActivity(guid)

Delete an activity

Returns: No Content (204) if succeeded. Not found (404) if activity can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesDeleteApi();
let guid = "guid_example"; // String | ID for the activity to delete
apiInstance.activitiesDeleteActivity(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the activity to delete | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activitiesDeleteExceptions

> activitiesDeleteExceptions(guid)

Resets exceptions from a recurring activity.

Returns: No Content (204) if succeeded. Not found (404) if activity can&#39;t be found or is not recurring.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesDeleteApi();
let guid = "guid_example"; // String | ID of the recurring activity
apiInstance.activitiesDeleteExceptions(guid, (error, data, response) => {
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
 **guid** | **String**| ID of the recurring activity | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityParticipantsDeleteActivityParticipant

> activityParticipantsDeleteActivityParticipant(activityGuid, activityParticipantGuid)

Delete activity participant.

Returns: No Content (204) if succeeded. Not found (404) if participant can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesDeleteApi();
let activityGuid = "activityGuid_example"; // String | ID of the activity from which to delete the participant. If an activity occurrence guid is given, this will create an exception to the recurring activity and delete the participant from that.
let activityParticipantGuid = "activityParticipantGuid_example"; // String | ID of the participant
apiInstance.activityParticipantsDeleteActivityParticipant(activityGuid, activityParticipantGuid, (error, data, response) => {
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
 **activityGuid** | **String**| ID of the activity from which to delete the participant. If an activity occurrence guid is given, this will create an exception to the recurring activity and delete the participant from that. | 
 **activityParticipantGuid** | **String**| ID of the participant | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

