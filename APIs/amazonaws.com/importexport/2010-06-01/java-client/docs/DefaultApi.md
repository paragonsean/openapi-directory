# DefaultApi

All URIs are relative to *http://importexport.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETCancelJob**](DefaultApi.md#gETCancelJob) | **GET** /#Operation&#x3D;CancelJob&amp;Action&#x3D;CancelJob |  |
| [**gETCreateJob**](DefaultApi.md#gETCreateJob) | **GET** /#Operation&#x3D;CreateJob&amp;Action&#x3D;CreateJob |  |
| [**gETGetShippingLabel**](DefaultApi.md#gETGetShippingLabel) | **GET** /#Operation&#x3D;GetShippingLabel&amp;Action&#x3D;GetShippingLabel |  |
| [**gETGetStatus**](DefaultApi.md#gETGetStatus) | **GET** /#Operation&#x3D;GetStatus&amp;Action&#x3D;GetStatus |  |
| [**gETListJobs**](DefaultApi.md#gETListJobs) | **GET** /#Operation&#x3D;ListJobs&amp;Action&#x3D;ListJobs |  |
| [**gETUpdateJob**](DefaultApi.md#gETUpdateJob) | **GET** /#Operation&#x3D;UpdateJob&amp;Action&#x3D;UpdateJob |  |
| [**pOSTCancelJob**](DefaultApi.md#pOSTCancelJob) | **POST** /#Operation&#x3D;CancelJob&amp;Action&#x3D;CancelJob |  |
| [**pOSTCreateJob**](DefaultApi.md#pOSTCreateJob) | **POST** /#Operation&#x3D;CreateJob&amp;Action&#x3D;CreateJob |  |
| [**pOSTGetShippingLabel**](DefaultApi.md#pOSTGetShippingLabel) | **POST** /#Operation&#x3D;GetShippingLabel&amp;Action&#x3D;GetShippingLabel |  |
| [**pOSTGetStatus**](DefaultApi.md#pOSTGetStatus) | **POST** /#Operation&#x3D;GetStatus&amp;Action&#x3D;GetStatus |  |
| [**pOSTListJobs**](DefaultApi.md#pOSTListJobs) | **POST** /#Operation&#x3D;ListJobs&amp;Action&#x3D;ListJobs |  |
| [**pOSTUpdateJob**](DefaultApi.md#pOSTUpdateJob) | **POST** /#Operation&#x3D;UpdateJob&amp;Action&#x3D;UpdateJob |  |


<a id="gETCancelJob"></a>
# **gETCancelJob**
> CancelJobOutput gETCancelJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, apIVersion)



This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String jobId = "jobId_example"; // String | 
    String operation = "CancelJob"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    String apIVersion = "apIVersion_example"; // String | 
    try {
      CancelJobOutput result = apiInstance.gETCancelJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, apIVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETCancelJob");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **jobId** | **String**|  | |
| **operation** | **String**|  | [enum: CancelJob] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **apIVersion** | **String**|  | [optional] |

### Return type

[**CancelJobOutput**](CancelJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidJobIdException |  -  |
| **481** | ExpiredJobIdException |  -  |
| **482** | CanceledJobIdException |  -  |
| **483** | UnableToCancelJobIdException |  -  |
| **484** | InvalidAccessKeyIdException |  -  |
| **485** | InvalidVersionException |  -  |

<a id="gETCreateJob"></a>
# **gETCreateJob**
> CreateJobOutput gETCreateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobType, manifest, validateOnly, operation, action, version, manifestAddendum, apIVersion)



This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String jobType = "Import"; // String | 
    String manifest = "manifest_example"; // String | 
    Boolean validateOnly = true; // Boolean | 
    String operation = "CreateJob"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    String manifestAddendum = "manifestAddendum_example"; // String | 
    String apIVersion = "apIVersion_example"; // String | 
    try {
      CreateJobOutput result = apiInstance.gETCreateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobType, manifest, validateOnly, operation, action, version, manifestAddendum, apIVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETCreateJob");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **jobType** | **String**|  | [enum: Import, Export] |
| **manifest** | **String**|  | |
| **validateOnly** | **Boolean**|  | |
| **operation** | **String**|  | [enum: CreateJob] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **manifestAddendum** | **String**|  | [optional] |
| **apIVersion** | **String**|  | [optional] |

### Return type

[**CreateJobOutput**](CreateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | MissingParameterException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidAccessKeyIdException |  -  |
| **483** | InvalidAddressException |  -  |
| **484** | InvalidManifestFieldException |  -  |
| **485** | MissingManifestFieldException |  -  |
| **486** | NoSuchBucketException |  -  |
| **487** | MissingCustomsException |  -  |
| **488** | InvalidCustomsException |  -  |
| **489** | InvalidFileSystemException |  -  |
| **490** | MultipleRegionsException |  -  |
| **491** | BucketPermissionException |  -  |
| **492** | MalformedManifestException |  -  |
| **493** | CreateJobQuotaExceededException |  -  |
| **494** | InvalidJobIdException |  -  |
| **495** | InvalidVersionException |  -  |

<a id="gETGetShippingLabel"></a>
# **gETGetShippingLabel**
> GetShippingLabelOutput gETGetShippingLabel(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobIds, operation, action, version, name, company, phoneNumber, country, stateOrProvince, city, postalCode, street1, street2, street3, apIVersion)



This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    List<String> jobIds = Arrays.asList(); // List<String> | 
    String operation = "GetShippingLabel"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    String name = "name_example"; // String | 
    String company = "company_example"; // String | 
    String phoneNumber = "phoneNumber_example"; // String | 
    String country = "country_example"; // String | 
    String stateOrProvince = "stateOrProvince_example"; // String | 
    String city = "city_example"; // String | 
    String postalCode = "postalCode_example"; // String | 
    String street1 = "street1_example"; // String | 
    String street2 = "street2_example"; // String | 
    String street3 = "street3_example"; // String | 
    String apIVersion = "apIVersion_example"; // String | 
    try {
      GetShippingLabelOutput result = apiInstance.gETGetShippingLabel(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobIds, operation, action, version, name, company, phoneNumber, country, stateOrProvince, city, postalCode, street1, street2, street3, apIVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETGetShippingLabel");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **jobIds** | [**List&lt;String&gt;**](String.md)|  | |
| **operation** | **String**|  | [enum: GetShippingLabel] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **name** | **String**|  | [optional] |
| **company** | **String**|  | [optional] |
| **phoneNumber** | **String**|  | [optional] |
| **country** | **String**|  | [optional] |
| **stateOrProvince** | **String**|  | [optional] |
| **city** | **String**|  | [optional] |
| **postalCode** | **String**|  | [optional] |
| **street1** | **String**|  | [optional] |
| **street2** | **String**|  | [optional] |
| **street3** | **String**|  | [optional] |
| **apIVersion** | **String**|  | [optional] |

### Return type

[**GetShippingLabelOutput**](GetShippingLabelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidJobIdException |  -  |
| **481** | ExpiredJobIdException |  -  |
| **482** | CanceledJobIdException |  -  |
| **483** | InvalidAccessKeyIdException |  -  |
| **484** | InvalidAddressException |  -  |
| **485** | InvalidVersionException |  -  |
| **486** | InvalidParameterException |  -  |

<a id="gETGetStatus"></a>
# **gETGetStatus**
> GetStatusOutput gETGetStatus(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, apIVersion)



This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String jobId = "jobId_example"; // String | 
    String operation = "GetStatus"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    String apIVersion = "apIVersion_example"; // String | 
    try {
      GetStatusOutput result = apiInstance.gETGetStatus(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, operation, action, version, apIVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETGetStatus");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **jobId** | **String**|  | |
| **operation** | **String**|  | [enum: GetStatus] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **apIVersion** | **String**|  | [optional] |

### Return type

[**GetStatusOutput**](GetStatusOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidJobIdException |  -  |
| **481** | ExpiredJobIdException |  -  |
| **482** | CanceledJobIdException |  -  |
| **483** | InvalidAccessKeyIdException |  -  |
| **484** | InvalidVersionException |  -  |

<a id="gETListJobs"></a>
# **gETListJobs**
> ListJobsOutput gETListJobs(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, maxJobs, marker, apIVersion)



This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "ListJobs"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    Integer maxJobs = 56; // Integer | 
    String marker = "marker_example"; // String | 
    String apIVersion = "apIVersion_example"; // String | 
    try {
      ListJobsOutput result = apiInstance.gETListJobs(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, maxJobs, marker, apIVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETListJobs");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: ListJobs] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **maxJobs** | **Integer**|  | [optional] |
| **marker** | **String**|  | [optional] |
| **apIVersion** | **String**|  | [optional] |

### Return type

[**ListJobsOutput**](ListJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidAccessKeyIdException |  -  |
| **482** | InvalidVersionException |  -  |

<a id="gETUpdateJob"></a>
# **gETUpdateJob**
> UpdateJobOutput gETUpdateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, manifest, jobType, validateOnly, operation, action, version, apIVersion)



You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String jobId = "jobId_example"; // String | 
    String manifest = "manifest_example"; // String | 
    String jobType = "Import"; // String | 
    Boolean validateOnly = true; // Boolean | 
    String operation = "UpdateJob"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    String apIVersion = "apIVersion_example"; // String | 
    try {
      UpdateJobOutput result = apiInstance.gETUpdateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, jobId, manifest, jobType, validateOnly, operation, action, version, apIVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETUpdateJob");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **jobId** | **String**|  | |
| **manifest** | **String**|  | |
| **jobType** | **String**|  | [enum: Import, Export] |
| **validateOnly** | **Boolean**|  | |
| **operation** | **String**|  | [enum: UpdateJob] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **apIVersion** | **String**|  | [optional] |

### Return type

[**UpdateJobOutput**](UpdateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | MissingParameterException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidAccessKeyIdException |  -  |
| **483** | InvalidAddressException |  -  |
| **484** | InvalidManifestFieldException |  -  |
| **485** | InvalidJobIdException |  -  |
| **486** | MissingManifestFieldException |  -  |
| **487** | NoSuchBucketException |  -  |
| **488** | ExpiredJobIdException |  -  |
| **489** | CanceledJobIdException |  -  |
| **490** | MissingCustomsException |  -  |
| **491** | InvalidCustomsException |  -  |
| **492** | InvalidFileSystemException |  -  |
| **493** | MultipleRegionsException |  -  |
| **494** | BucketPermissionException |  -  |
| **495** | MalformedManifestException |  -  |
| **496** | UnableToUpdateJobIdException |  -  |
| **497** | InvalidVersionException |  -  |

<a id="pOSTCancelJob"></a>
# **pOSTCancelJob**
> CancelJobOutput pOSTCancelJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, cancelJobInput)



This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "CancelJob"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    CancelJobInput cancelJobInput = new CancelJobInput(); // CancelJobInput | 
    try {
      CancelJobOutput result = apiInstance.pOSTCancelJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, cancelJobInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTCancelJob");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: CancelJob] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **cancelJobInput** | [**CancelJobInput**](CancelJobInput.md)|  | [optional] |

### Return type

[**CancelJobOutput**](CancelJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidJobIdException |  -  |
| **481** | ExpiredJobIdException |  -  |
| **482** | CanceledJobIdException |  -  |
| **483** | UnableToCancelJobIdException |  -  |
| **484** | InvalidAccessKeyIdException |  -  |
| **485** | InvalidVersionException |  -  |

<a id="pOSTCreateJob"></a>
# **pOSTCreateJob**
> CreateJobOutput pOSTCreateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, createJobInput)



This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "CreateJob"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    CreateJobInput createJobInput = new CreateJobInput(); // CreateJobInput | 
    try {
      CreateJobOutput result = apiInstance.pOSTCreateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, createJobInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTCreateJob");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: CreateJob] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **createJobInput** | [**CreateJobInput**](CreateJobInput.md)|  | [optional] |

### Return type

[**CreateJobOutput**](CreateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | MissingParameterException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidAccessKeyIdException |  -  |
| **483** | InvalidAddressException |  -  |
| **484** | InvalidManifestFieldException |  -  |
| **485** | MissingManifestFieldException |  -  |
| **486** | NoSuchBucketException |  -  |
| **487** | MissingCustomsException |  -  |
| **488** | InvalidCustomsException |  -  |
| **489** | InvalidFileSystemException |  -  |
| **490** | MultipleRegionsException |  -  |
| **491** | BucketPermissionException |  -  |
| **492** | MalformedManifestException |  -  |
| **493** | CreateJobQuotaExceededException |  -  |
| **494** | InvalidJobIdException |  -  |
| **495** | InvalidVersionException |  -  |

<a id="pOSTGetShippingLabel"></a>
# **pOSTGetShippingLabel**
> GetShippingLabelOutput pOSTGetShippingLabel(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, getShippingLabelInput)



This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "GetShippingLabel"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    GetShippingLabelInput getShippingLabelInput = new GetShippingLabelInput(); // GetShippingLabelInput | 
    try {
      GetShippingLabelOutput result = apiInstance.pOSTGetShippingLabel(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, getShippingLabelInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTGetShippingLabel");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: GetShippingLabel] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **getShippingLabelInput** | [**GetShippingLabelInput**](GetShippingLabelInput.md)|  | [optional] |

### Return type

[**GetShippingLabelOutput**](GetShippingLabelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidJobIdException |  -  |
| **481** | ExpiredJobIdException |  -  |
| **482** | CanceledJobIdException |  -  |
| **483** | InvalidAccessKeyIdException |  -  |
| **484** | InvalidAddressException |  -  |
| **485** | InvalidVersionException |  -  |
| **486** | InvalidParameterException |  -  |

<a id="pOSTGetStatus"></a>
# **pOSTGetStatus**
> GetStatusOutput pOSTGetStatus(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, getStatusInput)



This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "GetStatus"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    GetStatusInput getStatusInput = new GetStatusInput(); // GetStatusInput | 
    try {
      GetStatusOutput result = apiInstance.pOSTGetStatus(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, getStatusInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTGetStatus");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: GetStatus] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **getStatusInput** | [**GetStatusInput**](GetStatusInput.md)|  | [optional] |

### Return type

[**GetStatusOutput**](GetStatusOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidJobIdException |  -  |
| **481** | ExpiredJobIdException |  -  |
| **482** | CanceledJobIdException |  -  |
| **483** | InvalidAccessKeyIdException |  -  |
| **484** | InvalidVersionException |  -  |

<a id="pOSTListJobs"></a>
# **pOSTListJobs**
> ListJobsOutput pOSTListJobs(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, maxJobs, marker, listJobsInput)



This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "ListJobs"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    String maxJobs = "maxJobs_example"; // String | Pagination limit
    String marker = "marker_example"; // String | Pagination token
    ListJobsInput listJobsInput = new ListJobsInput(); // ListJobsInput | 
    try {
      ListJobsOutput result = apiInstance.pOSTListJobs(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, maxJobs, marker, listJobsInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTListJobs");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: ListJobs] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **maxJobs** | **String**| Pagination limit | [optional] |
| **marker** | **String**| Pagination token | [optional] |
| **listJobsInput** | [**ListJobsInput**](ListJobsInput.md)|  | [optional] |

### Return type

[**ListJobsOutput**](ListJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidAccessKeyIdException |  -  |
| **482** | InvalidVersionException |  -  |

<a id="pOSTUpdateJob"></a>
# **pOSTUpdateJob**
> UpdateJobOutput pOSTUpdateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, updateJobInput)



You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

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
    defaultClient.setBasePath("http://importexport.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String awSAccessKeyId = "awSAccessKeyId_example"; // String | 
    String signatureMethod = "signatureMethod_example"; // String | 
    String signatureVersion = "signatureVersion_example"; // String | 
    String timestamp = "timestamp_example"; // String | 
    String signature = "signature_example"; // String | 
    String operation = "UpdateJob"; // String | 
    String action = "action_example"; // String | 
    String version = "version_example"; // String | 
    UpdateJobInput updateJobInput = new UpdateJobInput(); // UpdateJobInput | 
    try {
      UpdateJobOutput result = apiInstance.pOSTUpdateJob(awSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, operation, action, version, updateJobInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pOSTUpdateJob");
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
| **awSAccessKeyId** | **String**|  | |
| **signatureMethod** | **String**|  | |
| **signatureVersion** | **String**|  | |
| **timestamp** | **String**|  | |
| **signature** | **String**|  | |
| **operation** | **String**|  | [enum: UpdateJob] |
| **action** | **String**|  | |
| **version** | **String**|  | |
| **updateJobInput** | [**UpdateJobInput**](UpdateJobInput.md)|  | [optional] |

### Return type

[**UpdateJobOutput**](UpdateJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | MissingParameterException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | InvalidAccessKeyIdException |  -  |
| **483** | InvalidAddressException |  -  |
| **484** | InvalidManifestFieldException |  -  |
| **485** | InvalidJobIdException |  -  |
| **486** | MissingManifestFieldException |  -  |
| **487** | NoSuchBucketException |  -  |
| **488** | ExpiredJobIdException |  -  |
| **489** | CanceledJobIdException |  -  |
| **490** | MissingCustomsException |  -  |
| **491** | InvalidCustomsException |  -  |
| **492** | InvalidFileSystemException |  -  |
| **493** | MultipleRegionsException |  -  |
| **494** | BucketPermissionException |  -  |
| **495** | MalformedManifestException |  -  |
| **496** | UnableToUpdateJobIdException |  -  |
| **497** | InvalidVersionException |  -  |

