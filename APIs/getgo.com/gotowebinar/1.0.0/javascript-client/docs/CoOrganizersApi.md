# GoToWebinar.CoOrganizersApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCoorganizers**](CoOrganizersApi.md#createCoorganizers) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers | Create co-organizers
[**deleteCoorganizer**](CoOrganizersApi.md#deleteCoorganizer) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers/{coorganizerKey} | Delete co-organizer
[**getCoorganizers**](CoOrganizersApi.md#getCoorganizers) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers | Get co-organizers
[**resendCoorganizerInvitation**](CoOrganizersApi.md#resendCoorganizerInvitation) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers/{coorganizerKey}/resendInvitation | Resend invitation



## createCoorganizers

> [Coorganizer] createCoorganizers(authorization, organizerKey, webinarKey, body)

Create co-organizers

Creates co-organizers for the specified webinar. For co-organizers that have a GoToWebinar account you have to set the parameter &#39;external&#39; to &#39;false&#39;. In this case you have to pass the parameter &#39;organizerKey&#39; only. For co-organizers that have no GoToWebinar account you have to set the parameter &#39;external&#39; to &#39;true&#39;. In this case you have to pass the parameters &#39;givenName&#39; and &#39;email&#39;. Since there is no parameter for &#39;surname&#39; you should pass first and last name to the parameter &#39;givenName&#39;.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.CoOrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let body = [new GoToWebinar.CoorganizerReqCreate()]; // [CoorganizerReqCreate] | The co-organizer details
apiInstance.createCoorganizers(authorization, organizerKey, webinarKey, body, (error, data, response) => {
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
 **body** | [**[CoorganizerReqCreate]**](CoorganizerReqCreate.md)| The co-organizer details | 

### Return type

[**[Coorganizer]**](Coorganizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCoorganizer

> deleteCoorganizer(authorization, organizerKey, webinarKey, coorganizerKey, opts)

Delete co-organizer

Deletes an internal co-organizer specified by the coorganizerKey (memberKey).

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.CoOrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let coorganizerKey = 789; // Number | The key of the internal or external co-organizer (memberKey)
let opts = {
  'external': true // Boolean | By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to 'true'.
};
apiInstance.deleteCoorganizer(authorization, organizerKey, webinarKey, coorganizerKey, opts, (error, data, response) => {
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
 **coorganizerKey** | **Number**| The key of the internal or external co-organizer (memberKey) | 
 **external** | **Boolean**| By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to &#39;true&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCoorganizers

> [Coorganizer] getCoorganizers(authorization, organizerKey, webinarKey)

Get co-organizers

Returns the co-organizers for the specified webinar. The original organizer who created the webinar is filtered out of the list. If the webinar has no co-organizers, an empty array is returned. Co-organizers that do not have a GoToWebinar account are returned as external co-organizers. For those organizers no surname is returned.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.CoOrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getCoorganizers(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**[Coorganizer]**](Coorganizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendCoorganizerInvitation

> resendCoorganizerInvitation(authorization, organizerKey, webinarKey, coorganizerKey, opts)

Resend invitation

Resends an invitation email to the specified co-organizer

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.CoOrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let coorganizerKey = 789; // Number | The key of the internal or external co-organizer (memberKey)
let opts = {
  'external': true // Boolean | By default only internal co-organizers (with a GoToWebinar account) will retrieve the resent invitation email. If you want to use this call for external co-organizers you have to set this parameter to 'true'.
};
apiInstance.resendCoorganizerInvitation(authorization, organizerKey, webinarKey, coorganizerKey, opts, (error, data, response) => {
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
 **coorganizerKey** | **Number**| The key of the internal or external co-organizer (memberKey) | 
 **external** | **Boolean**| By default only internal co-organizers (with a GoToWebinar account) will retrieve the resent invitation email. If you want to use this call for external co-organizers you have to set this parameter to &#39;true&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

