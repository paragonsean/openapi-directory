# DirectoryCountriesCountryIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**directoryCountryInformationAcquirerV1GetCountryInfoGet**](DirectoryCountriesCountryIdApi.md#directoryCountryInformationAcquirerV1GetCountryInfoGet) | **GET** /V1/directory/countries/{countryId} | directory/countries/{countryId} |


<a id="directoryCountryInformationAcquirerV1GetCountryInfoGet"></a>
# **directoryCountryInformationAcquirerV1GetCountryInfoGet**
> DirectoryDataCountryInformationInterface directoryCountryInformationAcquirerV1GetCountryInfoGet(countryId)

directory/countries/{countryId}

Get country and region information for the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryCountriesCountryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    DirectoryCountriesCountryIdApi apiInstance = new DirectoryCountriesCountryIdApi(defaultClient);
    String countryId = "countryId_example"; // String | 
    try {
      DirectoryDataCountryInformationInterface result = apiInstance.directoryCountryInformationAcquirerV1GetCountryInfoGet(countryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryCountriesCountryIdApi#directoryCountryInformationAcquirerV1GetCountryInfoGet");
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
| **countryId** | **String**|  | |

### Return type

[**DirectoryDataCountryInformationInterface**](DirectoryDataCountryInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

