# BlocksApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blocksGetBlocksAsync**](BlocksApi.md#blocksGetBlocksAsync) | **GET** /api/booking/v0/blocks | Gets a list of blocks. |
| [**blocksGetBlocksCountAsync**](BlocksApi.md#blocksGetBlocksCountAsync) | **GET** /api/booking/v0/blocks/$count | Get total blocks count that match the given filter criteria. |
| [**blocksGetSingleBlockAsync**](BlocksApi.md#blocksGetSingleBlockAsync) | **GET** /api/booking/v0/blocks/{blockCode} | Gets the details for a specific block. |


<a id="blocksGetBlocksAsync"></a>
# **blocksGetBlocksAsync**
> Object blocksGetBlocksAsync(appId, appKey, token, hotelId, groupCode, from, to, status, ratePlanCodes, countDetails, skip, top, inlinecount)

Gets a list of blocks.

With this endpoint you can request a list of blocks for the hotel chain. Currently we only support to optionally              filter by the group code linked to the block. Additional filters will be available soon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    CancellationToken token = new CancellationToken(); // CancellationToken | 
    Integer hotelId = 56; // Integer | Only return blocks for this specific hotel.
    String groupCode = "groupCode_example"; // String | Filter the blocks by the specified group code
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Return all blocks where the block's last_departure is greater than specified date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Return all blocks where the block's last_departure is less than specified date.
    String status = "Cancelled"; // String | Return all blocks where the block status is one of the specified values.
    List<String> ratePlanCodes = Arrays.asList(); // List<String> | Return all blocks that have related the specified comma-separated rate plans.
    Boolean countDetails = true; // Boolean | If true it will include also details of block count per each room type.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      Object result = apiInstance.blocksGetBlocksAsync(appId, appKey, token, hotelId, groupCode, from, to, status, ratePlanCodes, countDetails, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#blocksGetBlocksAsync");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **token** | [**CancellationToken**](CancellationToken.md)|  | |
| **hotelId** | **Integer**| Only return blocks for this specific hotel. | [optional] |
| **groupCode** | **String**| Filter the blocks by the specified group code | [optional] |
| **from** | **OffsetDateTime**| Return all blocks where the block&#39;s last_departure is greater than specified date. | [optional] |
| **to** | **OffsetDateTime**| Return all blocks where the block&#39;s last_departure is less than specified date. | [optional] |
| **status** | **String**| Return all blocks where the block status is one of the specified values. | [optional] [enum: Cancelled, Tentative, Definite] |
| **ratePlanCodes** | [**List&lt;String&gt;**](String.md)| Return all blocks that have related the specified comma-separated rate plans. | [optional] |
| **countDetails** | **Boolean**| If true it will include also details of block count per each room type. | [optional] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of blocks matching the provided filter criteria. |  -  |
| **204** | There are no blocks matching your filter criteria. |  -  |
| **400** | Bad request. Request parameters syntactically erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="blocksGetBlocksCountAsync"></a>
# **blocksGetBlocksCountAsync**
> TotalCountResponse blocksGetBlocksCountAsync(appId, appKey, token, hotelId, groupCode, from, to, status, ratePlanCodes, countDetails)

Get total blocks count that match the given filter criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    CancellationToken token = new CancellationToken(); // CancellationToken | 
    Integer hotelId = 56; // Integer | Only return blocks for this specific hotel.
    String groupCode = "groupCode_example"; // String | Filter the blocks by the specified group code
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Return all blocks where the block's last_departure is greater than specified date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Return all blocks where the block's last_departure is less than specified date.
    String status = "Cancelled"; // String | Return all blocks where the block status is one of the specified values.
    List<String> ratePlanCodes = Arrays.asList(); // List<String> | Return all blocks that have related the specified comma-separated rate plans.
    Boolean countDetails = true; // Boolean | If true it will include also details of block count per each room type.
    try {
      TotalCountResponse result = apiInstance.blocksGetBlocksCountAsync(appId, appKey, token, hotelId, groupCode, from, to, status, ratePlanCodes, countDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#blocksGetBlocksCountAsync");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **token** | [**CancellationToken**](CancellationToken.md)|  | |
| **hotelId** | **Integer**| Only return blocks for this specific hotel. | [optional] |
| **groupCode** | **String**| Filter the blocks by the specified group code | [optional] |
| **from** | **OffsetDateTime**| Return all blocks where the block&#39;s last_departure is greater than specified date. | [optional] |
| **to** | **OffsetDateTime**| Return all blocks where the block&#39;s last_departure is less than specified date. | [optional] |
| **status** | **String**| Return all blocks where the block status is one of the specified values. | [optional] [enum: Cancelled, Tentative, Definite] |
| **ratePlanCodes** | [**List&lt;String&gt;**](String.md)| Return all blocks that have related the specified comma-separated rate plans. | [optional] |
| **countDetails** | **Boolean**| If true it will include also details of block count per each room type. | [optional] |

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The total blocks count for a given filter criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **500** | We couldn&#39;t return the representation due to an internal server error. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="blocksGetSingleBlockAsync"></a>
# **blocksGetSingleBlockAsync**
> Object blocksGetSingleBlockAsync(appId, appKey, blockCode, token)

Gets the details for a specific block.

Read all informationen about a block including the numbers of blocked rooms per room type and business day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String blockCode = "blockCode_example"; // String | Specifies the block code. The block code is composed of the hotel code, a dash and the block code               as shown in the hetras UI.
    CancellationToken token = new CancellationToken(); // CancellationToken | 
    try {
      Object result = apiInstance.blocksGetSingleBlockAsync(appId, appKey, blockCode, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#blocksGetSingleBlockAsync");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **blockCode** | **String**| Specifies the block code. The block code is composed of the hotel code, a dash and the block code               as shown in the hetras UI. | |
| **token** | [**CancellationToken**](CancellationToken.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns you all details for the specific block. |  -  |
| **400** | Bad request. Request parameters syntactically erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

