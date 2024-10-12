# GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/StoredValue/v46*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postChangeStatus**](GeneralApi.md#postChangeStatus) | **POST** /changeStatus | Changes the status of the payment method. |
| [**postCheckBalance**](GeneralApi.md#postCheckBalance) | **POST** /checkBalance | Checks the balance. |
| [**postIssue**](GeneralApi.md#postIssue) | **POST** /issue | Issues a new card. |
| [**postLoad**](GeneralApi.md#postLoad) | **POST** /load | Loads the payment method. |
| [**postMergeBalance**](GeneralApi.md#postMergeBalance) | **POST** /mergeBalance | Merge the balance of two cards. |
| [**postVoidTransaction**](GeneralApi.md#postVoidTransaction) | **POST** /voidTransaction | Voids a transaction. |


<a id="postChangeStatus"></a>
# **postChangeStatus**
> StoredValueStatusChangeResponse postChangeStatus(storedValueStatusChangeRequest)

Changes the status of the payment method.

Changes the status of the provided payment method to the specified status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/StoredValue/v46");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    StoredValueStatusChangeRequest storedValueStatusChangeRequest = new StoredValueStatusChangeRequest(); // StoredValueStatusChangeRequest | 
    try {
      StoredValueStatusChangeResponse result = apiInstance.postChangeStatus(storedValueStatusChangeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postChangeStatus");
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
| **storedValueStatusChangeRequest** | [**StoredValueStatusChangeRequest**](StoredValueStatusChangeRequest.md)|  | [optional] |

### Return type

[**StoredValueStatusChangeResponse**](StoredValueStatusChangeResponse.md)

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
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCheckBalance"></a>
# **postCheckBalance**
> StoredValueBalanceCheckResponse postCheckBalance(storedValueBalanceCheckRequest)

Checks the balance.

Checks the balance of the provided payment method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/StoredValue/v46");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    StoredValueBalanceCheckRequest storedValueBalanceCheckRequest = new StoredValueBalanceCheckRequest(); // StoredValueBalanceCheckRequest | 
    try {
      StoredValueBalanceCheckResponse result = apiInstance.postCheckBalance(storedValueBalanceCheckRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postCheckBalance");
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
| **storedValueBalanceCheckRequest** | [**StoredValueBalanceCheckRequest**](StoredValueBalanceCheckRequest.md)|  | [optional] |

### Return type

[**StoredValueBalanceCheckResponse**](StoredValueBalanceCheckResponse.md)

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
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postIssue"></a>
# **postIssue**
> StoredValueIssueResponse postIssue(storedValueIssueRequest)

Issues a new card.

Issues a new card of the given payment method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/StoredValue/v46");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    StoredValueIssueRequest storedValueIssueRequest = new StoredValueIssueRequest(); // StoredValueIssueRequest | 
    try {
      StoredValueIssueResponse result = apiInstance.postIssue(storedValueIssueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postIssue");
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
| **storedValueIssueRequest** | [**StoredValueIssueRequest**](StoredValueIssueRequest.md)|  | [optional] |

### Return type

[**StoredValueIssueResponse**](StoredValueIssueResponse.md)

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
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLoad"></a>
# **postLoad**
> StoredValueLoadResponse postLoad(storedValueLoadRequest)

Loads the payment method.

Loads the payment method with the specified funds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/StoredValue/v46");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    StoredValueLoadRequest storedValueLoadRequest = new StoredValueLoadRequest(); // StoredValueLoadRequest | 
    try {
      StoredValueLoadResponse result = apiInstance.postLoad(storedValueLoadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postLoad");
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
| **storedValueLoadRequest** | [**StoredValueLoadRequest**](StoredValueLoadRequest.md)|  | [optional] |

### Return type

[**StoredValueLoadResponse**](StoredValueLoadResponse.md)

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
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMergeBalance"></a>
# **postMergeBalance**
> StoredValueBalanceMergeResponse postMergeBalance(storedValueBalanceMergeRequest)

Merge the balance of two cards.

Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/StoredValue/v46");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    StoredValueBalanceMergeRequest storedValueBalanceMergeRequest = new StoredValueBalanceMergeRequest(); // StoredValueBalanceMergeRequest | 
    try {
      StoredValueBalanceMergeResponse result = apiInstance.postMergeBalance(storedValueBalanceMergeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postMergeBalance");
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
| **storedValueBalanceMergeRequest** | [**StoredValueBalanceMergeRequest**](StoredValueBalanceMergeRequest.md)|  | [optional] |

### Return type

[**StoredValueBalanceMergeResponse**](StoredValueBalanceMergeResponse.md)

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
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postVoidTransaction"></a>
# **postVoidTransaction**
> StoredValueVoidResponse postVoidTransaction(storedValueVoidRequest)

Voids a transaction.

Voids the referenced stored value transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/StoredValue/v46");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    StoredValueVoidRequest storedValueVoidRequest = new StoredValueVoidRequest(); // StoredValueVoidRequest | 
    try {
      StoredValueVoidResponse result = apiInstance.postVoidTransaction(storedValueVoidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postVoidTransaction");
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
| **storedValueVoidRequest** | [**StoredValueVoidRequest**](StoredValueVoidRequest.md)|  | [optional] |

### Return type

[**StoredValueVoidResponse**](StoredValueVoidResponse.md)

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
| **500** | Internal Server Error - the server could not process the request. |  -  |

