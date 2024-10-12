# ManagedApisApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedApisGet**](ManagedApisApi.md#managedApisGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis/{apiName} | Gets managed API |
| [**managedApisList**](ManagedApisApi.md#managedApisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis | Lists managed APIs |


<a id="managedApisGet"></a>
# **managedApisGet**
> ManagedApiDefinition managedApisGet(subscriptionId, location, apiName, apiVersion)

Gets managed API

Gets a managed API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApisApi apiInstance = new ManagedApisApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String location = "location_example"; // String | The location
    String apiName = "apiName_example"; // String | API name
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ManagedApiDefinition result = apiInstance.managedApisGet(subscriptionId, location, apiName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApisApi#managedApisGet");
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
| **subscriptionId** | **String**| Subscription Id | |
| **location** | **String**| The location | |
| **apiName** | **String**| API name | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ManagedApiDefinition**](ManagedApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A managed API definition |  -  |

<a id="managedApisList"></a>
# **managedApisList**
> ManagedApiDefinitionCollection managedApisList(location, subscriptionId, apiVersion)

Lists managed APIs

Gets a list of managed APIs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApisApi apiInstance = new ManagedApisApi(defaultClient);
    String location = "location_example"; // String | The location
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ManagedApiDefinitionCollection result = apiInstance.managedApisList(location, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApisApi#managedApisList");
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
| **location** | **String**| The location | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ManagedApiDefinitionCollection**](ManagedApiDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of managed APIs |  -  |

