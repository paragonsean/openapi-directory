# ServiceDiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceDiagnosticSettingsCreateOrUpdate**](ServiceDiagnosticSettingsApi.md#serviceDiagnosticSettingsCreateOrUpdate) | **PUT** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/service |  |
| [**serviceDiagnosticSettingsGet**](ServiceDiagnosticSettingsApi.md#serviceDiagnosticSettingsGet) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/service |  |


<a id="serviceDiagnosticSettingsCreateOrUpdate"></a>
# **serviceDiagnosticSettingsCreateOrUpdate**
> ServiceDiagnosticSettingsResource serviceDiagnosticSettingsCreateOrUpdate(resourceUri, apiVersion, parameters)



Create or update new diagnostic settings for the specified resource. **WARNING**: This method will be deprecated in future releases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceDiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceDiagnosticSettingsApi apiInstance = new ServiceDiagnosticSettingsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ServiceDiagnosticSettingsResource parameters = new ServiceDiagnosticSettingsResource(); // ServiceDiagnosticSettingsResource | Parameters supplied to the operation.
    try {
      ServiceDiagnosticSettingsResource result = apiInstance.serviceDiagnosticSettingsCreateOrUpdate(resourceUri, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDiagnosticSettingsApi#serviceDiagnosticSettingsCreateOrUpdate");
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
| **parameters** | [**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)| Parameters supplied to the operation. | |

### Return type

[**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to create a service diagnostic setting |  -  |

<a id="serviceDiagnosticSettingsGet"></a>
# **serviceDiagnosticSettingsGet**
> ServiceDiagnosticSettingsResource serviceDiagnosticSettingsGet(resourceUri, apiVersion)



Gets the active diagnostic settings for the specified resource. **WARNING**: This method will be deprecated in future releases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceDiagnosticSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceDiagnosticSettingsApi apiInstance = new ServiceDiagnosticSettingsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ServiceDiagnosticSettingsResource result = apiInstance.serviceDiagnosticSettingsGet(resourceUri, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceDiagnosticSettingsApi#serviceDiagnosticSettingsGet");
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

[**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get more information about service diagnostic setting |  -  |
| **0** | Error response describing why the operation failed. |  -  |

