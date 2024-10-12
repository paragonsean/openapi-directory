# GlobalResourceGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalResourceGroupsMoveResources**](GlobalResourceGroupsApi.md#globalResourceGroupsMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources |  |


<a id="globalResourceGroupsMoveResources"></a>
# **globalResourceGroupsMoveResources**
> globalResourceGroupsMoveResources(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalResourceGroupsApi apiInstance = new GlobalResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | 
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmMoveResourceEnvelope moveResourceEnvelope = new CsmMoveResourceEnvelope(); // CsmMoveResourceEnvelope | 
    try {
      apiInstance.globalResourceGroupsMoveResources(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalResourceGroupsApi#globalResourceGroupsMoveResources");
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
| **resourceGroupName** | **String**|  | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **moveResourceEnvelope** | [**CsmMoveResourceEnvelope**](CsmMoveResourceEnvelope.md)|  | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

