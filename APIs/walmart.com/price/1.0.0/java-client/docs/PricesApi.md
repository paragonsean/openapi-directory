# PricesApi

All URIs are relative to *https://marketplace.walmartapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createStrategy**](PricesApi.md#createStrategy) | **POST** /v3/repricer/strategy | Create Repricer Strategy |
| [**deleteStrategy**](PricesApi.md#deleteStrategy) | **DELETE** /v3/repricer/strategy/{strategyCollectionId} | Delete Repricer Strategy |
| [**getRepricerFeed**](PricesApi.md#getRepricerFeed) | **POST** /v3/repricerFeeds | Assign/Unassign items to/from Repricer Strategy |
| [**getStrategies**](PricesApi.md#getStrategies) | **GET** /v3/repricer/strategies | List of Repricer Strategies |
| [**optCapProgramInPrice**](PricesApi.md#optCapProgramInPrice) | **POST** /v3/cppreference | Set up CAP SKU All |
| [**priceBulkUploads**](PricesApi.md#priceBulkUploads) | **POST** /v3/feeds | Update bulk prices (Multiple) |
| [**updatePrice**](PricesApi.md#updatePrice) | **PUT** /v3/price | Update a price |
| [**updateStrategy**](PricesApi.md#updateStrategy) | **PUT** /v3/repricer/strategy/{strategyCollectionId} | Update Repricer Strategy |


<a id="createStrategy"></a>
# **createStrategy**
> CreateStrategy200Response createStrategy(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, createStrategyRequest, WM_CONSUMER_CHANNEL_TYPE)

Create Repricer Strategy

Creates a new strategy for the seller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    CreateStrategyRequest createStrategyRequest = new CreateStrategyRequest(); // CreateStrategyRequest | The request body will have the strategy related information
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      CreateStrategy200Response result = apiInstance.createStrategy(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, createStrategyRequest, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#createStrategy");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **createStrategyRequest** | [**CreateStrategyRequest**](CreateStrategyRequest.md)| The request body will have the strategy related information | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**CreateStrategy200Response**](CreateStrategy200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="deleteStrategy"></a>
# **deleteStrategy**
> DeleteStrategy200Response deleteStrategy(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, strategyCollectionId, WM_CONSUMER_CHANNEL_TYPE)

Delete Repricer Strategy

Deletes the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String strategyCollectionId = "strategyCollectionId_example"; // String | Automatically added
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      DeleteStrategy200Response result = apiInstance.deleteStrategy(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, strategyCollectionId, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#deleteStrategy");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **strategyCollectionId** | **String**| Automatically added | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**DeleteStrategy200Response**](DeleteStrategy200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getRepricerFeed"></a>
# **getRepricerFeed**
> GetRepricerFeed200Response getRepricerFeed(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, getRepricerFeedRequest, WM_CONSUMER_CHANNEL_TYPE)

Assign/Unassign items to/from Repricer Strategy

Add/Remove one or more items from a strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    GetRepricerFeedRequest getRepricerFeedRequest = new GetRepricerFeedRequest(); // GetRepricerFeedRequest | 
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetRepricerFeed200Response result = apiInstance.getRepricerFeed(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, getRepricerFeedRequest, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#getRepricerFeed");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **getRepricerFeedRequest** | [**GetRepricerFeedRequest**](GetRepricerFeedRequest.md)|  | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetRepricerFeed200Response**](GetRepricerFeed200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getStrategies"></a>
# **getStrategies**
> GetStrategies200Response getStrategies(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, WM_CONSUMER_CHANNEL_TYPE)

List of Repricer Strategies

Get the list of strategies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      GetStrategies200Response result = apiInstance.getStrategies(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#getStrategies");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**GetStrategies200Response**](GetStrategies200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="optCapProgramInPrice"></a>
# **optCapProgramInPrice**
> OptCapProgramInPrice200Response optCapProgramInPrice(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, optCapProgramInPriceRequest, WM_CONSUMER_CHANNEL_TYPE)

Set up CAP SKU All

This API helps Sellers to completely opt-in or opt-out from CAP program.  If the subsidyEnrolled value &#x3D; \&quot;true\&quot;, the Seller enrolls in the CAP program. All eligible SKUs (current and future) are by default opt-in. Seller should use the SKU opt-in/opt-out API to opt-out individual items.  If the subsidyEnrolled value &#x3D; \&quot;false\&quot;, the Seller stops participating in the CAP program and all eligible SKUs (current and future) are opt-out of the CAP program.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    OptCapProgramInPriceRequest optCapProgramInPriceRequest = new OptCapProgramInPriceRequest(); // OptCapProgramInPriceRequest | Request fields
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      OptCapProgramInPrice200Response result = apiInstance.optCapProgramInPrice(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, optCapProgramInPriceRequest, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#optCapProgramInPrice");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **optCapProgramInPriceRequest** | [**OptCapProgramInPriceRequest**](OptCapProgramInPriceRequest.md)| Request fields | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**OptCapProgramInPrice200Response**](OptCapProgramInPrice200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="priceBulkUploads"></a>
# **priceBulkUploads**
> PriceBulkUploads200Response priceBulkUploads(feedType, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, _file, WM_CONSUMER_CHANNEL_TYPE)

Update bulk prices (Multiple)

Updates prices in bulk.  In one Feed you can update up to 10,000 items in bulk. To ensure optimal Feed processing time, we recommend sending no more than 1000 items in one Feed and keeping the Feed sizes below 10 MB.  The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:  The timestamp used to determine precedence is passed in the request headers. All price updates in the feed are considered to have the same timestamp. The timestamp in the XML file is used only for auditing. You can send a single SKU multiple times in one Feed. If a SKU is repeated in a Feed, the price will be set for that SKU on Walmart.com, but there is no guarantee as to which SKU&#39;s price within that feed will be used. This API should be used in preference to the update a price. It should be called no sooner than 24 hours after a new item is set up and a wpid (Walmart Part ID) is available. Thereafter, the bulk price update has an service level agreement (SLA) of 15 minutes.  After the update is submitted, wait for at least five minutes before verifying whether the bulk price update was successful. Individual SKU price update success or failure is only available after the entire feed is processed.  If a SKU&#39;s price update fails (for example, multiple price updates were sent for the same SKU in a single feed), an error will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String feedType = "price"; // String | The feed Type
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    File _file = new File("/path/to/file"); // File | Feed file to upload
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      PriceBulkUploads200Response result = apiInstance.priceBulkUploads(feedType, WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, _file, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#priceBulkUploads");
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
| **feedType** | **String**| The feed Type | [enum: price, CPT_SELLER_ELIGIBILITY] |
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **_file** | **File**| Feed file to upload | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**PriceBulkUploads200Response**](PriceBulkUploads200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updatePrice"></a>
# **updatePrice**
> UpdatePrice200Response updatePrice(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, updatePriceRequest, WM_CONSUMER_CHANNEL_TYPE)

Update a price

Updates the regular price for a given item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    UpdatePriceRequest updatePriceRequest = new UpdatePriceRequest(); // UpdatePriceRequest | The request body consists of a Feed file attached to the request.
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      UpdatePrice200Response result = apiInstance.updatePrice(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, updatePriceRequest, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#updatePrice");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **updatePriceRequest** | [**UpdatePriceRequest**](UpdatePriceRequest.md)| The request body consists of a Feed file attached to the request. | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**UpdatePrice200Response**](UpdatePrice200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="updateStrategy"></a>
# **updateStrategy**
> CreateStrategy200Response updateStrategy(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, strategyCollectionId, createStrategyRequest, WM_CONSUMER_CHANNEL_TYPE)

Update Repricer Strategy

Updates the existing strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketplace.walmartapis.com");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String WM_SEC_ACCESS_TOKEN = "eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM....."; // String | The access token retrieved in the Token API call
    String WM_QOS_CORRELATION_ID = "b3261d2d-028a-4ef7-8602-633c23200af6"; // String | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    String WM_SVC_NAME = "Walmart Service Name"; // String | Walmart Service Name
    String strategyCollectionId = "strategyCollectionId_example"; // String | Automatically added
    CreateStrategyRequest createStrategyRequest = new CreateStrategyRequest(); // CreateStrategyRequest | The request body will have the strategy related information
    String WM_CONSUMER_CHANNEL_TYPE = "WM_CONSUMER_CHANNEL_TYPE_example"; // String | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    try {
      CreateStrategy200Response result = apiInstance.updateStrategy(WM_SEC_ACCESS_TOKEN, WM_QOS_CORRELATION_ID, WM_SVC_NAME, strategyCollectionId, createStrategyRequest, WM_CONSUMER_CHANNEL_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#updateStrategy");
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
| **WM_SEC_ACCESS_TOKEN** | **String**| The access token retrieved in the Token API call | |
| **WM_QOS_CORRELATION_ID** | **String**| A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | |
| **WM_SVC_NAME** | **String**| Walmart Service Name | |
| **strategyCollectionId** | **String**| Automatically added | |
| **createStrategyRequest** | [**CreateStrategyRequest**](CreateStrategyRequest.md)| The request body will have the strategy related information | |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | [optional] |

### Return type

[**CreateStrategy200Response**](CreateStrategy200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

