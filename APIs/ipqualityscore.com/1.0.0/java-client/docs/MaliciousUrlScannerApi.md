# MaliciousUrlScannerApi

All URIs are relative to *https://ipqualityscore.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**maliciousUrlScanner**](MaliciousUrlScannerApi.md#maliciousUrlScanner) | **GET** /json/url/{YOUR_API_KEY_HERE}/{URL_HERE} | Malicious URL Scanner |


<a id="maliciousUrlScanner"></a>
# **maliciousUrlScanner**
> MaliciousUrlScanner200Response maliciousUrlScanner(YOUR_API_KEY_HERE, URL_HERE)

Malicious URL Scanner

Malicious URL Scanner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaliciousUrlScannerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ipqualityscore.com/api");

    MaliciousUrlScannerApi apiInstance = new MaliciousUrlScannerApi(defaultClient);
    String YOUR_API_KEY_HERE = "asd24#sdfs322#"; // String | (Required) YOUR_API_KEY_HERE
    String URL_HERE = "https%3A%2F%2Fgoogle.com"; // String | (Required) URL_HERE
    try {
      MaliciousUrlScanner200Response result = apiInstance.maliciousUrlScanner(YOUR_API_KEY_HERE, URL_HERE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaliciousUrlScannerApi#maliciousUrlScanner");
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
| **YOUR_API_KEY_HERE** | **String**| (Required) YOUR_API_KEY_HERE | |
| **URL_HERE** | **String**| (Required) URL_HERE | |

### Return type

[**MaliciousUrlScanner200Response**](MaliciousUrlScanner200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad Request |  -  |
| **500** | Unexpected error |  -  |

