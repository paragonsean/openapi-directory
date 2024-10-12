# WebhooksApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addWebhook**](WebhooksApi.md#addWebhook) | **POST** /webhooks | Add A New Webhook |
| [**deleteWebhook**](WebhooksApi.md#deleteWebhook) | **DELETE** /webhooks/{id} | Delete a webhook |
| [**getWebhookById**](WebhooksApi.md#getWebhookById) | **GET** /webhooks/{id} | Get info for a webhook |
| [**getWehooksList**](WebhooksApi.md#getWehooksList) | **GET** /webhooks | Get Webhooks List |
| [**regenerateWebhookToken**](WebhooksApi.md#regenerateWebhookToken) | **POST** /webhooks/regenerate-token/{id} | Regenerate security token |
| [**resendWebhookActivityEntry**](WebhooksApi.md#resendWebhookActivityEntry) | **POST** /webhooks/resend/{activityId} | Resend a webhook message |
| [**updateWebhook**](WebhooksApi.md#updateWebhook) | **PATCH** /webhooks/{id} | Update a webhook |


<a id="addWebhook"></a>
# **addWebhook**
> WebhookResponse addWebhook(evApiKey, evAccessToken, addWebhookRequestBody)

Add A New Webhook

Create a new Webhook on your account. Creating a Webhook will require an endpoint URL, a path, what events should trigger a webhook, and what request version to use. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    AddWebhookRequestBody addWebhookRequestBody = new AddWebhookRequestBody(); // AddWebhookRequestBody | 
    try {
      WebhookResponse result = apiInstance.addWebhook(evApiKey, evAccessToken, addWebhookRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#addWebhook");
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
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **addWebhookRequestBody** | [**AddWebhookRequestBody**](AddWebhookRequestBody.md)|  | [optional] |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteWebhook"></a>
# **deleteWebhook**
> EmptyResponse deleteWebhook(id, evApiKey, evAccessToken)

Delete a webhook

Deleted the specified webhook. This will not affect logs or any resources the webhook is connected to. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Integer id = 56; // Integer | Webhook endpoint ID
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    try {
      EmptyResponse result = apiInstance.deleteWebhook(id, evApiKey, evAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#deleteWebhook");
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
| **id** | **Integer**| Webhook endpoint ID | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful operation |  -  |

<a id="getWebhookById"></a>
# **getWebhookById**
> WebhookResponse getWebhookById(id, evApiKey, evAccessToken, include)

Get info for a webhook

Returns the metadata for a specific webhook. Webhook IDs can be retrieve from GET /webhooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Integer id = 56; // Integer | Webhook endpoint ID
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String include = "include_example"; // String |  Include metadata for related items; `ownerAccount` and/or `resource` 
    try {
      WebhookResponse result = apiInstance.getWebhookById(id, evApiKey, evAccessToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getWebhookById");
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
| **id** | **Integer**| Webhook endpoint ID | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **include** | **String**|  Include metadata for related items; &#x60;ownerAccount&#x60; and/or &#x60;resource&#x60;  | [optional] |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getWehooksList"></a>
# **getWehooksList**
> WebhookCollectionResponse getWehooksList(evApiKey, evAccessToken, include, offset, limit)

Get Webhooks List

Returns a list of Webhooks. By default, this will return metadata on all Webhooks within the account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String include = "include_example"; // String | List of related record types to include. Valid options are `owningAccount` and `resource`
    Integer offset = 100; // Integer | Records to skip before returning results.
    Integer limit = 100; // Integer | Limit of the records list
    try {
      WebhookCollectionResponse result = apiInstance.getWehooksList(evApiKey, evAccessToken, include, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getWehooksList");
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
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **include** | **String**| List of related record types to include. Valid options are &#x60;owningAccount&#x60; and &#x60;resource&#x60; | [optional] |
| **offset** | **Integer**| Records to skip before returning results. | [optional] |
| **limit** | **Integer**| Limit of the records list | [optional] |

### Return type

[**WebhookCollectionResponse**](WebhookCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="regenerateWebhookToken"></a>
# **regenerateWebhookToken**
> WebhookResponse regenerateWebhookToken(id, evApiKey, evAccessToken)

Regenerate security token

This endpoint will allow you to regenerate the security token for a webhook if you believe it’s been compromised in any way. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | Webhook ID
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    try {
      WebhookResponse result = apiInstance.regenerateWebhookToken(id, evApiKey, evAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#regenerateWebhookToken");
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
| **id** | **String**| Webhook ID | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="resendWebhookActivityEntry"></a>
# **resendWebhookActivityEntry**
> EmptyResponse resendWebhookActivityEntry(activityId, evApiKey, evAccessToken)

Resend a webhook message

This endpoint will allow you to resend a webhook that was previously sent. Resent webhooks will send exactly the same as the original webhook with the exception of the “sent” timestamp. Activity IDs can be retrieve from the webhook logs in your account or via GET /activity/webhooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String activityId = "activityId_example"; // String | Webhooks activity entry ID
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    try {
      EmptyResponse result = apiInstance.resendWebhookActivityEntry(activityId, evApiKey, evAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#resendWebhookActivityEntry");
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
| **activityId** | **String**| Webhooks activity entry ID | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateWebhook"></a>
# **updateWebhook**
> WebhookResponse updateWebhook(id, evApiKey, evAccessToken, updateWebhookRequestBody)

Update a webhook

Update the specified webhook. Updated webhooks will take effect immediately and could impact active workflows. Please be certain the webhook is not currently in use prior to updating.   You only need to send the portions of the webhook configuration you wish to change, rather than the entire webhook object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Integer id = 56; // Integer | Webhook endpoint ID
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    UpdateWebhookRequestBody updateWebhookRequestBody = new UpdateWebhookRequestBody(); // UpdateWebhookRequestBody | 
    try {
      WebhookResponse result = apiInstance.updateWebhook(id, evApiKey, evAccessToken, updateWebhookRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#updateWebhook");
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
| **id** | **Integer**| Webhook endpoint ID | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **updateWebhookRequestBody** | [**UpdateWebhookRequestBody**](UpdateWebhookRequestBody.md)|  | [optional] |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

