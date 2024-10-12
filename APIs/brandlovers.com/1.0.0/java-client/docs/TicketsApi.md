# TicketsApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ticketPost**](TicketsApi.md#ticketPost) | **POST** /ticket | Creates a new trouble ticket |
| [**ticketTicketIdMessagePost**](TicketsApi.md#ticketTicketIdMessagePost) | **POST** /ticket/{ticketId}/message | Add new message to trouble ticket |
| [**ticketTicketIdMessagesGet**](TicketsApi.md#ticketTicketIdMessagesGet) | **GET** /ticket/{ticketId}/messages | Get trouble ticket messages |
| [**ticketTicketIdStatusPut**](TicketsApi.md#ticketTicketIdStatusPut) | **PUT** /ticket/{ticketId}/status | Update trouble ticket status |
| [**ticketsGet**](TicketsApi.md#ticketsGet) | **GET** /tickets | Get customers trouble tickets |


<a id="ticketPost"></a>
# **ticketPost**
> ticketPost(authorization, newTicket)

Creates a new trouble ticket

Use this service to create a new trouble ticket. Use this to include relevant information about the order, comunicate with the customer or marketplace team. Whenever possible message will be pushed to Mobile first. This is the primary mean of comunicaiton with the customer regarding orders, shippments, shippments status. New tickets will be automatically be set to &#39;OPEN&#39;. Trouble tickets need to be associated with a orderId or customer. New tickets can optionally include a new message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    NewTicket newTicket = new NewTicket(); // NewTicket | JSON object with new trouble ticket
    try {
      apiInstance.ticketPost(authorization, newTicket);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketPost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **newTicket** | [**NewTicket**](NewTicket.md)| JSON object with new trouble ticket | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |

<a id="ticketTicketIdMessagePost"></a>
# **ticketTicketIdMessagePost**
> ticketTicketIdMessagePost(authorization, ticketId, message)

Add new message to trouble ticket

Add a new message to this trouble ticket. Messages can be &#x60;CUSTOMER&#x60; (customer will be able to see it) or &#x60;INTERNAL&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String ticketId = "ticketId_example"; // String | Trouble ticket ID.
    NewTicketMessage message = new NewTicketMessage(); // NewTicketMessage | New message object to append to trouble ticket.
    try {
      apiInstance.ticketTicketIdMessagePost(authorization, ticketId, message);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketTicketIdMessagePost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **ticketId** | **String**| Trouble ticket ID. | |
| **message** | [**NewTicketMessage**](NewTicketMessage.md)| New message object to append to trouble ticket. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **404** | Object not found. |  -  |

<a id="ticketTicketIdMessagesGet"></a>
# **ticketTicketIdMessagesGet**
> GetTicketMessages ticketTicketIdMessagesGet(authorization, ticketId, offset, limit)

Get trouble ticket messages

Returns trouble ticket history with all messages exchanged. Only tickets related to your seller will be returned. Attempt to read other tickets will return 403 (acess denied).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String ticketId = "ticketId_example"; // String | Trouble ticket ID.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetTicketMessages result = apiInstance.ticketTicketIdMessagesGet(authorization, ticketId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketTicketIdMessagesGet");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **ticketId** | **String**| Trouble ticket ID. | |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetTicketMessages**](GetTicketMessages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Access denied. You can only access your trouble tickets |  -  |

<a id="ticketTicketIdStatusPut"></a>
# **ticketTicketIdStatusPut**
> ticketTicketIdStatusPut(authorization, ticketId, body)

Update trouble ticket status

Alows the seller to update the status of a trouble ticket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String ticketId = "ticketId_example"; // String | Trouble ticket unique identification
    TicketStatus body = new TicketStatus(); // TicketStatus | New trouble ticket status
    try {
      apiInstance.ticketTicketIdStatusPut(authorization, ticketId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketTicketIdStatusPut");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **ticketId** | **String**| Trouble ticket unique identification | |
| **body** | [**TicketStatus**](TicketStatus.md)| New trouble ticket status | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successfully received transaction |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |
| **404** | Object not found. |  -  |

<a id="ticketsGet"></a>
# **ticketsGet**
> GetTickets ticketsGet(authorization, status, offset, limit)

Get customers trouble tickets

Allows seller to receive and status, queries, requests and complaints from customers. As well related messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String status = "OPEN"; // String | Query by trouble ticket status
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetTickets result = apiInstance.ticketsGet(authorization, status, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketsGet");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **status** | **String**| Query by trouble ticket status | [optional] [enum: OPEN, REOPENED, CLOSED] |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetTickets**](GetTickets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |

