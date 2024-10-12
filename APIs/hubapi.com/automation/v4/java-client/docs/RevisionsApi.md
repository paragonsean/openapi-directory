# RevisionsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage**](RevisionsApi.md#getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage) | **GET** /automation/v4/actions/{appId}/{definitionId}/revisions | Get all revisions for a given definition |
| [**getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById**](RevisionsApi.md#getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById) | **GET** /automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId} | Gets a revision for a given definition by revision id |


<a id="getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage"></a>
# **getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage**
> CollectionResponsePublicActionRevisionForwardPaging getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage(definitionId, appId, limit, after)

Get all revisions for a given definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RevisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    RevisionsApi apiInstance = new RevisionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    Integer appId = 56; // Integer | 
    Integer limit = 56; // Integer | The maximum number of results to display per page.
    String after = "after_example"; // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
    try {
      CollectionResponsePublicActionRevisionForwardPaging result = apiInstance.getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage(definitionId, appId, limit, after);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RevisionsApi#getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage");
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
| **definitionId** | **String**|  | |
| **appId** | **Integer**|  | |
| **limit** | **Integer**| The maximum number of results to display per page. | [optional] |
| **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] |

### Return type

[**CollectionResponsePublicActionRevisionForwardPaging**](CollectionResponsePublicActionRevisionForwardPaging.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById"></a>
# **getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById**
> PublicActionRevision getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById(definitionId, revisionId, appId)

Gets a revision for a given definition by revision id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RevisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    RevisionsApi apiInstance = new RevisionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String revisionId = "revisionId_example"; // String | 
    Integer appId = 56; // Integer | 
    try {
      PublicActionRevision result = apiInstance.getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById(definitionId, revisionId, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RevisionsApi#getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById");
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
| **definitionId** | **String**|  | |
| **revisionId** | **String**|  | |
| **appId** | **Integer**|  | |

### Return type

[**PublicActionRevision**](PublicActionRevision.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

