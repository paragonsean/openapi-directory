# BlockedNumbersApi

All URIs are relative to *https://api.bulksms.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blockedNumbersGet**](BlockedNumbersApi.md#blockedNumbersGet) | **GET** /blocked-numbers | List blocked numbers |
| [**blockedNumbersPost**](BlockedNumbersApi.md#blockedNumbersPost) | **POST** /blocked-numbers | Create a blocked number |


<a id="blockedNumbersGet"></a>
# **blockedNumbersGet**
> BlockedNumber blockedNumbersGet(minId, limit)

List blocked numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockedNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bulksms.com/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    BlockedNumbersApi apiInstance = new BlockedNumbersApi(defaultClient);
    Integer minId = 56; // Integer | Records with an `id` that is greater or equal to min-id will be returned. The default value is `0`.  You can add 1 to an id that you previously retrieved, to return subsequent records.
    Integer limit = 56; // Integer | The maximum number of records to return. The default value is `10000`. The value cannot be greater than 10000.
    try {
      BlockedNumber result = apiInstance.blockedNumbersGet(minId, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockedNumbersApi#blockedNumbersGet");
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
| **minId** | **Integer**| Records with an &#x60;id&#x60; that is greater or equal to min-id will be returned. The default value is &#x60;0&#x60;.  You can add 1 to an id that you previously retrieved, to return subsequent records. | [optional] |
| **limit** | **Integer**| The maximum number of records to return. The default value is &#x60;10000&#x60;. The value cannot be greater than 10000. | [optional] |

### Return type

[**BlockedNumber**](BlockedNumber.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of BlockedNumber objects |  -  |

<a id="blockedNumbersPost"></a>
# **blockedNumbersPost**
> blockedNumbersPost(requestBody)

Create a blocked number

Blocked numbers are phone numbers to which your account is not permitted to send messages. The numbers can be created via this API, by a recipient replying with a STOP message to one of your previous SENT messages, or by a BulkSMS administrator.  Sending a message to a blocked number will result in the message being assigned a status of &#x60;FAILED.BLOCKED&#x60;. Messages sent to blocked numbers are billed to your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockedNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bulksms.com/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    BlockedNumbersApi apiInstance = new BlockedNumbersApi(defaultClient);
    List<String> requestBody = Arrays.asList(); // List<String> | Maximum size: `1000` items
    try {
      apiInstance.blockedNumbersPost(requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockedNumbersApi#blockedNumbersPost");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)| Maximum size: &#x60;1000&#x60; items | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty body upon success |  -  |

