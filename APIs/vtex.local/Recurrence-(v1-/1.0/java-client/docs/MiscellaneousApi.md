# MiscellaneousApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addrecurrenceitem**](MiscellaneousApi.md#addrecurrenceitem) | **POST** /subscriptions/{recurrenceId}/items | Add Subscription item |
| [**getRecurrencebyemail**](MiscellaneousApi.md#getRecurrencebyemail) | **GET** /subscriptions | Get Subscriptions |
| [**getRecurrencebyrecurrenceId**](MiscellaneousApi.md#getRecurrencebyrecurrenceId) | **GET** /subscriptions/{recurrenceId} | Get Subscription by recurrenceId |
| [**getpaymentaccounts**](MiscellaneousApi.md#getpaymentaccounts) | **GET** /subscriptions/{recurrenceid}/accounts | Get payment accounts |
| [**getrecurrenceaddresses**](MiscellaneousApi.md#getrecurrenceaddresses) | **GET** /subscriptions/{recurrenceId}/addresses | Get Subscription addresses |
| [**getrecurrencesettings**](MiscellaneousApi.md#getrecurrencesettings) | **GET** /subscriptions/settings | Get Subscription settings |
| [**getselfrecurrence**](MiscellaneousApi.md#getselfrecurrence) | **GET** /subscriptions/me | Get self Subscription |
| [**reindexrecurrence**](MiscellaneousApi.md#reindexrecurrence) | **PATCH** /subscriptions/{recurrenceId}/reindex | Reindex Subscription |
| [**updatepartialrecurrence**](MiscellaneousApi.md#updatepartialrecurrence) | **PATCH** /subscriptions/{recurrenceId} | Update partial Subscription |
| [**updaterecurrence**](MiscellaneousApi.md#updaterecurrence) | **PUT** /subscriptions | Update Subscription |
| [**updaterecurrencesettings**](MiscellaneousApi.md#updaterecurrencesettings) | **PUT** /subscriptions/settings | Update Subscription settings |


<a id="addrecurrenceitem"></a>
# **addrecurrenceitem**
> addrecurrenceitem(contentType, accept, recurrenceId, addrecurrenceitemRequest)

Add Subscription item

Adds an item to a Subscription (formerly Recurrence).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String recurrenceId = "recurrenceId_example"; // String | 
    List<AddrecurrenceitemRequest> addrecurrenceitemRequest = Arrays.asList(); // List<AddrecurrenceitemRequest> | 
    try {
      apiInstance.addrecurrenceitem(contentType, accept, recurrenceId, addrecurrenceitemRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#addrecurrenceitem");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **recurrenceId** | **String**|  | |
| **addrecurrenceitemRequest** | [**List&lt;AddrecurrenceitemRequest&gt;**](AddrecurrenceitemRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getRecurrencebyemail"></a>
# **getRecurrencebyemail**
> getRecurrencebyemail(contentType, accept, email, cycleStatus)

Get Subscriptions

Retrieves a given Subscription (formerly recurrence). There are three options of filtering your Subscruptions v1. It&#39;s possible to get a list of all Subscriptions v1, by not adding any query params to your request, and simply executing a call to the url. It is also possible to list the Subscriptions by email, filtering by the email query param. And finnally, it is possible to list recurrences with failures on the last execution cycle, filtering by the cycleStatus query param.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String email = "{{email}}"; // String | If you wish to list tasks by email, insert the desired user's email.
    String cycleStatus = "{{cycleStatus}}"; // String | If you wish to list tasks by Subscriptions with failures on the last execution cycle, insert the desired cycleStatus.
    try {
      apiInstance.getRecurrencebyemail(contentType, accept, email, cycleStatus);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#getRecurrencebyemail");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **email** | **String**| If you wish to list tasks by email, insert the desired user&#39;s email. | [optional] |
| **cycleStatus** | **String**| If you wish to list tasks by Subscriptions with failures on the last execution cycle, insert the desired cycleStatus. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getRecurrencebyrecurrenceId"></a>
# **getRecurrencebyrecurrenceId**
> getRecurrencebyrecurrenceId(contentType, accept, recurrenceId)

Get Subscription by recurrenceId

Retrieves a given Subscription (formerly recurrence) by recurrenceId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String recurrenceId = "recurrenceId_example"; // String | 
    try {
      apiInstance.getRecurrencebyrecurrenceId(contentType, accept, recurrenceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#getRecurrencebyrecurrenceId");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **recurrenceId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getpaymentaccounts"></a>
# **getpaymentaccounts**
> getpaymentaccounts(recurrenceid, contentType, accept)

Get payment accounts

Lists payment accounts of a given Subscription (formerly Recurrence) by recurrenceId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String recurrenceid = "recurrenceid_example"; // String | 
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    try {
      apiInstance.getpaymentaccounts(recurrenceid, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#getpaymentaccounts");
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
| **recurrenceid** | **String**|  | |
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getrecurrenceaddresses"></a>
# **getrecurrenceaddresses**
> getrecurrenceaddresses(contentType, accept, recurrenceId)

Get Subscription addresses

Retrieves the addresses attached to a given subscription (formerly recurrence) by recurrenceId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String recurrenceId = "recurrenceId_example"; // String | 
    try {
      apiInstance.getrecurrenceaddresses(contentType, accept, recurrenceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#getrecurrenceaddresses");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **recurrenceId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getrecurrencesettings"></a>
# **getrecurrencesettings**
> getrecurrencesettings(contentType, accept)

Get Subscription settings

Retrieves your store&#39;s Subscriptions&#39; (formerly recurrence) settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    try {
      apiInstance.getrecurrencesettings(contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#getrecurrencesettings");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getselfrecurrence"></a>
# **getselfrecurrence**
> getselfrecurrence(contentType, accept)

Get self Subscription

Lists details of your self Subscription (formerly Recurrence).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    try {
      apiInstance.getselfrecurrence(contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#getselfrecurrence");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="reindexrecurrence"></a>
# **reindexrecurrence**
> reindexrecurrence(recurrenceId, contentType, accept, reindexrecurrenceRequest)

Reindex Subscription

Alters the frequency of a given Subscription (formerly Recurrence) by changing period and interval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String recurrenceId = "recurrenceId_example"; // String | 
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    List<ReindexrecurrenceRequest> reindexrecurrenceRequest = Arrays.asList(); // List<ReindexrecurrenceRequest> | 
    try {
      apiInstance.reindexrecurrence(recurrenceId, contentType, accept, reindexrecurrenceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#reindexrecurrence");
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
| **recurrenceId** | **String**|  | |
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **reindexrecurrenceRequest** | [**List&lt;ReindexrecurrenceRequest&gt;**](ReindexrecurrenceRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updatepartialrecurrence"></a>
# **updatepartialrecurrence**
> updatepartialrecurrence(recurrenceId, contentType, accept, updatepartialrecurrenceRequest)

Update partial Subscription

Updates partial information of a given subscription (formerly Recurrence).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String recurrenceId = "recurrenceId_example"; // String | 
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    UpdatepartialrecurrenceRequest updatepartialrecurrenceRequest = new UpdatepartialrecurrenceRequest(); // UpdatepartialrecurrenceRequest | 
    try {
      apiInstance.updatepartialrecurrence(recurrenceId, contentType, accept, updatepartialrecurrenceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#updatepartialrecurrence");
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
| **recurrenceId** | **String**|  | |
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **updatepartialrecurrenceRequest** | [**UpdatepartialrecurrenceRequest**](UpdatepartialrecurrenceRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updaterecurrence"></a>
# **updaterecurrence**
> updaterecurrence(contentType, accept, updaterecurrenceRequest)

Update Subscription

Updates details of a given Subscription (formerly recurrence).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    UpdaterecurrenceRequest updaterecurrenceRequest = new UpdaterecurrenceRequest(); // UpdaterecurrenceRequest | 
    try {
      apiInstance.updaterecurrence(contentType, accept, updaterecurrenceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#updaterecurrence");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **updaterecurrenceRequest** | [**UpdaterecurrenceRequest**](UpdaterecurrenceRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updaterecurrencesettings"></a>
# **updaterecurrencesettings**
> updaterecurrencesettings(contentType, accept, updaterecurrencesettingsRequest)

Update Subscription settings

Updates the Subscriptions&#39; (formerly Recurrence) settings of your store by salesChannel and defaultSLA.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    MiscellaneousApi apiInstance = new MiscellaneousApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    UpdaterecurrencesettingsRequest updaterecurrencesettingsRequest = new UpdaterecurrencesettingsRequest(); // UpdaterecurrencesettingsRequest | 
    try {
      apiInstance.updaterecurrencesettings(contentType, accept, updaterecurrencesettingsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousApi#updaterecurrencesettings");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | |
| **updaterecurrencesettingsRequest** | [**UpdaterecurrencesettingsRequest**](UpdaterecurrencesettingsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

