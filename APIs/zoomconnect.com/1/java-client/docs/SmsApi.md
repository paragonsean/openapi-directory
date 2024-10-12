# SmsApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRestV1SmsSendBulkGet**](SmsApi.md#apiRestV1SmsSendBulkGet) | **GET** /api/rest/v1/sms/send-bulk | send-bulk |
| [**apiRestV1SmsSendBulkPost**](SmsApi.md#apiRestV1SmsSendBulkPost) | **POST** /api/rest/v1/sms/send-bulk | send-bulk |
| [**apiRestV1SmsSendGet**](SmsApi.md#apiRestV1SmsSendGet) | **GET** /api/rest/v1/sms/send | send |
| [**apiRestV1SmsSendPost**](SmsApi.md#apiRestV1SmsSendPost) | **POST** /api/rest/v1/sms/send | send |
| [**apiRestV1SmsSendUrlParametersGet**](SmsApi.md#apiRestV1SmsSendUrlParametersGet) | **GET** /api/rest/v1/sms/send-url-parameters | send-url-parameters |
| [**apiRestV1SmsSendUrlParametersPost**](SmsApi.md#apiRestV1SmsSendUrlParametersPost) | **POST** /api/rest/v1/sms/send-url-parameters | send-url-parameters |
| [**apiRestV1SmsSendUrlTokenGet**](SmsApi.md#apiRestV1SmsSendUrlTokenGet) | **GET** /api/rest/v1/sms/send-url/{token} | send-url |
| [**apiRestV1SmsSendUrlTokenPost**](SmsApi.md#apiRestV1SmsSendUrlTokenPost) | **POST** /api/rest/v1/sms/send-url/{token} | send-url |


<a id="apiRestV1SmsSendBulkGet"></a>
# **apiRestV1SmsSendBulkGet**
> WebServiceSendSmsRequests apiRestV1SmsSendBulkGet()

send-bulk

Returns an example of the data to POST to send multiple messages in one transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    try {
      WebServiceSendSmsRequests result = apiInstance.apiRestV1SmsSendBulkGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendBulkGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebServiceSendSmsRequests**](WebServiceSendSmsRequests.md)

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

<a id="apiRestV1SmsSendBulkPost"></a>
# **apiRestV1SmsSendBulkPost**
> WebServiceSendSmsResponses apiRestV1SmsSendBulkPost(body)

send-bulk

Send multiple messages in one transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    WebServiceSendSmsRequests body = new WebServiceSendSmsRequests(); // WebServiceSendSmsRequests | requests
    try {
      WebServiceSendSmsResponses result = apiInstance.apiRestV1SmsSendBulkPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendBulkPost");
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
| **body** | [**WebServiceSendSmsRequests**](WebServiceSendSmsRequests.md)| requests | [optional] |

### Return type

[**WebServiceSendSmsResponses**](WebServiceSendSmsResponses.md)

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

<a id="apiRestV1SmsSendGet"></a>
# **apiRestV1SmsSendGet**
> WebServiceSendSmsRequest apiRestV1SmsSendGet()

send

Returns an example of the data to POST to send a single message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    try {
      WebServiceSendSmsRequest result = apiInstance.apiRestV1SmsSendGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebServiceSendSmsRequest**](WebServiceSendSmsRequest.md)

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

<a id="apiRestV1SmsSendPost"></a>
# **apiRestV1SmsSendPost**
> WebServiceSendSmsResponse apiRestV1SmsSendPost(body)

send

Sends a single message. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; fields are required. All other fields are optional.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    WebServiceSendSmsRequest body = new WebServiceSendSmsRequest(); // WebServiceSendSmsRequest | request
    try {
      WebServiceSendSmsResponse result = apiInstance.apiRestV1SmsSendPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendPost");
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
| **body** | [**WebServiceSendSmsRequest**](WebServiceSendSmsRequest.md)| request | [optional] |

### Return type

[**WebServiceSendSmsResponse**](WebServiceSendSmsResponse.md)

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
| **400** | Validation error&lt;/br&gt;&lt;/br&gt;Code and message:&lt;ul&gt;&lt;li&gt;2 - Invalid mobile number&lt;/li&gt;&lt;li&gt;3 - Message cannot be empty&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1SmsSendUrlParametersGet"></a>
# **apiRestV1SmsSendUrlParametersGet**
> String apiRestV1SmsSendUrlParametersGet(recipientNumber, message, dateToSend, campaign, dataField)

send-url-parameters

Send a single message using URL parameters.The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    String recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
    String message = "message_example"; // String | the message to send
    OffsetDateTime dateToSend = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMddHHmm
    String campaign = "campaign_example"; // String | optional campaign name
    String dataField = "dataField_example"; // String | optional extra data
    try {
      String result = apiInstance.apiRestV1SmsSendUrlParametersGet(recipientNumber, message, dateToSend, campaign, dataField);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendUrlParametersGet");
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
| **message** | **String**| the message to send | |
| **dateToSend** | **OffsetDateTime**| date format: yyyyMMddHHmm | [optional] |
| **campaign** | **String**| optional campaign name | [optional] |
| **dataField** | **String**| optional extra data | [optional] |

### Return type

**String**

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

<a id="apiRestV1SmsSendUrlParametersPost"></a>
# **apiRestV1SmsSendUrlParametersPost**
> String apiRestV1SmsSendUrlParametersPost(recipientNumber, message, dateToSend, campaign, dataField)

send-url-parameters

Send a single message using URL parameters.The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    String recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
    String message = "message_example"; // String | the message to send
    OffsetDateTime dateToSend = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMddHHmm
    String campaign = "campaign_example"; // String | optional campaign name
    String dataField = "dataField_example"; // String | optional extra data
    try {
      String result = apiInstance.apiRestV1SmsSendUrlParametersPost(recipientNumber, message, dateToSend, campaign, dataField);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendUrlParametersPost");
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
| **message** | **String**| the message to send | |
| **dateToSend** | **OffsetDateTime**| date format: yyyyMMddHHmm | [optional] |
| **campaign** | **String**| optional campaign name | [optional] |
| **dataField** | **String**| optional extra data | [optional] |

### Return type

**String**

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

<a id="apiRestV1SmsSendUrlTokenGet"></a>
# **apiRestV1SmsSendUrlTokenGet**
> String apiRestV1SmsSendUrlTokenGet(token, recipientNumber, message, dateToSend, campaign, dataField)

send-url

Send a single message using your unique URL without having to authenticate using your email address or REST API token. The token required is the URL Sending token available on the developer setting page. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional. Not that the token required here is 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    String token = "token_example"; // String | token
    String recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
    String message = "message_example"; // String | the message to send
    OffsetDateTime dateToSend = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMddHHmm
    String campaign = "campaign_example"; // String | optional campaign name
    String dataField = "dataField_example"; // String | optional extra data
    try {
      String result = apiInstance.apiRestV1SmsSendUrlTokenGet(token, recipientNumber, message, dateToSend, campaign, dataField);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendUrlTokenGet");
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
| **token** | **String**| token | |
| **recipientNumber** | **String**| the phone number of the recipient to send to | |
| **message** | **String**| the message to send | |
| **dateToSend** | **OffsetDateTime**| date format: yyyyMMddHHmm | [optional] |
| **campaign** | **String**| optional campaign name | [optional] |
| **dataField** | **String**| optional extra data | [optional] |

### Return type

**String**

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

<a id="apiRestV1SmsSendUrlTokenPost"></a>
# **apiRestV1SmsSendUrlTokenPost**
> String apiRestV1SmsSendUrlTokenPost(token, recipientNumber, message, dateToSend, campaign, dataField)

send-url

Send a single message using your unique URL without having to authenticate using your email address or REST API token. The token required is the URL Sending token available on the developer setting page. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional. Not that the token required here is 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    SmsApi apiInstance = new SmsApi(defaultClient);
    String token = "token_example"; // String | token
    String recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
    String message = "message_example"; // String | the message to send
    OffsetDateTime dateToSend = OffsetDateTime.now(); // OffsetDateTime | date format: yyyyMMddHHmm
    String campaign = "campaign_example"; // String | optional campaign name
    String dataField = "dataField_example"; // String | optional extra data
    try {
      String result = apiInstance.apiRestV1SmsSendUrlTokenPost(token, recipientNumber, message, dateToSend, campaign, dataField);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#apiRestV1SmsSendUrlTokenPost");
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
| **token** | **String**| token | |
| **recipientNumber** | **String**| the phone number of the recipient to send to | |
| **message** | **String**| the message to send | |
| **dateToSend** | **OffsetDateTime**| date format: yyyyMMddHHmm | [optional] |
| **campaign** | **String**| optional campaign name | [optional] |
| **dataField** | **String**| optional extra data | [optional] |

### Return type

**String**

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

