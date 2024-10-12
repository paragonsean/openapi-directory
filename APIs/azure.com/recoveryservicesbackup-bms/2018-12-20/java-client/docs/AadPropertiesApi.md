# AadPropertiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aadPropertiesGet**](AadPropertiesApi.md#aadPropertiesGet) | **GET** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupAadProperties/default | Fetches the AAD properties from target region BCM stamp. |


<a id="aadPropertiesGet"></a>
# **aadPropertiesGet**
> AADPropertiesResource aadPropertiesGet(apiVersion, azureRegion, subscriptionId)

Fetches the AAD properties from target region BCM stamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AadPropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AadPropertiesApi apiInstance = new AadPropertiesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String azureRegion = "azureRegion_example"; // String | Azure region to hit Api
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      AADPropertiesResource result = apiInstance.aadPropertiesGet(apiVersion, azureRegion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AadPropertiesApi#aadPropertiesGet");
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

### Return type

[**AADPropertiesResource**](AADPropertiesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

