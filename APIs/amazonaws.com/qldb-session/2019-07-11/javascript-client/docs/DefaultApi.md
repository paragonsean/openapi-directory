# AmazonQldbSession.DefaultApi

All URIs are relative to *http://session.qldb.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendCommand**](DefaultApi.md#sendCommand) | **POST** /#X-Amz-Target&#x3D;QLDBSession.SendCommand | 



## sendCommand

> SendCommandResult sendCommand(xAmzTarget, sendCommandRequest, opts)



&lt;p&gt;Sends a command to an Amazon QLDB ledger.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Instead of interacting directly with this API, we recommend using the QLDB driver or the QLDB shell to execute data transactions on a ledger.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are working with an AWS SDK, use the QLDB driver. The driver provides a high-level abstraction layer above this &lt;i&gt;QLDB Session&lt;/i&gt; data plane and manages &lt;code&gt;SendCommand&lt;/code&gt; API calls for you. For information and a list of supported programming languages, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-driver.html\&quot;&gt;Getting started with the driver&lt;/a&gt; in the &lt;i&gt;Amazon QLDB Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are working with the AWS Command Line Interface (AWS CLI), use the QLDB shell. The shell is a command line interface that uses the QLDB driver to interact with a ledger. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/qldb/latest/developerguide/data-shell.html\&quot;&gt;Accessing Amazon QLDB using the QLDB shell&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AmazonQldbSession from 'amazon_qldb_session';
let defaultClient = AmazonQldbSession.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonQldbSession.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendCommandRequest = new AmazonQldbSession.SendCommandRequest(); // SendCommandRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendCommand(xAmzTarget, sendCommandRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **sendCommandRequest** | [**SendCommandRequest**](SendCommandRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendCommandResult**](SendCommandResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

