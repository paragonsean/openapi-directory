# DiagnosticSettingsCategoriesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diagnosticSettingsCategoryGet**](DiagnosticSettingsCategoriesApi.md#diagnosticSettingsCategoryGet) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettingsCategories/{name} |  |
| [**diagnosticSettingsCategoryList**](DiagnosticSettingsCategoriesApi.md#diagnosticSettingsCategoryList) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettingsCategories |  |


<a id="diagnosticSettingsCategoryGet"></a>
# **diagnosticSettingsCategoryGet**
> DiagnosticSettingsCategoryResource diagnosticSettingsCategoryGet(resourceUri, apiVersion, name)



Gets the diagnostic settings category for the specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticSettingsCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticSettingsCategoriesApi apiInstance = new DiagnosticSettingsCategoriesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String name = "name_example"; // String | The name of the diagnostic setting.
    try {
      DiagnosticSettingsCategoryResource result = apiInstance.diagnosticSettingsCategoryGet(resourceUri, apiVersion, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticSettingsCategoriesApi#diagnosticSettingsCategoryGet");
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
| **resourceUri** | **String**| The identifier of the resource. | |
| **apiVersion** | **String**| Client Api Version. | |
| **name** | **String**| The name of the diagnostic setting. | |

### Return type

[**DiagnosticSettingsCategoryResource**](DiagnosticSettingsCategoryResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about diagnostic setting category |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="diagnosticSettingsCategoryList"></a>
# **diagnosticSettingsCategoryList**
> DiagnosticSettingsCategoryResourceCollection diagnosticSettingsCategoryList(resourceUri, apiVersion)



Lists the diagnostic settings categories for the specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticSettingsCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticSettingsCategoriesApi apiInstance = new DiagnosticSettingsCategoriesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DiagnosticSettingsCategoryResourceCollection result = apiInstance.diagnosticSettingsCategoryList(resourceUri, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticSettingsCategoriesApi#diagnosticSettingsCategoryList");
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
| **resourceUri** | **String**| The identifier of the resource. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DiagnosticSettingsCategoryResourceCollection**](DiagnosticSettingsCategoryResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about diagnostic setting category |  -  |
| **0** | Error response describing why the operation failed. |  -  |

