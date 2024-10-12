# DirectoryCountriesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**directoryCountryInformationAcquirerV1GetCountriesInfoGet**](DirectoryCountriesApi.md#directoryCountryInformationAcquirerV1GetCountriesInfoGet) | **GET** /V1/directory/countries | directory/countries |


<a id="directoryCountryInformationAcquirerV1GetCountriesInfoGet"></a>
# **directoryCountryInformationAcquirerV1GetCountriesInfoGet**
> List&lt;DirectoryDataCountryInformationInterface&gt; directoryCountryInformationAcquirerV1GetCountriesInfoGet()

directory/countries

Get all countries and regions information for the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryCountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    DirectoryCountriesApi apiInstance = new DirectoryCountriesApi(defaultClient);
    try {
      List<DirectoryDataCountryInformationInterface> result = apiInstance.directoryCountryInformationAcquirerV1GetCountriesInfoGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryCountriesApi#directoryCountryInformationAcquirerV1GetCountriesInfoGet");
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

[**List&lt;DirectoryDataCountryInformationInterface&gt;**](DirectoryDataCountryInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **0** | Unexpected error |  -  |

