# DirectoryCurrencyApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet**](DirectoryCurrencyApi.md#directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet) | **GET** /V1/directory/currency | directory/currency |


<a id="directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet"></a>
# **directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet**
> DirectoryDataCurrencyInformationInterface directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet()

directory/currency

Get currency information for the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryCurrencyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    DirectoryCurrencyApi apiInstance = new DirectoryCurrencyApi(defaultClient);
    try {
      DirectoryDataCurrencyInformationInterface result = apiInstance.directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryCurrencyApi#directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet");
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

[**DirectoryDataCurrencyInformationInterface**](DirectoryDataCurrencyInformationInterface.md)

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

