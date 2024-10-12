# TimeRuleApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeRuleDelete**](TimeRuleApi.md#timeRuleDelete) | **DELETE** /timerules/{webId} | Delete a Time Rule. |
| [**timeRuleGet**](TimeRuleApi.md#timeRuleGet) | **GET** /timerules/{webId} | Retrieve a Time Rule. |
| [**timeRuleGetByPath**](TimeRuleApi.md#timeRuleGetByPath) | **GET** /timerules | Retrieve a Time Rule by path. |
| [**timeRuleUpdate**](TimeRuleApi.md#timeRuleUpdate) | **PATCH** /timerules/{webId} | Update a Time Rule by replacing items in its definition. |


<a id="timeRuleDelete"></a>
# **timeRuleDelete**
> timeRuleDelete(webId)

Delete a Time Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TimeRuleApi apiInstance = new TimeRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Time Rule.
    try {
      apiInstance.timeRuleDelete(webId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeRuleApi#timeRuleDelete");
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
| **webId** | **String**| The ID of the Time Rule. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Time Rule was deleted. |  -  |

<a id="timeRuleGet"></a>
# **timeRuleGet**
> TimeRule timeRuleGet(webId, selectedFields, webIdType)

Retrieve a Time Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TimeRuleApi apiInstance = new TimeRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Time Rule.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      TimeRule result = apiInstance.timeRuleGet(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeRuleApi#timeRuleGet");
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
| **webId** | **String**| The ID of the Time Rule. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**TimeRule**](TimeRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Time Rule. |  -  |

<a id="timeRuleGetByPath"></a>
# **timeRuleGetByPath**
> TimeRule timeRuleGetByPath(path, selectedFields, webIdType)

Retrieve a Time Rule by path.

This method returns a Time Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TimeRuleApi apiInstance = new TimeRuleApi(defaultClient);
    String path = "path_example"; // String | The path to the Time Rule.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      TimeRule result = apiInstance.timeRuleGetByPath(path, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeRuleApi#timeRuleGetByPath");
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
| **path** | **String**| The path to the Time Rule. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**TimeRule**](TimeRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Time Rule. |  -  |

<a id="timeRuleUpdate"></a>
# **timeRuleUpdate**
> timeRuleUpdate(webId, timeRule)

Update a Time Rule by replacing items in its definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeRuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    TimeRuleApi apiInstance = new TimeRuleApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the Time Rule.
    TimeRule timeRule = new TimeRule(); // TimeRule | A partial Time Rule containing the desired changes.
    try {
      apiInstance.timeRuleUpdate(webId, timeRule);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeRuleApi#timeRuleUpdate");
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
| **webId** | **String**| The ID of the Time Rule. | |
| **timeRule** | [**TimeRule**](TimeRule.md)| A partial Time Rule containing the desired changes. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Time Rule was updated. |  -  |

