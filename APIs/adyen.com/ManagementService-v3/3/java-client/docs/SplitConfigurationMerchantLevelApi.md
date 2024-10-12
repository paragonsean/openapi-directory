# SplitConfigurationMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **DELETE** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Delete a split configuration |
| [**deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId**](SplitConfigurationMerchantLevelApi.md#deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId) | **DELETE** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | Delete a split configuration rule |
| [**getMerchantsMerchantIdSplitConfigurations**](SplitConfigurationMerchantLevelApi.md#getMerchantsMerchantIdSplitConfigurations) | **GET** /merchants/{merchantId}/splitConfigurations | Get a list of split configurations |
| [**getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **GET** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Get a split configuration |
| [**patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **PATCH** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Update split configuration description |
| [**patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId**](SplitConfigurationMerchantLevelApi.md#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId) | **PATCH** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | Update split conditions |
| [**patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId**](SplitConfigurationMerchantLevelApi.md#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId) | **PATCH** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId} | Update the split logic |
| [**postMerchantsMerchantIdSplitConfigurations**](SplitConfigurationMerchantLevelApi.md#postMerchantsMerchantIdSplitConfigurations) | **POST** /merchants/{merchantId}/splitConfigurations | Create a split configuration |
| [**postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **POST** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Create a rule |


<a id="deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId"></a>
# **deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**
> SplitConfiguration deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId)

Delete a split configuration

Deletes the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
    try {
      SplitConfiguration result = apiInstance.deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The unique identifier of the split configuration. | |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId"></a>
# **deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId**
> SplitConfiguration deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId)

Delete a split configuration rule

Deletes the split configuration rule specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
    String ruleId = "ruleId_example"; // String | 
    try {
      SplitConfiguration result = apiInstance.deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The unique identifier of the split configuration. | |
| **ruleId** | **String**|  | |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdSplitConfigurations"></a>
# **getMerchantsMerchantIdSplitConfigurations**
> SplitConfigurationList getMerchantsMerchantIdSplitConfigurations(merchantId)

Get a list of split configurations

Returns the list of split configurations for the merchant account.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    try {
      SplitConfigurationList result = apiInstance.getMerchantsMerchantIdSplitConfigurations(merchantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#getMerchantsMerchantIdSplitConfigurations");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |

### Return type

[**SplitConfigurationList**](SplitConfigurationList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId"></a>
# **getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**
> SplitConfiguration getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId)

Get a split configuration

Returns the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
    try {
      SplitConfiguration result = apiInstance.getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The unique identifier of the split configuration. | |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId"></a>
# **patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**
> SplitConfiguration patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, updateSplitConfigurationRequest)

Update split configuration description

Changes the description of the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
    UpdateSplitConfigurationRequest updateSplitConfigurationRequest = new UpdateSplitConfigurationRequest(); // UpdateSplitConfigurationRequest | 
    try {
      SplitConfiguration result = apiInstance.patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, updateSplitConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The unique identifier of the split configuration. | |
| **updateSplitConfigurationRequest** | [**UpdateSplitConfigurationRequest**](UpdateSplitConfigurationRequest.md)|  | [optional] |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId"></a>
# **patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId**
> SplitConfiguration patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId, updateSplitConfigurationRuleRequest)

Update split conditions

Changes the conditions of the split configuration rule specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The identifier of the split configuration.
    String ruleId = "ruleId_example"; // String | The unique identifier of the split configuration rule.
    UpdateSplitConfigurationRuleRequest updateSplitConfigurationRuleRequest = new UpdateSplitConfigurationRuleRequest(); // UpdateSplitConfigurationRuleRequest | 
    try {
      SplitConfiguration result = apiInstance.patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId, updateSplitConfigurationRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The identifier of the split configuration. | |
| **ruleId** | **String**| The unique identifier of the split configuration rule. | |
| **updateSplitConfigurationRuleRequest** | [**UpdateSplitConfigurationRuleRequest**](UpdateSplitConfigurationRuleRequest.md)|  | [optional] |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId"></a>
# **patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId**
> SplitConfiguration patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId(merchantId, splitConfigurationId, ruleId, splitLogicId, updateSplitConfigurationLogicRequest)

Update the split logic

Changes the split logic specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
    String ruleId = "ruleId_example"; // String | The unique identifier of the split configuration rule.
    String splitLogicId = "splitLogicId_example"; // String | The unique identifier of the split configuration split.
    UpdateSplitConfigurationLogicRequest updateSplitConfigurationLogicRequest = new UpdateSplitConfigurationLogicRequest(); // UpdateSplitConfigurationLogicRequest | 
    try {
      SplitConfiguration result = apiInstance.patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId(merchantId, splitConfigurationId, ruleId, splitLogicId, updateSplitConfigurationLogicRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The unique identifier of the split configuration. | |
| **ruleId** | **String**| The unique identifier of the split configuration rule. | |
| **splitLogicId** | **String**| The unique identifier of the split configuration split. | |
| **updateSplitConfigurationLogicRequest** | [**UpdateSplitConfigurationLogicRequest**](UpdateSplitConfigurationLogicRequest.md)|  | [optional] |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdSplitConfigurations"></a>
# **postMerchantsMerchantIdSplitConfigurations**
> SplitConfiguration postMerchantsMerchantIdSplitConfigurations(merchantId, splitConfiguration)

Create a split configuration

Creates a split configuration for the merchant account specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    SplitConfiguration splitConfiguration = new SplitConfiguration(); // SplitConfiguration | 
    try {
      SplitConfiguration result = apiInstance.postMerchantsMerchantIdSplitConfigurations(merchantId, splitConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#postMerchantsMerchantIdSplitConfigurations");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfiguration** | [**SplitConfiguration**](SplitConfiguration.md)|  | [optional] |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId"></a>
# **postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**
> SplitConfiguration postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, splitConfigurationRule)

Create a rule

Creates a rule in the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplitConfigurationMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SplitConfigurationMerchantLevelApi apiInstance = new SplitConfigurationMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
    SplitConfigurationRule splitConfigurationRule = new SplitConfigurationRule(); // SplitConfigurationRule | 
    try {
      SplitConfiguration result = apiInstance.postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, splitConfigurationRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplitConfigurationMerchantLevelApi#postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **splitConfigurationId** | **String**| The unique identifier of the split configuration. | |
| **splitConfigurationRule** | [**SplitConfigurationRule**](SplitConfigurationRule.md)|  | [optional] |

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

