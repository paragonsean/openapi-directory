# InfluxOssApiService.NotificationRulesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNotificationRule**](NotificationRulesApi.md#createNotificationRule) | **POST** /notificationRules | Add a notification rule
[**deleteNotificationRulesID**](NotificationRulesApi.md#deleteNotificationRulesID) | **DELETE** /notificationRules/{ruleID} | Delete a notification rule
[**deleteNotificationRulesIDLabelsID**](NotificationRulesApi.md#deleteNotificationRulesIDLabelsID) | **DELETE** /notificationRules/{ruleID}/labels/{labelID} | Delete label from a notification rule
[**getNotificationRules**](NotificationRulesApi.md#getNotificationRules) | **GET** /notificationRules | List all notification rules
[**getNotificationRulesID**](NotificationRulesApi.md#getNotificationRulesID) | **GET** /notificationRules/{ruleID} | Retrieve a notification rule
[**getNotificationRulesIDLabels**](NotificationRulesApi.md#getNotificationRulesIDLabels) | **GET** /notificationRules/{ruleID}/labels | List all labels for a notification rule
[**patchNotificationRulesID**](NotificationRulesApi.md#patchNotificationRulesID) | **PATCH** /notificationRules/{ruleID} | Update a notification rule
[**postNotificationRuleIDLabels**](NotificationRulesApi.md#postNotificationRuleIDLabels) | **POST** /notificationRules/{ruleID}/labels | Add a label to a notification rule
[**putNotificationRulesID**](NotificationRulesApi.md#putNotificationRulesID) | **PUT** /notificationRules/{ruleID} | Update a notification rule



## createNotificationRule

> NotificationRule createNotificationRule(postNotificationRule)

Add a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let postNotificationRule = new InfluxOssApiService.PostNotificationRule(); // PostNotificationRule | Notification rule to create
apiInstance.createNotificationRule(postNotificationRule, (error, data, response) => {
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
 **postNotificationRule** | [**PostNotificationRule**](PostNotificationRule.md)| Notification rule to create | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNotificationRulesID

> deleteNotificationRulesID(ruleID, opts)

Delete a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteNotificationRulesID(ruleID, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNotificationRulesIDLabelsID

> deleteNotificationRulesIDLabelsID(ruleID, labelID, opts)

Delete label from a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let labelID = "labelID_example"; // String | The ID of the label to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteNotificationRulesIDLabelsID(ruleID, labelID, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **labelID** | **String**| The ID of the label to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationRules

> NotificationRules getNotificationRules(orgID, opts)

List all notification rules

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let orgID = "orgID_example"; // String | Only show notification rules that belong to a specific organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20, // Number | 
  'checkID': "checkID_example", // String | Only show notifications that belong to the specific check ID.
  'tag': "env:prod" // String | Only return notification rules that \"would match\" statuses which contain the tag key value pairs provided.
};
apiInstance.getNotificationRules(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| Only show notification rules that belong to a specific organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **checkID** | **String**| Only show notifications that belong to the specific check ID. | [optional] 
 **tag** | **String**| Only return notification rules that \&quot;would match\&quot; statuses which contain the tag key value pairs provided. | [optional] 

### Return type

[**NotificationRules**](NotificationRules.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationRulesID

> NotificationRule getNotificationRulesID(ruleID, opts)

Retrieve a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getNotificationRulesID(ruleID, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationRulesIDLabels

> LabelsResponse getNotificationRulesIDLabels(ruleID, opts)

List all labels for a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getNotificationRulesIDLabels(ruleID, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchNotificationRulesID

> NotificationRule patchNotificationRulesID(ruleID, notificationRuleUpdate, opts)

Update a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let notificationRuleUpdate = new InfluxOssApiService.NotificationRuleUpdate(); // NotificationRuleUpdate | Notification rule update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchNotificationRulesID(ruleID, notificationRuleUpdate, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **notificationRuleUpdate** | [**NotificationRuleUpdate**](NotificationRuleUpdate.md)| Notification rule update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNotificationRuleIDLabels

> LabelResponse postNotificationRuleIDLabels(ruleID, labelMapping, opts)

Add a label to a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postNotificationRuleIDLabels(ruleID, labelMapping, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putNotificationRulesID

> NotificationRule putNotificationRulesID(ruleID, notificationRule, opts)

Update a notification rule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.NotificationRulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let notificationRule = new InfluxOssApiService.NotificationRule(); // NotificationRule | Notification rule update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putNotificationRulesID(ruleID, notificationRule, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **notificationRule** | [**NotificationRule**](NotificationRule.md)| Notification rule update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

