# SeveraPublicRestApiDocumentation.ActivitiesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activitiesPatchActivity**](ActivitiesWriteApi.md#activitiesPatchActivity) | **PATCH** /v1/activities/{guid} | Update (Patch) a activity or a part of it
[**activitiesPostActivity**](ActivitiesWriteApi.md#activitiesPostActivity) | **POST** /v1/activities | Insert a activity
[**activityParticipantsPatchActivityParticipants**](ActivitiesWriteApi.md#activityParticipantsPatchActivityParticipants) | **PATCH** /v1/activityparticipants/{guid} | Update (Patch) a activity participant or a part of it
[**activityParticipantsPostActivityParticipant**](ActivitiesWriteApi.md#activityParticipantsPostActivityParticipant) | **POST** /v1/activityparticipants | Adds an activity participant



## activitiesPatchActivity

> [ActivityModel] activitiesPatchActivity(guid, opts)

Update (Patch) a activity or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesWriteApi();
let guid = "guid_example"; // String | ID of the activity. Can also be comma separate list of IDs to patch multiple activities with one call. When multiple IDs are given, returns model which has list of succeeded activities and list of errors.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ActivityModel
};
apiInstance.activitiesPatchActivity(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the activity. Can also be comma separate list of IDs to patch multiple activities with one call. When multiple IDs are given, returns model which has list of succeeded activities and list of errors. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ActivityModel | [optional] 

### Return type

[**[ActivityModel]**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activitiesPostActivity

> ActivityModel activitiesPostActivity(opts)

Insert a activity

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesWriteApi();
let opts = {
  'activityModel': new SeveraPublicRestApiDocumentation.ActivityModel() // ActivityModel | ActivityModel
};
apiInstance.activitiesPostActivity(opts, (error, data, response) => {
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
 **activityModel** | [**ActivityModel**](ActivityModel.md)| ActivityModel | [optional] 

### Return type

[**ActivityModel**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activityParticipantsPatchActivityParticipants

> [ActivityParticipantModel] activityParticipantsPatchActivityParticipants(guid, opts)

Update (Patch) a activity participant or a part of it

Only IsConfirmed property can be updated.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesWriteApi();
let guid = "guid_example"; // String | ID of the activity participant
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ActivityParticipantModel
};
apiInstance.activityParticipantsPatchActivityParticipants(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the activity participant | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ActivityParticipantModel | [optional] 

### Return type

[**[ActivityParticipantModel]**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activityParticipantsPostActivityParticipant

> ActivityParticipantModel activityParticipantsPostActivityParticipant(opts)

Adds an activity participant

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesWriteApi();
let opts = {
  'activityParticipantModel': new SeveraPublicRestApiDocumentation.ActivityParticipantModel() // ActivityParticipantModel | ActivityParticipantModel
};
apiInstance.activityParticipantsPostActivityParticipant(opts, (error, data, response) => {
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
 **activityParticipantModel** | [**ActivityParticipantModel**](ActivityParticipantModel.md)| ActivityParticipantModel | [optional] 

### Return type

[**ActivityParticipantModel**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

