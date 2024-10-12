# DefaultApi

All URIs are relative to *https://api.landregistry.gov.uk/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDeed**](DefaultApi.md#addDeed) | **POST** /deed/ | Deed |


<a id="addDeed"></a>
# **addDeed**
> String addDeed(body)

Deed

The post Deed endpoint creates a new deed based on the JSON provided.  The reponse will return a URL that can retrieve the created deed.   &gt; REQUIRED: Land Registry system requests Conveyancer to confirm that the Borrowers identity has been established in accordance with Section 111 of the Network Access Agreement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.landregistry.gov.uk/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    DeedApplication body = new DeedApplication(); // DeedApplication | 
    try {
      String result = apiInstance.addDeed(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addDeed");
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
| **body** | [**DeedApplication**](DeedApplication.md)|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | URL to the GET endpoint for the deed is returned on successful creation.  |  -  |
| **400** | Bad Request due to invalid schema. Response will include 1 or more schema errors  |  -  |

