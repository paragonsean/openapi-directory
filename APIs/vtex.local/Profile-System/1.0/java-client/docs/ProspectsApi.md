# ProspectsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProspect**](ProspectsApi.md#createProspect) | **POST** /api/storage/profile-system/prospects | Create prospect |
| [**deleteProspect**](ProspectsApi.md#deleteProspect) | **DELETE** /api/storage/profile-system/prospects/{prospectId} | Delete prospect |
| [**getProspect**](ProspectsApi.md#getProspect) | **GET** /api/storage/profile-system/prospects/{prospectId} | Get prospect |
| [**getUnmaskedProspect**](ProspectsApi.md#getUnmaskedProspect) | **GET** /api/storage/profile-system/prospects/{prospectId}/unmask | Get unmasked prospect |
| [**updateProspect**](ProspectsApi.md#updateProspect) | **PATCH** /api/storage/profile-system/prospects/{prospectId} | Update prospect |


<a id="createProspect"></a>
# **createProspect**
> Object createProspect(contentType, accept, body)

Create prospect

Creates new prospect.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;prospectId&#x60; used to retrieve information on a specific prospect later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProspectsApi;

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

    ProspectsApi apiInstance = new ProspectsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createProspect(contentType, accept, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProspectsApi#createProspect");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteProspect"></a>
# **deleteProspect**
> deleteProspect(contentType, accept, prospectId)

Delete prospect

Deletes a prospect by &#x60;prospectId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProspectsApi;

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

    ProspectsApi apiInstance = new ProspectsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
    try {
      apiInstance.deleteProspect(contentType, accept, prospectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProspectsApi#deleteProspect");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | |

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
| **204** | No content |  -  |

<a id="getProspect"></a>
# **getProspect**
> List&lt;Object&gt; getProspect(contentType, accept, prospectId)

Get prospect

Retrieves the information of a specific prospect, by its &#x60;prospectId&#x60;.    &gt; For security and privacy reasons, this request returns masked prospect data. For unmasked information, see Get unmasked prospect.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProspectsApi;

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

    ProspectsApi apiInstance = new ProspectsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
    try {
      List<Object> result = apiInstance.getProspect(contentType, accept, prospectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProspectsApi#getProspect");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUnmaskedProspect"></a>
# **getUnmaskedProspect**
> List&lt;Object&gt; getUnmaskedProspect(contentType, accept, prospectId, reason)

Get unmasked prospect

Retrieves unmasked information of a specific prospect, by its &#x60;prospectId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProspectsApi;

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

    ProspectsApi apiInstance = new ProspectsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
    String reason = "data-validation"; // String | Reason for requesting unmasked data.
    try {
      List<Object> result = apiInstance.getUnmaskedProspect(contentType, accept, prospectId, reason);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProspectsApi#getUnmaskedProspect");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **reason** | **String**| Reason for requesting unmasked data. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateProspect"></a>
# **updateProspect**
> Object updateProspect(contentType, accept, prospectId, body)

Update prospect

Updates one or more fields of an existing prospect.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProspectsApi;

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

    ProspectsApi apiInstance = new ProspectsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String prospectId = "51clk394-8534-447e-a0ca-1803p669c987"; // String | ID of the prospect as returned by the Create prospect endpoint's response, in the `id` field.
    Object body = null; // Object | 
    try {
      Object result = apiInstance.updateProspect(contentType, accept, prospectId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProspectsApi#updateProspect");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **prospectId** | **String**| ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

