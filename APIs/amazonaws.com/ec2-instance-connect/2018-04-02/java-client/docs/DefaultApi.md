# DefaultApi

All URIs are relative to *http://ec2-instance-connect.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendSSHPublicKey**](DefaultApi.md#sendSSHPublicKey) | **POST** /#X-Amz-Target&#x3D;AWSEC2InstanceConnectService.SendSSHPublicKey |  |
| [**sendSerialConsoleSSHPublicKey**](DefaultApi.md#sendSerialConsoleSSHPublicKey) | **POST** /#X-Amz-Target&#x3D;AWSEC2InstanceConnectService.SendSerialConsoleSSHPublicKey |  |


<a id="sendSSHPublicKey"></a>
# **sendSSHPublicKey**
> SendSSHPublicKeyResponse sendSSHPublicKey(xAmzTarget, sendSSHPublicKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Pushes an SSH public key to the specified EC2 instance for use by the specified user. The key remains for 60 seconds. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html\&quot;&gt;Connect to your Linux instance using EC2 Instance Connect&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://ec2-instance-connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSEC2InstanceConnectService.SendSSHPublicKey"; // String | 
    SendSSHPublicKeyRequest sendSSHPublicKeyRequest = new SendSSHPublicKeyRequest(); // SendSSHPublicKeyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      SendSSHPublicKeyResponse result = apiInstance.sendSSHPublicKey(xAmzTarget, sendSSHPublicKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendSSHPublicKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSEC2InstanceConnectService.SendSSHPublicKey] |
| **sendSSHPublicKeyRequest** | [**SendSSHPublicKeyRequest**](SendSSHPublicKeyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**SendSSHPublicKeyResponse**](SendSSHPublicKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthException |  -  |
| **481** | InvalidArgsException |  -  |
| **482** | ServiceException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | EC2InstanceNotFoundException |  -  |
| **485** | EC2InstanceStateInvalidException |  -  |
| **486** | EC2InstanceUnavailableException |  -  |

<a id="sendSerialConsoleSSHPublicKey"></a>
# **sendSerialConsoleSSHPublicKey**
> SendSerialConsoleSSHPublicKeyResponse sendSerialConsoleSSHPublicKey(xAmzTarget, sendSerialConsoleSSHPublicKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Pushes an SSH public key to the specified EC2 instance. The key remains for 60 seconds, which gives you 60 seconds to establish a serial console connection to the instance using SSH. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html\&quot;&gt;EC2 Serial Console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://ec2-instance-connect.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSEC2InstanceConnectService.SendSerialConsoleSSHPublicKey"; // String | 
    SendSerialConsoleSSHPublicKeyRequest sendSerialConsoleSSHPublicKeyRequest = new SendSerialConsoleSSHPublicKeyRequest(); // SendSerialConsoleSSHPublicKeyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      SendSerialConsoleSSHPublicKeyResponse result = apiInstance.sendSerialConsoleSSHPublicKey(xAmzTarget, sendSerialConsoleSSHPublicKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendSerialConsoleSSHPublicKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzTarget** | **String**|  | [enum: AWSEC2InstanceConnectService.SendSerialConsoleSSHPublicKey] |
| **sendSerialConsoleSSHPublicKeyRequest** | [**SendSerialConsoleSSHPublicKeyRequest**](SendSerialConsoleSSHPublicKeyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**SendSerialConsoleSSHPublicKeyResponse**](SendSerialConsoleSSHPublicKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | AuthException |  -  |
| **481** | SerialConsoleAccessDisabledException |  -  |
| **482** | InvalidArgsException |  -  |
| **483** | ServiceException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | EC2InstanceNotFoundException |  -  |
| **486** | EC2InstanceTypeInvalidException |  -  |
| **487** | SerialConsoleSessionLimitExceededException |  -  |
| **488** | SerialConsoleSessionUnavailableException |  -  |
| **489** | EC2InstanceStateInvalidException |  -  |
| **490** | EC2InstanceUnavailableException |  -  |

