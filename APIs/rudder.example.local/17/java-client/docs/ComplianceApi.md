# ComplianceApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDirectiveComplianceId**](ComplianceApi.md#getDirectiveComplianceId) | **GET** /compliance/directives/{directiveId} | Compliance details by directive |
| [**getDirectivesCompliance**](ComplianceApi.md#getDirectivesCompliance) | **GET** /compliance/directives | Compliance details for all directives |
| [**getGlobalCompliance**](ComplianceApi.md#getGlobalCompliance) | **GET** /compliance | Global compliance |
| [**getNodeCompliance**](ComplianceApi.md#getNodeCompliance) | **GET** /compliance/nodes/{nodeId} | Compliance details by node |
| [**getNodesCompliance**](ComplianceApi.md#getNodesCompliance) | **GET** /compliance/nodes | Compliance details for all nodes |
| [**getRuleCompliance**](ComplianceApi.md#getRuleCompliance) | **GET** /compliance/rules/{ruleId} | Compliance details by rule |
| [**getRulesCompliance**](ComplianceApi.md#getRulesCompliance) | **GET** /compliance/rules | Compliance details for all rules |


<a id="getDirectiveComplianceId"></a>
# **getDirectiveComplianceId**
> GetDirectiveComplianceId200Response getDirectiveComplianceId(directiveId, format)

Compliance details by directive

Get current compliance of a directive of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    UUID directiveId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the directive
    String format = "[\"csv\"]"; // String | format of export
    try {
      GetDirectiveComplianceId200Response result = apiInstance.getDirectiveComplianceId(directiveId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getDirectiveComplianceId");
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
| **directiveId** | **UUID**| Id of the directive | |
| **format** | **String**| format of export | [optional] |

### Return type

[**GetDirectiveComplianceId200Response**](GetDirectiveComplianceId200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDirectivesCompliance"></a>
# **getDirectivesCompliance**
> GetDirectivesCompliance200Response getDirectivesCompliance()

Compliance details for all directives

Get current compliance of all the nodes of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    try {
      GetDirectivesCompliance200Response result = apiInstance.getDirectivesCompliance();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getDirectivesCompliance");
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

[**GetDirectivesCompliance200Response**](GetDirectivesCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGlobalCompliance"></a>
# **getGlobalCompliance**
> GetGlobalCompliance200Response getGlobalCompliance(precision)

Global compliance

Get current global compliance of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    Integer precision = 2; // Integer | Number of digits after comma in compliance percent figures
    try {
      GetGlobalCompliance200Response result = apiInstance.getGlobalCompliance(precision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getGlobalCompliance");
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
| **precision** | **Integer**| Number of digits after comma in compliance percent figures | [optional] [default to 2] |

### Return type

[**GetGlobalCompliance200Response**](GetGlobalCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getNodeCompliance"></a>
# **getNodeCompliance**
> GetNodeCompliance200Response getNodeCompliance(nodeId, level, precision)

Compliance details by node

Get current compliance of a node of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    Integer level = 10; // Integer | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    Integer precision = 2; // Integer | Number of digits after comma in compliance percent figures
    try {
      GetNodeCompliance200Response result = apiInstance.getNodeCompliance(nodeId, level, precision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getNodeCompliance");
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
| **nodeId** | **String**| Id of the target node | |
| **level** | **Integer**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10] |
| **precision** | **Integer**| Number of digits after comma in compliance percent figures | [optional] [default to 2] |

### Return type

[**GetNodeCompliance200Response**](GetNodeCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getNodesCompliance"></a>
# **getNodesCompliance**
> GetNodesCompliance200Response getNodesCompliance(level, precision)

Compliance details for all nodes

Get current compliance of all the nodes of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    Integer level = 10; // Integer | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    Integer precision = 2; // Integer | Number of digits after comma in compliance percent figures
    try {
      GetNodesCompliance200Response result = apiInstance.getNodesCompliance(level, precision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getNodesCompliance");
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
| **level** | **Integer**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10] |
| **precision** | **Integer**| Number of digits after comma in compliance percent figures | [optional] [default to 2] |

### Return type

[**GetNodesCompliance200Response**](GetNodesCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getRuleCompliance"></a>
# **getRuleCompliance**
> GetRuleCompliance200Response getRuleCompliance(ruleId, level, precision)

Compliance details by rule

Get current compliance of a rule of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    UUID ruleId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the target rule
    Integer level = 10; // Integer | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    Integer precision = 2; // Integer | Number of digits after comma in compliance percent figures
    try {
      GetRuleCompliance200Response result = apiInstance.getRuleCompliance(ruleId, level, precision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getRuleCompliance");
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
| **level** | **Integer**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10] |
| **precision** | **Integer**| Number of digits after comma in compliance percent figures | [optional] [default to 2] |

### Return type

[**GetRuleCompliance200Response**](GetRuleCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getRulesCompliance"></a>
# **getRulesCompliance**
> GetRulesCompliance200Response getRulesCompliance(level, precision)

Compliance details for all rules

Get current compliance of all the rules of a Rudder server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ComplianceApi apiInstance = new ComplianceApi(defaultClient);
    Integer level = 10; // Integer | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    Integer precision = 2; // Integer | Number of digits after comma in compliance percent figures
    try {
      GetRulesCompliance200Response result = apiInstance.getRulesCompliance(level, precision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceApi#getRulesCompliance");
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
| **level** | **Integer**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10] |
| **precision** | **Integer**| Number of digits after comma in compliance percent figures | [optional] [default to 2] |

### Return type

[**GetRulesCompliance200Response**](GetRulesCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

