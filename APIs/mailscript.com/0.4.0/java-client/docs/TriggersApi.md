# TriggersApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTrigger**](TriggersApi.md#addTrigger) | **POST** /triggers | Setup a trigger |
| [**deleteTrigger**](TriggersApi.md#deleteTrigger) | **DELETE** /triggers/{trigger} | Delete a trigger |
| [**getAllTriggers**](TriggersApi.md#getAllTriggers) | **GET** /triggers | Get all triggers you have access to |
| [**updateTrigger**](TriggersApi.md#updateTrigger) | **PUT** /triggers/{trigger} | Update a trigger |


<a id="addTrigger"></a>
# **addTrigger**
> AddTriggerResponse addTrigger(addTriggerRequest)

Setup a trigger



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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    AddTriggerRequest addTriggerRequest = new AddTriggerRequest(); // AddTriggerRequest | Trigger body
    try {
      AddTriggerResponse result = apiInstance.addTrigger(addTriggerRequest);
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
| **addTriggerRequest** | [**AddTriggerRequest**](AddTriggerRequest.md)| Trigger body | |

### Return type

[**AddTriggerResponse**](AddTriggerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful add operation |  -  |
| **400** | Invalid input |  -  |
| **403** | Bad credentials |  -  |

<a id="deleteTrigger"></a>
# **deleteTrigger**
> deleteTrigger(trigger)

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String trigger = "trigger_example"; // String | ID of the trigger
    try {
      apiInstance.deleteTrigger(trigger);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#deleteTrigger");
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
| **trigger** | **String**| ID of the trigger | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful delete operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

<a id="getAllTriggers"></a>
# **getAllTriggers**
> GetAllTriggersResponse getAllTriggers()

Get all triggers you have access to



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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    try {
      GetAllTriggersResponse result = apiInstance.getAllTriggers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#getAllTriggers");
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

[**GetAllTriggersResponse**](GetAllTriggersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid input |  -  |
| **403** | Bad credentials |  -  |

<a id="updateTrigger"></a>
# **updateTrigger**
> updateTrigger(trigger, addTriggerRequest)

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String trigger = "trigger_example"; // String | ID of the trigger
    AddTriggerRequest addTriggerRequest = new AddTriggerRequest(); // AddTriggerRequest | Trigger body
    try {
      apiInstance.updateTrigger(trigger, addTriggerRequest);
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
| **trigger** | **String**| ID of the trigger | |
| **addTriggerRequest** | [**AddTriggerRequest**](AddTriggerRequest.md)| Trigger body | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful update operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

