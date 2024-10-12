# FireteamApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fireteamGetActivePrivateClanFireteamCount**](FireteamApi.md#fireteamGetActivePrivateClanFireteamCount) | **GET** /Fireteam/Clan/{groupId}/ActiveCount/ |  |
| [**fireteamGetAvailableClanFireteams**](FireteamApi.md#fireteamGetAvailableClanFireteams) | **GET** /Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/ |  |
| [**fireteamGetClanFireteam**](FireteamApi.md#fireteamGetClanFireteam) | **GET** /Fireteam/Clan/{groupId}/Summary/{fireteamId}/ |  |
| [**fireteamGetMyClanFireteams**](FireteamApi.md#fireteamGetMyClanFireteams) | **GET** /Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/ |  |
| [**fireteamSearchPublicAvailableClanFireteams**](FireteamApi.md#fireteamSearchPublicAvailableClanFireteams) | **GET** /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/ |  |


<a id="fireteamGetActivePrivateClanFireteamCount"></a>
# **fireteamGetActivePrivateClanFireteamCount**
> Destiny2EquipItem200Response fireteamGetActivePrivateClanFireteamCount(groupId)



Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FireteamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FireteamApi apiInstance = new FireteamApi(defaultClient);
    Long groupId = 56L; // Long | The group id of the clan.
    try {
      Destiny2EquipItem200Response result = apiInstance.fireteamGetActivePrivateClanFireteamCount(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FireteamApi#fireteamGetActivePrivateClanFireteamCount");
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
| **groupId** | **Long**| The group id of the clan. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="fireteamGetAvailableClanFireteams"></a>
# **fireteamGetAvailableClanFireteams**
> FireteamGetAvailableClanFireteams200Response fireteamGetAvailableClanFireteams(activityType, dateRange, groupId, page, platform, publicOnly, slotFilter, excludeImmediate, langFilter)



Gets a listing of all of this clan&#39;s fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FireteamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FireteamApi apiInstance = new FireteamApi(defaultClient);
    Integer activityType = 56; // Integer | The activity type to filter by.
    Integer dateRange = 56; // Integer | The date range to grab available fireteams.
    Long groupId = 56L; // Long | The group id of the clan.
    Integer page = 56; // Integer | Zero based page
    Integer platform = 56; // Integer | The platform filter.
    Integer publicOnly = 56; // Integer | Determines public/private filtering.
    Integer slotFilter = 56; // Integer | Filters based on available slots
    Boolean excludeImmediate = true; // Boolean | If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
    String langFilter = "langFilter_example"; // String | An optional language filter.
    try {
      FireteamGetAvailableClanFireteams200Response result = apiInstance.fireteamGetAvailableClanFireteams(activityType, dateRange, groupId, page, platform, publicOnly, slotFilter, excludeImmediate, langFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FireteamApi#fireteamGetAvailableClanFireteams");
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
| **activityType** | **Integer**| The activity type to filter by. | |
| **dateRange** | **Integer**| The date range to grab available fireteams. | |
| **groupId** | **Long**| The group id of the clan. | |
| **page** | **Integer**| Zero based page | |
| **platform** | **Integer**| The platform filter. | |
| **publicOnly** | **Integer**| Determines public/private filtering. | |
| **slotFilter** | **Integer**| Filters based on available slots | |
| **excludeImmediate** | **Boolean**| If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum. | [optional] |
| **langFilter** | **String**| An optional language filter. | [optional] |

### Return type

[**FireteamGetAvailableClanFireteams200Response**](FireteamGetAvailableClanFireteams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="fireteamGetClanFireteam"></a>
# **fireteamGetClanFireteam**
> FireteamGetClanFireteam200Response fireteamGetClanFireteam(fireteamId, groupId)



Gets a specific fireteam.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FireteamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FireteamApi apiInstance = new FireteamApi(defaultClient);
    Long fireteamId = 56L; // Long | The unique id of the fireteam.
    Long groupId = 56L; // Long | The group id of the clan.
    try {
      FireteamGetClanFireteam200Response result = apiInstance.fireteamGetClanFireteam(fireteamId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FireteamApi#fireteamGetClanFireteam");
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
| **fireteamId** | **Long**| The unique id of the fireteam. | |
| **groupId** | **Long**| The group id of the clan. | |

### Return type

[**FireteamGetClanFireteam200Response**](FireteamGetClanFireteam200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="fireteamGetMyClanFireteams"></a>
# **fireteamGetMyClanFireteams**
> FireteamGetMyClanFireteams200Response fireteamGetMyClanFireteams(groupId, includeClosed, page, platform, groupFilter, langFilter)



Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FireteamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FireteamApi apiInstance = new FireteamApi(defaultClient);
    Long groupId = 56L; // Long | The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
    Boolean includeClosed = true; // Boolean | If true, return fireteams that have been closed.
    Integer page = 56; // Integer | Deprecated parameter, ignored.
    Integer platform = 56; // Integer | The platform filter.
    Boolean groupFilter = true; // Boolean | If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
    String langFilter = "langFilter_example"; // String | An optional language filter.
    try {
      FireteamGetMyClanFireteams200Response result = apiInstance.fireteamGetMyClanFireteams(groupId, includeClosed, page, platform, groupFilter, langFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FireteamApi#fireteamGetMyClanFireteams");
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
| **groupId** | **Long**| The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true). | |
| **includeClosed** | **Boolean**| If true, return fireteams that have been closed. | |
| **page** | **Integer**| Deprecated parameter, ignored. | |
| **platform** | **Integer**| The platform filter. | |
| **groupFilter** | **Boolean**| If true, filter by clan. Otherwise, ignore the clan and show all of the user&#39;s fireteams. | [optional] |
| **langFilter** | **String**| An optional language filter. | [optional] |

### Return type

[**FireteamGetMyClanFireteams200Response**](FireteamGetMyClanFireteams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="fireteamSearchPublicAvailableClanFireteams"></a>
# **fireteamSearchPublicAvailableClanFireteams**
> FireteamGetAvailableClanFireteams200Response fireteamSearchPublicAvailableClanFireteams(activityType, dateRange, page, platform, slotFilter, excludeImmediate, langFilter)



Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FireteamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FireteamApi apiInstance = new FireteamApi(defaultClient);
    Integer activityType = 56; // Integer | The activity type to filter by.
    Integer dateRange = 56; // Integer | The date range to grab available fireteams.
    Integer page = 56; // Integer | Zero based page
    Integer platform = 56; // Integer | The platform filter.
    Integer slotFilter = 56; // Integer | Filters based on available slots
    Boolean excludeImmediate = true; // Boolean | If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
    String langFilter = "langFilter_example"; // String | An optional language filter.
    try {
      FireteamGetAvailableClanFireteams200Response result = apiInstance.fireteamSearchPublicAvailableClanFireteams(activityType, dateRange, page, platform, slotFilter, excludeImmediate, langFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FireteamApi#fireteamSearchPublicAvailableClanFireteams");
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
| **activityType** | **Integer**| The activity type to filter by. | |
| **dateRange** | **Integer**| The date range to grab available fireteams. | |
| **page** | **Integer**| Zero based page | |
| **platform** | **Integer**| The platform filter. | |
| **slotFilter** | **Integer**| Filters based on available slots | |
| **excludeImmediate** | **Boolean**| If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum. | [optional] |
| **langFilter** | **String**| An optional language filter. | [optional] |

### Return type

[**FireteamGetAvailableClanFireteams200Response**](FireteamGetAvailableClanFireteams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

