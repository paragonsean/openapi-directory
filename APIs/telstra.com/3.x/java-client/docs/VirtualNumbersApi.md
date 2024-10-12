# VirtualNumbersApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignNumber**](VirtualNumbersApi.md#assignNumber) | **POST** /virtual-numbers | assign a virtual number |
| [**deleteNumber**](VirtualNumbersApi.md#deleteNumber) | **DELETE** /virtual-numbers/{virtual-number} | delete a virtual number |
| [**getNumbers**](VirtualNumbersApi.md#getNumbers) | **GET** /virtual-numbers | fetch all virtual numbers |
| [**getRecipientOptouts**](VirtualNumbersApi.md#getRecipientOptouts) | **GET** /virtual-numbers/{virtual-number}/optouts | Get recipient optouts list |
| [**getVirtualNumber**](VirtualNumbersApi.md#getVirtualNumber) | **GET** /virtual-numbers/{virtual-number} | fetch a virtual number |
| [**updateNumber**](VirtualNumbersApi.md#updateNumber) | **PUT** /virtual-numbers/{virtual-number} | update a virtual number |


<a id="assignNumber"></a>
# **assignNumber**
> VirtualNumber assignNumber(contentLanguage, authorization, accept, acceptCharset, contentType, assignNumberRequest, telstraApiVersion)

assign a virtual number

When a recipient receives your message, you can choose whether they&#39;ll see a privateNumber, Virtual Number or senderName (paid plans only) in the **from** field. If you want to use a Virtual Number, use this endpoint to assign one. Free Trial users can assign one Virtual Number, and those on a paid plan can assign up to 100.   Virtual Numbers that have not sent a message in 30 days (Free Trial) or sent/received a message in 18 months (paid plans) will be automatically unassigned from your account. You can check the **lastUse** date of your Virtual Number at any time using GET /virtual-numbers/{virtual-number}.  Note that Virtual Numbers used in v2 of the Messaging API cannot be used to send messages in v3. Please assign a new Virtual Number instead. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNumbersApi apiInstance = new VirtualNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    AssignNumberRequest assignNumberRequest = new AssignNumberRequest(); // AssignNumberRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      VirtualNumber result = apiInstance.assignNumber(contentLanguage, authorization, accept, acceptCharset, contentType, assignNumberRequest, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNumbersApi#assignNumber");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **assignNumberRequest** | [**AssignNumberRequest**](AssignNumberRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**VirtualNumber**](VirtualNumber.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A 201 Created response means a Virtual Number has been assigned to your account. You can find this 10-digit number in the response body.  |  * Content-Language -  <br>  * Location -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | TAGS_ERR | Ensure you&#39;ve assigned no more than 10 tags, using up to 64 characters for each. | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). | | ACCOUNT_LIMIT_ERROR | Check the maximum number of Virtual Numbers that can be assigned to your account. |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is POST. |  |  * Content-Language -  <br>  |
| **413** | Payload Too Large  | code | suggested_action | | :--- | :--- | | PAYLOAD_TOO_LARGE | Reduce body payload size |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="deleteNumber"></a>
# **deleteNumber**
> deleteNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, telstraApiVersion)

delete a virtual number

Use **virtual-number** to remove a Virtual Number that&#39;s been assigned to your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNumbersApi apiInstance = new VirtualNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      apiInstance.deleteNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, telstraApiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNumbersApi#deleteNumber");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | A 204 response means the Virtual Number has been successfully removed from your account.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_INVALID | Check the number is a valid Virtual Number. | | VIRTUAL_NUM_UNASSIGNED | Check the number is assigned to your account. | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_LENGTH_ERR | Check the field is within character limits. |  | FIELD_MISSING | Please supply all required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access Token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_UNKNOWN | Check the number is a valid Virtual Number. | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is DELETE. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getNumbers"></a>
# **getNumbers**
> GetNumbers200Response getNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion, limit, offset, filter)

fetch all virtual numbers

Use this endpoint to fetch all Virtual Numbers currently assigned to your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNumbersApi apiInstance = new VirtualNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String telstraApiVersion = "3.1.0"; // String | 
    Integer limit = 10; // Integer | Tell us how many results you want us to return, up to a maximum of 50. 
    Integer offset = 0; // Integer | Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on. 
    String filter = "filter_example"; // String | Filter your Virtual Numbers by tag or by number.
    try {
      GetNumbers200Response result = apiInstance.getNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion, limit, offset, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNumbersApi#getNumbers");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **telstraApiVersion** | **String**|  | [optional] |
| **limit** | **Integer**| Tell us how many results you want us to return, up to a maximum of 50.  | [optional] [default to 10] |
| **offset** | **Integer**| Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on.  | [optional] [default to 0] |
| **filter** | **String**| Filter your Virtual Numbers by tag or by number. | [optional] |

### Return type

[**GetNumbers200Response**](GetNumbers200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means your request has been successful. Your Virtual Number(s) will be returned in the response body.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getRecipientOptouts"></a>
# **getRecipientOptouts**
> GetRecipientOptouts200Response getRecipientOptouts(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, telstraApiVersion, limit, offset)

Get recipient optouts list

Use this endpoint to fetch any mobile number(s) that have opted out of receiving messages from a Virtual Number assigned to your account.  Recipients can opt out at any time by sending a message with industry standard keywords such as STOP, STOPALL, UNSUBSCRIBE, QUIT, END and CANCEL. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNumbersApi apiInstance = new VirtualNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
    String telstraApiVersion = "3.1.0"; // String | 
    Integer limit = 10; // Integer | Tell us how many results you want us to return, up to a maximum of 50. 
    Integer offset = 0; // Integer | Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on. 
    try {
      GetRecipientOptouts200Response result = apiInstance.getRecipientOptouts(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, telstraApiVersion, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNumbersApi#getRecipientOptouts");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | |
| **telstraApiVersion** | **String**|  | [optional] |
| **limit** | **Integer**| Tell us how many results you want us to return, up to a maximum of 50.  | [optional] [default to 10] |
| **offset** | **Integer**| Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on.  | [optional] [default to 0] |

### Return type

[**GetRecipientOptouts200Response**](GetRecipientOptouts200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_INVALID | Check the number is a valid Virtual Number. | | VIRTUAL_NUM_UNASSIGNED | Check the number is assigned to your account. | | FIELD_INVALID | Ensure the number is a 10-digit Australian mobile number in national format (e.g. 0412345678). | | FIELD_LENGTH_ERR | Ensure the number is 10 digits only (e.g. 0412345678). | | FIELD_MISSING | Please supply the number. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_UNKNOWN | Check the number is a valid Virtual Number. | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getVirtualNumber"></a>
# **getVirtualNumber**
> VirtualNumber getVirtualNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, telstraApiVersion)

fetch a virtual number

Fetch the tags, replyCallbackUrl and lastUse date for a Virtual Number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNumbersApi apiInstance = new VirtualNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      VirtualNumber result = apiInstance.getVirtualNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNumbersApi#getVirtualNumber");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**VirtualNumber**](VirtualNumber.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means your request has been successful.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_INVALID | Check the number is a valid Virtual Number. | | VIRTUAL_NUM_UNASSIGNED | Check the number is assigned to your account. | | FIELD_INVALID | Ensure the number is a 10-digit Australian mobile number in national format (e.g. 0412345678). | | FIELD_LENGTH_ERR | Ensure the number is 10 digits only (e.g. 0412345678). |  | FIELD_MISSING | Please supply the number. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_UNKNOWN | Check the number is a valid Virtual Number. | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="updateNumber"></a>
# **updateNumber**
> VirtualNumber updateNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, updateNumberRequest, telstraApiVersion)

update a virtual number

Use **virtual-number** to update the tags and/or replyCallbackUrl of a Virtual Number.  This request body will override the original POST/ virtual-numbers call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNumbersApi apiInstance = new VirtualNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
    UpdateNumberRequest updateNumberRequest = new UpdateNumberRequest(); // UpdateNumberRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      VirtualNumber result = apiInstance.updateNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, updateNumberRequest, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNumbersApi#updateNumber");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | |
| **updateNumberRequest** | [**UpdateNumberRequest**](UpdateNumberRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**VirtualNumber**](VirtualNumber.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means metadata for the Virtual Number has been successfully updated.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | TAGS_ERR | Ensure you&#39;ve assigned no more than 10 tags, using up to 64 characters for each. | | VIRTUAL_NUM_INVALID | Check the number is a valid Virtual Number. | | VIRTUAL_NUM_UNASSIGNED | Check the number is assigned to your account. | | FIELD_LENGTH_ERR | Check the field is within character limits. |  | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Please supply all required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access Token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | VIRTUAL_NUM_UNKNOWN | Check the number is a valid Virtual Number. | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is PUT. |  |  * Content-Language -  <br>  |
| **413** | Payload Too Large  | code | suggested_action | | :--- | :--- | | PAYLOAD_TOO_LARGE | Reduce body payload size |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

