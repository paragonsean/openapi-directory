# AwsIoTDataPlane.DefaultApi

All URIs are relative to *http://data-ats.iot.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteThingShadow**](DefaultApi.md#deleteThingShadow) | **DELETE** /things/{thingName}/shadow | 
[**getRetainedMessage**](DefaultApi.md#getRetainedMessage) | **GET** /retainedMessage/{topic} | 
[**getThingShadow**](DefaultApi.md#getThingShadow) | **GET** /things/{thingName}/shadow | 
[**listNamedShadowsForThing**](DefaultApi.md#listNamedShadowsForThing) | **GET** /api/things/shadow/ListNamedShadowsForThing/{thingName} | 
[**listRetainedMessages**](DefaultApi.md#listRetainedMessages) | **GET** /retainedMessage | 
[**publish**](DefaultApi.md#publish) | **POST** /topics/{topic} | 
[**updateThingShadow**](DefaultApi.md#updateThingShadow) | **POST** /things/{thingName}/shadow | 



## deleteThingShadow

> DeleteThingShadowResponse deleteThingShadow(thingName, opts)



&lt;p&gt;Deletes the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;DeleteThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html\&quot;&gt;DeleteThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let thingName = "thingName_example"; // String | The name of the thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example" // String | The name of the shadow.
};
apiInstance.deleteThingShadow(thingName, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **name** | **String**| The name of the shadow. | [optional] 

### Return type

[**DeleteThingShadowResponse**](DeleteThingShadowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRetainedMessage

> GetRetainedMessageResponse getRetainedMessage(topic, opts)



&lt;p&gt;Gets the details of a single retained message for the specified topic.&lt;/p&gt; &lt;p&gt;This action returns the message payload of the retained message, which can incur messaging costs. To list only the topic names of the retained messages, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html\&quot;&gt;ListRetainedMessages&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html#awsiotfleethubfordevicemanagement-actions-as-permissions\&quot;&gt;GetRetainedMessage&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let topic = "topic_example"; // String | The topic name of the retained message to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRetainedMessage(topic, opts, (error, data, response) => {
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
 **topic** | **String**| The topic name of the retained message to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRetainedMessageResponse**](GetRetainedMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThingShadow

> GetThingShadowResponse getThingShadow(thingName, opts)



&lt;p&gt;Gets the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html\&quot;&gt;GetThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let thingName = "thingName_example"; // String | The name of the thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example" // String | The name of the shadow.
};
apiInstance.getThingShadow(thingName, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **name** | **String**| The name of the shadow. | [optional] 

### Return type

[**GetThingShadowResponse**](GetThingShadowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNamedShadowsForThing

> ListNamedShadowsForThingResponse listNamedShadowsForThing(thingName, opts)



&lt;p&gt;Lists the shadows for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListNamedShadowsForThing&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let thingName = "thingName_example"; // String | The name of the thing.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to retrieve the next set of results.
  'pageSize': 56 // Number | The result page size.
};
apiInstance.listNamedShadowsForThing(thingName, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the thing. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to retrieve the next set of results. | [optional] 
 **pageSize** | **Number**| The result page size. | [optional] 

### Return type

[**ListNamedShadowsForThingResponse**](ListNamedShadowsForThingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRetainedMessages

> ListRetainedMessagesResponse listRetainedMessages(opts)



&lt;p&gt;Lists summary information about the retained messages stored for the account.&lt;/p&gt; &lt;p&gt;This action returns only the topic names of the retained messages. It doesn&#39;t return any message payloads. Although this action doesn&#39;t return a message payload, it can still incur messaging costs.&lt;/p&gt; &lt;p&gt;To get the message payload of a retained message, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html\&quot;&gt;GetRetainedMessage&lt;/a&gt; with the topic name of the retained message.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html#awsiotfleethubfordevicemanagement-actions-as-permissions\&quot;&gt;ListRetainedMessages&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
  'maxResults': 56 // Number | The maximum number of results to return at one time.
};
apiInstance.listRetainedMessages(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return at one time. | [optional] 

### Return type

[**ListRetainedMessagesResponse**](ListRetainedMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publish

> publish(topic, publishRequest, opts)



&lt;p&gt;Publishes an MQTT message.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;Publish&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about MQTT messages, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html\&quot;&gt;MQTT Protocol&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let topic = "topic_example"; // String | The name of the MQTT topic.
let publishRequest = new AwsIoTDataPlane.PublishRequest(); // PublishRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'qos': 56, // Number | The Quality of Service (QoS) level. The default QoS level is 0.
  'retain': true, // Boolean | <p>A Boolean value that determines whether to set the RETAIN flag when the message is published.</p> <p>Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default value: <code>false</code> </p>
  'xAmzMqtt5UserProperties': "xAmzMqtt5UserProperties_example", // String | <p>A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. <code>userProperties</code> is an HTTP header value in the API.</p> <p>The following example <code>userProperties</code> parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:</p> <p> <code>[{\"deviceName\": \"alpha\"}, {\"deviceCnt\": \"45\"}]</code> </p>
  'xAmzMqtt5PayloadFormatIndicator': "xAmzMqtt5PayloadFormatIndicator_example", // String | An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8. <code>payloadFormatIndicator</code> is an HTTP header value in the API.
  'contentType': "contentType_example", // String | A UTF-8 encoded string that describes the content of the publishing message.
  'responseTopic': "responseTopic_example", // String | A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.
  'xAmzMqtt5CorrelationData': "xAmzMqtt5CorrelationData_example", // String | The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. <code>correlationData</code> is an HTTP header value in the API.
  'messageExpiry': 56 // Number | A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn't expire. For more information about the limits of <code>messageExpiry</code>, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits\">Amazon Web Services IoT Core message broker and protocol limits and quotas </a> from the Amazon Web Services Reference Guide.
};
apiInstance.publish(topic, publishRequest, opts, (error, data, response) => {
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
 **topic** | **String**| The name of the MQTT topic. | 
 **publishRequest** | [**PublishRequest**](PublishRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **qos** | **Number**| The Quality of Service (QoS) level. The default QoS level is 0. | [optional] 
 **retain** | **Boolean**| &lt;p&gt;A Boolean value that determines whether to set the RETAIN flag when the message is published.&lt;/p&gt; &lt;p&gt;Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;true&lt;/code&gt; | &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; | [optional] 
 **xAmzMqtt5UserProperties** | **String**| &lt;p&gt;A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. &lt;code&gt;userProperties&lt;/code&gt; is an HTTP header value in the API.&lt;/p&gt; &lt;p&gt;The following example &lt;code&gt;userProperties&lt;/code&gt; parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:&lt;/p&gt; &lt;p&gt; &lt;code&gt;[{\&quot;deviceName\&quot;: \&quot;alpha\&quot;}, {\&quot;deviceCnt\&quot;: \&quot;45\&quot;}]&lt;/code&gt; &lt;/p&gt; | [optional] 
 **xAmzMqtt5PayloadFormatIndicator** | **String**| An &lt;code&gt;Enum&lt;/code&gt; string value that indicates whether the payload is formatted as UTF-8. &lt;code&gt;payloadFormatIndicator&lt;/code&gt; is an HTTP header value in the API. | [optional] 
 **contentType** | **String**| A UTF-8 encoded string that describes the content of the publishing message. | [optional] 
 **responseTopic** | **String**| A UTF-8 encoded string that&#39;s used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters. | [optional] 
 **xAmzMqtt5CorrelationData** | **String**| The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it&#39;s received. &lt;code&gt;correlationData&lt;/code&gt; is an HTTP header value in the API. | [optional] 
 **messageExpiry** | **Number**| A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn&#39;t expire. For more information about the limits of &lt;code&gt;messageExpiry&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits\&quot;&gt;Amazon Web Services IoT Core message broker and protocol limits and quotas &lt;/a&gt; from the Amazon Web Services Reference Guide. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateThingShadow

> UpdateThingShadowResponse updateThingShadow(thingName, updateThingShadowRequest, opts)



&lt;p&gt;Updates the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UpdateThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html\&quot;&gt;UpdateThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

### Example

```javascript
import AwsIoTDataPlane from 'aws_io_t_data_plane';
let defaultClient = AwsIoTDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoTDataPlane.DefaultApi();
let thingName = "thingName_example"; // String | The name of the thing.
let updateThingShadowRequest = new AwsIoTDataPlane.UpdateThingShadowRequest(); // UpdateThingShadowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example" // String | The name of the shadow.
};
apiInstance.updateThingShadow(thingName, updateThingShadowRequest, opts, (error, data, response) => {
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
 **thingName** | **String**| The name of the thing. | 
 **updateThingShadowRequest** | [**UpdateThingShadowRequest**](UpdateThingShadowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **name** | **String**| The name of the shadow. | [optional] 

### Return type

[**UpdateThingShadowResponse**](UpdateThingShadowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

