# MembersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMembersHistoryGet**](MembersApi.md#apiMembersHistoryGet) | **GET** /api/Members/History | Return members by ID with list of their historical names, parties and memberships |
| [**apiMembersIdBiographyGet**](MembersApi.md#apiMembersIdBiographyGet) | **GET** /api/Members/{id}/Biography | Return biography of member by ID |
| [**apiMembersIdContactGet**](MembersApi.md#apiMembersIdContactGet) | **GET** /api/Members/{id}/Contact | Return list of contact details of member by ID |
| [**apiMembersIdContributionSummaryGet**](MembersApi.md#apiMembersIdContributionSummaryGet) | **GET** /api/Members/{id}/ContributionSummary | Return contribution summary of member by ID |
| [**apiMembersIdEdmsGet**](MembersApi.md#apiMembersIdEdmsGet) | **GET** /api/Members/{id}/Edms | Return list of early day motions of member by ID |
| [**apiMembersIdExperienceGet**](MembersApi.md#apiMembersIdExperienceGet) | **GET** /api/Members/{id}/Experience | Return experience of member by ID |
| [**apiMembersIdFocusGet**](MembersApi.md#apiMembersIdFocusGet) | **GET** /api/Members/{id}/Focus | Return list of areas of focus of member by ID |
| [**apiMembersIdGet**](MembersApi.md#apiMembersIdGet) | **GET** /api/Members/{id} | Return member by ID |
| [**apiMembersIdLatestElectionResultGet**](MembersApi.md#apiMembersIdLatestElectionResultGet) | **GET** /api/Members/{id}/LatestElectionResult | Return latest election result of member by ID |
| [**apiMembersIdPortraitGet**](MembersApi.md#apiMembersIdPortraitGet) | **GET** /api/Members/{id}/Portrait | Return portrait of member by ID |
| [**apiMembersIdPortraitUrlGet**](MembersApi.md#apiMembersIdPortraitUrlGet) | **GET** /api/Members/{id}/PortraitUrl | Return portrait url of member by ID |
| [**apiMembersIdRegisteredInterestsGet**](MembersApi.md#apiMembersIdRegisteredInterestsGet) | **GET** /api/Members/{id}/RegisteredInterests | Return list of registered interests of member by ID |
| [**apiMembersIdStaffGet**](MembersApi.md#apiMembersIdStaffGet) | **GET** /api/Members/{id}/Staff | Return list of staff of member by ID |
| [**apiMembersIdSynopsisGet**](MembersApi.md#apiMembersIdSynopsisGet) | **GET** /api/Members/{id}/Synopsis | Return synopsis of member by ID |
| [**apiMembersIdThumbnailGet**](MembersApi.md#apiMembersIdThumbnailGet) | **GET** /api/Members/{id}/Thumbnail | Return thumbnail of member by ID |
| [**apiMembersIdThumbnailUrlGet**](MembersApi.md#apiMembersIdThumbnailUrlGet) | **GET** /api/Members/{id}/ThumbnailUrl | Return thumbnail url of member by ID |
| [**apiMembersIdVotingGet**](MembersApi.md#apiMembersIdVotingGet) | **GET** /api/Members/{id}/Voting | Return list of votes by member by ID |
| [**apiMembersIdWrittenQuestionsGet**](MembersApi.md#apiMembersIdWrittenQuestionsGet) | **GET** /api/Members/{id}/WrittenQuestions | Return list of written questions by member by ID |
| [**apiMembersSearchGet**](MembersApi.md#apiMembersSearchGet) | **GET** /api/Members/Search | Returns a list of current members of the Commons or Lords |
| [**apiMembersSearchHistoricalGet**](MembersApi.md#apiMembersSearchHistoricalGet) | **GET** /api/Members/SearchHistorical | Returns a list of members of the Commons or Lords |


<a id="apiMembersHistoryGet"></a>
# **apiMembersHistoryGet**
> List&lt;MemberHistoryItem&gt; apiMembersHistoryGet(ids)

Return members by ID with list of their historical names, parties and memberships

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | List of MemberIds to find
    try {
      List<MemberHistoryItem> result = apiInstance.apiMembersHistoryGet(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersHistoryGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| List of MemberIds to find | [optional] |

### Return type

[**List&lt;MemberHistoryItem&gt;**](MemberHistoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdBiographyGet"></a>
# **apiMembersIdBiographyGet**
> MemberBiographyItem apiMembersIdBiographyGet(id)

Return biography of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Biography of Member by ID specified
    try {
      MemberBiographyItem result = apiInstance.apiMembersIdBiographyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdBiographyGet");
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
| **id** | **Integer**| Biography of Member by ID specified | |

### Return type

[**MemberBiographyItem**](MemberBiographyItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdContactGet"></a>
# **apiMembersIdContactGet**
> ContactInformationListItem apiMembersIdContactGet(id)

Return list of contact details of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Contact details of Member by ID specified
    try {
      ContactInformationListItem result = apiInstance.apiMembersIdContactGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdContactGet");
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
| **id** | **Integer**| Contact details of Member by ID specified | |

### Return type

[**ContactInformationListItem**](ContactInformationListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdContributionSummaryGet"></a>
# **apiMembersIdContributionSummaryGet**
> DebateContributionMembersServiceSearchResult apiMembersIdContributionSummaryGet(id, page)

Return contribution summary of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Contribution summary of Member by ID specified
    Integer page = 56; // Integer | 
    try {
      DebateContributionMembersServiceSearchResult result = apiInstance.apiMembersIdContributionSummaryGet(id, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdContributionSummaryGet");
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
| **id** | **Integer**| Contribution summary of Member by ID specified | |
| **page** | **Integer**|  | [optional] |

### Return type

[**DebateContributionMembersServiceSearchResult**](DebateContributionMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdEdmsGet"></a>
# **apiMembersIdEdmsGet**
> EarlyDayMotionMembersServiceSearchResult apiMembersIdEdmsGet(id, page)

Return list of early day motions of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Early day motions of Member by ID specified
    Integer page = 56; // Integer | 
    try {
      EarlyDayMotionMembersServiceSearchResult result = apiInstance.apiMembersIdEdmsGet(id, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdEdmsGet");
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
| **id** | **Integer**| Early day motions of Member by ID specified | |
| **page** | **Integer**|  | [optional] |

### Return type

[**EarlyDayMotionMembersServiceSearchResult**](EarlyDayMotionMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdExperienceGet"></a>
# **apiMembersIdExperienceGet**
> BiographyExperienceListItem apiMembersIdExperienceGet(id)

Return experience of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Experience of Member by ID specified
    try {
      BiographyExperienceListItem result = apiInstance.apiMembersIdExperienceGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdExperienceGet");
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
| **id** | **Integer**| Experience of Member by ID specified | |

### Return type

[**BiographyExperienceListItem**](BiographyExperienceListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdFocusGet"></a>
# **apiMembersIdFocusGet**
> MemberFocusListItem apiMembersIdFocusGet(id)

Return list of areas of focus of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Areas of focus of Member by ID specified
    try {
      MemberFocusListItem result = apiInstance.apiMembersIdFocusGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdFocusGet");
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
| **id** | **Integer**| Areas of focus of Member by ID specified | |

### Return type

[**MemberFocusListItem**](MemberFocusListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdGet"></a>
# **apiMembersIdGet**
> MemberItem apiMembersIdGet(id, detailsForDate)

Return member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Member by ID specified
    OffsetDateTime detailsForDate = OffsetDateTime.now(); // OffsetDateTime | Member object will be populated with details from the date specified
    try {
      MemberItem result = apiInstance.apiMembersIdGet(id, detailsForDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdGet");
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
| **id** | **Integer**| Member by ID specified | |
| **detailsForDate** | **OffsetDateTime**| Member object will be populated with details from the date specified | [optional] |

### Return type

[**MemberItem**](MemberItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdLatestElectionResultGet"></a>
# **apiMembersIdLatestElectionResultGet**
> ElectionResultItem apiMembersIdLatestElectionResultGet(id)

Return latest election result of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Latest election result of Member by ID specified
    try {
      ElectionResultItem result = apiInstance.apiMembersIdLatestElectionResultGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdLatestElectionResultGet");
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
| **id** | **Integer**| Latest election result of Member by ID specified | |

### Return type

[**ElectionResultItem**](ElectionResultItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdPortraitGet"></a>
# **apiMembersIdPortraitGet**
> apiMembersIdPortraitGet(id, cropType, webVersion)

Return portrait of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Portrait of Member by ID specified
    PortraitCropEnum cropType = PortraitCropEnum.fromValue("0"); // PortraitCropEnum | 
    Boolean webVersion = true; // Boolean | 
    try {
      apiInstance.apiMembersIdPortraitGet(id, cropType, webVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdPortraitGet");
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
| **id** | **Integer**| Portrait of Member by ID specified | |
| **cropType** | [**PortraitCropEnum**](.md)|  | [optional] [enum: 0, 1, 2, 3] |
| **webVersion** | **Boolean**|  | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdPortraitUrlGet"></a>
# **apiMembersIdPortraitUrlGet**
> StringItem apiMembersIdPortraitUrlGet(id)

Return portrait url of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Portrait url of Member by ID specified
    try {
      StringItem result = apiInstance.apiMembersIdPortraitUrlGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdPortraitUrlGet");
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
| **id** | **Integer**| Portrait url of Member by ID specified | |

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdRegisteredInterestsGet"></a>
# **apiMembersIdRegisteredInterestsGet**
> RegisteredInterestCategoryListItem apiMembersIdRegisteredInterestsGet(id, house)

Return list of registered interests of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Registered interests of Member by ID specified
    House house = House.fromValue("1"); // House | Registered interests of Member by House specified
    try {
      RegisteredInterestCategoryListItem result = apiInstance.apiMembersIdRegisteredInterestsGet(id, house);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdRegisteredInterestsGet");
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
| **id** | **Integer**| Registered interests of Member by ID specified | |
| **house** | [**House**](.md)| Registered interests of Member by House specified | [optional] [enum: 1, 2] |

### Return type

[**RegisteredInterestCategoryListItem**](RegisteredInterestCategoryListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdStaffGet"></a>
# **apiMembersIdStaffGet**
> StaffListItem apiMembersIdStaffGet(id)

Return list of staff of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Staff of Member by ID specified
    try {
      StaffListItem result = apiInstance.apiMembersIdStaffGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdStaffGet");
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
| **id** | **Integer**| Staff of Member by ID specified | |

### Return type

[**StaffListItem**](StaffListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdSynopsisGet"></a>
# **apiMembersIdSynopsisGet**
> StringItem apiMembersIdSynopsisGet(id)

Return synopsis of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Synopsis of Member by ID specified
    try {
      StringItem result = apiInstance.apiMembersIdSynopsisGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdSynopsisGet");
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
| **id** | **Integer**| Synopsis of Member by ID specified | |

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdThumbnailGet"></a>
# **apiMembersIdThumbnailGet**
> apiMembersIdThumbnailGet(id)

Return thumbnail of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Thumbnail of Member by ID specified
    try {
      apiInstance.apiMembersIdThumbnailGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdThumbnailGet");
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
| **id** | **Integer**| Thumbnail of Member by ID specified | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdThumbnailUrlGet"></a>
# **apiMembersIdThumbnailUrlGet**
> StringItem apiMembersIdThumbnailUrlGet(id)

Return thumbnail url of member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Thumbnail url of Member by ID specified
    try {
      StringItem result = apiInstance.apiMembersIdThumbnailUrlGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdThumbnailUrlGet");
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
| **id** | **Integer**| Thumbnail url of Member by ID specified | |

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdVotingGet"></a>
# **apiMembersIdVotingGet**
> VoteMembersServiceSearchResult apiMembersIdVotingGet(id, house, page)

Return list of votes by member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Votes by Member by ID specified
    House house = House.fromValue("1"); // House | 
    Integer page = 56; // Integer | 
    try {
      VoteMembersServiceSearchResult result = apiInstance.apiMembersIdVotingGet(id, house, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdVotingGet");
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
| **id** | **Integer**| Votes by Member by ID specified | |
| **house** | [**House**](.md)|  | [enum: 1, 2] |
| **page** | **Integer**|  | [optional] |

### Return type

[**VoteMembersServiceSearchResult**](VoteMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersIdWrittenQuestionsGet"></a>
# **apiMembersIdWrittenQuestionsGet**
> WrittenQuestionMembersServiceSearchResult apiMembersIdWrittenQuestionsGet(id, page)

Return list of written questions by member by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    Integer id = 56; // Integer | Written questions by Member by ID specified
    Integer page = 56; // Integer | 
    try {
      WrittenQuestionMembersServiceSearchResult result = apiInstance.apiMembersIdWrittenQuestionsGet(id, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersIdWrittenQuestionsGet");
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
| **id** | **Integer**| Written questions by Member by ID specified | |
| **page** | **Integer**|  | [optional] |

### Return type

[**WrittenQuestionMembersServiceSearchResult**](WrittenQuestionMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiMembersSearchGet"></a>
# **apiMembersSearchGet**
> MemberMembersServiceSearchResult apiMembersSearchGet(name, location, postTitle, partyId, house, constituencyId, nameStartsWith, gender, membershipStartedSince, membershipEndedMembershipEndedSince, membershipEndedMembershipEndReasonIds, membershipInDateRangeWasMemberOnOrAfter, membershipInDateRangeWasMemberOnOrBefore, membershipInDateRangeWasMemberOfHouse, isEligible, isCurrentMember, policyInterestId, experience, skip, take)

Returns a list of current members of the Commons or Lords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String name = "name_example"; // String | Members where name contains term specified
    String location = "location_example"; // String | Members where postcode or geographical location matches the term specified
    String postTitle = "postTitle_example"; // String | Members which have held the post specified
    Integer partyId = 56; // Integer | Members which are currently affiliated with party with party ID
    House house = House.fromValue("1"); // House | Members where their most recent house is the house specified
    Integer constituencyId = 56; // Integer | Members which currently hold the constituency with constituency id
    String nameStartsWith = "nameStartsWith_example"; // String | Members with surname begining with letter(s) specified
    String gender = "gender_example"; // String | Members with the gender specified
    OffsetDateTime membershipStartedSince = OffsetDateTime.now(); // OffsetDateTime | Members who started on or after the date given
    OffsetDateTime membershipEndedMembershipEndedSince = OffsetDateTime.now(); // OffsetDateTime | Members who left the House on or after the date given
    List<Integer> membershipEndedMembershipEndReasonIds = Arrays.asList(); // List<Integer> | 
    OffsetDateTime membershipInDateRangeWasMemberOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | Members who were active on or after the date specified
    OffsetDateTime membershipInDateRangeWasMemberOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | Members who were active on or before the date specified
    House membershipInDateRangeWasMemberOfHouse = House.fromValue("1"); // House | Members who were active in the house specifid
    Boolean isEligible = true; // Boolean | Members currently Eligible to sit in their House
    Boolean isCurrentMember = true; // Boolean | Members who are current or former members
    Integer policyInterestId = 56; // Integer | Members with specified policy interest
    String experience = "experience_example"; // String | Members with specified experience
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0
    Integer take = 20; // Integer | The number of records to return, default is 20. Maximum is 20
    try {
      MemberMembersServiceSearchResult result = apiInstance.apiMembersSearchGet(name, location, postTitle, partyId, house, constituencyId, nameStartsWith, gender, membershipStartedSince, membershipEndedMembershipEndedSince, membershipEndedMembershipEndReasonIds, membershipInDateRangeWasMemberOnOrAfter, membershipInDateRangeWasMemberOnOrBefore, membershipInDateRangeWasMemberOfHouse, isEligible, isCurrentMember, policyInterestId, experience, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersSearchGet");
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
| **name** | **String**| Members where name contains term specified | [optional] |
| **location** | **String**| Members where postcode or geographical location matches the term specified | [optional] |
| **postTitle** | **String**| Members which have held the post specified | [optional] |
| **partyId** | **Integer**| Members which are currently affiliated with party with party ID | [optional] |
| **house** | [**House**](.md)| Members where their most recent house is the house specified | [optional] [enum: 1, 2] |
| **constituencyId** | **Integer**| Members which currently hold the constituency with constituency id | [optional] |
| **nameStartsWith** | **String**| Members with surname begining with letter(s) specified | [optional] |
| **gender** | **String**| Members with the gender specified | [optional] |
| **membershipStartedSince** | **OffsetDateTime**| Members who started on or after the date given | [optional] |
| **membershipEndedMembershipEndedSince** | **OffsetDateTime**| Members who left the House on or after the date given | [optional] |
| **membershipEndedMembershipEndReasonIds** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **membershipInDateRangeWasMemberOnOrAfter** | **OffsetDateTime**| Members who were active on or after the date specified | [optional] |
| **membershipInDateRangeWasMemberOnOrBefore** | **OffsetDateTime**| Members who were active on or before the date specified | [optional] |
| **membershipInDateRangeWasMemberOfHouse** | [**House**](.md)| Members who were active in the house specifid | [optional] [enum: 1, 2] |
| **isEligible** | **Boolean**| Members currently Eligible to sit in their House | [optional] |
| **isCurrentMember** | **Boolean**| Members who are current or former members | [optional] |
| **policyInterestId** | **Integer**| Members with specified policy interest | [optional] |
| **experience** | **String**| Members with specified experience | [optional] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0 | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20. Maximum is 20 | [optional] [default to 20] |

### Return type

[**MemberMembersServiceSearchResult**](MemberMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiMembersSearchHistoricalGet"></a>
# **apiMembersSearchHistoricalGet**
> MemberMembersServiceSearchResult apiMembersSearchHistoricalGet(name, dateToSearchFor, skip, take)

Returns a list of members of the Commons or Lords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String name = "name_example"; // String | Members with names containing the term specified
    OffsetDateTime dateToSearchFor = OffsetDateTime.now(); // OffsetDateTime | Members that were an active member of the Commons or Lords on the date specified
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0
    Integer take = 20; // Integer | The number of records to return, default is 20. Maximum is 20
    try {
      MemberMembersServiceSearchResult result = apiInstance.apiMembersSearchHistoricalGet(name, dateToSearchFor, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#apiMembersSearchHistoricalGet");
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
| **name** | **String**| Members with names containing the term specified | [optional] |
| **dateToSearchFor** | **OffsetDateTime**| Members that were an active member of the Commons or Lords on the date specified | [optional] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0 | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20. Maximum is 20 | [optional] [default to 20] |

### Return type

[**MemberMembersServiceSearchResult**](MemberMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

