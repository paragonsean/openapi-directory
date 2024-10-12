# OngoingActionsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2OngoingActionsJsonPost**](OngoingActionsApi.md#v2OngoingActionsJsonPost) | **POST** /v2/ongoing_actions.json | Create an ongoing action |


<a id="v2OngoingActionsJsonPost"></a>
# **v2OngoingActionsJsonPost**
> Action v2OngoingActionsJsonPost(actionId)

Create an ongoing action

Creates an ongoing action. An ongoing action is an action that is not yet completed, but progress has been made towards the completion. The user should not need to do anything for an ongoing action to be completed. An ongoing action can be later completed by creating an activity.  Ongoing actions are marked as status&#x3D;pending_activity. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OngoingActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    OngoingActionsApi apiInstance = new OngoingActionsApi(defaultClient);
    Integer actionId = 56; // Integer | Action that is being marked ongoing. This will validate that the action is still valid before modifying it. Ongoing actions can not be marked ongoing. 
    try {
      Action result = apiInstance.v2OngoingActionsJsonPost(actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OngoingActionsApi#v2OngoingActionsJsonPost");
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
| **actionId** | **Integer**| Action that is being marked ongoing. This will validate that the action is still valid before modifying it. Ongoing actions can not be marked ongoing.  | [optional] |

### Return type

[**Action**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

