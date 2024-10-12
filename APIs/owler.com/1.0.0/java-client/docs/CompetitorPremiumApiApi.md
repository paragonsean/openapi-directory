# CompetitorPremiumApiApi

All URIs are relative to *https://api.owler.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CompanyCompetitorpremiumIdCompanyIdGet**](CompetitorPremiumApiApi.md#v1CompanyCompetitorpremiumIdCompanyIdGet) | **GET** /v1/company/competitorpremium/id/{companyId} | Get Competitor information by Id |
| [**v1CompanyCompetitorpremiumUrlWebsiteGet**](CompetitorPremiumApiApi.md#v1CompanyCompetitorpremiumUrlWebsiteGet) | **GET** /v1/company/competitorpremium/url/{website} | Get Competitor information by Url |


<a id="v1CompanyCompetitorpremiumIdCompanyIdGet"></a>
# **v1CompanyCompetitorpremiumIdCompanyIdGet**
> Competitors v1CompanyCompetitorpremiumIdCompanyIdGet(companyId, paginationId, format)

Get Competitor information by Id

The Competitors API provides basic information about all competitors of a given company Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompetitorPremiumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompetitorPremiumApiApi apiInstance = new CompetitorPremiumApiApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String paginationId = "paginationId_example"; // String | Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors.
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Competitors result = apiInstance.v1CompanyCompetitorpremiumIdCompanyIdGet(companyId, paginationId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompetitorPremiumApiApi#v1CompanyCompetitorpremiumIdCompanyIdGet");
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
| **companyId** | **String**| Company Id | |
| **paginationId** | **String**| Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors. | [optional] |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**Competitors**](Competitors.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Competitors Data |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **404** | Resource Not Found |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="v1CompanyCompetitorpremiumUrlWebsiteGet"></a>
# **v1CompanyCompetitorpremiumUrlWebsiteGet**
> Competitors v1CompanyCompetitorpremiumUrlWebsiteGet(website, paginationId, format)

Get Competitor information by Url

The Competitors API provides basic information about all competitors of a given company Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompetitorPremiumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompetitorPremiumApiApi apiInstance = new CompetitorPremiumApiApi(defaultClient);
    String website = "website_example"; // String | Company Id
    String paginationId = "paginationId_example"; // String | Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors.
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Competitors result = apiInstance.v1CompanyCompetitorpremiumUrlWebsiteGet(website, paginationId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompetitorPremiumApiApi#v1CompanyCompetitorpremiumUrlWebsiteGet");
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
| **website** | **String**| Company Id | |
| **paginationId** | **String**| Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors. | [optional] |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**Competitors**](Competitors.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Competitors Data |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **404** | Resource Not Found |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

