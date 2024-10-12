# GetMetadataInformationApi

All URIs are relative to *http://169.254.169.254/metadata*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**identityGetInfo**](GetMetadataInformationApi.md#identityGetInfo) | **GET** /identity/info |  |


<a id="identityGetInfo"></a>
# **identityGetInfo**
> IdentityInfoResponse identityGetInfo(metadata, apiVersion)



Get information about AAD Metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetMetadataInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://169.254.169.254/metadata");

    GetMetadataInformationApi apiInstance = new GetMetadataInformationApi(defaultClient);
    String metadata = "true"; // String | This must be set to 'true'.
    String apiVersion = "2018-10-01"; // String | This is the API version to use.
    try {
      IdentityInfoResponse result = apiInstance.identityGetInfo(metadata, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetMetadataInformationApi#identityGetInfo");
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
| **metadata** | **String**| This must be set to &#39;true&#39;. | [enum: true] |
| **apiVersion** | **String**| This is the API version to use. | [enum: 2018-10-01] |

### Return type

[**IdentityInfoResponse**](IdentityInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | Error response describing why the operation failed. |  -  |

