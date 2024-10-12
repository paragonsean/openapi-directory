# DefaultApi

All URIs are relative to *http://cloudhsm.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTagsToResource**](DefaultApi.md#addTagsToResource) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.AddTagsToResource |  |
| [**createHapg**](DefaultApi.md#createHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.CreateHapg |  |
| [**createHsm**](DefaultApi.md#createHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.CreateHsm |  |
| [**createLunaClient**](DefaultApi.md#createLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.CreateLunaClient |  |
| [**deleteHapg**](DefaultApi.md#deleteHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DeleteHapg |  |
| [**deleteHsm**](DefaultApi.md#deleteHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DeleteHsm |  |
| [**deleteLunaClient**](DefaultApi.md#deleteLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DeleteLunaClient |  |
| [**describeHapg**](DefaultApi.md#describeHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DescribeHapg |  |
| [**describeHsm**](DefaultApi.md#describeHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DescribeHsm |  |
| [**describeLunaClient**](DefaultApi.md#describeLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DescribeLunaClient |  |
| [**getConfig**](DefaultApi.md#getConfig) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.GetConfig |  |
| [**listAvailableZones**](DefaultApi.md#listAvailableZones) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListAvailableZones |  |
| [**listHapgs**](DefaultApi.md#listHapgs) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListHapgs |  |
| [**listHsms**](DefaultApi.md#listHsms) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListHsms |  |
| [**listLunaClients**](DefaultApi.md#listLunaClients) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListLunaClients |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListTagsForResource |  |
| [**modifyHapg**](DefaultApi.md#modifyHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ModifyHapg |  |
| [**modifyHsm**](DefaultApi.md#modifyHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ModifyHsm |  |
| [**modifyLunaClient**](DefaultApi.md#modifyLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ModifyLunaClient |  |
| [**removeTagsFromResource**](DefaultApi.md#removeTagsFromResource) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.RemoveTagsFromResource |  |


<a id="addTagsToResource"></a>
# **addTagsToResource**
> AddTagsToResourceResponse addTagsToResource(xAmzTarget, addTagsToResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Adds or overwrites one or more tags for the specified AWS CloudHSM resource.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and a value. Tag keys must be unique to each resource.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.AddTagsToResource"; // String | 
    AddTagsToResourceRequest addTagsToResourceRequest = new AddTagsToResourceRequest(); // AddTagsToResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AddTagsToResourceResponse result = apiInstance.addTagsToResource(xAmzTarget, addTagsToResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addTagsToResource");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.AddTagsToResource] |
| **addTagsToResourceRequest** | [**AddTagsToResourceRequest**](AddTagsToResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AddTagsToResourceResponse**](AddTagsToResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="createHapg"></a>
# **createHapg**
> CreateHapgResponse createHapg(xAmzTarget, createHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.CreateHapg"; // String | 
    CreateHapgRequest createHapgRequest = new CreateHapgRequest(); // CreateHapgRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateHapgResponse result = apiInstance.createHapg(xAmzTarget, createHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createHapg");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.CreateHapg] |
| **createHapgRequest** | [**CreateHapgRequest**](CreateHapgRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateHapgResponse**](CreateHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="createHsm"></a>
# **createHsm**
> CreateHsmResponse createHsm(xAmzTarget, createHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates an uninitialized HSM instance.&lt;/p&gt; &lt;p&gt;There is an upfront fee charged for each HSM instance that you create with the &lt;code&gt;CreateHsm&lt;/code&gt; operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the &lt;a&gt;DeleteHsm&lt;/a&gt; operation, go to the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home\&quot;&gt;AWS Support Center&lt;/a&gt;, create a new case, and select &lt;b&gt;Account and Billing Support&lt;/b&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It can take up to 20 minutes to create and provision an HSM. You can monitor the status of the HSM with the &lt;a&gt;DescribeHsm&lt;/a&gt; operation. The HSM is ready to be initialized when the status changes to &lt;code&gt;RUNNING&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.CreateHsm"; // String | 
    CreateHsmRequest createHsmRequest = new CreateHsmRequest(); // CreateHsmRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateHsmResponse result = apiInstance.createHsm(xAmzTarget, createHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createHsm");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.CreateHsm] |
| **createHsmRequest** | [**CreateHsmRequest**](CreateHsmRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateHsmResponse**](CreateHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="createLunaClient"></a>
# **createLunaClient**
> CreateLunaClientResponse createLunaClient(xAmzTarget, createLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates an HSM client.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.CreateLunaClient"; // String | 
    CreateLunaClientRequest createLunaClientRequest = new CreateLunaClientRequest(); // CreateLunaClientRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateLunaClientResponse result = apiInstance.createLunaClient(xAmzTarget, createLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createLunaClient");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.CreateLunaClient] |
| **createLunaClientRequest** | [**CreateLunaClientRequest**](CreateLunaClientRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateLunaClientResponse**](CreateLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="deleteHapg"></a>
# **deleteHapg**
> DeleteHapgResponse deleteHapg(xAmzTarget, deleteHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes a high-availability partition group.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.DeleteHapg"; // String | 
    DeleteHapgRequest deleteHapgRequest = new DeleteHapgRequest(); // DeleteHapgRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteHapgResponse result = apiInstance.deleteHapg(xAmzTarget, deleteHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteHapg");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.DeleteHapg] |
| **deleteHapgRequest** | [**DeleteHapgRequest**](DeleteHapgRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteHapgResponse**](DeleteHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="deleteHsm"></a>
# **deleteHsm**
> DeleteHsmResponse deleteHsm(xAmzTarget, deleteHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.DeleteHsm"; // String | 
    DeleteHsmRequest deleteHsmRequest = new DeleteHsmRequest(); // DeleteHsmRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteHsmResponse result = apiInstance.deleteHsm(xAmzTarget, deleteHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteHsm");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.DeleteHsm] |
| **deleteHsmRequest** | [**DeleteHsmRequest**](DeleteHsmRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteHsmResponse**](DeleteHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="deleteLunaClient"></a>
# **deleteLunaClient**
> DeleteLunaClientResponse deleteLunaClient(xAmzTarget, deleteLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes a client.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.DeleteLunaClient"; // String | 
    DeleteLunaClientRequest deleteLunaClientRequest = new DeleteLunaClientRequest(); // DeleteLunaClientRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteLunaClientResponse result = apiInstance.deleteLunaClient(xAmzTarget, deleteLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteLunaClient");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.DeleteLunaClient] |
| **deleteLunaClientRequest** | [**DeleteLunaClientRequest**](DeleteLunaClientRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteLunaClientResponse**](DeleteLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="describeHapg"></a>
# **describeHapg**
> DescribeHapgResponse describeHapg(xAmzTarget, describeHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about a high-availability partition group.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.DescribeHapg"; // String | 
    DescribeHapgRequest describeHapgRequest = new DescribeHapgRequest(); // DescribeHapgRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeHapgResponse result = apiInstance.describeHapg(xAmzTarget, describeHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeHapg");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.DescribeHapg] |
| **describeHapgRequest** | [**DescribeHapgRequest**](DescribeHapgRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeHapgResponse**](DescribeHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="describeHsm"></a>
# **describeHsm**
> DescribeHsmResponse describeHsm(xAmzTarget, describeHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.DescribeHsm"; // String | 
    DescribeHsmRequest describeHsmRequest = new DescribeHsmRequest(); // DescribeHsmRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeHsmResponse result = apiInstance.describeHsm(xAmzTarget, describeHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeHsm");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.DescribeHsm] |
| **describeHsmRequest** | [**DescribeHsmRequest**](DescribeHsmRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeHsmResponse**](DescribeHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="describeLunaClient"></a>
# **describeLunaClient**
> DescribeLunaClientResponse describeLunaClient(xAmzTarget, describeLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about an HSM client.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.DescribeLunaClient"; // String | 
    DescribeLunaClientRequest describeLunaClientRequest = new DescribeLunaClientRequest(); // DescribeLunaClientRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeLunaClientResponse result = apiInstance.describeLunaClient(xAmzTarget, describeLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeLunaClient");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.DescribeLunaClient] |
| **describeLunaClientRequest** | [**DescribeLunaClientRequest**](DescribeLunaClientRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeLunaClientResponse**](DescribeLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="getConfig"></a>
# **getConfig**
> GetConfigResponse getConfig(xAmzTarget, getConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.GetConfig"; // String | 
    GetConfigRequest getConfigRequest = new GetConfigRequest(); // GetConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetConfigResponse result = apiInstance.getConfig(xAmzTarget, getConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getConfig");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.GetConfig] |
| **getConfigRequest** | [**GetConfigRequest**](GetConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetConfigResponse**](GetConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="listAvailableZones"></a>
# **listAvailableZones**
> ListAvailableZonesResponse listAvailableZones(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists the Availability Zones that have available AWS CloudHSM capacity.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ListAvailableZones"; // String | 
    Object body = null; // Object | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListAvailableZonesResponse result = apiInstance.listAvailableZones(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAvailableZones");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ListAvailableZones] |
| **body** | **Object**|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListAvailableZonesResponse**](ListAvailableZonesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="listHapgs"></a>
# **listHapgs**
> ListHapgsResponse listHapgs(xAmzTarget, listHapgsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists the high-availability partition groups for the account.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListHapgs&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ListHapgs"; // String | 
    ListHapgsRequest listHapgsRequest = new ListHapgsRequest(); // ListHapgsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListHapgsResponse result = apiInstance.listHapgs(xAmzTarget, listHapgsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listHapgs");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ListHapgs] |
| **listHapgsRequest** | [**ListHapgsRequest**](ListHapgsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListHapgsResponse**](ListHapgsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="listHsms"></a>
# **listHsms**
> ListHsmsResponse listHsms(xAmzTarget, listHsmsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves the identifiers of all of the HSMs provisioned for the current customer.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListHsms&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ListHsms"; // String | 
    ListHsmsRequest listHsmsRequest = new ListHsmsRequest(); // ListHsmsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListHsmsResponse result = apiInstance.listHsms(xAmzTarget, listHsmsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listHsms");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ListHsms] |
| **listHsmsRequest** | [**ListHsmsRequest**](ListHsmsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListHsmsResponse**](ListHsmsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="listLunaClients"></a>
# **listLunaClients**
> ListLunaClientsResponse listLunaClients(xAmzTarget, listLunaClientsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists all of the clients.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListLunaClients&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ListLunaClients"; // String | 
    ListLunaClientsRequest listLunaClientsRequest = new ListLunaClientsRequest(); // ListLunaClientsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListLunaClientsResponse result = apiInstance.listLunaClients(xAmzTarget, listLunaClientsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listLunaClients");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ListLunaClients] |
| **listLunaClientsRequest** | [**ListLunaClientsRequest**](ListLunaClientsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListLunaClientsResponse**](ListLunaClientsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Returns a list of all tags for the specified AWS CloudHSM resource.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ListTagsForResource"; // String | 
    ListTagsForResourceRequest listTagsForResourceRequest = new ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ListTagsForResource] |
| **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="modifyHapg"></a>
# **modifyHapg**
> ModifyHapgResponse modifyHapg(xAmzTarget, modifyHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies an existing high-availability partition group.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ModifyHapg"; // String | 
    ModifyHapgRequest modifyHapgRequest = new ModifyHapgRequest(); // ModifyHapgRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ModifyHapgResponse result = apiInstance.modifyHapg(xAmzTarget, modifyHapgRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modifyHapg");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ModifyHapg] |
| **modifyHapgRequest** | [**ModifyHapgRequest**](ModifyHapgRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ModifyHapgResponse**](ModifyHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="modifyHsm"></a>
# **modifyHsm**
> ModifyHsmResponse modifyHsm(xAmzTarget, modifyHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies an HSM.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation can result in the HSM being offline for up to 15 minutes while the AWS CloudHSM service is reconfigured. If you are modifying a production HSM, you should ensure that your AWS CloudHSM service is configured for high availability, and consider executing this operation during a maintenance window.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ModifyHsm"; // String | 
    ModifyHsmRequest modifyHsmRequest = new ModifyHsmRequest(); // ModifyHsmRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ModifyHsmResponse result = apiInstance.modifyHsm(xAmzTarget, modifyHsmRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modifyHsm");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ModifyHsm] |
| **modifyHsmRequest** | [**ModifyHsmRequest**](ModifyHsmRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ModifyHsmResponse**](ModifyHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

<a id="modifyLunaClient"></a>
# **modifyLunaClient**
> ModifyLunaClientResponse modifyLunaClient(xAmzTarget, modifyLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies the certificate used by the client.&lt;/p&gt; &lt;p&gt;This action can potentially start a workflow to install the new certificate on the client&#39;s HSMs.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.ModifyLunaClient"; // String | 
    ModifyLunaClientRequest modifyLunaClientRequest = new ModifyLunaClientRequest(); // ModifyLunaClientRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ModifyLunaClientResponse result = apiInstance.modifyLunaClient(xAmzTarget, modifyLunaClientRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modifyLunaClient");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.ModifyLunaClient] |
| **modifyLunaClientRequest** | [**ModifyLunaClientRequest**](ModifyLunaClientRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ModifyLunaClientResponse**](ModifyLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |

<a id="removeTagsFromResource"></a>
# **removeTagsFromResource**
> RemoveTagsFromResourceResponse removeTagsFromResource(xAmzTarget, removeTagsFromResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Removes one or more tags from the specified AWS CloudHSM resource.&lt;/p&gt; &lt;p&gt;To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use &lt;a&gt;AddTagsToResource&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://cloudhsm.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CloudHsmFrontendService.RemoveTagsFromResource"; // String | 
    RemoveTagsFromResourceRequest removeTagsFromResourceRequest = new RemoveTagsFromResourceRequest(); // RemoveTagsFromResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RemoveTagsFromResourceResponse result = apiInstance.removeTagsFromResource(xAmzTarget, removeTagsFromResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeTagsFromResource");
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
| **xAmzTarget** | **String**|  | [enum: CloudHsmFrontendService.RemoveTagsFromResource] |
| **removeTagsFromResourceRequest** | [**RemoveTagsFromResourceRequest**](RemoveTagsFromResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RemoveTagsFromResourceResponse**](RemoveTagsFromResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CloudHsmServiceException |  -  |
| **481** | CloudHsmInternalException |  -  |
| **482** | InvalidRequestException |  -  |

