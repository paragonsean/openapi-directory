# ViewsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**viewsOpen**](ViewsApi.md#viewsOpen) | **GET** /views.open |  |
| [**viewsPublish**](ViewsApi.md#viewsPublish) | **GET** /views.publish |  |
| [**viewsPush**](ViewsApi.md#viewsPush) | **GET** /views.push |  |
| [**viewsUpdate**](ViewsApi.md#viewsUpdate) | **GET** /views.update |  |


<a id="viewsOpen"></a>
# **viewsOpen**
> DefaultSuccessTemplate viewsOpen(token, triggerId, view)



Open a view for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String triggerId = "triggerId_example"; // String | Exchange a trigger to post to the user.
    String view = "view_example"; // String | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
    try {
      DefaultSuccessTemplate result = apiInstance.viewsOpen(token, triggerId, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsOpen");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **triggerId** | **String**| Exchange a trigger to post to the user. | |
| **view** | **String**| A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response includes the opened view payload. |  -  |
| **0** | Typical error response, before getting to any possible validation errors. |  -  |

<a id="viewsPublish"></a>
# **viewsPublish**
> DefaultSuccessTemplate viewsPublish(token, userId, view, hash)



Publish a static view for a User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String userId = "userId_example"; // String | `id` of the user you want publish a view to.
    String view = "view_example"; // String | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
    String hash = "hash_example"; // String | A string that represents view state to protect against possible race conditions.
    try {
      DefaultSuccessTemplate result = apiInstance.viewsPublish(token, userId, view, hash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsPublish");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **userId** | **String**| &#x60;id&#x60; of the user you want publish a view to. | |
| **view** | **String**| A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. | |
| **hash** | **String**| A string that represents view state to protect against possible race conditions. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response includes the published view payload. |  -  |
| **0** | Typical error response, before getting to any possible validation errors. |  -  |

<a id="viewsPush"></a>
# **viewsPush**
> DefaultSuccessTemplate viewsPush(token, triggerId, view)



Push a view onto the stack of a root view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String triggerId = "triggerId_example"; // String | Exchange a trigger to post to the user.
    String view = "view_example"; // String | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
    try {
      DefaultSuccessTemplate result = apiInstance.viewsPush(token, triggerId, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsPush");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **triggerId** | **String**| Exchange a trigger to post to the user. | |
| **view** | **String**| A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response includes the pushed view payload. |  -  |
| **0** | Typical error response. |  -  |

<a id="viewsUpdate"></a>
# **viewsUpdate**
> DefaultSuccessTemplate viewsUpdate(token, viewId, externalId, view, hash)



Update an existing view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String viewId = "viewId_example"; // String | A unique identifier of the view to be updated. Either `view_id` or `external_id` is required.
    String externalId = "externalId_example"; // String | A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either `view_id` or `external_id` is required.
    String view = "view_example"; // String | A [view object](/reference/surfaces/views). This must be a JSON-encoded string.
    String hash = "hash_example"; // String | A string that represents view state to protect against possible race conditions.
    try {
      DefaultSuccessTemplate result = apiInstance.viewsUpdate(token, viewId, externalId, view, hash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsUpdate");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **viewId** | **String**| A unique identifier of the view to be updated. Either &#x60;view_id&#x60; or &#x60;external_id&#x60; is required. | [optional] |
| **externalId** | **String**| A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either &#x60;view_id&#x60; or &#x60;external_id&#x60; is required. | [optional] |
| **view** | **String**| A [view object](/reference/surfaces/views). This must be a JSON-encoded string. | [optional] |
| **hash** | **String**| A string that represents view state to protect against possible race conditions. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response includes the updated view payload. |  -  |
| **0** | Typical error response. |  -  |

