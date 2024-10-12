# CountryApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCountryList**](CountryApi.md#getCountryList) | **GET** /v1/countries | List all countries |


<a id="getCountryList"></a>
# **getCountryList**
> CountryListVO getCountryList()

List all countries

List all countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    CountryApi apiInstance = new CountryApi(defaultClient);
    try {
      CountryListVO result = apiInstance.getCountryList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getCountryList");
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

[**CountryListVO**](CountryListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

