# HostShareApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkAddHostShares**](HostShareApi.md#bulkAddHostShares) | **POST** /host/share/bulk | Add NAS shares in bulk |
| [**bulkUpdateHostShare**](HostShareApi.md#bulkUpdateHostShare) | **PATCH** /host/share/bulk | Update network shares |


<a id="bulkAddHostShares"></a>
# **bulkAddHostShares**
> BulkShareAddResponse bulkAddHostShares(nasSharesToAdd)

Add NAS shares in bulk

Add NAS shares for a NAS host to the Rubrik cluster in bulk. This operation does not validate share credentials. If the default share credentials are incorrect, the share status on shares UI displays as \&quot;Wrong credential\&quot;. Use the PATCH /v1/host/share/bulk endpoint to enter the correct credentials when this status displays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostShareApi apiInstance = new HostShareApi(defaultClient);
    NasSharesToAdd nasSharesToAdd = new NasSharesToAdd(); // NasSharesToAdd | The properties used to add the NAS Shares to the Rubrik cluster.
    try {
      BulkShareAddResponse result = apiInstance.bulkAddHostShares(nasSharesToAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostShareApi#bulkAddHostShares");
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
| **nasSharesToAdd** | [**NasSharesToAdd**](NasSharesToAdd.md)| The properties used to add the NAS Shares to the Rubrik cluster. | |

### Return type

[**BulkShareAddResponse**](BulkShareAddResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a detailed view of all added network share objects and status of the job that validates the default credentials added to each object. |  -  |

<a id="bulkUpdateHostShare"></a>
# **bulkUpdateHostShare**
> List&lt;HostShareDetail&gt; bulkUpdateHostShare(hostShareUpdate)

Update network shares

Update the properties of the objects that represent the specified network share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostShareApi apiInstance = new HostShareApi(defaultClient);
    List<HostShareUpdate> hostShareUpdate = Arrays.asList(); // List<HostShareUpdate> | Properties to use for the update of network share objects.
    try {
      List<HostShareDetail> result = apiInstance.bulkUpdateHostShare(hostShareUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostShareApi#bulkUpdateHostShare");
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
| **hostShareUpdate** | [**List&lt;HostShareUpdate&gt;**](HostShareUpdate.md)| Properties to use for the update of network share objects. | |

### Return type

[**List&lt;HostShareDetail&gt;**](HostShareDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a detailed view of all updated network share objects. |  -  |

