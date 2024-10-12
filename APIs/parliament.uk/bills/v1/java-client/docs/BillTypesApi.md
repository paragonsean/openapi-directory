# BillTypesApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1BillTypesGet**](BillTypesApi.md#apiV1BillTypesGet) | **GET** /api/v1/BillTypes | Returns a list of Bill types. |


<a id="apiV1BillTypesGet"></a>
# **apiV1BillTypesGet**
> BillTypeSearchResult apiV1BillTypesGet(category, skip, take)

Returns a list of Bill types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    BillTypesApi apiInstance = new BillTypesApi(defaultClient);
    BillTypeCategory category = BillTypeCategory.fromValue("Public"); // BillTypeCategory | 
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      BillTypeSearchResult result = apiInstance.apiV1BillTypesGet(category, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillTypesApi#apiV1BillTypesGet");
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
| **category** | [**BillTypeCategory**](.md)|  | [optional] [enum: Public, Private, Hybrid] |
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**BillTypeSearchResult**](BillTypeSearchResult.md)

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

