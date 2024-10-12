# InvitesApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInvite**](InvitesApi.md#createInvite) | **POST** /invites.json | Create an invite |
| [**inviteToTopic_0**](InvitesApi.md#inviteToTopic_0) | **POST** /t/{id}/invite.json | Invite to topic |


<a id="createInvite"></a>
# **createInvite**
> CreateInvite200Response createInvite(apiKey, apiUsername, createInviteRequest)

Create an invite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    InvitesApi apiInstance = new InvitesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    CreateInviteRequest createInviteRequest = new CreateInviteRequest(); // CreateInviteRequest | 
    try {
      CreateInvite200Response result = apiInstance.createInvite(apiKey, apiUsername, createInviteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitesApi#createInvite");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **createInviteRequest** | [**CreateInviteRequest**](CreateInviteRequest.md)|  | [optional] |

### Return type

[**CreateInvite200Response**](CreateInvite200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="inviteToTopic_0"></a>
# **inviteToTopic_0**
> InviteToTopic200Response inviteToTopic_0(apiKey, apiUsername, id, inviteToTopicRequest)

Invite to topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    InvitesApi apiInstance = new InvitesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    InviteToTopicRequest inviteToTopicRequest = new InviteToTopicRequest(); // InviteToTopicRequest | 
    try {
      InviteToTopic200Response result = apiInstance.inviteToTopic_0(apiKey, apiUsername, id, inviteToTopicRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitesApi#inviteToTopic_0");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **inviteToTopicRequest** | [**InviteToTopicRequest**](InviteToTopicRequest.md)|  | [optional] |

### Return type

[**InviteToTopic200Response**](InviteToTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

