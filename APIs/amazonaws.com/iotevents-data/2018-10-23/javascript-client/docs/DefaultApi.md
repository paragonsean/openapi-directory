# AwsIoTEventsData.DefaultApi

All URIs are relative to *http://data.iotevents.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchAcknowledgeAlarm**](DefaultApi.md#batchAcknowledgeAlarm) | **POST** /alarms/acknowledge | 
[**batchDeleteDetector**](DefaultApi.md#batchDeleteDetector) | **POST** /detectors/delete | 
[**batchDisableAlarm**](DefaultApi.md#batchDisableAlarm) | **POST** /alarms/disable | 
[**batchEnableAlarm**](DefaultApi.md#batchEnableAlarm) | **POST** /alarms/enable | 
[**batchPutMessage**](DefaultApi.md#batchPutMessage) | **POST** /inputs/messages | 
[**batchResetAlarm**](DefaultApi.md#batchResetAlarm) | **POST** /alarms/reset | 
[**batchSnoozeAlarm**](DefaultApi.md#batchSnoozeAlarm) | **POST** /alarms/snooze | 
[**batchUpdateDetector**](DefaultApi.md#batchUpdateDetector) | **POST** /detectors | 
[**describeAlarm**](DefaultApi.md#describeAlarm) | **GET** /alarms/{alarmModelName}/keyValues/ | 
[**describeDetector**](DefaultApi.md#describeDetector) | **GET** /detectors/{detectorModelName}/keyValues/ | 
[**listAlarms**](DefaultApi.md#listAlarms) | **GET** /alarms/{alarmModelName} | 
[**listDetectors**](DefaultApi.md#listDetectors) | **GET** /detectors/{detectorModelName} | 



## batchAcknowledgeAlarm

> BatchAcknowledgeAlarmResponse batchAcknowledgeAlarm(batchAcknowledgeAlarmRequest, opts)



Acknowledges one or more alarms. The alarms change to the &lt;code&gt;ACKNOWLEDGED&lt;/code&gt; state after you acknowledge them.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchAcknowledgeAlarmRequest = new AwsIoTEventsData.BatchAcknowledgeAlarmRequest(); // BatchAcknowledgeAlarmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchAcknowledgeAlarm(batchAcknowledgeAlarmRequest, opts, (error, data, response) => {
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
 **batchAcknowledgeAlarmRequest** | [**BatchAcknowledgeAlarmRequest**](BatchAcknowledgeAlarmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchAcknowledgeAlarmResponse**](BatchAcknowledgeAlarmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteDetector

> BatchDeleteDetectorResponse batchDeleteDetector(batchDeleteDetectorRequest, opts)



Deletes one or more detectors that were created. When a detector is deleted, its state will be cleared and the detector will be removed from the list of detectors. The deleted detector will no longer appear if referenced in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListDetectors.html\&quot;&gt;ListDetectors&lt;/a&gt; API call.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchDeleteDetectorRequest = new AwsIoTEventsData.BatchDeleteDetectorRequest(); // BatchDeleteDetectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteDetector(batchDeleteDetectorRequest, opts, (error, data, response) => {
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
 **batchDeleteDetectorRequest** | [**BatchDeleteDetectorRequest**](BatchDeleteDetectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteDetectorResponse**](BatchDeleteDetectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDisableAlarm

> BatchDisableAlarmResponse batchDisableAlarm(batchDisableAlarmRequest, opts)



Disables one or more alarms. The alarms change to the &lt;code&gt;DISABLED&lt;/code&gt; state after you disable them.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchDisableAlarmRequest = new AwsIoTEventsData.BatchDisableAlarmRequest(); // BatchDisableAlarmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDisableAlarm(batchDisableAlarmRequest, opts, (error, data, response) => {
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
 **batchDisableAlarmRequest** | [**BatchDisableAlarmRequest**](BatchDisableAlarmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDisableAlarmResponse**](BatchDisableAlarmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchEnableAlarm

> BatchEnableAlarmResponse batchEnableAlarm(batchEnableAlarmRequest, opts)



Enables one or more alarms. The alarms change to the &lt;code&gt;NORMAL&lt;/code&gt; state after you enable them.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchEnableAlarmRequest = new AwsIoTEventsData.BatchEnableAlarmRequest(); // BatchEnableAlarmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchEnableAlarm(batchEnableAlarmRequest, opts, (error, data, response) => {
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
 **batchEnableAlarmRequest** | [**BatchEnableAlarmRequest**](BatchEnableAlarmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchEnableAlarmResponse**](BatchEnableAlarmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchPutMessage

> BatchPutMessageResponse batchPutMessage(batchPutMessageRequest, opts)



Sends a set of messages to the IoT Events system. Each message payload is transformed into the input you specify (&lt;code&gt;\&quot;inputName\&quot;&lt;/code&gt;) and ingested into any detectors that monitor that input. If multiple messages are sent, the order in which the messages are processed isn&#39;t guaranteed. To guarantee ordering, you must send messages one at a time and wait for a successful response.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchPutMessageRequest = new AwsIoTEventsData.BatchPutMessageRequest(); // BatchPutMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchPutMessage(batchPutMessageRequest, opts, (error, data, response) => {
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
 **batchPutMessageRequest** | [**BatchPutMessageRequest**](BatchPutMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchPutMessageResponse**](BatchPutMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchResetAlarm

> BatchResetAlarmResponse batchResetAlarm(batchResetAlarmRequest, opts)



Resets one or more alarms. The alarms return to the &lt;code&gt;NORMAL&lt;/code&gt; state after you reset them.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchResetAlarmRequest = new AwsIoTEventsData.BatchResetAlarmRequest(); // BatchResetAlarmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchResetAlarm(batchResetAlarmRequest, opts, (error, data, response) => {
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
 **batchResetAlarmRequest** | [**BatchResetAlarmRequest**](BatchResetAlarmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchResetAlarmResponse**](BatchResetAlarmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchSnoozeAlarm

> BatchSnoozeAlarmResponse batchSnoozeAlarm(batchSnoozeAlarmRequest, opts)



Changes one or more alarms to the snooze mode. The alarms change to the &lt;code&gt;SNOOZE_DISABLED&lt;/code&gt; state after you set them to the snooze mode.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchSnoozeAlarmRequest = new AwsIoTEventsData.BatchSnoozeAlarmRequest(); // BatchSnoozeAlarmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchSnoozeAlarm(batchSnoozeAlarmRequest, opts, (error, data, response) => {
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
 **batchSnoozeAlarmRequest** | [**BatchSnoozeAlarmRequest**](BatchSnoozeAlarmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchSnoozeAlarmResponse**](BatchSnoozeAlarmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdateDetector

> BatchUpdateDetectorResponse batchUpdateDetector(batchUpdateDetectorRequest, opts)



Updates the state, variable values, and timer settings of one or more detectors (instances) of a specified detector model.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let batchUpdateDetectorRequest = new AwsIoTEventsData.BatchUpdateDetectorRequest(); // BatchUpdateDetectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateDetector(batchUpdateDetectorRequest, opts, (error, data, response) => {
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
 **batchUpdateDetectorRequest** | [**BatchUpdateDetectorRequest**](BatchUpdateDetectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateDetectorResponse**](BatchUpdateDetectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAlarm

> DescribeAlarmResponse describeAlarm(alarmModelName, opts)



Retrieves information about an alarm.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let alarmModelName = "alarmModelName_example"; // String | The name of the alarm model.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'keyValue': "keyValue_example" // String | The value of the key used as a filter to select only the alarms associated with the <a href=\"https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key\">key</a>.
};
apiInstance.describeAlarm(alarmModelName, opts, (error, data, response) => {
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
 **alarmModelName** | **String**| The name of the alarm model. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **keyValue** | **String**| The value of the key used as a filter to select only the alarms associated with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key\&quot;&gt;key&lt;/a&gt;. | [optional] 

### Return type

[**DescribeAlarmResponse**](DescribeAlarmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDetector

> DescribeDetectorResponse describeDetector(detectorModelName, opts)



Returns information about the specified detector (instance).

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let detectorModelName = "detectorModelName_example"; // String | The name of the detector model whose detectors (instances) you want information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'keyValue': "keyValue_example" // String | A filter used to limit results to detectors (instances) created because of the given key ID.
};
apiInstance.describeDetector(detectorModelName, opts, (error, data, response) => {
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
 **detectorModelName** | **String**| The name of the detector model whose detectors (instances) you want information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **keyValue** | **String**| A filter used to limit results to detectors (instances) created because of the given key ID. | [optional] 

### Return type

[**DescribeDetectorResponse**](DescribeDetectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAlarms

> ListAlarmsResponse listAlarms(alarmModelName, opts)



Lists one or more alarms. The operation returns only the metadata associated with each alarm.

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let alarmModelName = "alarmModelName_example"; // String | The name of the alarm model.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token that you can use to return the next set of results.
  'maxResults': 56 // Number | The maximum number of results to be returned per request.
};
apiInstance.listAlarms(alarmModelName, opts, (error, data, response) => {
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
 **alarmModelName** | **String**| The name of the alarm model. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token that you can use to return the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per request. | [optional] 

### Return type

[**ListAlarmsResponse**](ListAlarmsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDetectors

> ListDetectorsResponse listDetectors(detectorModelName, opts)



Lists detectors (the instances of a detector model).

### Example

```javascript
import AwsIoTEventsData from 'aws_io_t_events_data';
let defaultClient = AwsIoTEventsData.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTEventsData.DefaultApi();
let detectorModelName = "detectorModelName_example"; // String | The name of the detector model whose detectors (instances) are listed.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'stateName': "stateName_example", // String | A filter that limits results to those detectors (instances) in the given state.
  'nextToken': "nextToken_example", // String | The token that you can use to return the next set of results.
  'maxResults': 56 // Number | The maximum number of results to be returned per request.
};
apiInstance.listDetectors(detectorModelName, opts, (error, data, response) => {
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
 **detectorModelName** | **String**| The name of the detector model whose detectors (instances) are listed. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **stateName** | **String**| A filter that limits results to those detectors (instances) in the given state. | [optional] 
 **nextToken** | **String**| The token that you can use to return the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned per request. | [optional] 

### Return type

[**ListDetectorsResponse**](ListDetectorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

