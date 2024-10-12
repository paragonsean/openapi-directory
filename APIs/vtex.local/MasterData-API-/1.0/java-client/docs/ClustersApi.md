# ClustersApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**validateDocumentbyClusters**](ClustersApi.md#validateDocumentbyClusters) | **POST** /api/dataentities/{acronym}/documents/{id}/clusters | Validate Document by Clusters |


<a id="validateDocumentbyClusters"></a>
# **validateDocumentbyClusters**
> validateDocumentbyClusters(accept, acronym, id, requestBody)

Validate Document by Clusters



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

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

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    List<Object> requestBody = [{"name":"male","rule":"gender=male"},{"name":"complex","rule":"((gender=male AND percent=0.35) AND any is null) AND (name=*go*)"},{"name":"complex2","rule":"((gender=male AND percent=0.35) AND any is not null) OR (name=*go*)"},{"name":"createdIn","rule":"createdIn between 2015-10-28 AND 2015-10-30"}]; // List<Object> | 
    try {
      apiInstance.validateDocumentbyClusters(accept, acronym, id, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#validateDocumentbyClusters");
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
| **requestBody** | [**List&lt;Object&gt;**](Object.md)|  | |

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

