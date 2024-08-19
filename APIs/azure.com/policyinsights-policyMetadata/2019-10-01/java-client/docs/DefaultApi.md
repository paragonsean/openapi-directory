# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyMetadataGetResource**](DefaultApi.md#policyMetadataGetResource) | **GET** /providers/Microsoft.PolicyInsights/policyMetadata/{resourceName} |  |
| [**policyMetadataList**](DefaultApi.md#policyMetadataList) | **GET** /providers/Microsoft.PolicyInsights/policyMetadata |  |


<a id="policyMetadataGetResource"></a>
# **policyMetadataGetResource**
> PolicyMetadata policyMetadataGetResource(resourceName, apiVersion)



Get policy metadata resource.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceName = "resourceName_example"; // String | The name of the policy metadata resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PolicyMetadata result = apiInstance.policyMetadataGetResource(resourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyMetadataGetResource");
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
| **resourceName** | **String**| The name of the policy metadata resource. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PolicyMetadata**](PolicyMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy metadata resource definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyMetadataList"></a>
# **policyMetadataList**
> PolicyMetadataCollection policyMetadataList(apiVersion, $top)



Get a list of the policy metadata resources.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    try {
      PolicyMetadataCollection result = apiInstance.policyMetadataList(apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyMetadataList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |

### Return type

[**PolicyMetadataCollection**](PolicyMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy metadata resource collection. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

