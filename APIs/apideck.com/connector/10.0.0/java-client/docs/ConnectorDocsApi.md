# ConnectorDocsApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectorDocsOne**](ConnectorDocsApi.md#connectorDocsOne) | **GET** /connector/connectors/{id}/docs/{doc_id} | Get Connector Doc content |


<a id="connectorDocsOne"></a>
# **connectorDocsOne**
> String connectorDocsOne(xApideckAppId, id, docId)

Get Connector Doc content

Get Connector Doc content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectorDocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ConnectorDocsApi apiInstance = new ConnectorDocsApi(defaultClient);
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String id = "id_example"; // String | ID of the record you are acting upon.
    String docId = "application_owner+oauth_credentials"; // String | ID of the Doc
    try {
      String result = apiInstance.connectorDocsOne(xApideckAppId, id, docId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectorDocsApi#connectorDocsOne");
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
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **id** | **String**| ID of the record you are acting upon. | |
| **docId** | **String**| ID of the Doc | |

### Return type

**String**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/markdown, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connectors |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **0** | Unexpected error |  -  |

