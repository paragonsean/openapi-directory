# ActivitiesDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activitiesDeleteActivity**](ActivitiesDeleteApi.md#activitiesDeleteActivity) | **DELETE** /v1/activities/{guid} | Delete an activity |
| [**activitiesDeleteExceptions**](ActivitiesDeleteApi.md#activitiesDeleteExceptions) | **DELETE** /v1/activities/{guid}/exceptions | Resets exceptions from a recurring activity. |
| [**activityParticipantsDeleteActivityParticipant**](ActivitiesDeleteApi.md#activityParticipantsDeleteActivityParticipant) | **DELETE** /v1/activities/{activityGuid}/activityparticipants/{activityParticipantGuid} | Delete activity participant. |


<a id="activitiesDeleteActivity"></a>
# **activitiesDeleteActivity**
> activitiesDeleteActivity(guid)

Delete an activity

Returns: No Content (204) if succeeded. Not found (404) if activity can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesDeleteApi;

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

    ActivitiesDeleteApi apiInstance = new ActivitiesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the activity to delete
    try {
      apiInstance.activitiesDeleteActivity(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesDeleteApi#activitiesDeleteActivity");
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
| **guid** | **String**| ID for the activity to delete | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activitiesDeleteExceptions"></a>
# **activitiesDeleteExceptions**
> activitiesDeleteExceptions(guid)

Resets exceptions from a recurring activity.

Returns: No Content (204) if succeeded. Not found (404) if activity can&#39;t be found or is not recurring.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesDeleteApi;

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

    ActivitiesDeleteApi apiInstance = new ActivitiesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the recurring activity
    try {
      apiInstance.activitiesDeleteExceptions(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesDeleteApi#activitiesDeleteExceptions");
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
| **guid** | **String**| ID of the recurring activity | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activityParticipantsDeleteActivityParticipant"></a>
# **activityParticipantsDeleteActivityParticipant**
> activityParticipantsDeleteActivityParticipant(activityGuid, activityParticipantGuid)

Delete activity participant.

Returns: No Content (204) if succeeded. Not found (404) if participant can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesDeleteApi;

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

    ActivitiesDeleteApi apiInstance = new ActivitiesDeleteApi(defaultClient);
    String activityGuid = "activityGuid_example"; // String | ID of the activity from which to delete the participant. If an activity occurrence guid is given, this will create an exception to the recurring activity and delete the participant from that.
    String activityParticipantGuid = "activityParticipantGuid_example"; // String | ID of the participant
    try {
      apiInstance.activityParticipantsDeleteActivityParticipant(activityGuid, activityParticipantGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesDeleteApi#activityParticipantsDeleteActivityParticipant");
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
| **activityGuid** | **String**| ID of the activity from which to delete the participant. If an activity occurrence guid is given, this will create an exception to the recurring activity and delete the participant from that. | |
| **activityParticipantGuid** | **String**| ID of the participant | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

