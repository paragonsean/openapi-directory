# RatePlansApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ratePlansBatchUpdateRates**](RatePlansApi.md#ratePlansBatchUpdateRates) | **PUT** /api/hotel/v0/hotels/{hotelId}/rateplans/batch/$rates | Update a list of base rateplans for a given period and a given base price for single occupancy. |
| [**ratePlansGetRate**](RatePlansApi.md#ratePlansGetRate) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates/{businessDay} | Get the setup of a daily rate for a specific business day and rateplan. |
| [**ratePlansGetRateplan**](RatePlansApi.md#ratePlansGetRateplan) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode} | Get all the details for a specific rateplan in the hotel. |
| [**ratePlansGetRateplans**](RatePlansApi.md#ratePlansGetRateplans) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans | Get a list of rateplans for the specified hotel id matching the filter criteria. |
| [**ratePlansGetRateplansCount**](RatePlansApi.md#ratePlansGetRateplansCount) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/$count | Get the count of all rateplans in the hotel matching the given filter criteria. |
| [**ratePlansGetRates**](RatePlansApi.md#ratePlansGetRates) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates | Get the setup of the daily rates for a specific rateplan and a defined timeperiod. |
| [**ratePlansGetRatesCount**](RatePlansApi.md#ratePlansGetRatesCount) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates/$count | Get the count of all active and loaded daily rates for the defined rateplan in a specified time period. |
| [**ratePlansPatchRate**](RatePlansApi.md#ratePlansPatchRate) | **PATCH** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates/{businessDay} | Partially update a rate of the specified rateplan for a defined business day. |
| [**ratePlansPatchRates**](RatePlansApi.md#ratePlansPatchRates) | **PATCH** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates | Partially update a rate of the specified rateplan for the defined time period. |


<a id="ratePlansBatchUpdateRates"></a>
# **ratePlansBatchUpdateRates**
> Object ratePlansBatchUpdateRates(appId, appKey, hotelId, request)

Update a list of base rateplans for a given period and a given base price for single occupancy.

Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified time period.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;rateplan\&quot;: \&quot;STDN01\&quot;, \&quot;from\&quot;: \&quot;2018-01-01\&quot;, \&quot;to\&quot;: \&quot;2018-01-30\&quot;, \&quot;base_price\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    List<RatesBatchUpdateRequestItem> request = Arrays.asList(); // List<RatesBatchUpdateRequestItem> | 
    try {
      Object result = apiInstance.ratePlansBatchUpdateRates(appId, appKey, hotelId, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansBatchUpdateRates");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **request** | [**List&lt;RatesBatchUpdateRequestItem&gt;**](RatesBatchUpdateRequestItem.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update was successful |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansGetRate"></a>
# **ratePlansGetRate**
> RateResponse ratePlansGetRate(appId, appKey, hotelId, rateplanCode, businessDay)

Get the setup of a daily rate for a specific business day and rateplan.

Read the setup of the daily rate for the defined rateplan for that specific business day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    String rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to see details for.
    OffsetDateTime businessDay = OffsetDateTime.now(); // OffsetDateTime | The business day you want to get the rate setup for.
    try {
      RateResponse result = apiInstance.ratePlansGetRate(appId, appKey, hotelId, rateplanCode, businessDay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansGetRate");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **rateplanCode** | **String**| The code of the rateplan you want to see details for. | |
| **businessDay** | **OffsetDateTime**| The business day you want to get the rate setup for. | |

### Return type

[**RateResponse**](RateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily rate with room type supplements for the specified rateplan and business day. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested              rateplan could not be found or the rate is inactive on this business day. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansGetRateplan"></a>
# **ratePlansGetRateplan**
> ExtendedRateplanEntry ratePlansGetRateplan(appId, appKey, hotelId, rateplanCode)

Get all the details for a specific rateplan in the hotel.

Read the details about a specific rateplan for the defined hotel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    String rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to see details for.
    try {
      ExtendedRateplanEntry result = apiInstance.ratePlansGetRateplan(appId, appKey, hotelId, rateplanCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansGetRateplan");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **rateplanCode** | **String**| The code of the rateplan you want to see details for. | |

### Return type

[**ExtendedRateplanEntry**](ExtendedRateplanEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rateplan details for the given rateplan and hotel. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested rateplan could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansGetRateplans"></a>
# **ratePlansGetRateplans**
> RateplansListResponse ratePlansGetRateplans(appId, appKey, hotelId, sellingStatus, commissionable, group, baseRateplan, channelGroup, channelCode, marketCodes, roomTypes, includedServices, skip, top, inlinecount)

Get a list of rateplans for the specified hotel id matching the filter criteria.

With this call you can find rateplans for a hotel by different filters. By default and without any filter criteria              defined it will return you all active rateplans.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id you are trying to find rateplans for.
    String sellingStatus = "Active"; // String | Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans.
    Boolean commissionable = true; // Boolean | Return all rateplans having commisionable status
    String group = "group_example"; // String | Return all rateplans belonging to the specified rateplan group
    String baseRateplan = "baseRateplan_example"; // String | Return all rateplans having the specified rateplan as base rateplan
    String channelGroup = "channelGroup_example"; // String | Return all rateplans that are sold through at least one channel out of the specified channel group
    String channelCode = "channelCode_example"; // String | Return all rateplans sold through the specified channel
    List<String> marketCodes = Arrays.asList(); // List<String> | Return all rateplans having one of the specified values as a market code
    List<String> roomTypes = Arrays.asList(); // List<String> | Return all rateplans by which at least one of the specified room types are sold
    List<String> includedServices = Arrays.asList(); // List<String> | Return all rateplans having at least one of the specified services included
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      RateplansListResponse result = apiInstance.ratePlansGetRateplans(appId, appKey, hotelId, sellingStatus, commissionable, group, baseRateplan, channelGroup, channelCode, marketCodes, roomTypes, includedServices, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansGetRateplans");
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
| **hotelId** | **Integer**| The hotel id you are trying to find rateplans for. | |
| **sellingStatus** | **String**| Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans. | [optional] [enum: Active, Inactive, All] |
| **commissionable** | **Boolean**| Return all rateplans having commisionable status | [optional] |
| **group** | **String**| Return all rateplans belonging to the specified rateplan group | [optional] |
| **baseRateplan** | **String**| Return all rateplans having the specified rateplan as base rateplan | [optional] |
| **channelGroup** | **String**| Return all rateplans that are sold through at least one channel out of the specified channel group | [optional] |
| **channelCode** | **String**| Return all rateplans sold through the specified channel | [optional] |
| **marketCodes** | [**List&lt;String&gt;**](String.md)| Return all rateplans having one of the specified values as a market code | [optional] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return all rateplans by which at least one of the specified room types are sold | [optional] |
| **includedServices** | [**List&lt;String&gt;**](String.md)| Return all rateplans having at least one of the specified services included | [optional] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**RateplansListResponse**](RateplansListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of rateplans for a requested hotel matching the filter criteria. |  -  |
| **204** | There are no rateplans found for the given filtering and pagination criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansGetRateplansCount"></a>
# **ratePlansGetRateplansCount**
> TotalCountResponse ratePlansGetRateplansCount(appId, appKey, hotelId, sellingStatus, commissionable, group, baseRateplan, channelGroup, channelCode, marketCodes, roomTypes, includedServices)

Get the count of all rateplans in the hotel matching the given filter criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel you are counting the rateplans for.
    String sellingStatus = "Active"; // String | Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans.
    Boolean commissionable = true; // Boolean | Return all rateplans having commisionable status
    String group = "group_example"; // String | Return all rateplans belonging to the specified rateplan group
    String baseRateplan = "baseRateplan_example"; // String | Return all rateplans having the specified rateplan as base rateplan
    String channelGroup = "channelGroup_example"; // String | Return all rateplans that are sold through at least one channel out of the specified channel group
    String channelCode = "channelCode_example"; // String | Return all rateplans sold through the specified channel
    List<String> marketCodes = Arrays.asList(); // List<String> | Return all rateplans having one of the specified values as a market code
    List<String> roomTypes = Arrays.asList(); // List<String> | Return all rateplans by which at least one of the specified room types are sold
    List<String> includedServices = Arrays.asList(); // List<String> | Return all rateplans having at least one of the specified services included
    try {
      TotalCountResponse result = apiInstance.ratePlansGetRateplansCount(appId, appKey, hotelId, sellingStatus, commissionable, group, baseRateplan, channelGroup, channelCode, marketCodes, roomTypes, includedServices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansGetRateplansCount");
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
| **hotelId** | **Integer**| The hotel you are counting the rateplans for. | |
| **sellingStatus** | **String**| Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans. | [optional] [enum: Active, Inactive, All] |
| **commissionable** | **Boolean**| Return all rateplans having commisionable status | [optional] |
| **group** | **String**| Return all rateplans belonging to the specified rateplan group | [optional] |
| **baseRateplan** | **String**| Return all rateplans having the specified rateplan as base rateplan | [optional] |
| **channelGroup** | **String**| Return all rateplans that are sold through at least one channel out of the specified channel group | [optional] |
| **channelCode** | **String**| Return all rateplans sold through the specified channel | [optional] |
| **marketCodes** | [**List&lt;String&gt;**](String.md)| Return all rateplans having one of the specified values as a market code | [optional] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return all rateplans by which at least one of the specified room types are sold | [optional] |
| **includedServices** | [**List&lt;String&gt;**](String.md)| Return all rateplans having at least one of the specified services included | [optional] |

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
| **200** | The rateplans count in the hotel matching the given filter criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansGetRates"></a>
# **ratePlansGetRates**
> RatesResponse ratePlansGetRates(appId, appKey, hotelId, rateplanCode, from, to, expand, skip, top, inlinecount)

Get the setup of the daily rates for a specific rateplan and a defined timeperiod.

With this call you can read the daily rates setup including the cancellation policy and minimum guarantee per day for the              specified rateplan. You can specify a timeperiod to read the daily rates for. The rateplan needs to be active for at least              one business day in the defined time period and have rates loaded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    String rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to see details for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Defines the last business day you would like to get rates for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Defines the first business day you would like to get rates for.
    String expand = "RoomTypeSupplements"; // String | You can expand the supplements per room type on demand. By default they are not shown.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      RatesResponse result = apiInstance.ratePlansGetRates(appId, appKey, hotelId, rateplanCode, from, to, expand, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansGetRates");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **rateplanCode** | **String**| The code of the rateplan you want to see details for. | |
| **from** | **OffsetDateTime**| Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | |
| **to** | **OffsetDateTime**| Defines the first business day you would like to get rates for. | |
| **expand** | **String**| You can expand the supplements per room type on demand. By default they are not shown. | [optional] [enum: RoomTypeSupplements] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**RatesResponse**](RatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of daily rates within the specified time preiod. |  -  |
| **204** | The rateplan does not have any active date or is not loaded within the defined time period. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested rateplan could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansGetRatesCount"></a>
# **ratePlansGetRatesCount**
> TotalCountResponse ratePlansGetRatesCount(appId, appKey, hotelId, rateplanCode, from, to)

Get the count of all active and loaded daily rates for the defined rateplan in a specified time period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    String rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to count daily rates for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Defines the last business day you would like to get rates for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Defines the first business day you would like to get rates for.
    try {
      TotalCountResponse result = apiInstance.ratePlansGetRatesCount(appId, appKey, hotelId, rateplanCode, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansGetRatesCount");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **rateplanCode** | **String**| The code of the rateplan you want to count daily rates for. | |
| **from** | **OffsetDateTime**| Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | |
| **to** | **OffsetDateTime**| Defines the first business day you would like to get rates for. | |

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
| **200** | The count of daily rates for the specified time period. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested room could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansPatchRate"></a>
# **ratePlansPatchRate**
> Object ratePlansPatchRate(appId, appKey, hotelId, rateplanCode, businessDay, patchRequest)

Partially update a rate of the specified rateplan for a defined business day.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified business day.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/base_price\&quot;, \&quot;value\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    String rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to update the daily rate details for.
    OffsetDateTime businessDay = OffsetDateTime.now(); // OffsetDateTime | The business day of the daily rate you want to update.
    List<OperationRatePatchRequest> patchRequest = Arrays.asList(); // List<OperationRatePatchRequest> | A set of JSON Patch operations.
    try {
      Object result = apiInstance.ratePlansPatchRate(appId, appKey, hotelId, rateplanCode, businessDay, patchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansPatchRate");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **rateplanCode** | **String**| The code of the rateplan you want to update the daily rate details for. | |
| **businessDay** | **OffsetDateTime**| The business day of the daily rate you want to update. | |
| **patchRequest** | [**List&lt;OperationRatePatchRequest&gt;**](OperationRatePatchRequest.md)| A set of JSON Patch operations. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update was successful |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="ratePlansPatchRates"></a>
# **ratePlansPatchRates**
> Object ratePlansPatchRates(appId, appKey, hotelId, rateplanCode, from, to, patchRequest)

Partially update a rate of the specified rateplan for the defined time period.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified time period.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/base_price\&quot;, \&quot;value\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatePlansApi apiInstance = new RatePlansApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the rateplan belongs to.
    String rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to update the daily rate details for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Defines the last business day you would like to get rates for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Defines the first business day you would like to get rates for.
    List<OperationRatePatchRequest> patchRequest = Arrays.asList(); // List<OperationRatePatchRequest> | A set of JSON Patch operations.
    try {
      Object result = apiInstance.ratePlansPatchRates(appId, appKey, hotelId, rateplanCode, from, to, patchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatePlansApi#ratePlansPatchRates");
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
| **hotelId** | **Integer**| The hotel id the rateplan belongs to. | |
| **rateplanCode** | **String**| The code of the rateplan you want to update the daily rate details for. | |
| **from** | **OffsetDateTime**| Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | |
| **to** | **OffsetDateTime**| Defines the first business day you would like to get rates for. | |
| **patchRequest** | [**List&lt;OperationRatePatchRequest&gt;**](OperationRatePatchRequest.md)| A set of JSON Patch operations. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update was successful |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

