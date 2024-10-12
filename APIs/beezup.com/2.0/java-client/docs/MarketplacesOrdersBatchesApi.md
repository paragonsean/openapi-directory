# MarketplacesOrdersBatchesApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeOrderList**](MarketplacesOrdersBatchesApi.md#changeOrderList) | **POST** /v2/user/marketplaces/orders/batches/changeOrders/{changeOrderType} | [DEPRECATED] Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call) |
| [**clearMerchantOrderInfoList**](MarketplacesOrdersBatchesApi.md#clearMerchantOrderInfoList) | **POST** /v2/user/marketplaces/orders/batches/clearMerchantOrderInfos | [DEPRECATED] Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call) |
| [**setMerchantOrderInfoList**](MarketplacesOrdersBatchesApi.md#setMerchantOrderInfoList) | **POST** /v2/user/marketplaces/orders/batches/setMerchantOrderInfos | [DEPRECATED] Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call) |


<a id="changeOrderList"></a>
# **changeOrderList**
> BatchOrderOperationResponse changeOrderList(changeOrderType, userName, changeOrderListRequest, testMode)

[DEPRECATED] Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersBatchesApi apiInstance = new MarketplacesOrdersBatchesApi(defaultClient);
    String changeOrderType = "changeOrderType_example"; // String | The Order change type
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    ChangeOrderListRequest changeOrderListRequest = new ChangeOrderListRequest(); // ChangeOrderListRequest | 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      BatchOrderOperationResponse result = apiInstance.changeOrderList(changeOrderType, userName, changeOrderListRequest, testMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersBatchesApi#changeOrderList");
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
| **changeOrderType** | **String**| The Order change type | |
| **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | |
| **changeOrderListRequest** | [**ChangeOrderListRequest**](ChangeOrderListRequest.md)|  | |
| **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false] |

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Succesfully received and processed batched operations. Please check response to see the status per operation. |  -  |
| **400** | Requested too many batch operations |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="clearMerchantOrderInfoList"></a>
# **clearMerchantOrderInfoList**
> BatchOrderOperationResponse clearMerchantOrderInfoList(clearMerchantOrderInfoListRequest)

[DEPRECATED] Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersBatchesApi apiInstance = new MarketplacesOrdersBatchesApi(defaultClient);
    ClearMerchantOrderInfoListRequest clearMerchantOrderInfoListRequest = new ClearMerchantOrderInfoListRequest(); // ClearMerchantOrderInfoListRequest | 
    try {
      BatchOrderOperationResponse result = apiInstance.clearMerchantOrderInfoList(clearMerchantOrderInfoListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersBatchesApi#clearMerchantOrderInfoList");
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
| **clearMerchantOrderInfoListRequest** | [**ClearMerchantOrderInfoListRequest**](ClearMerchantOrderInfoListRequest.md)|  | |

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Succesfully received and processed batched operations. Please check response to see the status per operation. |  -  |
| **400** | Requested too many batch operations |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="setMerchantOrderInfoList"></a>
# **setMerchantOrderInfoList**
> BatchOrderOperationResponse setMerchantOrderInfoList(setMerchantOrderInfoListRequest)

[DEPRECATED] Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersBatchesApi apiInstance = new MarketplacesOrdersBatchesApi(defaultClient);
    SetMerchantOrderInfoListRequest setMerchantOrderInfoListRequest = new SetMerchantOrderInfoListRequest(); // SetMerchantOrderInfoListRequest | 
    try {
      BatchOrderOperationResponse result = apiInstance.setMerchantOrderInfoList(setMerchantOrderInfoListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersBatchesApi#setMerchantOrderInfoList");
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
| **setMerchantOrderInfoListRequest** | [**SetMerchantOrderInfoListRequest**](SetMerchantOrderInfoListRequest.md)|  | |

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Succesfully received and processed batched operations. Please check response to see the status per operation. |  -  |
| **400** | Requested too many batch operations |  -  |
| **0** | Occurs when something goes wrong |  -  |

