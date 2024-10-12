# PatchApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotHubResourceUpdate**](PatchApi.md#iotHubResourceUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Update an existing IoT Hubs tags. |


<a id="iotHubResourceUpdate"></a>
# **iotHubResourceUpdate**
> IotHubDescription iotHubResourceUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, iotHubTags)

Update an existing IoT Hubs tags.

Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PatchApi apiInstance = new PatchApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String resourceName = "resourceName_example"; // String | Name of iot hub to update.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    TagsResource iotHubTags = new TagsResource(); // TagsResource | Updated tag information to set into the iot hub instance.
    try {
      IotHubDescription result = apiInstance.iotHubResourceUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, iotHubTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatchApi#iotHubResourceUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group identifier. | |
| **resourceName** | **String**| Name of iot hub to update. | |
| **apiVersion** | **String**| The version of the API. | |
| **iotHubTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the iot hub instance. | |

### Return type

[**IotHubDescription**](IotHubDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Iot Hub was successfully updated |  -  |

