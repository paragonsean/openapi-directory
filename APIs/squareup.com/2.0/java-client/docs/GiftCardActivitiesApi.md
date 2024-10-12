# GiftCardActivitiesApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGiftCardActivity**](GiftCardActivitiesApi.md#createGiftCardActivity) | **POST** /v2/gift-cards/activities | CreateGiftCardActivity |
| [**listGiftCardActivities**](GiftCardActivitiesApi.md#listGiftCardActivities) | **GET** /v2/gift-cards/activities | ListGiftCardActivities |


<a id="createGiftCardActivity"></a>
# **createGiftCardActivity**
> CreateGiftCardActivityResponse createGiftCardActivity(createGiftCardActivityRequest)

CreateGiftCardActivity

Creates a gift card activity. For more information, see  [GiftCardActivity](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#giftcardactivity) and  [Using activated gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#using-activated-gift-cards).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardActivitiesApi apiInstance = new GiftCardActivitiesApi(defaultClient);
    CreateGiftCardActivityRequest createGiftCardActivityRequest = new CreateGiftCardActivityRequest(); // CreateGiftCardActivityRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateGiftCardActivityResponse result = apiInstance.createGiftCardActivity(createGiftCardActivityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardActivitiesApi#createGiftCardActivity");
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
| **createGiftCardActivityRequest** | [**CreateGiftCardActivityRequest**](CreateGiftCardActivityRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateGiftCardActivityResponse**](CreateGiftCardActivityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listGiftCardActivities"></a>
# **listGiftCardActivities**
> ListGiftCardActivitiesResponse listGiftCardActivities(giftCardId, type, locationId, beginTime, endTime, limit, cursor, sortOrder)

ListGiftCardActivities

Lists gift card activities. By default, you get gift card activities for all gift cards in the seller&#39;s account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift card activities for a gift card, for all gift cards in a specific region, or for activities within a time window.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardActivitiesApi apiInstance = new GiftCardActivitiesApi(defaultClient);
    String giftCardId = "giftCardId_example"; // String | If you provide a gift card ID, the endpoint returns activities that belong  to the specified gift card. Otherwise, the endpoint returns all gift card activities for  the seller.
    String type = "type_example"; // String | If you provide a type, the endpoint returns gift card activities of this type.  Otherwise, the endpoint returns all types of gift card activities.
    String locationId = "locationId_example"; // String | If you provide a location ID, the endpoint returns gift card activities for that location.  Otherwise, the endpoint returns gift card activities for all locations.
    String beginTime = "beginTime_example"; // String | The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year.
    String endTime = "endTime_example"; // String | The timestamp for the end of the reporting period, in RFC 3339 format. Inclusive. Default: The current time.
    Integer limit = 56; // Integer | If you provide a limit value, the endpoint returns the specified number  of results (or less) per page. A maximum value is 100. The default value is 50.
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If you do not provide the cursor, the call returns the first page of the results.
    String sortOrder = "sortOrder_example"; // String | The order in which the endpoint returns the activities, based on `created_at`. - `ASC` - Oldest to newest. - `DESC` - Newest to oldest (default).
    try {
      ListGiftCardActivitiesResponse result = apiInstance.listGiftCardActivities(giftCardId, type, locationId, beginTime, endTime, limit, cursor, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardActivitiesApi#listGiftCardActivities");
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
| **giftCardId** | **String**| If you provide a gift card ID, the endpoint returns activities that belong  to the specified gift card. Otherwise, the endpoint returns all gift card activities for  the seller. | [optional] |
| **type** | **String**| If you provide a type, the endpoint returns gift card activities of this type.  Otherwise, the endpoint returns all types of gift card activities. | [optional] |
| **locationId** | **String**| If you provide a location ID, the endpoint returns gift card activities for that location.  Otherwise, the endpoint returns gift card activities for all locations. | [optional] |
| **beginTime** | **String**| The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year. | [optional] |
| **endTime** | **String**| The timestamp for the end of the reporting period, in RFC 3339 format. Inclusive. Default: The current time. | [optional] |
| **limit** | **Integer**| If you provide a limit value, the endpoint returns the specified number  of results (or less) per page. A maximum value is 100. The default value is 50. | [optional] |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If you do not provide the cursor, the call returns the first page of the results. | [optional] |
| **sortOrder** | **String**| The order in which the endpoint returns the activities, based on &#x60;created_at&#x60;. - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default). | [optional] |

### Return type

[**ListGiftCardActivitiesResponse**](ListGiftCardActivitiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

