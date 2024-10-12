# DefaultApi

All URIs are relative to *http://comprehendmedical.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**describeEntitiesDetectionV2Job**](DefaultApi.md#describeEntitiesDetectionV2Job) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeEntitiesDetectionV2Job |  |
| [**describeICD10CMInferenceJob**](DefaultApi.md#describeICD10CMInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeICD10CMInferenceJob |  |
| [**describePHIDetectionJob**](DefaultApi.md#describePHIDetectionJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribePHIDetectionJob |  |
| [**describeRxNormInferenceJob**](DefaultApi.md#describeRxNormInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeRxNormInferenceJob |  |
| [**describeSNOMEDCTInferenceJob**](DefaultApi.md#describeSNOMEDCTInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DescribeSNOMEDCTInferenceJob |  |
| [**detectEntities**](DefaultApi.md#detectEntities) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DetectEntities |  |
| [**detectEntitiesV2**](DefaultApi.md#detectEntitiesV2) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DetectEntitiesV2 |  |
| [**detectPHI**](DefaultApi.md#detectPHI) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.DetectPHI |  |
| [**inferICD10CM**](DefaultApi.md#inferICD10CM) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.InferICD10CM |  |
| [**inferRxNorm**](DefaultApi.md#inferRxNorm) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.InferRxNorm |  |
| [**inferSNOMEDCT**](DefaultApi.md#inferSNOMEDCT) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.InferSNOMEDCT |  |
| [**listEntitiesDetectionV2Jobs**](DefaultApi.md#listEntitiesDetectionV2Jobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListEntitiesDetectionV2Jobs |  |
| [**listICD10CMInferenceJobs**](DefaultApi.md#listICD10CMInferenceJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListICD10CMInferenceJobs |  |
| [**listPHIDetectionJobs**](DefaultApi.md#listPHIDetectionJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListPHIDetectionJobs |  |
| [**listRxNormInferenceJobs**](DefaultApi.md#listRxNormInferenceJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListRxNormInferenceJobs |  |
| [**listSNOMEDCTInferenceJobs**](DefaultApi.md#listSNOMEDCTInferenceJobs) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.ListSNOMEDCTInferenceJobs |  |
| [**startEntitiesDetectionV2Job**](DefaultApi.md#startEntitiesDetectionV2Job) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartEntitiesDetectionV2Job |  |
| [**startICD10CMInferenceJob**](DefaultApi.md#startICD10CMInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartICD10CMInferenceJob |  |
| [**startPHIDetectionJob**](DefaultApi.md#startPHIDetectionJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartPHIDetectionJob |  |
| [**startRxNormInferenceJob**](DefaultApi.md#startRxNormInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartRxNormInferenceJob |  |
| [**startSNOMEDCTInferenceJob**](DefaultApi.md#startSNOMEDCTInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StartSNOMEDCTInferenceJob |  |
| [**stopEntitiesDetectionV2Job**](DefaultApi.md#stopEntitiesDetectionV2Job) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopEntitiesDetectionV2Job |  |
| [**stopICD10CMInferenceJob**](DefaultApi.md#stopICD10CMInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopICD10CMInferenceJob |  |
| [**stopPHIDetectionJob**](DefaultApi.md#stopPHIDetectionJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopPHIDetectionJob |  |
| [**stopRxNormInferenceJob**](DefaultApi.md#stopRxNormInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopRxNormInferenceJob |  |
| [**stopSNOMEDCTInferenceJob**](DefaultApi.md#stopSNOMEDCTInferenceJob) | **POST** /#X-Amz-Target&#x3D;ComprehendMedical_20181030.StopSNOMEDCTInferenceJob |  |


<a id="describeEntitiesDetectionV2Job"></a>
# **describeEntitiesDetectionV2Job**
> DescribeEntitiesDetectionV2JobResponse describeEntitiesDetectionV2Job(xAmzTarget, describeEntitiesDetectionV2JobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the properties associated with a medical entities detection job. Use this operation to get the status of a detection job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DescribeEntitiesDetectionV2Job"; // String | 
    DescribeEntitiesDetectionV2JobRequest describeEntitiesDetectionV2JobRequest = new DescribeEntitiesDetectionV2JobRequest(); // DescribeEntitiesDetectionV2JobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeEntitiesDetectionV2JobResponse result = apiInstance.describeEntitiesDetectionV2Job(xAmzTarget, describeEntitiesDetectionV2JobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeEntitiesDetectionV2Job");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DescribeEntitiesDetectionV2Job] |
| **describeEntitiesDetectionV2JobRequest** | [**DescribeEntitiesDetectionV2JobRequest**](DescribeEntitiesDetectionV2JobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeEntitiesDetectionV2JobResponse**](DescribeEntitiesDetectionV2JobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeICD10CMInferenceJob"></a>
# **describeICD10CMInferenceJob**
> DescribeICD10CMInferenceJobResponse describeICD10CMInferenceJob(xAmzTarget, describeICD10CMInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the properties associated with an InferICD10CM job. Use this operation to get the status of an inference job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DescribeICD10CMInferenceJob"; // String | 
    DescribeICD10CMInferenceJobRequest describeICD10CMInferenceJobRequest = new DescribeICD10CMInferenceJobRequest(); // DescribeICD10CMInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeICD10CMInferenceJobResponse result = apiInstance.describeICD10CMInferenceJob(xAmzTarget, describeICD10CMInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeICD10CMInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DescribeICD10CMInferenceJob] |
| **describeICD10CMInferenceJobRequest** | [**DescribeICD10CMInferenceJobRequest**](DescribeICD10CMInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeICD10CMInferenceJobResponse**](DescribeICD10CMInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describePHIDetectionJob"></a>
# **describePHIDetectionJob**
> DescribePHIDetectionJobResponse describePHIDetectionJob(xAmzTarget, describePHIDetectionJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the properties associated with a protected health information (PHI) detection job. Use this operation to get the status of a detection job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DescribePHIDetectionJob"; // String | 
    DescribePHIDetectionJobRequest describePHIDetectionJobRequest = new DescribePHIDetectionJobRequest(); // DescribePHIDetectionJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribePHIDetectionJobResponse result = apiInstance.describePHIDetectionJob(xAmzTarget, describePHIDetectionJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describePHIDetectionJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DescribePHIDetectionJob] |
| **describePHIDetectionJobRequest** | [**DescribePHIDetectionJobRequest**](DescribePHIDetectionJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribePHIDetectionJobResponse**](DescribePHIDetectionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeRxNormInferenceJob"></a>
# **describeRxNormInferenceJob**
> DescribeRxNormInferenceJobResponse describeRxNormInferenceJob(xAmzTarget, describeRxNormInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the properties associated with an InferRxNorm job. Use this operation to get the status of an inference job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DescribeRxNormInferenceJob"; // String | 
    DescribeRxNormInferenceJobRequest describeRxNormInferenceJobRequest = new DescribeRxNormInferenceJobRequest(); // DescribeRxNormInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeRxNormInferenceJobResponse result = apiInstance.describeRxNormInferenceJob(xAmzTarget, describeRxNormInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeRxNormInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DescribeRxNormInferenceJob] |
| **describeRxNormInferenceJobRequest** | [**DescribeRxNormInferenceJobRequest**](DescribeRxNormInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeRxNormInferenceJobResponse**](DescribeRxNormInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeSNOMEDCTInferenceJob"></a>
# **describeSNOMEDCTInferenceJob**
> DescribeSNOMEDCTInferenceJobResponse describeSNOMEDCTInferenceJob(xAmzTarget, describeSNOMEDCTInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Gets the properties associated with an InferSNOMEDCT job. Use this operation to get the status of an inference job. 

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DescribeSNOMEDCTInferenceJob"; // String | 
    DescribeSNOMEDCTInferenceJobRequest describeSNOMEDCTInferenceJobRequest = new DescribeSNOMEDCTInferenceJobRequest(); // DescribeSNOMEDCTInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeSNOMEDCTInferenceJobResponse result = apiInstance.describeSNOMEDCTInferenceJob(xAmzTarget, describeSNOMEDCTInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeSNOMEDCTInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DescribeSNOMEDCTInferenceJob] |
| **describeSNOMEDCTInferenceJobRequest** | [**DescribeSNOMEDCTInferenceJobRequest**](DescribeSNOMEDCTInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeSNOMEDCTInferenceJobResponse**](DescribeSNOMEDCTInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="detectEntities"></a>
# **detectEntities**
> DetectEntitiesResponse detectEntities(xAmzTarget, detectEntitiesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;The &lt;code&gt;DetectEntities&lt;/code&gt; operation is deprecated. You should use the &lt;a&gt;DetectEntitiesV2&lt;/a&gt; operation instead.&lt;/p&gt; &lt;p&gt;Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information.&lt;/p&gt;

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DetectEntities"; // String | 
    DetectEntitiesRequest detectEntitiesRequest = new DetectEntitiesRequest(); // DetectEntitiesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DetectEntitiesResponse result = apiInstance.detectEntities(xAmzTarget, detectEntitiesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detectEntities");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DetectEntities] |
| **detectEntitiesRequest** | [**DetectEntitiesRequest**](DetectEntitiesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DetectEntitiesResponse**](DetectEntitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InvalidRequestException |  -  |
| **484** | InvalidEncodingException |  -  |
| **485** | TextSizeLimitExceededException |  -  |

<a id="detectEntitiesV2"></a>
# **detectEntitiesV2**
> DetectEntitiesV2Response detectEntitiesV2(xAmzTarget, detectEntitiesV2Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation replaces the &lt;a&gt;DetectEntities&lt;/a&gt; operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation in all new applications.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation returns the &lt;code&gt;Acuity&lt;/code&gt; and &lt;code&gt;Direction&lt;/code&gt; entities as attributes instead of types. &lt;/p&gt;

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DetectEntitiesV2"; // String | 
    DetectEntitiesV2Request detectEntitiesV2Request = new DetectEntitiesV2Request(); // DetectEntitiesV2Request | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DetectEntitiesV2Response result = apiInstance.detectEntitiesV2(xAmzTarget, detectEntitiesV2Request, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detectEntitiesV2");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DetectEntitiesV2] |
| **detectEntitiesV2Request** | [**DetectEntitiesV2Request**](DetectEntitiesV2Request.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DetectEntitiesV2Response**](DetectEntitiesV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InvalidRequestException |  -  |
| **484** | InvalidEncodingException |  -  |
| **485** | TextSizeLimitExceededException |  -  |

<a id="detectPHI"></a>
# **detectPHI**
> DetectPHIResponse detectPHI(xAmzTarget, detectPHIRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity. Amazon Comprehend Medical only detects entities in English language texts.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.DetectPHI"; // String | 
    DetectPHIRequest detectPHIRequest = new DetectPHIRequest(); // DetectPHIRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DetectPHIResponse result = apiInstance.detectPHI(xAmzTarget, detectPHIRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detectPHI");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.DetectPHI] |
| **detectPHIRequest** | [**DetectPHIRequest**](DetectPHIRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DetectPHIResponse**](DetectPHIResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InvalidRequestException |  -  |
| **484** | InvalidEncodingException |  -  |
| **485** | TextSizeLimitExceededException |  -  |

<a id="inferICD10CM"></a>
# **inferICD10CM**
> InferICD10CMResponse inferICD10CM(xAmzTarget, inferICD10CMRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts. 

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.InferICD10CM"; // String | 
    InferICD10CMRequest inferICD10CMRequest = new InferICD10CMRequest(); // InferICD10CMRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      InferICD10CMResponse result = apiInstance.inferICD10CM(xAmzTarget, inferICD10CMRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inferICD10CM");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.InferICD10CM] |
| **inferICD10CMRequest** | [**InferICD10CMRequest**](InferICD10CMRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**InferICD10CMResponse**](InferICD10CMResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InvalidRequestException |  -  |
| **484** | InvalidEncodingException |  -  |
| **485** | TextSizeLimitExceededException |  -  |

<a id="inferRxNorm"></a>
# **inferRxNorm**
> InferRxNormResponse inferRxNorm(xAmzTarget, inferRxNormRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine. Amazon Comprehend Medical only detects medical entities in English language texts. 

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.InferRxNorm"; // String | 
    InferRxNormRequest inferRxNormRequest = new InferRxNormRequest(); // InferRxNormRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      InferRxNormResponse result = apiInstance.inferRxNorm(xAmzTarget, inferRxNormRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inferRxNorm");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.InferRxNorm] |
| **inferRxNormRequest** | [**InferRxNormRequest**](InferRxNormRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**InferRxNormResponse**](InferRxNormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InvalidRequestException |  -  |
| **484** | InvalidEncodingException |  -  |
| **485** | TextSizeLimitExceededException |  -  |

<a id="inferSNOMEDCT"></a>
# **inferSNOMEDCT**
> InferSNOMEDCTResponse inferSNOMEDCT(xAmzTarget, inferSNOMEDCTRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.InferSNOMEDCT"; // String | 
    InferSNOMEDCTRequest inferSNOMEDCTRequest = new InferSNOMEDCTRequest(); // InferSNOMEDCTRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      InferSNOMEDCTResponse result = apiInstance.inferSNOMEDCT(xAmzTarget, inferSNOMEDCTRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inferSNOMEDCT");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.InferSNOMEDCT] |
| **inferSNOMEDCTRequest** | [**InferSNOMEDCTRequest**](InferSNOMEDCTRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**InferSNOMEDCTResponse**](InferSNOMEDCTResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InvalidRequestException |  -  |
| **484** | InvalidEncodingException |  -  |
| **485** | TextSizeLimitExceededException |  -  |

<a id="listEntitiesDetectionV2Jobs"></a>
# **listEntitiesDetectionV2Jobs**
> ListEntitiesDetectionV2JobsResponse listEntitiesDetectionV2Jobs(xAmzTarget, listEntitiesDetectionV2JobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a list of medical entity detection jobs that you have submitted.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.ListEntitiesDetectionV2Jobs"; // String | 
    ListEntitiesDetectionV2JobsRequest listEntitiesDetectionV2JobsRequest = new ListEntitiesDetectionV2JobsRequest(); // ListEntitiesDetectionV2JobsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListEntitiesDetectionV2JobsResponse result = apiInstance.listEntitiesDetectionV2Jobs(xAmzTarget, listEntitiesDetectionV2JobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listEntitiesDetectionV2Jobs");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.ListEntitiesDetectionV2Jobs] |
| **listEntitiesDetectionV2JobsRequest** | [**ListEntitiesDetectionV2JobsRequest**](ListEntitiesDetectionV2JobsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListEntitiesDetectionV2JobsResponse**](ListEntitiesDetectionV2JobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ValidationException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InternalServerException |  -  |

<a id="listICD10CMInferenceJobs"></a>
# **listICD10CMInferenceJobs**
> ListICD10CMInferenceJobsResponse listICD10CMInferenceJobs(xAmzTarget, listICD10CMInferenceJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a list of InferICD10CM jobs that you have submitted.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.ListICD10CMInferenceJobs"; // String | 
    ListICD10CMInferenceJobsRequest listICD10CMInferenceJobsRequest = new ListICD10CMInferenceJobsRequest(); // ListICD10CMInferenceJobsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListICD10CMInferenceJobsResponse result = apiInstance.listICD10CMInferenceJobs(xAmzTarget, listICD10CMInferenceJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listICD10CMInferenceJobs");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.ListICD10CMInferenceJobs] |
| **listICD10CMInferenceJobsRequest** | [**ListICD10CMInferenceJobsRequest**](ListICD10CMInferenceJobsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListICD10CMInferenceJobsResponse**](ListICD10CMInferenceJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ValidationException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InternalServerException |  -  |

<a id="listPHIDetectionJobs"></a>
# **listPHIDetectionJobs**
> ListPHIDetectionJobsResponse listPHIDetectionJobs(xAmzTarget, listPHIDetectionJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a list of protected health information (PHI) detection jobs you have submitted.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.ListPHIDetectionJobs"; // String | 
    ListPHIDetectionJobsRequest listPHIDetectionJobsRequest = new ListPHIDetectionJobsRequest(); // ListPHIDetectionJobsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListPHIDetectionJobsResponse result = apiInstance.listPHIDetectionJobs(xAmzTarget, listPHIDetectionJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPHIDetectionJobs");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.ListPHIDetectionJobs] |
| **listPHIDetectionJobsRequest** | [**ListPHIDetectionJobsRequest**](ListPHIDetectionJobsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListPHIDetectionJobsResponse**](ListPHIDetectionJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ValidationException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InternalServerException |  -  |

<a id="listRxNormInferenceJobs"></a>
# **listRxNormInferenceJobs**
> ListRxNormInferenceJobsResponse listRxNormInferenceJobs(xAmzTarget, listRxNormInferenceJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a list of InferRxNorm jobs that you have submitted.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.ListRxNormInferenceJobs"; // String | 
    ListRxNormInferenceJobsRequest listRxNormInferenceJobsRequest = new ListRxNormInferenceJobsRequest(); // ListRxNormInferenceJobsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListRxNormInferenceJobsResponse result = apiInstance.listRxNormInferenceJobs(xAmzTarget, listRxNormInferenceJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRxNormInferenceJobs");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.ListRxNormInferenceJobs] |
| **listRxNormInferenceJobsRequest** | [**ListRxNormInferenceJobsRequest**](ListRxNormInferenceJobsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListRxNormInferenceJobsResponse**](ListRxNormInferenceJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ValidationException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InternalServerException |  -  |

<a id="listSNOMEDCTInferenceJobs"></a>
# **listSNOMEDCTInferenceJobs**
> ListSNOMEDCTInferenceJobsResponse listSNOMEDCTInferenceJobs(xAmzTarget, listSNOMEDCTInferenceJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Gets a list of InferSNOMEDCT jobs a user has submitted. 

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.ListSNOMEDCTInferenceJobs"; // String | 
    ListSNOMEDCTInferenceJobsRequest listSNOMEDCTInferenceJobsRequest = new ListSNOMEDCTInferenceJobsRequest(); // ListSNOMEDCTInferenceJobsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListSNOMEDCTInferenceJobsResponse result = apiInstance.listSNOMEDCTInferenceJobs(xAmzTarget, listSNOMEDCTInferenceJobsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSNOMEDCTInferenceJobs");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.ListSNOMEDCTInferenceJobs] |
| **listSNOMEDCTInferenceJobsRequest** | [**ListSNOMEDCTInferenceJobsRequest**](ListSNOMEDCTInferenceJobsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListSNOMEDCTInferenceJobsResponse**](ListSNOMEDCTInferenceJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ValidationException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InternalServerException |  -  |

<a id="startEntitiesDetectionV2Job"></a>
# **startEntitiesDetectionV2Job**
> StartEntitiesDetectionV2JobResponse startEntitiesDetectionV2Job(xAmzTarget, startEntitiesDetectionV2JobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Starts an asynchronous medical entity detection job for a collection of documents. Use the &lt;code&gt;DescribeEntitiesDetectionV2Job&lt;/code&gt; operation to track the status of a job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StartEntitiesDetectionV2Job"; // String | 
    StartEntitiesDetectionV2JobRequest startEntitiesDetectionV2JobRequest = new StartEntitiesDetectionV2JobRequest(); // StartEntitiesDetectionV2JobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartEntitiesDetectionV2JobResponse result = apiInstance.startEntitiesDetectionV2Job(xAmzTarget, startEntitiesDetectionV2JobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startEntitiesDetectionV2Job");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StartEntitiesDetectionV2Job] |
| **startEntitiesDetectionV2JobRequest** | [**StartEntitiesDetectionV2JobRequest**](StartEntitiesDetectionV2JobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartEntitiesDetectionV2JobResponse**](StartEntitiesDetectionV2JobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="startICD10CMInferenceJob"></a>
# **startICD10CMInferenceJob**
> StartICD10CMInferenceJobResponse startICD10CMInferenceJob(xAmzTarget, startICD10CMInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Starts an asynchronous job to detect medical conditions and link them to the ICD-10-CM ontology. Use the &lt;code&gt;DescribeICD10CMInferenceJob&lt;/code&gt; operation to track the status of a job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StartICD10CMInferenceJob"; // String | 
    StartICD10CMInferenceJobRequest startICD10CMInferenceJobRequest = new StartICD10CMInferenceJobRequest(); // StartICD10CMInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartICD10CMInferenceJobResponse result = apiInstance.startICD10CMInferenceJob(xAmzTarget, startICD10CMInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startICD10CMInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StartICD10CMInferenceJob] |
| **startICD10CMInferenceJobRequest** | [**StartICD10CMInferenceJobRequest**](StartICD10CMInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartICD10CMInferenceJobResponse**](StartICD10CMInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="startPHIDetectionJob"></a>
# **startPHIDetectionJob**
> StartPHIDetectionJobResponse startPHIDetectionJob(xAmzTarget, startPHIDetectionJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Starts an asynchronous job to detect protected health information (PHI). Use the &lt;code&gt;DescribePHIDetectionJob&lt;/code&gt; operation to track the status of a job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StartPHIDetectionJob"; // String | 
    StartPHIDetectionJobRequest startPHIDetectionJobRequest = new StartPHIDetectionJobRequest(); // StartPHIDetectionJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartPHIDetectionJobResponse result = apiInstance.startPHIDetectionJob(xAmzTarget, startPHIDetectionJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startPHIDetectionJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StartPHIDetectionJob] |
| **startPHIDetectionJobRequest** | [**StartPHIDetectionJobRequest**](StartPHIDetectionJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartPHIDetectionJobResponse**](StartPHIDetectionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="startRxNormInferenceJob"></a>
# **startRxNormInferenceJob**
> StartRxNormInferenceJobResponse startRxNormInferenceJob(xAmzTarget, startRxNormInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology. Use the &lt;code&gt;DescribeRxNormInferenceJob&lt;/code&gt; operation to track the status of a job.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StartRxNormInferenceJob"; // String | 
    StartRxNormInferenceJobRequest startRxNormInferenceJobRequest = new StartRxNormInferenceJobRequest(); // StartRxNormInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartRxNormInferenceJobResponse result = apiInstance.startRxNormInferenceJob(xAmzTarget, startRxNormInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startRxNormInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StartRxNormInferenceJob] |
| **startRxNormInferenceJobRequest** | [**StartRxNormInferenceJobRequest**](StartRxNormInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartRxNormInferenceJobResponse**](StartRxNormInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="startSNOMEDCTInferenceJob"></a>
# **startSNOMEDCTInferenceJob**
> StartSNOMEDCTInferenceJobResponse startSNOMEDCTInferenceJob(xAmzTarget, startSNOMEDCTInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Starts an asynchronous job to detect medical concepts and link them to the SNOMED-CT ontology. Use the DescribeSNOMEDCTInferenceJob operation to track the status of a job. 

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StartSNOMEDCTInferenceJob"; // String | 
    StartSNOMEDCTInferenceJobRequest startSNOMEDCTInferenceJobRequest = new StartSNOMEDCTInferenceJobRequest(); // StartSNOMEDCTInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartSNOMEDCTInferenceJobResponse result = apiInstance.startSNOMEDCTInferenceJob(xAmzTarget, startSNOMEDCTInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startSNOMEDCTInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StartSNOMEDCTInferenceJob] |
| **startSNOMEDCTInferenceJobRequest** | [**StartSNOMEDCTInferenceJobRequest**](StartSNOMEDCTInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartSNOMEDCTInferenceJobResponse**](StartSNOMEDCTInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | TooManyRequestsException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="stopEntitiesDetectionV2Job"></a>
# **stopEntitiesDetectionV2Job**
> StopEntitiesDetectionV2JobResponse stopEntitiesDetectionV2Job(xAmzTarget, stopEntitiesDetectionV2JobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stops a medical entities detection job in progress.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StopEntitiesDetectionV2Job"; // String | 
    StopEntitiesDetectionV2JobRequest stopEntitiesDetectionV2JobRequest = new StopEntitiesDetectionV2JobRequest(); // StopEntitiesDetectionV2JobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopEntitiesDetectionV2JobResponse result = apiInstance.stopEntitiesDetectionV2Job(xAmzTarget, stopEntitiesDetectionV2JobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopEntitiesDetectionV2Job");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StopEntitiesDetectionV2Job] |
| **stopEntitiesDetectionV2JobRequest** | [**StopEntitiesDetectionV2JobRequest**](StopEntitiesDetectionV2JobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopEntitiesDetectionV2JobResponse**](StopEntitiesDetectionV2JobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="stopICD10CMInferenceJob"></a>
# **stopICD10CMInferenceJob**
> StopICD10CMInferenceJobResponse stopICD10CMInferenceJob(xAmzTarget, stopICD10CMInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stops an InferICD10CM inference job in progress.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StopICD10CMInferenceJob"; // String | 
    StopICD10CMInferenceJobRequest stopICD10CMInferenceJobRequest = new StopICD10CMInferenceJobRequest(); // StopICD10CMInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopICD10CMInferenceJobResponse result = apiInstance.stopICD10CMInferenceJob(xAmzTarget, stopICD10CMInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopICD10CMInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StopICD10CMInferenceJob] |
| **stopICD10CMInferenceJobRequest** | [**StopICD10CMInferenceJobRequest**](StopICD10CMInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopICD10CMInferenceJobResponse**](StopICD10CMInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="stopPHIDetectionJob"></a>
# **stopPHIDetectionJob**
> StopPHIDetectionJobResponse stopPHIDetectionJob(xAmzTarget, stopPHIDetectionJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stops a protected health information (PHI) detection job in progress.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StopPHIDetectionJob"; // String | 
    StopPHIDetectionJobRequest stopPHIDetectionJobRequest = new StopPHIDetectionJobRequest(); // StopPHIDetectionJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopPHIDetectionJobResponse result = apiInstance.stopPHIDetectionJob(xAmzTarget, stopPHIDetectionJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopPHIDetectionJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StopPHIDetectionJob] |
| **stopPHIDetectionJobRequest** | [**StopPHIDetectionJobRequest**](StopPHIDetectionJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopPHIDetectionJobResponse**](StopPHIDetectionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="stopRxNormInferenceJob"></a>
# **stopRxNormInferenceJob**
> StopRxNormInferenceJobResponse stopRxNormInferenceJob(xAmzTarget, stopRxNormInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stops an InferRxNorm inference job in progress.

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StopRxNormInferenceJob"; // String | 
    StopRxNormInferenceJobRequest stopRxNormInferenceJobRequest = new StopRxNormInferenceJobRequest(); // StopRxNormInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopRxNormInferenceJobResponse result = apiInstance.stopRxNormInferenceJob(xAmzTarget, stopRxNormInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopRxNormInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StopRxNormInferenceJob] |
| **stopRxNormInferenceJobRequest** | [**StopRxNormInferenceJobRequest**](StopRxNormInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopRxNormInferenceJobResponse**](StopRxNormInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InternalServerException |  -  |

<a id="stopSNOMEDCTInferenceJob"></a>
# **stopSNOMEDCTInferenceJob**
> StopSNOMEDCTInferenceJobResponse stopSNOMEDCTInferenceJob(xAmzTarget, stopSNOMEDCTInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Stops an InferSNOMEDCT inference job in progress. 

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
    defaultClient.setBasePath("http://comprehendmedical.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ComprehendMedical_20181030.StopSNOMEDCTInferenceJob"; // String | 
    StopSNOMEDCTInferenceJobRequest stopSNOMEDCTInferenceJobRequest = new StopSNOMEDCTInferenceJobRequest(); // StopSNOMEDCTInferenceJobRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopSNOMEDCTInferenceJobResponse result = apiInstance.stopSNOMEDCTInferenceJob(xAmzTarget, stopSNOMEDCTInferenceJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopSNOMEDCTInferenceJob");
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
| **xAmzTarget** | **String**|  | [enum: ComprehendMedical_20181030.StopSNOMEDCTInferenceJob] |
| **stopSNOMEDCTInferenceJobRequest** | [**StopSNOMEDCTInferenceJobRequest**](StopSNOMEDCTInferenceJobRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopSNOMEDCTInferenceJobResponse**](StopSNOMEDCTInferenceJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | InternalServerException |  -  |

