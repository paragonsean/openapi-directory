# Api20100401ConnectAppApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteConnectApp**](Api20100401ConnectAppApi.md#deleteConnectApp) | **DELETE** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json |  |
| [**fetchConnectApp**](Api20100401ConnectAppApi.md#fetchConnectApp) | **GET** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json |  |
| [**listConnectApp**](Api20100401ConnectAppApi.md#listConnectApp) | **GET** /2010-04-01/Accounts/{AccountSid}/ConnectApps.json |  |
| [**updateConnectApp**](Api20100401ConnectAppApi.md#updateConnectApp) | **POST** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json |  |


<a id="deleteConnectApp"></a>
# **deleteConnectApp**
> deleteConnectApp(accountSid, sid)



Delete an instance of a connect-app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ConnectAppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ConnectAppApi apiInstance = new Api20100401ConnectAppApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
    try {
      apiInstance.deleteConnectApp(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ConnectAppApi#deleteConnectApp");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch. | |

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

<a id="fetchConnectApp"></a>
# **fetchConnectApp**
> ApiV2010AccountConnectApp fetchConnectApp(accountSid, sid)



Fetch an instance of a connect-app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ConnectAppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ConnectAppApi apiInstance = new Api20100401ConnectAppApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
    try {
      ApiV2010AccountConnectApp result = apiInstance.fetchConnectApp(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ConnectAppApi#fetchConnectApp");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch. | |

### Return type

[**ApiV2010AccountConnectApp**](ApiV2010AccountConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConnectApp"></a>
# **listConnectApp**
> ListConnectAppResponse listConnectApp(accountSid, pageSize, page, pageToken)



Retrieve a list of connect-apps belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ConnectAppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ConnectAppApi apiInstance = new Api20100401ConnectAppApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConnectAppResponse result = apiInstance.listConnectApp(accountSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ConnectAppApi#listConnectApp");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConnectAppResponse**](ListConnectAppResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConnectApp"></a>
# **updateConnectApp**
> ApiV2010AccountConnectApp updateConnectApp(accountSid, sid, authorizeRedirectUrl, companyName, deauthorizeCallbackMethod, deauthorizeCallbackUrl, description, friendlyName, homepageUrl, permissions)



Update a connect-app with the specified parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ConnectAppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ConnectAppApi apiInstance = new Api20100401ConnectAppApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
    URI authorizeRedirectUrl = new URI(); // URI | The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App.
    String companyName = "companyName_example"; // String | The company name to set for the Connect App.
    String deauthorizeCallbackMethod = "HEAD"; // String | The HTTP method to use when calling `deauthorize_callback_url`.
    URI deauthorizeCallbackUrl = new URI(); // URI | The URL to call using the `deauthorize_callback_method` to de-authorize the Connect App.
    String description = "description_example"; // String | A description of the Connect App.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    URI homepageUrl = new URI(); // URI | A public URL where users can obtain more information about this Connect App.
    List<ConnectAppEnumPermission> permissions = Arrays.asList(); // List<ConnectAppEnumPermission> | A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: `get-all` and `post-all`.
    try {
      ApiV2010AccountConnectApp result = apiInstance.updateConnectApp(accountSid, sid, authorizeRedirectUrl, companyName, deauthorizeCallbackMethod, deauthorizeCallbackUrl, description, friendlyName, homepageUrl, permissions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ConnectAppApi#updateConnectApp");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ConnectApp resource to update. | |
| **authorizeRedirectUrl** | **URI**| The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App. | [optional] |
| **companyName** | **String**| The company name to set for the Connect App. | [optional] |
| **deauthorizeCallbackMethod** | **String**| The HTTP method to use when calling &#x60;deauthorize_callback_url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **deauthorizeCallbackUrl** | **URI**| The URL to call using the &#x60;deauthorize_callback_method&#x60; to de-authorize the Connect App. | [optional] |
| **description** | **String**| A description of the Connect App. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **homepageUrl** | **URI**| A public URL where users can obtain more information about this Connect App. | [optional] |
| **permissions** | [**List&lt;ConnectAppEnumPermission&gt;**](ConnectAppEnumPermission.md)| A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: &#x60;get-all&#x60; and &#x60;post-all&#x60;. | [optional] |

### Return type

[**ApiV2010AccountConnectApp**](ApiV2010AccountConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

