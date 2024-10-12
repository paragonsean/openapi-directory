# AwsEc2InstanceConnect.DefaultApi

All URIs are relative to *http://ec2-instance-connect.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendSSHPublicKey**](DefaultApi.md#sendSSHPublicKey) | **POST** /#X-Amz-Target&#x3D;AWSEC2InstanceConnectService.SendSSHPublicKey | 
[**sendSerialConsoleSSHPublicKey**](DefaultApi.md#sendSerialConsoleSSHPublicKey) | **POST** /#X-Amz-Target&#x3D;AWSEC2InstanceConnectService.SendSerialConsoleSSHPublicKey | 



## sendSSHPublicKey

> SendSSHPublicKeyResponse sendSSHPublicKey(xAmzTarget, sendSSHPublicKeyRequest, opts)



Pushes an SSH public key to the specified EC2 instance for use by the specified user. The key remains for 60 seconds. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html\&quot;&gt;Connect to your Linux instance using EC2 Instance Connect&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.

### Example

```javascript
import AwsEc2InstanceConnect from 'aws_ec2_instance_connect';
let defaultClient = AwsEc2InstanceConnect.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEc2InstanceConnect.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendSSHPublicKeyRequest = new AwsEc2InstanceConnect.SendSSHPublicKeyRequest(); // SendSSHPublicKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendSSHPublicKey(xAmzTarget, sendSSHPublicKeyRequest, opts, (error, data, response) => {
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
 **sendSSHPublicKeyRequest** | [**SendSSHPublicKeyRequest**](SendSSHPublicKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendSSHPublicKeyResponse**](SendSSHPublicKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendSerialConsoleSSHPublicKey

> SendSerialConsoleSSHPublicKeyResponse sendSerialConsoleSSHPublicKey(xAmzTarget, sendSerialConsoleSSHPublicKeyRequest, opts)



Pushes an SSH public key to the specified EC2 instance. The key remains for 60 seconds, which gives you 60 seconds to establish a serial console connection to the instance using SSH. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html\&quot;&gt;EC2 Serial Console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.

### Example

```javascript
import AwsEc2InstanceConnect from 'aws_ec2_instance_connect';
let defaultClient = AwsEc2InstanceConnect.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsEc2InstanceConnect.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendSerialConsoleSSHPublicKeyRequest = new AwsEc2InstanceConnect.SendSerialConsoleSSHPublicKeyRequest(); // SendSerialConsoleSSHPublicKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendSerialConsoleSSHPublicKey(xAmzTarget, sendSerialConsoleSSHPublicKeyRequest, opts, (error, data, response) => {
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
 **sendSerialConsoleSSHPublicKeyRequest** | [**SendSerialConsoleSSHPublicKeyRequest**](SendSerialConsoleSSHPublicKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendSerialConsoleSSHPublicKeyResponse**](SendSerialConsoleSSHPublicKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

