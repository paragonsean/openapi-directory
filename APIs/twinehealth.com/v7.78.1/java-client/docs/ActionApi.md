# ActionApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAction**](ActionApi.md#createAction) | **POST** /action | Create action |
| [**fetchAction**](ActionApi.md#fetchAction) | **GET** /action/{id} | Get an action |
| [**updateAction**](ActionApi.md#updateAction) | **PATCH** /action/{id} | Update an action |


<a id="createAction"></a>
# **createAction**
> CreateActionResponse createAction(createActionRequest)

Create action

Create a plan action

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    ActionApi apiInstance = new ActionApi(defaultClient);
    CreateActionRequest createActionRequest = new CreateActionRequest(); // CreateActionRequest | 
    try {
      CreateActionResponse result = apiInstance.createAction(createActionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#createAction");
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
| **createActionRequest** | [**CreateActionRequest**](CreateActionRequest.md)|  | |

### Return type

[**CreateActionResponse**](CreateActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchAction"></a>
# **fetchAction**
> FetchActionResponse fetchAction(id)

Get an action

Get a health action from a patient&#39;s plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "id_example"; // String | Action identifier
    try {
      FetchActionResponse result = apiInstance.fetchAction(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#fetchAction");
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
| **id** | **String**| Action identifier | |

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="updateAction"></a>
# **updateAction**
> UpdateActionResponse updateAction(id, updateActionRequest)

Update an action

Update a health action from a patient&#39;s plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "id_example"; // String | Action identifier
    UpdateActionRequest updateActionRequest = new UpdateActionRequest(); // UpdateActionRequest | 
    try {
      UpdateActionResponse result = apiInstance.updateAction(id, updateActionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#updateAction");
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
| **id** | **String**| Action identifier | |
| **updateActionRequest** | [**UpdateActionRequest**](UpdateActionRequest.md)|  | |

### Return type

[**UpdateActionResponse**](UpdateActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

