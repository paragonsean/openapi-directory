# PublicationTypesApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1PublicationTypesGet**](PublicationTypesApi.md#apiV1PublicationTypesGet) | **GET** /api/v1/PublicationTypes | Returns a list of publication types. |


<a id="apiV1PublicationTypesGet"></a>
# **apiV1PublicationTypesGet**
> PublicationTypeSearchResult apiV1PublicationTypesGet(skip, take)

Returns a list of publication types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicationTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    PublicationTypesApi apiInstance = new PublicationTypesApi(defaultClient);
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      PublicationTypeSearchResult result = apiInstance.apiV1PublicationTypesGet(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicationTypesApi#apiV1PublicationTypesGet");
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
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**PublicationTypeSearchResult**](PublicationTypeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

