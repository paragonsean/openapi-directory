# SuppressionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**suppressionsCreate**](SuppressionsApi.md#suppressionsCreate) | **PUT** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name} |  |
| [**suppressionsDelete**](SuppressionsApi.md#suppressionsDelete) | **DELETE** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name} |  |
| [**suppressionsGet**](SuppressionsApi.md#suppressionsGet) | **GET** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name} |  |
| [**suppressionsList**](SuppressionsApi.md#suppressionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/suppressions |  |


<a id="suppressionsCreate"></a>
# **suppressionsCreate**
> SuppressionContract suppressionsCreate(resourceUri, recommendationId, name, apiVersion, suppressionContract)



Enables the snoozed or dismissed attribute of a recommendation. The snoozed or dismissed attribute is referred to as a suppression. Use this API to create or update the snoozed or dismissed status of a recommendation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppressionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SuppressionsApi apiInstance = new SuppressionsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    String recommendationId = "recommendationId_example"; // String | The recommendation ID.
    String name = "name_example"; // String | The name of the suppression.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    SuppressionContract suppressionContract = new SuppressionContract(); // SuppressionContract | The snoozed or dismissed attribute; for example, the snooze duration.
    try {
      SuppressionContract result = apiInstance.suppressionsCreate(resourceUri, recommendationId, name, apiVersion, suppressionContract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppressionsApi#suppressionsCreate");
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
| **resourceUri** | **String**| The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. | |
| **recommendationId** | **String**| The recommendation ID. | |
| **name** | **String**| The name of the suppression. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **suppressionContract** | [**SuppressionContract**](SuppressionContract.md)| The snoozed or dismissed attribute; for example, the snooze duration. | |

### Return type

[**SuppressionContract**](SuppressionContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully created suppression. |  -  |

<a id="suppressionsDelete"></a>
# **suppressionsDelete**
> suppressionsDelete(resourceUri, recommendationId, name, apiVersion)



Enables the activation of a snoozed or dismissed recommendation. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppressionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SuppressionsApi apiInstance = new SuppressionsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    String recommendationId = "recommendationId_example"; // String | The recommendation ID.
    String name = "name_example"; // String | The name of the suppression.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      apiInstance.suppressionsDelete(resourceUri, recommendationId, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppressionsApi#suppressionsDelete");
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
| **resourceUri** | **String**| The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. | |
| **recommendationId** | **String**| The recommendation ID. | |
| **name** | **String**| The name of the suppression. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | NoContent. The recommendation has been activated. |  -  |

<a id="suppressionsGet"></a>
# **suppressionsGet**
> SuppressionContract suppressionsGet(resourceUri, recommendationId, name, apiVersion)



Obtains the details of a suppression.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppressionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SuppressionsApi apiInstance = new SuppressionsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    String recommendationId = "recommendationId_example"; // String | The recommendation ID.
    String name = "name_example"; // String | The name of the suppression.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      SuppressionContract result = apiInstance.suppressionsGet(resourceUri, recommendationId, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppressionsApi#suppressionsGet");
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
| **resourceUri** | **String**| The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. | |
| **recommendationId** | **String**| The recommendation ID. | |
| **name** | **String**| The name of the suppression. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**SuppressionContract**](SuppressionContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully got suppression detail. |  -  |

<a id="suppressionsList"></a>
# **suppressionsList**
> SuppressionContractListResult suppressionsList(subscriptionId, apiVersion, $top, $skipToken)



Retrieves the list of snoozed or dismissed suppressions for a subscription. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuppressionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SuppressionsApi apiInstance = new SuppressionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Integer $top = 56; // Integer | The number of suppressions per page if a paged version of this API is being used.
    String $skipToken = "$skipToken_example"; // String | The page-continuation token to use with a paged version of this API.
    try {
      SuppressionContractListResult result = apiInstance.suppressionsList(subscriptionId, apiVersion, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuppressionsApi#suppressionsList");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$top** | **Integer**| The number of suppressions per page if a paged version of this API is being used. | [optional] |
| **$skipToken** | **String**| The page-continuation token to use with a paged version of this API. | [optional] |

### Return type

[**SuppressionContractListResult**](SuppressionContractListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully got all suppressions in a subscription. |  -  |

