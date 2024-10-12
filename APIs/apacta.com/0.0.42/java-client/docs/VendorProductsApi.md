# VendorProductsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vendorProductsGet**](VendorProductsApi.md#vendorProductsGet) | **GET** /vendor_products | List vendor products |
| [**vendorProductsVendorProductIdGet**](VendorProductsApi.md#vendorProductsVendorProductIdGet) | **GET** /vendor_products/{vendor_product_id} | View single vendor product |


<a id="vendorProductsGet"></a>
# **vendorProductsGet**
> VendorProductsGet200Response vendorProductsGet(name, productNumber, barcode, vendorId)

List vendor products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    VendorProductsApi apiInstance = new VendorProductsApi(defaultClient);
    String name = "name_example"; // String | Used to filter on the `name` of the vendor products
    UUID productNumber = UUID.randomUUID(); // UUID | Used to filter on the `product_number` of the vendor products
    String barcode = "barcode_example"; // String | Used to filter on the `barcode` of the vendor products
    String vendorId = "vendorId_example"; // String | Used to filter on the `vendor_id` of the vendor products
    try {
      VendorProductsGet200Response result = apiInstance.vendorProductsGet(name, productNumber, barcode, vendorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorProductsApi#vendorProductsGet");
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
| **name** | **String**| Used to filter on the &#x60;name&#x60; of the vendor products | [optional] |
| **productNumber** | **UUID**| Used to filter on the &#x60;product_number&#x60; of the vendor products | [optional] |
| **barcode** | **String**| Used to filter on the &#x60;barcode&#x60; of the vendor products | [optional] |
| **vendorId** | **String**| Used to filter on the &#x60;vendor_id&#x60; of the vendor products | [optional] |

### Return type

[**VendorProductsGet200Response**](VendorProductsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vendorProductsVendorProductIdGet"></a>
# **vendorProductsVendorProductIdGet**
> VendorProductsVendorProductIdGet200Response vendorProductsVendorProductIdGet(vendorProductId)

View single vendor product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    VendorProductsApi apiInstance = new VendorProductsApi(defaultClient);
    String vendorProductId = "vendorProductId_example"; // String | 
    try {
      VendorProductsVendorProductIdGet200Response result = apiInstance.vendorProductsVendorProductIdGet(vendorProductId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorProductsApi#vendorProductsVendorProductIdGet");
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
| **vendorProductId** | **String**|  | |

### Return type

[**VendorProductsVendorProductIdGet200Response**](VendorProductsVendorProductIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

