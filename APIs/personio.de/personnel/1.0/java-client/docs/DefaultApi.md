# DefaultApi

All URIs are relative to *https://api.personio.de/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyAttendancesGet**](DefaultApi.md#companyAttendancesGet) | **GET** /company/attendances |  |
| [**companyAttendancesIdDelete**](DefaultApi.md#companyAttendancesIdDelete) | **DELETE** /company/attendances/{id} |  |
| [**companyAttendancesIdPatch**](DefaultApi.md#companyAttendancesIdPatch) | **PATCH** /company/attendances/{id} |  |
| [**companyAttendancesPost**](DefaultApi.md#companyAttendancesPost) | **POST** /company/attendances |  |
| [**companyEmployeesEmployeeIdGet**](DefaultApi.md#companyEmployeesEmployeeIdGet) | **GET** /company/employees/{employee_id} |  |
| [**companyEmployeesEmployeeIdProfilePictureWidthGet**](DefaultApi.md#companyEmployeesEmployeeIdProfilePictureWidthGet) | **GET** /company/employees/{employee_id}/profile-picture/{width} |  |
| [**companyEmployeesGet**](DefaultApi.md#companyEmployeesGet) | **GET** /company/employees |  |
| [**companyEmployeesPost**](DefaultApi.md#companyEmployeesPost) | **POST** /company/employees | Create an employee |
| [**companyTimeOffTypesGet**](DefaultApi.md#companyTimeOffTypesGet) | **GET** /company/time-off-types |  |
| [**companyTimeOffsGet**](DefaultApi.md#companyTimeOffsGet) | **GET** /company/time-offs |  |
| [**companyTimeOffsIdDelete**](DefaultApi.md#companyTimeOffsIdDelete) | **DELETE** /company/time-offs/{id} |  |
| [**companyTimeOffsIdGet**](DefaultApi.md#companyTimeOffsIdGet) | **GET** /company/time-offs/{id} |  |
| [**companyTimeOffsPost**](DefaultApi.md#companyTimeOffsPost) | **POST** /company/time-offs |  |


<a id="companyAttendancesGet"></a>
# **companyAttendancesGet**
> AttendancePeriodsResponse companyAttendancesGet(startDate, endDate, updatedFrom, updatedTo, employees, limit, offset)



This endpoint is responsible for fetching attendance data for the company employees. It is possible to paginate results, filter by period, the date and/or time it was updated, and/or specific employees. The result will contain a list of attendance periods, structured as defined here.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    LocalDate startDate = LocalDate.now(); // LocalDate | First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results
    LocalDate endDate = LocalDate.now(); // LocalDate | Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results.
    String updatedFrom = "updatedFrom_example"; // String | Datetime from when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_from will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone.
    String updatedTo = "updatedTo_example"; // String | Datetime until when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_to will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone.
    List<Integer> employees = Arrays.asList(); // List<Integer> | A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned.
    Integer limit = 200; // Integer | Pagination attribute to limit how many attendances will be returned per page
    Integer offset = 0; // Integer | Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
    try {
      AttendancePeriodsResponse result = apiInstance.companyAttendancesGet(startDate, endDate, updatedFrom, updatedTo, employees, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyAttendancesGet");
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
| **startDate** | **LocalDate**| First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results | |
| **endDate** | **LocalDate**| Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results. | |
| **updatedFrom** | **String**| Datetime from when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_from will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone. | [optional] |
| **updatedTo** | **String**| Datetime until when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_to will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone. | [optional] |
| **employees** | [**List&lt;Integer&gt;**](Integer.md)| A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned. | [optional] |
| **limit** | **Integer**| Pagination attribute to limit how many attendances will be returned per page | [optional] [default to 200] |
| **offset** | **Integer**| Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned. | [optional] [default to 0] |

### Return type

[**AttendancePeriodsResponse**](AttendancePeriodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="companyAttendancesIdDelete"></a>
# **companyAttendancesIdDelete**
> Response companyAttendancesIdDelete(id)



This endpoint is responsible for deleting attendance data for the company employees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer id = 56; // Integer | ID of the attendance period to delete
    try {
      Response result = apiInstance.companyAttendancesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyAttendancesIdDelete");
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
| **id** | **Integer**| ID of the attendance period to delete | |

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response |  -  |
| **404** | Not found response |  -  |

<a id="companyAttendancesIdPatch"></a>
# **companyAttendancesIdPatch**
> Response companyAttendancesIdPatch(id, updateAttendancePeriodRequest)



This endpoint is responsible for updating attendance data for the company employees. Attributes are not required and if not specified, the current value will be used. It is not possible to change the employee id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer id = 56; // Integer | ID of the attendance period to update
    UpdateAttendancePeriodRequest updateAttendancePeriodRequest = new UpdateAttendancePeriodRequest(); // UpdateAttendancePeriodRequest | attendance period data to update
    try {
      Response result = apiInstance.companyAttendancesIdPatch(id, updateAttendancePeriodRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyAttendancesIdPatch");
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
| **id** | **Integer**| ID of the attendance period to update | |
| **updateAttendancePeriodRequest** | [**UpdateAttendancePeriodRequest**](UpdateAttendancePeriodRequest.md)| attendance period data to update | |

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response |  -  |
| **404** | Not found response |  -  |

<a id="companyAttendancesPost"></a>
# **companyAttendancesPost**
> NewAttendancePeriodResponse companyAttendancesPost(newAttendancePeriodRequest)



This endpoint is responsible for adding attendance data for the company employees. It is possible to add attendances for one or many employees at the same time. The payload sent on the request should be a list of attendance periods, in the form of an array containing attendance period objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    NewAttendancePeriodRequest newAttendancePeriodRequest = new NewAttendancePeriodRequest(); // NewAttendancePeriodRequest | List of attendance periods to create
    try {
      NewAttendancePeriodResponse result = apiInstance.companyAttendancesPost(newAttendancePeriodRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyAttendancesPost");
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
| **newAttendancePeriodRequest** | [**NewAttendancePeriodRequest**](NewAttendancePeriodRequest.md)| List of attendance periods to create | |

### Return type

[**NewAttendancePeriodResponse**](NewAttendancePeriodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The attendance periods were created successfully |  -  |
| **400** | Invalid request |  -  |

<a id="companyEmployeesEmployeeIdGet"></a>
# **companyEmployeesEmployeeIdGet**
> EmployeeResponse companyEmployeesEmployeeIdGet(employeeId)



Show employee by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer employeeId = 56; // Integer | Numeric `id` of the employee
    try {
      EmployeeResponse result = apiInstance.companyEmployeesEmployeeIdGet(employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEmployeesEmployeeIdGet");
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
| **employeeId** | **Integer**| Numeric &#x60;id&#x60; of the employee | |

### Return type

[**EmployeeResponse**](EmployeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="companyEmployeesEmployeeIdProfilePictureWidthGet"></a>
# **companyEmployeesEmployeeIdProfilePictureWidthGet**
> File companyEmployeesEmployeeIdProfilePictureWidthGet(employeeId, width)



Show employee profile picture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer employeeId = 56; // Integer | Numeric `id` of the employee
    Integer width = 56; // Integer | Width of the image. Default 75x75
    try {
      File result = apiInstance.companyEmployeesEmployeeIdProfilePictureWidthGet(employeeId, width);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEmployeesEmployeeIdProfilePictureWidthGet");
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
| **employeeId** | **Integer**| Numeric &#x60;id&#x60; of the employee | |
| **width** | **Integer**| Width of the image. Default 75x75 | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="companyEmployeesGet"></a>
# **companyEmployeesGet**
> EmployeesResponse companyEmployeesGet()



List Employees

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      EmployeesResponse result = apiInstance.companyEmployeesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEmployeesGet");
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

[**EmployeesResponse**](EmployeesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="companyEmployeesPost"></a>
# **companyEmployeesPost**
> Response companyEmployeesPost(employeeEmail, employeeFirstName, employeeLastName, employeeDepartment, employeeGender, employeeHireDate, employeePosition, employeeWeeklyHours)

Create an employee

Creates new employee. Status of the employee will be set to &#x60;active&#x60; if &#x60;hire_date&#x60; provided is in past. Otherwise status will be set to &#x60;onboarding&#x60;. This endpoint will respond with &#x60;id&#x60; of created employee in case of success. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String employeeEmail = "employeeEmail_example"; // String | Employee email
    String employeeFirstName = "employeeFirstName_example"; // String | Employee first name
    String employeeLastName = "employeeLastName_example"; // String | Employee last name
    String employeeDepartment = "employeeDepartment_example"; // String | Employee department
    String employeeGender = "male"; // String | Employee gender
    LocalDate employeeHireDate = LocalDate.now(); // LocalDate | Employee hire date
    String employeePosition = "employeePosition_example"; // String | Employee position
    BigDecimal employeeWeeklyHours = new BigDecimal(78); // BigDecimal | Employee weekly working hours
    try {
      Response result = apiInstance.companyEmployeesPost(employeeEmail, employeeFirstName, employeeLastName, employeeDepartment, employeeGender, employeeHireDate, employeePosition, employeeWeeklyHours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEmployeesPost");
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
| **employeeEmail** | **String**| Employee email | |
| **employeeFirstName** | **String**| Employee first name | |
| **employeeLastName** | **String**| Employee last name | |
| **employeeDepartment** | **String**| Employee department | [optional] |
| **employeeGender** | **String**| Employee gender | [optional] [enum: male, female, diverse] |
| **employeeHireDate** | **LocalDate**| Employee hire date | [optional] |
| **employeePosition** | **String**| Employee position | [optional] |
| **employeeWeeklyHours** | **BigDecimal**| Employee weekly working hours | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful creation of a employee |  -  |

<a id="companyTimeOffTypesGet"></a>
# **companyTimeOffTypesGet**
> CompanyTimeOffTypesGet200Response companyTimeOffTypesGet(limit, offset)



Provides a list of available time-off types, for example &#39;Paid vacation&#39;, &#39;Parental leave&#39; or &#39;Home office&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 200; // Integer | Pagination attribute to limit how many records will be returned per page
    Integer offset = 0; // Integer | Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
    try {
      CompanyTimeOffTypesGet200Response result = apiInstance.companyTimeOffTypesGet(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyTimeOffTypesGet");
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
| **limit** | **Integer**| Pagination attribute to limit how many records will be returned per page | [optional] [default to 200] |
| **offset** | **Integer**| Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned. | [optional] [default to 0] |

### Return type

[**CompanyTimeOffTypesGet200Response**](CompanyTimeOffTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="companyTimeOffsGet"></a>
# **companyTimeOffsGet**
> AbsencePeriodsResponse companyTimeOffsGet(startDate, endDate, updatedFrom, updatedTo, employees, limit, offset)



This endpoint is responsible for fetching absence data for the company employees. It is possible to paginate results, filter by period and/or specific employees. The result will contain a list of absence periods, structured as defined here.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    LocalDate startDate = LocalDate.now(); // LocalDate | First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results
    LocalDate endDate = LocalDate.now(); // LocalDate | Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results.
    String updatedFrom = "updatedFrom_example"; // String | Datetime from when the queried periods have been updated. It is inclusive, so the day specified as updated_from will also be considered on the results.
    String updatedTo = "updatedTo_example"; // String | Datetime until when the queried periods have been updated. It is inclusive, so the day specified as updated_to will also be considered on the results.
    List<Integer> employees = Arrays.asList(); // List<Integer> | A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned.
    Integer limit = 200; // Integer | Pagination attribute to limit how many attendances will be returned per page
    Integer offset = 0; // Integer | Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
    try {
      AbsencePeriodsResponse result = apiInstance.companyTimeOffsGet(startDate, endDate, updatedFrom, updatedTo, employees, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyTimeOffsGet");
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
| **startDate** | **LocalDate**| First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results | [optional] |
| **endDate** | **LocalDate**| Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results. | [optional] |
| **updatedFrom** | **String**| Datetime from when the queried periods have been updated. It is inclusive, so the day specified as updated_from will also be considered on the results. | [optional] |
| **updatedTo** | **String**| Datetime until when the queried periods have been updated. It is inclusive, so the day specified as updated_to will also be considered on the results. | [optional] |
| **employees** | [**List&lt;Integer&gt;**](Integer.md)| A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned. | [optional] |
| **limit** | **Integer**| Pagination attribute to limit how many attendances will be returned per page | [optional] [default to 200] |
| **offset** | **Integer**| Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned. | [optional] [default to 0] |

### Return type

[**AbsencePeriodsResponse**](AbsencePeriodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="companyTimeOffsIdDelete"></a>
# **companyTimeOffsIdDelete**
> Response companyTimeOffsIdDelete(id)



This endpoint is responsible for deleting absence period data for the company employees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer id = 56; // Integer | ID of the absence period to delete
    try {
      Response result = apiInstance.companyTimeOffsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyTimeOffsIdDelete");
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
| **id** | **Integer**| ID of the absence period to delete | |

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response |  -  |
| **404** | Not found response |  -  |

<a id="companyTimeOffsIdGet"></a>
# **companyTimeOffsIdGet**
> Object companyTimeOffsIdGet(id)



Absence Period

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer id = 56; // Integer | Numeric `id` of the absence period
    try {
      Object result = apiInstance.companyTimeOffsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyTimeOffsIdGet");
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
| **id** | **Integer**| Numeric &#x60;id&#x60; of the absence period | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="companyTimeOffsPost"></a>
# **companyTimeOffsPost**
> CompanyTimeOffsPost201Response companyTimeOffsPost(createTimeOffPeriodRequest)



This endpoint is responsible for adding absence data for the company employees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.personio.de/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateTimeOffPeriodRequest createTimeOffPeriodRequest = new CreateTimeOffPeriodRequest(); // CreateTimeOffPeriodRequest | Absence period to create
    try {
      CompanyTimeOffsPost201Response result = apiInstance.companyTimeOffsPost(createTimeOffPeriodRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyTimeOffsPost");
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
| **createTimeOffPeriodRequest** | [**CreateTimeOffPeriodRequest**](CreateTimeOffPeriodRequest.md)| Absence period to create | |

### Return type

[**CompanyTimeOffsPost201Response**](CompanyTimeOffsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The absence period was created successfully |  -  |
| **400** | Invalid request |  -  |
| **404** | Employee or Absence type not found |  -  |
| **422** | Validation error |  -  |

