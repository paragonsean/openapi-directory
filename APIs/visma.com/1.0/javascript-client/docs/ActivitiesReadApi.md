# SeveraPublicRestApiDocumentation.ActivitiesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activitiesGetActivities**](ActivitiesReadApi.md#activitiesGetActivities) | **GET** /v1/activities | Get all activities of an organization
[**activitiesGetActivity**](ActivitiesReadApi.md#activitiesGetActivity) | **GET** /v1/activities/{guid} | Get activity by ID
[**activityParticipantsGetActivityParticipant**](ActivitiesReadApi.md#activityParticipantsGetActivityParticipant) | **GET** /v1/activityparticipants/{guid} | Get activity participant
[**activityParticipantsGetActivityParticipants**](ActivitiesReadApi.md#activityParticipantsGetActivityParticipants) | **GET** /v1/activities/{activityGuid}/activityparticipants | Get participants for an activity



## activitiesGetActivities

> [ActivityModel] activitiesGetActivities(opts)

Get all activities of an organization

Start and end date times accept values of DateTimeOffset type, based on UTF-8 encoding.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'closed': true, // Boolean | Optional: Which activities to fetch - open/closed, Default all.
  'activityCategories': [new SeveraPublicRestApiDocumentation.ActivityCategory()], // [ActivityCategory] | Optional: activity category for the activities to be fetched. Should be one of Personal/Absences/CalendarEntry/SalesEvent/Task. Default all.
  'customerGuids': ["null"], // [String] | Optional: ID of customer. Default all.
  'includeTasksWithNoCustomer': true, // Boolean | Optional: Include the activities that don't have customer. Default is true.
  'projectGuids': ["null"], // [String] | Optional: ID of the project for the activities to be fetched. If not provided, returns for all projects. Default all.
  'includeTasksWithNoProject': true, // Boolean | Optional: Include the activities that don't have project. Default is true.
  'projectBusinessUnitGuids': ["null"], // [String] | Optional: ID of the business unit of the project based on which activities should be filtered. If not provided, returns for all business units. Default all.
  'projectOwnerGuids': ["null"], // [String] | Optional: ID of the project manager. If not provided, returns for all project managers. Default all.
  'userGuids': ["null"], // [String] | Optional: ID of the user for the activities to be fetched. If not provided, returns for all users. Default all.
  'includeAsMember': false, // Boolean | Optional: Include the activities that the user is a member. Effective if userGuid is provided. Default is to not include.
  'userKeywordGuids': ["null"], // [String] | Optional: User keyword Ids of activity owner to search for.
  'startDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date and time from which to get the activities in user's timezone. Finds all activities that end after the date time. Format \"2017-04-12T13%3A20%3A00%2b02%3A00\". Default all.
  'endDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: ending date and time to which to get the activities in user's timezone. Finds all activities that start before or on the date time. Format \"2017-04-12T13%3A20%3A00%2b02%3A00\". Default all. If activities for one day are fetched, give start date time with time as 00:00 with the offset of the timezone and end time as 23:59:59 with the offset.
  'projectTaskStatusGuids': ["null"], // [String] | Optional: ID of the project task status. Default all.
  'phaseGuids': ["null"], // [String] | Optional: ID of the phase for the activities to be fetched. If not provided, returns for all phases. Default all.
  'includeSubPhases': false, // Boolean | Optional: If one phase guid is given include activities also from sub phases. If multiple phase guids are given, returns activities only for those regardless of this parameter. Default false.
  'contactGuids': ["null"], // [String] | Optional: ID of the contact for the activities to be fetched. If not provided, returns for all users. Default all.
  'hasDuration': true, // Boolean | Optional: has duration flag for the activity. Default all.
  'hasHours': true, // Boolean | Optional: has any work hour entries associated with the activity. Default all.
  'isUnassigned': true, // Boolean | Optional: is the activity unassigned. Default all.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get activities that have been added or changed after this date time (greater or equal).
  'useStrictStartAndEndDateTime': false, // Boolean | Optional: If given as true returns activities that start after start time and end before end time. If given as false returns activities that start before end time and end after start time. Limit are included in both cases. Default false.
  'activityTypeGuids': ["null"], // [String] | Optional: ID of the project activity type. Default all.
  'recurrenceType': new SeveraPublicRestApiDocumentation.RecurrenceType() // RecurrenceType | Optional: Type of the recurrence. Default returns all not recurring activities, instances and exceptions. (None = not recurring activity)
};
apiInstance.activitiesGetActivities(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **closed** | **Boolean**| Optional: Which activities to fetch - open/closed, Default all. | [optional] 
 **activityCategories** | [**[ActivityCategory]**](ActivityCategory.md)| Optional: activity category for the activities to be fetched. Should be one of Personal/Absences/CalendarEntry/SalesEvent/Task. Default all. | [optional] 
 **customerGuids** | [**[String]**](String.md)| Optional: ID of customer. Default all. | [optional] 
 **includeTasksWithNoCustomer** | **Boolean**| Optional: Include the activities that don&#39;t have customer. Default is true. | [optional] [default to true]
 **projectGuids** | [**[String]**](String.md)| Optional: ID of the project for the activities to be fetched. If not provided, returns for all projects. Default all. | [optional] 
 **includeTasksWithNoProject** | **Boolean**| Optional: Include the activities that don&#39;t have project. Default is true. | [optional] [default to true]
 **projectBusinessUnitGuids** | [**[String]**](String.md)| Optional: ID of the business unit of the project based on which activities should be filtered. If not provided, returns for all business units. Default all. | [optional] 
 **projectOwnerGuids** | [**[String]**](String.md)| Optional: ID of the project manager. If not provided, returns for all project managers. Default all. | [optional] 
 **userGuids** | [**[String]**](String.md)| Optional: ID of the user for the activities to be fetched. If not provided, returns for all users. Default all. | [optional] 
 **includeAsMember** | **Boolean**| Optional: Include the activities that the user is a member. Effective if userGuid is provided. Default is to not include. | [optional] [default to false]
 **userKeywordGuids** | [**[String]**](String.md)| Optional: User keyword Ids of activity owner to search for. | [optional] 
 **startDateTime** | **Date**| Optional: starting date and time from which to get the activities in user&#39;s timezone. Finds all activities that end after the date time. Format \&quot;2017-04-12T13%3A20%3A00%2b02%3A00\&quot;. Default all. | [optional] 
 **endDateTime** | **Date**| Optional: ending date and time to which to get the activities in user&#39;s timezone. Finds all activities that start before or on the date time. Format \&quot;2017-04-12T13%3A20%3A00%2b02%3A00\&quot;. Default all. If activities for one day are fetched, give start date time with time as 00:00 with the offset of the timezone and end time as 23:59:59 with the offset. | [optional] 
 **projectTaskStatusGuids** | [**[String]**](String.md)| Optional: ID of the project task status. Default all. | [optional] 
 **phaseGuids** | [**[String]**](String.md)| Optional: ID of the phase for the activities to be fetched. If not provided, returns for all phases. Default all. | [optional] 
 **includeSubPhases** | **Boolean**| Optional: If one phase guid is given include activities also from sub phases. If multiple phase guids are given, returns activities only for those regardless of this parameter. Default false. | [optional] [default to false]
 **contactGuids** | [**[String]**](String.md)| Optional: ID of the contact for the activities to be fetched. If not provided, returns for all users. Default all. | [optional] 
 **hasDuration** | **Boolean**| Optional: has duration flag for the activity. Default all. | [optional] 
 **hasHours** | **Boolean**| Optional: has any work hour entries associated with the activity. Default all. | [optional] 
 **isUnassigned** | **Boolean**| Optional: is the activity unassigned. Default all. | [optional] 
 **changedSince** | **Date**| Optional: Get activities that have been added or changed after this date time (greater or equal). | [optional] 
 **useStrictStartAndEndDateTime** | **Boolean**| Optional: If given as true returns activities that start after start time and end before end time. If given as false returns activities that start before end time and end after start time. Limit are included in both cases. Default false. | [optional] [default to false]
 **activityTypeGuids** | [**[String]**](String.md)| Optional: ID of the project activity type. Default all. | [optional] 
 **recurrenceType** | [**RecurrenceType**](.md)| Optional: Type of the recurrence. Default returns all not recurring activities, instances and exceptions. (None &#x3D; not recurring activity) | [optional] 

### Return type

[**[ActivityModel]**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activitiesGetActivity

> ActivityModel activitiesGetActivity(guid)

Get activity by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesReadApi();
let guid = "guid_example"; // String | GUID used to get the activity.
apiInstance.activitiesGetActivity(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the activity. | 

### Return type

[**ActivityModel**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityParticipantsGetActivityParticipant

> ActivityParticipantModel activityParticipantsGetActivityParticipant(guid)

Get activity participant

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesReadApi();
let guid = "guid_example"; // String | ID of the participant
apiInstance.activityParticipantsGetActivityParticipant(guid, (error, data, response) => {
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
 **guid** | **String**| ID of the participant | 

### Return type

[**ActivityParticipantModel**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityParticipantsGetActivityParticipants

> [ActivityParticipantModel] activityParticipantsGetActivityParticipants(activityGuid)

Get participants for an activity

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

let apiInstance = new SeveraPublicRestApiDocumentation.ActivitiesReadApi();
let activityGuid = "activityGuid_example"; // String | ID of the activity
apiInstance.activityParticipantsGetActivityParticipants(activityGuid, (error, data, response) => {
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
 **activityGuid** | **String**| ID of the activity | 

### Return type

[**[ActivityParticipantModel]**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

