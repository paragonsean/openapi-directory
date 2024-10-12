# ChargesApi

All URIs are relative to *https://api.idtbeyond.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iatuChargesReportsAllCsvGet**](ChargesApi.md#iatuChargesReportsAllCsvGet) | **GET** /iatu/charges/reports/all.csv | List of account charges in CSV |
| [**iatuChargesReportsAllGet**](ChargesApi.md#iatuChargesReportsAllGet) | **GET** /iatu/charges/reports/all | List of account charges in JSON |


<a id="iatuChargesReportsAllCsvGet"></a>
# **iatuChargesReportsAllCsvGet**
> iatuChargesReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account charges in CSV

Returns charges by date range in CSV.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    ChargesApi apiInstance = new ChargesApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String dateFrom = "2016-01-28"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    String dateTo = "2016-01-28"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    try {
      apiInstance.iatuChargesReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargesApi#iatuChargesReportsAllCsvGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |
| **dateFrom** | **String**| The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to 2016-01-28] |
| **dateTo** | **String**| The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to 2016-01-28] |

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
| **200** | Successful charges CSV response |  -  |

<a id="iatuChargesReportsAllGet"></a>
# **iatuChargesReportsAllGet**
> iatuChargesReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account charges in JSON

Returns charges by date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    ChargesApi apiInstance = new ChargesApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String dateFrom = "2016-01-28"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    String dateTo = "2016-01-28"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    try {
      apiInstance.iatuChargesReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargesApi#iatuChargesReportsAllGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |
| **dateFrom** | **String**| The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to 2016-01-28] |
| **dateTo** | **String**| The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39; | [default to 2016-01-28] |

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
| **200** | Successful charges JSON response |  -  |

