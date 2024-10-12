# AutofollowApiApi

All URIs are relative to *https://api.tradematic.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autofollowStrategiesGet**](AutofollowApiApi.md#autofollowStrategiesGet) | **GET** /autofollow/strategies | Get autofollow strategies list |
| [**autofollowStrategiesPost**](AutofollowApiApi.md#autofollowStrategiesPost) | **POST** /autofollow/strategies | Create new autofollow strategy |
| [**autofollowStrategiesStrategyidContentPut**](AutofollowApiApi.md#autofollowStrategiesStrategyidContentPut) | **PUT** /autofollow/strategies/{strategyid}/content | Update rules for strategy that was created with strategy builder |
| [**autofollowStrategiesStrategyidGet**](AutofollowApiApi.md#autofollowStrategiesStrategyidGet) | **GET** /autofollow/strategies/{strategyid} | Get autofollow strategy by ID |
| [**autofollowStrategiesStrategyidPositionsGet**](AutofollowApiApi.md#autofollowStrategiesStrategyidPositionsGet) | **GET** /autofollow/strategies/{strategyid}/positions | Get positions for strategy |
| [**autofollowStrategiesStrategyidPut**](AutofollowApiApi.md#autofollowStrategiesStrategyidPut) | **PUT** /autofollow/strategies/{strategyid} | Update autofollow strategy |
| [**autofollowStrategiesStrategyidSignalsGet**](AutofollowApiApi.md#autofollowStrategiesStrategyidSignalsGet) | **GET** /autofollow/strategies/{strategyid}/signals | Get trading signals for strategy |
| [**autofollowStrategiesStrategyidSignalsPost**](AutofollowApiApi.md#autofollowStrategiesStrategyidSignalsPost) | **POST** /autofollow/strategies/{strategyid}/signals | Send a new signal for autofollow strategy |


<a id="autofollowStrategiesGet"></a>
# **autofollowStrategiesGet**
> List&lt;Strategy&gt; autofollowStrategiesGet()

Get autofollow strategies list

Get autofollow strategies list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    try {
      List<Strategy> result = apiInstance.autofollowStrategiesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesGet");
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

[**List&lt;Strategy&gt;**](Strategy.md)

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

<a id="autofollowStrategiesPost"></a>
# **autofollowStrategiesPost**
> AutofollowStrategiesPost200Response autofollowStrategiesPost(body)

Create new autofollow strategy

Create new autofollow strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    AutofollowStrategiesPostRequest body = new AutofollowStrategiesPostRequest(); // AutofollowStrategiesPostRequest | 
    try {
      AutofollowStrategiesPost200Response result = apiInstance.autofollowStrategiesPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesPost");
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
| **body** | [**AutofollowStrategiesPostRequest**](AutofollowStrategiesPostRequest.md)|  | |

### Return type

[**AutofollowStrategiesPost200Response**](AutofollowStrategiesPost200Response.md)

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

<a id="autofollowStrategiesStrategyidContentPut"></a>
# **autofollowStrategiesStrategyidContentPut**
> AutofollowStrategiesStrategyidContentPut200Response autofollowStrategiesStrategyidContentPut(strategyid, body)

Update rules for strategy that was created with strategy builder

Update rules for strategy that was created with strategy builder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    AutofollowStrategiesStrategyidContentPutRequest body = new AutofollowStrategiesStrategyidContentPutRequest(); // AutofollowStrategiesStrategyidContentPutRequest | 
    try {
      AutofollowStrategiesStrategyidContentPut200Response result = apiInstance.autofollowStrategiesStrategyidContentPut(strategyid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesStrategyidContentPut");
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
| **strategyid** | **Long**|  | |
| **body** | [**AutofollowStrategiesStrategyidContentPutRequest**](AutofollowStrategiesStrategyidContentPutRequest.md)|  | |

### Return type

[**AutofollowStrategiesStrategyidContentPut200Response**](AutofollowStrategiesStrategyidContentPut200Response.md)

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

<a id="autofollowStrategiesStrategyidGet"></a>
# **autofollowStrategiesStrategyidGet**
> Strategy autofollowStrategiesStrategyidGet(strategyid)

Get autofollow strategy by ID

Get autofollow strategy by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    try {
      Strategy result = apiInstance.autofollowStrategiesStrategyidGet(strategyid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesStrategyidGet");
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
| **strategyid** | **Long**|  | |

### Return type

[**Strategy**](Strategy.md)

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

<a id="autofollowStrategiesStrategyidPositionsGet"></a>
# **autofollowStrategiesStrategyidPositionsGet**
> List&lt;StrategyPosition&gt; autofollowStrategiesStrategyidPositionsGet(strategyid)

Get positions for strategy

Get positions for strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    try {
      List<StrategyPosition> result = apiInstance.autofollowStrategiesStrategyidPositionsGet(strategyid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesStrategyidPositionsGet");
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
| **strategyid** | **Long**|  | |

### Return type

[**List&lt;StrategyPosition&gt;**](StrategyPosition.md)

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

<a id="autofollowStrategiesStrategyidPut"></a>
# **autofollowStrategiesStrategyidPut**
> AutofollowStrategiesStrategyidPut200Response autofollowStrategiesStrategyidPut(strategyid, body)

Update autofollow strategy

Update autofollow strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    AutofollowStrategiesStrategyidPutRequest body = new AutofollowStrategiesStrategyidPutRequest(); // AutofollowStrategiesStrategyidPutRequest | 
    try {
      AutofollowStrategiesStrategyidPut200Response result = apiInstance.autofollowStrategiesStrategyidPut(strategyid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesStrategyidPut");
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
| **strategyid** | **Long**|  | |
| **body** | [**AutofollowStrategiesStrategyidPutRequest**](AutofollowStrategiesStrategyidPutRequest.md)|  | |

### Return type

[**AutofollowStrategiesStrategyidPut200Response**](AutofollowStrategiesStrategyidPut200Response.md)

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

<a id="autofollowStrategiesStrategyidSignalsGet"></a>
# **autofollowStrategiesStrategyidSignalsGet**
> List&lt;Signal&gt; autofollowStrategiesStrategyidSignalsGet(strategyid, count)

Get trading signals for strategy

Get trading signals for strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    Long count = 56L; // Long | 
    try {
      List<Signal> result = apiInstance.autofollowStrategiesStrategyidSignalsGet(strategyid, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesStrategyidSignalsGet");
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
| **strategyid** | **Long**|  | |
| **count** | **Long**|  | |

### Return type

[**List&lt;Signal&gt;**](Signal.md)

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

<a id="autofollowStrategiesStrategyidSignalsPost"></a>
# **autofollowStrategiesStrategyidSignalsPost**
> AutofollowStrategiesStrategyidSignalsPost200Response autofollowStrategiesStrategyidSignalsPost(strategyid, body)

Send a new signal for autofollow strategy

Send a new signal for autofollow strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutofollowApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    AutofollowApiApi apiInstance = new AutofollowApiApi(defaultClient);
    Long strategyid = 56L; // Long | 
    AutofollowStrategiesStrategyidSignalsPostRequest body = new AutofollowStrategiesStrategyidSignalsPostRequest(); // AutofollowStrategiesStrategyidSignalsPostRequest | 
    try {
      AutofollowStrategiesStrategyidSignalsPost200Response result = apiInstance.autofollowStrategiesStrategyidSignalsPost(strategyid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutofollowApiApi#autofollowStrategiesStrategyidSignalsPost");
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
| **strategyid** | **Long**|  | |
| **body** | [**AutofollowStrategiesStrategyidSignalsPostRequest**](AutofollowStrategiesStrategyidSignalsPostRequest.md)|  | |

### Return type

[**AutofollowStrategiesStrategyidSignalsPost200Response**](AutofollowStrategiesStrategyidSignalsPost200Response.md)

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

