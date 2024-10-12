# ManagedApisApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedApisGet**](ManagedApisApi.md#managedApisGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis/{apiName} | Get managed API |
| [**managedApisList**](ManagedApisApi.md#managedApisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis | List managed Apis |


<a id="managedApisGet"></a>
# **managedApisGet**
> ApiEntity managedApisGet(location, apiName, subscriptionId, apiVersion, export)

Get managed API

Gets a managed API.

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
    String location = "location_example"; // String | The location.
    String apiName = "apiName_example"; // String | The managed API name.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean export = true; // Boolean | flag showing whether to export API definition in format specified by Accept header.
    try {
      ApiEntity result = apiInstance.managedApisGet(location, apiName, subscriptionId, apiVersion, export);
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
| **location** | **String**| The location. | |
| **apiName** | **String**| The managed API name. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **export** | **Boolean**| flag showing whether to export API definition in format specified by Accept header. | [optional] |

### Return type

[**ApiEntity**](ApiEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedApisList"></a>
# **managedApisList**
> ApisCollection managedApisList(location, subscriptionId, apiVersion)

List managed Apis

Gets a list of managed APIs.

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
    String location = "location_example"; // String | The location.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ApisCollection result = apiInstance.managedApisList(location, subscriptionId, apiVersion);
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
| **location** | **String**| The location. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ApisCollection**](ApisCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

