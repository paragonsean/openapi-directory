# TimesheetApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timesheetDelete**](TimesheetApi.md#timesheetDelete) | **DELETE** /api/Timesheet/{id} | Delete a Timesheet Entry |
| [**timesheetGet**](TimesheetApi.md#timesheetGet) | **GET** /api/Timesheet | Gets list of Timsheets |
| [**timesheetGetByID**](TimesheetApi.md#timesheetGetByID) | **GET** /api/Timesheet/{id} | Gets a Timesheet Entry by Timesheet ID |
| [**timesheetPost**](TimesheetApi.md#timesheetPost) | **POST** /api/Timesheet | Create a new Timesheet Entry |
| [**timesheetPut**](TimesheetApi.md#timesheetPut) | **PUT** /api/Timesheet | Update a Timesheet |


<a id="timesheetDelete"></a>
# **timesheetDelete**
> Object timesheetDelete(id)

Delete a Timesheet Entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetApi apiInstance = new TimesheetApi(defaultClient);
    Long id = 56L; // Long | The id of the timesheet entry to be deleted
    try {
      Object result = apiInstance.timesheetDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetApi#timesheetDelete");
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
| **id** | **Long**| The id of the timesheet entry to be deleted | |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timesheetGet"></a>
# **timesheetGet**
> TimesheetList timesheetGet(updatedAfter, entryDateFrom, entryDateTo, userID, userEmail, categoryName, projectID, isBillable, isInvoiced, isTimerRunning, pageSize, pageNumber, includeInvoiceDetails, sort)

Gets list of Timsheets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetApi apiInstance = new TimesheetApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime entryDateFrom = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime entryDateTo = OffsetDateTime.now(); // OffsetDateTime | 
    Integer userID = 56; // Integer | The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users.
    String userEmail = "userEmail_example"; // String | 
    String categoryName = "categoryName_example"; // String | 
    Integer projectID = 56; // Integer | 
    Boolean isBillable = true; // Boolean | 
    Boolean isInvoiced = true; // Boolean | 
    Boolean isTimerRunning = true; // Boolean | 
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    Boolean includeInvoiceDetails = true; // Boolean | Defaults to false. When true, the InvoiceIDFK value will be included in the response.
    String sort = "sort_example"; // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\",\"EntryDate\", \"EntryDate desc\", \"StartTimeLocal\",\"StartTimeLocal desc\", \"TimeSheetEntryID\", \"TimeSheetEntryID desc\"
    try {
      TimesheetList result = apiInstance.timesheetGet(updatedAfter, entryDateFrom, entryDateTo, userID, userEmail, categoryName, projectID, isBillable, isInvoiced, isTimerRunning, pageSize, pageNumber, includeInvoiceDetails, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetApi#timesheetGet");
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
| **updatedAfter** | **OffsetDateTime**|  | [optional] |
| **entryDateFrom** | **OffsetDateTime**|  | [optional] |
| **entryDateTo** | **OffsetDateTime**|  | [optional] |
| **userID** | **Integer**| The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users. | [optional] |
| **userEmail** | **String**|  | [optional] |
| **categoryName** | **String**|  | [optional] |
| **projectID** | **Integer**|  | [optional] |
| **isBillable** | **Boolean**|  | [optional] |
| **isInvoiced** | **Boolean**|  | [optional] |
| **isTimerRunning** | **Boolean**|  | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **includeInvoiceDetails** | **Boolean**| Defaults to false. When true, the InvoiceIDFK value will be included in the response. | [optional] |
| **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot; | [optional] |

### Return type

[**TimesheetList**](TimesheetList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="timesheetGetByID"></a>
# **timesheetGetByID**
> TimesheetDetails timesheetGetByID(id)

Gets a Timesheet Entry by Timesheet ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetApi apiInstance = new TimesheetApi(defaultClient);
    Long id = 56L; // Long | Timesheet ID number
    try {
      TimesheetDetails result = apiInstance.timesheetGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetApi#timesheetGetByID");
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
| **id** | **Long**| Timesheet ID number | |

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="timesheetPost"></a>
# **timesheetPost**
> TimesheetDetails timesheetPost(model)

Create a new Timesheet Entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetApi apiInstance = new TimesheetApi(defaultClient);
    NewTimesheet model = new NewTimesheet(); // NewTimesheet | 
    try {
      TimesheetDetails result = apiInstance.timesheetPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetApi#timesheetPost");
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
| **model** | [**NewTimesheet**](NewTimesheet.md)|  | |

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timesheetPut"></a>
# **timesheetPut**
> TimesheetDetails timesheetPut(model)

Update a Timesheet

The FieldsToUpdate field expects a string array collection of the field names you would like updated. Valid fields to update inlcude \&quot;ProjectIDFK\&quot;, \&quot;TimeSheetCategoryIDFK\&quot;, \&quot;TaskIDFK\&quot;, \&quot;Duration\&quot;, \&quot;EntryDate\&quot;, \&quot;Notes\&quot;, \&quot;hasStartEndTime\&quot;, \&quot;CustomMetadata\&quot;. If you intend to provide start/end times on timesheets, this is achieved by including the start time in the EntryDate field (Iso date format), along with a Duration (decimal format).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetApi apiInstance = new TimesheetApi(defaultClient);
    UpdateTimesheetModel model = new UpdateTimesheetModel(); // UpdateTimesheetModel | 
    try {
      TimesheetDetails result = apiInstance.timesheetPut(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetApi#timesheetPut");
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
| **model** | [**UpdateTimesheetModel**](UpdateTimesheetModel.md)|  | |

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

