# EmailListsAddressesApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryHardBouncedEmails**](EmailListsAddressesApi.md#queryHardBouncedEmails) | **GET** /email/hard_bounces | Query Hard Bounced Emails |
| [**queryListOfUnsubscribedEmailAddresses**](EmailListsAddressesApi.md#queryListOfUnsubscribedEmailAddresses) | **GET** /email/unsubscribes | Query List of Unsubscribed Email Addresses |


<a id="queryHardBouncedEmails"></a>
# **queryHardBouncedEmails**
> queryHardBouncedEmails(startDate, endDate, limit, offset, email)

Query Hard Bounced Emails

This endpoint allows you to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.  &gt; You must provide an &#x60;end_date&#x60;, as well as either an &#x60;email&#x60; or a &#x60;start_date&#x60;.&lt;br&gt;&lt;br&gt;If your date range has more than &#x60;limit&#x60; number of hard bounces, you will need to make multiple API calls, each time increasing the &#x60;offset&#x60; until a call returns either fewer than &#x60;limit&#x60; or zero results.  ## Response  Entries are listed in descending order.  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;emails\&quot;: [     {       \&quot;email\&quot;: \&quot;example1@braze.com\&quot;,       \&quot;hard_bounced_at\&quot;: \&quot;2016-08-25 15:24:32 +0000\&quot;     },     {       \&quot;email\&quot;: \&quot;example2@braze.com\&quot;,       \&quot;hard_bounced_at\&quot;: \&quot;2016-08-24 17:41:58 +0000\&quot;     },     {       \&quot;email\&quot;: \&quot;example3@braze.com\&quot;,       \&quot;hard_bounced_at\&quot;: \&quot;2016-08-24 12:01:13 +0000\&quot;     }   ],   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    EmailListsAddressesApi apiInstance = new EmailListsAddressesApi(defaultClient);
    String startDate = "2019-01-01"; // String | (Optional*) String in YYYY-MM-DD format   Start date of the range to retrieve hard bounces, must be earlier than `end_date`. This is treated as midnight in UTC time by the API.  *You must provide either an `email` or a `start_date`, and an `end_date`. 
    String endDate = "2019-02-01"; // String | (Optional*) String in YYYY-MM-DD format  String in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API.  *You must provide either an `email` or a `start_date`, and an `end_date`.
    String limit = "100"; // String | (Optional) Integer  Optional field to limit the number of results returned. Defaults to 100, maximum is 500.
    String offset = "1"; // String | (Optional) Integer  Optional beginning point in the list to retrieve from.
    String email = "example@braze.com"; // String | (Optional*) String  If provided, we will return whether or not the user has hard bounced.  *You must provide either an `email` or a `start_date`, and an `end_date`.
    try {
      apiInstance.queryHardBouncedEmails(startDate, endDate, limit, offset, email);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsAddressesApi#queryHardBouncedEmails");
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
| **startDate** | **String**| (Optional*) String in YYYY-MM-DD format   Start date of the range to retrieve hard bounces, must be earlier than &#x60;end_date&#x60;. This is treated as midnight in UTC time by the API.  *You must provide either an &#x60;email&#x60; or a &#x60;start_date&#x60;, and an &#x60;end_date&#x60;.  | [optional] |
| **endDate** | **String**| (Optional*) String in YYYY-MM-DD format  String in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API.  *You must provide either an &#x60;email&#x60; or a &#x60;start_date&#x60;, and an &#x60;end_date&#x60;. | [optional] |
| **limit** | **String**| (Optional) Integer  Optional field to limit the number of results returned. Defaults to 100, maximum is 500. | [optional] |
| **offset** | **String**| (Optional) Integer  Optional beginning point in the list to retrieve from. | [optional] |
| **email** | **String**| (Optional*) String  If provided, we will return whether or not the user has hard bounced.  *You must provide either an &#x60;email&#x60; or a &#x60;start_date&#x60;, and an &#x60;end_date&#x60;. | [optional] |

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
| **200** |  |  -  |

<a id="queryListOfUnsubscribedEmailAddresses"></a>
# **queryListOfUnsubscribedEmailAddresses**
> queryListOfUnsubscribedEmailAddresses(startDate, endDate, limit, offset, sortDirection, email)

Query List of Unsubscribed Email Addresses

Use the /email/unsubscribes endpoint to return emails that have unsubscribed during the time period from &#x60;start_date&#x60; to &#x60;end_date&#x60;. You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.  &gt; You must provide either an email or a start_date and an end_date. &lt;br&gt;&lt;br&gt;If your date range has more than &#x60;limit&#x60; number of unsubscribes, you will need to make multiple API calls, each time increasing the &#x60;offset&#x60; until a call returns either fewer than &#x60;limit&#x60; or zero results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    EmailListsAddressesApi apiInstance = new EmailListsAddressesApi(defaultClient);
    String startDate = "2020-01-01"; // String | (Optional*) String in YYYY-MM-DD format  Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API.
    String endDate = "2020-02-01"; // String | (Optional*)  String in YYYY-MM-DD format  End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API.
    String limit = "1"; // String | (Optional) Integer  Optional field to limit the number of results returned. Limit must be greater than 1. Defaults to 100, maximum is 500.
    String offset = "1"; // String | (Optional) Integer   Optional beginning point in the list to retrieve from
    String sortDirection = "desc"; // String | (Optional) String  Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest.
    String email = "example@braze.com"; // String | (Optional*) String  If provided, we will return whether or not the user has unsubscribed
    try {
      apiInstance.queryListOfUnsubscribedEmailAddresses(startDate, endDate, limit, offset, sortDirection, email);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsAddressesApi#queryListOfUnsubscribedEmailAddresses");
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
| **startDate** | **String**| (Optional*) String in YYYY-MM-DD format  Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. | [optional] |
| **endDate** | **String**| (Optional*)  String in YYYY-MM-DD format  End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. | [optional] |
| **limit** | **String**| (Optional) Integer  Optional field to limit the number of results returned. Limit must be greater than 1. Defaults to 100, maximum is 500. | [optional] |
| **offset** | **String**| (Optional) Integer   Optional beginning point in the list to retrieve from | [optional] |
| **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;asc&#x60; to sort unsubscribes from oldest to newest. Pass in &#x60;desc&#x60; to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. | [optional] |
| **email** | **String**| (Optional*) String  If provided, we will return whether or not the user has unsubscribed | [optional] |

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
| **200** |  |  -  |

