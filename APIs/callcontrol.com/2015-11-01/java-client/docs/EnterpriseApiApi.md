# EnterpriseApiApi

All URIs are relative to *https://api.callcontrol.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enterpriseApiGetUser**](EnterpriseApiApi.md#enterpriseApiGetUser) | **GET** /api/2015-11-01/Enterprise/GetUser/{phoneNumber} | Enterprise  GET: GetUser  Returns the current information from the user;  try 12066194123 as demo |
| [**enterpriseApiShouldBlock**](EnterpriseApiApi.md#enterpriseApiShouldBlock) | **GET** /api/2015-11-01/Enterprise/ShouldBlock/{phoneNumber}/{userPhoneNumber} | Enterprise  GET: ShouldBlock  Simple Enteprise which returns a call block proceed decision. |
| [**enterpriseApiUpsertUser**](EnterpriseApiApi.md#enterpriseApiUpsertUser) | **POST** /api/2015-11-01/Enterprise/UpsertUser | UpsertUser: insert or update all properties from a user  PhoneNumber  WhiteList (list of phone numbers to whitelist)  BlackList (list of phone numbers to blacklist)  QuietHourList (list of quiet hour objects)  UseCommunityBlacklist (enable / disable community blacklist) default true  BreakThroughQhWithMultipleCalls (break through quiet hours with two calls in 3 minutes)  WhiteListBreaksQh (break through quiet hours for whitelist) |


<a id="enterpriseApiGetUser"></a>
# **enterpriseApiGetUser**
> CallControlUser enterpriseApiGetUser(phoneNumber)

Enterprise  GET: GetUser  Returns the current information from the user;  try 12066194123 as demo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callcontrol.com");

    EnterpriseApiApi apiInstance = new EnterpriseApiApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | 
    try {
      CallControlUser result = apiInstance.enterpriseApiGetUser(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseApiApi#enterpriseApiGetUser");
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
| **phoneNumber** | **String**|  | |

### Return type

[**CallControlUser**](CallControlUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Object |  -  |
| **400** | Bad request (invalid phone number) |  -  |

<a id="enterpriseApiShouldBlock"></a>
# **enterpriseApiShouldBlock**
> String enterpriseApiShouldBlock(phoneNumber, userPhoneNumber)

Enterprise  GET: ShouldBlock  Simple Enteprise which returns a call block proceed decision.

This returns information required to perform basic call blocking behaviors              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callcontrol.com");

    EnterpriseApiApi apiInstance = new EnterpriseApiApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | phone number to search
    String userPhoneNumber = "userPhoneNumber_example"; // String | (OPTIONAL) phone number of user to look up block rules
    try {
      String result = apiInstance.enterpriseApiShouldBlock(phoneNumber, userPhoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseApiApi#enterpriseApiShouldBlock");
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
| **phoneNumber** | **String**| phone number to search | |
| **userPhoneNumber** | **String**| (OPTIONAL) phone number of user to look up block rules | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | true(block) false (no block) |  -  |
| **400** | Bad request (invalid phone number) |  -  |

<a id="enterpriseApiUpsertUser"></a>
# **enterpriseApiUpsertUser**
> Object enterpriseApiUpsertUser(user)

UpsertUser: insert or update all properties from a user  PhoneNumber  WhiteList (list of phone numbers to whitelist)  BlackList (list of phone numbers to blacklist)  QuietHourList (list of quiet hour objects)  UseCommunityBlacklist (enable / disable community blacklist) default true  BreakThroughQhWithMultipleCalls (break through quiet hours with two calls in 3 minutes)  WhiteListBreaksQh (break through quiet hours for whitelist)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callcontrol.com");

    EnterpriseApiApi apiInstance = new EnterpriseApiApi(defaultClient);
    CallControlUser user = new CallControlUser(); // CallControlUser | [FromBody] User               <remarks>This returns information required to perform basic call blocking behaviors.  The demo key will return ok, but will not save the data.<br /></remarks>
    try {
      Object result = apiInstance.enterpriseApiUpsertUser(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseApiApi#enterpriseApiUpsertUser");
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
| **user** | [**CallControlUser**](CallControlUser.md)| [FromBody] User               &lt;remarks&gt;This returns information required to perform basic call blocking behaviors.  The demo key will return ok, but will not save the data.&lt;br /&gt;&lt;/remarks&gt; | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **400** | Bad request (eg. invalid phone nubmer) |  -  |

