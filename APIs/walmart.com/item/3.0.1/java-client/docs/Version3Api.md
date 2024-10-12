# Version3Api

All URIs are relative to *https://developer.walmart.com/proxy/item-api-doc-app/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3doPostMultiPart**](Version3Api.md#v3doPostMultiPart) | **POST** /v3/feeds | Upload an item feed |
| [**v3getAllItemsStatus**](Version3Api.md#v3getAllItemsStatus) | **GET** /v3/feeds/{feedId} | Get status of an item within a feed |
| [**v3getFeedItemStatus**](Version3Api.md#v3getFeedItemStatus) | **GET** /v3/feeds | Get status of an item feed |


<a id="v3doPostMultiPart"></a>
# **v3doPostMultiPart**
> v3doPostMultiPart(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, _file, feedType)

Upload an item feed

You can upload an item feed. If the feed successfully processed, it returns a feed ID. Use the returned feed ID to retrieve a feed status. You need your Consumer ID and the Private Key to upload an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/proxy/item-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    File _file = new File("/path/to/file"); // File | Feed File to upload
    String feedType = "item"; // String | Feed Type
    try {
      apiInstance.v3doPostMultiPart(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, _file, feedType);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#v3doPostMultiPart");
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
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **_file** | **File**| Feed File to upload | |
| **feedType** | **String**| Feed Type | [optional] [default to item] [enum: item, SUPPLIER_FULL_ITEM, CONTENT_PRODUCT] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="v3getAllItemsStatus"></a>
# **v3getAllItemsStatus**
> v3getAllItemsStatus(feedId, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, includeDetails, offset, limit)

Get status of an item within a feed

You can display the status of all items within a feed. Use the feed ID returned from the upload an item API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/proxy/item-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String feedId = "feedId_example"; // String | The feed ID
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String includeDetails = "false"; // String | Includes details of each entity in the feed. Do not set this parameter to true.
    String offset = "0"; // String | The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true.
    String limit = "50"; // String | The number of entities to be returned. It cannot be more than 50 entities. Use it only when the includeDetails is set to true.
    try {
      apiInstance.v3getAllItemsStatus(feedId, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, includeDetails, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#v3getAllItemsStatus");
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
| **feedId** | **String**| The feed ID | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **includeDetails** | **String**| Includes details of each entity in the feed. Do not set this parameter to true. | [optional] [default to false] |
| **offset** | **String**| The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true. | [optional] [default to 0] |
| **limit** | **String**| The number of entities to be returned. It cannot be more than 50 entities. Use it only when the includeDetails is set to true. | [optional] [default to 50] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="v3getFeedItemStatus"></a>
# **v3getFeedItemStatus**
> v3getFeedItemStatus(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, feedId, includeDetails, offset, limit)

Get status of an item feed

You can display the status of an item within a feed. Use the feed ID returned from the upload an item API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/proxy/item-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String feedId = "feedId_example"; // String | The feed ID.
    String includeDetails = "false"; // String | Includes the status details for each item in the feed. Do not set this parameter to true as discrepancies may appear between the header and the item details (the item details may be incorrect). Instead, use the Get a feedItems status.
    String offset = "0"; // String | The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true.
    String limit = "50"; // String | The number of items to be returned. Cannot be more than 50 items. Use it only when the includeDetails is set to true.
    try {
      apiInstance.v3getFeedItemStatus(WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, feedId, includeDetails, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#v3getFeedItemStatus");
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
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **feedId** | **String**| The feed ID. | [optional] |
| **includeDetails** | **String**| Includes the status details for each item in the feed. Do not set this parameter to true as discrepancies may appear between the header and the item details (the item details may be incorrect). Instead, use the Get a feedItems status. | [optional] [default to false] |
| **offset** | **String**| The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true. | [optional] [default to 0] |
| **limit** | **String**| The number of items to be returned. Cannot be more than 50 items. Use it only when the includeDetails is set to true. | [optional] [default to 50] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

