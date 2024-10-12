# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceDiagnosticSettingsUpdate**](DefaultApi.md#serviceDiagnosticSettingsUpdate) | **PATCH** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/service |  |


<a id="serviceDiagnosticSettingsUpdate"></a>
# **serviceDiagnosticSettingsUpdate**
> ServiceDiagnosticSettingsResource serviceDiagnosticSettingsUpdate(resourceUri, apiVersion, serviceDiagnosticSettingsResource)



Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the CreateOrUpdate method. **WARNING**: This method will be deprecated in future releases.

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
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ServiceDiagnosticSettingsResourcePatch serviceDiagnosticSettingsResource = new ServiceDiagnosticSettingsResourcePatch(); // ServiceDiagnosticSettingsResourcePatch | Parameters supplied to the operation.
    try {
      ServiceDiagnosticSettingsResource result = apiInstance.serviceDiagnosticSettingsUpdate(resourceUri, apiVersion, serviceDiagnosticSettingsResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceDiagnosticSettingsUpdate");
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
| **serviceDiagnosticSettingsResource** | [**ServiceDiagnosticSettingsResourcePatch**](ServiceDiagnosticSettingsResourcePatch.md)| Parameters supplied to the operation. | |

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
| **200** | An existing service diagnostics setting resource was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

