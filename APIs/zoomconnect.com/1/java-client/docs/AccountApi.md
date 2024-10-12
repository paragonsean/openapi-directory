# AccountApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRestV1AccountUserPut**](AccountApi.md#apiRestV1AccountUserPut) | **PUT** /api/rest/v1/account/user | create |
| [**apiRestV1AccountUserUserIdPost**](AccountApi.md#apiRestV1AccountUserUserIdPost) | **POST** /api/rest/v1/account/user/{userId} | update |
| [**getBalance**](AccountApi.md#getBalance) | **GET** /api/rest/v1/account/balance | balance |
| [**getStatistics**](AccountApi.md#getStatistics) | **GET** /api/rest/v1/account/statistics | statistics |
| [**getUser**](AccountApi.md#getUser) | **GET** /api/rest/v1/account/user/{userId} | getUser |
| [**search**](AccountApi.md#search) | **GET** /api/rest/v1/account/user | search |
| [**transfer**](AccountApi.md#transfer) | **POST** /api/rest/v1/account/transfer | transfer |


<a id="apiRestV1AccountUserPut"></a>
# **apiRestV1AccountUserPut**
> WebServiceUser apiRestV1AccountUserPut(body)

create

Creates a new sub-account in your team. The following fields are required &lt;i&gt;firstname, lastname, email address, contact number&lt;/i&gt; and &lt;i&gt;password.&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    WebServiceUser body = new WebServiceUser(); // WebServiceUser | request
    try {
      WebServiceUser result = apiInstance.apiRestV1AccountUserPut(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#apiRestV1AccountUserPut");
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
| **body** | [**WebServiceUser**](WebServiceUser.md)| request | [optional] |

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1AccountUserUserIdPost"></a>
# **apiRestV1AccountUserUserIdPost**
> WebServiceUser apiRestV1AccountUserUserIdPost(userId, body)

update

Updates a sub-account in your team. The following fields can be updated &lt;i&gt;firstname, lastname, contact number&lt;/i&gt; and &lt;i&gt;password.&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long userId = 56L; // Long | userId
    WebServiceUser body = new WebServiceUser(); // WebServiceUser | request
    try {
      WebServiceUser result = apiInstance.apiRestV1AccountUserUserIdPost(userId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#apiRestV1AccountUserUserIdPost");
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
| **userId** | **Long**| userId | |
| **body** | [**WebServiceUser**](WebServiceUser.md)| request | [optional] |

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getBalance"></a>
# **getBalance**
> WebServiceAccount getBalance()

balance

Returns your account&#39;s credit balance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      WebServiceAccount result = apiInstance.getBalance();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getBalance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebServiceAccount**](WebServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getStatistics"></a>
# **getStatistics**
> WebServiceAccountStatistics getStatistics(from, to, userEmailAddress, campaign, includeRefundedAndOptout, calculateCreditValue)

statistics

Returns data from the statistics report. Note that by default the statistics shown are based on the number of messages, use the calculateCreditValue should you wish to calculate the statistics based on credit value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | date format: dd-MM-yyyy
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | date format: dd-MM-yyyy
    String userEmailAddress = "userEmailAddress_example"; // String | optional email address of user to return statistics for a single user, default is to return statistics for all users if administrator, or statistics for your own account if not an administrator
    String campaign = "campaign_example"; // String | optional campaign name
    Boolean includeRefundedAndOptout = true; // Boolean | optionally include refunded and optout counts, default is false
    Boolean calculateCreditValue = true; // Boolean | optionally calculate using credit value rather than message count, default is false
    try {
      WebServiceAccountStatistics result = apiInstance.getStatistics(from, to, userEmailAddress, campaign, includeRefundedAndOptout, calculateCreditValue);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getStatistics");
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
| **from** | **OffsetDateTime**| date format: dd-MM-yyyy | [optional] |
| **to** | **OffsetDateTime**| date format: dd-MM-yyyy | [optional] |
| **userEmailAddress** | **String**| optional email address of user to return statistics for a single user, default is to return statistics for all users if administrator, or statistics for your own account if not an administrator | [optional] |
| **campaign** | **String**| optional campaign name | [optional] |
| **includeRefundedAndOptout** | **Boolean**| optionally include refunded and optout counts, default is false | [optional] |
| **calculateCreditValue** | **Boolean**| optionally calculate using credit value rather than message count, default is false | [optional] |

### Return type

[**WebServiceAccountStatistics**](WebServiceAccountStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getUser"></a>
# **getUser**
> WebServiceUser getUser(userId)

getUser

Gets a user from a given user id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long userId = 56L; // Long | userId
    try {
      WebServiceUser result = apiInstance.getUser(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getUser");
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
| **userId** | **Long**| userId | |

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="search"></a>
# **search**
> WebServiceUsers search(searchEmail)

search

Find a user for a particular email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String searchEmail = "searchEmail_example"; // String | search by email address
    try {
      WebServiceUsers result = apiInstance.search(searchEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#search");
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
| **searchEmail** | **String**| search by email address | |

### Return type

[**WebServiceUsers**](WebServiceUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="transfer"></a>
# **transfer**
> WebServiceUser transfer(body)

transfer

Transfers credits between two users in the same team. The &lt;i&gt;account email address&lt;/i&gt; fields as well as the &lt;i&gt;number of credits to transfer&lt;/i&gt; are required. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    AccountApi apiInstance = new AccountApi(defaultClient);
    WebServiceTransferCreditsRequest body = new WebServiceTransferCreditsRequest(); // WebServiceTransferCreditsRequest | request
    try {
      WebServiceUser result = apiInstance.transfer(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#transfer");
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
| **body** | [**WebServiceTransferCreditsRequest**](WebServiceTransferCreditsRequest.md)| request | [optional] |

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

