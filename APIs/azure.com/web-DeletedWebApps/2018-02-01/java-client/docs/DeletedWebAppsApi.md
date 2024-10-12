# DeletedWebAppsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletedWebAppsGetDeletedWebAppByLocation**](DeletedWebAppsApi.md#deletedWebAppsGetDeletedWebAppByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/deletedSites/{deletedSiteId} | Get deleted app for a subscription at location. |
| [**deletedWebAppsList**](DeletedWebAppsApi.md#deletedWebAppsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites | Get all deleted apps for a subscription. |
| [**deletedWebAppsListByLocation**](DeletedWebAppsApi.md#deletedWebAppsListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/deletedSites | Get all deleted apps for a subscription at location |


<a id="deletedWebAppsGetDeletedWebAppByLocation"></a>
# **deletedWebAppsGetDeletedWebAppByLocation**
> DeletedWebAppsGetDeletedWebAppByLocation200Response deletedWebAppsGetDeletedWebAppByLocation(location, deletedSiteId, subscriptionId, apiVersion)

Get deleted app for a subscription at location.

Get deleted app for a subscription at location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedWebAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeletedWebAppsApi apiInstance = new DeletedWebAppsApi(defaultClient);
    String location = "location_example"; // String | 
    String deletedSiteId = "deletedSiteId_example"; // String | The numeric ID of the deleted app, e.g. 12345
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeletedWebAppsGetDeletedWebAppByLocation200Response result = apiInstance.deletedWebAppsGetDeletedWebAppByLocation(location, deletedSiteId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedWebAppsApi#deletedWebAppsGetDeletedWebAppByLocation");
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
| **location** | **String**|  | |
| **deletedSiteId** | **String**| The numeric ID of the deleted app, e.g. 12345 | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeletedWebAppsGetDeletedWebAppByLocation200Response**](DeletedWebAppsGetDeletedWebAppByLocation200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="deletedWebAppsList"></a>
# **deletedWebAppsList**
> DeletedWebAppCollection deletedWebAppsList(subscriptionId, apiVersion)

Get all deleted apps for a subscription.

Get all deleted apps for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedWebAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeletedWebAppsApi apiInstance = new DeletedWebAppsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeletedWebAppCollection result = apiInstance.deletedWebAppsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedWebAppsApi#deletedWebAppsList");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeletedWebAppCollection**](DeletedWebAppCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="deletedWebAppsListByLocation"></a>
# **deletedWebAppsListByLocation**
> DeletedWebAppCollection deletedWebAppsListByLocation(location, subscriptionId, apiVersion)

Get all deleted apps for a subscription at location

Get all deleted apps for a subscription at location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedWebAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeletedWebAppsApi apiInstance = new DeletedWebAppsApi(defaultClient);
    String location = "location_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeletedWebAppCollection result = apiInstance.deletedWebAppsListByLocation(location, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedWebAppsApi#deletedWebAppsListByLocation");
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
| **location** | **String**|  | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeletedWebAppCollection**](DeletedWebAppCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

