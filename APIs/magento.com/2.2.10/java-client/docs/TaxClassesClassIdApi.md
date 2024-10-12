# TaxClassesClassIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxClassRepositoryV1SavePut**](TaxClassesClassIdApi.md#taxTaxClassRepositoryV1SavePut) | **PUT** /V1/taxClasses/{classId} | taxClasses/{classId} |


<a id="taxTaxClassRepositoryV1SavePut"></a>
# **taxTaxClassRepositoryV1SavePut**
> String taxTaxClassRepositoryV1SavePut(classId, taxTaxClassRepositoryV1SavePostRequest)

taxClasses/{classId}

Create a Tax Class

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxClassesClassIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxClassesClassIdApi apiInstance = new TaxClassesClassIdApi(defaultClient);
    String classId = "classId_example"; // String | 
    TaxTaxClassRepositoryV1SavePostRequest taxTaxClassRepositoryV1SavePostRequest = new TaxTaxClassRepositoryV1SavePostRequest(); // TaxTaxClassRepositoryV1SavePostRequest | 
    try {
      String result = apiInstance.taxTaxClassRepositoryV1SavePut(classId, taxTaxClassRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxClassesClassIdApi#taxTaxClassRepositoryV1SavePut");
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
| **classId** | **String**|  | |
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

