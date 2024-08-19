# DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/reports*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCallLogs**](DefaultApi.md#getCallLogs) | **GET** /accounts/{account_id}/call-logs | Retrieve call logs for your account |


<a id="getCallLogs"></a>
# **getCallLogs**
> CallLogsHalResponse getCallLogs(accountId, startColonGte, startColonLte, pageSize, page, endColonGte, endColonLte, to, from, sourceUser, destinationUser, direction)

Retrieve call logs for your account

Retrieve call logs for your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/reports");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "913874"; // String | The Vonage Business Cloud account ID
    String startColonGte = "2019-01-01 00:00:00"; // String | Filter records by start date (greater equal or equal to)
    String startColonLte = "2019-01-01 00:00:00"; // String | Filter records by start date (less equal or equal to)
    BigDecimal pageSize = new BigDecimal("10"); // BigDecimal | Number of records per page
    BigDecimal page = new BigDecimal("0"); // BigDecimal | Current page number
    String endColonGte = "2019-01-01 00:00:00"; // String | Filter records by end date (greater equal or equal to)
    String endColonLte = "2019-01-01 00:00:00"; // String | Filter records by end date (less equal or equal to)
    String to = "17325550100"; // String | Filter by called number
    String from = "17325550100"; // String | Filter by source number
    String sourceUser = "sourceUser_example"; // String | Filter by source user
    String destinationUser = "destinationUser_example"; // String | Filter by destination user
    String direction = "Inbound"; // String | Filter by call direction.
    try {
      CallLogsHalResponse result = apiInstance.getCallLogs(accountId, startColonGte, startColonLte, pageSize, page, endColonGte, endColonLte, to, from, sourceUser, destinationUser, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCallLogs");
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
| **accountId** | **String**| The Vonage Business Cloud account ID | |
| **startColonGte** | **String**| Filter records by start date (greater equal or equal to) | |
| **startColonLte** | **String**| Filter records by start date (less equal or equal to) | |
| **pageSize** | **BigDecimal**| Number of records per page | [default to 10] |
| **page** | **BigDecimal**| Current page number | [default to 0] |
| **endColonGte** | **String**| Filter records by end date (greater equal or equal to) | [optional] |
| **endColonLte** | **String**| Filter records by end date (less equal or equal to) | [optional] |
| **to** | **String**| Filter by called number | [optional] |
| **from** | **String**| Filter by source number | [optional] |
| **sourceUser** | **String**| Filter by source user | [optional] |
| **destinationUser** | **String**| Filter by destination user | [optional] |
| **direction** | **String**| Filter by call direction. | [optional] [enum: Inbound, Outbound] |

### Return type

[**CallLogsHalResponse**](CallLogsHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid parameters given |  -  |

