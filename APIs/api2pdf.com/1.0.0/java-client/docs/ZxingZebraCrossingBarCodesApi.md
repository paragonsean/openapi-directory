# ZxingZebraCrossingBarCodesApi

All URIs are relative to *https://v2018.api2pdf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**zebraGET**](ZxingZebraCrossingBarCodesApi.md#zebraGET) | **GET** /zebra | Generate bar codes and QR codes with ZXING. |


<a id="zebraGET"></a>
# **zebraGET**
> File zebraGET(format, value, showlabel, height, width)

Generate bar codes and QR codes with ZXING.

See full list of options and documentation [here](https://www.api2pdf.com/documentation/advanced-options-zxing-zebra-crossing-barcodes/) ### Authorize via Query String Parameter **apikey&#x3D;YOUR-API-KEY** ### Example &#x60;&#x60;&#x60; https://v2018.api2pdf.com/zebra?format&#x3D;{format}&amp;apikey&#x3D;{YourApiKey}&amp;value&#x3D;{YourText} &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZxingZebraCrossingBarCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://v2018.api2pdf.com");
    
    // Configure API key authorization: QueryApiKey
    ApiKeyAuth QueryApiKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryApiKey");
    QueryApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryApiKey.setApiKeyPrefix("Token");

    ZxingZebraCrossingBarCodesApi apiInstance = new ZxingZebraCrossingBarCodesApi(defaultClient);
    String format = "format_example"; // String | Most common is CODE_39 or QR_CODE
    String value = "value_example"; // String | Specify the text value you want to convert
    Boolean showlabel = true; // Boolean | Show label of text below barcode
    Integer height = 56; // Integer | Height of the barcode generated image
    Integer width = 56; // Integer | Width of the barcode generated image
    try {
      File result = apiInstance.zebraGET(format, value, showlabel, height, width);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZxingZebraCrossingBarCodesApi#zebraGET");
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
| **format** | **String**| Most common is CODE_39 or QR_CODE | |
| **value** | **String**| Specify the text value you want to convert | |
| **showlabel** | **Boolean**| Show label of text below barcode | [optional] |
| **height** | **Integer**| Height of the barcode generated image | [optional] |
| **width** | **Integer**| Width of the barcode generated image | [optional] |

### Return type

[**File**](File.md)

### Authorization

[QueryApiKey](../README.md#QueryApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An image of the generated barcode or QR code |  -  |

