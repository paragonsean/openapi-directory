# ClientsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clientsPostByModel**](ClientsApi.md#clientsPostByModel) | **POST** /api/Clients |  |


<a id="clientsPostByModel"></a>
# **clientsPostByModel**
> ClientModel clientsPostByModel(model)



Description: This operation submits the Fact Finder data to an external system.&lt;br /&gt;                Purpose: Allows Fact Finder data to be persisted in another system for that system&#39;s consumption and use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    ClientsModel model = new ClientsModel(); // ClientsModel | 
    try {
      ClientModel result = apiInstance.clientsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#clientsPostByModel");
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
| **model** | [**ClientsModel**](ClientsModel.md)|  | |

### Return type

[**ClientModel**](ClientModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Client data access. |  -  |
| **403** | Request is restricted for access to Client. |  -  |

