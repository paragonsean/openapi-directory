# BarcodeGeneratorApi

All URIs are relative to *https://api.exoapi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**barcodeGeneratorPost**](BarcodeGeneratorApi.md#barcodeGeneratorPost) | **POST** /barcode-generator |  |


<a id="barcodeGeneratorPost"></a>
# **barcodeGeneratorPost**
> File barcodeGeneratorPost(barcodeGeneratorPostRequest)



Generate high quality QR code &amp; barcode images in a matter of seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BarcodeGeneratorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exoapi.dev");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    BarcodeGeneratorApi apiInstance = new BarcodeGeneratorApi(defaultClient);
    BarcodeGeneratorPostRequest barcodeGeneratorPostRequest = new BarcodeGeneratorPostRequest(); // BarcodeGeneratorPostRequest | 
    try {
      File result = apiInstance.barcodeGeneratorPost(barcodeGeneratorPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BarcodeGeneratorApi#barcodeGeneratorPost");
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
| **barcodeGeneratorPostRequest** | [**BarcodeGeneratorPostRequest**](BarcodeGeneratorPostRequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png, image/svg+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 🟢 200 OK |  -  |
| **400** | 🟡 400 Bad request |  -  |
| **401** | 🟡 401 Unauthorized |  -  |
| **429** | 🟡 429 Too many requests |  -  |
| **500** | 🔴 500 Internal server error |  -  |

