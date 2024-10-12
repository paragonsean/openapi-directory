# RegistriesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registriesGenerateCredentials**](RegistriesApi.md#registriesGenerateCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/generateCredentials |  |


<a id="registriesGenerateCredentials"></a>
# **registriesGenerateCredentials**
> GenerateCredentialsResult registriesGenerateCredentials(apiVersion, subscriptionId, resourceGroupName, registryName, generateCredentialsParameters)



Generate keys for a token of a specified container registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    GenerateCredentialsParameters generateCredentialsParameters = new GenerateCredentialsParameters(); // GenerateCredentialsParameters | The parameters for generating credentials.
    try {
      GenerateCredentialsResult result = apiInstance.registriesGenerateCredentials(apiVersion, subscriptionId, resourceGroupName, registryName, generateCredentialsParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#registriesGenerateCredentials");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **generateCredentialsParameters** | [**GenerateCredentialsParameters**](GenerateCredentialsParameters.md)| The parameters for generating credentials. | |

### Return type

[**GenerateCredentialsResult**](GenerateCredentialsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successful; the operation will complete asynchronously. |  -  |

