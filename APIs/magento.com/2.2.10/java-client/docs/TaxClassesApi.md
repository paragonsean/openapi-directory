# TaxClassesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxClassRepositoryV1SavePost**](TaxClassesApi.md#taxTaxClassRepositoryV1SavePost) | **POST** /V1/taxClasses | taxClasses |


<a id="taxTaxClassRepositoryV1SavePost"></a>
# **taxTaxClassRepositoryV1SavePost**
> String taxTaxClassRepositoryV1SavePost(taxTaxClassRepositoryV1SavePostRequest)

taxClasses

Create a Tax Class

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxClassesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxClassesApi apiInstance = new TaxClassesApi(defaultClient);
    TaxTaxClassRepositoryV1SavePostRequest taxTaxClassRepositoryV1SavePostRequest = new TaxTaxClassRepositoryV1SavePostRequest(); // TaxTaxClassRepositoryV1SavePostRequest | 
    try {
      String result = apiInstance.taxTaxClassRepositoryV1SavePost(taxTaxClassRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxClassesApi#taxTaxClassRepositoryV1SavePost");
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
| **taxTaxClassRepositoryV1SavePostRequest** | [**TaxTaxClassRepositoryV1SavePostRequest**](TaxTaxClassRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

