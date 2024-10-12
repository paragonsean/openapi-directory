# RulesApi

All URIs are relative to *https://api.ritc.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRule**](RulesApi.md#addRule) | **POST** /rules |  |
| [**getRule**](RulesApi.md#getRule) | **GET** /rules/{rule_id} |  |
| [**listRules**](RulesApi.md#listRules) | **GET** /rules |  |
| [**removeRule**](RulesApi.md#removeRule) | **DELETE** /rules/{rule_id} |  |
| [**runRule**](RulesApi.md#runRule) | **POST** /rules/{rule_id}/run |  |
| [**updateRule**](RulesApi.md#updateRule) | **PATCH** /rules/{rule_id} |  |


<a id="addRule"></a>
# **addRule**
> RuleFullResponse addRule(ruleObject)



Create a new rule

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
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    Rule ruleObject = new Rule(); // Rule | Rule information
    try {
      RuleFullResponse result = apiInstance.addRule(ruleObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#addRule");
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
| **ruleObject** | [**Rule**](Rule.md)| Rule information | |

### Return type

[**RuleFullResponse**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A rule was created |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="getRule"></a>
# **getRule**
> List&lt;RuleFullResponse&gt; getRule(ruleId)



Get a rule

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
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String ruleId = "ruleId_example"; // String | Id of rule
    try {
      List<RuleFullResponse> result = apiInstance.getRule(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#getRule");
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
| **ruleId** | **String**| Id of rule | |

### Return type

[**List&lt;RuleFullResponse&gt;**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about a rule |  -  |
| **0** | Unexpected error |  -  |

<a id="listRules"></a>
# **listRules**
> List&lt;RuleShortResponse&gt; listRules()



List rules

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
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    try {
      List<RuleShortResponse> result = apiInstance.listRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#listRules");
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

[**List&lt;RuleShortResponse&gt;**](RuleShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of rules in an app |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="removeRule"></a>
# **removeRule**
> removeRule(ruleId)



Delete a rule

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
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String ruleId = "ruleId_example"; // String | Id of rule
    try {
      apiInstance.removeRule(ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#removeRule");
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
| **ruleId** | **String**| Id of rule | |

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
| **200** | The rule was successfully removed |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="runRule"></a>
# **runRule**
> Object runRule(ruleId, initialData)



Run a rule

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
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String ruleId = "ruleId_example"; // String | Id of rule
    Object initialData = null; // Object | Initial data
    try {
      Object result = apiInstance.runRule(ruleId, initialData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#runRule");
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
| **ruleId** | **String**| Id of rule | |
| **initialData** | **Object**| Initial data | [optional] |

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A rule ran successfully |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="updateRule"></a>
# **updateRule**
> RuleFullResponse updateRule(ruleId, ruleObject)



Update information about a specific rule

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
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String ruleId = "ruleId_example"; // String | Id of user
    Rule ruleObject = new Rule(); // Rule | Rule information
    try {
      RuleFullResponse result = apiInstance.updateRule(ruleId, ruleObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#updateRule");
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
| **ruleId** | **String**| Id of user | |
| **ruleObject** | [**Rule**](Rule.md)| Rule information | |

### Return type

[**RuleFullResponse**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the rule was updated successfully |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

