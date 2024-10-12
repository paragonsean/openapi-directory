# DiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diagnosticSettingsCreateOrUpdate**](DiagnosticSettingsApi.md#diagnosticSettingsCreateOrUpdate) | **PUT** /providers/microsoft.aadiam/diagnosticSettings/{name} |  |
| [**diagnosticSettingsDelete**](DiagnosticSettingsApi.md#diagnosticSettingsDelete) | **DELETE** /providers/microsoft.aadiam/diagnosticSettings/{name} |  |
| [**diagnosticSettingsGet**](DiagnosticSettingsApi.md#diagnosticSettingsGet) | **GET** /providers/microsoft.aadiam/diagnosticSettings/{name} |  |
| [**diagnosticSettingsList**](DiagnosticSettingsApi.md#diagnosticSettingsList) | **GET** /providers/microsoft.aadiam/diagnosticSettings |  |


<a id="diagnosticSettingsCreateOrUpdate"></a>
# **diagnosticSettingsCreateOrUpdate**
> DiagnosticSettingsResource diagnosticSettingsCreateOrUpdate(apiVersion, name, parameters)



Creates or updates diagnostic settings for AadIam.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticSettingsApi apiInstance = new DiagnosticSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    DiagnosticSettingsResource parameters = new DiagnosticSettingsResource(); // DiagnosticSettingsResource | Parameters supplied to the operation.
    try {
      DiagnosticSettingsResource result = apiInstance.diagnosticSettingsCreateOrUpdate(apiVersion, name, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticSettingsApi#diagnosticSettingsCreateOrUpdate");
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
| **name** | **String**| The name of the diagnostic setting. | |
| **parameters** | [**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)| Parameters supplied to the operation. | |

### Return type

[**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to create AadIam diagnostic setting. |  -  |
| **0** | Error. The request to create diagnostic setting has failed. |  -  |

<a id="diagnosticSettingsDelete"></a>
# **diagnosticSettingsDelete**
> diagnosticSettingsDelete(apiVersion, name)



Deletes existing diagnostic setting for AadIam.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticSettingsApi apiInstance = new DiagnosticSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    try {
      apiInstance.diagnosticSettingsDelete(apiVersion, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticSettingsApi#diagnosticSettingsDelete");
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
| **200** | Successful request to remove a diagnostic setting |  -  |
| **204** | Successful request to remove a diagnostic setting |  -  |
| **0** | Error. The request to delete named diagnostic setting has failed. |  -  |

<a id="diagnosticSettingsGet"></a>
# **diagnosticSettingsGet**
> DiagnosticSettingsResource diagnosticSettingsGet(apiVersion, name)



Gets the active diagnostic setting for AadIam.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticSettingsApi apiInstance = new DiagnosticSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    try {
      DiagnosticSettingsResource result = apiInstance.diagnosticSettingsGet(apiVersion, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticSettingsApi#diagnosticSettingsGet");
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
| **name** | **String**| The name of the diagnostic setting. | |

### Return type

[**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about diagnostic setting |  -  |
| **0** | Error. Request for AadIam diagnostic setting has failed. |  -  |

<a id="diagnosticSettingsList"></a>
# **diagnosticSettingsList**
> DiagnosticSettingsResourceCollection diagnosticSettingsList(apiVersion)



Gets the active diagnostic settings list for AadIam.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticSettingsApi apiInstance = new DiagnosticSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DiagnosticSettingsResourceCollection result = apiInstance.diagnosticSettingsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticSettingsApi#diagnosticSettingsList");
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

### Return type

[**DiagnosticSettingsResourceCollection**](DiagnosticSettingsResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about AadIam diagnostic settings |  -  |
| **0** | Error. Request for AadIam diagnostic settings has failed |  -  |

