# CompetitorApiApi

All URIs are relative to *https://api.owler.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CompanyCompetitorIdCompanyIdGet**](CompetitorApiApi.md#v1CompanyCompetitorIdCompanyIdGet) | **GET** /v1/company/competitor/id/{companyId} | Get Competitor information by Id |
| [**v1CompanyCompetitorUrlWebsiteGet**](CompetitorApiApi.md#v1CompanyCompetitorUrlWebsiteGet) | **GET** /v1/company/competitor/url/{website} | Get Competitor information by URL |


<a id="v1CompanyCompetitorIdCompanyIdGet"></a>
# **v1CompanyCompetitorIdCompanyIdGet**
> CompanyCompetitorVO v1CompanyCompetitorIdCompanyIdGet(companyId, format)

Get Competitor information by Id

The Competitors API provides basic information about top 3 competitors of a company specified in the Company Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompetitorApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompetitorApiApi apiInstance = new CompetitorApiApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      CompanyCompetitorVO result = apiInstance.v1CompanyCompetitorIdCompanyIdGet(companyId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompetitorApiApi#v1CompanyCompetitorIdCompanyIdGet");
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
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**CompanyCompetitorVO**](CompanyCompetitorVO.md)

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

<a id="v1CompanyCompetitorUrlWebsiteGet"></a>
# **v1CompanyCompetitorUrlWebsiteGet**
> CompanyCompetitorVO v1CompanyCompetitorUrlWebsiteGet(website, format)

Get Competitor information by URL

The Competitors API provides basic information about top 3 competitors of a company specified in the website

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompetitorApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompetitorApiApi apiInstance = new CompetitorApiApi(defaultClient);
    String website = "website_example"; // String | Company Id
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      CompanyCompetitorVO result = apiInstance.v1CompanyCompetitorUrlWebsiteGet(website, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompetitorApiApi#v1CompanyCompetitorUrlWebsiteGet");
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
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**CompanyCompetitorVO**](CompanyCompetitorVO.md)

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

