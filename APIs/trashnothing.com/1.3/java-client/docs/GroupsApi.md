# GroupsApi

All URIs are relative to *https://trashnothing.com/api/v1.3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGroup**](GroupsApi.md#getGroup) | **GET** /groups/{group_id} | Retrieve a group |
| [**getGroupsByIds**](GroupsApi.md#getGroupsByIds) | **GET** /groups/multiple | Retrieve multiple groups |
| [**searchGroups**](GroupsApi.md#searchGroups) | **GET** /groups | Search groups |


<a id="getGroup"></a>
# **getGroup**
> Group getGroup(groupId)

Retrieve a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trashnothing.com/api/v1.3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | The ID of the group to retrieve.
    try {
      Group result = apiInstance.getGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroup");
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
| **groupId** | **String**| The ID of the group to retrieve. | |

### Return type

[**Group**](Group.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The group. |  -  |
| **404** | Group not found. |  -  |

<a id="getGroupsByIds"></a>
# **getGroupsByIds**
> List&lt;Group&gt; getGroupsByIds(groupIds)

Retrieve multiple groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trashnothing.com/api/v1.3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupIds = "groupIds_example"; // String | The IDs of the groups to retrieve.  If more than 20 group IDs are passed, only the first 20 groups will be returned.
    try {
      List<Group> result = apiInstance.getGroupsByIds(groupIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroupsByIds");
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
| **groupIds** | **String**| The IDs of the groups to retrieve.  If more than 20 group IDs are passed, only the first 20 groups will be returned. | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The groups. |  -  |
| **400** | Missing or invalid parameters. |  -  |

<a id="searchGroups"></a>
# **searchGroups**
> SearchGroups200Response searchGroups(name, latitude, longitude, distance, country, region, postalCode, page, perPage)

Search groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trashnothing.com/api/v1.3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String name = "name_example"; // String | Find groups that have the given text somewhere in their name (case insensitive).
    BigDecimal latitude = new BigDecimal(78); // BigDecimal | Find groups near the given latitude and longitude.
    BigDecimal longitude = new BigDecimal(78); // BigDecimal | Find groups near the given latitude and longitude.
    BigDecimal distance = new BigDecimal("100"); // BigDecimal | When latitude and longitude are passed, distance can optionally be passed to only return groups within a certain distance (in kilometers) from the point specified by the latitude and longitude.  The distance must be > 0 and <= 150 and will default to 100. 
    String country = "country_example"; // String | Find groups in the given country where country is a 2 letter country code for the country (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 ). 
    String region = "region_example"; // String | For countries with regions (AU, CA, GB, US), search groups in a specific region as specified by the region abbreviation.  The supported regions and their abbreviations are listed below. <br /><br /> NOTE: The region and postal_code parameters cannot be used at the same time and if both are passed then the postal_code will take priority. <br /><br /> --- <br /><br /> **AU**<br /> - QLD: Queensland<br /> - SA: South Australia<br /> - TAS: Tasmania<br /> - VIC: Victoria<br /> - WA: Western Australia<br /> - NT: Northern Territory<br /> - NSW: New South Wales - ACT<br /> <br /> **CA**<br /> - AB: Alberta<br /> - BC: British Columbia<br /> - MB: Manitoba<br /> - NB: New Brunswick<br /> - NL: Newfoundland and Labrador<br /> - NS: Nova Scotia<br /> - ON: Ontario<br /> - QC: Quebec<br /> - SK: Saskatchewan<br /> - PE: Prince Edward Island<br /> <br /> **GB**<br /> - E: East<br /> - EM: East Midlands<br /> - LDN: London<br /> - NE: North East<br /> - NW: North West<br /> - NI: Northern Ireland<br /> - SC: Scotland<br /> - SE: South East<br /> - SW: South West<br /> - WA: Wales<br /> - WM: West Midlands<br /> - YH: Yorkshire and the Humber<br /> <br /> **US**<br /> All 50 states and the District of Columbia are supported.  For the abbreviations, see: https://github.com/jasonong/List-of-US-States/blob/master/states.csv 
    String postalCode = "postalCode_example"; // String | Find groups in the given postal code.  Only a few countries support postal code searches (US, CA, AU, GB).  The country parameter must be passed when the postal_code parameter is set. <br /><br /> NOTE: The region and postal_code parameters cannot be used at the same time and if both are passed then the postal_code will take priority. 
    Integer page = 1; // Integer | The page of groups to return.
    Integer perPage = 20; // Integer | The number of groups to return per page (must be >= 1 and <= 100).
    try {
      SearchGroups200Response result = apiInstance.searchGroups(name, latitude, longitude, distance, country, region, postalCode, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#searchGroups");
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
| **name** | **String**| Find groups that have the given text somewhere in their name (case insensitive). | [optional] |
| **latitude** | **BigDecimal**| Find groups near the given latitude and longitude. | [optional] |
| **longitude** | **BigDecimal**| Find groups near the given latitude and longitude. | [optional] |
| **distance** | **BigDecimal**| When latitude and longitude are passed, distance can optionally be passed to only return groups within a certain distance (in kilometers) from the point specified by the latitude and longitude.  The distance must be &gt; 0 and &lt;&#x3D; 150 and will default to 100.  | [optional] [default to 100] |
| **country** | **String**| Find groups in the given country where country is a 2 letter country code for the country (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 ).  | [optional] |
| **region** | **String**| For countries with regions (AU, CA, GB, US), search groups in a specific region as specified by the region abbreviation.  The supported regions and their abbreviations are listed below. &lt;br /&gt;&lt;br /&gt; NOTE: The region and postal_code parameters cannot be used at the same time and if both are passed then the postal_code will take priority. &lt;br /&gt;&lt;br /&gt; --- &lt;br /&gt;&lt;br /&gt; **AU**&lt;br /&gt; - QLD: Queensland&lt;br /&gt; - SA: South Australia&lt;br /&gt; - TAS: Tasmania&lt;br /&gt; - VIC: Victoria&lt;br /&gt; - WA: Western Australia&lt;br /&gt; - NT: Northern Territory&lt;br /&gt; - NSW: New South Wales - ACT&lt;br /&gt; &lt;br /&gt; **CA**&lt;br /&gt; - AB: Alberta&lt;br /&gt; - BC: British Columbia&lt;br /&gt; - MB: Manitoba&lt;br /&gt; - NB: New Brunswick&lt;br /&gt; - NL: Newfoundland and Labrador&lt;br /&gt; - NS: Nova Scotia&lt;br /&gt; - ON: Ontario&lt;br /&gt; - QC: Quebec&lt;br /&gt; - SK: Saskatchewan&lt;br /&gt; - PE: Prince Edward Island&lt;br /&gt; &lt;br /&gt; **GB**&lt;br /&gt; - E: East&lt;br /&gt; - EM: East Midlands&lt;br /&gt; - LDN: London&lt;br /&gt; - NE: North East&lt;br /&gt; - NW: North West&lt;br /&gt; - NI: Northern Ireland&lt;br /&gt; - SC: Scotland&lt;br /&gt; - SE: South East&lt;br /&gt; - SW: South West&lt;br /&gt; - WA: Wales&lt;br /&gt; - WM: West Midlands&lt;br /&gt; - YH: Yorkshire and the Humber&lt;br /&gt; &lt;br /&gt; **US**&lt;br /&gt; All 50 states and the District of Columbia are supported.  For the abbreviations, see: https://github.com/jasonong/List-of-US-States/blob/master/states.csv  | [optional] |
| **postalCode** | **String**| Find groups in the given postal code.  Only a few countries support postal code searches (US, CA, AU, GB).  The country parameter must be passed when the postal_code parameter is set. &lt;br /&gt;&lt;br /&gt; NOTE: The region and postal_code parameters cannot be used at the same time and if both are passed then the postal_code will take priority.  | [optional] |
| **page** | **Integer**| The page of groups to return. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of groups to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100). | [optional] [default to 20] |

### Return type

[**SearchGroups200Response**](SearchGroups200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The groups and paging data. |  -  |
| **400** | Missing or invalid parameters. |  -  |

