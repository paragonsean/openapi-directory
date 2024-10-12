# RulesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRule**](RulesApi.md#createRule) | **PUT** /rules | Create a rule |
| [**createRuleCategory**](RulesApi.md#createRuleCategory) | **PUT** /rules/categories | Create a rule category |
| [**deleteRule**](RulesApi.md#deleteRule) | **DELETE** /rules/{ruleId} | Delete a rule |
| [**deleteRuleCategory**](RulesApi.md#deleteRuleCategory) | **DELETE** /rules/categories/{ruleCategoryId} | Delete group category |
| [**getRuleCategoryDetails**](RulesApi.md#getRuleCategoryDetails) | **GET** /rules/categories/{ruleCategoryId} | Get rule category details |
| [**getRuleTree**](RulesApi.md#getRuleTree) | **GET** /rules/tree | Get rules tree |
| [**listRules**](RulesApi.md#listRules) | **GET** /rules | List all rules |
| [**ruleDetails**](RulesApi.md#ruleDetails) | **GET** /rules/{ruleId} | Get a rule details |
| [**updateRule**](RulesApi.md#updateRule) | **POST** /rules/{ruleId} | Update a rule details |
| [**updateRuleCategory**](RulesApi.md#updateRuleCategory) | **POST** /rules/categories/{ruleCategoryId} | Update rule category details |


<a id="createRule"></a>
# **createRule**
> CreateRule200Response createRule(ruleNew)

Create a rule

Create a new rule. You can specify a source rule to clone it.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    RuleNew ruleNew = new RuleNew(); // RuleNew | 
    try {
      CreateRule200Response result = apiInstance.createRule(ruleNew);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#createRule");
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
| **ruleNew** | [**RuleNew**](RuleNew.md)|  | [optional] |

### Return type

[**CreateRule200Response**](CreateRule200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules information |  -  |

<a id="createRuleCategory"></a>
# **createRuleCategory**
> CreateRuleCategory200Response createRuleCategory(ruleCategory)

Create a rule category

Create a new rule category

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    RuleCategory ruleCategory = new RuleCategory(); // RuleCategory | 
    try {
      CreateRuleCategory200Response result = apiInstance.createRuleCategory(ruleCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#createRuleCategory");
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
| **ruleCategory** | [**RuleCategory**](RuleCategory.md)|  | |

### Return type

[**CreateRuleCategory200Response**](CreateRuleCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules category information |  -  |

<a id="deleteRule"></a>
# **deleteRule**
> DeleteRule200Response deleteRule(ruleId)

Delete a rule

Delete a rule.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    UUID ruleId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the target rule
    try {
      DeleteRule200Response result = apiInstance.deleteRule(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#deleteRule");
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
| **ruleId** | **UUID**| Id of the target rule | |

### Return type

[**DeleteRule200Response**](DeleteRule200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules information |  -  |

<a id="deleteRuleCategory"></a>
# **deleteRuleCategory**
> DeleteRuleCategory200Response deleteRuleCategory(ruleCategoryId)

Delete group category

Delete a group category. It must have no child groups and no children categories.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    UUID ruleCategoryId = UUID.fromString("e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"); // UUID | 
    try {
      DeleteRuleCategory200Response result = apiInstance.deleteRuleCategory(ruleCategoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#deleteRuleCategory");
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
| **ruleCategoryId** | **UUID**|  | |

### Return type

[**DeleteRuleCategory200Response**](DeleteRuleCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Groups category information |  -  |

<a id="getRuleCategoryDetails"></a>
# **getRuleCategoryDetails**
> GetRuleCategoryDetails200Response getRuleCategoryDetails(ruleCategoryId)

Get rule category details

Get detailed information about a rule category

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    UUID ruleCategoryId = UUID.fromString("e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"); // UUID | 
    try {
      GetRuleCategoryDetails200Response result = apiInstance.getRuleCategoryDetails(ruleCategoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#getRuleCategoryDetails");
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
| **ruleCategoryId** | **UUID**|  | |

### Return type

[**GetRuleCategoryDetails200Response**](GetRuleCategoryDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules category information |  -  |

<a id="getRuleTree"></a>
# **getRuleTree**
> GetRuleTree200Response getRuleTree()

Get rules tree

Get all available rules and their categories in a tree

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    try {
      GetRuleTree200Response result = apiInstance.getRuleTree();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#getRuleTree");
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

[**GetRuleTree200Response**](GetRuleTree200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules information |  -  |

<a id="listRules"></a>
# **listRules**
> ListRules200Response listRules()

List all rules

List all rules

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    try {
      ListRules200Response result = apiInstance.listRules();
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

[**ListRules200Response**](ListRules200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules information |  -  |

<a id="ruleDetails"></a>
# **ruleDetails**
> RuleDetails200Response ruleDetails(ruleId)

Get a rule details

Get the details of a rule

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    UUID ruleId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the target rule
    try {
      RuleDetails200Response result = apiInstance.ruleDetails(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#ruleDetails");
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
| **ruleId** | **UUID**| Id of the target rule | |

### Return type

[**RuleDetails200Response**](RuleDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules information |  -  |

<a id="updateRule"></a>
# **updateRule**
> UpdateRule200Response updateRule(ruleId, ruleWithCategory)

Update a rule details

Update the details of a rule

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    UUID ruleId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the target rule
    RuleWithCategory ruleWithCategory = new RuleWithCategory(); // RuleWithCategory | 
    try {
      UpdateRule200Response result = apiInstance.updateRule(ruleId, ruleWithCategory);
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
| **ruleId** | **UUID**| Id of the target rule | |
| **ruleWithCategory** | [**RuleWithCategory**](RuleWithCategory.md)|  | |

### Return type

[**UpdateRule200Response**](UpdateRule200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules information |  -  |

<a id="updateRuleCategory"></a>
# **updateRuleCategory**
> UpdateRuleCategory200Response updateRuleCategory(ruleCategoryId, ruleCategoryUpdate)

Update rule category details

Update detailed information about a rule category

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    UUID ruleCategoryId = UUID.fromString("e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"); // UUID | 
    RuleCategoryUpdate ruleCategoryUpdate = new RuleCategoryUpdate(); // RuleCategoryUpdate | 
    try {
      UpdateRuleCategory200Response result = apiInstance.updateRuleCategory(ruleCategoryId, ruleCategoryUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#updateRuleCategory");
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
| **ruleCategoryId** | **UUID**|  | |
| **ruleCategoryUpdate** | [**RuleCategoryUpdate**](RuleCategoryUpdate.md)|  | |

### Return type

[**UpdateRuleCategory200Response**](UpdateRuleCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules category information |  -  |

