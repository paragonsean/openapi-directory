# GroupsApi

All URIs are relative to *https://api.citrixonline.com/G2M/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups | Get groups |
| [**groupsGroupKeyAttendeesGet**](GroupsApi.md#groupsGroupKeyAttendeesGet) | **GET** /groups/{groupKey}/attendees | Get attendees by group |
| [**groupsGroupKeyHistoricalMeetingsGet**](GroupsApi.md#groupsGroupKeyHistoricalMeetingsGet) | **GET** /groups/{groupKey}/historicalMeetings | Get historical meetings by group |
| [**groupsGroupKeyMeetingsGet**](GroupsApi.md#groupsGroupKeyMeetingsGet) | **GET** /groups/{groupKey}/meetings | DEPRECATED: Get historical meetings by group |
| [**groupsGroupKeyOrganizersGet**](GroupsApi.md#groupsGroupKeyOrganizersGet) | **GET** /groups/{groupKey}/organizers | Get organizers by group |
| [**groupsGroupKeyOrganizersPost**](GroupsApi.md#groupsGroupKeyOrganizersPost) | **POST** /groups/{groupKey}/organizers | Create organizer in group |
| [**groupsGroupKeyUpcomingMeetingsGet**](GroupsApi.md#groupsGroupKeyUpcomingMeetingsGet) | **GET** /groups/{groupKey}/upcomingMeetings | Get upcoming meetings by group |


<a id="groupsGet"></a>
# **groupsGet**
> List&lt;Group&gt; groupsGet(authorization)

Get groups

List all groups for an account. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    try {
      List<Group> result = apiInstance.groupsGet(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGet");
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
| **authorization** | **String**| Access token | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |

<a id="groupsGroupKeyAttendeesGet"></a>
# **groupsGroupKeyAttendeesGet**
> List&lt;AttendeeByGroup&gt; groupsGroupKeyAttendeesGet(authorization, groupKey, startDate, endDate)

Get attendees by group

Returns all attendees for all meetings within specified date range held by organizers within the specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long groupKey = 56L; // Long | The key of the group
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | End of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<AttendeeByGroup> result = apiInstance.groupsGroupKeyAttendeesGet(authorization, groupKey, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGroupKeyAttendeesGet");
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
| **authorization** | **String**| Access token | |
| **groupKey** | **Long**| The key of the group | |
| **startDate** | **OffsetDateTime**| Start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | [optional] |
| **endDate** | **OffsetDateTime**| End of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | [optional] |

### Return type

[**List&lt;AttendeeByGroup&gt;**](AttendeeByGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="groupsGroupKeyHistoricalMeetingsGet"></a>
# **groupsGroupKeyHistoricalMeetingsGet**
> List&lt;HistoricalMeetingByGroup&gt; groupsGroupKeyHistoricalMeetingsGet(authorization, groupKey, startDate, endDate)

Get historical meetings by group

Get historical meetings for the specified group that started within the specified date/time range. This API call is only available to users with the admin role. This API call is restricted to groups with a maximum of 50 organizers. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long groupKey = 56L; // Long | The key of the group
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<HistoricalMeetingByGroup> result = apiInstance.groupsGroupKeyHistoricalMeetingsGet(authorization, groupKey, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGroupKeyHistoricalMeetingsGet");
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
| **authorization** | **String**| Access token | |
| **groupKey** | **Long**| The key of the group | |
| **startDate** | **OffsetDateTime**| Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | |
| **endDate** | **OffsetDateTime**| Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | |

### Return type

[**List&lt;HistoricalMeetingByGroup&gt;**](HistoricalMeetingByGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsGroupKeyMeetingsGet"></a>
# **groupsGroupKeyMeetingsGet**
> List&lt;HistoryMeetingByGroup&gt; groupsGroupKeyMeetingsGet(authorization, groupKey, history, startDate, endDate)

DEPRECATED: Get historical meetings by group

DEPRECATED: Please use the new API calls &#39;Get historical meetings by group&#39; and &#39;Get upcoming meetings by group&#39;. Get meetings for a specified group. Additional filters can be used to view only meetings within a specified date range. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long groupKey = 56L; // Long | The key of the group
    Boolean history = true; // Boolean | When 'true', returns all past meetings within date range
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | If history=true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | If history=true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<HistoryMeetingByGroup> result = apiInstance.groupsGroupKeyMeetingsGet(authorization, groupKey, history, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGroupKeyMeetingsGet");
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
| **authorization** | **String**| Access token | |
| **groupKey** | **Long**| The key of the group | |
| **history** | **Boolean**| When &#39;true&#39;, returns all past meetings within date range | |
| **startDate** | **OffsetDateTime**| If history&#x3D;true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | |
| **endDate** | **OffsetDateTime**| If history&#x3D;true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | |

### Return type

[**List&lt;HistoryMeetingByGroup&gt;**](HistoryMeetingByGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="groupsGroupKeyOrganizersGet"></a>
# **groupsGroupKeyOrganizersGet**
> List&lt;OrganizerByGroup&gt; groupsGroupKeyOrganizersGet(authorization, groupKey)

Get organizers by group

Returns all the organizers within a specific group. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long groupKey = 56L; // Long | The key of the group
    try {
      List<OrganizerByGroup> result = apiInstance.groupsGroupKeyOrganizersGet(authorization, groupKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGroupKeyOrganizersGet");
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
| **authorization** | **String**| Access token | |
| **groupKey** | **Long**| The key of the group | |

### Return type

[**List&lt;OrganizerByGroup&gt;**](OrganizerByGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="groupsGroupKeyOrganizersPost"></a>
# **groupsGroupKeyOrganizersPost**
> List&lt;OrganizerShort&gt; groupsGroupKeyOrganizersPost(authorization, groupKey, body)

Create organizer in group

Creates a new organizer and sends an email to the email address defined in request. This API call is only available to users with the admin role. You may also pass &#39;G2W&#39; or &#39;G2T&#39; or &#39;OPENVOICE&#39; as productType variables, creating organizers for those products. A G2W or G2T organizer will also have access to G2M.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long groupKey = 56L; // Long | The key of the group
    OrganizerReq body = new OrganizerReq(); // OrganizerReq | The details of the organizer to be created
    try {
      List<OrganizerShort> result = apiInstance.groupsGroupKeyOrganizersPost(authorization, groupKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGroupKeyOrganizersPost");
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
| **authorization** | **String**| Access token | |
| **groupKey** | **Long**| The key of the group | |
| **body** | [**OrganizerReq**](OrganizerReq.md)| The details of the organizer to be created | |

### Return type

[**List&lt;OrganizerShort&gt;**](OrganizerShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Server Error |  -  |
| **409** | Conflict |  -  |

<a id="groupsGroupKeyUpcomingMeetingsGet"></a>
# **groupsGroupKeyUpcomingMeetingsGet**
> List&lt;UpcomingMeetingByGroup&gt; groupsGroupKeyUpcomingMeetingsGet(authorization, groupKey)

Get upcoming meetings by group

Get upcoming meetings for a specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long groupKey = 56L; // Long | The key of the group
    try {
      List<UpcomingMeetingByGroup> result = apiInstance.groupsGroupKeyUpcomingMeetingsGet(authorization, groupKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGroupKeyUpcomingMeetingsGet");
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
| **authorization** | **String**| Access token | |
| **groupKey** | **Long**| The key of the group | |

### Return type

[**List&lt;UpcomingMeetingByGroup&gt;**](UpcomingMeetingByGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

