# MarketplacesOrdersV3BatchesApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeOrderListV2**](MarketplacesOrdersV3BatchesApi.md#changeOrderListV2) | **POST** /orders/v3/batches/changeOrders/{changeOrderType} | Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call) |
| [**changeOrderListV3**](MarketplacesOrdersV3BatchesApi.md#changeOrderListV3) | **POST** /orders/v3/batches/changeOrders | Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call) |
| [**clearMerchantOrderInfoListV3**](MarketplacesOrdersV3BatchesApi.md#clearMerchantOrderInfoListV3) | **POST** /orders/v3/batches/clearMerchantOrderInfos | Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call) |
| [**setMerchantOrderInfoListV3**](MarketplacesOrdersV3BatchesApi.md#setMerchantOrderInfoListV3) | **POST** /orders/v3/batches/setMerchantOrderInfos | Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call) |


<a id="changeOrderListV2"></a>
# **changeOrderListV2**
> BatchOrderOperationResponse changeOrderListV2(userName, changeOrderType, changeOrderListRequestV2, testMode)

Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3BatchesApi apiInstance = new MarketplacesOrdersV3BatchesApi(defaultClient);
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    String changeOrderType = "changeOrderType_example"; // String | The Order change type
    ChangeOrderListRequestV2 changeOrderListRequestV2 = new ChangeOrderListRequestV2(); // ChangeOrderListRequestV2 | 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      BatchOrderOperationResponse result = apiInstance.changeOrderListV2(userName, changeOrderType, changeOrderListRequestV2, testMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3BatchesApi#changeOrderListV2");
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
| **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | |
| **changeOrderType** | **String**| The Order change type | |
| **changeOrderListRequestV2** | [**ChangeOrderListRequestV2**](ChangeOrderListRequestV2.md)|  | |
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

<a id="changeOrderListV3"></a>
# **changeOrderListV3**
> BatchOrderOperationResponse changeOrderListV3(userName, changeOrderListRequest, testMode)

Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3BatchesApi apiInstance = new MarketplacesOrdersV3BatchesApi(defaultClient);
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    ChangeOrderListRequest changeOrderListRequest = new ChangeOrderListRequest(); // ChangeOrderListRequest | 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      BatchOrderOperationResponse result = apiInstance.changeOrderListV3(userName, changeOrderListRequest, testMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3BatchesApi#changeOrderListV3");
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

<a id="clearMerchantOrderInfoListV3"></a>
# **clearMerchantOrderInfoListV3**
> BatchOrderOperationResponse clearMerchantOrderInfoListV3(clearMerchantOrderInfoListRequest, testMode)

Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3BatchesApi apiInstance = new MarketplacesOrdersV3BatchesApi(defaultClient);
    ClearMerchantOrderInfoListRequest clearMerchantOrderInfoListRequest = new ClearMerchantOrderInfoListRequest(); // ClearMerchantOrderInfoListRequest | 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      BatchOrderOperationResponse result = apiInstance.clearMerchantOrderInfoListV3(clearMerchantOrderInfoListRequest, testMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3BatchesApi#clearMerchantOrderInfoListV3");
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

<a id="setMerchantOrderInfoListV3"></a>
# **setMerchantOrderInfoListV3**
> BatchOrderOperationResponse setMerchantOrderInfoListV3(setMerchantOrderInfoListRequest, testMode)

Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3BatchesApi apiInstance = new MarketplacesOrdersV3BatchesApi(defaultClient);
    SetMerchantOrderInfoListRequest setMerchantOrderInfoListRequest = new SetMerchantOrderInfoListRequest(); // SetMerchantOrderInfoListRequest | 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      BatchOrderOperationResponse result = apiInstance.setMerchantOrderInfoListV3(setMerchantOrderInfoListRequest, testMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3BatchesApi#setMerchantOrderInfoListV3");
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

