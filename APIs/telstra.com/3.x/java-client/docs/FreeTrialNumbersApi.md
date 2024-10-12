# FreeTrialNumbersApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrialNumbers**](FreeTrialNumbersApi.md#createTrialNumbers) | **POST** /free-trial-numbers | create free trial number list |
| [**getTrialNumbers**](FreeTrialNumbersApi.md#getTrialNumbers) | **GET** /free-trial-numbers | get all free trial numbers |


<a id="createTrialNumbers"></a>
# **createTrialNumbers**
> FreeTrialNumbers createTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, createTrialNumbersRequest, telstraApiVersion)

create free trial number list

Your Free Trial Numbers are the 10 recipient mobile numbers that you can message during the Free Trial. The first five numbers you send an SMS/MMS to will automatically be added to your Free Trial Numbers list. After that, you can use this endpoint to register another five. Alternatively, you can use this endpoint to register all 10 numbers.    Use this endpoint to register a Free Trial Number to your account. To test out all the features that the trial has to offer, we recommend registering your own mobile number to your Free Trial Numbers list.   Note that you can only message mobile numbers that have been added to your Free Trial list and once registered, a Free Trial Number cannot be removed or replaced. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FreeTrialNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    FreeTrialNumbersApi apiInstance = new FreeTrialNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    CreateTrialNumbersRequest createTrialNumbersRequest = new CreateTrialNumbersRequest(); // CreateTrialNumbersRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      FreeTrialNumbers result = apiInstance.createTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, createTrialNumbersRequest, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FreeTrialNumbersApi#createTrialNumbers");
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
| **createTrialNumbersRequest** | [**CreateTrialNumbersRequest**](CreateTrialNumbersRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**FreeTrialNumbers**](FreeTrialNumbers.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A 201 OK response means your request has been successful. Your registered Free Trial Number(s) will be returned in the response.  |  * Content-Language -  <br>  * Location -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_LENGTH_ERR | Check the field is within character limits. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | FREE_TRIAL_INTERNATIONAL_ERR | Move to a paid plan to send a message to an international destination. |  | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). | | ACCOUNT_LIMIT_ERROR | You&#39;ve reached the maximum quota of Free Trial Numbers that can be registered to your account. Upgrade to a paid plan to send a message to this recipient.   |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | FREE_TRIAL_ERR | This call is only applicable to Free Trial users. Check if the call is required. | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is POST. |  |  * Content-Language -  <br>  |
| **413** | Payload Too Large  | code | suggested_action | | :--- | :--- | | PAYLOAD_TOO_LARGE | Reduce body payload size |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getTrialNumbers"></a>
# **getTrialNumbers**
> FreeTrialNumbers getTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion)

get all free trial numbers

Use this endpoint to fetch the Free Trial Number(s) currently assigned to your account. These are the mobile numbers that you can message during the Free Trial.  If you&#39;re using a paid plan, there&#39;s no limit to the number of recipients that you can message, so you don&#39;t need to register Free Trial Numbers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FreeTrialNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    FreeTrialNumbersApi apiInstance = new FreeTrialNumbersApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      FreeTrialNumbers result = apiInstance.getTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FreeTrialNumbersApi#getTrialNumbers");
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

### Return type

[**FreeTrialNumbers**](FreeTrialNumbers.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means your request has been successful. Your Free Trial Number(s) will be returned in the response body.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_LENGTH_ERR | Check the field is within character limits. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | FREE_TRIAL_ERR | This call is only applicable to Free Trial users. Check if the call is required. | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

