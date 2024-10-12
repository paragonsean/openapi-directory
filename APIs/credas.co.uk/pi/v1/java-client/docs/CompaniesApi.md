# CompaniesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompany**](CompaniesApi.md#getCompany) | **GET** /api/companies/{companyId} |  |
| [**searchCompany**](CompaniesApi.md#searchCompany) | **POST** /api/companies | Searches for a company based on its Company Number and returns its details. |


<a id="getCompany"></a>
# **getCompany**
> CredasApiModelsCompaniesCompanyDetail getCompany(companyId, apikey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    UUID companyId = UUID.randomUUID(); // UUID | 
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsCompaniesCompanyDetail result = apiInstance.getCompany(companyId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#getCompany");
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
| **companyId** | **UUID**|  | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsCompaniesCompanyDetail**](CredasApiModelsCompaniesCompanyDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | If the consumer doesn&#39;t have the required permission to use the endpoint. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="searchCompany"></a>
# **searchCompany**
> CredasApiModelsCompaniesCompanyDetail searchCompany(apikey, companyNumber)

Searches for a company based on its Company Number and returns its details.

If a company appears multiple times within the structure, it will only be detailed in full (i.e. with significant ownership details) in its first instance. Subsequent instances will be               marked as duplicates.              Whilst duplicate instances of companies can and will be identified, it is not possible to categorically identify duplicated people.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    String companyNumber = "companyNumber_example"; // String | The company registration number of the company that should be searched.
    try {
      CredasApiModelsCompaniesCompanyDetail result = apiInstance.searchCompany(apikey, companyNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#searchCompany");
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
| **apikey** | **String**| ApiKey supplied. | |
| **companyNumber** | **String**| The company registration number of the company that should be searched. | [optional] |

### Return type

[**CredasApiModelsCompaniesCompanyDetail**](CredasApiModelsCompaniesCompanyDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | If the consumer doesn&#39;t have the required permission to use the endpoint. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

