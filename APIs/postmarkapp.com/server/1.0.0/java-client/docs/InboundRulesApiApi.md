# InboundRulesApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInboundRule**](InboundRulesApiApi.md#createInboundRule) | **POST** /triggers/inboundrules | Create an inbound rule trigger |
| [**deleteInboundRule**](InboundRulesApiApi.md#deleteInboundRule) | **DELETE** /triggers/inboundrules/{triggerid} | Delete a single trigger |
| [**listInboundRules**](InboundRulesApiApi.md#listInboundRules) | **GET** /triggers/inboundrules | List inbound rule triggers |


<a id="createInboundRule"></a>
# **createInboundRule**
> CreateInboundRule200Response createInboundRule(xPostmarkServerToken, body)

Create an inbound rule trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundRulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    InboundRulesApiApi apiInstance = new InboundRulesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    CreateInboundRuleRequest body = new CreateInboundRuleRequest(); // CreateInboundRuleRequest | 
    try {
      CreateInboundRule200Response result = apiInstance.createInboundRule(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundRulesApiApi#createInboundRule");
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
| **body** | [**CreateInboundRuleRequest**](CreateInboundRuleRequest.md)|  | [optional] |

### Return type

[**CreateInboundRule200Response**](CreateInboundRule200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="deleteInboundRule"></a>
# **deleteInboundRule**
> StandardPostmarkResponse deleteInboundRule(xPostmarkServerToken, triggerid)

Delete a single trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundRulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    InboundRulesApiApi apiInstance = new InboundRulesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer triggerid = 56; // Integer | The ID of the Inbound Rule that should be deleted.
    try {
      StandardPostmarkResponse result = apiInstance.deleteInboundRule(xPostmarkServerToken, triggerid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundRulesApiApi#deleteInboundRule");
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
| **triggerid** | **Integer**| The ID of the Inbound Rule that should be deleted. | |

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

<a id="listInboundRules"></a>
# **listInboundRules**
> ListInboundRules200Response listInboundRules(xPostmarkServerToken, count, offset)

List inbound rule triggers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundRulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    InboundRulesApiApi apiInstance = new InboundRulesApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    Integer count = 56; // Integer | Number of records to return per request.
    Integer offset = 56; // Integer | Number of records to skip.
    try {
      ListInboundRules200Response result = apiInstance.listInboundRules(xPostmarkServerToken, count, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundRulesApiApi#listInboundRules");
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
| **count** | **Integer**| Number of records to return per request. | |
| **offset** | **Integer**| Number of records to skip. | |

### Return type

[**ListInboundRules200Response**](ListInboundRules200Response.md)

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

