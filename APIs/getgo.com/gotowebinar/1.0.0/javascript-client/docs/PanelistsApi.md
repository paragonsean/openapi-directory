# GoToWebinar.PanelistsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPanelists**](PanelistsApi.md#createPanelists) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/panelists | Create Panelists
[**deleteWebinarPanelist**](PanelistsApi.md#deleteWebinarPanelist) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey}/panelists/{panelistKey} | Delete webinar panelist
[**getPanelists**](PanelistsApi.md#getPanelists) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/panelists | Get webinar panelists
[**resendPanelistInvitation**](PanelistsApi.md#resendPanelistInvitation) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/panelists/{panelistKey}/resendInvitation | Resend panelist invitation



## createPanelists

> [CreatedPanelist] createPanelists(authorization, organizerKey, webinarKey, body)

Create Panelists

Create panelists for a specified webinar

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.PanelistsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let body = [new GoToWebinar.PanelistReqCreate()]; // [PanelistReqCreate] | Array of panelists
apiInstance.createPanelists(authorization, organizerKey, webinarKey, body, (error, data, response) => {
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
 **body** | [**[PanelistReqCreate]**](PanelistReqCreate.md)| Array of panelists | 

### Return type

[**[CreatedPanelist]**](CreatedPanelist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWebinarPanelist

> deleteWebinarPanelist(authorization, organizerKey, webinarKey, panelistKey)

Delete webinar panelist

Removes a webinar panelist.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.PanelistsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let panelistKey = 789; // Number | The key of the webinar panelist
apiInstance.deleteWebinarPanelist(authorization, organizerKey, webinarKey, panelistKey, (error, data, response) => {
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
 **panelistKey** | **Number**| The key of the webinar panelist | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPanelists

> [Panelist] getPanelists(authorization, organizerKey, webinarKey)

Get webinar panelists

Retrieves all the panelists for a specific webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.PanelistsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getPanelists(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**[Panelist]**](Panelist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendPanelistInvitation

> resendPanelistInvitation(authorization, organizerKey, webinarKey, panelistKey)

Resend panelist invitation

Resend the panelist invitation email.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.PanelistsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let panelistKey = 789; // Number | The key of the webinar panelist
apiInstance.resendPanelistInvitation(authorization, organizerKey, webinarKey, panelistKey, (error, data, response) => {
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
 **panelistKey** | **Number**| The key of the webinar panelist | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

