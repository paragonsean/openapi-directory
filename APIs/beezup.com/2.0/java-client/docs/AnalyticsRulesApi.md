# AnalyticsRulesApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRule**](AnalyticsRulesApi.md#createRule) | **POST** /v2/user/analytics/{storeId}/rules | Rule creation |
| [**deleteRule**](AnalyticsRulesApi.md#deleteRule) | **DELETE** /v2/user/analytics/{storeId}/rules/{ruleId} | Delete Rule |
| [**disableRule**](AnalyticsRulesApi.md#disableRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/disable | Disable rule |
| [**enableRule**](AnalyticsRulesApi.md#enableRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/enable | Enable rule |
| [**getRule**](AnalyticsRulesApi.md#getRule) | **GET** /v2/user/analytics/{storeId}/rules/{ruleId} | Gets the rule |
| [**getRules**](AnalyticsRulesApi.md#getRules) | **GET** /v2/user/analytics/{storeId}/rules | Gets the list of rules for a given store |
| [**getRulesExecutions**](AnalyticsRulesApi.md#getRulesExecutions) | **GET** /v2/user/analytics/{storeId}/rules/executions | Get the rules execution history |
| [**moveDownRule**](AnalyticsRulesApi.md#moveDownRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/movedown | Move the rule down |
| [**moveUpRule**](AnalyticsRulesApi.md#moveUpRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/moveup | Move the rule up |
| [**runRule**](AnalyticsRulesApi.md#runRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/run | Run rule |
| [**runRules**](AnalyticsRulesApi.md#runRules) | **POST** /v2/user/analytics/{storeId}/rules/run | Run all rules for this store |
| [**updateRule**](AnalyticsRulesApi.md#updateRule) | **PATCH** /v2/user/analytics/{storeId}/rules/{ruleId} | Update Rule |


<a id="createRule"></a>
# **createRule**
> createRule(storeId, createRuleRequest)

Rule creation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    CreateRuleRequest createRuleRequest = new CreateRuleRequest(); // CreateRuleRequest | 
    try {
      apiInstance.createRule(storeId, createRuleRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#createRule");
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
| **storeId** | **String**| Your store identifier | |
| **createRuleRequest** | [**CreateRuleRequest**](CreateRuleRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Rule created |  -  |
| **400** | Period on filter cannot be custom or filter does not exist |  -  |
| **401** | Store not allowed to use rules. Please upgrade your offer or contact us. |  -  |
| **403** | Reached the maximum amount of rules allowed for your offer. Please upgrade your offer or contact us. |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="deleteRule"></a>
# **deleteRule**
> deleteRule(storeId, ruleId)

Delete Rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      apiInstance.deleteRule(storeId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#deleteRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

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
| **204** | Rule deleted |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="disableRule"></a>
# **disableRule**
> disableRule(storeId, ruleId)

Disable rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      apiInstance.disableRule(storeId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#disableRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

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
| **204** | Rule disabled |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="enableRule"></a>
# **enableRule**
> enableRule(storeId, ruleId)

Enable rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      apiInstance.enableRule(storeId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#enableRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

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
| **204** | Rune enabled |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getRule"></a>
# **getRule**
> Rule getRule(storeId, ruleId)

Gets the rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      Rule result = apiInstance.getRule(storeId, ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#getRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Rule |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getRules"></a>
# **getRules**
> RuleList getRules(storeId)

Gets the list of rules for a given store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      RuleList result = apiInstance.getRules(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#getRules");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**RuleList**](RuleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule list |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getRulesExecutions"></a>
# **getRulesExecutions**
> RuleExecutionReportings getRulesExecutions(storeId, pageNumber, pageSize)

Get the rules execution history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    Integer pageNumber = 56; // Integer | The page to retrieve
    Integer pageSize = 56; // Integer | The count of rule history to retrieve
    try {
      RuleExecutionReportings result = apiInstance.getRulesExecutions(storeId, pageNumber, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#getRulesExecutions");
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
| **storeId** | **String**| Your store identifier | |
| **pageNumber** | **Integer**| The page to retrieve | |
| **pageSize** | **Integer**| The count of rule history to retrieve | |

### Return type

[**RuleExecutionReportings**](RuleExecutionReportings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules executions list |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="moveDownRule"></a>
# **moveDownRule**
> moveDownRule(storeId, ruleId)

Move the rule down

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      apiInstance.moveDownRule(storeId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#moveDownRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

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
| **204** | Rule moved down |  -  |
| **400** | Priority can only be changed when more than one rule is defined |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="moveUpRule"></a>
# **moveUpRule**
> moveUpRule(storeId, ruleId)

Move the rule up

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      apiInstance.moveUpRule(storeId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#moveUpRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

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
| **204** | Rule moved up |  -  |
| **400** | Priority can only be changed when more than one rule is defined |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="runRule"></a>
# **runRule**
> runRule(storeId, ruleId)

Run rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    try {
      apiInstance.runRule(storeId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#runRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |

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
| **204** | Rule executed |  -  |
| **400** | Rule is not enabled. Please enable this run before trying to run it. |  -  |
| **401** | Store not allowed to use rules. Please upgrade your offer or contact us. |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="runRules"></a>
# **runRules**
> runRules(storeId)

Run all rules for this store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      apiInstance.runRules(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#runRules");
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
| **storeId** | **String**| Your store identifier | |

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
| **204** | All rules executed. |  -  |
| **401** | Store not allowed to use rules. Please upgrade your offer or contact us. |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="updateRule"></a>
# **updateRule**
> updateRule(storeId, ruleId, updateRuleRequest)

Update Rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsRulesApi apiInstance = new AnalyticsRulesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ruleId = "ruleId_example"; // String | Your rule identifier
    UpdateRuleRequest updateRuleRequest = new UpdateRuleRequest(); // UpdateRuleRequest | 
    try {
      apiInstance.updateRule(storeId, ruleId, updateRuleRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsRulesApi#updateRule");
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
| **storeId** | **String**| Your store identifier | |
| **ruleId** | **String**| Your rule identifier | |
| **updateRuleRequest** | [**UpdateRuleRequest**](UpdateRuleRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Rule updated |  -  |
| **400** | Filter does not exist or period on filter cannot be custom |  -  |
| **401** | Store not allowed to use rules. Please upgrade your offer or contact us. |  -  |
| **404** | Rule not found |  -  |
| **409** | Rules for this store are currently running. Please try again later. |  -  |
| **0** | Occurs when something goes wrong |  -  |

