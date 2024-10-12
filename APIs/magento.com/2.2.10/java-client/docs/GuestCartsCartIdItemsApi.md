# GuestCartsCartIdItemsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartItemRepositoryV1GetListGet**](GuestCartsCartIdItemsApi.md#quoteGuestCartItemRepositoryV1GetListGet) | **GET** /V1/guest-carts/{cartId}/items | guest-carts/{cartId}/items |
| [**quoteGuestCartItemRepositoryV1SavePost**](GuestCartsCartIdItemsApi.md#quoteGuestCartItemRepositoryV1SavePost) | **POST** /V1/guest-carts/{cartId}/items | guest-carts/{cartId}/items |


<a id="quoteGuestCartItemRepositoryV1GetListGet"></a>
# **quoteGuestCartItemRepositoryV1GetListGet**
> List&lt;QuoteDataCartItemInterface&gt; quoteGuestCartItemRepositoryV1GetListGet(cartId)

guest-carts/{cartId}/items

List items that are assigned to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdItemsApi apiInstance = new GuestCartsCartIdItemsApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      List<QuoteDataCartItemInterface> result = apiInstance.quoteGuestCartItemRepositoryV1GetListGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdItemsApi#quoteGuestCartItemRepositoryV1GetListGet");
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
| **cartId** | **String**| The cart ID. | |

### Return type

[**List&lt;QuoteDataCartItemInterface&gt;**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

<a id="quoteGuestCartItemRepositoryV1SavePost"></a>
# **quoteGuestCartItemRepositoryV1SavePost**
> QuoteDataCartItemInterface quoteGuestCartItemRepositoryV1SavePost(cartId, quoteCartItemRepositoryV1SavePostRequest)

guest-carts/{cartId}/items

Add/update the specified cart item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdItemsApi apiInstance = new GuestCartsCartIdItemsApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest = new QuoteCartItemRepositoryV1SavePostRequest(); // QuoteCartItemRepositoryV1SavePostRequest | 
    try {
      QuoteDataCartItemInterface result = apiInstance.quoteGuestCartItemRepositoryV1SavePost(cartId, quoteCartItemRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdItemsApi#quoteGuestCartItemRepositoryV1SavePost");
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
| **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

