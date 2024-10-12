# DestinationDefinitionSpecificationApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDestinationDefinitionSpecification**](DestinationDefinitionSpecificationApi.md#getDestinationDefinitionSpecification) | **POST** /v1/destination_definition_specifications/get | Get specification for a destinationDefinition |


<a id="getDestinationDefinitionSpecification"></a>
# **getDestinationDefinitionSpecification**
> DestinationDefinitionSpecificationRead getDestinationDefinitionSpecification(destinationDefinitionIdWithWorkspaceId)

Get specification for a destinationDefinition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionSpecificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionSpecificationApi apiInstance = new DestinationDefinitionSpecificationApi(defaultClient);
    DestinationDefinitionIdWithWorkspaceId destinationDefinitionIdWithWorkspaceId = new DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
    try {
      DestinationDefinitionSpecificationRead result = apiInstance.getDestinationDefinitionSpecification(destinationDefinitionIdWithWorkspaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionSpecificationApi#getDestinationDefinitionSpecification");
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
| **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | |

### Return type

[**DestinationDefinitionSpecificationRead**](DestinationDefinitionSpecificationRead.md)

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

