# CalculationApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calculationGetAtIntervals**](CalculationApi.md#calculationGetAtIntervals) | **GET** /calculation/intervals | Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval. |
| [**calculationGetAtRecorded**](CalculationApi.md#calculationGetAtRecorded) | **GET** /calculation/recorded | Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression. |
| [**calculationGetAtTimes**](CalculationApi.md#calculationGetAtTimes) | **GET** /calculation/times | Returns the result of evaluating the expression at the specified timestamps. |
| [**calculationGetSummary**](CalculationApi.md#calculationGetSummary) | **GET** /calculation/summary | Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval. |


<a id="calculationGetAtIntervals"></a>
# **calculationGetAtIntervals**
> TimedValues calculationGetAtIntervals(expression, endTime, sampleInterval, selectedFields, startTime, webId)

Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalculationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    CalculationApi apiInstance = new CalculationApi(defaultClient);
    String expression = "expression_example"; // String | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String sampleInterval = "sampleInterval_example"; // String | A time span specifies how often the filter expression is evaluated when computing the summary for an interval.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String webId = "webId_example"; // String | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    try {
      TimedValues result = apiInstance.calculationGetAtIntervals(expression, endTime, sampleInterval, selectedFields, startTime, webId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalculationApi#calculationGetAtIntervals");
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
| **expression** | **String**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **sampleInterval** | **String**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **webId** | **String**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] |

### Return type

[**TimedValues**](TimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The calculated values. |  -  |
| **409** | The targeted object does not support the calculation. |  -  |

<a id="calculationGetAtRecorded"></a>
# **calculationGetAtRecorded**
> TimedValues calculationGetAtRecorded(expression, endTime, selectedFields, startTime, webId)

Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalculationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    CalculationApi apiInstance = new CalculationApi(defaultClient);
    String expression = "expression_example"; // String | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String webId = "webId_example"; // String | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    try {
      TimedValues result = apiInstance.calculationGetAtRecorded(expression, endTime, selectedFields, startTime, webId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalculationApi#calculationGetAtRecorded");
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
| **expression** | **String**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **webId** | **String**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] |

### Return type

[**TimedValues**](TimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The calculated values. |  -  |
| **409** | The targeted object does not support the calculation. |  -  |

<a id="calculationGetAtTimes"></a>
# **calculationGetAtTimes**
> TimedValues calculationGetAtTimes(expression, time, selectedFields, sortOrder, webId)

Returns the result of evaluating the expression at the specified timestamps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalculationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    CalculationApi apiInstance = new CalculationApi(defaultClient);
    String expression = "expression_example"; // String | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    List<String> time = Arrays.asList(); // List<String> | A list of timestamps at which to calculate the expression.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String webId = "webId_example"; // String | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    try {
      TimedValues result = apiInstance.calculationGetAtTimes(expression, time, selectedFields, sortOrder, webId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalculationApi#calculationGetAtTimes");
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
| **expression** | **String**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | |
| **time** | [**List&lt;String&gt;**](String.md)| A list of timestamps at which to calculate the expression. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **webId** | **String**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] |

### Return type

[**TimedValues**](TimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The calculated values. |  -  |
| **409** | The targeted object does not support the calculation. |  -  |

<a id="calculationGetSummary"></a>
# **calculationGetSummary**
> ItemsSummaryValue calculationGetSummary(expression, calculationBasis, endTime, sampleInterval, sampleType, selectedFields, startTime, summaryDuration, summaryType, timeType, webId)

Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalculationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    CalculationApi apiInstance = new CalculationApi(defaultClient);
    String expression = "expression_example"; // String | A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    String calculationBasis = "calculationBasis_example"; // String | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String sampleInterval = "sampleInterval_example"; // String | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.
    String sampleType = "sampleType_example"; // String | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String summaryDuration = "summaryDuration_example"; // String | The duration of each summary interval.
    List<String> summaryType = Arrays.asList(); // List<String> | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.
    String timeType = "timeType_example"; // String | Specifies how to calculate the timestamp for each interval. The default is 'Auto'.
    String webId = "webId_example"; // String | The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    try {
      ItemsSummaryValue result = apiInstance.calculationGetSummary(expression, calculationBasis, endTime, sampleInterval, sampleType, selectedFields, startTime, summaryDuration, summaryType, timeType, webId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalculationApi#calculationGetSummary");
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
| **expression** | **String**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation. | |
| **calculationBasis** | **String**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **sampleInterval** | **String**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] |
| **sampleType** | **String**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **summaryDuration** | **String**| The duration of each summary interval. | [optional] |
| **summaryType** | [**List&lt;String&gt;**](String.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] |
| **timeType** | **String**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] |
| **webId** | **String**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null. | [optional] |

### Return type

[**ItemsSummaryValue**](ItemsSummaryValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The calculated values. |  -  |
| **409** | The targeted object does not support the calculation. |  -  |

