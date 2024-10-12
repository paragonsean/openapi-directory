# CartsMineCollectionPointSelectApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost**](CartsMineCollectionPointSelectApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost) | **POST** /V1/carts/mine/collection-point/select | carts/mine/collection-point/select |


<a id="temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost"></a>
# **temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost**
> Boolean temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost(temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest)

carts/mine/collection-point/select



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCollectionPointSelectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCollectionPointSelectApi apiInstance = new CartsMineCollectionPointSelectApi(defaultClient);
    TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest = new TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest(); // TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest | 
    try {
      Boolean result = apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost(temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCollectionPointSelectApi#temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost");
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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

