# PayrollAuApi

All URIs are relative to *https://api.xero.com/payroll.xro/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEmployee**](PayrollAuApi.md#createEmployee) | **POST** /Employees | Creates a payroll employee |
| [**createLeaveApplication**](PayrollAuApi.md#createLeaveApplication) | **POST** /LeaveApplications | Creates a leave application |
| [**createPayItem**](PayrollAuApi.md#createPayItem) | **POST** /PayItems | Creates a pay item |
| [**createPayRun**](PayrollAuApi.md#createPayRun) | **POST** /PayRuns | Creates a pay run |
| [**createPayrollCalendar**](PayrollAuApi.md#createPayrollCalendar) | **POST** /PayrollCalendars | Creates a Payroll Calendar |
| [**createSuperfund**](PayrollAuApi.md#createSuperfund) | **POST** /Superfunds | Creates a superfund |
| [**createTimesheet**](PayrollAuApi.md#createTimesheet) | **POST** /Timesheets | Creates a timesheet |
| [**getEmployee**](PayrollAuApi.md#getEmployee) | **GET** /Employees/{EmployeeID} | Retrieves an employee&#39;s detail by unique employee id |
| [**getEmployees**](PayrollAuApi.md#getEmployees) | **GET** /Employees | Searches payroll employees |
| [**getLeaveApplication**](PayrollAuApi.md#getLeaveApplication) | **GET** /LeaveApplications/{LeaveApplicationID} | Retrieves a leave application by a unique leave application id |
| [**getLeaveApplications**](PayrollAuApi.md#getLeaveApplications) | **GET** /LeaveApplications | Retrieves leave applications |
| [**getPayItems**](PayrollAuApi.md#getPayItems) | **GET** /PayItems | Retrieves pay items |
| [**getPayRun**](PayrollAuApi.md#getPayRun) | **GET** /PayRuns/{PayRunID} | Retrieves a pay run by using a unique pay run id |
| [**getPayRuns**](PayrollAuApi.md#getPayRuns) | **GET** /PayRuns | Retrieves pay runs |
| [**getPayrollCalendar**](PayrollAuApi.md#getPayrollCalendar) | **GET** /PayrollCalendars/{PayrollCalendarID} | Retrieves payroll calendar by using a unique payroll calendar ID |
| [**getPayrollCalendars**](PayrollAuApi.md#getPayrollCalendars) | **GET** /PayrollCalendars | Retrieves payroll calendars |
| [**getPayslip**](PayrollAuApi.md#getPayslip) | **GET** /Payslip/{PayslipID} | Retrieves for a payslip by a unique payslip id |
| [**getSettings**](PayrollAuApi.md#getSettings) | **GET** /Settings | Retrieves payroll settings |
| [**getSuperfund**](PayrollAuApi.md#getSuperfund) | **GET** /Superfunds/{SuperFundID} | Retrieves a superfund by using a unique superfund ID |
| [**getSuperfundProducts**](PayrollAuApi.md#getSuperfundProducts) | **GET** /SuperfundProducts | Retrieves superfund products |
| [**getSuperfunds**](PayrollAuApi.md#getSuperfunds) | **GET** /Superfunds | Retrieves superfunds |
| [**getTimesheet**](PayrollAuApi.md#getTimesheet) | **GET** /Timesheets/{TimesheetID} | Retrieves a timesheet by using a unique timesheet id |
| [**getTimesheets**](PayrollAuApi.md#getTimesheets) | **GET** /Timesheets | Retrieves timesheets |
| [**updateEmployee**](PayrollAuApi.md#updateEmployee) | **POST** /Employees/{EmployeeID} | Updates an employee&#39;s detail |
| [**updateLeaveApplication**](PayrollAuApi.md#updateLeaveApplication) | **POST** /LeaveApplications/{LeaveApplicationID} | Updates a specific leave application |
| [**updatePayRun**](PayrollAuApi.md#updatePayRun) | **POST** /PayRuns/{PayRunID} | Updates a pay run |
| [**updatePayslip**](PayrollAuApi.md#updatePayslip) | **POST** /Payslip/{PayslipID} | Updates a payslip |
| [**updateSuperfund**](PayrollAuApi.md#updateSuperfund) | **POST** /Superfunds/{SuperFundID} | Updates a superfund |
| [**updateTimesheet**](PayrollAuApi.md#updateTimesheet) | **POST** /Timesheets/{TimesheetID} | Updates a timesheet |


<a id="createEmployee"></a>
# **createEmployee**
> Employees createEmployee(xeroTenantId, employee)

Creates a payroll employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    List<Employee> employee = Arrays.asList(); // List<Employee> | 
    try {
      Employees result = apiInstance.createEmployee(xeroTenantId, employee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createEmployee");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **employee** | [**List&lt;Employee&gt;**](Employee.md)|  | |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="createLeaveApplication"></a>
# **createLeaveApplication**
> LeaveApplications createLeaveApplication(xeroTenantId, leaveApplication)

Creates a leave application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    List<LeaveApplication> leaveApplication = Arrays.asList(); // List<LeaveApplication> | 
    try {
      LeaveApplications result = apiInstance.createLeaveApplication(xeroTenantId, leaveApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createLeaveApplication");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **leaveApplication** | [**List&lt;LeaveApplication&gt;**](LeaveApplication.md)|  | |

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="createPayItem"></a>
# **createPayItem**
> PayItems createPayItem(xeroTenantId, payItem)

Creates a pay item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    PayItem payItem = new PayItem(); // PayItem | 
    try {
      PayItems result = apiInstance.createPayItem(xeroTenantId, payItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createPayItem");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payItem** | [**PayItem**](PayItem.md)|  | |

### Return type

[**PayItems**](PayItems.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request - currently returns empty array for JSON |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="createPayRun"></a>
# **createPayRun**
> PayRuns createPayRun(xeroTenantId, payRun)

Creates a pay run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    List<PayRun> payRun = Arrays.asList(); // List<PayRun> | 
    try {
      PayRuns result = apiInstance.createPayRun(xeroTenantId, payRun);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createPayRun");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payRun** | [**List&lt;PayRun&gt;**](PayRun.md)|  | |

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="createPayrollCalendar"></a>
# **createPayrollCalendar**
> PayrollCalendars createPayrollCalendar(xeroTenantId, payrollCalendar)

Creates a Payroll Calendar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    List<PayrollCalendar> payrollCalendar = Arrays.asList(); // List<PayrollCalendar> | 
    try {
      PayrollCalendars result = apiInstance.createPayrollCalendar(xeroTenantId, payrollCalendar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createPayrollCalendar");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payrollCalendar** | [**List&lt;PayrollCalendar&gt;**](PayrollCalendar.md)|  | |

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="createSuperfund"></a>
# **createSuperfund**
> SuperFunds createSuperfund(xeroTenantId, superFund)

Creates a superfund

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    List<SuperFund> superFund = Arrays.asList(); // List<SuperFund> | 
    try {
      SuperFunds result = apiInstance.createSuperfund(xeroTenantId, superFund);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createSuperfund");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **superFund** | [**List&lt;SuperFund&gt;**](SuperFund.md)|  | |

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="createTimesheet"></a>
# **createTimesheet**
> Timesheets createTimesheet(xeroTenantId, timesheet)

Creates a timesheet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    List<Timesheet> timesheet = Arrays.asList(); // List<Timesheet> | 
    try {
      Timesheets result = apiInstance.createTimesheet(xeroTenantId, timesheet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#createTimesheet");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **timesheet** | [**List&lt;Timesheet&gt;**](Timesheet.md)|  | |

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="getEmployee"></a>
# **getEmployee**
> Employees getEmployee(xeroTenantId, employeeID)

Retrieves an employee&#39;s detail by unique employee id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID employeeID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Employee id for single object
    try {
      Employees result = apiInstance.getEmployee(xeroTenantId, employeeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getEmployee");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **employeeID** | **UUID**| Employee id for single object | |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getEmployees"></a>
# **getEmployees**
> Employees getEmployees(xeroTenantId, ifModifiedSince, where, order, page)

Searches payroll employees

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 employees will be returned in a single API call
    try {
      Employees result = apiInstance.getEmployees(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getEmployees");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 employees will be returned in a single API call | [optional] |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getLeaveApplication"></a>
# **getLeaveApplication**
> LeaveApplications getLeaveApplication(xeroTenantId, leaveApplicationID)

Retrieves a leave application by a unique leave application id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID leaveApplicationID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Leave Application id for single object
    try {
      LeaveApplications result = apiInstance.getLeaveApplication(xeroTenantId, leaveApplicationID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getLeaveApplication");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **leaveApplicationID** | **UUID**| Leave Application id for single object | |

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getLeaveApplications"></a>
# **getLeaveApplications**
> LeaveApplications getLeaveApplications(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves leave applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 objects will be returned in a single API call
    try {
      LeaveApplications result = apiInstance.getLeaveApplications(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getLeaveApplications");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] |

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getPayItems"></a>
# **getPayItems**
> PayItems getPayItems(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves pay items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 objects will be returned in a single API call
    try {
      PayItems result = apiInstance.getPayItems(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getPayItems");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] |

### Return type

[**PayItems**](PayItems.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getPayRun"></a>
# **getPayRun**
> PayRuns getPayRun(xeroTenantId, payRunID)

Retrieves a pay run by using a unique pay run id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID payRunID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | PayRun id for single object
    try {
      PayRuns result = apiInstance.getPayRun(xeroTenantId, payRunID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getPayRun");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payRunID** | **UUID**| PayRun id for single object | |

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getPayRuns"></a>
# **getPayRuns**
> PayRuns getPayRuns(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves pay runs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 PayRuns will be returned in a single API call
    try {
      PayRuns result = apiInstance.getPayRuns(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getPayRuns");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 PayRuns will be returned in a single API call | [optional] |

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getPayrollCalendar"></a>
# **getPayrollCalendar**
> PayrollCalendars getPayrollCalendar(xeroTenantId, payrollCalendarID)

Retrieves payroll calendar by using a unique payroll calendar ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID payrollCalendarID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Payroll Calendar id for single object
    try {
      PayrollCalendars result = apiInstance.getPayrollCalendar(xeroTenantId, payrollCalendarID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getPayrollCalendar");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payrollCalendarID** | **UUID**| Payroll Calendar id for single object | |

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getPayrollCalendars"></a>
# **getPayrollCalendars**
> PayrollCalendars getPayrollCalendars(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves payroll calendars

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 objects will be returned in a single API call
    try {
      PayrollCalendars result = apiInstance.getPayrollCalendars(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getPayrollCalendars");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] |

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getPayslip"></a>
# **getPayslip**
> PayslipObject getPayslip(xeroTenantId, payslipID)

Retrieves for a payslip by a unique payslip id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID payslipID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Payslip id for single object
    try {
      PayslipObject result = apiInstance.getPayslip(xeroTenantId, payslipID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getPayslip");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payslipID** | **UUID**| Payslip id for single object | |

### Return type

[**PayslipObject**](PayslipObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getSettings"></a>
# **getSettings**
> SettingsObject getSettings(xeroTenantId)

Retrieves payroll settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    try {
      SettingsObject result = apiInstance.getSettings(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getSettings");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**SettingsObject**](SettingsObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | payroll settings |  -  |

<a id="getSuperfund"></a>
# **getSuperfund**
> SuperFunds getSuperfund(xeroTenantId, superFundID)

Retrieves a superfund by using a unique superfund ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID superFundID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Superfund id for single object
    try {
      SuperFunds result = apiInstance.getSuperfund(xeroTenantId, superFundID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getSuperfund");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **superFundID** | **UUID**| Superfund id for single object | |

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getSuperfundProducts"></a>
# **getSuperfundProducts**
> SuperFundProducts getSuperfundProducts(xeroTenantId, ABN, USI)

Retrieves superfund products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ABN = "40022701955"; // String | The ABN of the Regulated SuperFund
    String USI = "OSF0001AU"; // String | The USI of the Regulated SuperFund
    try {
      SuperFundProducts result = apiInstance.getSuperfundProducts(xeroTenantId, ABN, USI);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getSuperfundProducts");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ABN** | **String**| The ABN of the Regulated SuperFund | [optional] |
| **USI** | **String**| The USI of the Regulated SuperFund | [optional] |

### Return type

[**SuperFundProducts**](SuperFundProducts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getSuperfunds"></a>
# **getSuperfunds**
> SuperFunds getSuperfunds(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves superfunds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call
    try {
      SuperFunds result = apiInstance.getSuperfunds(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getSuperfunds");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 SuperFunds will be returned in a single API call | [optional] |

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="getTimesheet"></a>
# **getTimesheet**
> TimesheetObject getTimesheet(xeroTenantId, timesheetID)

Retrieves a timesheet by using a unique timesheet id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID timesheetID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Timesheet id for single object
    try {
      TimesheetObject result = apiInstance.getTimesheet(xeroTenantId, timesheetID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getTimesheet");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **timesheetID** | **UUID**| Timesheet id for single object | |

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getTimesheets"></a>
# **getTimesheets**
> Timesheets getTimesheets(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves timesheets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    String ifModifiedSince = "ifModifiedSince_example"; // String | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "EmailAddress%20DESC"; // String | Order by an any element
    Integer page = 56; // Integer | e.g. page=1 – Up to 100 timesheets will be returned in a single API call
    try {
      Timesheets result = apiInstance.getTimesheets(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#getTimesheets");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 timesheets will be returned in a single API call | [optional] |

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | validation error for a bad request |  -  |

<a id="updateEmployee"></a>
# **updateEmployee**
> Employees updateEmployee(xeroTenantId, employeeID, employee)

Updates an employee&#39;s detail

Update properties on a single employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID employeeID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Employee id for single object
    List<Employee> employee = Arrays.asList(); // List<Employee> | 
    try {
      Employees result = apiInstance.updateEmployee(xeroTenantId, employeeID, employee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#updateEmployee");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **employeeID** | **UUID**| Employee id for single object | |
| **employee** | [**List&lt;Employee&gt;**](Employee.md)|  | [optional] |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |

<a id="updateLeaveApplication"></a>
# **updateLeaveApplication**
> LeaveApplications updateLeaveApplication(xeroTenantId, leaveApplicationID, leaveApplication)

Updates a specific leave application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID leaveApplicationID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Leave Application id for single object
    List<LeaveApplication> leaveApplication = Arrays.asList(); // List<LeaveApplication> | 
    try {
      LeaveApplications result = apiInstance.updateLeaveApplication(xeroTenantId, leaveApplicationID, leaveApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#updateLeaveApplication");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **leaveApplicationID** | **UUID**| Leave Application id for single object | |
| **leaveApplication** | [**List&lt;LeaveApplication&gt;**](LeaveApplication.md)|  | |

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid - TODO |  -  |

<a id="updatePayRun"></a>
# **updatePayRun**
> PayRuns updatePayRun(xeroTenantId, payRunID, payRun)

Updates a pay run

Update properties on a single PayRun

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID payRunID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | PayRun id for single object
    List<PayRun> payRun = Arrays.asList(); // List<PayRun> | 
    try {
      PayRuns result = apiInstance.updatePayRun(xeroTenantId, payRunID, payRun);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#updatePayRun");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payRunID** | **UUID**| PayRun id for single object | |
| **payRun** | [**List&lt;PayRun&gt;**](PayRun.md)|  | [optional] |

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |

<a id="updatePayslip"></a>
# **updatePayslip**
> Payslips updatePayslip(xeroTenantId, payslipID, payslipLines)

Updates a payslip

Update lines on a single payslips

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID payslipID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Payslip id for single object
    List<PayslipLines> payslipLines = Arrays.asList(); // List<PayslipLines> | 
    try {
      Payslips result = apiInstance.updatePayslip(xeroTenantId, payslipID, payslipLines);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#updatePayslip");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payslipID** | **UUID**| Payslip id for single object | |
| **payslipLines** | [**List&lt;PayslipLines&gt;**](PayslipLines.md)|  | [optional] |

### Return type

[**Payslips**](Payslips.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request - currently returns empty array for JSON |  -  |

<a id="updateSuperfund"></a>
# **updateSuperfund**
> SuperFunds updateSuperfund(xeroTenantId, superFundID, superFund)

Updates a superfund

Update properties on a single Superfund

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID superFundID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Superfund id for single object
    List<SuperFund> superFund = Arrays.asList(); // List<SuperFund> | 
    try {
      SuperFunds result = apiInstance.updateSuperfund(xeroTenantId, superFundID, superFund);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#updateSuperfund");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **superFundID** | **UUID**| Superfund id for single object | |
| **superFund** | [**List&lt;SuperFund&gt;**](SuperFund.md)|  | [optional] |

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |

<a id="updateTimesheet"></a>
# **updateTimesheet**
> Timesheets updateTimesheet(xeroTenantId, timesheetID, timesheet)

Updates a timesheet

Update properties on a single timesheet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayrollAuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/payroll.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayrollAuApi apiInstance = new PayrollAuApi(defaultClient);
    String xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
    UUID timesheetID = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Timesheet id for single object
    List<Timesheet> timesheet = Arrays.asList(); // List<Timesheet> | 
    try {
      Timesheets result = apiInstance.updateTimesheet(xeroTenantId, timesheetID, timesheet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayrollAuApi#updateTimesheet");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **timesheetID** | **UUID**| Timesheet id for single object | |
| **timesheet** | [**List&lt;Timesheet&gt;**](Timesheet.md)|  | [optional] |

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |

