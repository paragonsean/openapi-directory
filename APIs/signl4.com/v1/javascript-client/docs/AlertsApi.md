# Signl4Api.AlertsApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsAcknowledgeAllPost**](AlertsApi.md#alertsAcknowledgeAllPost) | **POST** /alerts/acknowledgeAll | Confirms all visible alerts
[**alertsAcknowledgeMultiplePost**](AlertsApi.md#alertsAcknowledgeMultiplePost) | **POST** /alerts/acknowledgeMultiple | Acknowlegde multiple alerts
[**alertsAlertIdAcknowledgePost**](AlertsApi.md#alertsAlertIdAcknowledgePost) | **POST** /alerts/{alertId}/acknowledge | Acknowledge an alert
[**alertsAlertIdAnnotatePost**](AlertsApi.md#alertsAlertIdAnnotatePost) | **POST** /alerts/{alertId}/annotate | Annotate Alert
[**alertsAlertIdAnnotationsGet**](AlertsApi.md#alertsAlertIdAnnotationsGet) | **GET** /alerts/{alertId}/annotations | Get annotations of an alert
[**alertsAlertIdAttachmentsAttachmentIdGet**](AlertsApi.md#alertsAlertIdAttachmentsAttachmentIdGet) | **GET** /alerts/{alertId}/attachments/{attachmentId} | Gets a specified attachment of a specified alert.
[**alertsAlertIdAttachmentsGet**](AlertsApi.md#alertsAlertIdAttachmentsGet) | **GET** /alerts/{alertId}/attachments | Get attachments of an alert
[**alertsAlertIdClosePost**](AlertsApi.md#alertsAlertIdClosePost) | **POST** /alerts/{alertId}/close | Close an alert
[**alertsAlertIdGet**](AlertsApi.md#alertsAlertIdGet) | **GET** /alerts/{alertId} | Get Alert
[**alertsAlertIdNotificationsGet**](AlertsApi.md#alertsAlertIdNotificationsGet) | **GET** /alerts/{alertId}/notifications | Get alert notifications
[**alertsAlertIdOverviewGet**](AlertsApi.md#alertsAlertIdOverviewGet) | **GET** /alerts/{alertId}/overview | Get an overview alert.
[**alertsAlertIdUndoAcknowledgePost**](AlertsApi.md#alertsAlertIdUndoAcknowledgePost) | **POST** /alerts/{alertId}/undoAcknowledge | Undo the acknowledgement of an alert.
[**alertsAlertIdUndoClosePost**](AlertsApi.md#alertsAlertIdUndoClosePost) | **POST** /alerts/{alertId}/undoClose | Undo the closure of an alert.
[**alertsCloseAllPost**](AlertsApi.md#alertsCloseAllPost) | **POST** /alerts/closeAll | Close all acknowledged alerts.
[**alertsCloseMultiplePost**](AlertsApi.md#alertsCloseMultiplePost) | **POST** /alerts/closeMultiple | Close multiple alerts
[**alertsPagedPost**](AlertsApi.md#alertsPagedPost) | **POST** /alerts/paged | Gets alerts paged
[**alertsPost**](AlertsApi.md#alertsPost) | **POST** /alerts | Trigger Alert
[**alertsReportGet**](AlertsApi.md#alertsReportGet) | **GET** /alerts/report | Get Alert Report
[**alertsUndoAcknowledgeMultiplePost**](AlertsApi.md#alertsUndoAcknowledgeMultiplePost) | **POST** /alerts/undoAcknowledgeMultiple | Queue undo of multiple acknowledgments.
[**alertsUndoCloseMultiplePost**](AlertsApi.md#alertsUndoCloseMultiplePost) | **POST** /alerts/undoCloseMultiple | Withdraw closure of multiple alerts



## alertsAcknowledgeAllPost

> alertsAcknowledgeAllPost(opts)

Confirms all visible alerts

This method confirms all unhandled alerts your team currently has by a specific user.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'userId': "userId_example", // String | User ID of the user to be used to acknowledge the alarms.
  'changeAlertStatusFilterInfo': new Signl4Api.ChangeAlertStatusFilterInfo() // ChangeAlertStatusFilterInfo | 
};
apiInstance.alertsAcknowledgeAllPost(opts, (error, data, response) => {
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
 **userId** | **String**| User ID of the user to be used to acknowledge the alarms. | [optional] 
 **changeAlertStatusFilterInfo** | [**ChangeAlertStatusFilterInfo**](ChangeAlertStatusFilterInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsAcknowledgeMultiplePost

> alertsAcknowledgeMultiplePost(opts)

Acknowlegde multiple alerts

This method confirms all alerts provided.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'changeAlertStatusMultipleInfo': new Signl4Api.ChangeAlertStatusMultipleInfo() // ChangeAlertStatusMultipleInfo | 
};
apiInstance.alertsAcknowledgeMultiplePost(opts, (error, data, response) => {
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
 **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdAcknowledgePost

> AlertInfo alertsAlertIdAcknowledgePost(alertId, opts)

Acknowledge an alert

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id to acknowledge an alert.
let opts = {
  'changeAlertStatusInfo': new Signl4Api.ChangeAlertStatusInfo() // ChangeAlertStatusInfo | 
};
apiInstance.alertsAlertIdAcknowledgePost(alertId, opts, (error, data, response) => {
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
 **alertId** | **String**| Id to acknowledge an alert. | 
 **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] 

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdAnnotatePost

> AlertAnnotationInfo alertsAlertIdAnnotatePost(alertId, opts)

Annotate Alert

Annotates an alert by given Annotation Info.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the alert to annotate.
let opts = {
  'alertAnnotationInfo': new Signl4Api.AlertAnnotationInfo() // AlertAnnotationInfo | Annotation Information.
};
apiInstance.alertsAlertIdAnnotatePost(alertId, opts, (error, data, response) => {
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
 **alertId** | **String**| Id of the alert to annotate. | 
 **alertAnnotationInfo** | [**AlertAnnotationInfo**](AlertAnnotationInfo.md)| Annotation Information. | [optional] 

### Return type

[**AlertAnnotationInfo**](AlertAnnotationInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdAnnotationsGet

> [AlertAnnotationInfo] alertsAlertIdAnnotationsGet(alertId)

Get annotations of an alert

Get annotations of an alert by id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the requested Alert.
apiInstance.alertsAlertIdAnnotationsGet(alertId, (error, data, response) => {
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
 **alertId** | **String**| Id of the requested Alert. | 

### Return type

[**[AlertAnnotationInfo]**](AlertAnnotationInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdAttachmentsAttachmentIdGet

> File alertsAlertIdAttachmentsAttachmentIdGet(alertId, attachmentId, opts)

Gets a specified attachment of a specified alert.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the alert that contains the wanted attachment.
let attachmentId = "attachmentId_example"; // String | Id of the attachment, that you want to retrieve.
let opts = {
  'width': 56, // Number | Optional parameter defining the wanted width of the picture that is retrieved.
  'height': 56, // Number | Optional parameter defining the wanted height of the picture that is retrieved.
  'scale': true // Boolean | Optional parameter defining whether it's wanted to scale the retrieved image. Default is set to  true.
};
apiInstance.alertsAlertIdAttachmentsAttachmentIdGet(alertId, attachmentId, opts, (error, data, response) => {
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
 **alertId** | **String**| Id of the alert that contains the wanted attachment. | 
 **attachmentId** | **String**| Id of the attachment, that you want to retrieve. | 
 **width** | **Number**| Optional parameter defining the wanted width of the picture that is retrieved. | [optional] 
 **height** | **Number**| Optional parameter defining the wanted height of the picture that is retrieved. | [optional] 
 **scale** | **Boolean**| Optional parameter defining whether it&#39;s wanted to scale the retrieved image. Default is set to  true. | [optional] [default to true]

### Return type

**File**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdAttachmentsGet

> [AlertAttachmentInfo] alertsAlertIdAttachmentsGet(alertId)

Get attachments of an alert

Get attachments of an alert by id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the requested Alert.
apiInstance.alertsAlertIdAttachmentsGet(alertId, (error, data, response) => {
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
 **alertId** | **String**| Id of the requested Alert. | 

### Return type

[**[AlertAttachmentInfo]**](AlertAttachmentInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdClosePost

> AlertInfo alertsAlertIdClosePost(alertId, opts)

Close an alert

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id to acknowledge an alert.
let opts = {
  'changeAlertStatusInfo': new Signl4Api.ChangeAlertStatusInfo() // ChangeAlertStatusInfo | 
};
apiInstance.alertsAlertIdClosePost(alertId, opts, (error, data, response) => {
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
 **alertId** | **String**| Id to acknowledge an alert. | 
 **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] 

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdGet

> AlertInfo alertsAlertIdGet(alertId)

Get Alert

Gets an alert by id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the requested Alert.
apiInstance.alertsAlertIdGet(alertId, (error, data, response) => {
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
 **alertId** | **String**| Id of the requested Alert. | 

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdNotificationsGet

> [AlertNotificationInfo] alertsAlertIdNotificationsGet(alertId)

Get alert notifications

Get notifications of all users by alert id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the requested Alert.
apiInstance.alertsAlertIdNotificationsGet(alertId, (error, data, response) => {
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
 **alertId** | **String**| Id of the requested Alert. | 

### Return type

[**[AlertNotificationInfo]**](AlertNotificationInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdOverviewGet

> OverviewAlert alertsAlertIdOverviewGet(alertId)

Get an overview alert.

Get overview alert by id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | Id of the requested Alert.
apiInstance.alertsAlertIdOverviewGet(alertId, (error, data, response) => {
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
 **alertId** | **String**| Id of the requested Alert. | 

### Return type

[**OverviewAlert**](OverviewAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdUndoAcknowledgePost

> OverviewAlert alertsAlertIdUndoAcknowledgePost(alertId, opts)

Undo the acknowledgement of an alert.

This method tries to undo an alert acknowledgement.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | 
let opts = {
  'changeAlertStatusInfo': new Signl4Api.ChangeAlertStatusInfo() // ChangeAlertStatusInfo | 
};
apiInstance.alertsAlertIdUndoAcknowledgePost(alertId, opts, (error, data, response) => {
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
 **alertId** | **String**|  | 
 **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] 

### Return type

[**OverviewAlert**](OverviewAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsAlertIdUndoClosePost

> OverviewAlert alertsAlertIdUndoClosePost(alertId, opts)

Undo the closure of an alert.

This method tries to undo an alert close.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let alertId = "alertId_example"; // String | 
let opts = {
  'changeAlertStatusInfo': new Signl4Api.ChangeAlertStatusInfo() // ChangeAlertStatusInfo | 
};
apiInstance.alertsAlertIdUndoClosePost(alertId, opts, (error, data, response) => {
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
 **alertId** | **String**|  | 
 **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] 

### Return type

[**OverviewAlert**](OverviewAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsCloseAllPost

> alertsCloseAllPost(opts)

Close all acknowledged alerts.

This method closes all acknowledged alerts your team currently has.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'userId': "userId_example", // String | User ID of the user to be used to close the alarms.
  'changeAlertStatusFilterInfo': new Signl4Api.ChangeAlertStatusFilterInfo() // ChangeAlertStatusFilterInfo | 
};
apiInstance.alertsCloseAllPost(opts, (error, data, response) => {
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
 **userId** | **String**| User ID of the user to be used to close the alarms. | [optional] 
 **changeAlertStatusFilterInfo** | [**ChangeAlertStatusFilterInfo**](ChangeAlertStatusFilterInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsCloseMultiplePost

> alertsCloseMultiplePost(opts)

Close multiple alerts

This method closes all alerts provided.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'changeAlertStatusMultipleInfo': new Signl4Api.ChangeAlertStatusMultipleInfo() // ChangeAlertStatusMultipleInfo | 
};
apiInstance.alertsCloseMultiplePost(opts, (error, data, response) => {
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
 **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsPagedPost

> OverviewAlertPagedResultsPublic alertsPagedPost(opts)

Gets alerts paged

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'maxResults': 56, // Number | Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                  Number of alerts could be less if filtered but at least 1.
  'userId': "userId_example", // String | User ID of the user you want to get alerts for.
  'alertFilterPublic': new Signl4Api.AlertFilterPublic() // AlertFilterPublic | The filter defines which alerts are supposed to be retrieved.
};
apiInstance.alertsPagedPost(opts, (error, data, response) => {
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
 **maxResults** | **Number**| Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                  Number of alerts could be less if filtered but at least 1. | [optional] 
 **userId** | **String**| User ID of the user you want to get alerts for. | [optional] 
 **alertFilterPublic** | [**AlertFilterPublic**](AlertFilterPublic.md)| The filter defines which alerts are supposed to be retrieved. | [optional] 

### Return type

[**OverviewAlertPagedResultsPublic**](OverviewAlertPagedResultsPublic.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsPost

> AlertInfo alertsPost(opts)

Trigger Alert

Triggers a new alert for your team. All team members on duty will receive alert notifications.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'raiseAlertInfo': new Signl4Api.RaiseAlertInfo() // RaiseAlertInfo | Alert to raise.
};
apiInstance.alertsPost(opts, (error, data, response) => {
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
 **raiseAlertInfo** | [**RaiseAlertInfo**](RaiseAlertInfo.md)| Alert to raise. | [optional] 

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsReportGet

> AlertReport alertsReportGet(opts)

Get Alert Report

Returns information about the occurred alert volume in different time periods as well as information about the  response behaviour (amount of confirmed and unhandled alerts) of your team members.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'userId': "userId_example" // String | User ID of the user for whom you want a report.
};
apiInstance.alertsReportGet(opts, (error, data, response) => {
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
 **userId** | **String**| User ID of the user for whom you want a report. | [optional] 

### Return type

[**AlertReport**](AlertReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## alertsUndoAcknowledgeMultiplePost

> alertsUndoAcknowledgeMultiplePost(opts)

Queue undo of multiple acknowledgments.

This method tries to undo the acknowledgement of multiple alerts via a queue. The operation is handled in the background.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'changeAlertStatusMultipleInfo': new Signl4Api.ChangeAlertStatusMultipleInfo() // ChangeAlertStatusMultipleInfo | Configure which user should be undone for which alerts.
};
apiInstance.alertsUndoAcknowledgeMultiplePost(opts, (error, data, response) => {
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
 **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)| Configure which user should be undone for which alerts. | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## alertsUndoCloseMultiplePost

> alertsUndoCloseMultiplePost(opts)

Withdraw closure of multiple alerts

This method tries to undo multiple alert closes. The operation is handled in the background.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.AlertsApi();
let opts = {
  'changeAlertStatusMultipleInfo': new Signl4Api.ChangeAlertStatusMultipleInfo() // ChangeAlertStatusMultipleInfo | 
};
apiInstance.alertsUndoCloseMultiplePost(opts, (error, data, response) => {
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
 **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain

