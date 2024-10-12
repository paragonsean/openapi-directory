# GoToWebinar.RegistrantsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRegistrant**](RegistrantsApi.md#createRegistrant) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/registrants | Create registrant
[**deleteRegistrant**](RegistrantsApi.md#deleteRegistrant) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey}/registrants/{registrantKey} | Delete registrant
[**getAllRegistrantsForWebinar**](RegistrantsApi.md#getAllRegistrantsForWebinar) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/registrants | Get registrants
[**getRegistrant**](RegistrantsApi.md#getRegistrant) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/registrants/{registrantKey} | Get registrant
[**getRegistrationFields**](RegistrantsApi.md#getRegistrationFields) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/registrants/fields | Get registration fields



## createRegistrant

> RegistrantCreated createRegistrant(authorization, organizerKey, webinarKey, body, opts)

Create registrant

Register an attendee for a scheduled webinar. The response contains the registrantKey and join URL for the registrant. An email will be sent to the registrant unless the organizer turns off the confirmation email setting from the GoToWebinar website. Please note that you must provide all required fields including custom fields defined during the webinar creation. Use the API call &#39;Get registration fields&#39; to get a list of all fields, if they are required, and their possible values. At this time there are two versions of the &#39;Create Registrant&#39; call. The first version only accepts firstName, lastName, and email and ignores all other fields. If you have custom fields or want to capture additional information this version won&#39;t work for you. The second version allows you to pass all required and optional fields, including custom fields defined when creating the webinar. To use the second version you must pass the header value &#39;Accept: application/vnd.citrix.g2wapi-v1.1+json&#39; instead of &#39;Accept: application/json&#39;. Leaving this header out results in the first version of the API call.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.RegistrantsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let body = new GoToWebinar.RegistrantFields(); // RegistrantFields | The registrant details. To get all possible values run the API call 'Get registration fields' which is also part of this documentation.
let opts = {
  'accept': "accept_example", // String | Set to 'application/vnd.citrix.g2wapi-v1.1+json' to make a registration using fields (custom or default) additional to the basic ones.
  'resendConfirmation': true // Boolean | Indicates whether the confirmation email should be resent when a registrant is re-registered. The default value is false.
};
apiInstance.createRegistrant(authorization, organizerKey, webinarKey, body, opts, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **webinarKey** | **Number**| The key of the webinar | 
 **body** | [**RegistrantFields**](RegistrantFields.md)| The registrant details. To get all possible values run the API call &#39;Get registration fields&#39; which is also part of this documentation. | 
 **accept** | **String**| Set to &#39;application/vnd.citrix.g2wapi-v1.1+json&#39; to make a registration using fields (custom or default) additional to the basic ones. | [optional] 
 **resendConfirmation** | **Boolean**| Indicates whether the confirmation email should be resent when a registrant is re-registered. The default value is false. | [optional] 

### Return type

[**RegistrantCreated**](RegistrantCreated.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRegistrant

> deleteRegistrant(authorization, organizerKey, webinarKey, registrantKey)

Delete registrant

Removes a webinar registrant from current registrations for the specified webinar. The webinar must be a scheduled, future webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.RegistrantsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let registrantKey = 789; // Number | The key of the registrant
apiInstance.deleteRegistrant(authorization, organizerKey, webinarKey, registrantKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **webinarKey** | **Number**| The key of the webinar | 
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllRegistrantsForWebinar

> [Registrant] getAllRegistrantsForWebinar(authorization, organizerKey, webinarKey)

Get registrants

Retrieve registration details for all registrants of a specific webinar. Registrant details will not include all fields captured when creating the registrant. To see all data, use the API call &#39;Get Registrant&#39;. Registrants can have one of the following states; &lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval), &lt;br&gt;APPROVED - registrant registered and is approved, and &lt;br&gt;DENIED - registrant registered and was denied.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.RegistrantsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getAllRegistrantsForWebinar(authorization, organizerKey, webinarKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **webinarKey** | **Number**| The key of the webinar | 

### Return type

[**[Registrant]**](Registrant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegistrant

> RegistrantDetailed getRegistrant(authorization, organizerKey, webinarKey, registrantKey)

Get registrant

Retrieve registration details for a specific registrant.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.RegistrantsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let registrantKey = 789; // Number | The key of the registrant
apiInstance.getRegistrant(authorization, organizerKey, webinarKey, registrantKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **webinarKey** | **Number**| The key of the webinar | 
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

[**RegistrantDetailed**](RegistrantDetailed.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegistrationFields

> RegistrationFields getRegistrationFields(authorization, organizerKey, webinarKey)

Get registration fields

Retrieve required, optional registration, and custom questions for a specified webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.RegistrantsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getRegistrationFields(authorization, organizerKey, webinarKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **webinarKey** | **Number**| The key of the webinar | 

### Return type

[**RegistrationFields**](RegistrationFields.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

