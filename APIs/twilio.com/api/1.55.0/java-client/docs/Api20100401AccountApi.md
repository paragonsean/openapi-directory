# Api20100401AccountApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAccount**](Api20100401AccountApi.md#createAccount) | **POST** /2010-04-01/Accounts.json |  |
| [**fetchAccount**](Api20100401AccountApi.md#fetchAccount) | **GET** /2010-04-01/Accounts/{Sid}.json |  |
| [**listAccount**](Api20100401AccountApi.md#listAccount) | **GET** /2010-04-01/Accounts.json |  |
| [**updateAccount**](Api20100401AccountApi.md#updateAccount) | **POST** /2010-04-01/Accounts/{Sid}.json |  |


<a id="createAccount"></a>
# **createAccount**
> ApiV2010Account createAccount(friendlyName)



Create a new Twilio Subaccount from the account making the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AccountApi apiInstance = new Api20100401AccountApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A human readable description of the account to create, defaults to `SubAccount Created at {YYYY-MM-DD HH:MM meridian}`
    try {
      ApiV2010Account result = apiInstance.createAccount(friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AccountApi#createAccount");
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
| **friendlyName** | **String**| A human readable description of the account to create, defaults to &#x60;SubAccount Created at {YYYY-MM-DD HH:MM meridian}&#x60; | [optional] |

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchAccount"></a>
# **fetchAccount**
> ApiV2010Account fetchAccount(sid)



Fetch the account specified by the provided Account Sid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AccountApi apiInstance = new Api20100401AccountApi(defaultClient);
    String sid = "sid_example"; // String | The Account Sid that uniquely identifies the account to fetch
    try {
      ApiV2010Account result = apiInstance.fetchAccount(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AccountApi#fetchAccount");
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
| **sid** | **String**| The Account Sid that uniquely identifies the account to fetch | |

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAccount"></a>
# **listAccount**
> ListAccountResponse listAccount(friendlyName, status, pageSize, page, pageToken)



Retrieves a collection of Accounts belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AccountApi apiInstance = new Api20100401AccountApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | Only return the Account resources with friendly names that exactly match this name.
    AccountEnumStatus status = AccountEnumStatus.fromValue("active"); // AccountEnumStatus | Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAccountResponse result = apiInstance.listAccount(friendlyName, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AccountApi#listAccount");
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
| **friendlyName** | **String**| Only return the Account resources with friendly names that exactly match this name. | [optional] |
| **status** | **AccountEnumStatus**| Only return Account resources with the given status. Can be &#x60;closed&#x60;, &#x60;suspended&#x60; or &#x60;active&#x60;. | [optional] [enum: active, suspended, closed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListAccountResponse**](ListAccountResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAccount"></a>
# **updateAccount**
> ApiV2010Account updateAccount(sid, friendlyName, status)



Modify the properties of a given Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AccountApi apiInstance = new Api20100401AccountApi(defaultClient);
    String sid = "sid_example"; // String | The Account Sid that uniquely identifies the account to update
    String friendlyName = "friendlyName_example"; // String | Update the human-readable description of this Account
    AccountEnumStatus status = AccountEnumStatus.fromValue("active"); // AccountEnumStatus | 
    try {
      ApiV2010Account result = apiInstance.updateAccount(sid, friendlyName, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AccountApi#updateAccount");
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
| **sid** | **String**| The Account Sid that uniquely identifies the account to update | |
| **friendlyName** | **String**| Update the human-readable description of this Account | [optional] |
| **status** | **AccountEnumStatus**|  | [optional] [enum: active, suspended, closed] |

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

