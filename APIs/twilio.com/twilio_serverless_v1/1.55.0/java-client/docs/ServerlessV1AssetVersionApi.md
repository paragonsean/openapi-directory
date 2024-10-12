# ServerlessV1AssetVersionApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAssetVersion**](ServerlessV1AssetVersionApi.md#fetchAssetVersion) | **GET** /v1/Services/{ServiceSid}/Assets/{AssetSid}/Versions/{Sid} |  |
| [**listAssetVersion**](ServerlessV1AssetVersionApi.md#listAssetVersion) | **GET** /v1/Services/{ServiceSid}/Assets/{AssetSid}/Versions |  |


<a id="fetchAssetVersion"></a>
# **fetchAssetVersion**
> ServerlessV1ServiceAssetAssetVersion fetchAssetVersion(serviceSid, assetSid, sid)



Retrieve a specific Asset Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetVersionApi apiInstance = new ServerlessV1AssetVersionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Asset Version resource from.
    String assetSid = "assetSid_example"; // String | The SID of the Asset resource that is the parent of the Asset Version resource to fetch.
    String sid = "sid_example"; // String | The SID of the Asset Version resource to fetch.
    try {
      ServerlessV1ServiceAssetAssetVersion result = apiInstance.fetchAssetVersion(serviceSid, assetSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetVersionApi#fetchAssetVersion");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Asset Version resource from. | |
| **assetSid** | **String**| The SID of the Asset resource that is the parent of the Asset Version resource to fetch. | |
| **sid** | **String**| The SID of the Asset Version resource to fetch. | |

### Return type

[**ServerlessV1ServiceAssetAssetVersion**](ServerlessV1ServiceAssetAssetVersion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAssetVersion"></a>
# **listAssetVersion**
> ListAssetVersionResponse listAssetVersion(serviceSid, assetSid, pageSize, page, pageToken)



Retrieve a list of all Asset Versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetVersionApi apiInstance = new ServerlessV1AssetVersionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Asset Version resource from.
    String assetSid = "assetSid_example"; // String | The SID of the Asset resource that is the parent of the Asset Version resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAssetVersionResponse result = apiInstance.listAssetVersion(serviceSid, assetSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetVersionApi#listAssetVersion");
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
| **serviceSid** | **String**| The SID of the Service to read the Asset Version resource from. | |
| **assetSid** | **String**| The SID of the Asset resource that is the parent of the Asset Version resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListAssetVersionResponse**](ListAssetVersionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

