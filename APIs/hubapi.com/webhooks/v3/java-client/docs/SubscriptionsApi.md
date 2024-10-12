# SubscriptionsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive**](SubscriptionsApi.md#deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive) | **DELETE** /webhooks/v3/{appId}/subscriptions/{subscriptionId} |  |
| [**getWebhooksV3AppIdSubscriptionsGetAll**](SubscriptionsApi.md#getWebhooksV3AppIdSubscriptionsGetAll) | **GET** /webhooks/v3/{appId}/subscriptions |  |
| [**getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById**](SubscriptionsApi.md#getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById) | **GET** /webhooks/v3/{appId}/subscriptions/{subscriptionId} |  |
| [**patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate**](SubscriptionsApi.md#patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate) | **PATCH** /webhooks/v3/{appId}/subscriptions/{subscriptionId} |  |
| [**postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch**](SubscriptionsApi.md#postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch) | **POST** /webhooks/v3/{appId}/subscriptions/batch/update |  |
| [**postWebhooksV3AppIdSubscriptionsCreate**](SubscriptionsApi.md#postWebhooksV3AppIdSubscriptionsCreate) | **POST** /webhooks/v3/{appId}/subscriptions |  |


<a id="deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive"></a>
# **deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive**
> deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive(subscriptionId, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer subscriptionId = 56; // Integer | 
    Integer appId = 56; // Integer | 
    try {
      apiInstance.deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive(subscriptionId, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#deleteWebhooksV3AppIdSubscriptionsSubscriptionIdArchive");
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
| **subscriptionId** | **Integer**|  | |
| **appId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getWebhooksV3AppIdSubscriptionsGetAll"></a>
# **getWebhooksV3AppIdSubscriptionsGetAll**
> SubscriptionListResponse getWebhooksV3AppIdSubscriptionsGetAll(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer appId = 56; // Integer | 
    try {
      SubscriptionListResponse result = apiInstance.getWebhooksV3AppIdSubscriptionsGetAll(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#getWebhooksV3AppIdSubscriptionsGetAll");
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
| **appId** | **Integer**|  | |

### Return type

[**SubscriptionListResponse**](SubscriptionListResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById"></a>
# **getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById**
> SubscriptionResponse getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById(subscriptionId, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer subscriptionId = 56; // Integer | 
    Integer appId = 56; // Integer | 
    try {
      SubscriptionResponse result = apiInstance.getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById(subscriptionId, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#getWebhooksV3AppIdSubscriptionsSubscriptionIdGetById");
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
| **subscriptionId** | **Integer**|  | |
| **appId** | **Integer**|  | |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate"></a>
# **patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate**
> SubscriptionResponse patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate(subscriptionId, appId, subscriptionPatchRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer subscriptionId = 56; // Integer | 
    Integer appId = 56; // Integer | 
    SubscriptionPatchRequest subscriptionPatchRequest = new SubscriptionPatchRequest(); // SubscriptionPatchRequest | 
    try {
      SubscriptionResponse result = apiInstance.patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate(subscriptionId, appId, subscriptionPatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#patchWebhooksV3AppIdSubscriptionsSubscriptionIdUpdate");
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
| **subscriptionId** | **Integer**|  | |
| **appId** | **Integer**|  | |
| **subscriptionPatchRequest** | [**SubscriptionPatchRequest**](SubscriptionPatchRequest.md)|  | |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch"></a>
# **postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch**
> BatchResponseSubscriptionResponse postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch(appId, batchInputSubscriptionBatchUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer appId = 56; // Integer | 
    BatchInputSubscriptionBatchUpdateRequest batchInputSubscriptionBatchUpdateRequest = new BatchInputSubscriptionBatchUpdateRequest(); // BatchInputSubscriptionBatchUpdateRequest | 
    try {
      BatchResponseSubscriptionResponse result = apiInstance.postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch(appId, batchInputSubscriptionBatchUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#postWebhooksV3AppIdSubscriptionsBatchUpdateUpdateBatch");
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
| **appId** | **Integer**|  | |
| **batchInputSubscriptionBatchUpdateRequest** | [**BatchInputSubscriptionBatchUpdateRequest**](BatchInputSubscriptionBatchUpdateRequest.md)|  | |

### Return type

[**BatchResponseSubscriptionResponse**](BatchResponseSubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **207** | multiple statuses |  -  |
| **0** | An error occurred. |  -  |

<a id="postWebhooksV3AppIdSubscriptionsCreate"></a>
# **postWebhooksV3AppIdSubscriptionsCreate**
> SubscriptionResponse postWebhooksV3AppIdSubscriptionsCreate(appId, subscriptionCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    Integer appId = 56; // Integer | 
    SubscriptionCreateRequest subscriptionCreateRequest = new SubscriptionCreateRequest(); // SubscriptionCreateRequest | 
    try {
      SubscriptionResponse result = apiInstance.postWebhooksV3AppIdSubscriptionsCreate(appId, subscriptionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#postWebhooksV3AppIdSubscriptionsCreate");
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
| **appId** | **Integer**|  | |
| **subscriptionCreateRequest** | [**SubscriptionCreateRequest**](SubscriptionCreateRequest.md)|  | |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **0** | An error occurred. |  -  |

