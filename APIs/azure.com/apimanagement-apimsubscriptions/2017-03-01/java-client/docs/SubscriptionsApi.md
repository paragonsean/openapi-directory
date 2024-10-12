# SubscriptionsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionCreateOrUpdate**](SubscriptionsApi.md#subscriptionCreateOrUpdate) | **PUT** /subscriptions/{sid} |  |
| [**subscriptionDelete**](SubscriptionsApi.md#subscriptionDelete) | **DELETE** /subscriptions/{sid} |  |
| [**subscriptionGet**](SubscriptionsApi.md#subscriptionGet) | **GET** /subscriptions/{sid} |  |
| [**subscriptionList**](SubscriptionsApi.md#subscriptionList) | **GET** /subscriptions |  |
| [**subscriptionRegeneratePrimaryKey**](SubscriptionsApi.md#subscriptionRegeneratePrimaryKey) | **POST** /subscriptions/{sid}/regeneratePrimaryKey |  |
| [**subscriptionRegenerateSecondaryKey**](SubscriptionsApi.md#subscriptionRegenerateSecondaryKey) | **POST** /subscriptions/{sid}/regenerateSecondaryKey |  |
| [**subscriptionUpdate**](SubscriptionsApi.md#subscriptionUpdate) | **PATCH** /subscriptions/{sid} |  |


<a id="subscriptionCreateOrUpdate"></a>
# **subscriptionCreateOrUpdate**
> SubscriptionContract subscriptionCreateOrUpdate(sid, apiVersion, parameters, notify)



Creates or updates the subscription of specified user to the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    SubscriptionCreateParameters parameters = new SubscriptionCreateParameters(); // SubscriptionCreateParameters | Create parameters.
    String notify = "False"; // String | Notify the subscriber of the subscription state change to Submitted or Active state.
    try {
      SubscriptionContract result = apiInstance.subscriptionCreateOrUpdate(sid, apiVersion, parameters, notify);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionCreateOrUpdate");
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
| **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**SubscriptionCreateParameters**](SubscriptionCreateParameters.md)| Create parameters. | |
| **notify** | **String**| Notify the subscriber of the subscription state change to Submitted or Active state. | [optional] [default to False] [enum: False, True] |

### Return type

[**SubscriptionContract**](SubscriptionContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user already subscribed to the product. |  -  |
| **201** | The user was successfully subscribed to the product. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDelete"></a>
# **subscriptionDelete**
> subscriptionDelete(sid, ifMatch, apiVersion)



Deletes the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    String ifMatch = "ifMatch_example"; // String | ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.subscriptionDelete(sid, ifMatch, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionDelete");
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
| **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | |
| **ifMatch** | **String**| ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The subscription details were successfully deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionGet"></a>
# **subscriptionGet**
> SubscriptionContract subscriptionGet(sid, apiVersion)



Gets the specified Subscription entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      SubscriptionContract result = apiInstance.subscriptionGet(sid, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionGet");
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
| **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**SubscriptionContract**](SubscriptionContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the specified Subscription entity. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionList"></a>
# **subscriptionList**
> SubscriptionCollection subscriptionList(apiVersion, $filter, $top, $skip)



Lists all subscriptions of the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      SubscriptionCollection result = apiInstance.subscriptionList(apiVersion, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**SubscriptionCollection**](SubscriptionCollection.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of the Subscription entities for the specified API Management service instance. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionRegeneratePrimaryKey"></a>
# **subscriptionRegeneratePrimaryKey**
> subscriptionRegeneratePrimaryKey(sid, apiVersion)



Regenerates primary key of existing subscription of the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.subscriptionRegeneratePrimaryKey(sid, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionRegeneratePrimaryKey");
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
| **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The primary key was successfully regenerated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionRegenerateSecondaryKey"></a>
# **subscriptionRegenerateSecondaryKey**
> subscriptionRegenerateSecondaryKey(sid, apiVersion)



Regenerates secondary key of existing subscription of the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.subscriptionRegenerateSecondaryKey(sid, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionRegenerateSecondaryKey");
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
| **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The secondary key was successfully regenerated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionUpdate"></a>
# **subscriptionUpdate**
> subscriptionUpdate(sid, ifMatch, apiVersion, parameters, notify)



Updates the details of a subscription specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    String ifMatch = "ifMatch_example"; // String | ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    SubscriptionUpdateParameters parameters = new SubscriptionUpdateParameters(); // SubscriptionUpdateParameters | Update parameters.
    String notify = "False"; // String | Notify the subscriber of the subscription state change to Submitted or Active state.
    try {
      apiInstance.subscriptionUpdate(sid, ifMatch, apiVersion, parameters, notify);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#subscriptionUpdate");
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
| **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | |
| **ifMatch** | **String**| ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**SubscriptionUpdateParameters**](SubscriptionUpdateParameters.md)| Update parameters. | |
| **notify** | **String**| Notify the subscriber of the subscription state change to Submitted or Active state. | [optional] [default to False] [enum: False, True] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The subscription details were successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

