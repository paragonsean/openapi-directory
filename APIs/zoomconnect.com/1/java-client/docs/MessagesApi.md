# MessagesApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyse**](MessagesApi.md#analyse) | **POST** /api/rest/v1/messages/analyse/message-length-within-max-allowed | analyse- |
| [**analyseFull**](MessagesApi.md#analyseFull) | **POST** /api/rest/v1/messages/analyse/full | analyse-full |
| [**analyseMessageCreditCost**](MessagesApi.md#analyseMessageCreditCost) | **POST** /api/rest/v1/messages/analyse/message-credit-cost | analyse-message-credit-cost |
| [**analyseMessageEncoding**](MessagesApi.md#analyseMessageEncoding) | **POST** /api/rest/v1/messages/analyse/message-encoding | analyse-message-encoding |
| [**analyseMessageLength**](MessagesApi.md#analyseMessageLength) | **POST** /api/rest/v1/messages/analyse/message-length | analyse-message-length |
| [**analyseNumberOfMessages**](MessagesApi.md#analyseNumberOfMessages) | **POST** /api/rest/v1/messages/analyse/number-of-messages | analyse-number-of-messages |
| [**apiRestV1MessagesAllGet**](MessagesApi.md#apiRestV1MessagesAllGet) | **GET** /api/rest/v1/messages/all | all |
| [**apiRestV1MessagesMessageIdDelete**](MessagesApi.md#apiRestV1MessagesMessageIdDelete) | **DELETE** /api/rest/v1/messages/{messageId} | delete |
| [**apiRestV1MessagesMessageIdGet**](MessagesApi.md#apiRestV1MessagesMessageIdGet) | **GET** /api/rest/v1/messages/{messageId} | get |
| [**apiRestV1MessagesMessageIdMarkReadPost**](MessagesApi.md#apiRestV1MessagesMessageIdMarkReadPost) | **POST** /api/rest/v1/messages/{messageId}/markRead | markRead |
| [**apiRestV1MessagesMessageIdMarkReadPut**](MessagesApi.md#apiRestV1MessagesMessageIdMarkReadPut) | **PUT** /api/rest/v1/messages/{messageId}/markRead | markRead |
| [**apiRestV1MessagesMessageIdMarkUnreadPost**](MessagesApi.md#apiRestV1MessagesMessageIdMarkUnreadPost) | **POST** /api/rest/v1/messages/{messageId}/markUnread | markUnread |
| [**apiRestV1MessagesMessageIdMarkUnreadPut**](MessagesApi.md#apiRestV1MessagesMessageIdMarkUnreadPut) | **PUT** /api/rest/v1/messages/{messageId}/markUnread | markUnread |


<a id="analyse"></a>
# **analyse**
> Boolean analyse(body)

analyse-

Returns details for a single message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    WebServiceAnalyseMessageRequestMessageOnly body = new WebServiceAnalyseMessageRequestMessageOnly(); // WebServiceAnalyseMessageRequestMessageOnly | request
    try {
      Boolean result = apiInstance.analyse(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#analyse");
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
| **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] |

### Return type

**Boolean**

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

<a id="analyseFull"></a>
# **analyseFull**
> WebServiceAnalyseMessageResponse analyseFull(body)

analyse-full

Returns full analysis of message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    WebServiceAnalyseMessageRequestMessageAndRecipientNumber body = new WebServiceAnalyseMessageRequestMessageAndRecipientNumber(); // WebServiceAnalyseMessageRequestMessageAndRecipientNumber | request
    try {
      WebServiceAnalyseMessageResponse result = apiInstance.analyseFull(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#analyseFull");
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
| **body** | [**WebServiceAnalyseMessageRequestMessageAndRecipientNumber**](WebServiceAnalyseMessageRequestMessageAndRecipientNumber.md)| request | [optional] |

### Return type

[**WebServiceAnalyseMessageResponse**](WebServiceAnalyseMessageResponse.md)

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

<a id="analyseMessageCreditCost"></a>
# **analyseMessageCreditCost**
> Double analyseMessageCreditCost(body)

analyse-message-credit-cost

Returns the number of credit which would be required to send the request message to the requested recipient number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    WebServiceAnalyseMessageRequestMessageAndRecipientNumber body = new WebServiceAnalyseMessageRequestMessageAndRecipientNumber(); // WebServiceAnalyseMessageRequestMessageAndRecipientNumber | request
    try {
      Double result = apiInstance.analyseMessageCreditCost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#analyseMessageCreditCost");
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
| **body** | [**WebServiceAnalyseMessageRequestMessageAndRecipientNumber**](WebServiceAnalyseMessageRequestMessageAndRecipientNumber.md)| request | [optional] |

### Return type

**Double**

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

<a id="analyseMessageEncoding"></a>
# **analyseMessageEncoding**
> String analyseMessageEncoding(body)

analyse-message-encoding

Returns the message encoding that would be required to send the requested message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    WebServiceAnalyseMessageRequestMessageOnly body = new WebServiceAnalyseMessageRequestMessageOnly(); // WebServiceAnalyseMessageRequestMessageOnly | request
    try {
      String result = apiInstance.analyseMessageEncoding(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#analyseMessageEncoding");
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
| **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] |

### Return type

**String**

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

<a id="analyseMessageLength"></a>
# **analyseMessageLength**
> Integer analyseMessageLength(body)

analyse-message-length

Returns the number of characters the requested message consists of

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    WebServiceAnalyseMessageRequestMessageOnly body = new WebServiceAnalyseMessageRequestMessageOnly(); // WebServiceAnalyseMessageRequestMessageOnly | request
    try {
      Integer result = apiInstance.analyseMessageLength(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#analyseMessageLength");
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
| **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] |

### Return type

**Integer**

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

<a id="analyseNumberOfMessages"></a>
# **analyseNumberOfMessages**
> Integer analyseNumberOfMessages(body)

analyse-number-of-messages

Returns the number of SMS parts which would be sent when sending the requested message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    WebServiceAnalyseMessageRequestMessageOnly body = new WebServiceAnalyseMessageRequestMessageOnly(); // WebServiceAnalyseMessageRequestMessageOnly | request
    try {
      Integer result = apiInstance.analyseNumberOfMessages(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#analyseNumberOfMessages");
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
| **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] |

### Return type

**Integer**

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

<a id="apiRestV1MessagesAllGet"></a>
# **apiRestV1MessagesAllGet**
> WebServiceMessages apiRestV1MessagesAllGet(pageSize, page, type, status, fromDateTimeSent, toDateTimeSent, fromDateTimeReceived, toDateTimeReceived, fromNumber, toNumber, message, campaign, dataField, deleted, read, repliesToMessageId)

all

Returns all messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    Integer pageSize = 100; // Integer | number of elements to return at a time
    Integer page = 1; // Integer | page number
    String type = "OUTBOUND"; // String | filter by message type
    String status = "SCHEDULED"; // String | filter by message status
    OffsetDateTime fromDateTimeSent = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMdd
    OffsetDateTime toDateTimeSent = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMdd
    OffsetDateTime fromDateTimeReceived = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMdd
    OffsetDateTime toDateTimeReceived = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMdd
    String fromNumber = "fromNumber_example"; // String | phone number the message was sent from
    String toNumber = "toNumber_example"; // String | phone number the message was sent to
    String message = "message_example"; // String | search matching message text
    String campaign = "campaign_example"; // String | search by campaign
    String dataField = "dataField_example"; // String | search by data field
    Boolean deleted = true; // Boolean | return only deleted / not deleted messages
    Boolean read = true; // Boolean | return only read / unread messages (inbox messages only)
    String repliesToMessageId = "repliesToMessageId_example"; // String | return only inbox messages which are a reply to the message with the given message id
    try {
      WebServiceMessages result = apiInstance.apiRestV1MessagesAllGet(pageSize, page, type, status, fromDateTimeSent, toDateTimeSent, fromDateTimeReceived, toDateTimeReceived, fromNumber, toNumber, message, campaign, dataField, deleted, read, repliesToMessageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesAllGet");
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
| **type** | **String**| filter by message type | [optional] [enum: OUTBOUND, INBOUND] |
| **status** | **String**| filter by message status | [optional] [enum: SCHEDULED, UNKNOWN, SENT, FAILED, FAILED_REFUNDED, FAILED_OPTOUT, DELIVERED] |
| **fromDateTimeSent** | **OffsetDateTime**| date format: yyyyMMdd | [optional] |
| **toDateTimeSent** | **OffsetDateTime**| date format: yyyyMMdd | [optional] |
| **fromDateTimeReceived** | **OffsetDateTime**| date format: yyyyMMdd | [optional] |
| **toDateTimeReceived** | **OffsetDateTime**| date format: yyyyMMdd | [optional] |
| **fromNumber** | **String**| phone number the message was sent from | [optional] |
| **toNumber** | **String**| phone number the message was sent to | [optional] |
| **message** | **String**| search matching message text | [optional] |
| **campaign** | **String**| search by campaign | [optional] |
| **dataField** | **String**| search by data field | [optional] |
| **deleted** | **Boolean**| return only deleted / not deleted messages | [optional] |
| **read** | **Boolean**| return only read / unread messages (inbox messages only) | [optional] |
| **repliesToMessageId** | **String**| return only inbox messages which are a reply to the message with the given message id | [optional] |

### Return type

[**WebServiceMessages**](WebServiceMessages.md)

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

<a id="apiRestV1MessagesMessageIdDelete"></a>
# **apiRestV1MessagesMessageIdDelete**
> apiRestV1MessagesMessageIdDelete(messageId)

delete

Deletes a  message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      apiInstance.apiRestV1MessagesMessageIdDelete(messageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesMessageIdDelete");
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

<a id="apiRestV1MessagesMessageIdGet"></a>
# **apiRestV1MessagesMessageIdGet**
> WebServiceMessage apiRestV1MessagesMessageIdGet(messageId)

get

Returns details for a single message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      WebServiceMessage result = apiInstance.apiRestV1MessagesMessageIdGet(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesMessageIdGet");
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

[**WebServiceMessage**](WebServiceMessage.md)

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

<a id="apiRestV1MessagesMessageIdMarkReadPost"></a>
# **apiRestV1MessagesMessageIdMarkReadPost**
> WebServiceMessage apiRestV1MessagesMessageIdMarkReadPost(messageId)

markRead

Marks a  message as read

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      WebServiceMessage result = apiInstance.apiRestV1MessagesMessageIdMarkReadPost(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesMessageIdMarkReadPost");
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

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1MessagesMessageIdMarkReadPut"></a>
# **apiRestV1MessagesMessageIdMarkReadPut**
> WebServiceMessage apiRestV1MessagesMessageIdMarkReadPut(messageId)

markRead

Marks a  message as read

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      WebServiceMessage result = apiInstance.apiRestV1MessagesMessageIdMarkReadPut(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesMessageIdMarkReadPut");
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

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1MessagesMessageIdMarkUnreadPost"></a>
# **apiRestV1MessagesMessageIdMarkUnreadPost**
> WebServiceMessage apiRestV1MessagesMessageIdMarkUnreadPost(messageId)

markUnread

Marks a  message as unread

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      WebServiceMessage result = apiInstance.apiRestV1MessagesMessageIdMarkUnreadPost(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesMessageIdMarkUnreadPost");
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

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1MessagesMessageIdMarkUnreadPut"></a>
# **apiRestV1MessagesMessageIdMarkUnreadPut**
> WebServiceMessage apiRestV1MessagesMessageIdMarkUnreadPut(messageId)

markUnread

Marks a  message as unread

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageId = "messageId_example"; // String | messageId
    try {
      WebServiceMessage result = apiInstance.apiRestV1MessagesMessageIdMarkUnreadPut(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#apiRestV1MessagesMessageIdMarkUnreadPut");
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

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

