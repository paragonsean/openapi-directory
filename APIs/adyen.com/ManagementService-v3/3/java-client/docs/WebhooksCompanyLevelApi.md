# WebhooksCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCompaniesCompanyIdWebhooksWebhookId**](WebhooksCompanyLevelApi.md#deleteCompaniesCompanyIdWebhooksWebhookId) | **DELETE** /companies/{companyId}/webhooks/{webhookId} | Remove a webhook |
| [**getCompaniesCompanyIdWebhooks**](WebhooksCompanyLevelApi.md#getCompaniesCompanyIdWebhooks) | **GET** /companies/{companyId}/webhooks | List all webhooks |
| [**getCompaniesCompanyIdWebhooksWebhookId**](WebhooksCompanyLevelApi.md#getCompaniesCompanyIdWebhooksWebhookId) | **GET** /companies/{companyId}/webhooks/{webhookId} | Get a webhook |
| [**patchCompaniesCompanyIdWebhooksWebhookId**](WebhooksCompanyLevelApi.md#patchCompaniesCompanyIdWebhooksWebhookId) | **PATCH** /companies/{companyId}/webhooks/{webhookId} | Update a webhook |
| [**postCompaniesCompanyIdWebhooks**](WebhooksCompanyLevelApi.md#postCompaniesCompanyIdWebhooks) | **POST** /companies/{companyId}/webhooks | Set up a webhook |
| [**postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac**](WebhooksCompanyLevelApi.md#postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac) | **POST** /companies/{companyId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key |
| [**postCompaniesCompanyIdWebhooksWebhookIdTest**](WebhooksCompanyLevelApi.md#postCompaniesCompanyIdWebhooksWebhookIdTest) | **POST** /companies/{companyId}/webhooks/{webhookId}/test | Test a webhook |


<a id="deleteCompaniesCompanyIdWebhooksWebhookId"></a>
# **deleteCompaniesCompanyIdWebhooksWebhookId**
> deleteCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId)

Remove a webhook

Remove the configuration for the webhook identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
    try {
      apiInstance.deleteCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#deleteCompaniesCompanyIdWebhooksWebhookId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **webhookId** | **String**| Unique identifier of the webhook configuration. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - look at the actual response code for the status of the request.  |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdWebhooks"></a>
# **getCompaniesCompanyIdWebhooks**
> ListWebhooksResponse getCompaniesCompanyIdWebhooks(companyId, pageNumber, pageSize)

List all webhooks

Lists all webhook configurations for the company account.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    Integer pageNumber = 56; // Integer | The number of the page to fetch.
    Integer pageSize = 56; // Integer | The number of items to have on a page, maximum 100. The default is 10 items on a page.
    try {
      ListWebhooksResponse result = apiInstance.getCompaniesCompanyIdWebhooks(companyId, pageNumber, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#getCompaniesCompanyIdWebhooks");
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
| **companyId** | **String**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | |
| **pageNumber** | **Integer**| The number of the page to fetch. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] |

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdWebhooksWebhookId"></a>
# **getCompaniesCompanyIdWebhooksWebhookId**
> Webhook getCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId)

Get a webhook

Returns the configuration for the webhook identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    String webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
    try {
      Webhook result = apiInstance.getCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#getCompaniesCompanyIdWebhooksWebhookId");
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
| **companyId** | **String**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | |
| **webhookId** | **String**| Unique identifier of the webhook configuration. | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchCompaniesCompanyIdWebhooksWebhookId"></a>
# **patchCompaniesCompanyIdWebhooksWebhookId**
> Webhook patchCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId, updateCompanyWebhookRequest)

Update a webhook

Make changes to the configuration of the webhook identified in the path. The request contains the new values you want to have in the webhook configuration. The response contains the full configuration for the webhook, which includes the new values from the request.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
    UpdateCompanyWebhookRequest updateCompanyWebhookRequest = new UpdateCompanyWebhookRequest(); // UpdateCompanyWebhookRequest | 
    try {
      Webhook result = apiInstance.patchCompaniesCompanyIdWebhooksWebhookId(companyId, webhookId, updateCompanyWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#patchCompaniesCompanyIdWebhooksWebhookId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **webhookId** | **String**| Unique identifier of the webhook configuration. | |
| **updateCompanyWebhookRequest** | [**UpdateCompanyWebhookRequest**](UpdateCompanyWebhookRequest.md)|  | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdWebhooks"></a>
# **postCompaniesCompanyIdWebhooks**
> Webhook postCompaniesCompanyIdWebhooks(companyId, createCompanyWebhookRequest)

Set up a webhook

Subscribe to receive webhook notifications about events related to your company account. You can add basic authentication to make sure the data is secure.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    CreateCompanyWebhookRequest createCompanyWebhookRequest = new CreateCompanyWebhookRequest(); // CreateCompanyWebhookRequest | 
    try {
      Webhook result = apiInstance.postCompaniesCompanyIdWebhooks(companyId, createCompanyWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#postCompaniesCompanyIdWebhooks");
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
| **companyId** | **String**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | |
| **createCompanyWebhookRequest** | [**CreateCompanyWebhookRequest**](CreateCompanyWebhookRequest.md)|  | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac"></a>
# **postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac**
> GenerateHmacKeyResponse postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac(companyId, webhookId)

Generate an HMAC key

Returns an [HMAC key](https://en.wikipedia.org/wiki/HMAC) for the webhook identified in the path. This key allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you start receiving [HMAC-signed notifications](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures) from Adyen. Find out more about how to [verify HMAC signatures](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
    try {
      GenerateHmacKeyResponse result = apiInstance.postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac(companyId, webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#postCompaniesCompanyIdWebhooksWebhookIdGenerateHmac");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **webhookId** | **String**| Unique identifier of the webhook configuration. | |

### Return type

[**GenerateHmacKeyResponse**](GenerateHmacKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdWebhooksWebhookIdTest"></a>
# **postCompaniesCompanyIdWebhooksWebhookIdTest**
> TestWebhookResponse postCompaniesCompanyIdWebhooksWebhookIdTest(companyId, webhookId, testCompanyWebhookRequest)

Test a webhook

Sends sample notifications to test if the webhook is set up correctly.  We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the webhook is configured for more than 20 merchant accounts, use the &#x60;merchantIds&#x60; array to specify a subset of the merchant accounts for which to send test notifications.  We send four test notifications for each event code you choose. They cover success and failure scenarios for the hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom notifications, we only send the specified custom notification.  The response describes the result of the test. The &#x60;status&#x60; field tells you if the test was successful or not. You can use the other response fields to troubleshoot unsuccessful tests.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksCompanyLevelApi;

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

    WebhooksCompanyLevelApi apiInstance = new WebhooksCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String webhookId = "webhookId_example"; // String | Unique identifier of the webhook configuration.
    TestCompanyWebhookRequest testCompanyWebhookRequest = new TestCompanyWebhookRequest(); // TestCompanyWebhookRequest | 
    try {
      TestWebhookResponse result = apiInstance.postCompaniesCompanyIdWebhooksWebhookIdTest(companyId, webhookId, testCompanyWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksCompanyLevelApi#postCompaniesCompanyIdWebhooksWebhookIdTest");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **webhookId** | **String**| Unique identifier of the webhook configuration. | |
| **testCompanyWebhookRequest** | [**TestCompanyWebhookRequest**](TestCompanyWebhookRequest.md)|  | [optional] |

### Return type

[**TestWebhookResponse**](TestWebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

