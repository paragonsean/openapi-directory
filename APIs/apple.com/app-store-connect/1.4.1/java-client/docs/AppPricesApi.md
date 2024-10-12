# AppPricesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appPricesGetInstance**](AppPricesApi.md#appPricesGetInstance) | **GET** /v1/appPrices/{id} |  |


<a id="appPricesGetInstance"></a>
# **appPricesGetInstance**
> AppPriceResponse appPricesGetInstance(id, fieldsAppPrices, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPricesApi apiInstance = new AppPricesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPrices = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPrices
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppPriceResponse result = apiInstance.appPricesGetInstance(id, fieldsAppPrices, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPricesApi#appPricesGetInstance");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsAppPrices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPrices | [optional] [enum: app, priceTier] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, priceTier] |

### Return type

[**AppPriceResponse**](AppPriceResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppPrice |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

