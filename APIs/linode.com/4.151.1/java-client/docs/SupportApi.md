# SupportApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**closeTicket**](SupportApi.md#closeTicket) | **POST** /support/tickets/{ticketId}/close | Support Ticket Close |
| [**createTicket**](SupportApi.md#createTicket) | **POST** /support/tickets | Support Ticket Open |
| [**createTicketAttachment**](SupportApi.md#createTicketAttachment) | **POST** /support/tickets/{ticketId}/attachments | Support Ticket Attachment Create |
| [**createTicketReply**](SupportApi.md#createTicketReply) | **POST** /support/tickets/{ticketId}/replies | Reply Create |
| [**getTicket**](SupportApi.md#getTicket) | **GET** /support/tickets/{ticketId} | Support Ticket View |
| [**getTicketReplies**](SupportApi.md#getTicketReplies) | **GET** /support/tickets/{ticketId}/replies | Replies List |
| [**getTickets**](SupportApi.md#getTickets) | **GET** /support/tickets | Support Tickets List |


<a id="closeTicket"></a>
# **closeTicket**
> Object closeTicket(ticketId)

Support Ticket Close

Closes a Support Ticket you have access to modify. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    Integer ticketId = 56; // Integer | The ID of the Support Ticket.
    try {
      Object result = apiInstance.closeTicket(ticketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#closeTicket");
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
| **ticketId** | **Integer**| The ID of the Support Ticket. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Support Ticket closed successfully. |  -  |
| **0** | Error |  -  |

<a id="createTicket"></a>
# **createTicket**
> SupportTicket createTicket(supportTicketRequest)

Support Ticket Open

Open a Support Ticket. Only one of the ID attributes (&#x60;linode_id&#x60;, &#x60;domain_id&#x60;, etc.) can be set on a single Support Ticket. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    SupportTicketRequest supportTicketRequest = new SupportTicketRequest(); // SupportTicketRequest | Open a Support Ticket.
    try {
      SupportTicket result = apiInstance.createTicket(supportTicketRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#createTicket");
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
| **supportTicketRequest** | [**SupportTicketRequest**](SupportTicketRequest.md)| Open a Support Ticket. | [optional] |

### Return type

[**SupportTicket**](SupportTicket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Support Ticket opened. |  -  |
| **0** | Error |  -  |

<a id="createTicketAttachment"></a>
# **createTicketAttachment**
> Object createTicketAttachment(ticketId, _file)

Support Ticket Attachment Create

Adds a file attachment to an existing Support Ticket on your Account. File attachments are used to assist our Support team in resolving your Ticket. Examples of attachments are screen shots and text files that provide additional information.  The file attachment is submitted in the request as multipart/form-data.  **Note**: Accepted file extensions include: .gif, .jpg, .jpeg, .pjpg, .pjpeg, .tif, .tiff, .png, .pdf, or .txt. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    Integer ticketId = 56; // Integer | The ID of the Support Ticket.
    String _file = "_file_example"; // String | The local, absolute path to the file you want to attach to your Support Ticket. 
    try {
      Object result = apiInstance.createTicketAttachment(ticketId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#createTicketAttachment");
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
| **ticketId** | **Integer**| The ID of the Support Ticket. | |
| **_file** | **String**| The local, absolute path to the file you want to attach to your Support Ticket.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment created. |  -  |
| **0** | Error |  -  |

<a id="createTicketReply"></a>
# **createTicketReply**
> SupportTicketReply createTicketReply(ticketId, createTicketReplyRequest)

Reply Create

Adds a reply to an existing Support Ticket. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    Integer ticketId = 56; // Integer | The ID of the Support Ticket.
    CreateTicketReplyRequest createTicketReplyRequest = new CreateTicketReplyRequest(); // CreateTicketReplyRequest | Add a reply.
    try {
      SupportTicketReply result = apiInstance.createTicketReply(ticketId, createTicketReplyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#createTicketReply");
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
| **ticketId** | **Integer**| The ID of the Support Ticket. | |
| **createTicketReplyRequest** | [**CreateTicketReplyRequest**](CreateTicketReplyRequest.md)| Add a reply. | |

### Return type

[**SupportTicketReply**](SupportTicketReply.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reply created. |  -  |
| **0** | Error |  -  |

<a id="getTicket"></a>
# **getTicket**
> SupportTicket getTicket(ticketId)

Support Ticket View

Returns a Support Ticket under your Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    Integer ticketId = 56; // Integer | The ID of the Support Ticket.
    try {
      SupportTicket result = apiInstance.getTicket(ticketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#getTicket");
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
| **ticketId** | **Integer**| The ID of the Support Ticket. | |

### Return type

[**SupportTicket**](SupportTicket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single SupportTicket object. |  -  |
| **0** | Error |  -  |

<a id="getTicketReplies"></a>
# **getTicketReplies**
> GetTicketReplies200Response getTicketReplies(ticketId, page, pageSize)

Replies List

Returns a collection of replies to a Support Ticket on your Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    Integer ticketId = 56; // Integer | The ID of the Support Ticket.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetTicketReplies200Response result = apiInstance.getTicketReplies(ticketId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#getTicketReplies");
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
| **ticketId** | **Integer**| The ID of the Support Ticket. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetTicketReplies200Response**](GetTicketReplies200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of SupportTicketReply objects. |  -  |
| **0** | Error |  -  |

<a id="getTickets"></a>
# **getTickets**
> GetTickets200Response getTickets(page, pageSize)

Support Tickets List

Returns a collection of Support Tickets on your Account. Support Tickets can be both tickets you open with Linode for support, as well as tickets generated by Linode regarding your Account. This collection includes all Support Tickets generated on your Account, with open tickets returned first. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SupportApi apiInstance = new SupportApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetTickets200Response result = apiInstance.getTickets(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#getTickets");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetTickets200Response**](GetTickets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of SupportTicket objects. |  -  |
| **0** | Error |  -  |

