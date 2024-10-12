# ConfigurationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurationAdd**](ConfigurationApi.md#configurationAdd) | **POST** /providers/Microsoft.ADHybridHealthService/configuration |  |
| [**configurationGet**](ConfigurationApi.md#configurationGet) | **GET** /providers/Microsoft.ADHybridHealthService/configuration |  |
| [**configurationUpdate**](ConfigurationApi.md#configurationUpdate) | **PATCH** /providers/Microsoft.ADHybridHealthService/configuration |  |


<a id="configurationAdd"></a>
# **configurationAdd**
> Tenant configurationAdd(apiVersion)



Onboards a tenant in Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Tenant result = apiInstance.configurationAdd(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationAdd");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added the tenant. |  -  |

<a id="configurationGet"></a>
# **configurationGet**
> Tenant configurationGet(apiVersion)



Gets the details of a tenant onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Tenant result = apiInstance.configurationGet(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationGet");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tenant details. |  -  |

<a id="configurationUpdate"></a>
# **configurationUpdate**
> Tenant configurationUpdate(apiVersion, tenant)



Updates tenant properties for tenants onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Tenant tenant = new Tenant(); // Tenant | The tenant object with the properties set to the updated value.
    try {
      Tenant result = apiInstance.configurationUpdate(apiVersion, tenant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationUpdate");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **tenant** | [**Tenant**](Tenant.md)| The tenant object with the properties set to the updated value. | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the tenant. |  -  |

