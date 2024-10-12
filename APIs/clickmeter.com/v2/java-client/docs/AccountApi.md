# AccountApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountDeleteDomainWhitelist**](AccountApi.md#accountDeleteDomainWhitelist) | **DELETE** /account/domainwhitelist/{whitelistId} | Delete an domain entry |
| [**accountDeleteGuest**](AccountApi.md#accountDeleteGuest) | **DELETE** /account/guests/{guestId} | Delete a guest |
| [**accountDeleteIpBlacklist**](AccountApi.md#accountDeleteIpBlacklist) | **DELETE** /account/ipblacklist/{blacklistId} | Delete an ip blacklist entry |
| [**accountGet**](AccountApi.md#accountGet) | **GET** /account | Retrieve current account data |
| [**accountGetDomainWhitelist**](AccountApi.md#accountGetDomainWhitelist) | **GET** /account/domainwhitelist | Retrieve list of a domains allowed to redirect in DDU mode |
| [**accountGetGuest**](AccountApi.md#accountGetGuest) | **GET** /account/guests/{guestId} | Retrieve a guest |
| [**accountGetGuests**](AccountApi.md#accountGetGuests) | **GET** /account/guests | Retrieve list of a guest |
| [**accountGetGuestsCount**](AccountApi.md#accountGetGuestsCount) | **GET** /account/guests/count | Retrieve count of guests |
| [**accountGetIpBlacklist**](AccountApi.md#accountGetIpBlacklist) | **GET** /account/ipblacklist | Retrieve list of a ip to exclude from event tracking |
| [**accountGetPermissions**](AccountApi.md#accountGetPermissions) | **GET** /account/guests/{guestId}/permissions | Retrieve permissions for a guest |
| [**accountGetPermissionsCount**](AccountApi.md#accountGetPermissionsCount) | **GET** /account/guests/{guestId}/permissions/count | Retrieve count of the permissions for a guest |
| [**accountGetPlan**](AccountApi.md#accountGetPlan) | **GET** /account/plan | Retrieve current account plan |
| [**accountGuestsGuestIdTypePermissionsPatchPost**](AccountApi.md#accountGuestsGuestIdTypePermissionsPatchPost) | **POST** /account/guests/{guestId}/{type}/permissions/patch | Change the permission on a shared object |
| [**accountPatchPermissions**](AccountApi.md#accountPatchPermissions) | **PUT** /account/guests/{guestId}/{type}/permissions/patch | Change the permission on a shared object |
| [**accountPost**](AccountApi.md#accountPost) | **POST** /account | Update current account data |
| [**accountPostGuest**](AccountApi.md#accountPostGuest) | **POST** /account/guests/{guestId} | Update a guest |
| [**accountPutDomainWhitelist**](AccountApi.md#accountPutDomainWhitelist) | **POST** /account/domainwhitelist | Create an domain entry |
| [**accountPutGuest**](AccountApi.md#accountPutGuest) | **POST** /account/guests | Create a guest |
| [**accountPutIpBlacklist**](AccountApi.md#accountPutIpBlacklist) | **POST** /account/ipblacklist | Create an ip blacklist entry |


<a id="accountDeleteDomainWhitelist"></a>
# **accountDeleteDomainWhitelist**
> ApiCoreDtoAccountingDomainWhitelistEntry accountDeleteDomainWhitelist(whitelistId)

Delete an domain entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String whitelistId = "whitelistId_example"; // String | The id of the domain to delete
    try {
      ApiCoreDtoAccountingDomainWhitelistEntry result = apiInstance.accountDeleteDomainWhitelist(whitelistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountDeleteDomainWhitelist");
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
| **whitelistId** | **String**| The id of the domain to delete | |

### Return type

[**ApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreDtoAccountingDomainWhitelistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountDeleteGuest"></a>
# **accountDeleteGuest**
> ApiCoreResponsesEntityUriSystemInt64 accountDeleteGuest(guestId)

Delete a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.accountDeleteGuest(guestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountDeleteGuest");
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
| **guestId** | **Long**| Id of the guest | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountDeleteIpBlacklist"></a>
# **accountDeleteIpBlacklist**
> ApiCoreDtoAccountingIpBlacklistEntry accountDeleteIpBlacklist(blacklistId)

Delete an ip blacklist entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String blacklistId = "blacklistId_example"; // String | The id of the ip to delete
    try {
      ApiCoreDtoAccountingIpBlacklistEntry result = apiInstance.accountDeleteIpBlacklist(blacklistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountDeleteIpBlacklist");
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
| **blacklistId** | **String**| The id of the ip to delete | |

### Return type

[**ApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreDtoAccountingIpBlacklistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGet"></a>
# **accountGet**
> ApiCoreDtoAccountingUser accountGet()

Retrieve current account data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      ApiCoreDtoAccountingUser result = apiInstance.accountGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGet");
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

[**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetDomainWhitelist"></a>
# **accountGetDomainWhitelist**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry accountGetDomainWhitelist(offset, limit)

Retrieve list of a domains allowed to redirect in DDU mode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry result = apiInstance.accountGetDomainWhitelist(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetDomainWhitelist");
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
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetGuest"></a>
# **accountGetGuest**
> ApiCoreDtoAccountingGuest accountGetGuest(guestId)

Retrieve a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    try {
      ApiCoreDtoAccountingGuest result = apiInstance.accountGetGuest(guestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetGuest");
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
| **guestId** | **Long**| Id of the guest | |

### Return type

[**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetGuests"></a>
# **accountGetGuests**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 accountGetGuests(offset, limit, sortBy, sortDirection, textSearch)

Retrieve list of a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.accountGetGuests(offset, limit, sortBy, sortDirection, textSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetGuests");
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
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetGuestsCount"></a>
# **accountGetGuestsCount**
> ApiCoreResponsesCountResponce accountGetGuestsCount(textSearch)

Retrieve count of guests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    try {
      ApiCoreResponsesCountResponce result = apiInstance.accountGetGuestsCount(textSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetGuestsCount");
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
| **textSearch** | **String**| Filter fields by this pattern | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetIpBlacklist"></a>
# **accountGetIpBlacklist**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry accountGetIpBlacklist(offset, limit)

Retrieve list of a ip to exclude from event tracking

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry result = apiInstance.accountGetIpBlacklist(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetIpBlacklist");
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
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetPermissions"></a>
# **accountGetPermissions**
> ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant accountGetPermissions(guestId, entityType, offset, limit, type, entityId)

Retrieve permissions for a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    String entityType = "datapoint"; // String | Can be \"datapoint\" or \"group\"
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String type = "r"; // String | Can be \"w\" or \"r\"
    Long entityId = 56L; // Long | Optional id of the datapoint/group entity to filter by
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant result = apiInstance.accountGetPermissions(guestId, entityType, offset, limit, type, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetPermissions");
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
| **guestId** | **Long**| Id of the guest | |
| **entityType** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | [optional] [enum: datapoint, group] |
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **type** | **String**| Can be \&quot;w\&quot; or \&quot;r\&quot; | [optional] [enum: r, w] |
| **entityId** | **Long**| Optional id of the datapoint/group entity to filter by | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant**](ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetPermissionsCount"></a>
# **accountGetPermissionsCount**
> ApiCoreResponsesCountResponce accountGetPermissionsCount(guestId, entityType, type, entityId)

Retrieve count of the permissions for a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    String entityType = "datapoint"; // String | Can be \"datapoint\" or \"group\"
    String type = "r"; // String | Can be \"w\" or \"r\"
    Long entityId = 56L; // Long | Optional id of the datapoint/group entity to filter by
    try {
      ApiCoreResponsesCountResponce result = apiInstance.accountGetPermissionsCount(guestId, entityType, type, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetPermissionsCount");
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
| **guestId** | **Long**| Id of the guest | |
| **entityType** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | [optional] [enum: datapoint, group] |
| **type** | **String**| Can be \&quot;w\&quot; or \&quot;r\&quot; | [optional] [enum: r, w] |
| **entityId** | **Long**| Optional id of the datapoint/group entity to filter by | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGetPlan"></a>
# **accountGetPlan**
> ApiCoreDtoAccountingPlan accountGetPlan()

Retrieve current account plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      ApiCoreDtoAccountingPlan result = apiInstance.accountGetPlan();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGetPlan");
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

[**ApiCoreDtoAccountingPlan**](ApiCoreDtoAccountingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountGuestsGuestIdTypePermissionsPatchPost"></a>
# **accountGuestsGuestIdTypePermissionsPatchPost**
> ApiCoreResponsesEntityUriSystemInt64 accountGuestsGuestIdTypePermissionsPatchPost(guestId, type, apiCoreRequestsPermissionPatchRequest)

Change the permission on a shared object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    String type = "datapoint"; // String | Can be \"datapoint\" or \"group\"
    ApiCoreRequestsPermissionPatchRequest apiCoreRequestsPermissionPatchRequest = new ApiCoreRequestsPermissionPatchRequest(); // ApiCoreRequestsPermissionPatchRequest | The patch permission request
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.accountGuestsGuestIdTypePermissionsPatchPost(guestId, type, apiCoreRequestsPermissionPatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGuestsGuestIdTypePermissionsPatchPost");
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
| **guestId** | **Long**| Id of the guest | |
| **type** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | [enum: datapoint, group] |
| **apiCoreRequestsPermissionPatchRequest** | [**ApiCoreRequestsPermissionPatchRequest**](ApiCoreRequestsPermissionPatchRequest.md)| The patch permission request | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountPatchPermissions"></a>
# **accountPatchPermissions**
> ApiCoreResponsesEntityUriSystemInt64 accountPatchPermissions(guestId, type, apiCoreRequestsPermissionPatchRequest)

Change the permission on a shared object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    String type = "datapoint"; // String | Can be \"datapoint\" or \"group\"
    ApiCoreRequestsPermissionPatchRequest apiCoreRequestsPermissionPatchRequest = new ApiCoreRequestsPermissionPatchRequest(); // ApiCoreRequestsPermissionPatchRequest | The patch permission request
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.accountPatchPermissions(guestId, type, apiCoreRequestsPermissionPatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountPatchPermissions");
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
| **guestId** | **Long**| Id of the guest | |
| **type** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | [enum: datapoint, group] |
| **apiCoreRequestsPermissionPatchRequest** | [**ApiCoreRequestsPermissionPatchRequest**](ApiCoreRequestsPermissionPatchRequest.md)| The patch permission request | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountPost"></a>
# **accountPost**
> ApiCoreDtoAccountingUser accountPost(apiCoreDtoAccountingUser)

Update current account data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    ApiCoreDtoAccountingUser apiCoreDtoAccountingUser = new ApiCoreDtoAccountingUser(); // ApiCoreDtoAccountingUser | 
    try {
      ApiCoreDtoAccountingUser result = apiInstance.accountPost(apiCoreDtoAccountingUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountPost");
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
| **apiCoreDtoAccountingUser** | [**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)|  | |

### Return type

[**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountPostGuest"></a>
# **accountPostGuest**
> ApiCoreDtoAccountingGuest accountPostGuest(guestId, apiCoreDtoAccountingGuest)

Update a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Long guestId = 56L; // Long | Id of the guest
    ApiCoreDtoAccountingGuest apiCoreDtoAccountingGuest = new ApiCoreDtoAccountingGuest(); // ApiCoreDtoAccountingGuest | Guest object with field updated
    try {
      ApiCoreDtoAccountingGuest result = apiInstance.accountPostGuest(guestId, apiCoreDtoAccountingGuest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountPostGuest");
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
| **guestId** | **Long**| Id of the guest | |
| **apiCoreDtoAccountingGuest** | [**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)| Guest object with field updated | |

### Return type

[**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountPutDomainWhitelist"></a>
# **accountPutDomainWhitelist**
> ApiCoreDtoAccountingDomainWhitelistEntry accountPutDomainWhitelist(apiCoreDtoAccountingDomainWhitelistEntry)

Create an domain entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    ApiCoreDtoAccountingDomainWhitelistEntry apiCoreDtoAccountingDomainWhitelistEntry = new ApiCoreDtoAccountingDomainWhitelistEntry(); // ApiCoreDtoAccountingDomainWhitelistEntry | The entry to add
    try {
      ApiCoreDtoAccountingDomainWhitelistEntry result = apiInstance.accountPutDomainWhitelist(apiCoreDtoAccountingDomainWhitelistEntry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountPutDomainWhitelist");
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
| **apiCoreDtoAccountingDomainWhitelistEntry** | [**ApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreDtoAccountingDomainWhitelistEntry.md)| The entry to add | |

### Return type

[**ApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreDtoAccountingDomainWhitelistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountPutGuest"></a>
# **accountPutGuest**
> ApiCoreDtoAccountingGuest accountPutGuest(apiCoreDtoAccountingGuest)

Create a guest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    ApiCoreDtoAccountingGuest apiCoreDtoAccountingGuest = new ApiCoreDtoAccountingGuest(); // ApiCoreDtoAccountingGuest | Guest object to create
    try {
      ApiCoreDtoAccountingGuest result = apiInstance.accountPutGuest(apiCoreDtoAccountingGuest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountPutGuest");
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
| **apiCoreDtoAccountingGuest** | [**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)| Guest object to create | |

### Return type

[**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="accountPutIpBlacklist"></a>
# **accountPutIpBlacklist**
> ApiCoreDtoAccountingIpBlacklistEntry accountPutIpBlacklist(apiCoreDtoAccountingIpBlacklistEntry)

Create an ip blacklist entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    ApiCoreDtoAccountingIpBlacklistEntry apiCoreDtoAccountingIpBlacklistEntry = new ApiCoreDtoAccountingIpBlacklistEntry(); // ApiCoreDtoAccountingIpBlacklistEntry | The entry to add
    try {
      ApiCoreDtoAccountingIpBlacklistEntry result = apiInstance.accountPutIpBlacklist(apiCoreDtoAccountingIpBlacklistEntry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountPutIpBlacklist");
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
| **apiCoreDtoAccountingIpBlacklistEntry** | [**ApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreDtoAccountingIpBlacklistEntry.md)| The entry to add | |

### Return type

[**ApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreDtoAccountingIpBlacklistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

