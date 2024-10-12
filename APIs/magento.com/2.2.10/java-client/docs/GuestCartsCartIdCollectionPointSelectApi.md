# GuestCartsCartIdCollectionPointSelectApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost**](GuestCartsCartIdCollectionPointSelectApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost) | **POST** /V1/guest-carts/{cartId}/collection-point/select | guest-carts/{cartId}/collection-point/select |


<a id="temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost"></a>
# **temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost**
> Boolean temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost(cartId, temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest)

guest-carts/{cartId}/collection-point/select



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCollectionPointSelectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCollectionPointSelectApi apiInstance = new GuestCartsCartIdCollectionPointSelectApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest = new TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest(); // TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest | 
    try {
      Boolean result = apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost(cartId, temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCollectionPointSelectApi#temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost");
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
| **temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest** | [**TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest**](TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

