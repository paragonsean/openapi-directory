# AccountsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adsensehostAccountsAdclientsGet**](AccountsApi.md#adsensehostAccountsAdclientsGet) | **GET** /accounts/{accountId}/adclients/{adClientId} |  |
| [**adsensehostAccountsAdclientsList**](AccountsApi.md#adsensehostAccountsAdclientsList) | **GET** /accounts/{accountId}/adclients |  |
| [**adsensehostAccountsAdunitsDelete**](AccountsApi.md#adsensehostAccountsAdunitsDelete) | **DELETE** /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId} |  |
| [**adsensehostAccountsAdunitsGet**](AccountsApi.md#adsensehostAccountsAdunitsGet) | **GET** /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId} |  |
| [**adsensehostAccountsAdunitsGetAdCode**](AccountsApi.md#adsensehostAccountsAdunitsGetAdCode) | **GET** /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}/adcode |  |
| [**adsensehostAccountsAdunitsInsert**](AccountsApi.md#adsensehostAccountsAdunitsInsert) | **POST** /accounts/{accountId}/adclients/{adClientId}/adunits |  |
| [**adsensehostAccountsAdunitsList**](AccountsApi.md#adsensehostAccountsAdunitsList) | **GET** /accounts/{accountId}/adclients/{adClientId}/adunits |  |
| [**adsensehostAccountsAdunitsPatch**](AccountsApi.md#adsensehostAccountsAdunitsPatch) | **PATCH** /accounts/{accountId}/adclients/{adClientId}/adunits |  |
| [**adsensehostAccountsAdunitsUpdate**](AccountsApi.md#adsensehostAccountsAdunitsUpdate) | **PUT** /accounts/{accountId}/adclients/{adClientId}/adunits |  |
| [**adsensehostAccountsGet**](AccountsApi.md#adsensehostAccountsGet) | **GET** /accounts/{accountId} |  |
| [**adsensehostAccountsList**](AccountsApi.md#adsensehostAccountsList) | **GET** /accounts |  |
| [**adsensehostAccountsReportsGenerate**](AccountsApi.md#adsensehostAccountsReportsGenerate) | **GET** /accounts/{accountId}/reports |  |


<a id="adsensehostAccountsAdclientsGet"></a>
# **adsensehostAccountsAdclientsGet**
> AdClient adsensehostAccountsAdclientsGet(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get information about one of the ad clients in the specified publisher&#39;s AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad client.
    String adClientId = "adClientId_example"; // String | Ad client to get.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AdClient result = apiInstance.adsensehostAccountsAdclientsGet(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdclientsGet");
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
| **accountId** | **String**| Account which contains the ad client. | |
| **adClientId** | **String**| Ad client to get. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AdClient**](AdClient.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdclientsList"></a>
# **adsensehostAccountsAdclientsList**
> AdClients adsensehostAccountsAdclientsList(accountId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken)



List all hosted ad clients in the specified hosted account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account for which to list ad clients.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | The maximum number of ad clients to include in the response, used for paging.
    String pageToken = "pageToken_example"; // String | A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response.
    try {
      AdClients result = apiInstance.adsensehostAccountsAdclientsList(accountId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdclientsList");
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
| **accountId** | **String**| Account for which to list ad clients. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| The maximum number of ad clients to include in the response, used for paging. | [optional] |
| **pageToken** | **String**| A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] |

### Return type

[**AdClients**](AdClients.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsDelete"></a>
# **adsensehostAccountsAdunitsDelete**
> AdUnit adsensehostAccountsAdunitsDelete(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Delete the specified ad unit from the specified publisher AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad unit.
    String adClientId = "adClientId_example"; // String | Ad client for which to get ad unit.
    String adUnitId = "adUnitId_example"; // String | Ad unit to delete.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AdUnit result = apiInstance.adsensehostAccountsAdunitsDelete(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsDelete");
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
| **accountId** | **String**| Account which contains the ad unit. | |
| **adClientId** | **String**| Ad client for which to get ad unit. | |
| **adUnitId** | **String**| Ad unit to delete. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsGet"></a>
# **adsensehostAccountsAdunitsGet**
> AdUnit adsensehostAccountsAdunitsGet(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get the specified host ad unit in this AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad unit.
    String adClientId = "adClientId_example"; // String | Ad client for which to get ad unit.
    String adUnitId = "adUnitId_example"; // String | Ad unit to get.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AdUnit result = apiInstance.adsensehostAccountsAdunitsGet(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsGet");
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
| **accountId** | **String**| Account which contains the ad unit. | |
| **adClientId** | **String**| Ad client for which to get ad unit. | |
| **adUnitId** | **String**| Ad unit to get. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsGetAdCode"></a>
# **adsensehostAccountsAdunitsGetAdCode**
> AdCode adsensehostAccountsAdunitsGetAdCode(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, hostCustomChannelId)



Get ad code for the specified ad unit, attaching the specified host custom channels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad client.
    String adClientId = "adClientId_example"; // String | Ad client with contains the ad unit.
    String adUnitId = "adUnitId_example"; // String | Ad unit to get the code for.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    List<String> hostCustomChannelId = Arrays.asList(); // List<String> | Host custom channel to attach to the ad code.
    try {
      AdCode result = apiInstance.adsensehostAccountsAdunitsGetAdCode(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, hostCustomChannelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsGetAdCode");
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
| **accountId** | **String**| Account which contains the ad client. | |
| **adClientId** | **String**| Ad client with contains the ad unit. | |
| **adUnitId** | **String**| Ad unit to get the code for. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **hostCustomChannelId** | [**List&lt;String&gt;**](String.md)| Host custom channel to attach to the ad code. | [optional] |

### Return type

[**AdCode**](AdCode.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsInsert"></a>
# **adsensehostAccountsAdunitsInsert**
> AdUnit adsensehostAccountsAdunitsInsert(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, adUnit)



Insert the supplied ad unit into the specified publisher AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which will contain the ad unit.
    String adClientId = "adClientId_example"; // String | Ad client into which to insert the ad unit.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AdUnit adUnit = new AdUnit(); // AdUnit | 
    try {
      AdUnit result = apiInstance.adsensehostAccountsAdunitsInsert(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, adUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsInsert");
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
| **accountId** | **String**| Account which will contain the ad unit. | |
| **adClientId** | **String**| Ad client into which to insert the ad unit. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **adUnit** | [**AdUnit**](AdUnit.md)|  | [optional] |

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsList"></a>
# **adsensehostAccountsAdunitsList**
> AdUnits adsensehostAccountsAdunitsList(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, includeInactive, maxResults, pageToken)



List all ad units in the specified publisher&#39;s AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad client.
    String adClientId = "adClientId_example"; // String | Ad client for which to list ad units.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean includeInactive = true; // Boolean | Whether to include inactive ad units. Default: true.
    Integer maxResults = 56; // Integer | The maximum number of ad units to include in the response, used for paging.
    String pageToken = "pageToken_example"; // String | A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response.
    try {
      AdUnits result = apiInstance.adsensehostAccountsAdunitsList(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, includeInactive, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsList");
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
| **accountId** | **String**| Account which contains the ad client. | |
| **adClientId** | **String**| Ad client for which to list ad units. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **includeInactive** | **Boolean**| Whether to include inactive ad units. Default: true. | [optional] |
| **maxResults** | **Integer**| The maximum number of ad units to include in the response, used for paging. | [optional] |
| **pageToken** | **String**| A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] |

### Return type

[**AdUnits**](AdUnits.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsPatch"></a>
# **adsensehostAccountsAdunitsPatch**
> AdUnit adsensehostAccountsAdunitsPatch(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, adUnit)



Update the supplied ad unit in the specified publisher AdSense account. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad client.
    String adClientId = "adClientId_example"; // String | Ad client which contains the ad unit.
    String adUnitId = "adUnitId_example"; // String | Ad unit to get.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AdUnit adUnit = new AdUnit(); // AdUnit | 
    try {
      AdUnit result = apiInstance.adsensehostAccountsAdunitsPatch(accountId, adClientId, adUnitId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, adUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsPatch");
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
| **accountId** | **String**| Account which contains the ad client. | |
| **adClientId** | **String**| Ad client which contains the ad unit. | |
| **adUnitId** | **String**| Ad unit to get. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **adUnit** | [**AdUnit**](AdUnit.md)|  | [optional] |

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsAdunitsUpdate"></a>
# **adsensehostAccountsAdunitsUpdate**
> AdUnit adsensehostAccountsAdunitsUpdate(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, adUnit)



Update the supplied ad unit in the specified publisher AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account which contains the ad client.
    String adClientId = "adClientId_example"; // String | Ad client which contains the ad unit.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AdUnit adUnit = new AdUnit(); // AdUnit | 
    try {
      AdUnit result = apiInstance.adsensehostAccountsAdunitsUpdate(accountId, adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, adUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsAdunitsUpdate");
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
| **accountId** | **String**| Account which contains the ad client. | |
| **adClientId** | **String**| Ad client which contains the ad unit. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **adUnit** | [**AdUnit**](AdUnit.md)|  | [optional] |

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsGet"></a>
# **adsensehostAccountsGet**
> Account adsensehostAccountsGet(accountId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get information about the selected associated AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to get information about.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Account result = apiInstance.adsensehostAccountsGet(accountId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsGet");
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
| **accountId** | **String**| Account to get information about. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Account**](Account.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsList"></a>
# **adsensehostAccountsList**
> Accounts adsensehostAccountsList(filterAdClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



List hosted accounts associated with this AdSense account by ad client id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    List<String> filterAdClientId = Arrays.asList(); // List<String> | Ad clients to list accounts for.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Accounts result = apiInstance.adsensehostAccountsList(filterAdClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsList");
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
| **filterAdClientId** | [**List&lt;String&gt;**](String.md)| Ad clients to list accounts for. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAccountsReportsGenerate"></a>
# **adsensehostAccountsReportsGenerate**
> Report adsensehostAccountsReportsGenerate(accountId, startDate, endDate, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, dimension, filter, locale, maxResults, metric, sort, startIndex)



Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify \&quot;alt&#x3D;csv\&quot; as a query parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Hosted account upon which to report.
    String startDate = "startDate_example"; // String | Start of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
    String endDate = "endDate_example"; // String | End of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    List<String> dimension = Arrays.asList(); // List<String> | Dimensions to base the report on.
    List<String> filter = Arrays.asList(); // List<String> | Filters to be run on the report.
    String locale = "locale_example"; // String | Optional locale to use for translating report output to a local language. Defaults to \"en_US\" if not specified.
    Integer maxResults = 56; // Integer | The maximum number of rows of report data to return.
    List<String> metric = Arrays.asList(); // List<String> | Numeric columns to include in the report.
    List<String> sort = Arrays.asList(); // List<String> | The name of a dimension or metric to sort the resulting report on, optionally prefixed with \"+\" to sort ascending or \"-\" to sort descending. If no prefix is specified, the column is sorted ascending.
    Integer startIndex = 56; // Integer | Index of the first row of report data to return.
    try {
      Report result = apiInstance.adsensehostAccountsReportsGenerate(accountId, startDate, endDate, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, dimension, filter, locale, maxResults, metric, sort, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#adsensehostAccountsReportsGenerate");
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
| **accountId** | **String**| Hosted account upon which to report. | |
| **startDate** | **String**| Start of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | |
| **endDate** | **String**| End of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **dimension** | [**List&lt;String&gt;**](String.md)| Dimensions to base the report on. | [optional] |
| **filter** | [**List&lt;String&gt;**](String.md)| Filters to be run on the report. | [optional] |
| **locale** | **String**| Optional locale to use for translating report output to a local language. Defaults to \&quot;en_US\&quot; if not specified. | [optional] |
| **maxResults** | **Integer**| The maximum number of rows of report data to return. | [optional] |
| **metric** | [**List&lt;String&gt;**](String.md)| Numeric columns to include in the report. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The name of a dimension or metric to sort the resulting report on, optionally prefixed with \&quot;+\&quot; to sort ascending or \&quot;-\&quot; to sort descending. If no prefix is specified, the column is sorted ascending. | [optional] |
| **startIndex** | **Integer**| Index of the first row of report data to return. | [optional] |

### Return type

[**Report**](Report.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

