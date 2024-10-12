# V1CompanyApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyAlternativeSearch**](V1CompanyApi.md#companyAlternativeSearch) | **POST** /api/v1/company/search/{country} | Retrieves a list of companies from the KYC API company index |
| [**companyAnnouncement**](V1CompanyApi.md#companyAnnouncement) | **GET** /api/v1/company/announcement/{id} | Retrieves announcement data |
| [**companyDeepsearchISIN**](V1CompanyApi.md#companyDeepsearchISIN) | **POST** /api/v1/company/deepsearch/isin | Retrieves a list of stock exchange listings |
| [**companyDeepsearchLEI**](V1CompanyApi.md#companyDeepsearchLEI) | **GET** /api/v1/company/deepsearch/lei/{number} | Retrieves a list of companies |
| [**companyDeepsearchName**](V1CompanyApi.md#companyDeepsearchName) | **GET** /api/v1/company/deepsearch/name/{country}/{name} | Retrieves a list of companies from the official business register |
| [**companyDeepsearchNumber**](V1CompanyApi.md#companyDeepsearchNumber) | **GET** /api/v1/company/deepsearch/number/{country}/{number} | Retrieves a list of companies from the official business register |
| [**companyIdAnnouncements**](V1CompanyApi.md#companyIdAnnouncements) | **GET** /api/v1/company/{id}/announcements | Retrieves company announcements |
| [**companyIdDataset**](V1CompanyApi.md#companyIdDataset) | **GET** /api/v1/company/{id}/{dataset} | Retrieves company details |
| [**companyIdSuper**](V1CompanyApi.md#companyIdSuper) | **GET** /api/v1/company/{id}/super/{country} | Retrieves structured data extracted from a company document |
| [**companyMonitorChangeTypesList**](V1CompanyApi.md#companyMonitorChangeTypesList) | **GET** /api/v1/company/monitoring/changeTypes | Get available ChangeTypes |
| [**companyMonitorId**](V1CompanyApi.md#companyMonitorId) | **GET** /api/v1/company/monitoring/list/{id} | Get monitor status for specific company id |
| [**companyMonitorList**](V1CompanyApi.md#companyMonitorList) | **GET** /api/v1/company/monitoring/list | Retrieves a list of registered monitors |
| [**companyMonitorRegister**](V1CompanyApi.md#companyMonitorRegister) | **POST** /api/v1/company/monitoring/register/{id} | Register a Company for monitoring |
| [**companyMonitorUnregister**](V1CompanyApi.md#companyMonitorUnregister) | **POST** /api/v1/company/monitoring/unregister/{id} | Deactivates an active notification |
| [**companyNotificationId**](V1CompanyApi.md#companyNotificationId) | **GET** /api/v1/company/notification/list/{id} | Retrieves a list of registered notifications |
| [**companyNotificationList**](V1CompanyApi.md#companyNotificationList) | **GET** /api/v1/company/notification/list | Retrieves a list of registered notifications |
| [**companyNotificationRegister**](V1CompanyApi.md#companyNotificationRegister) | **POST** /api/v1/company/notification/register/{id} | Creates a new notification |
| [**companyNotificationUnregister**](V1CompanyApi.md#companyNotificationUnregister) | **POST** /api/v1/company/notification/unregister/{id} | Unregister a company from Monitoring |
| [**companySearchName**](V1CompanyApi.md#companySearchName) | **GET** /api/v1/company/search/name/{country}/{name} | Retrieves a list of companies from the KYC API company index |
| [**companySearchNumber**](V1CompanyApi.md#companySearchNumber) | **GET** /api/v1/company/search/number/{country}/{number} | Retrieves a list of companies from the KYC API company index |


<a id="companyAlternativeSearch"></a>
# **companyAlternativeSearch**
> companyAlternativeSearch(country, address, name, number, phone, url, vat)

Retrieves a list of companies from the KYC API company index

KYC API company index lookup by country and mixed parameters. This function requires a country code then a mixture of name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String address = "address_example"; // String | Company address (or address partial)
    String name = "name_example"; // String | Company name
    String number = "number_example"; // String | Company registration number
    String phone = "phone_example"; // String | Company contact phone number
    String url = "url_example"; // String | Company url
    String vat = "vat_example"; // String | Company VAT number
    try {
      apiInstance.companyAlternativeSearch(country, address, name, number, phone, url, vat);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyAlternativeSearch");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **address** | **String**| Company address (or address partial) | [optional] |
| **name** | **String**| Company name | [optional] |
| **number** | **String**| Company registration number | [optional] |
| **phone** | **String**| Company contact phone number | [optional] |
| **url** | **String**| Company url | [optional] |
| **vat** | **String**| Company VAT number | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyAnnouncement"></a>
# **companyAnnouncement**
> List&lt;CompanyAnnouncement200ResponseInner&gt; companyAnnouncement(id)

Retrieves announcement data

Request full announcement data identified by announcement id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | announcement hex ID
    try {
      List<CompanyAnnouncement200ResponseInner> result = apiInstance.companyAnnouncement(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyAnnouncement");
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
| **id** | **String**| announcement hex ID | |

### Return type

[**List&lt;CompanyAnnouncement200ResponseInner&gt;**](CompanyAnnouncement200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of announcements |  -  |
| **0** |  |  -  |

<a id="companyDeepsearchISIN"></a>
# **companyDeepsearchISIN**
> List&lt;CompanyDeepsearchISIN200ResponseInner&gt; companyDeepsearchISIN(isin)

Retrieves a list of stock exchange listings

Lookup stock exchange listings identified by an ISIN (International Securities Identification Number) number. Search is forwarded to a provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String isin = "isin_example"; // String | A list of ISIN numbers seperated by comma (maximum) is 100
    try {
      List<CompanyDeepsearchISIN200ResponseInner> result = apiInstance.companyDeepsearchISIN(isin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyDeepsearchISIN");
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
| **isin** | **String**| A list of ISIN numbers seperated by comma (maximum) is 100 | [optional] |

### Return type

[**List&lt;CompanyDeepsearchISIN200ResponseInner&gt;**](CompanyDeepsearchISIN200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a lookup by ISIN number |  -  |
| **0** |  |  -  |

<a id="companyDeepsearchLEI"></a>
# **companyDeepsearchLEI**
> CompanyDeepsearchLEI200Response companyDeepsearchLEI(number, page)

Retrieves a list of companies

Lookup companies identified by a LEI (Legal Entity Identifier) number. Search is forwarded to a provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String number = "number_example"; // String | lei number
    Integer page = 1; // Integer | Pagination for the ISIN number results (1000 numbers per page)
    try {
      CompanyDeepsearchLEI200Response result = apiInstance.companyDeepsearchLEI(number, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyDeepsearchLEI");
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
| **number** | **String**| lei number | |
| **page** | **Integer**| Pagination for the ISIN number results (1000 numbers per page) | [optional] |

### Return type

[**CompanyDeepsearchLEI200Response**](CompanyDeepsearchLEI200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a lookup by LEI number |  -  |
| **0** |  |  -  |

<a id="companyDeepsearchName"></a>
# **companyDeepsearchName**
> companyDeepsearchName(country, name)

Retrieves a list of companies from the official business register

Search for companies with a certain name. Search is forwarded to the respective business register of the country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String name = "name_example"; // String | company name
    try {
      apiInstance.companyDeepsearchName(country, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyDeepsearchName");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **name** | **String**| company name | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyDeepsearchNumber"></a>
# **companyDeepsearchNumber**
> companyDeepsearchNumber(country, number)

Retrieves a list of companies from the official business register

Search for companies with a certain register number. Search is forwarded to the respective business register of the country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String number = "number_example"; // String | company registration number
    try {
      apiInstance.companyDeepsearchNumber(country, number);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyDeepsearchNumber");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **number** | **String**| company registration number | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyIdAnnouncements"></a>
# **companyIdAnnouncements**
> companyIdAnnouncements(id, limit, offset, data)

Retrieves company announcements

Search announcements filed to the business register from a company identified by an id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | company hex ID
    Integer limit = 56; // Integer | limit of announcements in response (default 10)
    Integer offset = 56; // Integer | to paginate through results (default 0)
    Boolean data = true; // Boolean | If this parameter is set to false, you will only receive ids, and no additional data about announcements and no hits to the metric will be counted. (and potentially minimizing your costs)
    try {
      apiInstance.companyIdAnnouncements(id, limit, offset, data);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyIdAnnouncements");
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
| **id** | **String**| company hex ID | |
| **limit** | **Integer**| limit of announcements in response (default 10) | [optional] |
| **offset** | **Integer**| to paginate through results (default 0) | [optional] |
| **data** | **Boolean**| If this parameter is set to false, you will only receive ids, and no additional data about announcements and no hits to the metric will be counted. (and potentially minimizing your costs) | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyIdDataset"></a>
# **companyIdDataset**
> Object companyIdDataset(id, dataset, checkStockListing, lang)

Retrieves company details

Get company details by id. The level of details is defined by the dataset parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | company master data by id
    String dataset = ""; // String | company master data by id
    Boolean checkStockListing = true; // Boolean | Try to retrieve additional stock information for this company. (Only available on refresh)
    String lang = ""; // String | Optional data translation (only available in limited jurisdictions)
    try {
      Object result = apiInstance.companyIdDataset(id, dataset, checkStockListing, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyIdDataset");
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
| **id** | **String**| company master data by id | |
| **dataset** | **String**| company master data by id | [enum: , mini, master, full, refresh] |
| **checkStockListing** | **Boolean**| Try to retrieve additional stock information for this company. (Only available on refresh) | [optional] |
| **lang** | **String**| Optional data translation (only available in limited jurisdictions) | [optional] [enum: , EN, ES, FR] |

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyIdSuper"></a>
# **companyIdSuper**
> companyIdSuper(id, country, lang)

Retrieves structured data extracted from a company document

Request company superdata identified by company id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | company superdata by id
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String lang = ""; // String | Optional data translation (only available in limited jurisdictions)
    try {
      apiInstance.companyIdSuper(id, country, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyIdSuper");
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
| **id** | **String**| company superdata by id | |
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **lang** | **String**| Optional data translation (only available in limited jurisdictions) | [optional] [enum: , OG, EN] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyMonitorChangeTypesList"></a>
# **companyMonitorChangeTypesList**
> List&lt;String&gt; companyMonitorChangeTypesList()

Get available ChangeTypes

Get current list of available ChangeTypes to subscribe to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    try {
      List<String> result = apiInstance.companyMonitorChangeTypesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyMonitorChangeTypesList");
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

**List&lt;String&gt;**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of ChangeTypes |  -  |
| **0** |  |  -  |

<a id="companyMonitorId"></a>
# **companyMonitorId**
> companyMonitorId(id)

Get monitor status for specific company id

Query status of registered monitors for a specific company identified by a company id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | Company Hex ID
    try {
      apiInstance.companyMonitorId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyMonitorId");
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
| **id** | **String**| Company Hex ID | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyMonitorList"></a>
# **companyMonitorList**
> companyMonitorList()

Retrieves a list of registered monitors

Query list of all registered monitors for logged in user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    try {
      apiInstance.companyMonitorList();
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyMonitorList");
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

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyMonitorRegister"></a>
# **companyMonitorRegister**
> companyMonitorRegister(id, callbackUrl, changeType)

Register a Company for monitoring

Add a company to your perpetual monitoring list and register a callback URL to get monitoring alerts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | Company Hex ID
    String callbackUrl = "callbackUrl_example"; // String | Callback URL
    String changeType = "changeType_example"; // String | ChangeType to monitor
    try {
      apiInstance.companyMonitorRegister(id, callbackUrl, changeType);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyMonitorRegister");
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
| **id** | **String**| Company Hex ID | |
| **callbackUrl** | **String**| Callback URL | |
| **changeType** | **String**| ChangeType to monitor | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyMonitorUnregister"></a>
# **companyMonitorUnregister**
> companyMonitorUnregister(id)

Deactivates an active notification

Deactivate a previously registered company monitor identified by the notifier id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | Registration id of monitoring request record
    try {
      apiInstance.companyMonitorUnregister(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyMonitorUnregister");
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
| **id** | **String**| Registration id of monitoring request record | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty response body |  -  |
| **0** |  |  -  |

<a id="companyNotificationId"></a>
# **companyNotificationId**
> List&lt;CompanyNotificationId200ResponseInner&gt; companyNotificationId(id)

Retrieves a list of registered notifications

Query list of registered notifications for a specific company identified by a company id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | Company Hex ID
    try {
      List<CompanyNotificationId200ResponseInner> result = apiInstance.companyNotificationId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyNotificationId");
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
| **id** | **String**| Company Hex ID | |

### Return type

[**List&lt;CompanyNotificationId200ResponseInner&gt;**](CompanyNotificationId200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of monitor webhooks |  -  |
| **0** |  |  -  |

<a id="companyNotificationList"></a>
# **companyNotificationList**
> companyNotificationList()

Retrieves a list of registered notifications

Query list of registered callback URLs for logged in user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    try {
      apiInstance.companyNotificationList();
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyNotificationList");
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

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="companyNotificationRegister"></a>
# **companyNotificationRegister**
> CompanyNotificationRegister200Response companyNotificationRegister(id, callbackUrl)

Creates a new notification

Register a new callback URL to get notifications about companies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | Company Hex ID
    String callbackUrl = "callbackUrl_example"; // String | Callback URL
    try {
      CompanyNotificationRegister200Response result = apiInstance.companyNotificationRegister(id, callbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyNotificationRegister");
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
| **id** | **String**| Company Hex ID | |
| **callbackUrl** | **String**| Callback URL | |

### Return type

[**CompanyNotificationRegister200Response**](CompanyNotificationRegister200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful webhook registration response |  -  |
| **0** |  |  -  |

<a id="companyNotificationUnregister"></a>
# **companyNotificationUnregister**
> companyNotificationUnregister(id)

Unregister a company from Monitoring

Deactivate a previously registered company monitor identified by the notifier id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String id = "id_example"; // String | Registration id of monitoring request record
    try {
      apiInstance.companyNotificationUnregister(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companyNotificationUnregister");
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
| **id** | **String**| Registration id of monitoring request record | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty response body |  -  |
| **0** |  |  -  |

<a id="companySearchName"></a>
# **companySearchName**
> List&lt;CompanySearchName200ResponseInner&gt; companySearchName(country, name, limit)

Retrieves a list of companies from the KYC API company index

KYC API company index lookup for companies with a certain name in a country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String name = "name_example"; // String | company name
    Long limit = 56L; // Long | number of search results
    try {
      List<CompanySearchName200ResponseInner> result = apiInstance.companySearchName(country, name, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companySearchName");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **name** | **String**| company name | |
| **limit** | **Long**| number of search results | [optional] |

### Return type

[**List&lt;CompanySearchName200ResponseInner&gt;**](CompanySearchName200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of companies |  -  |
| **0** |  |  -  |

<a id="companySearchNumber"></a>
# **companySearchNumber**
> companySearchNumber(country, number, limit)

Retrieves a list of companies from the KYC API company index

KYC API company index lookup for companies with a certain register number in a country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1CompanyApi apiInstance = new V1CompanyApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String number = "number_example"; // String | company registration number
    Long limit = 56L; // Long | number of search results
    try {
      apiInstance.companySearchNumber(country, number, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1CompanyApi#companySearchNumber");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **number** | **String**| company registration number | |
| **limit** | **Long**| number of search results | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

