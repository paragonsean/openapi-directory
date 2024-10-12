# CompanyApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companySearchRead**](CompanyApi.md#companySearchRead) | **GET** /api/v1/company/search/{company_name} | Return company search result |


<a id="companySearchRead"></a>
# **companySearchRead**
> companySearchRead(companyName)

Return company search result

Return company search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search companies,  For more details on how companies are listed [see here][ref]. [ref]: https://etmdb.com/en/company-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    String companyName = "companyName_example"; // String | 
    try {
      apiInstance.companySearchRead(companyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#companySearchRead");
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
| **companyName** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

