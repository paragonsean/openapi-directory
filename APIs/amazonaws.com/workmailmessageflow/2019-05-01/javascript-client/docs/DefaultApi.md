# AmazonWorkMailMessageFlow.DefaultApi

All URIs are relative to *http://workmailmessageflow.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRawMessageContent**](DefaultApi.md#getRawMessageContent) | **GET** /messages/{messageId} | 
[**putRawMessageContent**](DefaultApi.md#putRawMessageContent) | **POST** /messages/{messageId} | 



## getRawMessageContent

> GetRawMessageContentResponse getRawMessageContent(messageId, opts)



Retrieves the raw content of an in-transit email message, in MIME format.

### Example

```javascript
import AmazonWorkMailMessageFlow from 'amazon_work_mail_message_flow';
let defaultClient = AmazonWorkMailMessageFlow.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonWorkMailMessageFlow.DefaultApi();
let messageId = "messageId_example"; // String | The identifier of the email message to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRawMessageContent(messageId, opts, (error, data, response) => {
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
 **messageId** | **String**| The identifier of the email message to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRawMessageContentResponse**](GetRawMessageContentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putRawMessageContent

> Object putRawMessageContent(messageId, putRawMessageContentRequest, opts)



&lt;p&gt;Updates the raw content of an in-transit email message, in MIME format.&lt;/p&gt; &lt;p&gt;This example describes how to update in-transit email message. For more information and examples for using this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html\&quot;&gt; Updating message content with AWS Lambda&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Updates to an in-transit message only appear when you call &lt;code&gt;PutRawMessageContent&lt;/code&gt; from an AWS Lambda function configured with a synchronous &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html#synchronous-rules\&quot;&gt; Run Lambda&lt;/a&gt; rule. If you call &lt;code&gt;PutRawMessageContent&lt;/code&gt; on a delivered or sent message, the message remains unchanged, even though &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html\&quot;&gt;GetRawMessageContent&lt;/a&gt; returns an updated message. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonWorkMailMessageFlow from 'amazon_work_mail_message_flow';
let defaultClient = AmazonWorkMailMessageFlow.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonWorkMailMessageFlow.DefaultApi();
let messageId = "messageId_example"; // String | The identifier of the email message being updated.
let putRawMessageContentRequest = new AmazonWorkMailMessageFlow.PutRawMessageContentRequest(); // PutRawMessageContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRawMessageContent(messageId, putRawMessageContentRequest, opts, (error, data, response) => {
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
 **messageId** | **String**| The identifier of the email message being updated. | 
 **putRawMessageContentRequest** | [**PutRawMessageContentRequest**](PutRawMessageContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

