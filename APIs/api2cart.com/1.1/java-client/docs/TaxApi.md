# TaxApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxClassInfo**](TaxApi.md#taxClassInfo) | **GET** /tax.class.info.json |  |


<a id="taxClassInfo"></a>
# **taxClassInfo**
> TaxClassInfo200Response taxClassInfo(taxClassId, storeId, langId, params, responseFields, exclude)



Get info about tax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    TaxApi apiInstance = new TaxApi(defaultClient);
    String taxClassId = "taxClassId_example"; // String | Retrieves taxes specified by class id
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String params = "tax_class_id,name,avail"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      TaxClassInfo200Response result = apiInstance.taxClassInfo(taxClassId, storeId, langId, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxApi#taxClassInfo");
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
| **taxClassId** | **String**| Retrieves taxes specified by class id | |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to tax_class_id,name,avail] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**TaxClassInfo200Response**](TaxClassInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

