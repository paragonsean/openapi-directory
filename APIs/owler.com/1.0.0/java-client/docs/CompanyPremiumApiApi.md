# CompanyPremiumApiApi

All URIs are relative to *https://api.owler.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CompanypremiumIdCompanyIdGet**](CompanyPremiumApiApi.md#v1CompanypremiumIdCompanyIdGet) | **GET** /v1/companypremium/id/{companyId} | Get Complete Company Info by Id |
| [**v1CompanypremiumUrlWebsiteGet**](CompanyPremiumApiApi.md#v1CompanypremiumUrlWebsiteGet) | **GET** /v1/companypremium/url/{website} | Get Basic Company Info by Url |


<a id="v1CompanypremiumIdCompanyIdGet"></a>
# **v1CompanypremiumIdCompanyIdGet**
> Company v1CompanypremiumIdCompanyIdGet(companyId, format)

Get Complete Company Info by Id

The Company Premium Data API provides complete information about a company for the specified Company Id 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyPremiumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyPremiumApiApi apiInstance = new CompanyPremiumApiApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Company result = apiInstance.v1CompanypremiumIdCompanyIdGet(companyId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyPremiumApiApi#v1CompanypremiumIdCompanyIdGet");
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

[**Company**](Company.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Company Data |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **404** | Resource Not Found |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="v1CompanypremiumUrlWebsiteGet"></a>
# **v1CompanypremiumUrlWebsiteGet**
> Company v1CompanypremiumUrlWebsiteGet(website, format)

Get Basic Company Info by Url

The Company Data API provides complete information about a company for the specified URL 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyPremiumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyPremiumApiApi apiInstance = new CompanyPremiumApiApi(defaultClient);
    String website = "website_example"; // String | Company Domain
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Company result = apiInstance.v1CompanypremiumUrlWebsiteGet(website, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyPremiumApiApi#v1CompanypremiumUrlWebsiteGet");
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
| **website** | **String**| Company Domain | |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**Company**](Company.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Company Data |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **404** | Resource Not Found |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

