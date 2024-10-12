# CatalogApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCatalog**](CatalogApi.md#getCatalog) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Capacity/catalogs | Get the regions and skus that are available for RI purchase for the specified Azure subscription. |


<a id="getCatalog"></a>
# **getCatalog**
> List&lt;Catalog&gt; getCatalog(apiVersion, subscriptionId, reservedResourceType, location)

Get the regions and skus that are available for RI purchase for the specified Azure subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Supported version.
    String subscriptionId = "subscriptionId_example"; // String | Id of the subscription
    String reservedResourceType = "reservedResourceType_example"; // String | The type of the resource for which the skus should be provided.
    String location = "location_example"; // String | Filters the skus based on the location specified in this parameter. This can be an azure region or global
    try {
      List<Catalog> result = apiInstance.getCatalog(apiVersion, subscriptionId, reservedResourceType, location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#getCatalog");
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
| **apiVersion** | **String**| Supported version. | |
| **subscriptionId** | **String**| Id of the subscription | |
| **reservedResourceType** | **String**| The type of the resource for which the skus should be provided. | |
| **location** | **String**| Filters the skus based on the location specified in this parameter. This can be an azure region or global | [optional] |

### Return type

[**List&lt;Catalog&gt;**](Catalog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of available resources |  -  |
| **0** | Unexpected error |  -  |

