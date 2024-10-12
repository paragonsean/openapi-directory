# ClustersApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**validatedocumentbyclusters**](ClustersApi.md#validatedocumentbyclusters) | **POST** /api/dataentities/{dataEntityName}/documents/{id}/clusters | Validate document by clusters |


<a id="validatedocumentbyclusters"></a>
# **validatedocumentbyclusters**
> validatedocumentbyclusters(dataEntityName, accept, id, body)

Validate document by clusters

Check if a document is present in one or more clusters (specific set of field values).    &gt; There is a limit of five rules per request.

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
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    String body = [
    {
        "name": "male",        
        "rule": "gender=male"
    },
    {
        "name": "complex",
        "rule": "((gender=male AND percent=0.35) AND any is null) AND (name=*go*)"
    },    
    {
        "name": "complex2",
        "rule": "((gender=male AND percent=0.35) AND any is not null) OR (name=*go*)"
    },
    {
        "name": "createdIn",
        "rule": "createdIn between 2015-10-28 AND 2015-10-30"
    }
]; // String | Request body for validating a document by clusters
    try {
      apiInstance.validatedocumentbyclusters(dataEntityName, accept, id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#validatedocumentbyclusters");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |
| **body** | **String**| Request body for validating a document by clusters | |

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
| **200** | OK |  -  |

