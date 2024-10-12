# PatchApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotDpsResourceUpdate**](PatchApi.md#iotDpsResourceUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Update an existing provisioning service&#39;s tags. |


<a id="iotDpsResourceUpdate"></a>
# **iotDpsResourceUpdate**
> ProvisioningServiceDescription iotDpsResourceUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, provisioningServiceTags)

Update an existing provisioning service&#39;s tags.

Update an existing provisioning service&#39;s tags. to update other fields use the CreateOrUpdate method

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
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to create or update.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    TagsResource provisioningServiceTags = new TagsResource(); // TagsResource | Updated tag information to set into the provisioning service instance.
    try {
      ProvisioningServiceDescription result = apiInstance.iotDpsResourceUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, provisioningServiceTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatchApi#iotDpsResourceUpdate");
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
| **provisioningServiceName** | **String**| Name of provisioning service to create or update. | |
| **apiVersion** | **String**| The version of the API. | |
| **provisioningServiceTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the provisioning service instance. | |

### Return type

[**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Provisioning Service was successfully updated |  -  |

