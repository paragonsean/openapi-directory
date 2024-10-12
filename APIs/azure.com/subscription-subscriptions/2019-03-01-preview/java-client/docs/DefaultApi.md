# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionsCancel**](DefaultApi.md#subscriptionsCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/cancel |  |
| [**subscriptionsEnable**](DefaultApi.md#subscriptionsEnable) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/enable |  |
| [**subscriptionsRename**](DefaultApi.md#subscriptionsRename) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/rename |  |


<a id="subscriptionsCancel"></a>
# **subscriptionsCancel**
> CanceledSubscriptionId subscriptionsCancel(subscriptionId, apiVersion)



The operation to cancel a subscription

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-03-01-preview
    try {
      CanceledSubscriptionId result = apiInstance.subscriptionsCancel(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionsCancel");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-03-01-preview | |

### Return type

[**CanceledSubscriptionId**](CanceledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Describes the error if the operation is not successful. |  -  |

<a id="subscriptionsEnable"></a>
# **subscriptionsEnable**
> EnabledSubscriptionId subscriptionsEnable(subscriptionId, apiVersion)



The operation to enable a subscription

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-03-01-preview
    try {
      EnabledSubscriptionId result = apiInstance.subscriptionsEnable(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionsEnable");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-03-01-preview | |

### Return type

[**EnabledSubscriptionId**](EnabledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Describes the error if the operation is not successful. |  -  |

<a id="subscriptionsRename"></a>
# **subscriptionsRename**
> RenamedSubscriptionId subscriptionsRename(subscriptionId, apiVersion, body)



The operation to rename a subscription

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-03-01-preview
    SubscriptionName body = new SubscriptionName(); // SubscriptionName | Subscription Name
    try {
      RenamedSubscriptionId result = apiInstance.subscriptionsRename(subscriptionId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionsRename");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-03-01-preview | |
| **body** | [**SubscriptionName**](SubscriptionName.md)| Subscription Name | |

### Return type

[**RenamedSubscriptionId**](RenamedSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Describes the error if the operation is not successful. |  -  |

