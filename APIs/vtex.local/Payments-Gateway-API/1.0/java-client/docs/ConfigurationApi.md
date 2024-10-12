# ConfigurationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**affiliationById**](ConfigurationApi.md#affiliationById) | **GET** /api/pvt/affiliations/{affiliationId} | Affiliation By Id |
| [**affiliations**](ConfigurationApi.md#affiliations) | **GET** /api/pvt/affiliations | Affiliations |
| [**availablePaymentMethods**](ConfigurationApi.md#availablePaymentMethods) | **GET** /api/pvt/merchants/payment-systems | Available Payment Methods |
| [**insertAffiliation**](ConfigurationApi.md#insertAffiliation) | **POST** /api/pvt/affiliations | Insert Affiliation |
| [**insertRule**](ConfigurationApi.md#insertRule) | **POST** /api/pvt/rules | Insert Rule |
| [**putRuleById**](ConfigurationApi.md#putRuleById) | **PUT** /api/pvt/rules/{ruleId} | Rule By Id |
| [**rule**](ConfigurationApi.md#rule) | **DELETE** /api/pvt/rules/{ruleId} | Delete Rule |
| [**ruleById**](ConfigurationApi.md#ruleById) | **GET** /api/pvt/rules/{ruleId} | Rule By Id |
| [**rules**](ConfigurationApi.md#rules) | **GET** /api/pvt/rules | Rules |
| [**updateAffiliation**](ConfigurationApi.md#updateAffiliation) | **PUT** /api/pvt/affiliations/{affiliationId} | Update Affiliation |


<a id="affiliationById"></a>
# **affiliationById**
> affiliationById(affiliationId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Affiliation By Id

Returns associated data for the specified affiliation Id, like name and implementation, for example.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String affiliationId = "e046d326-5421-45ab-95ae-f13d37f260b5"; // String | 
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    try {
      apiInstance.affiliationById(affiliationId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#affiliationById");
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
| **affiliationId** | **String**|  | |
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="affiliations"></a>
# **affiliations**
> affiliations(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Affiliations

Returns all affiliations that your provider can handle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    try {
      apiInstance.affiliations(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#affiliations");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="availablePaymentMethods"></a>
# **availablePaymentMethods**
> List&lt;PaymentSystemsResponse&gt; availablePaymentMethods(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Available Payment Methods

Returns enabled payment methods, like visa, master, bankissueinvoice that are shown for the final user and enabled to receive payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    try {
      List<PaymentSystemsResponse> result = apiInstance.availablePaymentMethods(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#availablePaymentMethods");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |

### Return type

[**List&lt;PaymentSystemsResponse&gt;**](PaymentSystemsResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * x-vtex-operation-id -  <br>  |

<a id="insertAffiliation"></a>
# **insertAffiliation**
> insertAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, insertAffiliationRequest)

Insert Affiliation

Creates a new affiliation and returns a successful response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    InsertAffiliationRequest insertAffiliationRequest = new InsertAffiliationRequest(); // InsertAffiliationRequest | 
    try {
      apiInstance.insertAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, insertAffiliationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#insertAffiliation");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **insertAffiliationRequest** | [**InsertAffiliationRequest**](InsertAffiliationRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="insertRule"></a>
# **insertRule**
> insertRule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, insertRuleRequest)

Insert Rule

Creates a new rule and returns a successful response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    InsertRuleRequest insertRuleRequest = new InsertRuleRequest(); // InsertRuleRequest | 
    try {
      apiInstance.insertRule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, insertRuleRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#insertRule");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **insertRuleRequest** | [**InsertRuleRequest**](InsertRuleRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="putRuleById"></a>
# **putRuleById**
> putRuleById(accept, contentType, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, ruleId, ruleByIdRequest)

Rule By Id

Update Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String ruleId = "ruleId_example"; // String | 
    RuleByIdRequest ruleByIdRequest = new RuleByIdRequest(); // RuleByIdRequest | 
    try {
      apiInstance.putRuleById(accept, contentType, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, ruleId, ruleByIdRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#putRuleById");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **ruleId** | **String**|  | |
| **ruleByIdRequest** | [**RuleByIdRequest**](RuleByIdRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="rule"></a>
# **rule**
> rule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId)

Delete Rule

Deletes rules by specified Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String ruleId = "ruleId_example"; // String | 
    try {
      apiInstance.rule(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#rule");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **ruleId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ruleById"></a>
# **ruleById**
> ruleById(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId)

Rule By Id

Returns rule by specified RuleId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String ruleId = "ruleId_example"; // String | 
    try {
      apiInstance.ruleById(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#ruleById");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **ruleId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="rules"></a>
# **rules**
> rules(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept)

Rules

Returns all rules conditions your provider can handle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    try {
      apiInstance.rules(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#rules");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateAffiliation"></a>
# **updateAffiliation**
> updateAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, affiliationId, updateAffiliationRequest)

Update Affiliation

Returns all affiliations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
    String xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
    String affiliationId = "e046d326-5421-45ab-95ae-f13d37f260b5"; // String | 
    UpdateAffiliationRequest updateAffiliationRequest = new UpdateAffiliationRequest(); // UpdateAffiliationRequest | 
    try {
      apiInstance.updateAffiliation(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, affiliationId, updateAffiliationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#updateAffiliation");
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
| **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | |
| **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | |
| **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | |
| **affiliationId** | **String**|  | |
| **updateAffiliationRequest** | [**UpdateAffiliationRequest**](UpdateAffiliationRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

