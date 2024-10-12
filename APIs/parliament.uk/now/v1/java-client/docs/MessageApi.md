# MessageApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMessageMessageAnnunciatorCurrentGet**](MessageApi.md#apiMessageMessageAnnunciatorCurrentGet) | **GET** /api/Message/message/{annunciator}/current | Return the current message by annunciator type |
| [**apiMessageMessageAnnunciatorDateGet**](MessageApi.md#apiMessageMessageAnnunciatorDateGet) | **GET** /api/Message/message/{annunciator}/{date} | Return the most recent message by annunciator after date time specified |


<a id="apiMessageMessageAnnunciatorCurrentGet"></a>
# **apiMessageMessageAnnunciatorCurrentGet**
> MessageViewModel apiMessageMessageAnnunciatorCurrentGet(annunciator)

Return the current message by annunciator type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MessageApi apiInstance = new MessageApi(defaultClient);
    AnnunciatorMessageType annunciator = AnnunciatorMessageType.fromValue("CommonsMain"); // AnnunciatorMessageType | Current message by annunciator
    try {
      MessageViewModel result = apiInstance.apiMessageMessageAnnunciatorCurrentGet(annunciator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageApi#apiMessageMessageAnnunciatorCurrentGet");
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
| **annunciator** | [**AnnunciatorMessageType**](.md)| Current message by annunciator | [enum: CommonsMain, LordsMain] |

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="apiMessageMessageAnnunciatorDateGet"></a>
# **apiMessageMessageAnnunciatorDateGet**
> MessageViewModel apiMessageMessageAnnunciatorDateGet(annunciator, date)

Return the most recent message by annunciator after date time specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MessageApi apiInstance = new MessageApi(defaultClient);
    AnnunciatorMessageType annunciator = AnnunciatorMessageType.fromValue("CommonsMain"); // AnnunciatorMessageType | Message by annunciator type
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | First message after date time specified
    try {
      MessageViewModel result = apiInstance.apiMessageMessageAnnunciatorDateGet(annunciator, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageApi#apiMessageMessageAnnunciatorDateGet");
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
| **annunciator** | [**AnnunciatorMessageType**](.md)| Message by annunciator type | [enum: CommonsMain, LordsMain] |
| **date** | **OffsetDateTime**| First message after date time specified | |

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Latest message for given annunciator was issued before specified date |  -  |
| **400** | Date provided wasn&#39;t in a valid format |  -  |
| **404** | No message for given annunciator was issued before specified date |  -  |

