# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTicket**](V1Api.md#createTicket) | **POST** /v1/abuse/tickets | Create a new abuse ticket |
| [**getTicketInfo**](V1Api.md#getTicketInfo) | **GET** /v1/abuse/tickets/{ticketId} | Return the abuse ticket data for a given ticket id |
| [**getTickets**](V1Api.md#getTickets) | **GET** /v1/abuse/tickets | List all abuse tickets ids that match user provided filters |


<a id="createTicket"></a>
# **createTicket**
> createTicket(abuseTicketCreate)

Create a new abuse ticket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    AbuseTicketCreate abuseTicketCreate = new AbuseTicketCreate(); // AbuseTicketCreate | The endpoint which allows the Reporter to create a new abuse ticket
    try {
      apiInstance.createTicket(abuseTicketCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#createTicket");
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
| **abuseTicketCreate** | [**AbuseTicketCreate**](AbuseTicketCreate.md)| The endpoint which allows the Reporter to create a new abuse ticket | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Success |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | Error |  -  |

<a id="getTicketInfo"></a>
# **getTicketInfo**
> AbuseTicket getTicketInfo(ticketId)

Return the abuse ticket data for a given ticket id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String ticketId = "ticketId_example"; // String | A unique abuse ticket identifier
    try {
      AbuseTicket result = apiInstance.getTicketInfo(ticketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#getTicketInfo");
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
| **ticketId** | **String**| A unique abuse ticket identifier | |

### Return type

[**AbuseTicket**](AbuseTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Invalid ticket id provided |  -  |

<a id="getTickets"></a>
# **getTickets**
> AbuseTicketList getTickets(type, closed, sourceDomainOrIp, target, createdStart, createdEnd, limit, offset)

List all abuse tickets ids that match user provided filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String type = "A_RECORD"; // String | The type of abuse.
    Boolean closed = false; // Boolean | Is this abuse ticket closed?
    String sourceDomainOrIp = "sourceDomainOrIp_example"; // String | The domain name or ip address the abuse originated from
    String target = "target_example"; // String | The brand/company the abuse is targeting. ie: brand name/bank name
    String createdStart = "createdStart_example"; // String | The earliest abuse ticket creation date to pull abuse tickets for
    String createdEnd = "createdEnd_example"; // String | The latest abuse ticket creation date to pull abuse tickets for
    Integer limit = 100; // Integer | Number of abuse ticket numbers to return.
    Integer offset = 0; // Integer | The earliest result set record number to pull abuse tickets for
    try {
      AbuseTicketList result = apiInstance.getTickets(type, closed, sourceDomainOrIp, target, createdStart, createdEnd, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#getTickets");
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
| **type** | **String**| The type of abuse. | [optional] [enum: A_RECORD, CHILD_ABUSE, CONTENT, FRAUD_WIRE, IP_BLOCK, MALWARE, NETWORK_ABUSE, PHISHING, SPAM] |
| **closed** | **Boolean**| Is this abuse ticket closed? | [optional] [default to false] |
| **sourceDomainOrIp** | **String**| The domain name or ip address the abuse originated from | [optional] |
| **target** | **String**| The brand/company the abuse is targeting. ie: brand name/bank name | [optional] |
| **createdStart** | **String**| The earliest abuse ticket creation date to pull abuse tickets for | [optional] |
| **createdEnd** | **String**| The latest abuse ticket creation date to pull abuse tickets for | [optional] |
| **limit** | **Integer**| Number of abuse ticket numbers to return. | [optional] [default to 100] |
| **offset** | **Integer**| The earliest result set record number to pull abuse tickets for | [optional] [default to 0] |

### Return type

[**AbuseTicketList**](AbuseTicketList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | Error |  -  |

