# AssessmentsMetadataApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assessmentsMetadataGet**](AssessmentsMetadataApi.md#assessmentsMetadataGet) | **GET** /providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} |  |
| [**assessmentsMetadataList**](AssessmentsMetadataApi.md#assessmentsMetadataList) | **GET** /providers/Microsoft.Security/assessmentMetadata |  |
| [**assessmentsMetadataSubscriptionCreate**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} |  |
| [**assessmentsMetadataSubscriptionDelete**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} |  |
| [**assessmentsMetadataSubscriptionGet**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} |  |
| [**assessmentsMetadataSubscriptionList**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata |  |


<a id="assessmentsMetadataGet"></a>
# **assessmentsMetadataGet**
> SecurityAssessmentMetadata assessmentsMetadataGet(apiVersion, assessmentMetadataName)



Get metadata information on an assessment type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssessmentsMetadataApi apiInstance = new AssessmentsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
    try {
      SecurityAssessmentMetadata result = apiInstance.assessmentsMetadataGet(apiVersion, assessmentMetadataName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentsMetadataApi#assessmentsMetadataGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | |

### Return type

[**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsMetadataList"></a>
# **assessmentsMetadataList**
> SecurityAssessmentMetadataList assessmentsMetadataList(apiVersion)



Get metadata information on all assessment types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssessmentsMetadataApi apiInstance = new AssessmentsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    try {
      SecurityAssessmentMetadataList result = apiInstance.assessmentsMetadataList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentsMetadataApi#assessmentsMetadataList");
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
| **apiVersion** | **String**| API version for the operation | |

### Return type

[**SecurityAssessmentMetadataList**](SecurityAssessmentMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsMetadataSubscriptionCreate"></a>
# **assessmentsMetadataSubscriptionCreate**
> SecurityAssessmentMetadata assessmentsMetadataSubscriptionCreate(apiVersion, assessmentMetadataName, subscriptionId, assessmentMetadata)



Create metadata information on an assessment type in a specific subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssessmentsMetadataApi apiInstance = new AssessmentsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    SecurityAssessmentMetadata assessmentMetadata = new SecurityAssessmentMetadata(); // SecurityAssessmentMetadata | AssessmentMetadata object
    try {
      SecurityAssessmentMetadata result = apiInstance.assessmentsMetadataSubscriptionCreate(apiVersion, assessmentMetadataName, subscriptionId, assessmentMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentsMetadataApi#assessmentsMetadataSubscriptionCreate");
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
| **apiVersion** | **String**| API version for the operation | |
| **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **assessmentMetadata** | [**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)| AssessmentMetadata object | |

### Return type

[**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsMetadataSubscriptionDelete"></a>
# **assessmentsMetadataSubscriptionDelete**
> assessmentsMetadataSubscriptionDelete(apiVersion, assessmentMetadataName, subscriptionId)



Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssessmentsMetadataApi apiInstance = new AssessmentsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      apiInstance.assessmentsMetadataSubscriptionDelete(apiVersion, assessmentMetadataName, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentsMetadataApi#assessmentsMetadataSubscriptionDelete");
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
| **apiVersion** | **String**| API version for the operation | |
| **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsMetadataSubscriptionGet"></a>
# **assessmentsMetadataSubscriptionGet**
> SecurityAssessmentMetadata assessmentsMetadataSubscriptionGet(apiVersion, assessmentMetadataName, subscriptionId)



Get metadata information on an assessment type in a specific subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssessmentsMetadataApi apiInstance = new AssessmentsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      SecurityAssessmentMetadata result = apiInstance.assessmentsMetadataSubscriptionGet(apiVersion, assessmentMetadataName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentsMetadataApi#assessmentsMetadataSubscriptionGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsMetadataSubscriptionList"></a>
# **assessmentsMetadataSubscriptionList**
> SecurityAssessmentMetadataList assessmentsMetadataSubscriptionList(apiVersion, subscriptionId)



Get metadata information on all assessment types in a specific subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssessmentsMetadataApi apiInstance = new AssessmentsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      SecurityAssessmentMetadataList result = apiInstance.assessmentsMetadataSubscriptionList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentsMetadataApi#assessmentsMetadataSubscriptionList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**SecurityAssessmentMetadataList**](SecurityAssessmentMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

