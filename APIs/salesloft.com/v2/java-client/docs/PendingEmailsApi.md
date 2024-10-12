# PendingEmailsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2PendingEmailsIdJsonPut**](PendingEmailsApi.md#v2PendingEmailsIdJsonPut) | **PUT** /v2/pending_emails/{id}.json | Updates the status of an email sent by an External Email Client |
| [**v2PendingEmailsJsonGet**](PendingEmailsApi.md#v2PendingEmailsJsonGet) | **GET** /v2/pending_emails.json | Fetches a list of emails ready to be sent by an external email service. Only emails sent with an External Email Client will appear here. |


<a id="v2PendingEmailsIdJsonPut"></a>
# **v2PendingEmailsIdJsonPut**
> PendingEmail v2PendingEmailsIdJsonPut(id, messageId, status, errorMessage, sentAt)

Updates the status of an email sent by an External Email Client

Updates the status of an email sent by an External Email Client. Does not affect lofted emails. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PendingEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PendingEmailsApi apiInstance = new PendingEmailsApi(defaultClient);
    String id = "id_example"; // String | Email ID
    String messageId = "messageId_example"; // String | The message id of the email that was sent
    String status = "status_example"; // String | Delivery status of the email.  Valid statuses are 'sent' and 'failed'
    String errorMessage = "errorMessage_example"; // String | The error message indicating why the email failed to send
    String sentAt = "sentAt_example"; // String | The time that the email was actually sent in iso8601 format
    try {
      PendingEmail result = apiInstance.v2PendingEmailsIdJsonPut(id, messageId, status, errorMessage, sentAt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PendingEmailsApi#v2PendingEmailsIdJsonPut");
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
| **id** | **String**| Email ID | |
| **messageId** | **String**| The message id of the email that was sent | |
| **status** | **String**| Delivery status of the email.  Valid statuses are &#39;sent&#39; and &#39;failed&#39; | |
| **errorMessage** | **String**| The error message indicating why the email failed to send | [optional] |
| **sentAt** | **String**| The time that the email was actually sent in iso8601 format | [optional] |

### Return type

[**PendingEmail**](PendingEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2PendingEmailsJsonGet"></a>
# **v2PendingEmailsJsonGet**
> List&lt;PendingEmail&gt; v2PendingEmailsJsonGet(perPage, page, includePagingCounts, limitPagingCounts)

Fetches a list of emails ready to be sent by an external email service. Only emails sent with an External Email Client will appear here.

Fetches a list of emails ready to be sent by an external email service. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PendingEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PendingEmailsApi apiInstance = new PendingEmailsApi(defaultClient);
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<PendingEmail> result = apiInstance.v2PendingEmailsJsonGet(perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PendingEmailsApi#v2PendingEmailsJsonGet");
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
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;PendingEmail&gt;**](PendingEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

