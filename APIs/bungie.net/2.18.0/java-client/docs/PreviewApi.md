# PreviewApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**destiny2GetClanAggregateStats_0**](PreviewApi.md#destiny2GetClanAggregateStats_0) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ |  |
| [**destiny2GetClanLeaderboards_0**](PreviewApi.md#destiny2GetClanLeaderboards_0) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ |  |
| [**destiny2GetLeaderboardsForCharacter_0**](PreviewApi.md#destiny2GetLeaderboardsForCharacter_0) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ |  |
| [**destiny2GetLeaderboards_0**](PreviewApi.md#destiny2GetLeaderboards_0) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ |  |
| [**destiny2GetPublicVendors_0**](PreviewApi.md#destiny2GetPublicVendors_0) | **GET** /Destiny2/Vendors/ |  |
| [**destiny2InsertSocketPlugFree_0**](PreviewApi.md#destiny2InsertSocketPlugFree_0) | **POST** /Destiny2/Actions/Items/InsertSocketPlugFree/ |  |
| [**destiny2InsertSocketPlug_0**](PreviewApi.md#destiny2InsertSocketPlug_0) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ |  |


<a id="destiny2GetClanAggregateStats_0"></a>
# **destiny2GetClanAggregateStats_0**
> Destiny2GetClanAggregateStats200Response destiny2GetClanAggregateStats_0(groupId, modes)



Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    Long groupId = 56L; // Long | Group ID of the clan whose leaderboards you wish to fetch.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    try {
      Destiny2GetClanAggregateStats200Response result = apiInstance.destiny2GetClanAggregateStats_0(groupId, modes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2GetClanAggregateStats_0");
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
| **groupId** | **Long**| Group ID of the clan whose leaderboards you wish to fetch. | |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |

### Return type

[**Destiny2GetClanAggregateStats200Response**](Destiny2GetClanAggregateStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetClanLeaderboards_0"></a>
# **destiny2GetClanLeaderboards_0**
> Destiny2GetClanLeaderboards200Response destiny2GetClanLeaderboards_0(groupId, maxtop, modes, statid)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    Long groupId = 56L; // Long | Group ID of the clan whose leaderboards you wish to fetch.
    Integer maxtop = 56; // Integer | Maximum number of top players to return. Use a large number to get entire leaderboard.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    String statid = "statid_example"; // String | ID of stat to return rather than returning all Leaderboard stats.
    try {
      Destiny2GetClanLeaderboards200Response result = apiInstance.destiny2GetClanLeaderboards_0(groupId, maxtop, modes, statid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2GetClanLeaderboards_0");
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
| **groupId** | **Long**| Group ID of the clan whose leaderboards you wish to fetch. | |
| **maxtop** | **Integer**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] |

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetLeaderboardsForCharacter_0"></a>
# **destiny2GetLeaderboardsForCharacter_0**
> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboardsForCharacter_0(characterId, destinyMembershipId, membershipType, maxtop, modes, statid)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    Long characterId = 56L; // Long | The specific character to build the leaderboard around for the provided Destiny Membership.
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    Integer maxtop = 56; // Integer | Maximum number of top players to return. Use a large number to get entire leaderboard.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    String statid = "statid_example"; // String | ID of stat to return rather than returning all Leaderboard stats.
    try {
      Destiny2GetClanLeaderboards200Response result = apiInstance.destiny2GetLeaderboardsForCharacter_0(characterId, destinyMembershipId, membershipType, maxtop, modes, statid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2GetLeaderboardsForCharacter_0");
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
| **characterId** | **Long**| The specific character to build the leaderboard around for the provided Destiny Membership. | |
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **maxtop** | **Integer**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] |

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetLeaderboards_0"></a>
# **destiny2GetLeaderboards_0**
> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboards_0(destinyMembershipId, membershipType, maxtop, modes, statid)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    Integer maxtop = 56; // Integer | Maximum number of top players to return. Use a large number to get entire leaderboard.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    String statid = "statid_example"; // String | ID of stat to return rather than returning all Leaderboard stats.
    try {
      Destiny2GetClanLeaderboards200Response result = apiInstance.destiny2GetLeaderboards_0(destinyMembershipId, membershipType, maxtop, modes, statid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2GetLeaderboards_0");
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
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **maxtop** | **Integer**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] |

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetPublicVendors_0"></a>
# **destiny2GetPublicVendors_0**
> Destiny2GetPublicVendors200Response destiny2GetPublicVendors_0(components)



Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor&#39;s available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: &#39;It&#39;s a long story...&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetPublicVendors200Response result = apiInstance.destiny2GetPublicVendors_0(components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2GetPublicVendors_0");
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
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetPublicVendors200Response**](Destiny2GetPublicVendors200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing all valid components for the public Vendors endpoint.   It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.   If you want any of the other data - item details, whether or not you can buy it, etc... you&#39;ll have to call in the context of a character. I know, sad but true. |  -  |

<a id="destiny2InsertSocketPlugFree_0"></a>
# **destiny2InsertSocketPlugFree_0**
> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlugFree_0()



Insert a &#39;free&#39; plug into an item&#39;s socket. This does not require &#39;Advanced Write Action&#39; authorization and is available to 3rd-party apps, but will only work on &#39;free and reversible&#39; socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    try {
      Destiny2InsertSocketPlug200Response result = apiInstance.destiny2InsertSocketPlugFree_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2InsertSocketPlugFree_0");
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

[**Destiny2InsertSocketPlug200Response**](Destiny2InsertSocketPlug200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2InsertSocketPlug_0"></a>
# **destiny2InsertSocketPlug_0**
> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlug_0()



Insert a plug into a socketed item. I know how it sounds, but I assure you it&#39;s much more G-rated than you might be guessing. We haven&#39;t decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for &#39;InsertPlugs&#39; from the account owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PreviewApi apiInstance = new PreviewApi(defaultClient);
    try {
      Destiny2InsertSocketPlug200Response result = apiInstance.destiny2InsertSocketPlug_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewApi#destiny2InsertSocketPlug_0");
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

[**Destiny2InsertSocketPlug200Response**](Destiny2InsertSocketPlug200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

