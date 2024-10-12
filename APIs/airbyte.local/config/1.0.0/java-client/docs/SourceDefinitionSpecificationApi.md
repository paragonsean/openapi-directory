# SourceDefinitionSpecificationApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSourceDefinitionSpecification**](SourceDefinitionSpecificationApi.md#getSourceDefinitionSpecification) | **POST** /v1/source_definition_specifications/get | Get specification for a SourceDefinition. |


<a id="getSourceDefinitionSpecification"></a>
# **getSourceDefinitionSpecification**
> SourceDefinitionSpecificationRead getSourceDefinitionSpecification(sourceDefinitionIdWithWorkspaceId)

Get specification for a SourceDefinition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionSpecificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionSpecificationApi apiInstance = new SourceDefinitionSpecificationApi(defaultClient);
    SourceDefinitionIdWithWorkspaceId sourceDefinitionIdWithWorkspaceId = new SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
    try {
      SourceDefinitionSpecificationRead result = apiInstance.getSourceDefinitionSpecification(sourceDefinitionIdWithWorkspaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionSpecificationApi#getSourceDefinitionSpecification");
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
| **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | |

### Return type

[**SourceDefinitionSpecificationRead**](SourceDefinitionSpecificationRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

