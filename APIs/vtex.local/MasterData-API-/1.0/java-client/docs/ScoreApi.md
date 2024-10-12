# ScoreApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletescorebyfield**](ScoreApi.md#deletescorebyfield) | **DELETE** /api/dataentities/{acronym}/documents/{id}/score/{field-name} | Delete score by field |
| [**putscorebyfield**](ScoreApi.md#putscorebyfield) | **PUT** /api/dataentities/{acronym}/documents/{id}/score/{field-name} | Put score by field |
| [**putscores**](ScoreApi.md#putscores) | **PUT** /api/dataentities/{acronym}/documents/{id}/score | Put scores |


<a id="deletescorebyfield"></a>
# **deletescorebyfield**
> deletescorebyfield(accept, acronym, id, fieldName, deletescorebyfieldRequest)

Delete score by field

Allows you to remove a key from a specific field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

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

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    String fieldName = "{{field-name}}"; // String | Name of the field to remove score from
    DeletescorebyfieldRequest deletescorebyfieldRequest = new DeletescorebyfieldRequest(); // DeletescorebyfieldRequest | 
    try {
      apiInstance.deletescorebyfield(accept, acronym, id, fieldName, deletescorebyfieldRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#deletescorebyfield");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **fieldName** | **String**| Name of the field to remove score from | [default to {{field-name}}] |
| **deletescorebyfieldRequest** | [**DeletescorebyfieldRequest**](DeletescorebyfieldRequest.md)|  | |

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

<a id="putscorebyfield"></a>
# **putscorebyfield**
> putscorebyfield(accept, acronym, id, fieldName, putscorebyfieldRequest)

Put score by field

It allows to punctuate in a specific field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

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

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    String fieldName = "{{field-name}}"; // String | Name of the field to score
    PutscorebyfieldRequest putscorebyfieldRequest = new PutscorebyfieldRequest(); // PutscorebyfieldRequest | 
    try {
      apiInstance.putscorebyfield(accept, acronym, id, fieldName, putscorebyfieldRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#putscorebyfield");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **fieldName** | **String**| Name of the field to score | [default to {{field-name}}] |
| **putscorebyfieldRequest** | [**PutscorebyfieldRequest**](PutscorebyfieldRequest.md)|  | |

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

<a id="putscores"></a>
# **putscores**
> putscores(accept, acronym, id, putscoresRequest)

Put scores

It allows punctuate in more than one field and more than one key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

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

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    List<PutscoresRequest> putscoresRequest = Arrays.asList(); // List<PutscoresRequest> | 
    try {
      apiInstance.putscores(accept, acronym, id, putscoresRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#putscores");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **putscoresRequest** | [**List&lt;PutscoresRequest&gt;**](PutscoresRequest.md)|  | |

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

