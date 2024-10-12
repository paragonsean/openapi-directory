# KeyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**spatialAnchorsAccountsGetKeys**](KeyApi.md#spatialAnchorsAccountsGetKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName}/keys |  |
| [**spatialAnchorsAccountsRegenerateKeys**](KeyApi.md#spatialAnchorsAccountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName}/keys |  |


<a id="spatialAnchorsAccountsGetKeys"></a>
# **spatialAnchorsAccountsGetKeys**
> SpatialAnchorsAccountsGetKeys200Response spatialAnchorsAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Get Both of the 2 Keys of a Spatial Anchors Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      SpatialAnchorsAccountsGetKeys200Response result = apiInstance.spatialAnchorsAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#spatialAnchorsAccountsGetKeys");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Name of an Mixed Reality Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**SpatialAnchorsAccountsGetKeys200Response**](SpatialAnchorsAccountsGetKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="spatialAnchorsAccountsRegenerateKeys"></a>
# **spatialAnchorsAccountsRegenerateKeys**
> SpatialAnchorsAccountsGetKeys200Response spatialAnchorsAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate)



Regenerate specified Key of a Spatial Anchors Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    SpatialAnchorsAccountsRegenerateKeysRequest regenerate = new SpatialAnchorsAccountsRegenerateKeysRequest(); // SpatialAnchorsAccountsRegenerateKeysRequest | Required information for key regeneration.
    try {
      SpatialAnchorsAccountsGetKeys200Response result = apiInstance.spatialAnchorsAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#spatialAnchorsAccountsRegenerateKeys");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Name of an Mixed Reality Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **regenerate** | [**SpatialAnchorsAccountsRegenerateKeysRequest**](SpatialAnchorsAccountsRegenerateKeysRequest.md)| Required information for key regeneration. | |

### Return type

[**SpatialAnchorsAccountsGetKeys200Response**](SpatialAnchorsAccountsGetKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

