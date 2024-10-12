# PlacementGroupsApi

All URIs are relative to *https://dfareporting.googleapis.com/dfareporting/v3.3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dfareportingPlacementGroupsGet**](PlacementGroupsApi.md#dfareportingPlacementGroupsGet) | **GET** /userprofiles/{profileId}/placementGroups/{id} |  |
| [**dfareportingPlacementGroupsInsert**](PlacementGroupsApi.md#dfareportingPlacementGroupsInsert) | **POST** /userprofiles/{profileId}/placementGroups |  |
| [**dfareportingPlacementGroupsList**](PlacementGroupsApi.md#dfareportingPlacementGroupsList) | **GET** /userprofiles/{profileId}/placementGroups |  |
| [**dfareportingPlacementGroupsPatch**](PlacementGroupsApi.md#dfareportingPlacementGroupsPatch) | **PATCH** /userprofiles/{profileId}/placementGroups |  |
| [**dfareportingPlacementGroupsUpdate**](PlacementGroupsApi.md#dfareportingPlacementGroupsUpdate) | **PUT** /userprofiles/{profileId}/placementGroups |  |


<a id="dfareportingPlacementGroupsGet"></a>
# **dfareportingPlacementGroupsGet**
> PlacementGroup dfareportingPlacementGroupsGet(profileId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets one placement group by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String id = "id_example"; // String | Placement group ID.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    try {
      PlacementGroup result = apiInstance.dfareportingPlacementGroupsGet(profileId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#dfareportingPlacementGroupsGet");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **id** | **String**| Placement group ID. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dfareportingPlacementGroupsInsert"></a>
# **dfareportingPlacementGroupsInsert**
> PlacementGroup dfareportingPlacementGroupsInsert(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, placementGroup)



Inserts a new placement group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    PlacementGroup placementGroup = new PlacementGroup(); // PlacementGroup | 
    try {
      PlacementGroup result = apiInstance.dfareportingPlacementGroupsInsert(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, placementGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#dfareportingPlacementGroupsInsert");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **placementGroup** | [**PlacementGroup**](PlacementGroup.md)|  | [optional] |

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dfareportingPlacementGroupsList"></a>
# **dfareportingPlacementGroupsList**
> PlacementGroupsListResponse dfareportingPlacementGroupsList(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserIds, archived, campaignIds, contentCategoryIds, directorySiteIds, ids, maxEndDate, maxResults, maxStartDate, minEndDate, minStartDate, pageToken, placementGroupType, placementStrategyIds, pricingTypes, searchString, siteIds, sortField, sortOrder)



Retrieves a list of placement groups, possibly filtered. This method supports paging.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> advertiserIds = Arrays.asList(); // List<String> | Select only placement groups that belong to these advertisers.
    Boolean archived = true; // Boolean | Select only archived placements. Don't set this field to select both archived and non-archived placements.
    List<String> campaignIds = Arrays.asList(); // List<String> | Select only placement groups that belong to these campaigns.
    List<String> contentCategoryIds = Arrays.asList(); // List<String> | Select only placement groups that are associated with these content categories.
    List<String> directorySiteIds = Arrays.asList(); // List<String> | Select only placement groups that are associated with these directory sites.
    List<String> ids = Arrays.asList(); // List<String> | Select only placement groups with these IDs.
    String maxEndDate = "maxEndDate_example"; // String | Select only placements or placement groups whose end date is on or before the specified maxEndDate. The date should be formatted as \"yyyy-MM-dd\".
    Integer maxResults = 56; // Integer | Maximum number of results to return.
    String maxStartDate = "maxStartDate_example"; // String | Select only placements or placement groups whose start date is on or before the specified maxStartDate. The date should be formatted as \"yyyy-MM-dd\".
    String minEndDate = "minEndDate_example"; // String | Select only placements or placement groups whose end date is on or after the specified minEndDate. The date should be formatted as \"yyyy-MM-dd\".
    String minStartDate = "minStartDate_example"; // String | Select only placements or placement groups whose start date is on or after the specified minStartDate. The date should be formatted as \"yyyy-MM-dd\".
    String pageToken = "pageToken_example"; // String | Value of the nextPageToken from the previous result page.
    String placementGroupType = "PLACEMENT_PACKAGE"; // String | Select only placement groups belonging with this group type. A package is a simple group of placements that acts as a single pricing point for a group of tags. A roadblock is a group of placements that not only acts as a single pricing point but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned placements to be marked as primary for reporting.
    List<String> placementStrategyIds = Arrays.asList(); // List<String> | Select only placement groups that are associated with these placement strategies.
    List<String> pricingTypes = Arrays.asList(); // List<String> | Select only placement groups with these pricing types.
    String searchString = "searchString_example"; // String | Allows searching for placement groups by name or ID. Wildcards (*) are allowed. For example, \"placement*2015\" will return placement groups with names like \"placement group June 2015\", \"placement group May 2015\", or simply \"placements 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"placementgroup\" will match placement groups with name \"my placementgroup\", \"placementgroup 2015\", or simply \"placementgroup\".
    List<String> siteIds = Arrays.asList(); // List<String> | Select only placement groups that are associated with these sites.
    String sortField = "ID"; // String | Field by which to sort the list.
    String sortOrder = "ASCENDING"; // String | Order of sorted results.
    try {
      PlacementGroupsListResponse result = apiInstance.dfareportingPlacementGroupsList(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, advertiserIds, archived, campaignIds, contentCategoryIds, directorySiteIds, ids, maxEndDate, maxResults, maxStartDate, minEndDate, minStartDate, pageToken, placementGroupType, placementStrategyIds, pricingTypes, searchString, siteIds, sortField, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#dfareportingPlacementGroupsList");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **advertiserIds** | [**List&lt;String&gt;**](String.md)| Select only placement groups that belong to these advertisers. | [optional] |
| **archived** | **Boolean**| Select only archived placements. Don&#39;t set this field to select both archived and non-archived placements. | [optional] |
| **campaignIds** | [**List&lt;String&gt;**](String.md)| Select only placement groups that belong to these campaigns. | [optional] |
| **contentCategoryIds** | [**List&lt;String&gt;**](String.md)| Select only placement groups that are associated with these content categories. | [optional] |
| **directorySiteIds** | [**List&lt;String&gt;**](String.md)| Select only placement groups that are associated with these directory sites. | [optional] |
| **ids** | [**List&lt;String&gt;**](String.md)| Select only placement groups with these IDs. | [optional] |
| **maxEndDate** | **String**| Select only placements or placement groups whose end date is on or before the specified maxEndDate. The date should be formatted as \&quot;yyyy-MM-dd\&quot;. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return. | [optional] |
| **maxStartDate** | **String**| Select only placements or placement groups whose start date is on or before the specified maxStartDate. The date should be formatted as \&quot;yyyy-MM-dd\&quot;. | [optional] |
| **minEndDate** | **String**| Select only placements or placement groups whose end date is on or after the specified minEndDate. The date should be formatted as \&quot;yyyy-MM-dd\&quot;. | [optional] |
| **minStartDate** | **String**| Select only placements or placement groups whose start date is on or after the specified minStartDate. The date should be formatted as \&quot;yyyy-MM-dd\&quot;. | [optional] |
| **pageToken** | **String**| Value of the nextPageToken from the previous result page. | [optional] |
| **placementGroupType** | **String**| Select only placement groups belonging with this group type. A package is a simple group of placements that acts as a single pricing point for a group of tags. A roadblock is a group of placements that not only acts as a single pricing point but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned placements to be marked as primary for reporting. | [optional] [enum: PLACEMENT_PACKAGE, PLACEMENT_ROADBLOCK] |
| **placementStrategyIds** | [**List&lt;String&gt;**](String.md)| Select only placement groups that are associated with these placement strategies. | [optional] |
| **pricingTypes** | [**List&lt;String&gt;**](String.md)| Select only placement groups with these pricing types. | [optional] [enum: PRICING_TYPE_CPM, PRICING_TYPE_CPC, PRICING_TYPE_CPA, PRICING_TYPE_FLAT_RATE_IMPRESSIONS, PRICING_TYPE_FLAT_RATE_CLICKS, PRICING_TYPE_CPM_ACTIVEVIEW] |
| **searchString** | **String**| Allows searching for placement groups by name or ID. Wildcards (*) are allowed. For example, \&quot;placement*2015\&quot; will return placement groups with names like \&quot;placement group June 2015\&quot;, \&quot;placement group May 2015\&quot;, or simply \&quot;placements 2015\&quot;. Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \&quot;placementgroup\&quot; will match placement groups with name \&quot;my placementgroup\&quot;, \&quot;placementgroup 2015\&quot;, or simply \&quot;placementgroup\&quot;. | [optional] |
| **siteIds** | [**List&lt;String&gt;**](String.md)| Select only placement groups that are associated with these sites. | [optional] |
| **sortField** | **String**| Field by which to sort the list. | [optional] [enum: ID, NAME] |
| **sortOrder** | **String**| Order of sorted results. | [optional] [enum: ASCENDING, DESCENDING] |

### Return type

[**PlacementGroupsListResponse**](PlacementGroupsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dfareportingPlacementGroupsPatch"></a>
# **dfareportingPlacementGroupsPatch**
> PlacementGroup dfareportingPlacementGroupsPatch(profileId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, placementGroup)



Updates an existing placement group. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String id = "id_example"; // String | PlacementGroup ID.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    PlacementGroup placementGroup = new PlacementGroup(); // PlacementGroup | 
    try {
      PlacementGroup result = apiInstance.dfareportingPlacementGroupsPatch(profileId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, placementGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#dfareportingPlacementGroupsPatch");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **id** | **String**| PlacementGroup ID. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **placementGroup** | [**PlacementGroup**](PlacementGroup.md)|  | [optional] |

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dfareportingPlacementGroupsUpdate"></a>
# **dfareportingPlacementGroupsUpdate**
> PlacementGroup dfareportingPlacementGroupsUpdate(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, placementGroup)



Updates an existing placement group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    PlacementGroup placementGroup = new PlacementGroup(); // PlacementGroup | 
    try {
      PlacementGroup result = apiInstance.dfareportingPlacementGroupsUpdate(profileId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, placementGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#dfareportingPlacementGroupsUpdate");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **placementGroup** | [**PlacementGroup**](PlacementGroup.md)|  | [optional] |

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

