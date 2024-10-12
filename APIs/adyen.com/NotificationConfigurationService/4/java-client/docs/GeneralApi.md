# GeneralApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Notification/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCreateNotificationConfiguration**](GeneralApi.md#postCreateNotificationConfiguration) | **POST** /createNotificationConfiguration | Subscribe to notifications |
| [**postDeleteNotificationConfigurations**](GeneralApi.md#postDeleteNotificationConfigurations) | **POST** /deleteNotificationConfigurations | Delete a notification subscription configuration |
| [**postGetNotificationConfiguration**](GeneralApi.md#postGetNotificationConfiguration) | **POST** /getNotificationConfiguration | Get a notification subscription configuration |
| [**postGetNotificationConfigurationList**](GeneralApi.md#postGetNotificationConfigurationList) | **POST** /getNotificationConfigurationList | Get a list of notification subscription configurations |
| [**postTestNotificationConfiguration**](GeneralApi.md#postTestNotificationConfiguration) | **POST** /testNotificationConfiguration | Test a notification configuration |
| [**postUpdateNotificationConfiguration**](GeneralApi.md#postUpdateNotificationConfiguration) | **POST** /updateNotificationConfiguration | Update a notification subscription configuration |


<a id="postCreateNotificationConfiguration"></a>
# **postCreateNotificationConfiguration**
> GetNotificationConfigurationResponse postCreateNotificationConfiguration(createNotificationConfigurationRequest)

Subscribe to notifications

Creates a subscription to notifications informing you of events on your platform. After the subscription is created, the events specified in the configuration will be sent to the URL specified in the configuration. Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis), so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few different endpoints as configured.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Notification/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    CreateNotificationConfigurationRequest createNotificationConfigurationRequest = new CreateNotificationConfigurationRequest(); // CreateNotificationConfigurationRequest | 
    try {
      GetNotificationConfigurationResponse result = apiInstance.postCreateNotificationConfiguration(createNotificationConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postCreateNotificationConfiguration");
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
| **createNotificationConfigurationRequest** | [**CreateNotificationConfigurationRequest**](CreateNotificationConfigurationRequest.md)|  | [optional] |

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDeleteNotificationConfigurations"></a>
# **postDeleteNotificationConfigurations**
> GenericResponse postDeleteNotificationConfigurations(deleteNotificationConfigurationRequest)

Delete a notification subscription configuration

Deletes an existing notification subscription configuration. After the subscription is deleted, no further event notifications will be sent to the URL defined in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Notification/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    DeleteNotificationConfigurationRequest deleteNotificationConfigurationRequest = new DeleteNotificationConfigurationRequest(); // DeleteNotificationConfigurationRequest | 
    try {
      GenericResponse result = apiInstance.postDeleteNotificationConfigurations(deleteNotificationConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postDeleteNotificationConfigurations");
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
| **deleteNotificationConfigurationRequest** | [**DeleteNotificationConfigurationRequest**](DeleteNotificationConfigurationRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postGetNotificationConfiguration"></a>
# **postGetNotificationConfiguration**
> GetNotificationConfigurationResponse postGetNotificationConfiguration(getNotificationConfigurationRequest)

Get a notification subscription configuration

Returns the details of the configuration of a notification subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Notification/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    GetNotificationConfigurationRequest getNotificationConfigurationRequest = new GetNotificationConfigurationRequest(); // GetNotificationConfigurationRequest | 
    try {
      GetNotificationConfigurationResponse result = apiInstance.postGetNotificationConfiguration(getNotificationConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postGetNotificationConfiguration");
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
| **getNotificationConfigurationRequest** | [**GetNotificationConfigurationRequest**](GetNotificationConfigurationRequest.md)|  | [optional] |

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postGetNotificationConfigurationList"></a>
# **postGetNotificationConfigurationList**
> GetNotificationConfigurationListResponse postGetNotificationConfigurationList(body)

Get a list of notification subscription configurations

Returns the details of the configurations of all of the notification subscriptions in the platform of the executing user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Notification/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    Object body = null; // Object | 
    try {
      GetNotificationConfigurationListResponse result = apiInstance.postGetNotificationConfigurationList(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postGetNotificationConfigurationList");
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
| **body** | **Object**|  | [optional] |

### Return type

[**GetNotificationConfigurationListResponse**](GetNotificationConfigurationListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postTestNotificationConfiguration"></a>
# **postTestNotificationConfiguration**
> TestNotificationConfigurationResponse postTestNotificationConfiguration(testNotificationConfigurationRequest)

Test a notification configuration

Tests an existing notification subscription configuration. For each event type specified, a test notification will be generated and sent to the URL configured in the subscription specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Notification/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    TestNotificationConfigurationRequest testNotificationConfigurationRequest = new TestNotificationConfigurationRequest(); // TestNotificationConfigurationRequest | 
    try {
      TestNotificationConfigurationResponse result = apiInstance.postTestNotificationConfiguration(testNotificationConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postTestNotificationConfiguration");
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
| **testNotificationConfigurationRequest** | [**TestNotificationConfigurationRequest**](TestNotificationConfigurationRequest.md)|  | [optional] |

### Return type

[**TestNotificationConfigurationResponse**](TestNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postUpdateNotificationConfiguration"></a>
# **postUpdateNotificationConfiguration**
> GetNotificationConfigurationResponse postUpdateNotificationConfiguration(updateNotificationConfigurationRequest)

Update a notification subscription configuration

Updates an existing notification subscription configuration. If you are updating the event types, you must provide all event types, otherwise the previous event type configuration will be overwritten.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Notification/v4");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    UpdateNotificationConfigurationRequest updateNotificationConfigurationRequest = new UpdateNotificationConfigurationRequest(); // UpdateNotificationConfigurationRequest | 
    try {
      GetNotificationConfigurationResponse result = apiInstance.postUpdateNotificationConfiguration(updateNotificationConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postUpdateNotificationConfiguration");
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
| **updateNotificationConfigurationRequest** | [**UpdateNotificationConfigurationRequest**](UpdateNotificationConfigurationRequest.md)|  | [optional] |

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

