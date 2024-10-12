# EmailHistoryApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchEmailHistories**](EmailHistoryApi.md#fetchEmailHistories) | **GET** /email_history | List email histories |
| [**fetchEmailHistory**](EmailHistoryApi.md#fetchEmailHistory) | **GET** /email_history/{id} | Get an email history |


<a id="fetchEmailHistories"></a>
# **fetchEmailHistories**
> FetchEmailHistoriesResponse fetchEmailHistories(filterReceiver, filterSender, filterEmailType, sort)

List email histories

Get a list of email histories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    EmailHistoryApi apiInstance = new EmailHistoryApi(defaultClient);
    String filterReceiver = "filterReceiver_example"; // String | Fitbit Plus user id of email recipient. Required if filter[sender] is not defined.
    String filterSender = "filterSender_example"; // String | Fitbit Plus user id of email sender. Required if filter[receiver] is not defined.
    String filterEmailType = "filterEmailType_example"; // String | Type of email
    String sort = "send_time"; // String | valid sorts:   * send_time - ascending by send_time   * -send_time - descending by send_time 
    try {
      FetchEmailHistoriesResponse result = apiInstance.fetchEmailHistories(filterReceiver, filterSender, filterEmailType, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailHistoryApi#fetchEmailHistories");
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
| **filterReceiver** | **String**| Fitbit Plus user id of email recipient. Required if filter[sender] is not defined. | [optional] |
| **filterSender** | **String**| Fitbit Plus user id of email sender. Required if filter[receiver] is not defined. | [optional] |
| **filterEmailType** | **String**| Type of email | [optional] |
| **sort** | **String**| valid sorts:   * send_time - ascending by send_time   * -send_time - descending by send_time  | [optional] [enum: send_time, -send_time] |

### Return type

[**FetchEmailHistoriesResponse**](FetchEmailHistoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchEmailHistory"></a>
# **fetchEmailHistory**
> FetchEmailHistoryResponse fetchEmailHistory(id)

Get an email history

Get an email history by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    EmailHistoryApi apiInstance = new EmailHistoryApi(defaultClient);
    String id = "id_example"; // String | Email history identifier
    try {
      FetchEmailHistoryResponse result = apiInstance.fetchEmailHistory(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailHistoryApi#fetchEmailHistory");
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
| **id** | **String**| Email history identifier | |

### Return type

[**FetchEmailHistoryResponse**](FetchEmailHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

