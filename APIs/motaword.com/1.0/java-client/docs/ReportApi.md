# ReportApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateQAReport**](ReportApi.md#generateQAReport) | **POST** /reports/qa | Generate a QA report for given filter |
| [**getFilterContents**](ReportApi.md#getFilterContents) | **POST** /reports/filter | Returns available options for selected timeframe. |
| [**getLanguagePairsReport**](ReportApi.md#getLanguagePairsReport) | **POST** /reports/language-pairs | Language pairs report |
| [**getProjectsReport**](ReportApi.md#getProjectsReport) | **POST** /reports/projects | Projects report |
| [**getUsersReport**](ReportApi.md#getUsersReport) | **POST** /reports/users | Company users report |


<a id="generateQAReport"></a>
# **generateQAReport**
> QaWarnings generateQAReport(qaFilter)

Generate a QA report for given filter

Generate a QA report for given filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReportApi apiInstance = new ReportApi(defaultClient);
    QaFilter qaFilter = new QaFilter(); // QaFilter | 
    try {
      QaWarnings result = apiInstance.generateQAReport(qaFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#generateQAReport");
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
| **qaFilter** | [**QaFilter**](QaFilter.md)|  | [optional] |

### Return type

[**QaWarnings**](QaWarnings.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of QA entries |  -  |
| **400** | MissingParameter |  -  |

<a id="getFilterContents"></a>
# **getFilterContents**
> FilterContents getFilterContents(filterDates)

Returns available options for selected timeframe.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReportApi apiInstance = new ReportApi(defaultClient);
    FilterDates filterDates = new FilterDates(); // FilterDates | 
    try {
      FilterContents result = apiInstance.getFilterContents(filterDates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#getFilterContents");
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
| **filterDates** | [**FilterDates**](FilterDates.md)|  | [optional] |

### Return type

[**FilterContents**](FilterContents.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Filter contents |  -  |
| **404** | UserNotFound |  -  |

<a id="getLanguagePairsReport"></a>
# **getLanguagePairsReport**
> LanguagePairsReport getLanguagePairsReport(reportFilter)

Language pairs report

View translation reports for each language pair with translations under your account. You can view company-wide language pairs if you have the user permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReportApi apiInstance = new ReportApi(defaultClient);
    ReportFilter reportFilter = new ReportFilter(); // ReportFilter | 
    try {
      LanguagePairsReport result = apiInstance.getLanguagePairsReport(reportFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#getLanguagePairsReport");
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
| **reportFilter** | [**ReportFilter**](ReportFilter.md)|  | [optional] |

### Return type

[**LanguagePairsReport**](LanguagePairsReport.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Language pairs stats for client and vendors |  -  |
| **404** | UserNotFound |  -  |

<a id="getProjectsReport"></a>
# **getProjectsReport**
> ProjectList getProjectsReport(reportFilter)

Projects report

View projects under your account, with advanced filtering. You can view company-wide projects if you have the user permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReportApi apiInstance = new ReportApi(defaultClient);
    ReportFilter reportFilter = new ReportFilter(); // ReportFilter | 
    try {
      ProjectList result = apiInstance.getProjectsReport(reportFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#getProjectsReport");
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
| **reportFilter** | [**ReportFilter**](ReportFilter.md)|  | [optional] |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User stats for client and vendors |  -  |
| **404** | UserNotFound |  -  |

<a id="getUsersReport"></a>
# **getUsersReport**
> UsersReport getUsersReport(reportFilter)

Company users report

View translation reports for each user under your company account. You need the permission to view users in your company.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReportApi apiInstance = new ReportApi(defaultClient);
    ReportFilter reportFilter = new ReportFilter(); // ReportFilter | 
    try {
      UsersReport result = apiInstance.getUsersReport(reportFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#getUsersReport");
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
| **reportFilter** | [**ReportFilter**](ReportFilter.md)|  | [optional] |

### Return type

[**UsersReport**](UsersReport.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User stats for client and vendors |  -  |
| **404** | UserNotFound |  -  |

