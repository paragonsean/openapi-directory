# ProductsOnlineApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProductSlug**](ProductsOnlineApi.md#createProductSlug) | **POST** /organizations/{organizationUuid}/products/online/slug | Create a product identifier |


<a id="createProductSlug"></a>
# **createProductSlug**
> SlugResponse createProductSlug(organizationUuid, createSlugRequest)

Create a product identifier

Creates a unique slug (identifier) for a product. The slug is used to create a product URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsOnlineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsOnlineApi apiInstance = new ProductsOnlineApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    CreateSlugRequest createSlugRequest = new CreateSlugRequest(); // CreateSlugRequest | 
    try {
      SlugResponse result = apiInstance.createProductSlug(organizationUuid, createSlugRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsOnlineApi#createProductSlug");
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
| **organizationUuid** | **UUID**|  | |
| **createSlugRequest** | [**CreateSlugRequest**](CreateSlugRequest.md)|  | |

### Return type

[**SlugResponse**](SlugResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product slug |  -  |

