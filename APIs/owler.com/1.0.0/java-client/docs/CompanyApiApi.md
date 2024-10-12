# CompanyApiApi

All URIs are relative to *https://api.owler.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**basicCompanySearch**](CompanyApiApi.md#basicCompanySearch) | **GET** /v1/company/basicsearch | Basic Search Company by Ticker or Website or Name or PermID |
| [**fuzzyCompanySearch**](CompanyApiApi.md#fuzzyCompanySearch) | **GET** /v1/company/fuzzysearch | Fuzzy Search Company by Name or Address or Phone |
| [**searchCompany**](CompanyApiApi.md#searchCompany) | **GET** /v1/company/search | Search Company by Ticker or Website or Name or PermID |
| [**v1CompanyIdCompanyIdGet**](CompanyApiApi.md#v1CompanyIdCompanyIdGet) | **GET** /v1/company/id/{companyId} | Get Company by Id |
| [**v1CompanyUrlWebsiteGet**](CompanyApiApi.md#v1CompanyUrlWebsiteGet) | **GET** /v1/company/url/{website} | Get Company by URL |


<a id="basicCompanySearch"></a>
# **basicCompanySearch**
> BasicResults basicCompanySearch(q, fields, limit, format)

Basic Search Company by Ticker or Website or Name or PermID

The Company Basic Search API searches for a company based on the input and will returns results containing basic details about matching companies. By default the API returns the top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyApiApi apiInstance = new CompanyApiApi(defaultClient);
    String q = "q_example"; // String | Search term
    List<String> fields = Arrays.asList(); // List<String> | Fields to be searched - name, website, ticker, permid. If not specfied, will be searched against all fields
    String limit = "limit_example"; // String | Number of results to be displayed - 10 (by default, if not specified) to 30
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      BasicResults result = apiInstance.basicCompanySearch(q, fields, limit, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApiApi#basicCompanySearch");
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
| **q** | **String**| Search term | |
| **fields** | [**List&lt;String&gt;**](String.md)| Fields to be searched - name, website, ticker, permid. If not specfied, will be searched against all fields | [optional] [enum: name, website, ticker, permid] |
| **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 30 | [optional] |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**BasicResults**](BasicResults.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search Results |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="fuzzyCompanySearch"></a>
# **fuzzyCompanySearch**
> Object fuzzyCompanySearch(q, fields, limit, format)

Fuzzy Search Company by Name or Address or Phone

The Company Fuzzy Search API searches for a company based on the input and will return results containing basic details about matching companies. By default the API returns at most top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyApiApi apiInstance = new CompanyApiApi(defaultClient);
    String q = "q_example"; // String | Search term
    List<String> fields = Arrays.asList(); // List<String> | Fields to be searched - name, website, ticker, permid, address, phone. Each field and its corresponding value has to be specified
    String limit = "limit_example"; // String | Number of results to be displayed - 10 (by default, if not specified) to 30
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Object result = apiInstance.fuzzyCompanySearch(q, fields, limit, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApiApi#fuzzyCompanySearch");
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
| **q** | **String**| Search term | |
| **fields** | [**List&lt;String&gt;**](String.md)| Fields to be searched - name, website, ticker, permid, address, phone. Each field and its corresponding value has to be specified | [enum: name, website, ticker, permid, address, phone] |
| **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 30 | [optional] |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search Results |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="searchCompany"></a>
# **searchCompany**
> Results searchCompany(q, fields, limit, format)

Search Company by Ticker or Website or Name or PermID

The Company Search API searches for a company based on the input and will returns results containing basic details about matching companies. By default the API returns the top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyApiApi apiInstance = new CompanyApiApi(defaultClient);
    String q = "q_example"; // String | Search term
    List<String> fields = Arrays.asList(); // List<String> | Fields to be searched - name, website, ticker. If not specified, will be searched against all fields
    String limit = "limit_example"; // String | Number of results to be displayed - 10 (by default, if not specified) to 30
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Results result = apiInstance.searchCompany(q, fields, limit, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApiApi#searchCompany");
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
| **q** | **String**| Search term | |
| **fields** | [**List&lt;String&gt;**](String.md)| Fields to be searched - name, website, ticker. If not specified, will be searched against all fields | [optional] [enum: name, website, ticker, permid] |
| **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 30 | [optional] |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |

### Return type

[**Results**](Results.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search Results |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="v1CompanyIdCompanyIdGet"></a>
# **v1CompanyIdCompanyIdGet**
> Company v1CompanyIdCompanyIdGet(companyId, format)

Get Company by Id

The Company Data API provides complete information about a company for the specified Company Id 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyApiApi apiInstance = new CompanyApiApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Company result = apiInstance.v1CompanyIdCompanyIdGet(companyId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApiApi#v1CompanyIdCompanyIdGet");
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

<a id="v1CompanyUrlWebsiteGet"></a>
# **v1CompanyUrlWebsiteGet**
> Company v1CompanyUrlWebsiteGet(website, format)

Get Company by URL

The Company Data API provides complete information about a company for the specified URL 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CompanyApiApi apiInstance = new CompanyApiApi(defaultClient);
    String website = "website_example"; // String | Company Domain
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    try {
      Company result = apiInstance.v1CompanyUrlWebsiteGet(website, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApiApi#v1CompanyUrlWebsiteGet");
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

