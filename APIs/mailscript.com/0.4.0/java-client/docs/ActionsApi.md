# ActionsApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAction**](ActionsApi.md#addAction) | **POST** /actions | Add an action |
| [**deleteAction**](ActionsApi.md#deleteAction) | **DELETE** /actions/{action} | Delete an action |
| [**getAllActions**](ActionsApi.md#getAllActions) | **GET** /actions | Get all actions for the user |
| [**updateAction**](ActionsApi.md#updateAction) | **PUT** /actions/{action} | Update an action key |


<a id="addAction"></a>
# **addAction**
> AddActionResponse addAction(addActionRequest)

Add an action

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    AddActionRequest addActionRequest = new AddActionRequest(); // AddActionRequest | Add action body
    try {
      AddActionResponse result = apiInstance.addAction(addActionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#addAction");
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
| **addActionRequest** | [**AddActionRequest**](AddActionRequest.md)| Add action body | |

### Return type

[**AddActionResponse**](AddActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |
| **400** | Failure |  -  |
| **403** | Not authorized or bad code |  -  |

<a id="deleteAction"></a>
# **deleteAction**
> deleteAction(action)

Delete an action

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String action = "action_example"; // String | ID of the action
    try {
      apiInstance.deleteAction(action);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#deleteAction");
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
| **action** | **String**| ID of the action | |

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

<a id="getAllActions"></a>
# **getAllActions**
> GetAllActionsResponse getAllActions()

Get all actions for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    try {
      GetAllActionsResponse result = apiInstance.getAllActions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#getAllActions");
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

[**GetAllActionsResponse**](GetAllActionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **403** | Bad credentials |  -  |

<a id="updateAction"></a>
# **updateAction**
> Key updateAction(action, addActionRequest)

Update an action key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String action = "action_example"; // String | ID of action
    AddActionRequest addActionRequest = new AddActionRequest(); // AddActionRequest | Action body
    try {
      Key result = apiInstance.updateAction(action, addActionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#updateAction");
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
| **action** | **String**| ID of action | |
| **addActionRequest** | [**AddActionRequest**](AddActionRequest.md)| Action body | |

### Return type

[**Key**](Key.md)

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

