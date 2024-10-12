# HoursReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntriesGetTimeEntries**](HoursReadApi.md#timeEntriesGetTimeEntries) | **GET** /v1/timeentries | Get the time entries. |
| [**timeEntriesGetTimeEntriesForUser**](HoursReadApi.md#timeEntriesGetTimeEntriesForUser) | **GET** /v1/users/{userGuid}/timeentries | Get all the time entries for a user. |
| [**timeEntriesGetTimeEntry**](HoursReadApi.md#timeEntriesGetTimeEntry) | **GET** /v1/timeentries/{guid} | Get time entry by ID. |
| [**workHoursGetDeletedWorkHours**](HoursReadApi.md#workHoursGetDeletedWorkHours) | **GET** /v1/deletedworkhours | Get the deleted work hours. |
| [**workHoursGetProjectWorkHours**](HoursReadApi.md#workHoursGetProjectWorkHours) | **GET** /v1/projects/{projectGuid}/workhours | Get all the work hours for phases of a project for invoicing |
| [**workHoursGetWorkHour**](HoursReadApi.md#workHoursGetWorkHour) | **GET** /v1/workhours/{guid} | Get work hour by ID |
| [**workHoursGetWorkHours**](HoursReadApi.md#workHoursGetWorkHours) | **GET** /v1/workhours | Get the work hours. |
| [**workHoursGetWorkHoursForUser**](HoursReadApi.md#workHoursGetWorkHoursForUser) | **GET** /v1/users/{userGuid}/workhours | Get all the work hours for a user |


<a id="timeEntriesGetTimeEntries"></a>
# **timeEntriesGetTimeEntries**
> List&lt;TimeEntryModel&gt; timeEntriesGetTimeEntries(firstRow, phaseGuid, timeEntryTypeGuid, rowCount, changedSince)

Get the time entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    List<String> phaseGuid = Arrays.asList(); // List<String> | Optional: Filters time entries for given phases.
    List<String> timeEntryTypeGuid = Arrays.asList(); // List<String> | Optional: Filters time entries for given time entry types.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get time entries that have been added or changed after this date time (greater or equal).
    try {
      List<TimeEntryModel> result = apiInstance.timeEntriesGetTimeEntries(firstRow, phaseGuid, timeEntryTypeGuid, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#timeEntriesGetTimeEntries");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **phaseGuid** | [**List&lt;String&gt;**](String.md)| Optional: Filters time entries for given phases. | [optional] |
| **timeEntryTypeGuid** | [**List&lt;String&gt;**](String.md)| Optional: Filters time entries for given time entry types. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get time entries that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;TimeEntryModel&gt;**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timeEntriesGetTimeEntriesForUser"></a>
# **timeEntriesGetTimeEntriesForUser**
> List&lt;TimeEntryModel&gt; timeEntriesGetTimeEntriesForUser(userGuid, startDate, endDate, phaseGuid, timeEntryTypeGuid, firstRow, rowCount)

Get all the time entries for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date from which to get the time entries. Default all.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date to which to get the time entries. Default all.
    List<String> phaseGuid = Arrays.asList(); // List<String> | Optional: Filters time entries for given phases.
    List<String> timeEntryTypeGuid = Arrays.asList(); // List<String> | Optional: Filters time entries for given time entry types.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<TimeEntryModel> result = apiInstance.timeEntriesGetTimeEntriesForUser(userGuid, startDate, endDate, phaseGuid, timeEntryTypeGuid, firstRow, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#timeEntriesGetTimeEntriesForUser");
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
| **userGuid** | **String**| ID of the user. | |
| **startDate** | **OffsetDateTime**| Optional: starting date from which to get the time entries. Default all. | [optional] |
| **endDate** | **OffsetDateTime**| Optional: starting date to which to get the time entries. Default all. | [optional] |
| **phaseGuid** | [**List&lt;String&gt;**](String.md)| Optional: Filters time entries for given phases. | [optional] |
| **timeEntryTypeGuid** | [**List&lt;String&gt;**](String.md)| Optional: Filters time entries for given time entry types. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;TimeEntryModel&gt;**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TimeEntries. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timeEntriesGetTimeEntry"></a>
# **timeEntriesGetTimeEntry**
> TimeEntryModel timeEntriesGetTimeEntry(guid)

Get time entry by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the time entry.
    try {
      TimeEntryModel result = apiInstance.timeEntriesGetTimeEntry(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#timeEntriesGetTimeEntry");
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
| **guid** | **String**| Id used to get the time entry. | |

### Return type

[**TimeEntryModel**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetDeletedWorkHours"></a>
# **workHoursGetDeletedWorkHours**
> List&lt;DeletedWorkHourModel&gt; workHoursGetDeletedWorkHours(pageToken, rowCount, projectGuids, userGuids, deletedSince)

Get the deleted work hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    List<String> projectGuids = Arrays.asList(); // List<String> | Optional: ID of the project for the deleted work hours to be fetched. If not provided, returns for all projects. Default all.
    List<String> userGuids = Arrays.asList(); // List<String> | Optional: ID of the user. If not provided, returns for all users. Default all.
    OffsetDateTime deletedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get work hours that have been deleted after this date time (greater or equal).
    try {
      List<DeletedWorkHourModel> result = apiInstance.workHoursGetDeletedWorkHours(pageToken, rowCount, projectGuids, userGuids, deletedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#workHoursGetDeletedWorkHours");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project for the deleted work hours to be fetched. If not provided, returns for all projects. Default all. | [optional] |
| **userGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the user. If not provided, returns for all users. Default all. | [optional] |
| **deletedSince** | **OffsetDateTime**| Optional: Get work hours that have been deleted after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;DeletedWorkHourModel&gt;**](DeletedWorkHourModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetProjectWorkHours"></a>
# **workHoursGetProjectWorkHours**
> List&lt;WorkHourOutputModel&gt; workHoursGetProjectWorkHours(projectGuid, isBillable, isBilled, startDate, endDate, pageToken, rowCount)

Get all the work hours for phases of a project for invoicing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    Boolean isBillable = true; // Boolean | Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    Boolean isBilled = true; // Boolean | Optional: Filter the work hours. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date from which to get the hours. Default all.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date to which to get the hours. Default all.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursGetProjectWorkHours(projectGuid, isBillable, isBilled, startDate, endDate, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#workHoursGetProjectWorkHours");
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
| **projectGuid** | **String**| ID of the project. | |
| **isBillable** | **Boolean**| Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |
| **isBilled** | **Boolean**| Optional: Filter the work hours. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] |
| **startDate** | **OffsetDateTime**| Optional: starting date from which to get the hours. Default all. | [optional] |
| **endDate** | **OffsetDateTime**| Optional: starting date to which to get the hours. Default all. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WorkHours |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetWorkHour"></a>
# **workHoursGetWorkHour**
> WorkHourOutputModel workHoursGetWorkHour(guid)

Get work hour by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the work hour.
    try {
      WorkHourOutputModel result = apiInstance.workHoursGetWorkHour(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#workHoursGetWorkHour");
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
| **guid** | **String**| Id used to get the work hour. | |

### Return type

[**WorkHourOutputModel**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetWorkHours"></a>
# **workHoursGetWorkHours**
> List&lt;WorkHourOutputModel&gt; workHoursGetWorkHours(pageToken, rowCount, changedSince, billableStatus, eventDateStart, eventDateEnd)

Get the work hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get work hours that have been added or changed after this date time (greater or equal).
    BillableStatusType billableStatus = BillableStatusType.fromValue("Billable"); // BillableStatusType | Billable status type
    LocalDate eventDateStart = LocalDate.now(); // LocalDate | Optional: Get work hours that have event date after this date time (greater or equal).
    LocalDate eventDateEnd = LocalDate.now(); // LocalDate | Optional: Get work hours that have event date before this date time (less or equal).
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursGetWorkHours(pageToken, rowCount, changedSince, billableStatus, eventDateStart, eventDateEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#workHoursGetWorkHours");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get work hours that have been added or changed after this date time (greater or equal). | [optional] |
| **billableStatus** | [**BillableStatusType**](.md)| Billable status type | [optional] [enum: Billable, NotBillable, RemovedFromInvoice] |
| **eventDateStart** | **LocalDate**| Optional: Get work hours that have event date after this date time (greater or equal). | [optional] |
| **eventDateEnd** | **LocalDate**| Optional: Get work hours that have event date before this date time (less or equal). | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetWorkHoursForUser"></a>
# **workHoursGetWorkHoursForUser**
> List&lt;WorkHourOutputModel&gt; workHoursGetWorkHoursForUser(userGuid, startDate, endDate, phaseGuid, workTypeGuid, pageToken, rowCount)

Get all the work hours for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursReadApi apiInstance = new HoursReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date from which to get the hours. Default all.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date to which to get the hours. Default all.
    List<String> phaseGuid = Arrays.asList(); // List<String> | Optional: ID of the phase to get the hours for. Default all.
    List<String> workTypeGuid = Arrays.asList(); // List<String> | Optional: ID of the work type. Default all.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursGetWorkHoursForUser(userGuid, startDate, endDate, phaseGuid, workTypeGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursReadApi#workHoursGetWorkHoursForUser");
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
| **userGuid** | **String**| ID of the user. | |
| **startDate** | **OffsetDateTime**| Optional: starting date from which to get the hours. Default all. | [optional] |
| **endDate** | **OffsetDateTime**| Optional: starting date to which to get the hours. Default all. | [optional] |
| **phaseGuid** | [**List&lt;String&gt;**](String.md)| Optional: ID of the phase to get the hours for. Default all. | [optional] |
| **workTypeGuid** | [**List&lt;String&gt;**](String.md)| Optional: ID of the work type. Default all. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WorkHours |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

