# AgentOsApiV3DiaryCallGroup.DiaryControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diaryControllerAddFeedback**](DiaryControllerApi.md#diaryControllerAddFeedback) | **POST** /v3/diary/{shortName}/appointment/feedback | Submit appointment feedback
[**diaryControllerCancelAppointment**](DiaryControllerApi.md#diaryControllerCancelAppointment) | **PATCH** /v3/diary/{shortName}/appointment/{appointmentID}/cancel | Cancel an existing appointment using its unique identifier
[**diaryControllerDeleteAppointment**](DiaryControllerApi.md#diaryControllerDeleteAppointment) | **DELETE** /v3/diary/{shortName}/appointment | Delete an existing appointment using its unique identifier
[**diaryControllerGetAllocations**](DiaryControllerApi.md#diaryControllerGetAllocations) | **GET** /v3/diary/{shortName}/allocations | Get a list of all available allocations for a date + 7 days for a specified appointment type
[**diaryControllerGetAppointment**](DiaryControllerApi.md#diaryControllerGetAppointment) | **GET** /v3/diary/{shortName}/appointment | Get an appointment by ID
[**diaryControllerGetAppointmentTypes**](DiaryControllerApi.md#diaryControllerGetAppointmentTypes) | **GET** /v3/diary/{shortName}/appointmenttypes | A collection of all diary appointment types
[**diaryControllerGetAppointmentsBetweenDates**](DiaryControllerApi.md#diaryControllerGetAppointmentsBetweenDates) | **GET** /v3/diary/{shortName}/appointmentsbetweendates | A collection of diary appointments linked to a company filtered between specific dates and by appointment type
[**diaryControllerGetRecurringAppointments**](DiaryControllerApi.md#diaryControllerGetRecurringAppointments) | **GET** /v3/diary/{shortName}/recurringappointment | Retrieves all recurring appointments:-
[**diaryControllerPostAppointment**](DiaryControllerApi.md#diaryControllerPostAppointment) | **POST** /v3/diary/{shortName}/appointment | Post an appointment into a valid diary allocation
[**diaryControllerPutAppointment**](DiaryControllerApi.md#diaryControllerPutAppointment) | **PUT** /v3/diary/{shortName}/appointment | Update an existing appointment using its unique identifier
[**diaryControllerSearchGuest**](DiaryControllerApi.md#diaryControllerSearchGuest) | **GET** /v3/diary/{shortname}/{branchID}/guest/search | Match Guest Parameters with existing applicants



## diaryControllerAddFeedback

> String diaryControllerAddFeedback(shortName, feedbackSubmissionModel)

Submit appointment feedback

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let feedbackSubmissionModel = new AgentOsApiV3DiaryCallGroup.FeedbackSubmissionModel(); // FeedbackSubmissionModel | Feedback submission model
apiInstance.diaryControllerAddFeedback(shortName, feedbackSubmissionModel, (error, data, response) => {
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
 **feedbackSubmissionModel** | [**FeedbackSubmissionModel**](FeedbackSubmissionModel.md)| Feedback submission model | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerCancelAppointment

> String diaryControllerCancelAppointment(shortName, appointmentID)

Cancel an existing appointment using its unique identifier

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let appointmentID = "appointmentID_example"; // String | The unique appointment id
apiInstance.diaryControllerCancelAppointment(shortName, appointmentID, (error, data, response) => {
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
 **appointmentID** | **String**| The unique appointment id | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerDeleteAppointment

> String diaryControllerDeleteAppointment(shortName, appointmentID)

Delete an existing appointment using its unique identifier

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let appointmentID = "appointmentID_example"; // String | The unique appointment id
apiInstance.diaryControllerDeleteAppointment(shortName, appointmentID, (error, data, response) => {
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
 **appointmentID** | **String**| The unique appointment id | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerGetAllocations

> [DiaryBookingModel] diaryControllerGetAllocations(shortName, preferredDate, appointmentType, opts)

Get a list of all available allocations for a date + 7 days for a specified appointment type

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let preferredDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search from
let appointmentType = "appointmentType_example"; // String | The unique appointment type identifier
let opts = {
  'lettings': true, // Boolean | Sales or Lettings property?
  'propertyIdentifier': "propertyIdentifier_example", // String | The unique property identifier (Sales or Lettings) determines branch and property type
  'branchID': "branchID_example" // String | Branch ID to check appointments (required if no property submitted)
};
apiInstance.diaryControllerGetAllocations(shortName, preferredDate, appointmentType, opts, (error, data, response) => {
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
 **preferredDate** | **Date**| The date to search from | 
 **appointmentType** | **String**| The unique appointment type identifier | 
 **lettings** | **Boolean**| Sales or Lettings property? | [optional] 
 **propertyIdentifier** | **String**| The unique property identifier (Sales or Lettings) determines branch and property type | [optional] 
 **branchID** | **String**| Branch ID to check appointments (required if no property submitted) | [optional] 

### Return type

[**[DiaryBookingModel]**](DiaryBookingModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerGetAppointment

> DiaryAppointmentModel diaryControllerGetAppointment(shortName, appointmentID)

Get an appointment by ID

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | Company short name
let appointmentID = "appointmentID_example"; // String | Appointment ID
apiInstance.diaryControllerGetAppointment(shortName, appointmentID, (error, data, response) => {
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
 **shortName** | **String**| Company short name | 
 **appointmentID** | **String**| Appointment ID | 

### Return type

[**DiaryAppointmentModel**](DiaryAppointmentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## diaryControllerGetAppointmentTypes

> DiaryAppointmentTypeModelResults diaryControllerGetAppointmentTypes(shortName, offset, count)

A collection of all diary appointment types

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.diaryControllerGetAppointmentTypes(shortName, offset, count, (error, data, response) => {
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
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**DiaryAppointmentTypeModelResults**](DiaryAppointmentTypeModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerGetAppointmentsBetweenDates

> DiaryAppointmentModelResults diaryControllerGetAppointmentsBetweenDates(shortName, branchID, startDate, endDate, appointmentTypesToSearch, offset, count)

A collection of diary appointments linked to a company filtered between specific dates and by appointment type

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The search from date
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The search to date
let appointmentTypesToSearch = ["null"]; // [String] | The appointment IDs to search for
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.diaryControllerGetAppointmentsBetweenDates(shortName, branchID, startDate, endDate, appointmentTypesToSearch, offset, count, (error, data, response) => {
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
 **branchID** | **String**| The unique ID of the Branch | 
 **startDate** | **Date**| The search from date | 
 **endDate** | **Date**| The search to date | 
 **appointmentTypesToSearch** | [**[String]**](String.md)| The appointment IDs to search for | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**DiaryAppointmentModelResults**](DiaryAppointmentModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerGetRecurringAppointments

> DiaryAppointmentModelResults diaryControllerGetRecurringAppointments(shortName, branchID, appointmentTypesToSearch, offset, count)

Retrieves all recurring appointments:-

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let appointmentTypesToSearch = ["null"]; // [String] | The appointment IDs to search for
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.diaryControllerGetRecurringAppointments(shortName, branchID, appointmentTypesToSearch, offset, count, (error, data, response) => {
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
 **branchID** | **String**| The unique ID of the Branch | 
 **appointmentTypesToSearch** | [**[String]**](String.md)| The appointment IDs to search for | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**DiaryAppointmentModelResults**](DiaryAppointmentModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerPostAppointment

> String diaryControllerPostAppointment(shortName, propertyIdentifier, diaryAppointmentDetails, opts)

Post an appointment into a valid diary allocation

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let propertyIdentifier = ["null"]; // [String] | The unique property identifier (Sales or Lettings)
let diaryAppointmentDetails = new AgentOsApiV3DiaryCallGroup.DiaryAppointmentDetails(); // DiaryAppointmentDetails | The appointment details model
let opts = {
  'lettings': true // Boolean | Sales or Lettings property?
};
apiInstance.diaryControllerPostAppointment(shortName, propertyIdentifier, diaryAppointmentDetails, opts, (error, data, response) => {
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
 **propertyIdentifier** | [**[String]**](String.md)| The unique property identifier (Sales or Lettings) | 
 **diaryAppointmentDetails** | [**DiaryAppointmentDetails**](DiaryAppointmentDetails.md)| The appointment details model | 
 **lettings** | **Boolean**| Sales or Lettings property? | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerPutAppointment

> String diaryControllerPutAppointment(shortName, appointmentID, diaryAppointmentDetails, opts)

Update an existing appointment using its unique identifier

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let appointmentID = "appointmentID_example"; // String | The unique appointment id
let diaryAppointmentDetails = new AgentOsApiV3DiaryCallGroup.DiaryAppointmentDetails(); // DiaryAppointmentDetails | The appointment details model
let opts = {
  'lettings': true, // Boolean | Sales or Lettings property?
  'allowMarketingCorrespondence': true // Boolean | Sales or Lettings property?
};
apiInstance.diaryControllerPutAppointment(shortName, appointmentID, diaryAppointmentDetails, opts, (error, data, response) => {
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
 **appointmentID** | **String**| The unique appointment id | 
 **diaryAppointmentDetails** | [**DiaryAppointmentDetails**](DiaryAppointmentDetails.md)| The appointment details model | 
 **lettings** | **Boolean**| Sales or Lettings property? | [optional] 
 **allowMarketingCorrespondence** | **Boolean**| Sales or Lettings property? | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## diaryControllerSearchGuest

> GuestDiaryParametersResultsModel diaryControllerSearchGuest(shortname, branchID, forename, emailaddress, surname, offset, count)

Match Guest Parameters with existing applicants

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
let shortname = "shortname_example"; // String | 
let branchID = "branchID_example"; // String | 
let forename = "forename_example"; // String | 
let emailaddress = "emailaddress_example"; // String | 
let surname = "surname_example"; // String | 
let offset = 56; // Number | 
let count = 56; // Number | 
apiInstance.diaryControllerSearchGuest(shortname, branchID, forename, emailaddress, surname, offset, count, (error, data, response) => {
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
 **shortname** | **String**|  | 
 **branchID** | **String**|  | 
 **forename** | **String**|  | 
 **emailaddress** | **String**|  | 
 **surname** | **String**|  | 
 **offset** | **Number**|  | 
 **count** | **Number**|  | 

### Return type

[**GuestDiaryParametersResultsModel**](GuestDiaryParametersResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

