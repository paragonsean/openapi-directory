# VendorProductPriceFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vendorProductPriceFilesGet**](VendorProductPriceFilesApi.md#vendorProductPriceFilesGet) | **GET** /vendor_product_price_files | Get a list of price files |
| [**vendorProductPriceFilesPost**](VendorProductPriceFilesApi.md#vendorProductPriceFilesPost) | **POST** /vendor_product_price_files | Upload a vendor price file |
| [**vendorProductPriceFilesVendorProductPriceFileIdGet**](VendorProductPriceFilesApi.md#vendorProductPriceFilesVendorProductPriceFileIdGet) | **GET** /vendor_product_price_files/{vendor_product_price_file_id} | Get a single price file |


<a id="vendorProductPriceFilesGet"></a>
# **vendorProductPriceFilesGet**
> VendorProductPriceFilesGet200Response vendorProductPriceFilesGet(fileName, vendorName, vendorIds, status)

Get a list of price files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorProductPriceFilesApi;

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

    VendorProductPriceFilesApi apiInstance = new VendorProductPriceFilesApi(defaultClient);
    String fileName = "fileName_example"; // String | 
    String vendorName = "vendorName_example"; // String | 
    List<String> vendorIds = Arrays.asList(); // List<String> | 
    String status = "awaiting"; // String | 
    try {
      VendorProductPriceFilesGet200Response result = apiInstance.vendorProductPriceFilesGet(fileName, vendorName, vendorIds, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorProductPriceFilesApi#vendorProductPriceFilesGet");
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
| **fileName** | **String**|  | [optional] |
| **vendorName** | **String**|  | [optional] |
| **vendorIds** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **status** | **String**|  | [optional] [enum: awaiting, fresh, expired, failed] |

### Return type

[**VendorProductPriceFilesGet200Response**](VendorProductPriceFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vendorProductPriceFilesPost"></a>
# **vendorProductPriceFilesPost**
> CreateSuccessResponse vendorProductPriceFilesPost(companiesVendorId, _file)

Upload a vendor price file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorProductPriceFilesApi;

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

    VendorProductPriceFilesApi apiInstance = new VendorProductPriceFilesApi(defaultClient);
    String companiesVendorId = "companiesVendorId_example"; // String | 
    File _file = new File("/path/to/file"); // File | 
    try {
      CreateSuccessResponse result = apiInstance.vendorProductPriceFilesPost(companiesVendorId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorProductPriceFilesApi#vendorProductPriceFilesPost");
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
| **companiesVendorId** | **String**|  | |
| **_file** | **File**|  | |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Bad Request |  -  |

<a id="vendorProductPriceFilesVendorProductPriceFileIdGet"></a>
# **vendorProductPriceFilesVendorProductPriceFileIdGet**
> VendorProductPriceFilesVendorProductPriceFileIdGet200Response vendorProductPriceFilesVendorProductPriceFileIdGet(vendorProductPriceFileId)

Get a single price file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorProductPriceFilesApi;

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

    VendorProductPriceFilesApi apiInstance = new VendorProductPriceFilesApi(defaultClient);
    String vendorProductPriceFileId = "vendorProductPriceFileId_example"; // String | Automatically added
    try {
      VendorProductPriceFilesVendorProductPriceFileIdGet200Response result = apiInstance.vendorProductPriceFilesVendorProductPriceFileIdGet(vendorProductPriceFileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorProductPriceFilesApi#vendorProductPriceFilesVendorProductPriceFileIdGet");
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
| **vendorProductPriceFileId** | **String**| Automatically added | |

### Return type

[**VendorProductPriceFilesVendorProductPriceFileIdGet200Response**](VendorProductPriceFilesVendorProductPriceFileIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

