# GetVisitorHistoryApi

All URIs are relative to *http://service.miataru.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVisitorHistory**](GetVisitorHistoryApi.md#getVisitorHistory) | **POST** /GetVisitorHistory |  |


<a id="getVisitorHistory"></a>
# **getVisitorHistory**
> MiataruGetVisitorHistoryResponse getVisitorHistory(body)



Visitor History is stored on the server with every request to the location or location history information of a device. There is a server-side setting that controls up to how many Visitors the server is storing in the Visitor History before it removes the oldest one. To request the Visitor History of a particular device the client sends the following POST request to the GetVisitorHistory service URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetVisitorHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.miataru.com/v1");

    GetVisitorHistoryApi apiInstance = new GetVisitorHistoryApi(defaultClient);
    MiataruGetVisitorHistoryRequest body = new MiataruGetVisitorHistoryRequest(); // MiataruGetVisitorHistoryRequest | the complex JSON formatted datastructure to get the visitor history of one device
    try {
      MiataruGetVisitorHistoryResponse result = apiInstance.getVisitorHistory(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetVisitorHistoryApi#getVisitorHistory");
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
| **body** | [**MiataruGetVisitorHistoryRequest**](MiataruGetVisitorHistoryRequest.md)| the complex JSON formatted datastructure to get the visitor history of one device | |

### Return type

[**MiataruGetVisitorHistoryResponse**](MiataruGetVisitorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | visitor history response |  -  |

