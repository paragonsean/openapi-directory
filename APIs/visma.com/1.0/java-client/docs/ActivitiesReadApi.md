# ActivitiesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activitiesGetActivities**](ActivitiesReadApi.md#activitiesGetActivities) | **GET** /v1/activities | Get all activities of an organization |
| [**activitiesGetActivity**](ActivitiesReadApi.md#activitiesGetActivity) | **GET** /v1/activities/{guid} | Get activity by ID |
| [**activityParticipantsGetActivityParticipant**](ActivitiesReadApi.md#activityParticipantsGetActivityParticipant) | **GET** /v1/activityparticipants/{guid} | Get activity participant |
| [**activityParticipantsGetActivityParticipants**](ActivitiesReadApi.md#activityParticipantsGetActivityParticipants) | **GET** /v1/activities/{activityGuid}/activityparticipants | Get participants for an activity |


<a id="activitiesGetActivities"></a>
# **activitiesGetActivities**
> List&lt;ActivityModel&gt; activitiesGetActivities(pageToken, rowCount, closed, activityCategories, customerGuids, includeTasksWithNoCustomer, projectGuids, includeTasksWithNoProject, projectBusinessUnitGuids, projectOwnerGuids, userGuids, includeAsMember, userKeywordGuids, startDateTime, endDateTime, projectTaskStatusGuids, phaseGuids, includeSubPhases, contactGuids, hasDuration, hasHours, isUnassigned, changedSince, useStrictStartAndEndDateTime, activityTypeGuids, recurrenceType)

Get all activities of an organization

Start and end date times accept values of DateTimeOffset type, based on UTF-8 encoding.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesReadApi;

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

    ActivitiesReadApi apiInstance = new ActivitiesReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean closed = true; // Boolean | Optional: Which activities to fetch - open/closed, Default all.
    List<ActivityCategory> activityCategories = Arrays.asList(); // List<ActivityCategory> | Optional: activity category for the activities to be fetched. Should be one of Personal/Absences/CalendarEntry/SalesEvent/Task. Default all.
    List<String> customerGuids = Arrays.asList(); // List<String> | Optional: ID of customer. Default all.
    Boolean includeTasksWithNoCustomer = true; // Boolean | Optional: Include the activities that don't have customer. Default is true.
    List<String> projectGuids = Arrays.asList(); // List<String> | Optional: ID of the project for the activities to be fetched. If not provided, returns for all projects. Default all.
    Boolean includeTasksWithNoProject = true; // Boolean | Optional: Include the activities that don't have project. Default is true.
    List<String> projectBusinessUnitGuids = Arrays.asList(); // List<String> | Optional: ID of the business unit of the project based on which activities should be filtered. If not provided, returns for all business units. Default all.
    List<String> projectOwnerGuids = Arrays.asList(); // List<String> | Optional: ID of the project manager. If not provided, returns for all project managers. Default all.
    List<String> userGuids = Arrays.asList(); // List<String> | Optional: ID of the user for the activities to be fetched. If not provided, returns for all users. Default all.
    Boolean includeAsMember = false; // Boolean | Optional: Include the activities that the user is a member. Effective if userGuid is provided. Default is to not include.
    List<String> userKeywordGuids = Arrays.asList(); // List<String> | Optional: User keyword Ids of activity owner to search for.
    OffsetDateTime startDateTime = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date and time from which to get the activities in user's timezone. Finds all activities that end after the date time. Format \"2017-04-12T13%3A20%3A00%2b02%3A00\". Default all.
    OffsetDateTime endDateTime = OffsetDateTime.now(); // OffsetDateTime | Optional: ending date and time to which to get the activities in user's timezone. Finds all activities that start before or on the date time. Format \"2017-04-12T13%3A20%3A00%2b02%3A00\". Default all. If activities for one day are fetched, give start date time with time as 00:00 with the offset of the timezone and end time as 23:59:59 with the offset.
    List<String> projectTaskStatusGuids = Arrays.asList(); // List<String> | Optional: ID of the project task status. Default all.
    List<String> phaseGuids = Arrays.asList(); // List<String> | Optional: ID of the phase for the activities to be fetched. If not provided, returns for all phases. Default all.
    Boolean includeSubPhases = false; // Boolean | Optional: If one phase guid is given include activities also from sub phases. If multiple phase guids are given, returns activities only for those regardless of this parameter. Default false.
    List<String> contactGuids = Arrays.asList(); // List<String> | Optional: ID of the contact for the activities to be fetched. If not provided, returns for all users. Default all.
    Boolean hasDuration = true; // Boolean | Optional: has duration flag for the activity. Default all.
    Boolean hasHours = true; // Boolean | Optional: has any work hour entries associated with the activity. Default all.
    Boolean isUnassigned = true; // Boolean | Optional: is the activity unassigned. Default all.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get activities that have been added or changed after this date time (greater or equal).
    Boolean useStrictStartAndEndDateTime = false; // Boolean | Optional: If given as true returns activities that start after start time and end before end time. If given as false returns activities that start before end time and end after start time. Limit are included in both cases. Default false.
    List<String> activityTypeGuids = Arrays.asList(); // List<String> | Optional: ID of the project activity type. Default all.
    RecurrenceType recurrenceType = RecurrenceType.fromValue("None"); // RecurrenceType | Optional: Type of the recurrence. Default returns all not recurring activities, instances and exceptions. (None = not recurring activity)
    try {
      List<ActivityModel> result = apiInstance.activitiesGetActivities(pageToken, rowCount, closed, activityCategories, customerGuids, includeTasksWithNoCustomer, projectGuids, includeTasksWithNoProject, projectBusinessUnitGuids, projectOwnerGuids, userGuids, includeAsMember, userKeywordGuids, startDateTime, endDateTime, projectTaskStatusGuids, phaseGuids, includeSubPhases, contactGuids, hasDuration, hasHours, isUnassigned, changedSince, useStrictStartAndEndDateTime, activityTypeGuids, recurrenceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesReadApi#activitiesGetActivities");
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
| **closed** | **Boolean**| Optional: Which activities to fetch - open/closed, Default all. | [optional] |
| **activityCategories** | [**List&lt;ActivityCategory&gt;**](ActivityCategory.md)| Optional: activity category for the activities to be fetched. Should be one of Personal/Absences/CalendarEntry/SalesEvent/Task. Default all. | [optional] |
| **customerGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of customer. Default all. | [optional] |
| **includeTasksWithNoCustomer** | **Boolean**| Optional: Include the activities that don&#39;t have customer. Default is true. | [optional] [default to true] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project for the activities to be fetched. If not provided, returns for all projects. Default all. | [optional] |
| **includeTasksWithNoProject** | **Boolean**| Optional: Include the activities that don&#39;t have project. Default is true. | [optional] [default to true] |
| **projectBusinessUnitGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the business unit of the project based on which activities should be filtered. If not provided, returns for all business units. Default all. | [optional] |
| **projectOwnerGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project manager. If not provided, returns for all project managers. Default all. | [optional] |
| **userGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the user for the activities to be fetched. If not provided, returns for all users. Default all. | [optional] |
| **includeAsMember** | **Boolean**| Optional: Include the activities that the user is a member. Effective if userGuid is provided. Default is to not include. | [optional] [default to false] |
| **userKeywordGuids** | [**List&lt;String&gt;**](String.md)| Optional: User keyword Ids of activity owner to search for. | [optional] |
| **startDateTime** | **OffsetDateTime**| Optional: starting date and time from which to get the activities in user&#39;s timezone. Finds all activities that end after the date time. Format \&quot;2017-04-12T13%3A20%3A00%2b02%3A00\&quot;. Default all. | [optional] |
| **endDateTime** | **OffsetDateTime**| Optional: ending date and time to which to get the activities in user&#39;s timezone. Finds all activities that start before or on the date time. Format \&quot;2017-04-12T13%3A20%3A00%2b02%3A00\&quot;. Default all. If activities for one day are fetched, give start date time with time as 00:00 with the offset of the timezone and end time as 23:59:59 with the offset. | [optional] |
| **projectTaskStatusGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project task status. Default all. | [optional] |
| **phaseGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the phase for the activities to be fetched. If not provided, returns for all phases. Default all. | [optional] |
| **includeSubPhases** | **Boolean**| Optional: If one phase guid is given include activities also from sub phases. If multiple phase guids are given, returns activities only for those regardless of this parameter. Default false. | [optional] [default to false] |
| **contactGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the contact for the activities to be fetched. If not provided, returns for all users. Default all. | [optional] |
| **hasDuration** | **Boolean**| Optional: has duration flag for the activity. Default all. | [optional] |
| **hasHours** | **Boolean**| Optional: has any work hour entries associated with the activity. Default all. | [optional] |
| **isUnassigned** | **Boolean**| Optional: is the activity unassigned. Default all. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get activities that have been added or changed after this date time (greater or equal). | [optional] |
| **useStrictStartAndEndDateTime** | **Boolean**| Optional: If given as true returns activities that start after start time and end before end time. If given as false returns activities that start before end time and end after start time. Limit are included in both cases. Default false. | [optional] [default to false] |
| **activityTypeGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project activity type. Default all. | [optional] |
| **recurrenceType** | [**RecurrenceType**](.md)| Optional: Type of the recurrence. Default returns all not recurring activities, instances and exceptions. (None &#x3D; not recurring activity) | [optional] [enum: None, Occurrence, Exception, Series] |

### Return type

[**List&lt;ActivityModel&gt;**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activities for a project |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activitiesGetActivity"></a>
# **activitiesGetActivity**
> ActivityModel activitiesGetActivity(guid)

Get activity by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesReadApi;

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

    ActivitiesReadApi apiInstance = new ActivitiesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the activity.
    try {
      ActivityModel result = apiInstance.activitiesGetActivity(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesReadApi#activitiesGetActivity");
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
| **guid** | **String**| GUID used to get the activity. | |

### Return type

[**ActivityModel**](ActivityModel.md)

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

<a id="activityParticipantsGetActivityParticipant"></a>
# **activityParticipantsGetActivityParticipant**
> ActivityParticipantModel activityParticipantsGetActivityParticipant(guid)

Get activity participant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesReadApi;

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

    ActivitiesReadApi apiInstance = new ActivitiesReadApi(defaultClient);
    String guid = "guid_example"; // String | ID of the participant
    try {
      ActivityParticipantModel result = apiInstance.activityParticipantsGetActivityParticipant(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesReadApi#activityParticipantsGetActivityParticipant");
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
| **guid** | **String**| ID of the participant | |

### Return type

[**ActivityParticipantModel**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ActivityParticipant |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activityParticipantsGetActivityParticipants"></a>
# **activityParticipantsGetActivityParticipants**
> List&lt;ActivityParticipantModel&gt; activityParticipantsGetActivityParticipants(activityGuid)

Get participants for an activity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesReadApi;

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

    ActivitiesReadApi apiInstance = new ActivitiesReadApi(defaultClient);
    String activityGuid = "activityGuid_example"; // String | ID of the activity
    try {
      List<ActivityParticipantModel> result = apiInstance.activityParticipantsGetActivityParticipants(activityGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesReadApi#activityParticipantsGetActivityParticipants");
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
| **activityGuid** | **String**| ID of the activity | |

### Return type

[**List&lt;ActivityParticipantModel&gt;**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ActivityParticipants for an activity |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

