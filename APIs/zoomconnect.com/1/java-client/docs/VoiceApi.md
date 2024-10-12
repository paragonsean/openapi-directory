# VoiceApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRestV1VoiceAllGet**](VoiceApi.md#apiRestV1VoiceAllGet) | **GET** /api/rest/v1/voice/all | all |
| [**apiRestV1VoiceMessageIdDelete**](VoiceApi.md#apiRestV1VoiceMessageIdDelete) | **DELETE** /api/rest/v1/voice/{messageId} | delete |
| [**apiRestV1VoiceMessageIdGet**](VoiceApi.md#apiRestV1VoiceMessageIdGet) | **GET** /api/rest/v1/voice/{messageId} | get |
| [**singleAudio**](VoiceApi.md#singleAudio) | **POST** /api/rest/v1/voice/single-audio | single-audio |
| [**singleText**](VoiceApi.md#singleText) | **POST** /api/rest/v1/voice/single-text | single-text |


<a id="apiRestV1VoiceAllGet"></a>
# **apiRestV1VoiceAllGet**
> WebServiceVoiceMessages apiRestV1VoiceAllGet(pageSize, page, status, fromDateTimeSent, toDateTimeSent, toNumber, message, campaign, dataField, deleted)

all

Returns all voice messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    VoiceApi apiInstance = new VoiceApi(defaultClient);
    Integer pageSize = 100; // Integer | number of elements to return at a time
    Integer page = 1; // Integer | page number
    String status = "SCHEDULED"; // String | filter by message status
    OffsetDateTime fromDateTimeSent = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMdd
    OffsetDateTime toDateTimeSent = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMdd
    String toNumber = "toNumber_example"; // String | phone number the message was sent to
    String message = "message_example"; // String | search matching message text
    String campaign = "campaign_example"; // String | search by campaign
    String dataField = "dataField_example"; // String | search by data field
    Boolean deleted = true; // Boolean | return only deleted / not deleted messages
    try {
      WebServiceVoiceMessages result = apiInstance.apiRestV1VoiceAllGet(pageSize, page, status, fromDateTimeSent, toDateTimeSent, toNumber, message, campaign, dataField, deleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceApi#apiRestV1VoiceAllGet");
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
| **pageSize** | **Integer**| number of elements to return at a time | [optional] [default to 100] |
| **page** | **Integer**| page number | [optional] [default to 1] |
| **status** | **String**| filter by message status | [optional] [enum: SCHEDULED, UNKNOWN, SENT, FAILED, FAILED_REFUNDED, FAILED_OPTOUT, DELIVERED] |
| **fromDateTimeSent** | **OffsetDateTime**| date format: yyyyMMdd | [optional] |
| **toDateTimeSent** | **OffsetDateTime**| date format: yyyyMMdd | [optional] |
| **toNumber** | **String**| phone number the message was sent to | [optional] |
| **message** | **String**| search matching message text | [optional] |
| **campaign** | **String**| search by campaign | [optional] |
| **dataField** | **String**| search by data field | [optional] |
| **deleted** | **Boolean**| return only deleted / not deleted messages | [optional] |

### Return type

[**WebServiceVoiceMessages**](WebServiceVoiceMessages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1VoiceMessageIdDelete"></a>
# **apiRestV1VoiceMessageIdDelete**
> apiRestV1VoiceMessageIdDelete(messageId)

delete

Deletes a  message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    VoiceApi apiInstance = new VoiceApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      apiInstance.apiRestV1VoiceMessageIdDelete(messageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceApi#apiRestV1VoiceMessageIdDelete");
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
| **messageId** | **String**| messageId | |

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
| **200** | Description was not specified |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="apiRestV1VoiceMessageIdGet"></a>
# **apiRestV1VoiceMessageIdGet**
> WebServiceVoiceMessage apiRestV1VoiceMessageIdGet(messageId)

get

Returns details for a single message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    VoiceApi apiInstance = new VoiceApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      WebServiceVoiceMessage result = apiInstance.apiRestV1VoiceMessageIdGet(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceApi#apiRestV1VoiceMessageIdGet");
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
| **messageId** | **String**| messageId | |

### Return type

[**WebServiceVoiceMessage**](WebServiceVoiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="singleAudio"></a>
# **singleAudio**
> WebServiceSendVoiceMessageResponse singleAudio(recipientNumber, _file, campaign, dataField, retryCount, retryMinimumInterval, retryMaximumInterval)

single-audio

Send a single audio voice message to one recipient. Note, Content-Type header must be set to multipart/form-data for this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    VoiceApi apiInstance = new VoiceApi(defaultClient);
    String recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
    File _file = new File("/path/to/file"); // File | audio file to play, supports MP3 or WAV format
    String campaign = "campaign_example"; // String | optional campaign name
    String dataField = "dataField_example"; // String | optional extra data
    Integer retryCount = 56; // Integer | optional number of times to retry unanswered call
    Integer retryMinimumInterval = 56; // Integer | optional minimum interval in minutes between retry attempts
    Integer retryMaximumInterval = 56; // Integer | optional maximum interval in minutes between retry attempts
    try {
      WebServiceSendVoiceMessageResponse result = apiInstance.singleAudio(recipientNumber, _file, campaign, dataField, retryCount, retryMinimumInterval, retryMaximumInterval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceApi#singleAudio");
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
| **recipientNumber** | **String**| the phone number of the recipient to send to | |
| **_file** | **File**| audio file to play, supports MP3 or WAV format | |
| **campaign** | **String**| optional campaign name | [optional] |
| **dataField** | **String**| optional extra data | [optional] |
| **retryCount** | **Integer**| optional number of times to retry unanswered call | [optional] |
| **retryMinimumInterval** | **Integer**| optional minimum interval in minutes between retry attempts | [optional] |
| **retryMaximumInterval** | **Integer**| optional maximum interval in minutes between retry attempts | [optional] |

### Return type

[**WebServiceSendVoiceMessageResponse**](WebServiceSendVoiceMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="singleText"></a>
# **singleText**
> WebServiceSendVoiceMessageResponse singleText(body)

single-text

Send a single text voice message to one recipient

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    VoiceApi apiInstance = new VoiceApi(defaultClient);
    WebServiceVoiceMessageSendSingleTextRequest body = new WebServiceVoiceMessageSendSingleTextRequest(); // WebServiceVoiceMessageSendSingleTextRequest | request
    try {
      WebServiceSendVoiceMessageResponse result = apiInstance.singleText(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceApi#singleText");
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
| **body** | [**WebServiceVoiceMessageSendSingleTextRequest**](WebServiceVoiceMessageSendSingleTextRequest.md)| request | [optional] |

### Return type

[**WebServiceSendVoiceMessageResponse**](WebServiceSendVoiceMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

