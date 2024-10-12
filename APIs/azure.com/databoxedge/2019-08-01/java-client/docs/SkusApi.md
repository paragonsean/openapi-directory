# SkusApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**skusList**](SkusApi.md#skusList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataBoxEdge/skus | List all the available Skus in the region and information related to them |


<a id="skusList"></a>
# **skusList**
> SkuInformationList skusList(subscriptionId, apiVersion, $filter)

List all the available Skus in the region and information related to them

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SkusApi apiInstance = new SkusApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "apiVersion_example"; // String | The API version.
    String $filter = "$filter_example"; // String | Specify $filter='location eq <location>' to filter on location.
    try {
      SkuInformationList result = apiInstance.skusList(subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkusApi#skusList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **apiVersion** | **String**| The API version. | |
| **$filter** | **String**| Specify $filter&#x3D;&#39;location eq &lt;location&gt;&#39; to filter on location. | [optional] |

### Return type

[**SkuInformationList**](SkuInformationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists the available Skus and information related to them. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

