# CollectionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ioTSpacesList**](CollectionApi.md#ioTSpacesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.IoTSpaces/Graph |  |
| [**ioTSpacesListByResourceGroup**](CollectionApi.md#ioTSpacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph |  |


<a id="ioTSpacesList"></a>
# **ioTSpacesList**
> IoTSpacesDescriptionListResult ioTSpacesList(apiVersion, subscriptionId)



Get all the IoTSpaces instances in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    try {
      IoTSpacesDescriptionListResult result = apiInstance.ioTSpacesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#ioTSpacesList");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |

### Return type

[**IoTSpacesDescriptionListResult**](IoTSpacesDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the IoTSpaces instances in the subscription. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="ioTSpacesListByResourceGroup"></a>
# **ioTSpacesListByResourceGroup**
> IoTSpacesDescriptionListResult ioTSpacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the IoTSpaces instances in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String apiVersion = "2017-10-01-preview"; // String | The version of the API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoTSpaces instance.
    try {
      IoTSpacesDescriptionListResult result = apiInstance.ioTSpacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#ioTSpacesListByResourceGroup");
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
| **apiVersion** | **String**| The version of the API. | [enum: 2017-10-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoTSpaces instance. | |

### Return type

[**IoTSpacesDescriptionListResult**](IoTSpacesDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the IoTSpaces instances in the resource group. |  -  |
| **0** | DefaultErrorResponse |  -  |

