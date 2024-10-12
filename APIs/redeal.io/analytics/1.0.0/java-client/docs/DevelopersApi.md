# DevelopersApi

All URIs are relative to *https://analytics.redeal.io/api/1.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEvents**](DevelopersApi.md#getEvents) | **GET** /events | get events for analytics |


<a id="getEvents"></a>
# **getEvents**
> List&lt;EventRecord&gt; getEvents(company, site, deal, type, nexttoken, queryexecutionid)

get events for analytics

By passing in the company, site or deal Id a set of user interaction event records is returned. For pagination of a large result set use queryexecutionid and nexttoken instead. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevelopersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://analytics.redeal.io/api/1.0.0");

    DevelopersApi apiInstance = new DevelopersApi(defaultClient);
    String company = "company_example"; // String | pass an optional company Id
    String site = "site_example"; // String | pass an optional site Id
    String deal = "deal_example"; // String | pass an optional deal Id
    String type = "all"; // String | type of records to return
    String nexttoken = "nexttoken_example"; // String | next token to start returning records from
    String queryexecutionid = "queryexecutionid_example"; // String | id of execution to get more records based on next token
    try {
      List<EventRecord> result = apiInstance.getEvents(company, site, deal, type, nexttoken, queryexecutionid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevelopersApi#getEvents");
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
| **company** | **String**| pass an optional company Id | [optional] |
| **site** | **String**| pass an optional site Id | [optional] |
| **deal** | **String**| pass an optional deal Id | [optional] |
| **type** | **String**| type of records to return | [optional] [enum: all, clicks, contacts] |
| **nexttoken** | **String**| next token to start returning records from | [optional] |
| **queryexecutionid** | **String**| id of execution to get more records based on next token | [optional] |

### Return type

[**List&lt;EventRecord&gt;**](EventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | analytics results matching criteria |  -  |
| **400** | bad input parameter |  -  |

