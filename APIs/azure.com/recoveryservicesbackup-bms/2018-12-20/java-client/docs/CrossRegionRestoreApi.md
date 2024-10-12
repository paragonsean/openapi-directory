# CrossRegionRestoreApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**crossRegionRestoreTrigger**](CrossRegionRestoreApi.md#crossRegionRestoreTrigger) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupCrossRegionRestore | Restores the specified backed up data in a different region as compared to where the data is backed up. |


<a id="crossRegionRestoreTrigger"></a>
# **crossRegionRestoreTrigger**
> crossRegionRestoreTrigger(apiVersion, azureRegion, subscriptionId, parameters)

Restores the specified backed up data in a different region as compared to where the data is backed up.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossRegionRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CrossRegionRestoreApi apiInstance = new CrossRegionRestoreApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String azureRegion = "azureRegion_example"; // String | Azure region to hit Api
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    CrossRegionRestoreRequestResource parameters = new CrossRegionRestoreRequestResource(); // CrossRegionRestoreRequestResource | resource cross region restore request
    try {
      apiInstance.crossRegionRestoreTrigger(apiVersion, azureRegion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossRegionRestoreApi#crossRegionRestoreTrigger");
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
| **parameters** | [**CrossRegionRestoreRequestResource**](CrossRegionRestoreRequestResource.md)| resource cross region restore request | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

