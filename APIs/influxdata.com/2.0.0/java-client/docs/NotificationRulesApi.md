# NotificationRulesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNotificationRule**](NotificationRulesApi.md#createNotificationRule) | **POST** /notificationRules | Add a notification rule |
| [**deleteNotificationRulesID**](NotificationRulesApi.md#deleteNotificationRulesID) | **DELETE** /notificationRules/{ruleID} | Delete a notification rule |
| [**deleteNotificationRulesIDLabelsID**](NotificationRulesApi.md#deleteNotificationRulesIDLabelsID) | **DELETE** /notificationRules/{ruleID}/labels/{labelID} | Delete label from a notification rule |
| [**getNotificationRules**](NotificationRulesApi.md#getNotificationRules) | **GET** /notificationRules | List all notification rules |
| [**getNotificationRulesID**](NotificationRulesApi.md#getNotificationRulesID) | **GET** /notificationRules/{ruleID} | Retrieve a notification rule |
| [**getNotificationRulesIDLabels**](NotificationRulesApi.md#getNotificationRulesIDLabels) | **GET** /notificationRules/{ruleID}/labels | List all labels for a notification rule |
| [**patchNotificationRulesID**](NotificationRulesApi.md#patchNotificationRulesID) | **PATCH** /notificationRules/{ruleID} | Update a notification rule |
| [**postNotificationRuleIDLabels**](NotificationRulesApi.md#postNotificationRuleIDLabels) | **POST** /notificationRules/{ruleID}/labels | Add a label to a notification rule |
| [**putNotificationRulesID**](NotificationRulesApi.md#putNotificationRulesID) | **PUT** /notificationRules/{ruleID} | Update a notification rule |


<a id="createNotificationRule"></a>
# **createNotificationRule**
> NotificationRule createNotificationRule(postNotificationRule)

Add a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    PostNotificationRule postNotificationRule = new PostNotificationRule(); // PostNotificationRule | Notification rule to create
    try {
      NotificationRule result = apiInstance.createNotificationRule(postNotificationRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#createNotificationRule");
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
| **postNotificationRule** | [**PostNotificationRule**](PostNotificationRule.md)| Notification rule to create | |

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Notification rule created |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteNotificationRulesID"></a>
# **deleteNotificationRulesID**
> deleteNotificationRulesID(ruleID, zapTraceSpan)

Delete a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteNotificationRulesID(ruleID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#deleteNotificationRulesID");
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
| **ruleID** | **String**| The notification rule ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | The check was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteNotificationRulesIDLabelsID"></a>
# **deleteNotificationRulesIDLabelsID**
> deleteNotificationRulesIDLabelsID(ruleID, labelID, zapTraceSpan)

Delete label from a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    String labelID = "labelID_example"; // String | The ID of the label to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteNotificationRulesIDLabelsID(ruleID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#deleteNotificationRulesIDLabelsID");
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
| **ruleID** | **String**| The notification rule ID. | |
| **labelID** | **String**| The ID of the label to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Rule or label not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getNotificationRules"></a>
# **getNotificationRules**
> NotificationRules getNotificationRules(orgID, zapTraceSpan, offset, limit, checkID, tag)

List all notification rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String orgID = "orgID_example"; // String | Only show notification rules that belong to a specific organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Integer offset = 56; // Integer | 
    Integer limit = 20; // Integer | 
    String checkID = "checkID_example"; // String | Only show notifications that belong to the specific check ID.
    String tag = "env:prod"; // String | Only return notification rules that \"would match\" statuses which contain the tag key value pairs provided.
    try {
      NotificationRules result = apiInstance.getNotificationRules(orgID, zapTraceSpan, offset, limit, checkID, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#getNotificationRules");
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
| **orgID** | **String**| Only show notification rules that belong to a specific organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **checkID** | **String**| Only show notifications that belong to the specific check ID. | [optional] |
| **tag** | **String**| Only return notification rules that \&quot;would match\&quot; statuses which contain the tag key value pairs provided. | [optional] |

### Return type

[**NotificationRules**](NotificationRules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification rules |  -  |
| **0** | Unexpected error |  -  |

<a id="getNotificationRulesID"></a>
# **getNotificationRulesID**
> NotificationRule getNotificationRulesID(ruleID, zapTraceSpan)

Retrieve a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      NotificationRule result = apiInstance.getNotificationRulesID(ruleID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#getNotificationRulesID");
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
| **ruleID** | **String**| The notification rule ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The notification rule requested |  -  |
| **0** | Unexpected error |  -  |

<a id="getNotificationRulesIDLabels"></a>
# **getNotificationRulesIDLabels**
> LabelsResponse getNotificationRulesIDLabels(ruleID, zapTraceSpan)

List all labels for a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getNotificationRulesIDLabels(ruleID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#getNotificationRulesIDLabels");
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
| **ruleID** | **String**| The notification rule ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all labels for a notification rule |  -  |
| **0** | Unexpected error |  -  |

<a id="patchNotificationRulesID"></a>
# **patchNotificationRulesID**
> NotificationRule patchNotificationRulesID(ruleID, notificationRuleUpdate, zapTraceSpan)

Update a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    NotificationRuleUpdate notificationRuleUpdate = new NotificationRuleUpdate(); // NotificationRuleUpdate | Notification rule update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      NotificationRule result = apiInstance.patchNotificationRulesID(ruleID, notificationRuleUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#patchNotificationRulesID");
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
| **ruleID** | **String**| The notification rule ID. | |
| **notificationRuleUpdate** | [**NotificationRuleUpdate**](NotificationRuleUpdate.md)| Notification rule update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated notification rule |  -  |
| **404** | The notification rule was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="postNotificationRuleIDLabels"></a>
# **postNotificationRuleIDLabels**
> LabelResponse postNotificationRuleIDLabels(ruleID, labelMapping, zapTraceSpan)

Add a label to a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postNotificationRuleIDLabels(ruleID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#postNotificationRuleIDLabels");
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
| **ruleID** | **String**| The notification rule ID. | |
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The label was added to the notification rule |  -  |
| **0** | Unexpected error |  -  |

<a id="putNotificationRulesID"></a>
# **putNotificationRulesID**
> NotificationRule putNotificationRulesID(ruleID, notificationRule, zapTraceSpan)

Update a notification rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationRulesApi apiInstance = new NotificationRulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    NotificationRule notificationRule = new NotificationRule(); // NotificationRule | Notification rule update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      NotificationRule result = apiInstance.putNotificationRulesID(ruleID, notificationRule, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationRulesApi#putNotificationRulesID");
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
| **ruleID** | **String**| The notification rule ID. | |
| **notificationRule** | [**NotificationRule**](NotificationRule.md)| Notification rule update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated notification rule |  -  |
| **404** | The notification rule was not found |  -  |
| **0** | Unexpected error |  -  |

