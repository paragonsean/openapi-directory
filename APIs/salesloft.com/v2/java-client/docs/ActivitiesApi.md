# ActivitiesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ActivitiesJsonPost**](ActivitiesApi.md#v2ActivitiesJsonPost) | **POST** /v2/activities.json | Create an activity |


<a id="v2ActivitiesJsonPost"></a>
# **v2ActivitiesJsonPost**
> Activity v2ActivitiesJsonPost(actionId, taskId)

Create an activity

Creates an activity. An activity will mark the associated action as completed. Currently, only certain action types can have an activity explicitly created for them. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    Integer actionId = 56; // Integer | Action that is being completed. This will validate that the action is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The action must have a type of 'integration'. 
    Integer taskId = 56; // Integer | Task that is being completed. This will validate that the task is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The task must have a type of 'integration'. 
    try {
      Activity result = apiInstance.v2ActivitiesJsonPost(actionId, taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#v2ActivitiesJsonPost");
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
| **actionId** | **Integer**| Action that is being completed. This will validate that the action is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The action must have a type of &#39;integration&#39;.  | [optional] |
| **taskId** | **Integer**| Task that is being completed. This will validate that the task is still valid before completed it. The same action can never be successfully passed twice to this endpoint. The task must have a type of &#39;integration&#39;.  | [optional] |

### Return type

[**Activity**](Activity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

