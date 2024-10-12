# DatesApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarDatesExportGet**](DatesApi.md#calendarDatesExportGet) | **GET** /calendar-dates/export/ |  |
| [**calendarDatesGet**](DatesApi.md#calendarDatesGet) | **GET** /calendar-dates/ |  |
| [**electionDatesGet**](DatesApi.md#electionDatesGet) | **GET** /election-dates/ |  |
| [**reportingDatesGet**](DatesApi.md#reportingDatesGet) | **GET** /reporting-dates/ |  |


<a id="calendarDatesExportGet"></a>
# **calendarDatesExportGet**
> CalendarDatePage calendarDatesExportGet(apiKey, calendarCategoryId, description, sortNullsLast, sortNullOnly, page, maxEndDate, summary, minEndDate, sortHideNull, minStartDate, perPage, maxStartDate, renderer, sort, eventId)



 Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State filtering now applies to elections, reports and reporting periods.  Presidential pre-primary report due dates are not shown on even years. Filers generally opt to file monthly rather than submit over 50 pre-primary election reports. All reporting deadlines are available at /reporting-dates/ for reference.  This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql) that creates the calendar.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DatesApi apiInstance = new DatesApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> calendarCategoryId = Arrays.asList(); // List<Integer> |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
    List<String> description = Arrays.asList(); // List<String> | Brief description of event
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    LocalDate maxEndDate = LocalDate.now(); // LocalDate |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    List<String> summary = Arrays.asList(); // List<String> | Longer description of event
    LocalDate minEndDate = LocalDate.now(); // LocalDate |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    LocalDate minStartDate = LocalDate.now(); // LocalDate |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    LocalDate maxStartDate = LocalDate.now(); // LocalDate |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    String renderer = "ics"; // String | 
    String sort = "-start_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Integer eventId = 56; // Integer | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
    try {
      CalendarDatePage result = apiInstance.calendarDatesExportGet(apiKey, calendarCategoryId, description, sortNullsLast, sortNullOnly, page, maxEndDate, summary, minEndDate, sortHideNull, minStartDate, perPage, maxStartDate, renderer, sort, eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatesApi#calendarDatesExportGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **calendarCategoryId** | [**List&lt;Integer&gt;**](Integer.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] |
| **description** | [**List&lt;String&gt;**](String.md)| Brief description of event | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **maxEndDate** | **LocalDate**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **summary** | [**List&lt;String&gt;**](String.md)| Longer description of event | [optional] |
| **minEndDate** | **LocalDate**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **minStartDate** | **LocalDate**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **maxStartDate** | **LocalDate**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **renderer** | **String**|  | [optional] [default to ics] [enum: ics, csv] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -start_date] |
| **eventId** | **Integer**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] |

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="calendarDatesGet"></a>
# **calendarDatesGet**
> CalendarDatePage calendarDatesGet(apiKey, calendarCategoryId, description, sortNullsLast, sortNullOnly, page, maxEndDate, summary, minEndDate, sortHideNull, minStartDate, maxStartDate, perPage, sort, eventId)



 Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State and report type filtering is no longer available. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DatesApi apiInstance = new DatesApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> calendarCategoryId = Arrays.asList(); // List<Integer> |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
    List<String> description = Arrays.asList(); // List<String> | Brief description of event
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    LocalDate maxEndDate = LocalDate.now(); // LocalDate |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    List<String> summary = Arrays.asList(); // List<String> | Longer description of event
    LocalDate minEndDate = LocalDate.now(); // LocalDate |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    LocalDate minStartDate = LocalDate.now(); // LocalDate |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    LocalDate maxStartDate = LocalDate.now(); // LocalDate |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-start_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Integer eventId = 56; // Integer | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
    try {
      CalendarDatePage result = apiInstance.calendarDatesGet(apiKey, calendarCategoryId, description, sortNullsLast, sortNullOnly, page, maxEndDate, summary, minEndDate, sortHideNull, minStartDate, maxStartDate, perPage, sort, eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatesApi#calendarDatesGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **calendarCategoryId** | [**List&lt;Integer&gt;**](Integer.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] |
| **description** | [**List&lt;String&gt;**](String.md)| Brief description of event | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **maxEndDate** | **LocalDate**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **summary** | [**List&lt;String&gt;**](String.md)| Longer description of event | [optional] |
| **minEndDate** | **LocalDate**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **minStartDate** | **LocalDate**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **maxStartDate** | **LocalDate**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -start_date] |
| **eventId** | **Integer**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] |

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="electionDatesGet"></a>
# **electionDatesGet**
> ElectionDatesGetDefaultResponse electionDatesGet(apiKey, electionState, maxElectionDate, electionDistrict, minUpdateDate, sortNullOnly, sortHideNull, maxCreateDate, perPage, electionYear, sort, minCreateDate, electionParty, officeSought, sortNullsLast, page, maxUpdateDate, electionTypeId, maxPrimaryGeneralDate, minElectionDate, minPrimaryGeneralDate)



 FEC election dates since 1995. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DatesApi apiInstance = new DatesApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> electionState = Arrays.asList(); // List<String> |  State or territory of the office sought. 
    LocalDate maxElectionDate = LocalDate.now(); // LocalDate |  The maximum date of election. 
    List<String> electionDistrict = Arrays.asList(); // List<String> |  House district of the office sought, if applicable. 
    LocalDate minUpdateDate = LocalDate.now(); // LocalDate |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    LocalDate maxCreateDate = LocalDate.now(); // LocalDate |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> electionYear = Arrays.asList(); // List<String> | Year of election
    String sort = "-election_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    LocalDate minCreateDate = LocalDate.now(); // LocalDate |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    List<String> electionParty = Arrays.asList(); // List<String> |  Party, if applicable. 
    List<String> officeSought = Arrays.asList(); // List<String> |  House, Senate or presidential office. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    LocalDate maxUpdateDate = LocalDate.now(); // LocalDate |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    List<String> electionTypeId = Arrays.asList(); // List<String> |  Election type id 
    LocalDate maxPrimaryGeneralDate = LocalDate.now(); // LocalDate |  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
    LocalDate minElectionDate = LocalDate.now(); // LocalDate |  The minimum date of election. 
    LocalDate minPrimaryGeneralDate = LocalDate.now(); // LocalDate |  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
    try {
      ElectionDatesGetDefaultResponse result = apiInstance.electionDatesGet(apiKey, electionState, maxElectionDate, electionDistrict, minUpdateDate, sortNullOnly, sortHideNull, maxCreateDate, perPage, electionYear, sort, minCreateDate, electionParty, officeSought, sortNullsLast, page, maxUpdateDate, electionTypeId, maxPrimaryGeneralDate, minElectionDate, minPrimaryGeneralDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatesApi#electionDatesGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **electionState** | [**List&lt;String&gt;**](String.md)|  State or territory of the office sought.  | [optional] |
| **maxElectionDate** | **LocalDate**|  The maximum date of election.  | [optional] |
| **electionDistrict** | [**List&lt;String&gt;**](String.md)|  House district of the office sought, if applicable.  | [optional] |
| **minUpdateDate** | **LocalDate**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **maxCreateDate** | **LocalDate**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;String&gt;**](String.md)| Year of election | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -election_date] |
| **minCreateDate** | **LocalDate**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **electionParty** | [**List&lt;String&gt;**](String.md)|  Party, if applicable.  | [optional] |
| **officeSought** | [**List&lt;String&gt;**](String.md)|  House, Senate or presidential office.  | [optional] [enum: H, S, P] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **maxUpdateDate** | **LocalDate**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **electionTypeId** | [**List&lt;String&gt;**](String.md)|  Election type id  | [optional] |
| **maxPrimaryGeneralDate** | **LocalDate**|  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **minElectionDate** | **LocalDate**|  The minimum date of election.  | [optional] |
| **minPrimaryGeneralDate** | **LocalDate**|  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |

### Return type

[**ElectionDatesGetDefaultResponse**](ElectionDatesGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="reportingDatesGet"></a>
# **reportingDatesGet**
> ReportingDatesGetDefaultResponse reportingDatesGet(apiKey, minUpdateDate, reportType, minDueDate, sortNullOnly, page, maxDueDate, reportYear, sortNullsLast, maxCreateDate, maxUpdateDate, perPage, sortHideNull, sort, minCreateDate)



 FEC election dates since 1995. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DatesApi apiInstance = new DatesApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minUpdateDate = LocalDate.now(); // LocalDate |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    List<String> reportType = Arrays.asList(); // List<String> | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
    LocalDate minDueDate = LocalDate.now(); // LocalDate |  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    LocalDate maxDueDate = LocalDate.now(); // LocalDate |  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
    List<Integer> reportYear = Arrays.asList(); // List<Integer> |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    LocalDate maxCreateDate = LocalDate.now(); // LocalDate |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    LocalDate maxUpdateDate = LocalDate.now(); // LocalDate |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    String sort = "-due_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    LocalDate minCreateDate = LocalDate.now(); // LocalDate |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
    try {
      ReportingDatesGetDefaultResponse result = apiInstance.reportingDatesGet(apiKey, minUpdateDate, reportType, minDueDate, sortNullOnly, page, maxDueDate, reportYear, sortNullsLast, maxCreateDate, maxUpdateDate, perPage, sortHideNull, sort, minCreateDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatesApi#reportingDatesGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **minUpdateDate** | **LocalDate**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **reportType** | [**List&lt;String&gt;**](String.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] |
| **minDueDate** | **LocalDate**|  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **maxDueDate** | **LocalDate**|  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **reportYear** | [**List&lt;Integer&gt;**](Integer.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **maxCreateDate** | **LocalDate**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **maxUpdateDate** | **LocalDate**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -due_date] |
| **minCreateDate** | **LocalDate**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |

### Return type

[**ReportingDatesGetDefaultResponse**](ReportingDatesGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

