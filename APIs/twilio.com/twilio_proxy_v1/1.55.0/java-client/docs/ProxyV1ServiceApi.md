# ProxyV1ServiceApi

All URIs are relative to *https://proxy.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](ProxyV1ServiceApi.md#createService) | **POST** /v1/Services |  |
| [**deleteService**](ProxyV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} |  |
| [**fetchService**](ProxyV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} |  |
| [**listService**](ProxyV1ServiceApi.md#listService) | **GET** /v1/Services |  |
| [**updateService**](ProxyV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> ProxyV1Service createService(uniqueName, callbackUrl, chatInstanceSid, defaultTtl, geoMatchLevel, interceptCallbackUrl, numberSelectionBehavior, outOfSessionCallbackUrl)



Create a new Service for Twilio Proxy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ServiceApi apiInstance = new ProxyV1ServiceApi(defaultClient);
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
    URI callbackUrl = new URI(); // URI | The URL we should call when the interaction status changes.
    String chatInstanceSid = "chatInstanceSid_example"; // String | The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
    Integer defaultTtl = 56; // Integer | The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
    ServiceEnumGeoMatchLevel geoMatchLevel = ServiceEnumGeoMatchLevel.fromValue("area-code"); // ServiceEnumGeoMatchLevel | 
    URI interceptCallbackUrl = new URI(); // URI | The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
    ServiceEnumNumberSelectionBehavior numberSelectionBehavior = ServiceEnumNumberSelectionBehavior.fromValue("avoid-sticky"); // ServiceEnumNumberSelectionBehavior | 
    URI outOfSessionCallbackUrl = new URI(); // URI | The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
    try {
      ProxyV1Service result = apiInstance.createService(uniqueName, callbackUrl, chatInstanceSid, defaultTtl, geoMatchLevel, interceptCallbackUrl, numberSelectionBehavior, outOfSessionCallbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ServiceApi#createService");
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
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.** | |
| **callbackUrl** | **URI**| The URL we should call when the interaction status changes. | [optional] |
| **chatInstanceSid** | **String**| The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship. | [optional] |
| **defaultTtl** | **Integer**| The default &#x60;ttl&#x60; value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value. | [optional] |
| **geoMatchLevel** | **ServiceEnumGeoMatchLevel**|  | [optional] [enum: area-code, overlay, radius, country] |
| **interceptCallbackUrl** | **URI**| The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues. | [optional] |
| **numberSelectionBehavior** | **ServiceEnumNumberSelectionBehavior**|  | [optional] [enum: avoid-sticky, prefer-sticky] |
| **outOfSessionCallbackUrl** | **URI**| The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information. | [optional] |

### Return type

[**ProxyV1Service**](ProxyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)



Delete a specific Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ServiceApi apiInstance = new ProxyV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ServiceApi#deleteService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchService"></a>
# **fetchService**
> ProxyV1Service fetchService(sid)



Fetch a specific Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ServiceApi apiInstance = new ProxyV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to fetch.
    try {
      ProxyV1Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ServiceApi#fetchService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to fetch. | |

### Return type

[**ProxyV1Service**](ProxyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)



Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ServiceApi apiInstance = new ProxyV1ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ServiceApi#listService");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> ProxyV1Service updateService(sid, callbackUrl, chatInstanceSid, defaultTtl, geoMatchLevel, interceptCallbackUrl, numberSelectionBehavior, outOfSessionCallbackUrl, uniqueName)



Update a specific Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ServiceApi apiInstance = new ProxyV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
    URI callbackUrl = new URI(); // URI | The URL we should call when the interaction status changes.
    String chatInstanceSid = "chatInstanceSid_example"; // String | The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
    Integer defaultTtl = 56; // Integer | The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
    ServiceEnumGeoMatchLevel geoMatchLevel = ServiceEnumGeoMatchLevel.fromValue("area-code"); // ServiceEnumGeoMatchLevel | 
    URI interceptCallbackUrl = new URI(); // URI | The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
    ServiceEnumNumberSelectionBehavior numberSelectionBehavior = ServiceEnumNumberSelectionBehavior.fromValue("avoid-sticky"); // ServiceEnumNumberSelectionBehavior | 
    URI outOfSessionCallbackUrl = new URI(); // URI | The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
    try {
      ProxyV1Service result = apiInstance.updateService(sid, callbackUrl, chatInstanceSid, defaultTtl, geoMatchLevel, interceptCallbackUrl, numberSelectionBehavior, outOfSessionCallbackUrl, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ServiceApi#updateService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | |
| **callbackUrl** | **URI**| The URL we should call when the interaction status changes. | [optional] |
| **chatInstanceSid** | **String**| The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship. | [optional] |
| **defaultTtl** | **Integer**| The default &#x60;ttl&#x60; value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value. | [optional] |
| **geoMatchLevel** | **ServiceEnumGeoMatchLevel**|  | [optional] [enum: area-code, overlay, radius, country] |
| **interceptCallbackUrl** | **URI**| The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues. | [optional] |
| **numberSelectionBehavior** | **ServiceEnumNumberSelectionBehavior**|  | [optional] [enum: avoid-sticky, prefer-sticky] |
| **outOfSessionCallbackUrl** | **URI**| The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.** | [optional] |

### Return type

[**ProxyV1Service**](ProxyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

