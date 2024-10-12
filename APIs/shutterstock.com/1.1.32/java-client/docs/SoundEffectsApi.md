# SoundEffectsApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadSfx**](SoundEffectsApi.md#downloadSfx) | **POST** /v2/sfx/licenses/{id}/downloads | Download sound effects |
| [**getSfxDetails**](SoundEffectsApi.md#getSfxDetails) | **GET** /v2/sfx/{id} | Get details about sound effects |
| [**getSfxLicenseList**](SoundEffectsApi.md#getSfxLicenseList) | **GET** /v2/sfx/licenses | List sound effects licenses |
| [**getSfxListDetails**](SoundEffectsApi.md#getSfxListDetails) | **GET** /v2/sfx | List details about sound effects |
| [**licensesSFX**](SoundEffectsApi.md#licensesSFX) | **POST** /v2/sfx/licenses | License sound effects |
| [**searchSFX**](SoundEffectsApi.md#searchSFX) | **GET** /v2/sfx/search | Search for sound effects |


<a id="downloadSfx"></a>
# **downloadSfx**
> SfxUrl downloadSfx(id)

Download sound effects

This endpoint redownloads sound effects that you have already received a license for. The download links in the response are valid for 8 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    SoundEffectsApi apiInstance = new SoundEffectsApi(defaultClient);
    String id = "123"; // String | License ID
    try {
      SfxUrl result = apiInstance.downloadSfx(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundEffectsApi#downloadSfx");
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
| **id** | **String**| License ID | |

### Return type

[**SfxUrl**](SfxUrl.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getSfxDetails"></a>
# **getSfxDetails**
> SFX getSfxDetails(id, language, view, library, searchId)

Get details about sound effects

This endpoint shows information about a sound effect.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SoundEffectsApi apiInstance = new SoundEffectsApi(defaultClient);
    Integer id = 442583; // Integer | Audio track ID
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    String view = "minimal"; // String | Amount of detail to render in the response
    String library = "shutterstock"; // String | Which library to fetch from
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      SFX result = apiInstance.getSfxDetails(id, language, view, library, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundEffectsApi#getSfxDetails");
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
| **id** | **Integer**| Audio track ID | |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **library** | **String**| Which library to fetch from | [optional] [enum: shutterstock, premier, premiumbeat] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**SFX**](SFX.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **503** | Service Unavailable |  -  |

<a id="getSfxLicenseList"></a>
# **getSfxLicenseList**
> DownloadHistoryDataList getSfxLicenseList(sfxId, license, page, perPage, sort, username, startDate, endDate, licenseId, downloadAvailability, teamHistory)

List sound effects licenses

This endpoint lists existing licenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    SoundEffectsApi apiInstance = new SoundEffectsApi(defaultClient);
    String sfxId = "12345678"; // String | Show licenses for the specified sound effects ID
    String license = "standard"; // String | Show sound effects that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    String username = "aUniqueUsername"; // String | Filter licenses by username of licensee
    OffsetDateTime startDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created on or after the specified date
    OffsetDateTime endDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created before the specified date
    String licenseId = "licenseId_example"; // String | Filter by the license ID
    String downloadAvailability = "all"; // String | Filter licenses by download availability
    Boolean teamHistory = false; // Boolean | Set to true to see license history for all members of your team.
    try {
      DownloadHistoryDataList result = apiInstance.getSfxLicenseList(sfxId, license, page, perPage, sort, username, startDate, endDate, licenseId, downloadAvailability, teamHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundEffectsApi#getSfxLicenseList");
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
| **sfxId** | **String**| Show licenses for the specified sound effects ID | [optional] |
| **license** | **String**| Show sound effects that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort order | [optional] [default to newest] [enum: newest, oldest] |
| **username** | **String**| Filter licenses by username of licensee | [optional] |
| **startDate** | **OffsetDateTime**| Show licenses created on or after the specified date | [optional] |
| **endDate** | **OffsetDateTime**| Show licenses created before the specified date | [optional] |
| **licenseId** | **String**| Filter by the license ID | [optional] |
| **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to all] [enum: all, downloadable, non_downloadable] |
| **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false] |

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getSfxListDetails"></a>
# **getSfxListDetails**
> SFXDataList getSfxListDetails(id, view, language, library, searchId)

List details about sound effects

This endpoint shows information about sound effects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SoundEffectsApi apiInstance = new SoundEffectsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | One or more sound effect IDs
    String view = "minimal"; // String | Amount of detail to render in the response
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    String library = "shutterstock"; // String | Which library to fetch from
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      SFXDataList result = apiInstance.getSfxListDetails(id, view, language, library, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundEffectsApi#getSfxListDetails");
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
| **id** | [**List&lt;String&gt;**](String.md)| One or more sound effect IDs | |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **library** | **String**| Which library to fetch from | [optional] [enum: shutterstock, premier, premiumbeat] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**SFXDataList**](SFXDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="licensesSFX"></a>
# **licensesSFX**
> LicenseSFXResultDataList licensesSFX(licenseSFXRequest)

License sound effects

This endpoint licenses sounds effect assets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SoundEffectsApi apiInstance = new SoundEffectsApi(defaultClient);
    LicenseSFXRequest licenseSFXRequest = new LicenseSFXRequest(); // LicenseSFXRequest | 
    try {
      LicenseSFXResultDataList result = apiInstance.licensesSFX(licenseSFXRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundEffectsApi#licensesSFX");
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
| **licenseSFXRequest** | [**LicenseSFXRequest**](LicenseSFXRequest.md)|  | |

### Return type

[**LicenseSFXResultDataList**](LicenseSFXResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="searchSFX"></a>
# **searchSFX**
> SFXSearchResults searchSFX(addedDate, addedDateStart, addedDateEnd, duration, durationFrom, durationTo, page, perPage, query, safe, sort, view, language)

Search for sound effects

This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND condition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoundEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    SoundEffectsApi apiInstance = new SoundEffectsApi(defaultClient);
    LocalDate addedDate = LocalDate.parse("2022-09-23"); // LocalDate | Show sound effects added on the specified date
    LocalDate addedDateStart = LocalDate.parse("2021-03-29"); // LocalDate | Show sound effects added on or after the specified date
    LocalDate addedDateEnd = LocalDate.parse("2021-03-29"); // LocalDate | Show sound effects added before the specified date
    Integer duration = 180; // Integer | Show sound effects with the specified duration in seconds
    Integer durationFrom = 30; // Integer | Show sound effects with the specified duration or longer in seconds
    Integer durationTo = 180; // Integer | Show sound effects with the specified duration or shorter in seconds
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String query = "drum"; // String | One or more search terms separated by spaces
    Boolean safe = true; // Boolean | Enable or disable safe search
    String sort = "popular"; // String | Sort by
    String view = "minimal"; // String | Amount of detail to render in the response
    Language language = Language.fromValue("ar"); // Language | Set query and result language (uses Accept-Language header if not set)
    try {
      SFXSearchResults result = apiInstance.searchSFX(addedDate, addedDateStart, addedDateEnd, duration, durationFrom, durationTo, page, perPage, query, safe, sort, view, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoundEffectsApi#searchSFX");
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
| **addedDate** | **LocalDate**| Show sound effects added on the specified date | [optional] |
| **addedDateStart** | **LocalDate**| Show sound effects added on or after the specified date | [optional] |
| **addedDateEnd** | **LocalDate**| Show sound effects added before the specified date | [optional] |
| **duration** | **Integer**| Show sound effects with the specified duration in seconds | [optional] |
| **durationFrom** | **Integer**| Show sound effects with the specified duration or longer in seconds | [optional] |
| **durationTo** | **Integer**| Show sound effects with the specified duration or shorter in seconds | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **query** | **String**| One or more search terms separated by spaces | [optional] |
| **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true] |
| **sort** | **String**| Sort by | [optional] [default to popular] [enum: popular, newest, relevance, random, oldest] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |

### Return type

[**SFXSearchResults**](SFXSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **503** | Service Unavailable |  -  |

