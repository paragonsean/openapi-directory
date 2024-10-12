# GuestCartsCartIdCollectionPointSearchResultApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet**](GuestCartsCartIdCollectionPointSearchResultApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet) | **GET** /V1/guest-carts/{cartId}/collection-point/search-result | guest-carts/{cartId}/collection-point/search-result |


<a id="temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet"></a>
# **temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet**
> List&lt;TemandoShippingDataCollectionPointQuoteCollectionPointInterface&gt; temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet(cartId)

guest-carts/{cartId}/collection-point/search-result



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCollectionPointSearchResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCollectionPointSearchResultApi apiInstance = new GuestCartsCartIdCollectionPointSearchResultApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    try {
      List<TemandoShippingDataCollectionPointQuoteCollectionPointInterface> result = apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCollectionPointSearchResultApi#temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet");
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
| **cartId** | **String**|  | |

### Return type

[**List&lt;TemandoShippingDataCollectionPointQuoteCollectionPointInterface&gt;**](TemandoShippingDataCollectionPointQuoteCollectionPointInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **0** | Unexpected error |  -  |

