# DataExtractsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDataExtractsEvents**](DataExtractsApi.md#getDataExtractsEvents) | **GET** /dataExtracts/events | Get Events |
| [**getDataExtractsUserData**](DataExtractsApi.md#getDataExtractsUserData) | **GET** /dataExtracts/userData | Get userData |


<a id="getDataExtractsEvents"></a>
# **getDataExtractsEvents**
> DataExtractsEventResponse getDataExtractsEvents(eventName, fromDate, toDate)

Get Events

The get extracts events service is used to learn about occurrences of data extract related events. This service currently supports only the DATA_UPDATES event.&lt;br&gt;Passing the event name as DATA_UPDATES provides information about users for whom data has been modified in the system for the specified time range. To learn more, please refer to the &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/DataExtracts\&quot;&gt;dataExtracts&lt;/a&gt; page.&lt;br&gt;You can retrieve data in increments of no more than 60 minutes over the period of the last 7 days from today&#39;s date.&lt;br&gt;This service is only invoked with either admin access token or a cobrand session.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExtractsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DataExtractsApi apiInstance = new DataExtractsApi(defaultClient);
    String eventName = "eventName_example"; // String | Event Name
    String fromDate = "fromDate_example"; // String | From DateTime (YYYY-MM-DDThh:mm:ssZ)
    String toDate = "toDate_example"; // String | To DateTime (YYYY-MM-DDThh:mm:ssZ)
    try {
      DataExtractsEventResponse result = apiInstance.getDataExtractsEvents(eventName, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExtractsApi#getDataExtractsEvents");
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
| **eventName** | **String**| Event Name | |
| **fromDate** | **String**| From DateTime (YYYY-MM-DDThh:mm:ssZ) | |
| **toDate** | **String**| To DateTime (YYYY-MM-DDThh:mm:ssZ) | |

### Return type

[**DataExtractsEventResponse**](DataExtractsEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for fromDate.fromDate cannot be greater than current time&lt;br&gt;Y800 : Invalid value for toDate.toDate cannot be greater than current time&lt;br&gt;Y800 : Invalid value for fromDate or toDate.fromDate and toDate cannot be older than 7 days&lt;br&gt;Y800 : Invalid value for fromDate.fromDate cannot be greater than toDate. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getDataExtractsUserData"></a>
# **getDataExtractsUserData**
> DataExtractsUserDataResponse getDataExtractsUserData(fromDate, loginName, toDate)

Get userData

The get user data service is used to get a user&#39;s modified data for a particular period of time for accounts, transactions, holdings, and provider account information.&lt;br&gt;The time difference between fromDate and toDate fields cannot be more than 60 minutes.&lt;br&gt;By default, pagination is available for the transaction entity in this API. In the first response, the API will retrieve 500 transactions along with other data. The response header will provide a link to retrieve the next set of transactions.&lt;br&gt;In the response body of the first API response, totalTransactionsCount indicates the total number of transactions the API will retrieve for the user.&lt;br&gt;This service is only invoked with either admin access token or a cobrand session.&lt;br/&gt;Refer to &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/DataExtracts\&quot;&gt;dataExtracts&lt;/a&gt; page for more information.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExtractsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DataExtractsApi apiInstance = new DataExtractsApi(defaultClient);
    String fromDate = "fromDate_example"; // String | From DateTime (YYYY-MM-DDThh:mm:ssZ)
    String loginName = "loginName_example"; // String | Login Name
    String toDate = "toDate_example"; // String | To DateTime (YYYY-MM-DDThh:mm:ssZ)
    try {
      DataExtractsUserDataResponse result = apiInstance.getDataExtractsUserData(fromDate, loginName, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExtractsApi#getDataExtractsUserData");
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
| **fromDate** | **String**| From DateTime (YYYY-MM-DDThh:mm:ssZ) | |
| **loginName** | **String**| Login Name | |
| **toDate** | **String**| To DateTime (YYYY-MM-DDThh:mm:ssZ) | |

### Return type

[**DataExtractsUserDataResponse**](DataExtractsUserDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for eventName&lt;br&gt;Y821 : Data update event not supported&lt;br&gt;Y800 : Invalid value for fromDate.fromDate cannot be greater than current time&lt;br&gt;Y800 : Invalid value for toDate.toDate cannot be greater than current time&lt;br&gt;.Y800 : Invalid value for fromDate or toDate.fromDate and toDate cannot be older than 7 days&lt;br&gt;Y800 : Invalid value for fromDate.fromDate can not be greater than toDate&lt;br&gt;Y800 : Invalid value for loginName |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

