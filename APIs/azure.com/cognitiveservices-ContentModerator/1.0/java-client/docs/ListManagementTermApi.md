# ListManagementTermApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listManagementTermAddTerm**](ListManagementTermApi.md#listManagementTermAddTerm) | **POST** /contentmoderator/lists/v1.0/termlists/{listId}/terms/{term} |  |
| [**listManagementTermDeleteAllTerms**](ListManagementTermApi.md#listManagementTermDeleteAllTerms) | **DELETE** /contentmoderator/lists/v1.0/termlists/{listId}/terms |  |
| [**listManagementTermDeleteTerm**](ListManagementTermApi.md#listManagementTermDeleteTerm) | **DELETE** /contentmoderator/lists/v1.0/termlists/{listId}/terms/{term} |  |
| [**listManagementTermGetAllTerms**](ListManagementTermApi.md#listManagementTermGetAllTerms) | **GET** /contentmoderator/lists/v1.0/termlists/{listId}/terms |  |


<a id="listManagementTermAddTerm"></a>
# **listManagementTermAddTerm**
> listManagementTermAddTerm(listId, term, language)



Add a term to the term list with list Id equal to list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermApi apiInstance = new ListManagementTermApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String term = "term_example"; // String | Term to be deleted
    String language = "language_example"; // String | Language of the terms.
    try {
      apiInstance.listManagementTermAddTerm(listId, term, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermApi#listManagementTermAddTerm");
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
| **listId** | **String**| List Id of the image list. | |
| **term** | **String**| Term to be deleted | |
| **language** | **String**| Language of the terms. | |

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
| **201** | Created |  -  |
| **0** | Error response. |  -  |

<a id="listManagementTermDeleteAllTerms"></a>
# **listManagementTermDeleteAllTerms**
> String listManagementTermDeleteAllTerms(listId, language)



Deletes all terms from the list with list Id equal to the list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermApi apiInstance = new ListManagementTermApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String language = "language_example"; // String | Language of the terms.
    try {
      String result = apiInstance.listManagementTermDeleteAllTerms(listId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermApi#listManagementTermDeleteAllTerms");
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
| **listId** | **String**| List Id of the image list. | |
| **language** | **String**| Language of the terms. | |

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response. |  -  |

<a id="listManagementTermDeleteTerm"></a>
# **listManagementTermDeleteTerm**
> String listManagementTermDeleteTerm(listId, term, language)



Deletes a term from the list with list Id equal to the list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermApi apiInstance = new ListManagementTermApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String term = "term_example"; // String | Term to be deleted
    String language = "language_example"; // String | Language of the terms.
    try {
      String result = apiInstance.listManagementTermDeleteTerm(listId, term, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermApi#listManagementTermDeleteTerm");
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
| **listId** | **String**| List Id of the image list. | |
| **term** | **String**| Term to be deleted | |
| **language** | **String**| Language of the terms. | |

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response. |  -  |

<a id="listManagementTermGetAllTerms"></a>
# **listManagementTermGetAllTerms**
> Terms listManagementTermGetAllTerms(listId, language, offset, limit)



Gets all terms from the list with list Id equal to the list Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListManagementTermApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ListManagementTermApi apiInstance = new ListManagementTermApi(defaultClient);
    String listId = "listId_example"; // String | List Id of the image list.
    String language = "language_example"; // String | Language of the terms.
    Integer offset = 56; // Integer | The pagination start index.
    Integer limit = 56; // Integer | The max limit.
    try {
      Terms result = apiInstance.listManagementTermGetAllTerms(listId, language, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListManagementTermApi#listManagementTermGetAllTerms");
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
| **listId** | **String**| List Id of the image list. | |
| **language** | **String**| Language of the terms. | |
| **offset** | **Integer**| The pagination start index. | [optional] |
| **limit** | **Integer**| The max limit. | [optional] |

### Return type

[**Terms**](Terms.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

