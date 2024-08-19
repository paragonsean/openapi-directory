# TopupsApi

All URIs are relative to *https://api.idtbeyond.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iatuTopupsPost**](TopupsApi.md#iatuTopupsPost) | **POST** /iatu/topups | Topup a mobile phone |
| [**iatuTopupsReportsAllCsvGet**](TopupsApi.md#iatuTopupsReportsAllCsvGet) | **GET** /iatu/topups/reports/all.csv | List of account topups in CSV |
| [**iatuTopupsReportsAllGet**](TopupsApi.md#iatuTopupsReportsAllGet) | **GET** /iatu/topups/reports/all | List of account topups in JSON |
| [**iatuTopupsReportsPost**](TopupsApi.md#iatuTopupsReportsPost) | **POST** /iatu/topups/reports | Search topups transactions |
| [**iatuTopupsReportsTotalsGet**](TopupsApi.md#iatuTopupsReportsTotalsGet) | **GET** /iatu/topups/reports/totals | Summary of account topups in JSON |
| [**iatuTopupsReversePost**](TopupsApi.md#iatuTopupsReversePost) | **POST** /iatu/topups/reverse | Reversal of a Topup |


<a id="iatuTopupsPost"></a>
# **iatuTopupsPost**
> iatuTopupsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body)

Topup a mobile phone

Submits an IATU transaction request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    TopupsApi apiInstance = new TopupsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    Topups body = new Topups(); // Topups | Topups details
    try {
      apiInstance.iatuTopupsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopupsApi#iatuTopupsPost");
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
| **body** | [**Topups**](Topups.md)| Topups details | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The transaction has been completed successfully. |  -  |
| **202** | The transaction has been received, but the final status is unknown. Please query by the client_transaction_id to get the current status of the transaction. |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | X not found |  -  |
| **405** | Validation exception |  -  |
| **500** | There is an error in your transaction. Please check the error code contained in the result for more information. |  -  |

<a id="iatuTopupsReportsAllCsvGet"></a>
# **iatuTopupsReportsAllCsvGet**
> iatuTopupsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account topups in CSV

Returns topups by date range in CSV.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    TopupsApi apiInstance = new TopupsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String dateFrom = "2016-01-28"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    String dateTo = "2016-01-28"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    try {
      apiInstance.iatuTopupsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopupsApi#iatuTopupsReportsAllCsvGet");
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
| **200** | Successful topups CSV response |  -  |

<a id="iatuTopupsReportsAllGet"></a>
# **iatuTopupsReportsAllGet**
> iatuTopupsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

List of account topups in JSON

Returns topups by date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    TopupsApi apiInstance = new TopupsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String dateFrom = "2016-01-28"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    String dateTo = "2016-01-28"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    try {
      apiInstance.iatuTopupsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopupsApi#iatuTopupsReportsAllGet");
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
| **200** | Successful topups JSON response |  -  |

<a id="iatuTopupsReportsPost"></a>
# **iatuTopupsReportsPost**
> iatuTopupsReportsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body)

Search topups transactions

Search topups transactions, by date, with client_transaction_id or to_service_number. Use &#39;client_transaction_id&#39; to search by transaction number, or &#39;to_service_number&#39; to get transaction status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    TopupsApi apiInstance = new TopupsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    TopupsReports body = new TopupsReports(); // TopupsReports | Topups reports request details
    try {
      apiInstance.iatuTopupsReportsPost(xIdtBeyondAppId, xIdtBeyondAppKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopupsApi#iatuTopupsReportsPost");
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
| **body** | [**TopupsReports**](TopupsReports.md)| Topups reports request details | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful topups JSON response |  -  |

<a id="iatuTopupsReportsTotalsGet"></a>
# **iatuTopupsReportsTotalsGet**
> iatuTopupsReportsTotalsGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo)

Summary of account topups in JSON

Returns topups totals by date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    TopupsApi apiInstance = new TopupsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String dateFrom = "2016-01-28"; // String | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    String dateTo = "2016-01-28"; // String | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). '2016-01-28'
    try {
      apiInstance.iatuTopupsReportsTotalsGet(xIdtBeyondAppId, xIdtBeyondAppKey, dateFrom, dateTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopupsApi#iatuTopupsReportsTotalsGet");
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
| **200** | Successful topups JSON response |  -  |

<a id="iatuTopupsReversePost"></a>
# **iatuTopupsReversePost**
> iatuTopupsReversePost(xIdtBeyondAppId, xIdtBeyondAppKey, body)

Reversal of a Topup

Occasionally, a carrier will not be able to successfully complete a topup request. In this case, we will attempt to automatically reverse the transaction for you, and return the money into your account. In the case when this is not possible, you may need to request a reverse on the transaction that has a status of &#39;transaction_status&#39; &#39;notredeemed&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    TopupsApi apiInstance = new TopupsApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    TopupsReversal body = new TopupsReversal(); // TopupsReversal | Topups details
    try {
      apiInstance.iatuTopupsReversePost(xIdtBeyondAppId, xIdtBeyondAppKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopupsApi#iatuTopupsReversePost");
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
| **body** | [**TopupsReversal**](TopupsReversal.md)| Topups details | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful charges JSON response |  -  |

