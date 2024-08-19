# RulesApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppIdRulesGet**](RulesApi.md#appsAppIdRulesGet) | **GET** /apps/{app_id}/rules | Lists Integration rules |
| [**appsAppIdRulesPost**](RulesApi.md#appsAppIdRulesPost) | **POST** /apps/{app_id}/rules | Creates a Integration Rule |
| [**appsAppIdRulesRuleIdDelete**](RulesApi.md#appsAppIdRulesRuleIdDelete) | **DELETE** /apps/{app_id}/rules/{rule_id} | Deletes a Integration Rule |
| [**appsAppIdRulesRuleIdGet**](RulesApi.md#appsAppIdRulesRuleIdGet) | **GET** /apps/{app_id}/rules/{rule_id} | Gets a Integration Rule by ID |
| [**appsAppIdRulesRuleIdPatch**](RulesApi.md#appsAppIdRulesRuleIdPatch) | **PATCH** /apps/{app_id}/rules/{rule_id} | Updates a Integration Rule |


<a id="appsAppIdRulesGet"></a>
# **appsAppIdRulesGet**
> List&lt;RuleResponse&gt; appsAppIdRulesGet(appId)

Lists Integration rules

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
    String appId = "appId_example"; // String | 
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
| **appId** | **String**|  | |

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
| **200** | Integration Rule list |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesPost"></a>
# **appsAppIdRulesPost**
> RuleResponse appsAppIdRulesPost(appId, rulePost)

Creates a Integration Rule

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
    String appId = "appId_example"; // String | 
    RulePost rulePost = new RulePost(); // RulePost | 
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
| **appId** | **String**|  | |
| **rulePost** | [**RulePost**](RulePost.md)|  | [optional] |

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
| **201** | Integration Rule created |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **403** | Forbidden |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesRuleIdDelete"></a>
# **appsAppIdRulesRuleIdDelete**
> appsAppIdRulesRuleIdDelete(appId, ruleId)

Deletes a Integration Rule

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
    String appId = "appId_example"; // String | 
    String ruleId = "ruleId_example"; // String | 
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
| **appId** | **String**|  | |
| **ruleId** | **String**|  | |

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
| **204** | Integration Rule deleted |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesRuleIdGet"></a>
# **appsAppIdRulesRuleIdGet**
> RuleResponse appsAppIdRulesRuleIdGet(appId, ruleId)

Gets a Integration Rule by ID

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
    String appId = "appId_example"; // String | 
    String ruleId = "ruleId_example"; // String | 
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
| **appId** | **String**|  | |
| **ruleId** | **String**|  | |

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
| **200** | Integration Rule |  -  |
| **401** | Authentication failed |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdRulesRuleIdPatch"></a>
# **appsAppIdRulesRuleIdPatch**
> RuleResponse appsAppIdRulesRuleIdPatch(appId, ruleId, rulePatch)

Updates a Integration Rule

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
    String appId = "appId_example"; // String | 
    String ruleId = "ruleId_example"; // String | 
    RulePatch rulePatch = new RulePatch(); // RulePatch | 
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
| **appId** | **String**|  | |
| **ruleId** | **String**|  | |
| **rulePatch** | [**RulePatch**](RulePatch.md)|  | [optional] |

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
| **200** | Integration Rule updated |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

