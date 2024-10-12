# DomainsApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainsTldZoneIdDownloadGet**](DomainsApi.md#domainsTldZoneIdDownloadGet) | **GET** /domains/tld/{zone_id}/download | Download Whole Dataset for TLD |
| [**domainsTldZoneIdSearchGet**](DomainsApi.md#domainsTldZoneIdSearchGet) | **GET** /domains/tld/{zone_id}/search | Domains Search for TLD |
| [**domainsUpdatesAddedDownloadGet**](DomainsApi.md#domainsUpdatesAddedDownloadGet) | **GET** /domains/updates/added/download | Download added domains, latest if date not specified |
| [**domainsUpdatesAddedGet**](DomainsApi.md#domainsUpdatesAddedGet) | **GET** /domains/updates/added | Get added domains, latest if date not specified |
| [**domainsUpdatesDeletedDownloadGet**](DomainsApi.md#domainsUpdatesDeletedDownloadGet) | **GET** /domains/updates/deleted/download | Download deleted domains, latest if date not specified |
| [**domainsUpdatesDeletedGet**](DomainsApi.md#domainsUpdatesDeletedGet) | **GET** /domains/updates/deleted | Get deleted domains, latest if date not specified |
| [**domainsUpdatesListGet**](DomainsApi.md#domainsUpdatesListGet) | **GET** /domains/updates/list | List of updates |
| [**getSearchDomainItem**](DomainsApi.md#getSearchDomainItem) | **GET** /domains/search | Domains Database Search |
| [**getTldDomainItem**](DomainsApi.md#getTldDomainItem) | **GET** /domains/tld/{zone_id} | Get TLD records |


<a id="domainsTldZoneIdDownloadGet"></a>
# **domainsTldZoneIdDownloadGet**
> domainsTldZoneIdDownloadGet(zoneId, apiKey, date)

Download Whole Dataset for TLD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    try {
      apiInstance.domainsTldZoneIdDownloadGet(zoneId, apiKey, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsTldZoneIdDownloadGet");
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
| **zoneId** | **String**|  | |
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |

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
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="domainsTldZoneIdSearchGet"></a>
# **domainsTldZoneIdSearchGet**
> SearchResults domainsTldZoneIdSearchGet(zoneId, apiKey, date, page, limit, domain, country, isDead, A, NS, CNAME, MX, TXT)

Domains Search for TLD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    String domain = "domain_example"; // String | Domain includes
    String country = "country_example"; // String | Hosting Country
    Boolean isDead = true; // Boolean | Dead or Not, default not
    String A = "A_example"; // String | A record includes
    String NS = "NS_example"; // String | NS record includes
    String CNAME = "CNAME_example"; // String | CNAME record includes
    String MX = "MX_example"; // String | MX record includes
    String TXT = "TXT_example"; // String | TXT record includes
    try {
      SearchResults result = apiInstance.domainsTldZoneIdSearchGet(zoneId, apiKey, date, page, limit, domain, country, isDead, A, NS, CNAME, MX, TXT);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsTldZoneIdSearchGet");
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
| **zoneId** | **String**|  | |
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |
| **domain** | **String**| Domain includes | [optional] |
| **country** | **String**| Hosting Country | [optional] |
| **isDead** | **Boolean**| Dead or Not, default not | [optional] |
| **A** | **String**| A record includes | [optional] |
| **NS** | **String**| NS record includes | [optional] |
| **CNAME** | **String**| CNAME record includes | [optional] |
| **MX** | **String**| MX record includes | [optional] |
| **TXT** | **String**| TXT record includes | [optional] |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="domainsUpdatesAddedDownloadGet"></a>
# **domainsUpdatesAddedDownloadGet**
> domainsUpdatesAddedDownloadGet(apiKey, date)

Download added domains, latest if date not specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    try {
      apiInstance.domainsUpdatesAddedDownloadGet(apiKey, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdatesAddedDownloadGet");
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
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |

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
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="domainsUpdatesAddedGet"></a>
# **domainsUpdatesAddedGet**
> SearchResults domainsUpdatesAddedGet(apiKey, date, page, limit)

Get added domains, latest if date not specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    try {
      SearchResults result = apiInstance.domainsUpdatesAddedGet(apiKey, date, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdatesAddedGet");
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
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="domainsUpdatesDeletedDownloadGet"></a>
# **domainsUpdatesDeletedDownloadGet**
> domainsUpdatesDeletedDownloadGet(apiKey, date)

Download deleted domains, latest if date not specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    try {
      apiInstance.domainsUpdatesDeletedDownloadGet(apiKey, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdatesDeletedDownloadGet");
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
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |

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
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="domainsUpdatesDeletedGet"></a>
# **domainsUpdatesDeletedGet**
> SearchResults domainsUpdatesDeletedGet(apiKey, date, page, limit)

Get deleted domains, latest if date not specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    try {
      SearchResults result = apiInstance.domainsUpdatesDeletedGet(apiKey, date, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdatesDeletedGet");
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
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="domainsUpdatesListGet"></a>
# **domainsUpdatesListGet**
> UpdateModel domainsUpdatesListGet(apiKey)

List of updates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    try {
      UpdateModel result = apiInstance.domainsUpdatesListGet(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdatesListGet");
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
| **apiKey** | **String**| API key | [optional] |

### Return type

[**UpdateModel**](UpdateModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

<a id="getSearchDomainItem"></a>
# **getSearchDomainItem**
> SearchResults getSearchDomainItem(apiKey, date, page, limit, domain, zone, country, isDead, A, NS, CNAME, MX, TXT)

Domains Database Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    String domain = "domain_example"; // String | Domain includes
    String zone = "zone_example"; // String | In Zone
    String country = "country_example"; // String | Hosting Country
    Boolean isDead = true; // Boolean | Dead or Not, default not
    String A = "A_example"; // String | A record includes
    String NS = "NS_example"; // String | NS record includes
    String CNAME = "CNAME_example"; // String | CNAME record includes
    String MX = "MX_example"; // String | MX record includes
    String TXT = "TXT_example"; // String | TXT record includes
    try {
      SearchResults result = apiInstance.getSearchDomainItem(apiKey, date, page, limit, domain, zone, country, isDead, A, NS, CNAME, MX, TXT);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getSearchDomainItem");
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
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |
| **domain** | **String**| Domain includes | [optional] |
| **zone** | **String**| In Zone | [optional] |
| **country** | **String**| Hosting Country | [optional] |
| **isDead** | **Boolean**| Dead or Not, default not | [optional] |
| **A** | **String**| A record includes | [optional] |
| **NS** | **String**| NS record includes | [optional] |
| **CNAME** | **String**| CNAME record includes | [optional] |
| **MX** | **String**| MX record includes | [optional] |
| **TXT** | **String**| TXT record includes | [optional] |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | api_key is not valid |  -  |
| **404** | Results not found |  -  |

<a id="getTldDomainItem"></a>
# **getTldDomainItem**
> SearchResults getTldDomainItem(zoneId, apiKey, date, page, limit, domain, country, isDead, A, NS, CNAME, MX, TXT)

Get TLD records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String zoneId = "zoneId_example"; // String | 
    String apiKey = "apiKey_example"; // String | API key
    String date = "date_example"; // String | Request date
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    String domain = "domain_example"; // String | Domain includes
    String country = "country_example"; // String | Hosting Country
    Boolean isDead = true; // Boolean | Dead or Not, default not
    String A = "A_example"; // String | A record includes
    String NS = "NS_example"; // String | NS record includes
    String CNAME = "CNAME_example"; // String | CNAME record includes
    String MX = "MX_example"; // String | MX record includes
    String TXT = "TXT_example"; // String | TXT record includes
    try {
      SearchResults result = apiInstance.getTldDomainItem(zoneId, apiKey, date, page, limit, domain, country, isDead, A, NS, CNAME, MX, TXT);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getTldDomainItem");
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
| **zoneId** | **String**|  | |
| **apiKey** | **String**| API key | [optional] |
| **date** | **String**| Request date | [optional] |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |
| **domain** | **String**| Domain includes | [optional] |
| **country** | **String**| Hosting Country | [optional] |
| **isDead** | **Boolean**| Dead or Not, default not | [optional] |
| **A** | **String**| A record includes | [optional] |
| **NS** | **String**| NS record includes | [optional] |
| **CNAME** | **String**| CNAME record includes | [optional] |
| **MX** | **String**| MX record includes | [optional] |
| **TXT** | **String**| TXT record includes | [optional] |

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | No api_key or it&#39;s not valid |  -  |
| **404** | Results not found |  -  |

