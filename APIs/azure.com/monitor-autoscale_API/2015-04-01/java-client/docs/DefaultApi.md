# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoscaleSettingsUpdate**](DefaultApi.md#autoscaleSettingsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} |  |


<a id="autoscaleSettingsUpdate"></a>
# **autoscaleSettingsUpdate**
> AutoscaleSettingResource autoscaleSettingsUpdate(subscriptionId, resourceGroupName, autoscaleSettingName, apiVersion, autoscaleSettingResource)



Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    AutoscaleSettingResourcePatch autoscaleSettingResource = new AutoscaleSettingResourcePatch(); // AutoscaleSettingResourcePatch | Parameters supplied to the operation.
    try {
      AutoscaleSettingResource result = apiInstance.autoscaleSettingsUpdate(subscriptionId, resourceGroupName, autoscaleSettingName, apiVersion, autoscaleSettingResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#autoscaleSettingsUpdate");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **autoscaleSettingName** | **String**| The autoscale setting name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **autoscaleSettingResource** | [**AutoscaleSettingResourcePatch**](AutoscaleSettingResourcePatch.md)| Parameters supplied to the operation. | |

### Return type

[**AutoscaleSettingResource**](AutoscaleSettingResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing autoscale setting resource was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

