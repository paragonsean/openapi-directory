# PayStatementsApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear**](PayStatementsApi.md#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year} | Get employee pay statement details data for the specified year. |
| [**getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate**](PayStatementsApi.md#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}/{checkDate} | Get employee pay statement details data for the specified year and check date. |
| [**getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear**](PayStatementsApi.md#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year} | Get employee pay statement summary data for the specified year. |
| [**getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate**](PayStatementsApi.md#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate} | Get employee pay statement summary data for the specified year and check date. |


<a id="getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear"></a>
# **getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear**
> List&lt;PayStatementDetails&gt; getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear(companyId, employeeId, year, pagesize, pagenumber, includetotalcount, codegroup)

Get employee pay statement details data for the specified year.

Get pay statement details API will return employee pay statement details data currently available in Web Pay for the specified year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    PayStatementsApi apiInstance = new PayStatementsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String year = "year_example"; // String | The year for which to retrieve pay statement data
    Integer pagesize = 56; // Integer | Number of records per page. Default value is 25.
    Integer pagenumber = 56; // Integer | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
    Boolean includetotalcount = true; // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
    String codegroup = "codegroup_example"; // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    try {
      List<PayStatementDetails> result = apiInstance.getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear(companyId, employeeId, year, pagesize, pagenumber, includetotalcount, codegroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayStatementsApi#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear");
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
| **employeeId** | **String**| Employee Id | |
| **year** | **String**| The year for which to retrieve pay statement data | |
| **pagesize** | **Integer**| Number of records per page. Default value is 25. | [optional] |
| **pagenumber** | **Integer**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] |
| **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] |
| **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] |

### Return type

[**List&lt;PayStatementDetails&gt;**](PayStatementDetails.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully Retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee, specified year, or check date does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate"></a>
# **getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate**
> List&lt;PayStatementDetails&gt; getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, pagesize, pagenumber, includetotalcount, codegroup)

Get employee pay statement details data for the specified year and check date.

Get pay statement details API will return employee pay statement detail data currently available in Web Pay for the specified year and check date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    PayStatementsApi apiInstance = new PayStatementsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String year = "year_example"; // String | The year for which to retrieve pay statement data
    String checkDate = "checkDate_example"; // String | The check date for which to retrieve pay statement data
    Integer pagesize = 56; // Integer | Number of records per page. Default value is 25.
    Integer pagenumber = 56; // Integer | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
    Boolean includetotalcount = true; // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
    String codegroup = "codegroup_example"; // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    try {
      List<PayStatementDetails> result = apiInstance.getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, pagesize, pagenumber, includetotalcount, codegroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayStatementsApi#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate");
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
| **employeeId** | **String**| Employee Id | |
| **year** | **String**| The year for which to retrieve pay statement data | |
| **checkDate** | **String**| The check date for which to retrieve pay statement data | |
| **pagesize** | **Integer**| Number of records per page. Default value is 25. | [optional] |
| **pagenumber** | **Integer**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] |
| **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] |
| **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] |

### Return type

[**List&lt;PayStatementDetails&gt;**](PayStatementDetails.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully Retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee, specified year, or check date does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear"></a>
# **getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear**
> List&lt;PayStatementSummary&gt; getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear(companyId, employeeId, year, pagesize, pagenumber, includetotalcount, codegroup)

Get employee pay statement summary data for the specified year.

Get pay statement summary API will return employee pay statement summary data currently available in Web Pay for the specified year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    PayStatementsApi apiInstance = new PayStatementsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String year = "year_example"; // String | The year for which to retrieve pay statement data
    Integer pagesize = 56; // Integer | Number of records per page. Default value is 25.
    Integer pagenumber = 56; // Integer | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
    Boolean includetotalcount = true; // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
    String codegroup = "codegroup_example"; // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    try {
      List<PayStatementSummary> result = apiInstance.getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear(companyId, employeeId, year, pagesize, pagenumber, includetotalcount, codegroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayStatementsApi#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear");
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
| **employeeId** | **String**| Employee Id | |
| **year** | **String**| The year for which to retrieve pay statement data | |
| **pagesize** | **Integer**| Number of records per page. Default value is 25. | [optional] |
| **pagenumber** | **Integer**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] |
| **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] |
| **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] |

### Return type

[**List&lt;PayStatementSummary&gt;**](PayStatementSummary.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully Retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee, specified year, or check date does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate"></a>
# **getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate**
> List&lt;PayStatementSummary&gt; getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, pagesize, pagenumber, includetotalcount, codegroup)

Get employee pay statement summary data for the specified year and check date.

Get pay statement summary API will return employee pay statement summary data currently available in Web Pay for the specified year and check date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    PayStatementsApi apiInstance = new PayStatementsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    String year = "year_example"; // String | The year for which to retrieve pay statement data
    String checkDate = "checkDate_example"; // String | The check date for which to retrieve pay statement data
    Integer pagesize = 56; // Integer | Number of records per page. Default value is 25.
    Integer pagenumber = 56; // Integer | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
    Boolean includetotalcount = true; // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
    String codegroup = "codegroup_example"; // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    try {
      List<PayStatementSummary> result = apiInstance.getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, pagesize, pagenumber, includetotalcount, codegroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayStatementsApi#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate");
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
| **employeeId** | **String**| Employee Id | |
| **year** | **String**| The year for which to retrieve pay statement data | |
| **checkDate** | **String**| The check date for which to retrieve pay statement data | |
| **pagesize** | **Integer**| Number of records per page. Default value is 25. | [optional] |
| **pagenumber** | **Integer**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] |
| **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] |
| **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] |

### Return type

[**List&lt;PayStatementSummary&gt;**](PayStatementSummary.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully Retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee, specified year, or check date does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

