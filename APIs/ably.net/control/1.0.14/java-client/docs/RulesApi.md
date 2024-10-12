# RulesApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppIdRulesGet**](RulesApi.md#appsAppIdRulesGet) | **GET** /apps/{app_id}/rules | Lists Reactor rules |
| [**appsAppIdRulesPost**](RulesApi.md#appsAppIdRulesPost) | **POST** /apps/{app_id}/rules | Creates a Reactor rule |
| [**appsAppIdRulesRuleIdDelete**](RulesApi.md#appsAppIdRulesRuleIdDelete) | **DELETE** /apps/{app_id}/rules/{rule_id} | Deletes a Reactor rule |
| [**appsAppIdRulesRuleIdGet**](RulesApi.md#appsAppIdRulesRuleIdGet) | **GET** /apps/{app_id}/rules/{rule_id} | Gets a reactor rule by rule ID |
| [**appsAppIdRulesRuleIdPatch**](RulesApi.md#appsAppIdRulesRuleIdPatch) | **PATCH** /apps/{app_id}/rules/{rule_id} | Updates a Reactor rule |


<a id="appsAppIdRulesGet"></a>
# **appsAppIdRulesGet**
> List&lt;RuleResponse&gt; appsAppIdRulesGet(appId)

Lists Reactor rules

Lists the rules for the application specified by the application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    try {
      List<RuleResponse> result = apiInstance.appsAppIdRulesGet(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#appsAppIdRulesGet");
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
| **appId** | **String**| The application ID. | |

### Return type

[**List&lt;RuleResponse&gt;**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reactor rule list |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesPost"></a>
# **appsAppIdRulesPost**
> RuleResponse appsAppIdRulesPost(appId, rulePost)

Creates a Reactor rule

Creates a rule for the application with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    RulePost rulePost = new RulePost(); // RulePost | The rule properties.
    try {
      RuleResponse result = apiInstance.appsAppIdRulesPost(appId, rulePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#appsAppIdRulesPost");
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
| **appId** | **String**| The application ID. | |
| **rulePost** | [**RulePost**](RulePost.md)| The rule properties. | [optional] |

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reactor rule created |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesRuleIdDelete"></a>
# **appsAppIdRulesRuleIdDelete**
> appsAppIdRulesRuleIdDelete(appId, ruleId)

Deletes a Reactor rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String ruleId = "ruleId_example"; // String | The rule ID.
    try {
      apiInstance.appsAppIdRulesRuleIdDelete(appId, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#appsAppIdRulesRuleIdDelete");
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
| **appId** | **String**| The application ID. | |
| **ruleId** | **String**| The rule ID. | |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Reactor rule deleted |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesRuleIdGet"></a>
# **appsAppIdRulesRuleIdGet**
> RuleResponse appsAppIdRulesRuleIdGet(appId, ruleId)

Gets a reactor rule by rule ID

Returns the rule specified by the rule ID, for the application specified by application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String ruleId = "ruleId_example"; // String | The rule ID.
    try {
      RuleResponse result = apiInstance.appsAppIdRulesRuleIdGet(appId, ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#appsAppIdRulesRuleIdGet");
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
| **appId** | **String**| The application ID. | |
| **ruleId** | **String**| The rule ID. | |

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reactor rule |  -  |
| **401** | Authentication failed |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesRuleIdPatch"></a>
# **appsAppIdRulesRuleIdPatch**
> RuleResponse appsAppIdRulesRuleIdPatch(appId, ruleId, rulePatch)

Updates a Reactor rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String ruleId = "ruleId_example"; // String | The rule ID.
    RulePatch rulePatch = new RulePatch(); // RulePatch | Properties for the rule.
    try {
      RuleResponse result = apiInstance.appsAppIdRulesRuleIdPatch(appId, ruleId, rulePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#appsAppIdRulesRuleIdPatch");
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
| **appId** | **String**| The application ID. | |
| **ruleId** | **String**| The rule ID. | |
| **rulePatch** | [**RulePatch**](RulePatch.md)| Properties for the rule. | [optional] |

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reactor rule updated |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

