# SubscriptionDiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionDiagnosticSettingsCreateOrUpdate**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings/{name} |  |
| [**subscriptionDiagnosticSettingsDelete**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings/{name} |  |
| [**subscriptionDiagnosticSettingsGet**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsGet) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings/{name} |  |
| [**subscriptionDiagnosticSettingsList**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings |  |


<a id="subscriptionDiagnosticSettingsCreateOrUpdate"></a>
# **subscriptionDiagnosticSettingsCreateOrUpdate**
> SubscriptionDiagnosticSettingsResource subscriptionDiagnosticSettingsCreateOrUpdate(subscriptionId, apiVersion, name, parameters)



Creates or updates subscription diagnostic settings for the specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDiagnosticSettingsApi apiInstance = new SubscriptionDiagnosticSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    SubscriptionDiagnosticSettingsResource parameters = new SubscriptionDiagnosticSettingsResource(); // SubscriptionDiagnosticSettingsResource | Parameters supplied to the operation.
    try {
      SubscriptionDiagnosticSettingsResource result = apiInstance.subscriptionDiagnosticSettingsCreateOrUpdate(subscriptionId, apiVersion, name, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDiagnosticSettingsApi#subscriptionDiagnosticSettingsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **name** | **String**| The name of the diagnostic setting. | |
| **parameters** | [**SubscriptionDiagnosticSettingsResource**](SubscriptionDiagnosticSettingsResource.md)| Parameters supplied to the operation. | |

### Return type

[**SubscriptionDiagnosticSettingsResource**](SubscriptionDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to create a subscription diagnostic setting |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDiagnosticSettingsDelete"></a>
# **subscriptionDiagnosticSettingsDelete**
> subscriptionDiagnosticSettingsDelete(subscriptionId, apiVersion, name)



Deletes existing subscription diagnostic settings for the specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDiagnosticSettingsApi apiInstance = new SubscriptionDiagnosticSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    try {
      apiInstance.subscriptionDiagnosticSettingsDelete(subscriptionId, apiVersion, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDiagnosticSettingsApi#subscriptionDiagnosticSettingsDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **name** | **String**| The name of the diagnostic setting. | |

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
| **200** | Successful request to remove a subscription diagnostic setting |  -  |
| **204** | Successful request to remove a subscription diagnostic setting |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDiagnosticSettingsGet"></a>
# **subscriptionDiagnosticSettingsGet**
> SubscriptionDiagnosticSettingsResource subscriptionDiagnosticSettingsGet(subscriptionId, apiVersion, name)



Gets the active subscription diagnostic settings for the specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDiagnosticSettingsApi apiInstance = new SubscriptionDiagnosticSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    try {
      SubscriptionDiagnosticSettingsResource result = apiInstance.subscriptionDiagnosticSettingsGet(subscriptionId, apiVersion, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDiagnosticSettingsApi#subscriptionDiagnosticSettingsGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **name** | **String**| The name of the diagnostic setting. | |

### Return type

[**SubscriptionDiagnosticSettingsResource**](SubscriptionDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about diagnostic setting. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDiagnosticSettingsList"></a>
# **subscriptionDiagnosticSettingsList**
> SubscriptionDiagnosticSettingsResourceCollection subscriptionDiagnosticSettingsList(subscriptionId, apiVersion)



Gets the active subscription diagnostic settings list for the specified subscriptionId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDiagnosticSettingsApi apiInstance = new SubscriptionDiagnosticSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      SubscriptionDiagnosticSettingsResourceCollection result = apiInstance.subscriptionDiagnosticSettingsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDiagnosticSettingsApi#subscriptionDiagnosticSettingsList");
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
| **subscriptionId** | **String**| The subscription id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**SubscriptionDiagnosticSettingsResourceCollection**](SubscriptionDiagnosticSettingsResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about subscription diagnostic setting |  -  |
| **0** | Error response describing why the operation failed. |  -  |

