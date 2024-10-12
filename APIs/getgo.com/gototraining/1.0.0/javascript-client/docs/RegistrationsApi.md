# GoToTraining.RegistrationsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelRegistration**](RegistrationsApi.md#cancelRegistration) | **DELETE** /organizers/{organizerKey}/trainings/{trainingKey}/registrants/{registrantKey} | Cancel Registration
[**getRegistrant**](RegistrationsApi.md#getRegistrant) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/registrants/{registrantKey} | Get Registrant
[**getRegistrants**](RegistrationsApi.md#getRegistrants) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/registrants | Get Training Registrants
[**registerForTraining**](RegistrationsApi.md#registerForTraining) | **POST** /organizers/{organizerKey}/trainings/{trainingKey}/registrants | Register for Training



## cancelRegistration

> cancelRegistration(authorization, organizerKey, trainingKey, registrantKey)

Cancel Registration

This call cancels a registration in a scheduled training for a specific registrant. If the registrant has paid for the training, a cancellation cannot be completed with this method; it must be completed on the external admin site. No notification is sent to the registrant or the organizer by default. The registrant can re-register if needed.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.RegistrationsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let trainingKey = 789; // Number | The key of the training
let registrantKey = 789; // Number | The key of the registrant
apiInstance.cancelRegistration(authorization, organizerKey, trainingKey, registrantKey, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **organizerKey** | **Number**| The key of the training organizer | 
 **trainingKey** | **Number**| The key of the training | 
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRegistrant

> Registrant getRegistrant(authorization, organizerKey, trainingKey, registrantKey)

Get Registrant

Retrieves details for specific registrant in a specific training. Registrants can be:&lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval)&lt;br&gt;APPROVED - registrant registered and is approved&lt;br&gt;DENIED - registrant registered and was not approved.&lt;br&gt;&lt;br&gt;IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.RegistrationsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let trainingKey = 789; // Number | The key of the training
let registrantKey = 789; // Number | The key of the registrant
apiInstance.getRegistrant(authorization, organizerKey, trainingKey, registrantKey, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **organizerKey** | **Number**| The key of the training organizer | 
 **trainingKey** | **Number**| The key of the training | 
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

[**Registrant**](Registrant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegistrants

> [Registrant] getRegistrants(authorization, organizerKey, trainingKey)

Get Training Registrants

Retrieves details on all registrants for a specific training. Registrants can be:&lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval)&lt;br&gt;APPROVED - registrant registered and is approved&lt;br&gt;DENIED - registrant registered and was not approved.&lt;br&gt;&lt;br&gt;IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.RegistrationsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let trainingKey = 789; // Number | The key of the training
apiInstance.getRegistrants(authorization, organizerKey, trainingKey, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **organizerKey** | **Number**| The key of the training organizer | 
 **trainingKey** | **Number**| The key of the training | 

### Return type

[**[Registrant]**](Registrant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerForTraining

> RegistrantCreated registerForTraining(authorization, organizerKey, trainingKey, body)

Register for Training

Registers one person, identified by a unique email address, for a training. Approval is automatic unless payment or approval is required. The response contains the Confirmation page URL and Join URL for the registrant. NOTE: If some registrants do not receive a confirmation email, the emails could be getting blocked by their email server due to spam filtering or a grey-listing setting.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.RegistrationsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let trainingKey = 789; // Number | The key of the training
let body = new GoToTraining.RegistrantReqCreate(); // RegistrantReqCreate | The details of the registrant to create
apiInstance.registerForTraining(authorization, organizerKey, trainingKey, body, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **organizerKey** | **Number**| The key of the training organizer | 
 **trainingKey** | **Number**| The key of the training | 
 **body** | [**RegistrantReqCreate**](RegistrantReqCreate.md)| The details of the registrant to create | 

### Return type

[**RegistrantCreated**](RegistrantCreated.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

