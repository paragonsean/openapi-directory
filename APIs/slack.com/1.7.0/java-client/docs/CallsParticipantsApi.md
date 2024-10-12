# CallsParticipantsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callsParticipantsAdd**](CallsParticipantsApi.md#callsParticipantsAdd) | **POST** /calls.participants.add |  |
| [**callsParticipantsRemove**](CallsParticipantsApi.md#callsParticipantsRemove) | **POST** /calls.participants.remove |  |


<a id="callsParticipantsAdd"></a>
# **callsParticipantsAdd**
> DefaultSuccessTemplate callsParticipantsAdd(token, id, users)



Registers new participants added to a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsParticipantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsParticipantsApi apiInstance = new CallsParticipantsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
    String users = "users_example"; // String | The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    try {
      DefaultSuccessTemplate result = apiInstance.callsParticipantsAdd(token, id, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsParticipantsApi#callsParticipantsAdd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |
| **users** | **String**| The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="callsParticipantsRemove"></a>
# **callsParticipantsRemove**
> DefaultSuccessTemplate callsParticipantsRemove(token, id, users)



Registers participants removed from a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsParticipantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsParticipantsApi apiInstance = new CallsParticipantsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
    String users = "users_example"; // String | The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    try {
      DefaultSuccessTemplate result = apiInstance.callsParticipantsRemove(token, id, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsParticipantsApi#callsParticipantsRemove");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |
| **users** | **String**| The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

