# ProductSubscriptionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productSubscriptionsListByProducts**](ProductSubscriptionsApi.md#productSubscriptionsListByProducts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/subscriptions |  |


<a id="productSubscriptionsListByProducts"></a>
# **productSubscriptionsListByProducts**
> ProductSubscriptionsListByProducts200Response productSubscriptionsListByProducts(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, $filter, $top, $skip)



Lists the collection of subscriptions to the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductSubscriptionsApi apiInstance = new ProductSubscriptionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ProductSubscriptionsListByProducts200Response result = apiInstance.productSubscriptionsListByProducts(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSubscriptionsApi#productSubscriptionsListByProducts");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ProductSubscriptionsListByProducts200Response**](ProductSubscriptionsListByProducts200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of subscription entities. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

