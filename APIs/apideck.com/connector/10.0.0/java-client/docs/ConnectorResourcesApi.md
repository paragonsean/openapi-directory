# ConnectorResourcesApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectorResourcesOne**](ConnectorResourcesApi.md#connectorResourcesOne) | **GET** /connector/connectors/{id}/resources/{resource_id} | Get Connector Resource |


<a id="connectorResourcesOne"></a>
# **connectorResourcesOne**
> GetConnectorResourceResponse connectorResourcesOne(xApideckAppId, id, resourceId, unifiedApi)

Get Connector Resource

Get Connector Resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectorResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ConnectorResourcesApi apiInstance = new ConnectorResourcesApi(defaultClient);
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String id = "id_example"; // String | ID of the record you are acting upon.
    String resourceId = "resourceId_example"; // String | ID of the resource you are acting upon.
    UnifiedApiId unifiedApi = UnifiedApiId.fromValue("accounting"); // UnifiedApiId | Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs
    try {
      GetConnectorResourceResponse result = apiInstance.connectorResourcesOne(xApideckAppId, id, resourceId, unifiedApi);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectorResourcesApi#connectorResourcesOne");
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
| **resourceId** | **String**| ID of the resource you are acting upon. | |
| **unifiedApi** | [**UnifiedApiId**](.md)| Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs | [optional] [enum: accounting, ats, calendar, crm, csp, customer-support, ecommerce, email, email-marketing, expense-management, file-storage, form, hris, lead, payroll, pos, procurement, project-management, script, sms, spreadsheet, team-messaging, issue-tracking, time-registration, transactional-email, vault, data-warehouse] |

### Return type

[**GetConnectorResourceResponse**](GetConnectorResourceResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ConnectorResources |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **0** | Unexpected error |  -  |

