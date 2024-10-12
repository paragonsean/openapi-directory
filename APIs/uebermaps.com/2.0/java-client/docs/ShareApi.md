# ShareApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shareMapIdGet**](ShareApi.md#shareMapIdGet) | **GET** /share/map/{id} | Get secret access token to share map |


<a id="shareMapIdGet"></a>
# **shareMapIdGet**
> MapWithAuthToken shareMapIdGet(id)

Get secret access token to share map

Get secret access token of an uebermap with access set to &#39;Secret link&#39;. Pass the &#39;token&#39; on every request you make to access this uebermap and its resources. F.e. token&#x3D;1-x_gqu7eLBe3uKoAGAGXy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    ShareApi apiInstance = new ShareApi(defaultClient);
    Integer id = 56; // Integer | Id of map
    try {
      MapWithAuthToken result = apiInstance.shareMapIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#shareMapIdGet");
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
| **id** | **Integer**| Id of map | |

### Return type

[**MapWithAuthToken**](MapWithAuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains map data and a secret token to access this map. |  -  |

