# MultipleQrCodesApi

All URIs are relative to *https://run.byvalue.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**qrCodeBatchBatchQrcodePost**](MultipleQrCodesApi.md#qrCodeBatchBatchQrcodePost) | **POST** /batch/qrcode | QR Code Batch |


<a id="qrCodeBatchBatchQrcodePost"></a>
# **qrCodeBatchBatchQrcodePost**
> File qrCodeBatchBatchQrcodePost(autoQRCodeBatch)

QR Code Batch

This endpoint allows you to generate an archive containing multiple QR Codes with a single request. The endpoint response is the archive containing the generated image files and &#x60;items.json&#x60; file which is a record of the specifications of each of the files in the archive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleQrCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    MultipleQrCodesApi apiInstance = new MultipleQrCodesApi(defaultClient);
    AutoQRCodeBatch autoQRCodeBatch = new AutoQRCodeBatch(); // AutoQRCodeBatch | 
    try {
      File result = apiInstance.qrCodeBatchBatchQrcodePost(autoQRCodeBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleQrCodesApi#qrCodeBatchBatchQrcodePost");
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
| **autoQRCodeBatch** | [**AutoQRCodeBatch**](AutoQRCodeBatch.md)|  | |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/gzip, application/zip, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return an images bundle |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

