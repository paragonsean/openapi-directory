# FeatureSupportApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**featureSupportValidate**](FeatureSupportApi.md#featureSupportValidate) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupValidateFeatures | It will validate if given feature with resource properties is supported in service |


<a id="featureSupportValidate"></a>
# **featureSupportValidate**
> AzureVMResourceFeatureSupportResponse featureSupportValidate(apiVersion, azureRegion, subscriptionId, parameters)

It will validate if given feature with resource properties is supported in service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureSupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FeatureSupportApi apiInstance = new FeatureSupportApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String azureRegion = "azureRegion_example"; // String | Azure region to hit Api
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    FeatureSupportRequest parameters = new FeatureSupportRequest(); // FeatureSupportRequest | Feature support request object
    try {
      AzureVMResourceFeatureSupportResponse result = apiInstance.featureSupportValidate(apiVersion, azureRegion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureSupportApi#featureSupportValidate");
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
| **azureRegion** | **String**| Azure region to hit Api | |
| **subscriptionId** | **String**| The subscription Id. | |
| **parameters** | [**FeatureSupportRequest**](FeatureSupportRequest.md)| Feature support request object | |

### Return type

[**AzureVMResourceFeatureSupportResponse**](AzureVMResourceFeatureSupportResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

