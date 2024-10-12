# ReputationApi

All URIs are relative to *https://api.callcontrol.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reputationReport**](ReputationApi.md#reputationReport) | **POST** /api/2015-11-01/Report | Report: report spam calls received to better tune our algorithms based upon spam calls you receive |
| [**reputationReputation**](ReputationApi.md#reputationReputation) | **GET** /api/2015-11-01/Reputation/{phoneNumber} | Reputation:  Premium service which returns a reputation informaiton of a phone number via API. |


<a id="reputationReport"></a>
# **reputationReport**
> reputationReport(callReport)

Report: report spam calls received to better tune our algorithms based upon spam calls you receive

This returns information required to perform basic call blocking behaviors&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReputationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callcontrol.com");

    ReputationApi apiInstance = new ReputationApi(defaultClient);
    CallReport callReport = new CallReport(); // CallReport | [FromBody] Call Report              PhoneNumber,               Caller name(optional),               Call category(optional),               Comment or tags(free text) (optional),               Unwanted call  - yes/no(optional),
    try {
      apiInstance.reputationReport(callReport);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReputationApi#reputationReport");
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
| **callReport** | [**CallReport**](CallReport.md)| [FromBody] Call Report              PhoneNumber,               Caller name(optional),               Call category(optional),               Comment or tags(free text) (optional),               Unwanted call  - yes/no(optional), | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request (eg. invalid phone nubmer) |  -  |

<a id="reputationReputation"></a>
# **reputationReputation**
> Reputation reputationReputation(phoneNumber)

Reputation:  Premium service which returns a reputation informaiton of a phone number via API.

This returns information required to perform basic call blocking behaviors&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReputationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callcontrol.com");

    ReputationApi apiInstance = new ReputationApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | phone number to search
    try {
      Reputation result = apiInstance.reputationReputation(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReputationApi#reputationReputation");
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
| **phoneNumber** | **String**| phone number to search | |

### Return type

[**Reputation**](Reputation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reputation information |  -  |
| **400** | Bad request (invalid phone number) |  -  |

