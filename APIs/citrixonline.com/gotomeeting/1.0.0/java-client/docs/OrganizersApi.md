# OrganizersApi

All URIs are relative to *https://api.citrixonline.com/G2M/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organizersDelete**](OrganizersApi.md#organizersDelete) | **DELETE** /organizers | Delete organizer by email |
| [**organizersGet**](OrganizersApi.md#organizersGet) | **GET** /organizers | Get organizer by email / Get all organizers |
| [**organizersOrganizerKeyAttendeesGet**](OrganizersApi.md#organizersOrganizerKeyAttendeesGet) | **GET** /organizers/{organizerKey}/attendees | Get attendees by organizer |
| [**organizersOrganizerKeyDelete**](OrganizersApi.md#organizersOrganizerKeyDelete) | **DELETE** /organizers/{organizerKey} | Delete organizer |
| [**organizersOrganizerKeyGet**](OrganizersApi.md#organizersOrganizerKeyGet) | **GET** /organizers/{organizerKey} | Get organizer |
| [**organizersOrganizerKeyHistoricalMeetingsGet**](OrganizersApi.md#organizersOrganizerKeyHistoricalMeetingsGet) | **GET** /organizers/{organizerKey}/historicalMeetings | Get historical meetings by organizer |
| [**organizersOrganizerKeyMeetingsGet**](OrganizersApi.md#organizersOrganizerKeyMeetingsGet) | **GET** /organizers/{organizerKey}/meetings | DEPRECATED: Get meetings by organizer |
| [**organizersOrganizerKeyPut**](OrganizersApi.md#organizersOrganizerKeyPut) | **PUT** /organizers/{organizerKey} | Update organizer |
| [**organizersOrganizerKeyUpcomingMeetingsGet**](OrganizersApi.md#organizersOrganizerKeyUpcomingMeetingsGet) | **GET** /organizers/{organizerKey}/upcomingMeetings | Get upcoming meetings by organizer |
| [**organizersPost**](OrganizersApi.md#organizersPost) | **POST** /organizers | Create organizer |


<a id="organizersDelete"></a>
# **organizersDelete**
> organizersDelete(authorization, email)

Delete organizer by email

Deletes the individual organizer specified by the email address. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    String email = "email_example"; // String | The email address of the organizer
    try {
      apiInstance.organizersDelete(authorization, email);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersDelete");
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
| **email** | **String**| The email address of the organizer | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |

<a id="organizersGet"></a>
# **organizersGet**
> List&lt;Organizer&gt; organizersGet(authorization, email)

Get organizer by email / Get all organizers

Gets the individual organizer specified by the organizer&#39;s email address. If an email address is not specified, all organizers are returned. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    String email = "email_example"; // String | The email address of the organizer
    try {
      List<Organizer> result = apiInstance.organizersGet(authorization, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersGet");
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
| **email** | **String**| The email address of the organizer | [optional] |

### Return type

[**List&lt;Organizer&gt;**](Organizer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyAttendeesGet"></a>
# **organizersOrganizerKeyAttendeesGet**
> List&lt;AttendeeByOrganizer&gt; organizersOrganizerKeyAttendeesGet(authorization, organizerKey, startDate, endDate)

Get attendees by organizer

Lists all attendees for all meetings within a specified date range for a specified organizer. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | A required start of date range in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | A required end of date range in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<AttendeeByOrganizer> result = apiInstance.organizersOrganizerKeyAttendeesGet(authorization, organizerKey, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyAttendeesGet");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **startDate** | **OffsetDateTime**| A required start of date range in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | |
| **endDate** | **OffsetDateTime**| A required end of date range in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | |

### Return type

[**List&lt;AttendeeByOrganizer&gt;**](AttendeeByOrganizer.md)

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
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyDelete"></a>
# **organizersOrganizerKeyDelete**
> organizersOrganizerKeyDelete(authorization, organizerKey)

Delete organizer

Deletes the individual organizer specified by the organizer key. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    try {
      apiInstance.organizersOrganizerKeyDelete(authorization, organizerKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyDelete");
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
| **organizerKey** | **Long**| The key of the organizer | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyGet"></a>
# **organizersOrganizerKeyGet**
> List&lt;Organizer&gt; organizersOrganizerKeyGet(authorization, organizerKey)

Get organizer

Returns the individual organizer specified by the key. This API call is only available to users with the admin role. Non-admin users can only make this call for their own organizerKey.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    try {
      List<Organizer> result = apiInstance.organizersOrganizerKeyGet(authorization, organizerKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyGet");
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
| **organizerKey** | **Long**| The key of the organizer | |

### Return type

[**List&lt;Organizer&gt;**](Organizer.md)

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
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyHistoricalMeetingsGet"></a>
# **organizersOrganizerKeyHistoricalMeetingsGet**
> List&lt;HistoricalMeeting&gt; organizersOrganizerKeyHistoricalMeetingsGet(authorization, organizerKey, startDate, endDate)

Get historical meetings by organizer

Get historical meetings for the specified organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<HistoricalMeeting> result = apiInstance.organizersOrganizerKeyHistoricalMeetingsGet(authorization, organizerKey, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyHistoricalMeetingsGet");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **startDate** | **OffsetDateTime**| Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | |
| **endDate** | **OffsetDateTime**| Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | |

### Return type

[**List&lt;HistoricalMeeting&gt;**](HistoricalMeeting.md)

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
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyMeetingsGet"></a>
# **organizersOrganizerKeyMeetingsGet**
> List&lt;MeetingByOrganizer&gt; organizersOrganizerKeyMeetingsGet(authorization, organizerKey, scheduled, history, startDate, endDate)

DEPRECATED: Get meetings by organizer

DEPRECATED: Please use the new API calls &#39;Get historical meetings by organizer&#39; and &#39;Get upcoming meetings by organizer&#39;. Gets future (scheduled) or past (history) meetings for a specified organizer. Include &#39;history&#x3D;true&#39; and the past start and end dates in the URL to retrieve past meetings. Enter &#39;scheduled&#x3D;true&#39; (without dates) to get scheduled meetings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Boolean scheduled = true; // Boolean | When 'true', returns all future meetings. Date range not supported.
    Boolean history = true; // Boolean | When 'true', returns all past meetings within date range
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | If history is 'true', required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | If history is 'true', required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<MeetingByOrganizer> result = apiInstance.organizersOrganizerKeyMeetingsGet(authorization, organizerKey, scheduled, history, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyMeetingsGet");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **scheduled** | **Boolean**| When &#39;true&#39;, returns all future meetings. Date range not supported. | [optional] |
| **history** | **Boolean**| When &#39;true&#39;, returns all past meetings within date range | [optional] |
| **startDate** | **OffsetDateTime**| If history is &#39;true&#39;, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | [optional] |
| **endDate** | **OffsetDateTime**| If history is &#39;true&#39;, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | [optional] |

### Return type

[**List&lt;MeetingByOrganizer&gt;**](MeetingByOrganizer.md)

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
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyPut"></a>
# **organizersOrganizerKeyPut**
> organizersOrganizerKeyPut(authorization, organizerKey, body)

Update organizer

Updates the products of the specified organizer. To add a product (G2M, G2W, G2T, OPENVOICE) for the organizer, the call must be sent once for each product you want to add. To remove all products for the organizer, set status to &#39;suspended&#39;. The call is limited to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    OrganizerStatus body = new OrganizerStatus(); // OrganizerStatus | The organizer's status
    try {
      apiInstance.organizersOrganizerKeyPut(authorization, organizerKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyPut");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **body** | [**OrganizerStatus**](OrganizerStatus.md)| The organizer&#39;s status | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="organizersOrganizerKeyUpcomingMeetingsGet"></a>
# **organizersOrganizerKeyUpcomingMeetingsGet**
> List&lt;UpcomingMeeting&gt; organizersOrganizerKeyUpcomingMeetingsGet(authorization, organizerKey)

Get upcoming meetings by organizer

Get upcoming meetings for a specified organizer. This API call is only available to users with the admin role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    try {
      List<UpcomingMeeting> result = apiInstance.organizersOrganizerKeyUpcomingMeetingsGet(authorization, organizerKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersOrganizerKeyUpcomingMeetingsGet");
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
| **organizerKey** | **Long**| The key of the organizer | |

### Return type

[**List&lt;UpcomingMeeting&gt;**](UpcomingMeeting.md)

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
| **404** | Not found |  -  |

<a id="organizersPost"></a>
# **organizersPost**
> List&lt;OrganizerShort&gt; organizersPost(authorization, body)

Create organizer

Creates a new organizer and sends an email to the email address defined in the request. This API call is only available to users with the admin role. You may also pass &#39;G2W&#39; or &#39;G2T&#39; or &#39;OPENVOICE&#39; as productType variables, creating organizers for those products. A G2W or G2T organizer will also have access to G2M.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    OrganizerReq body = new OrganizerReq(); // OrganizerReq | The details of the organizer to be created
    try {
      List<OrganizerShort> result = apiInstance.organizersPost(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#organizersPost");
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

