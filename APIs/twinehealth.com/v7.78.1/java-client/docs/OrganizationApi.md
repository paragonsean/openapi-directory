# OrganizationApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchOrganization**](OrganizationApi.md#fetchOrganization) | **GET** /organization/{id} | Get an organization |


<a id="fetchOrganization"></a>
# **fetchOrganization**
> FetchOrganizationResponse fetchOrganization(id)

Get an organization

Get an organization record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String id = "id_example"; // String | Organization identifier
    try {
      FetchOrganizationResponse result = apiInstance.fetchOrganization(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#fetchOrganization");
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
| **id** | **String**| Organization identifier | |

### Return type

[**FetchOrganizationResponse**](FetchOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

