# ActivitiesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activitiesDeleteActivity**](ActivitiesApi.md#activitiesDeleteActivity) | **DELETE** /api/v2/activities/{activityID} | Mark the delete flag for the Activity |
| [**activitiesGetActivities**](ActivitiesApi.md#activitiesGetActivities) | **GET** /api/v2/activities | Get Activities |
| [**activitiesGetActivity**](ActivitiesApi.md#activitiesGetActivity) | **GET** /api/v2/activities/{activityID} | Get an Activity by ID |
| [**activitiesPostActivity**](ActivitiesApi.md#activitiesPostActivity) | **POST** /api/v2/activities | Create an Activity |
| [**activitiesPutActivity**](ActivitiesApi.md#activitiesPutActivity) | **PUT** /api/v2/activities/{activityID} | Update an Activity |


<a id="activitiesDeleteActivity"></a>
# **activitiesDeleteActivity**
> activitiesDeleteActivity(activityID)

Mark the delete flag for the Activity

Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    Integer activityID = 56; // Integer | The id of the activity to delete
    try {
      apiInstance.activitiesDeleteActivity(activityID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesDeleteActivity");
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
| **activityID** | **Integer**| The id of the activity to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="activitiesGetActivities"></a>
# **activitiesGetActivities**
> APIPagedResponseBuildSystemSharedDTOActivity activitiesGetActivities(limit, offset, isIncludeDeleted)

Get Activities

Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.                If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Boolean isIncludeDeleted = true; // Boolean | Does it include deleted activity, or not
    try {
      APIPagedResponseBuildSystemSharedDTOActivity result = apiInstance.activitiesGetActivities(limit, offset, isIncludeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesGetActivities");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **isIncludeDeleted** | **Boolean**| Does it include deleted activity, or not | [optional] |

### Return type

[**APIPagedResponseBuildSystemSharedDTOActivity**](APIPagedResponseBuildSystemSharedDTOActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="activitiesGetActivity"></a>
# **activitiesGetActivity**
> BuildSystemSharedDTOActivity activitiesGetActivity(activityID, isIncludeDeleted)

Get an Activity by ID

Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,              an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    Integer activityID = 56; // Integer | The ID of the Activity to get.
    Boolean isIncludeDeleted = true; // Boolean | Does it include deleted activity, or not
    try {
      BuildSystemSharedDTOActivity result = apiInstance.activitiesGetActivity(activityID, isIncludeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesGetActivity");
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
| **activityID** | **Integer**| The ID of the Activity to get. | |
| **isIncludeDeleted** | **Boolean**| Does it include deleted activity, or not | [optional] |

### Return type

[**BuildSystemSharedDTOActivity**](BuildSystemSharedDTOActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="activitiesPostActivity"></a>
# **activitiesPostActivity**
> Integer activitiesPostActivity(buildSystemSharedDTOActivity)

Create an Activity

Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned              on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an               appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    BuildSystemSharedDTOActivity buildSystemSharedDTOActivity = new BuildSystemSharedDTOActivity(); // BuildSystemSharedDTOActivity | The activity to create.  The ActivityID will be assigned on creation of the Activity.
    try {
      Integer result = apiInstance.activitiesPostActivity(buildSystemSharedDTOActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesPostActivity");
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
| **buildSystemSharedDTOActivity** | [**BuildSystemSharedDTOActivity**](BuildSystemSharedDTOActivity.md)| The activity to create.  The ActivityID will be assigned on creation of the Activity. | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="activitiesPutActivity"></a>
# **activitiesPutActivity**
> activitiesPutActivity(activityID, buildSystemSharedDTOActivity)

Update an Activity

Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    Integer activityID = 56; // Integer | The id of the activity to update
    BuildSystemSharedDTOActivity buildSystemSharedDTOActivity = new BuildSystemSharedDTOActivity(); // BuildSystemSharedDTOActivity | The updated activity
    try {
      apiInstance.activitiesPutActivity(activityID, buildSystemSharedDTOActivity);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#activitiesPutActivity");
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
| **activityID** | **Integer**| The id of the activity to update | |
| **buildSystemSharedDTOActivity** | [**BuildSystemSharedDTOActivity**](BuildSystemSharedDTOActivity.md)| The updated activity | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

