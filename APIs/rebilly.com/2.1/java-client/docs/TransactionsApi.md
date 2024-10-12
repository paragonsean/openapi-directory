# TransactionsApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteTransactionTimeline**](TransactionsApi.md#deleteTransactionTimeline) | **DELETE** /transactions/{id}/timeline/{messageId} | Delete a Transaction Timeline message |
| [**getTransaction**](TransactionsApi.md#getTransaction) | **GET** /transactions/{id} | Retrieve a Transaction |
| [**getTransactionCollection**](TransactionsApi.md#getTransactionCollection) | **GET** /transactions | Retrieve a list of transactions |
| [**getTransactionTimeline**](TransactionsApi.md#getTransactionTimeline) | **GET** /transactions/{id}/timeline/{messageId} | Retrieve a transaction Timeline message |
| [**getTransactionTimelineCollection**](TransactionsApi.md#getTransactionTimelineCollection) | **GET** /transactions/{id}/timeline | Retrieve a list of transaction timeline messages |
| [**patchTransaction**](TransactionsApi.md#patchTransaction) | **PATCH** /transactions/{id} | Update a transaction |
| [**postPayout**](TransactionsApi.md#postPayout) | **POST** /payouts | Create a credit transaction |
| [**postReadyToPay**](TransactionsApi.md#postReadyToPay) | **POST** /ready-to-pay | Ready to Pay |
| [**postTransaction**](TransactionsApi.md#postTransaction) | **POST** /transactions | Create a transaction |
| [**postTransactionQuery**](TransactionsApi.md#postTransactionQuery) | **POST** /transactions/{id}/query | Query a Transaction |
| [**postTransactionRefund**](TransactionsApi.md#postTransactionRefund) | **POST** /transactions/{id}/refund | Refund a Transaction |
| [**postTransactionTimeline**](TransactionsApi.md#postTransactionTimeline) | **POST** /transactions/{id}/timeline | Create a transaction Timeline comment |
| [**postTransactionUpdate**](TransactionsApi.md#postTransactionUpdate) | **POST** /transactions/{id}/update | Update a Transaction status |


<a id="deleteTransactionTimeline"></a>
# **deleteTransactionTimeline**
> deleteTransactionTimeline(id, messageId, organizationId)

Delete a Transaction Timeline message

Delete a Transaction Timeline message with predefined identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String messageId = "messageId_example"; // String | The Transaction Timeline message ID.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      apiInstance.deleteTransactionTimeline(id, messageId, organizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#deleteTransactionTimeline");
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
| **id** | **String**| The resource identifier string. | |
| **messageId** | **String**| The Transaction Timeline message ID. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

null (empty response body)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Transaction Timeline message was deleted. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **409** | Conflict. |  -  |

<a id="getTransaction"></a>
# **getTransaction**
> Transaction getTransaction(id, organizationId, expand)

Retrieve a Transaction

Retrieve a Transaction with specified identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      Transaction result = apiInstance.getTransaction(id, organizationId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransaction");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getTransactionCollection"></a>
# **getTransactionCollection**
> List&lt;Transaction&gt; getTransactionCollection(organizationId, limit, offset, filter, q, sort, expand)

Retrieve a list of transactions

Retrieve a list of transactions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    String q = "q_example"; // String | The partial search of the text fields.
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      List<Transaction> result = apiInstance.getTransactionCollection(organizationId, limit, offset, filter, q, sort, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionCollection");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |
| **q** | **String**| The partial search of the text fields. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**List&lt;Transaction&gt;**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of transactions was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="getTransactionTimeline"></a>
# **getTransactionTimeline**
> TransactionTimeline getTransactionTimeline(id, messageId, organizationId)

Retrieve a transaction Timeline message

Retrieve a timeline message with specified identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String messageId = "messageId_example"; // String | The Transaction Timeline message ID.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      TransactionTimeline result = apiInstance.getTransactionTimeline(id, messageId, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionTimeline");
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
| **id** | **String**| The resource identifier string. | |
| **messageId** | **String**| The Transaction Timeline message ID. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**TransactionTimeline**](TransactionTimeline.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Timeline message was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getTransactionTimelineCollection"></a>
# **getTransactionTimelineCollection**
> List&lt;TransactionTimeline&gt; getTransactionTimelineCollection(id, organizationId, limit, offset, filter)

Retrieve a list of transaction timeline messages

Retrieve a list of transaction timeline messages. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    try {
      List<TransactionTimeline> result = apiInstance.getTransactionTimelineCollection(id, organizationId, limit, offset, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionTimelineCollection");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |

### Return type

[**List&lt;TransactionTimeline&gt;**](TransactionTimeline.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of transaction timeline messages was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="patchTransaction"></a>
# **patchTransaction**
> Transaction patchTransaction(id, patchTransactionRequest, organizationId)

Update a transaction

Update a transaction&#39;s custom fields. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    PatchTransactionRequest patchTransactionRequest = new PatchTransactionRequest(); // PatchTransactionRequest | Use the patch transaction request to modify custom fields.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Transaction result = apiInstance.patchTransaction(id, patchTransactionRequest, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#patchTransaction");
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
| **id** | **String**| The resource identifier string. | |
| **patchTransactionRequest** | [**PatchTransactionRequest**](PatchTransactionRequest.md)| Use the patch transaction request to modify custom fields. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction was updated successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="postPayout"></a>
# **postPayout**
> Transaction postPayout(payoutRequest, organizationId)

Create a credit transaction

Create a transaction of type &#x60;credit&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    PayoutRequest payoutRequest = new PayoutRequest(); // PayoutRequest | Transaction resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Transaction result = apiInstance.postPayout(payoutRequest, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postPayout");
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
| **payoutRequest** | [**PayoutRequest**](PayoutRequest.md)| Transaction resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction was created. |  -  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **409** | Conflict. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postReadyToPay"></a>
# **postReadyToPay**
> List&lt;ReadyToPayMethodsInner&gt; postReadyToPay(organizationId, coreReadyToPay)

Ready to Pay

Get available payment methods for a specific transaction or a purchase.  The payment methods order shown to a customer **SHOULD** be the same as the order in the response.  The list of available methods is generated from available [Gateway Accounts](https://user-api-docs.rebilly.com/tag/Gateway-Accounts) intersected with the last matched [Rules Engine](https://user-api-docs.rebilly.com/tag/Rules#operation/PutEventRule) &#x60;adjust-ready-to-pay&#x60; action on &#x60;ready-to-pay-requested&#x60; event.  If there were no actions matched for the specific request – all methods supported by the Gateway Accounts are sent.  To invert this behavior – place an all-matching rule at the very end of the &#x60;ready-to-pay-requested&#x60; event in Rules Engine with an empty &#x60;paymentMethods&#x60; property of the &#x60;adjust-ready-to-pay&#x60; action. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    CoreReadyToPay coreReadyToPay = new CoreReadyToPay(); // CoreReadyToPay | 
    try {
      List<ReadyToPayMethodsInner> result = apiInstance.postReadyToPay(organizationId, coreReadyToPay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postReadyToPay");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **coreReadyToPay** | [**CoreReadyToPay**](CoreReadyToPay.md)|  | [optional] |

### Return type

[**List&lt;ReadyToPayMethodsInner&gt;**](ReadyToPayMethodsInner.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment methods retrieved. |  -  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postTransaction"></a>
# **postTransaction**
> Transaction postTransaction(transactionRequest, organizationId, expand)

Create a transaction

Create a transaction of type &#x60;sale&#x60; or &#x60;authorize&#x60;. This endpoint supports two main styles of transactions:   1. A real-time decision and response.   2. User approval/interaction is required.  A real-time decision is very familiar.  You send a request, and inspect the &#x60;result&#x60; of the response for &#x60;approved&#x60; or &#x60;declined&#x60;.  However, many transactions, especially those for alternative methods, require the user to interact with a 3rd party.  You may be able to envision PayPal, for example, the user must give permission to complete the payment (or accept the billing agreement).  Even payment cards may require user approval in the case of 3D secure authentication.  In the event that approval is required, you will receive a response back and notice that the &#x60;result&#x60; is &#x60;unknown&#x60;.  You will find that the &#x60;status&#x60; is &#x60;waiting-approval&#x60;. And you will find in the &#x60;_links&#x60; section of the response a link for the &#x60;approvalUrl&#x60;.  In this case you would either open the &#x60;approvalUrl&#x60; in an iframe or in a pop (better workflow for mobile). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    TransactionRequest transactionRequest = new TransactionRequest(); // TransactionRequest | Transaction resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      Transaction result = apiInstance.postTransaction(transactionRequest, organizationId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postTransaction");
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
| **transactionRequest** | [**TransactionRequest**](TransactionRequest.md)| Transaction resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction was created. |  -  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **409** | Conflict. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postTransactionQuery"></a>
# **postTransactionQuery**
> TransactionQuery postTransactionQuery(id, organizationId)

Query a Transaction

Query a Transaction with a specified identifier string. The query will contact the gateway account to find the result and amount/currency. The response should be analyzed.  If deemed appropriate, the transaction could be updated using the Transaction Update API. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      TransactionQuery result = apiInstance.postTransactionQuery(id, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postTransactionQuery");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**TransactionQuery**](TransactionQuery.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction was queried successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="postTransactionRefund"></a>
# **postTransactionRefund**
> Transaction postTransactionRefund(id, transactionRefund, organizationId)

Refund a Transaction

Refund a Transaction with specified identifier string. Note that the refund will be in the same currency as the original transaction. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    TransactionRefund transactionRefund = new TransactionRefund(); // TransactionRefund | Transaction resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Transaction result = apiInstance.postTransactionRefund(id, transactionRefund, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postTransactionRefund");
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
| **id** | **String**| The resource identifier string. | |
| **transactionRefund** | [**TransactionRefund**](TransactionRefund.md)| Transaction resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction was refunded successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="postTransactionTimeline"></a>
# **postTransactionTimeline**
> TransactionTimeline postTransactionTimeline(id, transactionTimeline, organizationId)

Create a transaction Timeline comment

Create a transaction Timeline comment. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    TransactionTimeline transactionTimeline = new TransactionTimeline(); // TransactionTimeline | Transaction Timeline resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      TransactionTimeline result = apiInstance.postTransactionTimeline(id, transactionTimeline, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postTransactionTimeline");
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
| **id** | **String**| The resource identifier string. | |
| **transactionTimeline** | [**TransactionTimeline**](TransactionTimeline.md)| Transaction Timeline resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**TransactionTimeline**](TransactionTimeline.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction Timeline comment was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postTransactionUpdate"></a>
# **postTransactionUpdate**
> Transaction postTransactionUpdate(id, transactionUpdate, organizationId)

Update a Transaction status

Update a Transaction manually to completed status with given result with optional currency and amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    TransactionUpdate transactionUpdate = new TransactionUpdate(); // TransactionUpdate | 
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      Transaction result = apiInstance.postTransactionUpdate(id, transactionUpdate, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#postTransactionUpdate");
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
| **id** | **String**| The resource identifier string. | |
| **transactionUpdate** | [**TransactionUpdate**](TransactionUpdate.md)|  | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction was updated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

