# ProductApi

All URIs are relative to *https://go-upc.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProductInfo**](ProductApi.md#getProductInfo) | **GET** /code/{code} | Retrieve product info for a particular barcode number (UPC, EAN, or ISBN). |


<a id="getProductInfo"></a>
# **getProductInfo**
> GetProductInfo200Response getProductInfo(code)

Retrieve product info for a particular barcode number (UPC, EAN, or ISBN).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go-upc.com/api/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String code = "code_example"; // String | 
    try {
      GetProductInfo200Response result = apiInstance.getProductInfo(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#getProductInfo");
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
| **code** | **String**|  | |

### Return type

[**GetProductInfo200Response**](GetProductInfo200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The product corresponding to the provided &#x60;code&#x60; |  -  |
| **404** | No product information was found for the given &#x60;code&#x60;. |  -  |
| **500** | Unexpected error |  -  |

