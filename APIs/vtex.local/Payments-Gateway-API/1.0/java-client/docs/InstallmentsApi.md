# InstallmentsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**installmentsoptions**](InstallmentsApi.md#installmentsoptions) | **GET** /api/pvt/installments | Installments options |


<a id="installmentsoptions"></a>
# **installmentsoptions**
> ValidRequest installmentsoptions(requestValue, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, requestSalesChannel, requestPaymentDetails0Id, requestPaymentDetails0Value, requestPaymentDetails0Bin)

Installments options

Returns the best installment options according to the informed params.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstallmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    InstallmentsApi apiInstance = new InstallmentsApi(defaultClient);
    Integer requestValue = 10; // Integer | 
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    Integer requestSalesChannel = 1; // Integer | 
    Integer requestPaymentDetails0Id = 2; // Integer | 
    Integer requestPaymentDetails0Value = 10; // Integer | 
    Integer requestPaymentDetails0Bin = 411111; // Integer | 
    try {
      ValidRequest result = apiInstance.installmentsoptions(requestValue, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, requestSalesChannel, requestPaymentDetails0Id, requestPaymentDetails0Value, requestPaymentDetails0Bin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstallmentsApi#installmentsoptions");
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
| **requestValue** | **Integer**|  | |
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **requestSalesChannel** | **Integer**|  | [optional] |
| **requestPaymentDetails0Id** | **Integer**|  | [optional] |
| **requestPaymentDetails0Value** | **Integer**|  | [optional] |
| **requestPaymentDetails0Bin** | **Integer**|  | [optional] |

### Return type

[**ValidRequest**](ValidRequest.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-Accel-Expires -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * x-vtex-operation-id -  <br>  |
| **400** | Bad Request |  -  |

