# MessagesApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bypassRulesForInboundMessage**](MessagesApiApi.md#bypassRulesForInboundMessage) | **PUT** /messages/inbound/{messageid}/bypass | Bypass rules for a blocked inbound message |
| [**getClicksForSingleOutboundMessage**](MessagesApiApi.md#getClicksForSingleOutboundMessage) | **GET** /messages/outbound/clicks/{messageid} | Retrieve Message Clicks |
| [**getInboundMessageDetails**](MessagesApiApi.md#getInboundMessageDetails) | **GET** /messages/inbound/{messageid}/details | Inbound message details |
| [**getOpensForSingleOutboundMessage**](MessagesApiApi.md#getOpensForSingleOutboundMessage) | **GET** /messages/outbound/opens/{messageid} | Retrieve Message Opens |
| [**getOutboundMessageDetails**](MessagesApiApi.md#getOutboundMessageDetails) | **GET** /messages/outbound/{messageid}/details | Outbound message details |
| [**getOutboundMessageDump**](MessagesApiApi.md#getOutboundMessageDump) | **GET** /messages/outbound/{messageid}/dump | Outbound message dump |
| [**retryInboundMessageProcessing**](MessagesApiApi.md#retryInboundMessageProcessing) | **PUT** /messages/inbound/{messageid}/retry | Retry a failed inbound message for processing |
| [**searchClicksForOutboundMessages**](MessagesApiApi.md#searchClicksForOutboundMessages) | **GET** /messages/outbound/clicks | Clicks for a all messages |
| [**searchInboundMessages**](MessagesApiApi.md#searchInboundMessages) | **GET** /messages/inbound | Inbound message search |
| [**searchOpensForOutboundMessages**](MessagesApiApi.md#searchOpensForOutboundMessages) | **GET** /messages/outbound/opens | Opens for all messages |
| [**searchOutboundMessages**](MessagesApiApi.md#searchOutboundMessages) | **GET** /messages/outbound | Outbound message search |


<a id="bypassRulesForInboundMessage"></a>
# **bypassRulesForInboundMessage**
> StandardPostmarkResponse bypassRulesForInboundMessage(xPostmarkServerToken, messageid)

Bypass rules for a blocked inbound message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the message which should bypass inbound rules.
    try {
      StandardPostmarkResponse result = apiInstance.bypassRulesForInboundMessage(xPostmarkServerToken, messageid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#bypassRulesForInboundMessage");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the message which should bypass inbound rules. | |

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getClicksForSingleOutboundMessage"></a>
# **getClicksForSingleOutboundMessage**
> MessageClickSearchResponse getClicksForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset)

Retrieve Message Clicks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the Outbound Message for which click statistics should be retrieved.
    Integer count = 1; // Integer | Number of message clicks to return per request. Max 500.
    Integer offset = 0; // Integer | Number of messages to skip.
    try {
      MessageClickSearchResponse result = apiInstance.getClicksForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#getClicksForSingleOutboundMessage");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the Outbound Message for which click statistics should be retrieved. | |
| **count** | **Integer**| Number of message clicks to return per request. Max 500. | [default to 1] |
| **offset** | **Integer**| Number of messages to skip. | [default to 0] |

### Return type

[**MessageClickSearchResponse**](MessageClickSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getInboundMessageDetails"></a>
# **getInboundMessageDetails**
> InboundMessageFullDetailsResponse getInboundMessageDetails(xPostmarkServerToken, messageid)

Inbound message details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the message for which to details will be retrieved.
    try {
      InboundMessageFullDetailsResponse result = apiInstance.getInboundMessageDetails(xPostmarkServerToken, messageid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#getInboundMessageDetails");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the message for which to details will be retrieved. | |

### Return type

[**InboundMessageFullDetailsResponse**](InboundMessageFullDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOpensForSingleOutboundMessage"></a>
# **getOpensForSingleOutboundMessage**
> MessageOpenSearchResponse getOpensForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset)

Retrieve Message Opens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the Outbound Message for which open statistics should be retrieved.
    Integer count = 1; // Integer | Number of message opens to return per request. Max 500.
    Integer offset = 0; // Integer | Number of messages to skip.
    try {
      MessageOpenSearchResponse result = apiInstance.getOpensForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#getOpensForSingleOutboundMessage");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the Outbound Message for which open statistics should be retrieved. | |
| **count** | **Integer**| Number of message opens to return per request. Max 500. | [default to 1] |
| **offset** | **Integer**| Number of messages to skip. | [default to 0] |

### Return type

[**MessageOpenSearchResponse**](MessageOpenSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundMessageDetails"></a>
# **getOutboundMessageDetails**
> OutboundMessageDetailsResponse getOutboundMessageDetails(xPostmarkServerToken, messageid)

Outbound message details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the message for which to retrieve details.
    try {
      OutboundMessageDetailsResponse result = apiInstance.getOutboundMessageDetails(xPostmarkServerToken, messageid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#getOutboundMessageDetails");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the message for which to retrieve details. | |

### Return type

[**OutboundMessageDetailsResponse**](OutboundMessageDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundMessageDump"></a>
# **getOutboundMessageDump**
> OutboundMessageDumpResponse getOutboundMessageDump(xPostmarkServerToken, messageid)

Outbound message dump

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the message for which to retrieve a dump.
    try {
      OutboundMessageDumpResponse result = apiInstance.getOutboundMessageDump(xPostmarkServerToken, messageid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#getOutboundMessageDump");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the message for which to retrieve a dump. | |

### Return type

[**OutboundMessageDumpResponse**](OutboundMessageDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="retryInboundMessageProcessing"></a>
# **retryInboundMessageProcessing**
> StandardPostmarkResponse retryInboundMessageProcessing(xPostmarkServerToken, messageid)

Retry a failed inbound message for processing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String messageid = "messageid_example"; // String | The ID of the inbound message on which we should retry processing.
    try {
      StandardPostmarkResponse result = apiInstance.retryInboundMessageProcessing(xPostmarkServerToken, messageid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#retryInboundMessageProcessing");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **messageid** | **String**| The ID of the inbound message on which we should retry processing. | |

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="searchClicksForOutboundMessages"></a>
# **searchClicksForOutboundMessages**
> MessageClickSearchResponse searchClicksForOutboundMessages(xPostmarkServerToken, count, offset, recipient, tag, clientName, clientCompany, clientFamily, osName, osFamily, osCompany, platform, country, region, city)

Clicks for a all messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer count = 56; // Integer | Number of message clicks to return per request. Max 500.
    Integer offset = 56; // Integer | Number of messages to skip
    String recipient = "recipient_example"; // String | Filter by To, Cc, Bcc
    String tag = "tag_example"; // String | Filter by tag
    String clientName = "clientName_example"; // String | Filter by client name, i.e. Outlook, Gmail
    String clientCompany = "clientCompany_example"; // String | Filter by company, i.e. Microsoft, Apple, Google
    String clientFamily = "clientFamily_example"; // String | Filter by client family, i.e. OS X, Chrome
    String osName = "osName_example"; // String | Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7
    String osFamily = "osFamily_example"; // String | Filter by kind of OS used without specific version, i.e. OS X, Windows
    String osCompany = "osCompany_example"; // String | Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation
    String platform = "platform_example"; // String | Filter by platform, i.e. webmail, desktop, mobile
    String country = "country_example"; // String | Filter by country messages were opened in, i.e. Denmark, Russia
    String region = "region_example"; // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
    String city = "city_example"; // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
    try {
      MessageClickSearchResponse result = apiInstance.searchClicksForOutboundMessages(xPostmarkServerToken, count, offset, recipient, tag, clientName, clientCompany, clientFamily, osName, osFamily, osCompany, platform, country, region, city);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#searchClicksForOutboundMessages");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **count** | **Integer**| Number of message clicks to return per request. Max 500. | |
| **offset** | **Integer**| Number of messages to skip | |
| **recipient** | **String**| Filter by To, Cc, Bcc | [optional] |
| **tag** | **String**| Filter by tag | [optional] |
| **clientName** | **String**| Filter by client name, i.e. Outlook, Gmail | [optional] |
| **clientCompany** | **String**| Filter by company, i.e. Microsoft, Apple, Google | [optional] |
| **clientFamily** | **String**| Filter by client family, i.e. OS X, Chrome | [optional] |
| **osName** | **String**| Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7 | [optional] |
| **osFamily** | **String**| Filter by kind of OS used without specific version, i.e. OS X, Windows | [optional] |
| **osCompany** | **String**| Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation | [optional] |
| **platform** | **String**| Filter by platform, i.e. webmail, desktop, mobile | [optional] |
| **country** | **String**| Filter by country messages were opened in, i.e. Denmark, Russia | [optional] |
| **region** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] |
| **city** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] |

### Return type

[**MessageClickSearchResponse**](MessageClickSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="searchInboundMessages"></a>
# **searchInboundMessages**
> InboundSearchResponse searchInboundMessages(xPostmarkServerToken, count, offset, recipient, fromemail, subject, mailboxhash, tag, status, todate, fromdate)

Inbound message search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer count = 56; // Integer | Number of messages to return per request. Max 500.
    Integer offset = 56; // Integer | Number of messages to skip
    String recipient = "recipient_example"; // String | Filter by the user who was receiving the email
    String fromemail = "fromemail_example"; // String | Filter by the sender email address
    String subject = "subject_example"; // String | Filter by email subject
    String mailboxhash = "mailboxhash_example"; // String | Filter by mailboxhash
    String tag = "tag_example"; // String | Filter by tag
    String status = "blocked"; // String | Filter by status (`blocked`, `processed`, `queued`, `failed`, `scheduled`)
    LocalDate todate = LocalDate.now(); // LocalDate | Filter messages up to the date specified. e.g. `2014-02-01`
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter messages starting from the date specified. e.g. `2014-02-01`
    try {
      InboundSearchResponse result = apiInstance.searchInboundMessages(xPostmarkServerToken, count, offset, recipient, fromemail, subject, mailboxhash, tag, status, todate, fromdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#searchInboundMessages");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **count** | **Integer**| Number of messages to return per request. Max 500. | |
| **offset** | **Integer**| Number of messages to skip | |
| **recipient** | **String**| Filter by the user who was receiving the email | [optional] |
| **fromemail** | **String**| Filter by the sender email address | [optional] |
| **subject** | **String**| Filter by email subject | [optional] |
| **mailboxhash** | **String**| Filter by mailboxhash | [optional] |
| **tag** | **String**| Filter by tag | [optional] |
| **status** | **String**| Filter by status (&#x60;blocked&#x60;, &#x60;processed&#x60;, &#x60;queued&#x60;, &#x60;failed&#x60;, &#x60;scheduled&#x60;) | [optional] [enum: blocked, processed, queued, failed, scheduled] |
| **todate** | **LocalDate**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |
| **fromdate** | **LocalDate**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**InboundSearchResponse**](InboundSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="searchOpensForOutboundMessages"></a>
# **searchOpensForOutboundMessages**
> MessageOpenSearchResponse searchOpensForOutboundMessages(xPostmarkServerToken, count, offset, recipient, tag, clientName, clientCompany, clientFamily, osName, osFamily, osCompany, platform, country, region, city)

Opens for all messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer count = 56; // Integer | Number of message opens to return per request. Max 500.
    Integer offset = 56; // Integer | Number of messages to skip
    String recipient = "recipient_example"; // String | Filter by To, Cc, Bcc
    String tag = "tag_example"; // String | Filter by tag
    String clientName = "clientName_example"; // String | Filter by client name, i.e. Outlook, Gmail
    String clientCompany = "clientCompany_example"; // String | Filter by company, i.e. Microsoft, Apple, Google
    String clientFamily = "clientFamily_example"; // String | Filter by client family, i.e. OS X, Chrome
    String osName = "osName_example"; // String | Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7
    String osFamily = "osFamily_example"; // String | Filter by kind of OS used without specific version, i.e. OS X, Windows
    String osCompany = "osCompany_example"; // String | Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation
    String platform = "platform_example"; // String | Filter by platform, i.e. webmail, desktop, mobile
    String country = "country_example"; // String | Filter by country messages were opened in, i.e. Denmark, Russia
    String region = "region_example"; // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
    String city = "city_example"; // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
    try {
      MessageOpenSearchResponse result = apiInstance.searchOpensForOutboundMessages(xPostmarkServerToken, count, offset, recipient, tag, clientName, clientCompany, clientFamily, osName, osFamily, osCompany, platform, country, region, city);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#searchOpensForOutboundMessages");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **count** | **Integer**| Number of message opens to return per request. Max 500. | |
| **offset** | **Integer**| Number of messages to skip | |
| **recipient** | **String**| Filter by To, Cc, Bcc | [optional] |
| **tag** | **String**| Filter by tag | [optional] |
| **clientName** | **String**| Filter by client name, i.e. Outlook, Gmail | [optional] |
| **clientCompany** | **String**| Filter by company, i.e. Microsoft, Apple, Google | [optional] |
| **clientFamily** | **String**| Filter by client family, i.e. OS X, Chrome | [optional] |
| **osName** | **String**| Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7 | [optional] |
| **osFamily** | **String**| Filter by kind of OS used without specific version, i.e. OS X, Windows | [optional] |
| **osCompany** | **String**| Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation | [optional] |
| **platform** | **String**| Filter by platform, i.e. webmail, desktop, mobile | [optional] |
| **country** | **String**| Filter by country messages were opened in, i.e. Denmark, Russia | [optional] |
| **region** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] |
| **city** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] |

### Return type

[**MessageOpenSearchResponse**](MessageOpenSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="searchOutboundMessages"></a>
# **searchOutboundMessages**
> OutboundSearchResponse searchOutboundMessages(xPostmarkServerToken, count, offset, recipient, fromemail, tag, status, todate, fromdate)

Outbound message search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    MessagesApiApi apiInstance = new MessagesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer count = 56; // Integer | Number of messages to return per request. Max 500.
    Integer offset = 56; // Integer | Number of messages to skip
    String recipient = "recipient_example"; // String | Filter by the user who was receiving the email
    String fromemail = "fromemail_example"; // String | Filter by the sender email address
    String tag = "tag_example"; // String | Filter by tag
    String status = "queued"; // String | Filter by status (`queued` or `sent`)
    LocalDate todate = LocalDate.now(); // LocalDate | Filter messages up to the date specified. e.g. `2014-02-01`
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter messages starting from the date specified. e.g. `2014-02-01`
    try {
      OutboundSearchResponse result = apiInstance.searchOutboundMessages(xPostmarkServerToken, count, offset, recipient, fromemail, tag, status, todate, fromdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApiApi#searchOutboundMessages");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **count** | **Integer**| Number of messages to return per request. Max 500. | |
| **offset** | **Integer**| Number of messages to skip | |
| **recipient** | **String**| Filter by the user who was receiving the email | [optional] |
| **fromemail** | **String**| Filter by the sender email address | [optional] |
| **tag** | **String**| Filter by tag | [optional] |
| **status** | **String**| Filter by status (&#x60;queued&#x60; or &#x60;sent&#x60;) | [optional] [enum: queued, sent] |
| **todate** | **LocalDate**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |
| **fromdate** | **LocalDate**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**OutboundSearchResponse**](OutboundSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

