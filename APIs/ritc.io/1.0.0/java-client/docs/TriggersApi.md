# TriggersApi

All URIs are relative to *https://api.ritc.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTrigger**](TriggersApi.md#addTrigger) | **POST** /triggers |  |
| [**getTrigger**](TriggersApi.md#getTrigger) | **GET** /triggers/{trigger_id} |  |
| [**listTriggers**](TriggersApi.md#listTriggers) | **GET** /triggers |  |
| [**removeTrigger**](TriggersApi.md#removeTrigger) | **DELETE** /triggers/{trigger_id} |  |
| [**updateTrigger**](TriggersApi.md#updateTrigger) | **PATCH** /triggers/{trigger_id} |  |


<a id="addTrigger"></a>
# **addTrigger**
> TriggerShortResponse addTrigger(triggerObject)



Create a new trigger in an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    Trigger54 triggerObject = new Trigger54(); // Trigger54 | Trigger parameters and configuration
    try {
      TriggerShortResponse result = apiInstance.addTrigger(triggerObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#addTrigger");
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
| **triggerObject** | [**Trigger54**](Trigger54.md)| Trigger parameters and configuration | |

### Return type

[**TriggerShortResponse**](TriggerShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A trigger was successfully created |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="getTrigger"></a>
# **getTrigger**
> List&lt;TriggerFullResponse&gt; getTrigger(triggerId)



Get a trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String triggerId = "triggerId_example"; // String | Id of Trigger
    try {
      List<TriggerFullResponse> result = apiInstance.getTrigger(triggerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#getTrigger");
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
| **triggerId** | **String**| Id of Trigger | |

### Return type

[**List&lt;TriggerFullResponse&gt;**](TriggerFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about a trigger |  -  |
| **0** | Unexpected error |  -  |

<a id="listTriggers"></a>
# **listTriggers**
> List&lt;TriggerShortResponse&gt; listTriggers()



Triggers in an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    try {
      List<TriggerShortResponse> result = apiInstance.listTriggers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#listTriggers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;TriggerShortResponse&gt;**](TriggerShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of triggers in an app |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="removeTrigger"></a>
# **removeTrigger**
> removeTrigger(triggerId)



Delete a trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String triggerId = "triggerId_example"; // String | Id of Trigger
    try {
      apiInstance.removeTrigger(triggerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#removeTrigger");
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
| **triggerId** | **String**| Id of Trigger | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The trigger was successfully removed |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="updateTrigger"></a>
# **updateTrigger**
> TriggerShortResponse updateTrigger(triggerId, triggerObject)



Update a trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String triggerId = "triggerId_example"; // String | Id of user
    Trigger54 triggerObject = new Trigger54(); // Trigger54 | Trigger information
    try {
      TriggerShortResponse result = apiInstance.updateTrigger(triggerId, triggerObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#updateTrigger");
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
| **triggerId** | **String**| Id of user | |
| **triggerObject** | [**Trigger54**](Trigger54.md)| Trigger information | |

### Return type

[**TriggerShortResponse**](TriggerShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the trigger was updated successfully |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

