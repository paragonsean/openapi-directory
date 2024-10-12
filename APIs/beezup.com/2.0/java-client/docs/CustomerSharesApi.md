# CustomerSharesApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteStoreShare**](CustomerSharesApi.md#deleteStoreShare) | **DELETE** /v2/user/customer/stores/{storeId}/shares/{userId} | Delete a share of a store to another user |
| [**getStoreShares**](CustomerSharesApi.md#getStoreShares) | **GET** /v2/user/customer/stores/{storeId}/shares | Get shares related to this store |
| [**shareStore**](CustomerSharesApi.md#shareStore) | **POST** /v2/user/customer/stores/{storeId}/shares | Share a store to another user |


<a id="deleteStoreShare"></a>
# **deleteStoreShare**
> deleteStoreShare(storeId, userId)

Delete a share of a store to another user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerSharesApi apiInstance = new CustomerSharesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String userId = "userId_example"; // String | The friend user id
    try {
      apiInstance.deleteStoreShare(storeId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSharesApi#deleteStoreShare");
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
| **storeId** | **String**| Your store identifier | |
| **userId** | **String**| The friend user id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Share deleted |  -  |
| **404** | Store not found or customer not the owner |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreShares"></a>
# **getStoreShares**
> StoreShares getStoreShares(storeId, ifNoneMatch)

Get shares related to this store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerSharesApi apiInstance = new CustomerSharesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      StoreShares result = apiInstance.getStoreShares(storeId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSharesApi#getStoreShares");
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
| **storeId** | **String**| Your store identifier | |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**StoreShares**](StoreShares.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The sharing list of the store |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Store not found or customer not the owner |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="shareStore"></a>
# **shareStore**
> shareStore(storeId, body)

Share a store to another user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerSharesApi apiInstance = new CustomerSharesApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String body = "body_example"; // String | Your friend's email
    try {
      apiInstance.shareStore(storeId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSharesApi#shareStore");
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
| **storeId** | **String**| Your store identifier | |
| **body** | **String**| Your friend&#39;s email | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Store shared |  -  |
| **402** | Free offer is not allowed to share store. |  -  |
| **404** | Only the owner of the store can make this operation or user not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

