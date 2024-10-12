# CountryApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDailyReportAllCountries**](CountryApi.md#getDailyReportAllCountries) | **GET** /report/country/all | getDailyReportAllCountries |
| [**getDailyReportByCountryCode**](CountryApi.md#getDailyReportByCountryCode) | **GET** /report/country/code | getDailyReportByCountryCode |
| [**getDailyReportByCountryName**](CountryApi.md#getDailyReportByCountryName) | **GET** /report/country/name | getDailyReportByCountryName |
| [**getLatestAllCountries**](CountryApi.md#getLatestAllCountries) | **GET** /country/all | getLatestAllCountries |
| [**getLatestCountryDataByCode**](CountryApi.md#getLatestCountryDataByCode) | **GET** /country/code | getLatestCountryDataByCode |
| [**getLatestCountryDataByName**](CountryApi.md#getLatestCountryDataByName) | **GET** /country | getLatestCountryDataByName |


<a id="getDailyReportAllCountries"></a>
# **getDailyReportAllCountries**
> List&lt;GetDailyReportAllCountries200ResponseInner&gt; getDailyReportAllCountries(date, dateFormat, format)

getDailyReportAllCountries

Get daily report for all countries. Date is mandatory parametar. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String date = "date_example"; // String | Date of the report.
    String dateFormat = "YYYY-MM-DD"; // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    String format = "json"; // String | Format of the response
    try {
      List<GetDailyReportAllCountries200ResponseInner> result = apiInstance.getDailyReportAllCountries(date, dateFormat, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getDailyReportAllCountries");
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
| **date** | **String**| Date of the report. | |
| **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to YYYY-MM-DD] [enum: YYYY-MM-DD, YYYY-DD-MM, DD-MM-YYYY, MM-DD-YYYY] |
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetDailyReportAllCountries200ResponseInner&gt;**](GetDailyReportAllCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily report for COVID-19 for selected country. |  -  |

<a id="getDailyReportByCountryCode"></a>
# **getDailyReportByCountryCode**
> List&lt;GetDailyReportAllCountries200ResponseInner&gt; getDailyReportByCountryCode(code, date, dateFormat, format)

getDailyReportByCountryCode

Get daily report for specific country. Country code and date are mandatory in parametars. Country code is in ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String code = "code_example"; // String | Country code. Country code is by ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type.
    String date = "date_example"; // String | Date of the report.
    String dateFormat = "YYYY-MM-DD"; // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    String format = "json"; // String | Format of the response
    try {
      List<GetDailyReportAllCountries200ResponseInner> result = apiInstance.getDailyReportByCountryCode(code, date, dateFormat, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getDailyReportByCountryCode");
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
| **code** | **String**| Country code. Country code is by ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type. | |
| **date** | **String**| Date of the report. | |
| **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to YYYY-MM-DD] [enum: YYYY-MM-DD, YYYY-DD-MM, DD-MM-YYYY, MM-DD-YYYY] |
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetDailyReportAllCountries200ResponseInner&gt;**](GetDailyReportAllCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily report for COVID-19 for selected country. |  -  |

<a id="getDailyReportByCountryName"></a>
# **getDailyReportByCountryName**
> List&lt;GetDailyReportAllCountries200ResponseInner&gt; getDailyReportByCountryName(name, date, dateFormat, format)

getDailyReportByCountryName

Get daily report for specific country. Country name and date are mandatory in parametars. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String name = "name_example"; // String | Country name.
    String date = "date_example"; // String | Date of the report.
    String dateFormat = "YYYY-MM-DD"; // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    String format = "json"; // String | Format of the response
    try {
      List<GetDailyReportAllCountries200ResponseInner> result = apiInstance.getDailyReportByCountryName(name, date, dateFormat, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getDailyReportByCountryName");
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
| **name** | **String**| Country name. | |
| **date** | **String**| Date of the report. | |
| **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to YYYY-MM-DD] [enum: YYYY-MM-DD, YYYY-DD-MM, DD-MM-YYYY, MM-DD-YYYY] |
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetDailyReportAllCountries200ResponseInner&gt;**](GetDailyReportAllCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily report for COVID-19 for selected country. |  -  |

<a id="getLatestAllCountries"></a>
# **getLatestAllCountries**
> List&lt;GetLatestCountryDataByName200ResponseInner&gt; getLatestAllCountries(format)

getLatestAllCountries

Get latest data from all countries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String format = "json"; // String | Format of the response
    try {
      List<GetLatestCountryDataByName200ResponseInner> result = apiInstance.getLatestAllCountries(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getLatestAllCountries");
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
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetLatestCountryDataByName200ResponseInner&gt;**](GetLatestCountryDataByName200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all countries with latest data about COVID-19 |  -  |

<a id="getLatestCountryDataByCode"></a>
# **getLatestCountryDataByCode**
> List&lt;GetLatestCountryDataByName200ResponseInner&gt; getLatestCountryDataByCode(code, format)

getLatestCountryDataByCode

Get latest data for specific country. Country code and format are in parametars. Country code is in ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String code = "code_example"; // String | Country code
    String format = "json"; // String | Format of the response
    try {
      List<GetLatestCountryDataByName200ResponseInner> result = apiInstance.getLatestCountryDataByCode(code, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getLatestCountryDataByCode");
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
| **code** | **String**| Country code | |
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetLatestCountryDataByName200ResponseInner&gt;**](GetLatestCountryDataByName200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Latest data about COVID-19 for selected country |  -  |

<a id="getLatestCountryDataByName"></a>
# **getLatestCountryDataByName**
> List&lt;GetLatestCountryDataByName200ResponseInner&gt; getLatestCountryDataByName(name, format)

getLatestCountryDataByName

Get latest data for specific country. Country name and format are in parametars.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CountryApi apiInstance = new CountryApi(defaultClient);
    String name = "name_example"; // String | Name of the country
    String format = "json"; // String | Format of the response
    try {
      List<GetLatestCountryDataByName200ResponseInner> result = apiInstance.getLatestCountryDataByName(name, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryApi#getLatestCountryDataByName");
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
| **name** | **String**| Name of the country | |
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetLatestCountryDataByName200ResponseInner&gt;**](GetLatestCountryDataByName200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Latest data about COVID-19 for selected country |  -  |

