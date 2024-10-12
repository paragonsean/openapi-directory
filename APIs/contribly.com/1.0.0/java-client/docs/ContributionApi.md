# ContributionApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contributionRefinementTypesGet**](ContributionApi.md#contributionRefinementTypesGet) | **GET** /contribution-refinement-types | List valid contribution refinement types |
| [**contributionRefinementsGet**](ContributionApi.md#contributionRefinementsGet) | **GET** /contribution-refinements | List contribution refinement options |
| [**contributionsGet**](ContributionApi.md#contributionsGet) | **GET** /contributions | List contributions |
| [**contributionsIdDelete**](ContributionApi.md#contributionsIdDelete) | **DELETE** /contributions/{id} | Delete this contribution |
| [**contributionsIdFlagPost**](ContributionApi.md#contributionsIdFlagPost) | **POST** /contributions/{id}/flag | Raise a flag against this contribution |
| [**contributionsIdGet**](ContributionApi.md#contributionsIdGet) | **GET** /contributions/{id} | Get a single contribution by id |
| [**contributionsIdLikePost**](ContributionApi.md#contributionsIdLikePost) | **POST** /contributions/{id}/like | Allows a user to mark a contribution as liked |
| [**contributionsIdLikesGet**](ContributionApi.md#contributionsIdLikesGet) | **GET** /contributions/{id}/likes | List users who have liked this contributions |
| [**contributionsIdModeratePost**](ContributionApi.md#contributionsIdModeratePost) | **POST** /contributions/{id}/moderate | Perform a moderation action on this contribution |
| [**contributionsPost**](ContributionApi.md#contributionsPost) | **POST** /contributions | Create a new contribution |
| [**exportPost**](ContributionApi.md#exportPost) | **POST** /export | Export contributions. |
| [**exportSummaryPost**](ContributionApi.md#exportSummaryPost) | **POST** /export-summary | Export contributions preflight summary. |
| [**exportsIdGet**](ContributionApi.md#exportsIdGet) | **GET** /exports/{id} | Get a single export job; poll to follow export progress. |


<a id="contributionRefinementTypesGet"></a>
# **contributionRefinementTypesGet**
> List&lt;String&gt; contributionRefinementTypesGet()

List valid contribution refinement types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    try {
      List<String> result = apiInstance.contributionRefinementTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionRefinementTypesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of refinement types. These are the possible values of the get contribution refinements parameter. |  -  |

<a id="contributionRefinementsGet"></a>
# **contributionRefinementsGet**
> Map&lt;String, List&lt;String&gt;&gt; contributionRefinementsGet(assignment, country, createdBefore, createdAfter, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user, refinements, refinementSize)

List contribution refinement options

Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String assignment = "assignment_example"; // String | Restrict results to contributions submitted to this assignment.
    String country = "country_example"; // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created before this date time.
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created after this date time.
    String geohash = "geohash_example"; // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    Boolean hasLocation = true; // Boolean | Restrict results to contributions which have a publicly visible location.
    String latLong = "latLong_example"; // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    Double radius = 3.4D; // Double | When limiting result by location with the latLong parameter, specify the radius in kilometers.
    String mediaType = "mediaType_example"; // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
    String ownedBy = "ownedBy_example"; // String | Restrict results to contributions which are fall under the jurisdiction by this user.
    String q = "q_example"; // String | Restrict results to contributions whose headline text matches this keyword.
    String urlWords = "urlWords_example"; // String | Locate a specific contribution by URL words
    String user = "user_example"; // String | Restrict results to contributions by this user identified by id.
    String refinements = "refinements_example"; // String | Comma seperated list of refinement names.
    BigDecimal refinementSize = new BigDecimal(78); // BigDecimal | Number of refinement options to return.
    try {
      Map<String, List<String>> result = apiInstance.contributionRefinementsGet(assignment, country, createdBefore, createdAfter, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user, refinements, refinementSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionRefinementsGet");
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
| **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] |
| **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] |
| **createdBefore** | **OffsetDateTime**| Limit results to contributions created before this date time. | [optional] |
| **createdAfter** | **OffsetDateTime**| Limit results to contributions created after this date time. | [optional] |
| **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] |
| **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] |
| **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] |
| **radius** | **Double**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] |
| **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] |
| **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] |
| **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] |
| **urlWords** | **String**| Locate a specific contribution by URL words | [optional] |
| **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] |
| **refinements** | **String**| Comma seperated list of refinement names. | [optional] |
| **refinementSize** | **BigDecimal**| Number of refinement options to return. | [optional] |

### Return type

[**Map&lt;String, List&lt;String&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A map of refinement names to lists of options |  -  |

<a id="contributionsGet"></a>
# **contributionsGet**
> List&lt;Contribution&gt; contributionsGet(assignment, country, createdBefore, createdAfter, createdDay, createdMonth, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user, ids, format)

List contributions

Retrieve contributions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String assignment = "assignment_example"; // String | Restrict results to contributions submitted to this assignment.
    String country = "country_example"; // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created before this date time.
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created after this date time.
    LocalDate createdDay = LocalDate.now(); // LocalDate | Limit results to contributions created on this day.
    String createdMonth = "createdMonth_example"; // String | Limit results to contributions created during this month.
    String geohash = "geohash_example"; // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    Boolean hasLocation = true; // Boolean | Restrict results to contributions which have a publicly visible location.
    String latLong = "latLong_example"; // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    Double radius = 3.4D; // Double | When limiting result by location with the latLong parameter, specify the radius in kilometers.
    String mediaType = "mediaType_example"; // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
    String ownedBy = "ownedBy_example"; // String | Restrict results to contributions which are fall under the jurisdiction by this user.
    String q = "q_example"; // String | Restrict results to contributions whose headline text matches this keyword.
    String urlWords = "urlWords_example"; // String | Locate a specific contribution by URL words
    String user = "user_example"; // String | Restrict results to contributions by this user identified by id.
    String ids = "ids_example"; // String | Restrict results to a list of specific contributions identified by a comma seperated list of ids.
    String format = "format_example"; // String | Select output format. 'json' or 'rss'. Defaults to JSON.
    try {
      List<Contribution> result = apiInstance.contributionsGet(assignment, country, createdBefore, createdAfter, createdDay, createdMonth, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user, ids, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsGet");
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
| **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] |
| **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] |
| **createdBefore** | **OffsetDateTime**| Limit results to contributions created before this date time. | [optional] |
| **createdAfter** | **OffsetDateTime**| Limit results to contributions created after this date time. | [optional] |
| **createdDay** | **LocalDate**| Limit results to contributions created on this day. | [optional] |
| **createdMonth** | **String**| Limit results to contributions created during this month. | [optional] |
| **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] |
| **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] |
| **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] |
| **radius** | **Double**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] |
| **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] |
| **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] |
| **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] |
| **urlWords** | **String**| Locate a specific contribution by URL words | [optional] |
| **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] |
| **ids** | **String**| Restrict results to a list of specific contributions identified by a comma seperated list of ids. | [optional] |
| **format** | **String**| Select output format. &#39;json&#39; or &#39;rss&#39;. Defaults to JSON. | [optional] |

### Return type

[**List&lt;Contribution&gt;**](Contribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of contributions |  -  |

<a id="contributionsIdDelete"></a>
# **contributionsIdDelete**
> Contribution contributionsIdDelete(id)

Delete this contribution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution to delete
    try {
      Contribution result = apiInstance.contributionsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsIdDelete");
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
| **id** | **String**| Id of the contribution to delete | |

### Return type

[**Contribution**](Contribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deletion request has been accepted and will be processed in the background. |  -  |
| **403** | The currently authorised user is not allowed to delete this contribution. |  -  |
| **404** | Not found |  -  |

<a id="contributionsIdFlagPost"></a>
# **contributionsIdFlagPost**
> Flag contributionsIdFlagPost(id, flag)

Raise a flag against this contribution

Allows end users to bring potential issues with publicly visible content to the attention of moderators.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution to flag
    Flag flag = new Flag(); // Flag | Flag to be created
    try {
      Flag result = apiInstance.contributionsIdFlagPost(id, flag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsIdFlagPost");
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
| **id** | **String**| Id of the contribution to flag | |
| **flag** | [**Flag**](Flag.md)| Flag to be created | |

### Return type

[**Flag**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flag created |  -  |

<a id="contributionsIdGet"></a>
# **contributionsIdGet**
> Contribution contributionsIdGet(id)

Get a single contribution by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution to return
    try {
      Contribution result = apiInstance.contributionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsIdGet");
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
| **id** | **String**| Id of the contribution to return | |

### Return type

[**Contribution**](Contribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **404** | Not found |  -  |

<a id="contributionsIdLikePost"></a>
# **contributionsIdLikePost**
> BigDecimal contributionsIdLikePost(id)

Allows a user to mark a contribution as liked

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution
    try {
      BigDecimal result = apiInstance.contributionsIdLikePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsIdLikePost");
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
| **id** | **String**| Id of the contribution | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated like count for this contribution. |  -  |

<a id="contributionsIdLikesGet"></a>
# **contributionsIdLikesGet**
> List&lt;String&gt; contributionsIdLikesGet(id)

List users who have liked this contributions

Returns a list of user ids of users who have liked this conribution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution
    try {
      List<String> result = apiInstance.contributionsIdLikesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsIdLikesGet");
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
| **id** | **String**| Id of the contribution | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of user ids. |  -  |

<a id="contributionsIdModeratePost"></a>
# **contributionsIdModeratePost**
> String contributionsIdModeratePost(id, moderationHistoryItemSubmission)

Perform a moderation action on this contribution

Allows the contribution to approved of rejected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the contribution to moderate
    ModerationHistoryItemSubmission moderationHistoryItemSubmission = new ModerationHistoryItemSubmission(); // ModerationHistoryItemSubmission | A moderation action
    try {
      String result = apiInstance.contributionsIdModeratePost(id, moderationHistoryItemSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsIdModeratePost");
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
| **id** | **String**| Id of the contribution to moderate | |
| **moderationHistoryItemSubmission** | [**ModerationHistoryItemSubmission**](ModerationHistoryItemSubmission.md)| A moderation action | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The moderation action was successfully applied |  -  |
| **400** | The submission falied to validate. Check the response body for details. |  -  |
| **401** | The request was not correctly authorised. |  -  |
| **403** | You do not have permission to perform this moderation action. |  -  |
| **500** | An unexpected error occurred. |  -  |

<a id="contributionsPost"></a>
# **contributionsPost**
> Contribution contributionsPost(contribution)

Create a new contribution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    Contribution contribution = new Contribution(); // Contribution | Contribution object to be created
    try {
      Contribution result = apiInstance.contributionsPost(contribution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#contributionsPost");
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
| **contribution** | [**Contribution**](Contribution.md)| Contribution object to be created | |

### Return type

[**Contribution**](Contribution.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contribution created |  -  |

<a id="exportPost"></a>
# **exportPost**
> Export exportPost(assignment, country, createdBefore, createdAfter, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user, tagged, combined, individual, format, json)

Export contributions.

Begin an export job. Returns a export job which can be polled to follow the progress of an export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String assignment = "assignment_example"; // String | Restrict results to contributions submitted to this assignment.
    String country = "country_example"; // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created before this date time.
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created after this date time.
    String geohash = "geohash_example"; // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    Boolean hasLocation = true; // Boolean | Restrict results to contributions which have a publicly visible location.
    String latLong = "latLong_example"; // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    Double radius = 3.4D; // Double | When limiting result by location with the latLong parameter, specify the radius in kilometers.
    String mediaType = "mediaType_example"; // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
    String ownedBy = "ownedBy_example"; // String | Restrict results to contributions which are fall under the jurisdiction by this user.
    String q = "q_example"; // String | Restrict results to contributions whose headline text matches this keyword.
    String urlWords = "urlWords_example"; // String | Locate a specific contribution by URL words
    String user = "user_example"; // String | Restrict results to contributions by this user identified by id.
    Boolean tagged = true; // Boolean | Should exported media files be tagged with metadata. Deprecated; use format instead.
    Boolean combined = true; // Boolean | Included a combined file with all contribution text.
    Boolean individual = true; // Boolean | Include individual text files for each contribution.
    String format = "format_example"; // String | Media format to export; none, fullsize, tagged or original.
    Boolean json = true; // Boolean | Include raw JSON for each contribution.
    try {
      Export result = apiInstance.exportPost(assignment, country, createdBefore, createdAfter, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user, tagged, combined, individual, format, json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#exportPost");
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
| **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] |
| **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] |
| **createdBefore** | **OffsetDateTime**| Limit results to contributions created before this date time. | [optional] |
| **createdAfter** | **OffsetDateTime**| Limit results to contributions created after this date time. | [optional] |
| **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] |
| **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] |
| **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] |
| **radius** | **Double**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] |
| **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] |
| **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] |
| **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] |
| **urlWords** | **String**| Locate a specific contribution by URL words | [optional] |
| **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] |
| **tagged** | **Boolean**| Should exported media files be tagged with metadata. Deprecated; use format instead. | [optional] |
| **combined** | **Boolean**| Included a combined file with all contribution text. | [optional] |
| **individual** | **Boolean**| Include individual text files for each contribution. | [optional] |
| **format** | **String**| Media format to export; none, fullsize, tagged or original. | [optional] |
| **json** | **Boolean**| Include raw JSON for each contribution. | [optional] |

### Return type

[**Export**](Export.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | An export job describing the state of an export job. |  -  |

<a id="exportSummaryPost"></a>
# **exportSummaryPost**
> ExportSummary exportSummaryPost(assignment, country, createdBefore, createdAfter, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user)

Export contributions preflight summary.

Provide a preflight summary of an export request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String assignment = "assignment_example"; // String | Restrict results to contributions submitted to this assignment.
    String country = "country_example"; // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created before this date time.
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to contributions created after this date time.
    String geohash = "geohash_example"; // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
    Boolean hasLocation = true; // Boolean | Restrict results to contributions which have a publicly visible location.
    String latLong = "latLong_example"; // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
    Double radius = 3.4D; // Double | When limiting result by location with the latLong parameter, specify the radius in kilometers.
    String mediaType = "mediaType_example"; // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
    String ownedBy = "ownedBy_example"; // String | Restrict results to contributions which are fall under the jurisdiction by this user.
    String q = "q_example"; // String | Restrict results to contributions whose headline text matches this keyword.
    String urlWords = "urlWords_example"; // String | Locate a specific contribution by URL words
    String user = "user_example"; // String | Restrict results to contributions by this user identified by id.
    try {
      ExportSummary result = apiInstance.exportSummaryPost(assignment, country, createdBefore, createdAfter, geohash, hasLocation, latLong, radius, mediaType, ownedBy, q, urlWords, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#exportSummaryPost");
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
| **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] |
| **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] |
| **createdBefore** | **OffsetDateTime**| Limit results to contributions created before this date time. | [optional] |
| **createdAfter** | **OffsetDateTime**| Limit results to contributions created after this date time. | [optional] |
| **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] |
| **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] |
| **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] |
| **radius** | **Double**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] |
| **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] |
| **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] |
| **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] |
| **urlWords** | **String**| Locate a specific contribution by URL words | [optional] |
| **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] |

### Return type

[**ExportSummary**](ExportSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A summary of the number of contributions, media files and approximate total size of media files. |  -  |

<a id="exportsIdGet"></a>
# **exportsIdGet**
> Export exportsIdGet(id)

Get a single export job; poll to follow export progress.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    ContributionApi apiInstance = new ContributionApi(defaultClient);
    String id = "id_example"; // String | Id of the export job to return
    try {
      Export result = apiInstance.exportsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributionApi#exportsIdGet");
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
| **id** | **String**| Id of the export job to return | |

### Return type

[**Export**](Export.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **404** | Not found |  -  |

