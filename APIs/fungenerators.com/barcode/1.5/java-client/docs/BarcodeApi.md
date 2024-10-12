# BarcodeApi

All URIs are relative to *http://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**barcodeDecodePost**](BarcodeApi.md#barcodeDecodePost) | **POST** /barcode/decode |  |
| [**barcodeDecodeTypesGet**](BarcodeApi.md#barcodeDecodeTypesGet) | **GET** /barcode/decode/types |  |
| [**barcodeEncodeGet**](BarcodeApi.md#barcodeEncodeGet) | **GET** /barcode/encode |  |
| [**barcodeEncodeTypesGet**](BarcodeApi.md#barcodeEncodeTypesGet) | **GET** /barcode/encode/types |  |


<a id="barcodeDecodePost"></a>
# **barcodeDecodePost**
> barcodeDecodePost(barimage)



Decode a Barcode image and return the cotents if successful

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BarcodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    BarcodeApi apiInstance = new BarcodeApi(defaultClient);
    File barimage = new File("/path/to/file"); // File | Barcode image to decode and get the content value
    try {
      apiInstance.barcodeDecodePost(barimage);
    } catch (ApiException e) {
      System.err.println("Exception when calling BarcodeApi#barcodeDecodePost");
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
| **barimage** | **File**| Barcode image to decode and get the content value | |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="barcodeDecodeTypesGet"></a>
# **barcodeDecodeTypesGet**
> barcodeDecodeTypesGet()



Get the supported barcode types for the decoding process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BarcodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    BarcodeApi apiInstance = new BarcodeApi(defaultClient);
    try {
      apiInstance.barcodeDecodeTypesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling BarcodeApi#barcodeDecodeTypesGet");
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

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="barcodeEncodeGet"></a>
# **barcodeEncodeGet**
> barcodeEncodeGet(number, barcodeformat, outputformat, widthfactor, totalheight)



Get a Bar Code image for the given barcode number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BarcodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    BarcodeApi apiInstance = new BarcodeApi(defaultClient);
    String number = "number_example"; // String | Barcode number
    String barcodeformat = "barcodeformat_example"; // String | Barcode format default C39. Valid values are the keys to those returned from /barcode/encode/types.
    String outputformat = "outputformat_example"; // String | Output image format. Must be one of png/html/jpg/svg
    Integer widthfactor = 56; // Integer | Width factor of the image
    Integer totalheight = 56; // Integer | Total height of the image
    try {
      apiInstance.barcodeEncodeGet(number, barcodeformat, outputformat, widthfactor, totalheight);
    } catch (ApiException e) {
      System.err.println("Exception when calling BarcodeApi#barcodeEncodeGet");
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
| **number** | **String**| Barcode number | |
| **barcodeformat** | **String**| Barcode format default C39. Valid values are the keys to those returned from /barcode/encode/types. | [optional] |
| **outputformat** | **String**| Output image format. Must be one of png/html/jpg/svg | [optional] |
| **widthfactor** | **Integer**| Width factor of the image | [optional] |
| **totalheight** | **Integer**| Total height of the image | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="barcodeEncodeTypesGet"></a>
# **barcodeEncodeTypesGet**
> barcodeEncodeTypesGet()



Get the supported barcode types for encoding / image generation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BarcodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    BarcodeApi apiInstance = new BarcodeApi(defaultClient);
    try {
      apiInstance.barcodeEncodeTypesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling BarcodeApi#barcodeEncodeTypesGet");
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

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

