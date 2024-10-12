# SshApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllSshKeys**](SshApi.md#getAllSshKeys) | **GET** /ssh | Overview of SSH keys |


<a id="getAllSshKeys"></a>
# **getAllSshKeys**
> List&lt;SshKeyDetail&gt; getAllSshKeys(skip, take)

Overview of SSH keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<SshKeyDetail> result = apiInstance.getAllSshKeys(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#getAllSshKeys");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;SshKeyDetail&gt;**](SshKeyDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

