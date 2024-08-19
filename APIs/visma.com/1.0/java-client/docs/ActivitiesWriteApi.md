# ActivitiesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activitiesPatchActivity**](ActivitiesWriteApi.md#activitiesPatchActivity) | **PATCH** /v1/activities/{guid} | Update (Patch) a activity or a part of it |
| [**activitiesPostActivity**](ActivitiesWriteApi.md#activitiesPostActivity) | **POST** /v1/activities | Insert a activity |
| [**activityParticipantsPatchActivityParticipants**](ActivitiesWriteApi.md#activityParticipantsPatchActivityParticipants) | **PATCH** /v1/activityparticipants/{guid} | Update (Patch) a activity participant or a part of it |
| [**activityParticipantsPostActivityParticipant**](ActivitiesWriteApi.md#activityParticipantsPostActivityParticipant) | **POST** /v1/activityparticipants | Adds an activity participant |


<a id="activitiesPatchActivity"></a>
# **activitiesPatchActivity**
> List&lt;ActivityModel&gt; activitiesPatchActivity(guid, patchOperation)

Update (Patch) a activity or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesWriteApi;

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

    ActivitiesWriteApi apiInstance = new ActivitiesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the activity. Can also be comma separate list of IDs to patch multiple activities with one call. When multiple IDs are given, returns model which has list of succeeded activities and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ActivityModel
    try {
      List<ActivityModel> result = apiInstance.activitiesPatchActivity(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesWriteApi#activitiesPatchActivity");
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
| **guid** | **String**| ID of the activity. Can also be comma separate list of IDs to patch multiple activities with one call. When multiple IDs are given, returns model which has list of succeeded activities and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ActivityModel | [optional] |

### Return type

[**List&lt;ActivityModel&gt;**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated activities |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activitiesPostActivity"></a>
# **activitiesPostActivity**
> ActivityModel activitiesPostActivity(activityModel)

Insert a activity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesWriteApi;

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

    ActivitiesWriteApi apiInstance = new ActivitiesWriteApi(defaultClient);
    ActivityModel activityModel = new ActivityModel(); // ActivityModel | ActivityModel
    try {
      ActivityModel result = apiInstance.activitiesPostActivity(activityModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesWriteApi#activitiesPostActivity");
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
| **activityModel** | [**ActivityModel**](ActivityModel.md)| ActivityModel | [optional] |

### Return type

[**ActivityModel**](ActivityModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created activity |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activityParticipantsPatchActivityParticipants"></a>
# **activityParticipantsPatchActivityParticipants**
> List&lt;ActivityParticipantModel&gt; activityParticipantsPatchActivityParticipants(guid, patchOperation)

Update (Patch) a activity participant or a part of it

Only IsConfirmed property can be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesWriteApi;

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

    ActivitiesWriteApi apiInstance = new ActivitiesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the activity participant
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ActivityParticipantModel
    try {
      List<ActivityParticipantModel> result = apiInstance.activityParticipantsPatchActivityParticipants(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesWriteApi#activityParticipantsPatchActivityParticipants");
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
| **guid** | **String**| ID of the activity participant | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ActivityParticipantModel | [optional] |

### Return type

[**List&lt;ActivityParticipantModel&gt;**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated activity participants |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activityParticipantsPostActivityParticipant"></a>
# **activityParticipantsPostActivityParticipant**
> ActivityParticipantModel activityParticipantsPostActivityParticipant(activityParticipantModel)

Adds an activity participant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesWriteApi;

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

    ActivitiesWriteApi apiInstance = new ActivitiesWriteApi(defaultClient);
    ActivityParticipantModel activityParticipantModel = new ActivityParticipantModel(); // ActivityParticipantModel | ActivityParticipantModel
    try {
      ActivityParticipantModel result = apiInstance.activityParticipantsPostActivityParticipant(activityParticipantModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesWriteApi#activityParticipantsPostActivityParticipant");
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
| **activityParticipantModel** | [**ActivityParticipantModel**](ActivityParticipantModel.md)| ActivityParticipantModel | [optional] |

### Return type

[**ActivityParticipantModel**](ActivityParticipantModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added participant |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

