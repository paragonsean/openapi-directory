# CartsMineCollectionPointSearchResultApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet**](CartsMineCollectionPointSearchResultApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet) | **GET** /V1/carts/mine/collection-point/search-result | carts/mine/collection-point/search-result |


<a id="temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet"></a>
# **temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet**
> List&lt;TemandoShippingDataCollectionPointQuoteCollectionPointInterface&gt; temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet()

carts/mine/collection-point/search-result



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCollectionPointSearchResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCollectionPointSearchResultApi apiInstance = new CartsMineCollectionPointSearchResultApi(defaultClient);
    try {
      List<TemandoShippingDataCollectionPointQuoteCollectionPointInterface> result = apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCollectionPointSearchResultApi#temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

