# OnDemandPurchasesAndRentalsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkIfVodWasPurchased**](OnDemandPurchasesAndRentalsApi.md#checkIfVodWasPurchased) | **GET** /users/{user_id}/ondemand/purchases | Check if a user has made a purchase or rental from an On Demand page |
| [**checkIfVodWasPurchasedAlt1**](OnDemandPurchasesAndRentalsApi.md#checkIfVodWasPurchasedAlt1) | **GET** /me/ondemand/purchases/{ondemand_id} | Check if a user has made a purchase or rental from an On Demand page |
| [**getVodPurchases**](OnDemandPurchasesAndRentalsApi.md#getVodPurchases) | **GET** /me/ondemand/purchases | Get all the On Demand purchases and rentals that a user has made |


<a id="checkIfVodWasPurchased"></a>
# **checkIfVodWasPurchased**
> OnDemandPage checkIfVodWasPurchased(userId)

Check if a user has made a purchase or rental from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPurchasesAndRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPurchasesAndRentalsApi apiInstance = new OnDemandPurchasesAndRentalsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      OnDemandPage result = apiInstance.checkIfVodWasPurchased(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPurchasesAndRentalsApi#checkIfVodWasPurchased");
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
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You have purchased the On Demand page. |  -  |
| **403** | The requested user isn&#39;t the same as the authenticated user. |  -  |
| **404** | No such user or On Demand page exists. |  -  |

<a id="checkIfVodWasPurchasedAlt1"></a>
# **checkIfVodWasPurchasedAlt1**
> OnDemandPage checkIfVodWasPurchasedAlt1(ondemandId)

Check if a user has made a purchase or rental from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPurchasesAndRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPurchasesAndRentalsApi apiInstance = new OnDemandPurchasesAndRentalsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandPage result = apiInstance.checkIfVodWasPurchasedAlt1(ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPurchasesAndRentalsApi#checkIfVodWasPurchasedAlt1");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You have purchased the On Demand page. |  -  |
| **403** | The requested user isn&#39;t the same as the authenticated user. |  -  |
| **404** | No such user or On Demand page exists. |  -  |

<a id="getVodPurchases"></a>
# **getVodPurchases**
> List&lt;OnDemandPage&gt; getVodPurchases(direction, filter, page, perPage, sort)

Get all the On Demand purchases and rentals that a user has made

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandPurchasesAndRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandPurchasesAndRentalsApi apiInstance = new OnDemandPurchasesAndRentalsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "all"; // String | The type of On Demand videos to show.  Option descriptions:  * `important` - Will show all pages which are about to expire. 
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "added"; // String | The way to sort the results.
    try {
      List<OnDemandPage> result = apiInstance.getVodPurchases(direction, filter, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandPurchasesAndRentalsApi#getVodPurchases");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The type of On Demand videos to show.  Option descriptions:  * &#x60;important&#x60; - Will show all pages which are about to expire.  | [optional] [enum: all, expiring_soon, film, important, purchased, rented, series, subscription, unwatched, watched] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: added, alphabetical, date, name, purchase_time, rating, release_date] |

### Return type

[**List&lt;OnDemandPage&gt;**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The purchases and rentals were returned. |  -  |
| **403** | The authenticated user can&#39;t view the purchases and rentals for another user&#39;s account. |  -  |

