# Api20100401IpAddressApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipIpAddress**](Api20100401IpAddressApi.md#createSipIpAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json |  |
| [**deleteSipIpAddress**](Api20100401IpAddressApi.md#deleteSipIpAddress) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json |  |
| [**fetchSipIpAddress**](Api20100401IpAddressApi.md#fetchSipIpAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json |  |
| [**listSipIpAddress**](Api20100401IpAddressApi.md#listSipIpAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json |  |
| [**updateSipIpAddress**](Api20100401IpAddressApi.md#updateSipIpAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json |  |


<a id="createSipIpAddress"></a>
# **createSipIpAddress**
> ApiV2010AccountSipSipIpAccessControlListSipIpAddress createSipIpAddress(accountSid, ipAccessControlListSid, friendlyName, ipAddress, cidrPrefixLength)



Create a new IpAddress resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAddressApi apiInstance = new Api20100401IpAddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid with which to associate the created IpAddress resource.
    String friendlyName = "friendlyName_example"; // String | A human readable descriptive text for this resource, up to 255 characters long.
    String ipAddress = "ipAddress_example"; // String | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
    Integer cidrPrefixLength = 56; // Integer | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
    try {
      ApiV2010AccountSipSipIpAccessControlListSipIpAddress result = apiInstance.createSipIpAddress(accountSid, ipAccessControlListSid, friendlyName, ipAddress, cidrPrefixLength);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAddressApi#createSipIpAddress");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **ipAccessControlListSid** | **String**| The IpAccessControlList Sid with which to associate the created IpAddress resource. | |
| **friendlyName** | **String**| A human readable descriptive text for this resource, up to 255 characters long. | |
| **ipAddress** | **String**| An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. | |
| **cidrPrefixLength** | **Integer**| An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional] |

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipIpAddress"></a>
# **deleteSipIpAddress**
> deleteSipIpAddress(accountSid, ipAccessControlListSid, sid)



Delete an IpAddress resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAddressApi apiInstance = new Api20100401IpAddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to delete.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
    try {
      apiInstance.deleteSipIpAddress(accountSid, ipAccessControlListSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAddressApi#deleteSipIpAddress");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to delete. | |
| **sid** | **String**| A 34 character string that uniquely identifies the resource to delete. | |

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

<a id="fetchSipIpAddress"></a>
# **fetchSipIpAddress**
> ApiV2010AccountSipSipIpAccessControlListSipIpAddress fetchSipIpAddress(accountSid, ipAccessControlListSid, sid)



Read one IpAddress resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAddressApi apiInstance = new Api20100401IpAddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the IpAddress resource to fetch.
    try {
      ApiV2010AccountSipSipIpAccessControlListSipIpAddress result = apiInstance.fetchSipIpAddress(accountSid, ipAccessControlListSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAddressApi#fetchSipIpAddress");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to fetch. | |
| **sid** | **String**| A 34 character string that uniquely identifies the IpAddress resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipIpAddress"></a>
# **listSipIpAddress**
> ListSipIpAddressResponse listSipIpAddress(accountSid, ipAccessControlListSid, pageSize, page, pageToken)



Read multiple IpAddress resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAddressApi apiInstance = new Api20100401IpAddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipIpAddressResponse result = apiInstance.listSipIpAddress(accountSid, ipAccessControlListSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAddressApi#listSipIpAddress");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipIpAddressResponse**](ListSipIpAddressResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSipIpAddress"></a>
# **updateSipIpAddress**
> ApiV2010AccountSipSipIpAccessControlListSipIpAddress updateSipIpAddress(accountSid, ipAccessControlListSid, sid, cidrPrefixLength, friendlyName, ipAddress)



Update an IpAddress resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAddressApi apiInstance = new Api20100401IpAddressApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to update.
    String sid = "sid_example"; // String | A 34 character string that identifies the IpAddress resource to update.
    Integer cidrPrefixLength = 56; // Integer | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
    String friendlyName = "friendlyName_example"; // String | A human readable descriptive text for this resource, up to 255 characters long.
    String ipAddress = "ipAddress_example"; // String | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
    try {
      ApiV2010AccountSipSipIpAccessControlListSipIpAddress result = apiInstance.updateSipIpAddress(accountSid, ipAccessControlListSid, sid, cidrPrefixLength, friendlyName, ipAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAddressApi#updateSipIpAddress");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to update. | |
| **sid** | **String**| A 34 character string that identifies the IpAddress resource to update. | |
| **cidrPrefixLength** | **Integer**| An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional] |
| **friendlyName** | **String**| A human readable descriptive text for this resource, up to 255 characters long. | [optional] |
| **ipAddress** | **String**| An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. | [optional] |

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

