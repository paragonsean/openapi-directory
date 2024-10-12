# ReportsApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteReportDefinition**](ReportsApi.md#deleteReportDefinition) | **DELETE** /Report/{ReportDefinitionId} | Deletes a report definition |
| [**deleteTransformDefinition**](ReportsApi.md#deleteTransformDefinition) | **DELETE** /Transform/{TransformDefinitionId} | Deletes a transform definition |
| [**getActivePayInstructionsReportOutput**](ReportsApi.md#getActivePayInstructionsReportOutput) | **GET** /Report/ACTPAYINS/run | Runs the active pay instructions report |
| [**getAoeLiabilityReportOuput**](ReportsApi.md#getAoeLiabilityReportOuput) | **GET** /Report/AOELIABILITY/run | Runs the AOE liability report |
| [**getDpsMessageReportOutput**](ReportsApi.md#getDpsMessageReportOutput) | **GET** /Report/DPSMSG/run | Runs the DPS message report |
| [**getEmployerSummaryReportOuput**](ReportsApi.md#getEmployerSummaryReportOuput) | **GET** /Report/EMPSUM/run | Runs the employer summary report |
| [**getGrossToNetReportOutput**](ReportsApi.md#getGrossToNetReportOutput) | **GET** /Report/GRO2NET/run | Runs the gross to net report |
| [**getHolidayBalanceReportOutput**](ReportsApi.md#getHolidayBalanceReportOutput) | **GET** /Report/HOLBAL/run | Runs the holiday balance report |
| [**getJournalReportOuput**](ReportsApi.md#getJournalReportOuput) | **GET** /Report/JOURNAL/run | Runs the journal report |
| [**getLastPayDateReportOuput**](ReportsApi.md#getLastPayDateReportOuput) | **GET** /Report/LASTPAYDATE/run | Runs the last pay date report |
| [**getNetPayReportOutput**](ReportsApi.md#getNetPayReportOutput) | **GET** /Report/NETPAY/run | Runs the net pay report |
| [**getNextPayPeriodDatesReportOutput**](ReportsApi.md#getNextPayPeriodDatesReportOutput) | **GET** /Report/NEXTPERIOD/run | Runs the next pay period report |
| [**getP11SummaryReportOutput**](ReportsApi.md#getP11SummaryReportOutput) | **GET** /Report/P11SUM/run | Runs the P11 summary report |
| [**getP32NetReportOutput**](ReportsApi.md#getP32NetReportOutput) | **GET** /Report/P32/run | Runs the P32 report |
| [**getP32SummaryNetReportOutput**](ReportsApi.md#getP32SummaryNetReportOutput) | **GET** /Report/P32SUM/run | Runs the P32 summary report |
| [**getP45ReportOutput**](ReportsApi.md#getP45ReportOutput) | **GET** /Report/P45/run | Runs the P45 report |
| [**getP60ReportOutput**](ReportsApi.md#getP60ReportOutput) | **GET** /Report/P60/run | Runs the P60 report |
| [**getPapdisReportOuput**](ReportsApi.md#getPapdisReportOuput) | **GET** /Report/PAPDIS/run | Runs the PAPDIS report |
| [**getPassReportOuput**](ReportsApi.md#getPassReportOuput) | **GET** /Report/PASS/run | Runs the PASS report |
| [**getPayDashboardPayslipReportOuput**](ReportsApi.md#getPayDashboardPayslipReportOuput) | **GET** /Report/PAYDASHBOARD/run | Runs the Pay Dashboard payslips report |
| [**getPayslip3ReportOutput**](ReportsApi.md#getPayslip3ReportOutput) | **GET** /Report/PAYSLIP3/run | Runs the verbose payslip report |
| [**getPensionLiabilityReportOutput**](ReportsApi.md#getPensionLiabilityReportOutput) | **GET** /Report/PENLIABILITY/run | Runs the pension liability report |
| [**getReportDefinitionFromApplication**](ReportsApi.md#getReportDefinitionFromApplication) | **GET** /Report/{ReportDefinitionId} | Get the report definition |
| [**getReportDefinitionsFromApplication**](ReportsApi.md#getReportDefinitionsFromApplication) | **GET** /Reports | Gets all reports |
| [**getReportOutput**](ReportsApi.md#getReportOutput) | **GET** /Report/{ReportDefinitionId}/run | Runs the specified report definition |
| [**getTransformDefinitionFromApplication**](ReportsApi.md#getTransformDefinitionFromApplication) | **GET** /Transform/{TransformDefinitionId} | Get the transform definition |
| [**getTransformDefinitionsFromApplication**](ReportsApi.md#getTransformDefinitionsFromApplication) | **GET** /Transforms | Gets all transform definitions |
| [**postReportDefinition**](ReportsApi.md#postReportDefinition) | **POST** /Reports | Create a new report definition |
| [**postTransformDefinition**](ReportsApi.md#postTransformDefinition) | **POST** /Transforms | Create a new transform definition |
| [**putReportDefinition**](ReportsApi.md#putReportDefinition) | **PUT** /Report/{ReportDefinitionId} | Updates a report definition |
| [**putTransformDefinition**](ReportsApi.md#putTransformDefinition) | **PUT** /Transform/{TransformDefinitionId} | Updates a transform definition |


<a id="deleteReportDefinition"></a>
# **deleteReportDefinition**
> deleteReportDefinition(reportDefinitionId, authorization, apiVersion)

Deletes a report definition

Delete the specified report definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteReportDefinition(reportDefinitionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#deleteReportDefinition");
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
| **reportDefinitionId** | **String**| The report definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="deleteTransformDefinition"></a>
# **deleteTransformDefinition**
> deleteTransformDefinition(transformDefinitionId, authorization, apiVersion)

Deletes a transform definition

Delete the specified transform definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String transformDefinitionId = "transformDefinitionId_example"; // String | The transform definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteTransformDefinition(transformDefinitionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#deleteTransformDefinition");
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
| **transformDefinitionId** | **String**| The transform definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getActivePayInstructionsReportOutput"></a>
# **getActivePayInstructionsReportOutput**
> File getActivePayInstructionsReportOutput(employerKey, employeeKey, fromDate, authorization, apiVersion, activeOn, toDate, type)

Runs the active pay instructions report

Returns the result of the executed active pay instructions report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String employeeKey = "employeeKey_example"; // String | The employee unique key. E.g. EE001
    LocalDate fromDate = LocalDate.now(); // LocalDate | The lower filter date. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    LocalDate activeOn = LocalDate.now(); // LocalDate | The active date to consider. E.g 2017-04-05
    LocalDate toDate = LocalDate.now(); // LocalDate | The upper filter date. E.g 2017-04-05
    String type = "type_example"; // String | the data type to filter on. E.g. TaxPayInstruction
    try {
      File result = apiInstance.getActivePayInstructionsReportOutput(employerKey, employeeKey, fromDate, authorization, apiVersion, activeOn, toDate, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getActivePayInstructionsReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **employeeKey** | **String**| The employee unique key. E.g. EE001 | |
| **fromDate** | **LocalDate**| The lower filter date. E.g 2016-04-06 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **activeOn** | **LocalDate**| The active date to consider. E.g 2017-04-05 | [optional] |
| **toDate** | **LocalDate**| The upper filter date. E.g 2017-04-05 | [optional] |
| **type** | **String**| the data type to filter on. E.g. TaxPayInstruction | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the active pay instructions report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAoeLiabilityReportOuput"></a>
# **getAoeLiabilityReportOuput**
> File getAoeLiabilityReportOuput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, taxPeriod, transformDefinitionKey)

Runs the AOE liability report

Returns the result of the executed AOE liability report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    Integer taxPeriod = 56; // Integer | The tax period number.
    String transformDefinitionKey = "transformDefinitionKey_example"; // String | The transform definition unique key. E.g. P45-Pdf
    try {
      File result = apiInstance.getAoeLiabilityReportOuput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, taxPeriod, transformDefinitionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getAoeLiabilityReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **taxPeriod** | **Integer**| The tax period number. | [optional] |
| **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the AOE liability report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getDpsMessageReportOutput"></a>
# **getDpsMessageReportOutput**
> File getDpsMessageReportOutput(employerKey, fromDate, authorization, apiVersion, toDate, messageTypes, messageStatuses, startIndex, maxIndex)

Runs the DPS message report

Returns the result of the executed DPS message report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    LocalDate fromDate = LocalDate.now(); // LocalDate | The lower filter date. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    LocalDate toDate = LocalDate.now(); // LocalDate | The upper filter date. E.g 2017-04-05
    String messageTypes = "messageTypes_example"; // String | The DPS message types as a CSV list. E.g. P6,P9,SL1,SL2
    String messageStatuses = "messageStatuses_example"; // String | The DPS message status as a CSV list. E.g. Retrieved,Processed,Blocked,Ignored
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    try {
      File result = apiInstance.getDpsMessageReportOutput(employerKey, fromDate, authorization, apiVersion, toDate, messageTypes, messageStatuses, startIndex, maxIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getDpsMessageReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **fromDate** | **LocalDate**| The lower filter date. E.g 2016-04-06 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **toDate** | **LocalDate**| The upper filter date. E.g 2017-04-05 | [optional] |
| **messageTypes** | **String**| The DPS message types as a CSV list. E.g. P6,P9,SL1,SL2 | [optional] |
| **messageStatuses** | **String**| The DPS message status as a CSV list. E.g. Retrieved,Processed,Blocked,Ignored | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the DPS message report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getEmployerSummaryReportOuput"></a>
# **getEmployerSummaryReportOuput**
> File getEmployerSummaryReportOuput(employerKey, contextDate, authorization, apiVersion)

Runs the employer summary report

Returns the result of the employer summary report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    LocalDate contextDate = LocalDate.now(); // LocalDate | The date context for the report. E.g. 2018-04-30
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getEmployerSummaryReportOuput(employerKey, contextDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getEmployerSummaryReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **contextDate** | **LocalDate**| The date context for the report. E.g. 2018-04-30 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the employer summary report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getGrossToNetReportOutput"></a>
# **getGrossToNetReportOutput**
> File getGrossToNetReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, taxPeriod, startIndex, maxIndex)

Runs the gross to net report

Returns the result of the executed gross to net report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    Integer taxPeriod = 56; // Integer | The tax period number.
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    try {
      File result = apiInstance.getGrossToNetReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, taxPeriod, startIndex, maxIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getGrossToNetReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **taxPeriod** | **Integer**| The tax period number. | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the gross to net report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getHolidayBalanceReportOutput"></a>
# **getHolidayBalanceReportOutput**
> File getHolidayBalanceReportOutput(employerKey, holidayYearEnd, authorization, apiVersion, employeeCodes, startIndex, maxIndex)

Runs the holiday balance report

Returns the result of the executed holiday balance report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    LocalDate holidayYearEnd = LocalDate.now(); // LocalDate | The holiday year end for the report. E.g. 2018-12-31
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    String employeeCodes = "employeeCodes_example"; // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    try {
      File result = apiInstance.getHolidayBalanceReportOutput(employerKey, holidayYearEnd, authorization, apiVersion, employeeCodes, startIndex, maxIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getHolidayBalanceReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **holidayYearEnd** | **LocalDate**| The holiday year end for the report. E.g. 2018-12-31 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the holiday balance report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getJournalReportOuput"></a>
# **getJournalReportOuput**
> File getJournalReportOuput(employerKey, payFrequency, taxYear, ledgerTarget, authorization, apiVersion, taxPeriod)

Runs the journal report

Returns the result of the journal report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payFrequency = "payFrequency_example"; // String | The pay frequency option. E.g. Monthly
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String ledgerTarget = "ledgerTarget_example"; // String | Specific to JOURNAL report, a filter used to select the journal lines for the specified ledger target. E.g. [Default]
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    Integer taxPeriod = 56; // Integer | The tax period number.
    try {
      File result = apiInstance.getJournalReportOuput(employerKey, payFrequency, taxYear, ledgerTarget, authorization, apiVersion, taxPeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getJournalReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payFrequency** | **String**| The pay frequency option. E.g. Monthly | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **ledgerTarget** | **String**| Specific to JOURNAL report, a filter used to select the journal lines for the specified ledger target. E.g. [Default] | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **taxPeriod** | **Integer**| The tax period number. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the journal report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getLastPayDateReportOuput"></a>
# **getLastPayDateReportOuput**
> File getLastPayDateReportOuput(employerKey, employeeKey, authorization, apiVersion)

Runs the last pay date report

Returns the result of the executed last pay date report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String employeeKey = "employeeKey_example"; // String | The employee unique key. E.g. EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getLastPayDateReportOuput(employerKey, employeeKey, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getLastPayDateReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **employeeKey** | **String**| The employee unique key. E.g. EE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the last pay date report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getNetPayReportOutput"></a>
# **getNetPayReportOutput**
> File getNetPayReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, taxPeriod, startIndex, maxIndex)

Runs the net pay report

Returns the result of the executed net pay report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    Integer taxPeriod = 56; // Integer | The tax period number.
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    try {
      File result = apiInstance.getNetPayReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, taxPeriod, startIndex, maxIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getNetPayReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **taxPeriod** | **Integer**| The tax period number. | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the net pay report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getNextPayPeriodDatesReportOutput"></a>
# **getNextPayPeriodDatesReportOutput**
> File getNextPayPeriodDatesReportOutput(employerKey, payScheduleKey, authorization, apiVersion)

Runs the next pay period report

Returns the result of the executed next pay period report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getNextPayPeriodDatesReportOutput(employerKey, payScheduleKey, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getNextPayPeriodDatesReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the next pay period report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getP11SummaryReportOutput"></a>
# **getP11SummaryReportOutput**
> File getP11SummaryReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, startIndex, maxIndex)

Runs the P11 summary report

Returns the result of the executed P11 summary report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    try {
      File result = apiInstance.getP11SummaryReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, startIndex, maxIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getP11SummaryReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the P11 report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getP32NetReportOutput"></a>
# **getP32NetReportOutput**
> File getP32NetReportOutput(employerKey, taxYear, authorization, apiVersion)

Runs the P32 report

Returns the result of the executed P32 report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getP32NetReportOutput(employerKey, taxYear, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getP32NetReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the P32 report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getP32SummaryNetReportOutput"></a>
# **getP32SummaryNetReportOutput**
> File getP32SummaryNetReportOutput(employerKey, taxYear, authorization, apiVersion)

Runs the P32 summary report

Returns the result of the executed P32 summary report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getP32SummaryNetReportOutput(employerKey, taxYear, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getP32SummaryNetReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the P32 summary report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getP45ReportOutput"></a>
# **getP45ReportOutput**
> File getP45ReportOutput(employerKey, employeeKey, authorization, apiVersion, transformDefinitionKey)

Runs the P45 report

Returns the result of the executed P45 report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String employeeKey = "employeeKey_example"; // String | The employee unique key. E.g. EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    String transformDefinitionKey = "transformDefinitionKey_example"; // String | The transform definition unique key. E.g. P45-Pdf
    try {
      File result = apiInstance.getP45ReportOutput(employerKey, employeeKey, authorization, apiVersion, transformDefinitionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getP45ReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **employeeKey** | **String**| The employee unique key. E.g. EE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the P45 report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getP60ReportOutput"></a>
# **getP60ReportOutput**
> File getP60ReportOutput(employerKey, taxYear, authorization, apiVersion, employeeCodes, transformDefinitionKey, startIndex, maxIndex)

Runs the P60 report

Returns the result of the executed P60 report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    String employeeCodes = "employeeCodes_example"; // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
    String transformDefinitionKey = "transformDefinitionKey_example"; // String | The transform definition unique key. E.g. P45-Pdf
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    try {
      File result = apiInstance.getP60ReportOutput(employerKey, taxYear, authorization, apiVersion, employeeCodes, transformDefinitionKey, startIndex, maxIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getP60ReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] |
| **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the P60 report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPapdisReportOuput"></a>
# **getPapdisReportOuput**
> File getPapdisReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, authorization, apiVersion, paymentDate, transformDefinitionKey)

Runs the PAPDIS report

Returns the result of the executed PAPDIS report. PAPDIS is a free and open data interface standard designed to allow payroll and middleware software developers to create a file that can be used by pension providers to exchange data. http://www.papdis.org/

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String pensionKey = "pensionKey_example"; // String | The pension scheme unique key. E.g. PENSCH001
    String messageFunctionCode = "messageFunctionCode_example"; // String | Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions).
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    LocalDate paymentDate = LocalDate.now(); // LocalDate | The payment date context for the report. E.g. 2018-04-30
    String transformDefinitionKey = "transformDefinitionKey_example"; // String | The transform definition unique key. E.g. P45-Pdf
    try {
      File result = apiInstance.getPapdisReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, authorization, apiVersion, paymentDate, transformDefinitionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getPapdisReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **pensionKey** | **String**| The pension scheme unique key. E.g. PENSCH001 | |
| **messageFunctionCode** | **String**| Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions). | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **paymentDate** | **LocalDate**| The payment date context for the report. E.g. 2018-04-30 | [optional] |
| **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the PAPDIS report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPassReportOuput"></a>
# **getPassReportOuput**
> File getPassReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, intermediaryId, documentId, authorization, apiVersion, paymentDate)

Runs the PASS report

Returns the result of the executed PASS report. PASS stands for Payroll and Systemsync. PASS 1.1 is an extension of the PAPDIS V1.1 schema. https://pensionsynckb.systemsyncsolutions.com/display/PKB/PASS+1.1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String pensionKey = "pensionKey_example"; // String | The pension scheme unique key. E.g. PENSCH001
    String messageFunctionCode = "messageFunctionCode_example"; // String | Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions).
    String intermediaryId = "intermediaryId_example"; // String | Specific to PensionSync PASS report, a unique identifier for the Intermediary who is acting on behalf of the employer.
    String documentId = "documentId_example"; // String | Specific to PensionSync PASS report, a document identifier unique for this document within the Intermediary.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    LocalDate paymentDate = LocalDate.now(); // LocalDate | The payment date context for the report. E.g. 2018-04-30
    try {
      File result = apiInstance.getPassReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, intermediaryId, documentId, authorization, apiVersion, paymentDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getPassReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **pensionKey** | **String**| The pension scheme unique key. E.g. PENSCH001 | |
| **messageFunctionCode** | **String**| Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions). | |
| **intermediaryId** | **String**| Specific to PensionSync PASS report, a unique identifier for the Intermediary who is acting on behalf of the employer. | |
| **documentId** | **String**| Specific to PensionSync PASS report, a document identifier unique for this document within the Intermediary. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **paymentDate** | **LocalDate**| The payment date context for the report. E.g. 2018-04-30 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the PASS report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPayDashboardPayslipReportOuput"></a>
# **getPayDashboardPayslipReportOuput**
> File getPayDashboardPayslipReportOuput(employerKey, payScheduleKey, taxYear, publicationDate, authorization, apiVersion, employeeCodes, transformDefinitionKey, startIndex, maxIndex, paymentDate)

Runs the Pay Dashboard payslips report

Returns the result of the executed Pay Dashboard payslip report for the given query parameters. See https://api.paydashboard.com for details. For compatability should be returned as JSON with TransformDefinitionKey&#x3D;Json-Clean.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    LocalDate publicationDate = LocalDate.now(); // LocalDate | Specific to the Pay Dashboard report, allows the specification of a future payslip publication date. E.g. 2018-12-31
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    String employeeCodes = "employeeCodes_example"; // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
    String transformDefinitionKey = "transformDefinitionKey_example"; // String | The transform definition unique key. E.g. P45-Pdf
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    LocalDate paymentDate = LocalDate.now(); // LocalDate | The payment date context for the report. E.g. 2018-04-30
    try {
      File result = apiInstance.getPayDashboardPayslipReportOuput(employerKey, payScheduleKey, taxYear, publicationDate, authorization, apiVersion, employeeCodes, transformDefinitionKey, startIndex, maxIndex, paymentDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getPayDashboardPayslipReportOuput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **publicationDate** | **LocalDate**| Specific to the Pay Dashboard report, allows the specification of a future payslip publication date. E.g. 2018-12-31 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] |
| **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |
| **paymentDate** | **LocalDate**| The payment date context for the report. E.g. 2018-04-30 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the Pay Dashboard payslip report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPayslip3ReportOutput"></a>
# **getPayslip3ReportOutput**
> File getPayslip3ReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, employeeCodes, transformDefinitionKey, startIndex, maxIndex, paymentDate)

Runs the verbose payslip report

Returns the result of the executed verbose payslip report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    String payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    String employeeCodes = "employeeCodes_example"; // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
    String transformDefinitionKey = "transformDefinitionKey_example"; // String | The transform definition unique key. E.g. P45-Pdf
    String startIndex = "startIndex_example"; // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
    String maxIndex = "maxIndex_example"; // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    LocalDate paymentDate = LocalDate.now(); // LocalDate | The payment date context for the report. E.g. 2018-04-30
    try {
      File result = apiInstance.getPayslip3ReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, employeeCodes, transformDefinitionKey, startIndex, maxIndex, paymentDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getPayslip3ReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] |
| **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] |
| **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] |
| **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] |
| **paymentDate** | **LocalDate**| The payment date context for the report. E.g. 2018-04-30 | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the verbose payslip report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPensionLiabilityReportOutput"></a>
# **getPensionLiabilityReportOutput**
> File getPensionLiabilityReportOutput(employerKey, taxYear, pensionKey, authorization, apiVersion)

Runs the pension liability report

Returns the result of the executed pension liability report for the given query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
    Integer taxYear = 56; // Integer | The tax year. E.g. 2017 = 2017/18 year.
    String pensionKey = "pensionKey_example"; // String | The pension scheme unique key. E.g. PENSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getPensionLiabilityReportOutput(employerKey, taxYear, pensionKey, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getPensionLiabilityReportOutput");
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
| **employerKey** | **String**| The employer unique key. E.g. ER001 | |
| **taxYear** | **Integer**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | |
| **pensionKey** | **String**| The pension scheme unique key. E.g. PENSCH001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the pension liability report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getReportDefinitionFromApplication"></a>
# **getReportDefinitionFromApplication**
> ReportDefinition getReportDefinitionFromApplication(reportDefinitionId, authorization, apiVersion)

Get the report definition

Returns the specified report definition from the authroised application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      ReportDefinition result = apiInstance.getReportDefinitionFromApplication(reportDefinitionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReportDefinitionFromApplication");
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
| **reportDefinitionId** | **String**| The report definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**ReportDefinition**](ReportDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The report definition object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getReportDefinitionsFromApplication"></a>
# **getReportDefinitionsFromApplication**
> LinkCollection getReportDefinitionsFromApplication(authorization, apiVersion)

Gets all reports

Get links to all saved report definitions under authorised application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getReportDefinitionsFromApplication(authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReportDefinitionsFromApplication");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link collection object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getReportOutput"></a>
# **getReportOutput**
> File getReportOutput(reportDefinitionId, authorization, apiVersion)

Runs the specified report definition

Returns the result of the executed report definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      File result = apiInstance.getReportOutput(reportDefinitionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReportOutput");
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
| **reportDefinitionId** | **String**| The report definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the report execution |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getTransformDefinitionFromApplication"></a>
# **getTransformDefinitionFromApplication**
> TransformDefinition getTransformDefinitionFromApplication(transformDefinitionId, authorization, apiVersion)

Get the transform definition

Returns the specified transform definition from the authroised application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String transformDefinitionId = "transformDefinitionId_example"; // String | The transform definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      TransformDefinition result = apiInstance.getTransformDefinitionFromApplication(transformDefinitionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getTransformDefinitionFromApplication");
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
| **transformDefinitionId** | **String**| The transform definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**TransformDefinition**](TransformDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The transform definition object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getTransformDefinitionsFromApplication"></a>
# **getTransformDefinitionsFromApplication**
> LinkCollection getTransformDefinitionsFromApplication(authorization, apiVersion)

Gets all transform definitions

Get links to all saved transform definitions under authorised application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTransformDefinitionsFromApplication(authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getTransformDefinitionsFromApplication");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link collection object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postReportDefinition"></a>
# **postReportDefinition**
> Link postReportDefinition(authorization, apiVersion, reportDefinition)

Create a new report definition

Creates a new report defintion object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    ReportDefinition reportDefinition = new ReportDefinition(); // ReportDefinition | The report definition object.
    try {
      Link result = apiInstance.postReportDefinition(authorization, apiVersion, reportDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#postReportDefinition");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **reportDefinition** | [**ReportDefinition**](ReportDefinition.md)| The report definition object. | |

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The link object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postTransformDefinition"></a>
# **postTransformDefinition**
> Link postTransformDefinition(authorization, apiVersion, transformDefinition)

Create a new transform definition

Creates a new transform defintion object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    TransformDefinition transformDefinition = new TransformDefinition(); // TransformDefinition | The transform definition object to be executed against the report data.
    try {
      Link result = apiInstance.postTransformDefinition(authorization, apiVersion, transformDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#postTransformDefinition");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **transformDefinition** | [**TransformDefinition**](TransformDefinition.md)| The transform definition object to be executed against the report data. | |

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The link object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putReportDefinition"></a>
# **putReportDefinition**
> ReportDefinition putReportDefinition(reportDefinitionId, authorization, apiVersion, reportDefinition)

Updates a report definition

Updates the existing specified report definition object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    ReportDefinition reportDefinition = new ReportDefinition(); // ReportDefinition | The report definition object.
    try {
      ReportDefinition result = apiInstance.putReportDefinition(reportDefinitionId, authorization, apiVersion, reportDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#putReportDefinition");
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
| **reportDefinitionId** | **String**| The report definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **reportDefinition** | [**ReportDefinition**](ReportDefinition.md)| The report definition object. | |

### Return type

[**ReportDefinition**](ReportDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The report definition object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putTransformDefinition"></a>
# **putTransformDefinition**
> TransformDefinition putTransformDefinition(transformDefinitionId, authorization, apiVersion, transformDefinition)

Updates a transform definition

Updates the existing specified transform definition object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String transformDefinitionId = "transformDefinitionId_example"; // String | The transform definition unique identifier.
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    TransformDefinition transformDefinition = new TransformDefinition(); // TransformDefinition | The transform definition object to be executed against the report data.
    try {
      TransformDefinition result = apiInstance.putTransformDefinition(transformDefinitionId, authorization, apiVersion, transformDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#putTransformDefinition");
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
| **transformDefinitionId** | **String**| The transform definition unique identifier. | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **transformDefinition** | [**TransformDefinition**](TransformDefinition.md)| The transform definition object to be executed against the report data. | |

### Return type

[**TransformDefinition**](TransformDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The transform definition object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

