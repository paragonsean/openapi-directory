# BuilderApiApi

All URIs are relative to *https://api.tradematic.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**builderRulesGet**](BuilderApiApi.md#builderRulesGet) | **GET** /builder/rules | Get strategy builder rules list |
| [**builderRulesRuleidGet**](BuilderApiApi.md#builderRulesRuleidGet) | **GET** /builder/rules/{ruleid} | Get strategy builder rules by ID |


<a id="builderRulesGet"></a>
# **builderRulesGet**
> List&lt;Rule&gt; builderRulesGet()

Get strategy builder rules list

Get strategy builder rules list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuilderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    BuilderApiApi apiInstance = new BuilderApiApi(defaultClient);
    try {
      List<Rule> result = apiInstance.builderRulesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuilderApiApi#builderRulesGet");
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

[**List&lt;Rule&gt;**](Rule.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="builderRulesRuleidGet"></a>
# **builderRulesRuleidGet**
> List&lt;Rule&gt; builderRulesRuleidGet(ruleid)

Get strategy builder rules by ID

Get strategy builder rules by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuilderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    BuilderApiApi apiInstance = new BuilderApiApi(defaultClient);
    Long ruleid = 56L; // Long | 
    try {
      List<Rule> result = apiInstance.builderRulesRuleidGet(ruleid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuilderApiApi#builderRulesRuleidGet");
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
| **ruleid** | **Long**|  | |

### Return type

[**List&lt;Rule&gt;**](Rule.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

