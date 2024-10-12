# EditsApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidpublisherEditsApklistingsDelete**](EditsApi.md#androidpublisherEditsApklistingsDelete) | **DELETE** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} |  |
| [**androidpublisherEditsApklistingsDeleteall**](EditsApi.md#androidpublisherEditsApklistingsDeleteall) | **DELETE** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings |  |
| [**androidpublisherEditsApklistingsGet**](EditsApi.md#androidpublisherEditsApklistingsGet) | **GET** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} |  |
| [**androidpublisherEditsApklistingsList**](EditsApi.md#androidpublisherEditsApklistingsList) | **GET** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings |  |
| [**androidpublisherEditsApklistingsPatch**](EditsApi.md#androidpublisherEditsApklistingsPatch) | **PATCH** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} |  |
| [**androidpublisherEditsApklistingsUpdate**](EditsApi.md#androidpublisherEditsApklistingsUpdate) | **PUT** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} |  |
| [**androidpublisherEditsApksAddexternallyhosted**](EditsApi.md#androidpublisherEditsApksAddexternallyhosted) | **POST** /{packageName}/edits/{editId}/apks/externallyHosted |  |
| [**androidpublisherEditsApksList**](EditsApi.md#androidpublisherEditsApksList) | **GET** /{packageName}/edits/{editId}/apks |  |
| [**androidpublisherEditsApksUpload**](EditsApi.md#androidpublisherEditsApksUpload) | **POST** /{packageName}/edits/{editId}/apks |  |
| [**androidpublisherEditsBundlesList**](EditsApi.md#androidpublisherEditsBundlesList) | **GET** /{packageName}/edits/{editId}/bundles |  |
| [**androidpublisherEditsBundlesUpload**](EditsApi.md#androidpublisherEditsBundlesUpload) | **POST** /{packageName}/edits/{editId}/bundles |  |
| [**androidpublisherEditsCommit**](EditsApi.md#androidpublisherEditsCommit) | **POST** /{packageName}/edits/{editId}:commit |  |
| [**androidpublisherEditsDelete**](EditsApi.md#androidpublisherEditsDelete) | **DELETE** /{packageName}/edits/{editId} |  |
| [**androidpublisherEditsDeobfuscationfilesUpload**](EditsApi.md#androidpublisherEditsDeobfuscationfilesUpload) | **POST** /{packageName}/edits/{editId}/apks/{apkVersionCode}/deobfuscationFiles/{deobfuscationFileType} |  |
| [**androidpublisherEditsDetailsGet**](EditsApi.md#androidpublisherEditsDetailsGet) | **GET** /{packageName}/edits/{editId}/details |  |
| [**androidpublisherEditsDetailsPatch**](EditsApi.md#androidpublisherEditsDetailsPatch) | **PATCH** /{packageName}/edits/{editId}/details |  |
| [**androidpublisherEditsDetailsUpdate**](EditsApi.md#androidpublisherEditsDetailsUpdate) | **PUT** /{packageName}/edits/{editId}/details |  |
| [**androidpublisherEditsExpansionfilesGet**](EditsApi.md#androidpublisherEditsExpansionfilesGet) | **GET** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} |  |
| [**androidpublisherEditsExpansionfilesPatch**](EditsApi.md#androidpublisherEditsExpansionfilesPatch) | **PATCH** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} |  |
| [**androidpublisherEditsExpansionfilesUpdate**](EditsApi.md#androidpublisherEditsExpansionfilesUpdate) | **PUT** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} |  |
| [**androidpublisherEditsExpansionfilesUpload**](EditsApi.md#androidpublisherEditsExpansionfilesUpload) | **POST** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} |  |
| [**androidpublisherEditsGet**](EditsApi.md#androidpublisherEditsGet) | **GET** /{packageName}/edits/{editId} |  |
| [**androidpublisherEditsImagesDelete**](EditsApi.md#androidpublisherEditsImagesDelete) | **DELETE** /{packageName}/edits/{editId}/listings/{language}/{imageType}/{imageId} |  |
| [**androidpublisherEditsImagesDeleteall**](EditsApi.md#androidpublisherEditsImagesDeleteall) | **DELETE** /{packageName}/edits/{editId}/listings/{language}/{imageType} |  |
| [**androidpublisherEditsImagesList**](EditsApi.md#androidpublisherEditsImagesList) | **GET** /{packageName}/edits/{editId}/listings/{language}/{imageType} |  |
| [**androidpublisherEditsImagesUpload**](EditsApi.md#androidpublisherEditsImagesUpload) | **POST** /{packageName}/edits/{editId}/listings/{language}/{imageType} |  |
| [**androidpublisherEditsInsert**](EditsApi.md#androidpublisherEditsInsert) | **POST** /{packageName}/edits |  |
| [**androidpublisherEditsListingsDelete**](EditsApi.md#androidpublisherEditsListingsDelete) | **DELETE** /{packageName}/edits/{editId}/listings/{language} |  |
| [**androidpublisherEditsListingsDeleteall**](EditsApi.md#androidpublisherEditsListingsDeleteall) | **DELETE** /{packageName}/edits/{editId}/listings |  |
| [**androidpublisherEditsListingsGet**](EditsApi.md#androidpublisherEditsListingsGet) | **GET** /{packageName}/edits/{editId}/listings/{language} |  |
| [**androidpublisherEditsListingsList**](EditsApi.md#androidpublisherEditsListingsList) | **GET** /{packageName}/edits/{editId}/listings |  |
| [**androidpublisherEditsListingsPatch**](EditsApi.md#androidpublisherEditsListingsPatch) | **PATCH** /{packageName}/edits/{editId}/listings/{language} |  |
| [**androidpublisherEditsListingsUpdate**](EditsApi.md#androidpublisherEditsListingsUpdate) | **PUT** /{packageName}/edits/{editId}/listings/{language} |  |
| [**androidpublisherEditsTestersGet**](EditsApi.md#androidpublisherEditsTestersGet) | **GET** /{packageName}/edits/{editId}/testers/{track} |  |
| [**androidpublisherEditsTestersPatch**](EditsApi.md#androidpublisherEditsTestersPatch) | **PATCH** /{packageName}/edits/{editId}/testers/{track} |  |
| [**androidpublisherEditsTestersUpdate**](EditsApi.md#androidpublisherEditsTestersUpdate) | **PUT** /{packageName}/edits/{editId}/testers/{track} |  |
| [**androidpublisherEditsTracksGet**](EditsApi.md#androidpublisherEditsTracksGet) | **GET** /{packageName}/edits/{editId}/tracks/{track} |  |
| [**androidpublisherEditsTracksList**](EditsApi.md#androidpublisherEditsTracksList) | **GET** /{packageName}/edits/{editId}/tracks |  |
| [**androidpublisherEditsTracksPatch**](EditsApi.md#androidpublisherEditsTracksPatch) | **PATCH** /{packageName}/edits/{editId}/tracks/{track} |  |
| [**androidpublisherEditsTracksUpdate**](EditsApi.md#androidpublisherEditsTracksUpdate) | **PUT** /{packageName}/edits/{editId}/tracks/{track} |  |
| [**androidpublisherEditsValidate**](EditsApi.md#androidpublisherEditsValidate) | **POST** /{packageName}/edits/{editId}:validate |  |


<a id="androidpublisherEditsApklistingsDelete"></a>
# **androidpublisherEditsApklistingsDelete**
> androidpublisherEditsApklistingsDelete(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes the APK-specific localized listing for a specified APK and language code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The APK version code whose APK-specific listings should be read or modified.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherEditsApklistingsDelete(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApklistingsDelete");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The APK version code whose APK-specific listings should be read or modified. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApklistingsDeleteall"></a>
# **androidpublisherEditsApklistingsDeleteall**
> androidpublisherEditsApklistingsDeleteall(packageName, editId, apkVersionCode, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes all the APK-specific localized listings for a specified APK.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The APK version code whose APK-specific listings should be read or modified.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherEditsApklistingsDeleteall(packageName, editId, apkVersionCode, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApklistingsDeleteall");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The APK version code whose APK-specific listings should be read or modified. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApklistingsGet"></a>
# **androidpublisherEditsApklistingsGet**
> ApkListing androidpublisherEditsApklistingsGet(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Fetches the APK-specific localized listing for a specified APK and language code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The APK version code whose APK-specific listings should be read or modified.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ApkListing result = apiInstance.androidpublisherEditsApklistingsGet(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApklistingsGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The APK version code whose APK-specific listings should be read or modified. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ApkListing**](ApkListing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApklistingsList"></a>
# **androidpublisherEditsApklistingsList**
> ApkListingsListResponse androidpublisherEditsApklistingsList(packageName, editId, apkVersionCode, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Lists all the APK-specific localized listings for a specified APK.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The APK version code whose APK-specific listings should be read or modified.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ApkListingsListResponse result = apiInstance.androidpublisherEditsApklistingsList(packageName, editId, apkVersionCode, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApklistingsList");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The APK version code whose APK-specific listings should be read or modified. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ApkListingsListResponse**](ApkListingsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApklistingsPatch"></a>
# **androidpublisherEditsApklistingsPatch**
> ApkListing androidpublisherEditsApklistingsPatch(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, apkListing)



Updates or creates the APK-specific localized listing for a specified APK and language code. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The APK version code whose APK-specific listings should be read or modified.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ApkListing apkListing = new ApkListing(); // ApkListing | 
    try {
      ApkListing result = apiInstance.androidpublisherEditsApklistingsPatch(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, apkListing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApklistingsPatch");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The APK version code whose APK-specific listings should be read or modified. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **apkListing** | [**ApkListing**](ApkListing.md)|  | [optional] |

### Return type

[**ApkListing**](ApkListing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApklistingsUpdate"></a>
# **androidpublisherEditsApklistingsUpdate**
> ApkListing androidpublisherEditsApklistingsUpdate(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, apkListing)



Updates or creates the APK-specific localized listing for a specified APK and language code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The APK version code whose APK-specific listings should be read or modified.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ApkListing apkListing = new ApkListing(); // ApkListing | 
    try {
      ApkListing result = apiInstance.androidpublisherEditsApklistingsUpdate(packageName, editId, apkVersionCode, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, apkListing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApklistingsUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The APK version code whose APK-specific listings should be read or modified. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **apkListing** | [**ApkListing**](ApkListing.md)|  | [optional] |

### Return type

[**ApkListing**](ApkListing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApksAddexternallyhosted"></a>
# **androidpublisherEditsApksAddexternallyhosted**
> ApksAddExternallyHostedResponse androidpublisherEditsApksAddexternallyhosted(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, apksAddExternallyHostedRequest)



Creates a new APK without uploading the APK itself to Google Play, instead hosting the APK at a specified URL. This function is only available to enterprises using Google Play for Work whose application is configured to restrict distribution to the enterprise domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ApksAddExternallyHostedRequest apksAddExternallyHostedRequest = new ApksAddExternallyHostedRequest(); // ApksAddExternallyHostedRequest | 
    try {
      ApksAddExternallyHostedResponse result = apiInstance.androidpublisherEditsApksAddexternallyhosted(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, apksAddExternallyHostedRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApksAddexternallyhosted");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **apksAddExternallyHostedRequest** | [**ApksAddExternallyHostedRequest**](ApksAddExternallyHostedRequest.md)|  | [optional] |

### Return type

[**ApksAddExternallyHostedResponse**](ApksAddExternallyHostedResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApksList"></a>
# **androidpublisherEditsApksList**
> ApksListResponse androidpublisherEditsApksList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ApksListResponse result = apiInstance.androidpublisherEditsApksList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApksList");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ApksListResponse**](ApksListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsApksUpload"></a>
# **androidpublisherEditsApksUpload**
> Apk androidpublisherEditsApksUpload(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Apk result = apiInstance.androidpublisherEditsApksUpload(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsApksUpload");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Apk**](Apk.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsBundlesList"></a>
# **androidpublisherEditsBundlesList**
> BundlesListResponse androidpublisherEditsBundlesList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      BundlesListResponse result = apiInstance.androidpublisherEditsBundlesList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsBundlesList");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**BundlesListResponse**](BundlesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsBundlesUpload"></a>
# **androidpublisherEditsBundlesUpload**
> Bundle androidpublisherEditsBundlesUpload(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ackBundleInstallationWarning)



Uploads a new Android App Bundle to this edit. If you are using the Google API client libraries, please increase the timeout of the http request before calling this endpoint (a timeout of 2 minutes is recommended). See: https://developers.google.com/api-client-library/java/google-api-java-client/errors for an example in java.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean ackBundleInstallationWarning = true; // Boolean | Must be set to true if the bundle installation may trigger a warning on user devices (for example, if installation size may be over a threshold, typically 100 MB).
    try {
      Bundle result = apiInstance.androidpublisherEditsBundlesUpload(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ackBundleInstallationWarning);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsBundlesUpload");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ackBundleInstallationWarning** | **Boolean**| Must be set to true if the bundle installation may trigger a warning on user devices (for example, if installation size may be over a threshold, typically 100 MB). | [optional] |

### Return type

[**Bundle**](Bundle.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsCommit"></a>
# **androidpublisherEditsCommit**
> AppEdit androidpublisherEditsCommit(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Commits/applies the changes made in this edit back to the app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AppEdit result = apiInstance.androidpublisherEditsCommit(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsCommit");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsDelete"></a>
# **androidpublisherEditsDelete**
> androidpublisherEditsDelete(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes an edit for an app. Creating a new edit will automatically delete any of your previous edits so this method need only be called if you want to preemptively abandon an edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherEditsDelete(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsDelete");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsDeobfuscationfilesUpload"></a>
# **androidpublisherEditsDeobfuscationfilesUpload**
> DeobfuscationFilesUploadResponse androidpublisherEditsDeobfuscationfilesUpload(packageName, editId, apkVersionCode, deobfuscationFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Uploads the deobfuscation file of the specified APK. If a deobfuscation or symbolication file already exists, it will be replaced. See https://developer.android.com/studio/build/shrink-code to learn more about deobfuscation files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier of the Android app for which the deobfuscation files are being uploaded; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The version code of the APK whose deobfuscation file is being uploaded.
    String deobfuscationFileType = "nativeCode"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      DeobfuscationFilesUploadResponse result = apiInstance.androidpublisherEditsDeobfuscationfilesUpload(packageName, editId, apkVersionCode, deobfuscationFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsDeobfuscationfilesUpload");
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
| **packageName** | **String**| Unique identifier of the Android app for which the deobfuscation files are being uploaded; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The version code of the APK whose deobfuscation file is being uploaded. | |
| **deobfuscationFileType** | **String**|  | [enum: nativeCode, proguard] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**DeobfuscationFilesUploadResponse**](DeobfuscationFilesUploadResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsDetailsGet"></a>
# **androidpublisherEditsDetailsGet**
> AppDetails androidpublisherEditsDetailsGet(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Fetches app details for this edit. This includes the default language and developer support contact information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AppDetails result = apiInstance.androidpublisherEditsDetailsGet(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsDetailsGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AppDetails**](AppDetails.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsDetailsPatch"></a>
# **androidpublisherEditsDetailsPatch**
> AppDetails androidpublisherEditsDetailsPatch(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, appDetails)



Updates app details for this edit. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AppDetails appDetails = new AppDetails(); // AppDetails | 
    try {
      AppDetails result = apiInstance.androidpublisherEditsDetailsPatch(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, appDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsDetailsPatch");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **appDetails** | [**AppDetails**](AppDetails.md)|  | [optional] |

### Return type

[**AppDetails**](AppDetails.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsDetailsUpdate"></a>
# **androidpublisherEditsDetailsUpdate**
> AppDetails androidpublisherEditsDetailsUpdate(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, appDetails)



Updates app details for this edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AppDetails appDetails = new AppDetails(); // AppDetails | 
    try {
      AppDetails result = apiInstance.androidpublisherEditsDetailsUpdate(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, appDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsDetailsUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **appDetails** | [**AppDetails**](AppDetails.md)|  | [optional] |

### Return type

[**AppDetails**](AppDetails.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsExpansionfilesGet"></a>
# **androidpublisherEditsExpansionfilesGet**
> ExpansionFile androidpublisherEditsExpansionfilesGet(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Fetches the Expansion File configuration for the APK specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The version code of the APK whose Expansion File configuration is being read or modified.
    String expansionFileType = "main"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ExpansionFile result = apiInstance.androidpublisherEditsExpansionfilesGet(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsExpansionfilesGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The version code of the APK whose Expansion File configuration is being read or modified. | |
| **expansionFileType** | **String**|  | [enum: main, patch] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ExpansionFile**](ExpansionFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsExpansionfilesPatch"></a>
# **androidpublisherEditsExpansionfilesPatch**
> ExpansionFile androidpublisherEditsExpansionfilesPatch(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, expansionFile)



Updates the APK&#39;s Expansion File configuration to reference another APK&#39;s Expansion Files. To add a new Expansion File use the Upload method. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The version code of the APK whose Expansion File configuration is being read or modified.
    String expansionFileType = "main"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ExpansionFile expansionFile = new ExpansionFile(); // ExpansionFile | 
    try {
      ExpansionFile result = apiInstance.androidpublisherEditsExpansionfilesPatch(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, expansionFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsExpansionfilesPatch");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The version code of the APK whose Expansion File configuration is being read or modified. | |
| **expansionFileType** | **String**|  | [enum: main, patch] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **expansionFile** | [**ExpansionFile**](ExpansionFile.md)|  | [optional] |

### Return type

[**ExpansionFile**](ExpansionFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsExpansionfilesUpdate"></a>
# **androidpublisherEditsExpansionfilesUpdate**
> ExpansionFile androidpublisherEditsExpansionfilesUpdate(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, expansionFile)



Updates the APK&#39;s Expansion File configuration to reference another APK&#39;s Expansion Files. To add a new Expansion File use the Upload method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The version code of the APK whose Expansion File configuration is being read or modified.
    String expansionFileType = "main"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ExpansionFile expansionFile = new ExpansionFile(); // ExpansionFile | 
    try {
      ExpansionFile result = apiInstance.androidpublisherEditsExpansionfilesUpdate(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, expansionFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsExpansionfilesUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The version code of the APK whose Expansion File configuration is being read or modified. | |
| **expansionFileType** | **String**|  | [enum: main, patch] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **expansionFile** | [**ExpansionFile**](ExpansionFile.md)|  | [optional] |

### Return type

[**ExpansionFile**](ExpansionFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsExpansionfilesUpload"></a>
# **androidpublisherEditsExpansionfilesUpload**
> ExpansionFilesUploadResponse androidpublisherEditsExpansionfilesUpload(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Uploads and attaches a new Expansion File to the APK specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    Integer apkVersionCode = 56; // Integer | The version code of the APK whose Expansion File configuration is being read or modified.
    String expansionFileType = "main"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ExpansionFilesUploadResponse result = apiInstance.androidpublisherEditsExpansionfilesUpload(packageName, editId, apkVersionCode, expansionFileType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsExpansionfilesUpload");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **apkVersionCode** | **Integer**| The version code of the APK whose Expansion File configuration is being read or modified. | |
| **expansionFileType** | **String**|  | [enum: main, patch] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ExpansionFilesUploadResponse**](ExpansionFilesUploadResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsGet"></a>
# **androidpublisherEditsGet**
> AppEdit androidpublisherEditsGet(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Returns information about the edit specified. Calls will fail if the edit is no long active (e.g. has been deleted, superseded or expired).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AppEdit result = apiInstance.androidpublisherEditsGet(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsImagesDelete"></a>
# **androidpublisherEditsImagesDelete**
> androidpublisherEditsImagesDelete(packageName, editId, language, imageType, imageId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes the image (specified by id) from the edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
    String imageType = "featureGraphic"; // String | 
    String imageId = "imageId_example"; // String | Unique identifier an image within the set of images attached to this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherEditsImagesDelete(packageName, editId, language, imageType, imageId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsImagesDelete");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **imageType** | **String**|  | [enum: featureGraphic, icon, phoneScreenshots, promoGraphic, sevenInchScreenshots, tenInchScreenshots, tvBanner, tvScreenshots, wearScreenshots] |
| **imageId** | **String**| Unique identifier an image within the set of images attached to this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsImagesDeleteall"></a>
# **androidpublisherEditsImagesDeleteall**
> ImagesDeleteAllResponse androidpublisherEditsImagesDeleteall(packageName, editId, language, imageType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes all images for the specified language and image type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
    String imageType = "featureGraphic"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ImagesDeleteAllResponse result = apiInstance.androidpublisherEditsImagesDeleteall(packageName, editId, language, imageType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsImagesDeleteall");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **imageType** | **String**|  | [enum: featureGraphic, icon, phoneScreenshots, promoGraphic, sevenInchScreenshots, tenInchScreenshots, tvBanner, tvScreenshots, wearScreenshots] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ImagesDeleteAllResponse**](ImagesDeleteAllResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsImagesList"></a>
# **androidpublisherEditsImagesList**
> ImagesListResponse androidpublisherEditsImagesList(packageName, editId, language, imageType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Lists all images for the specified language and image type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
    String imageType = "featureGraphic"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ImagesListResponse result = apiInstance.androidpublisherEditsImagesList(packageName, editId, language, imageType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsImagesList");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **imageType** | **String**|  | [enum: featureGraphic, icon, phoneScreenshots, promoGraphic, sevenInchScreenshots, tenInchScreenshots, tvBanner, tvScreenshots, wearScreenshots] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ImagesListResponse**](ImagesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsImagesUpload"></a>
# **androidpublisherEditsImagesUpload**
> ImagesUploadResponse androidpublisherEditsImagesUpload(packageName, editId, language, imageType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Uploads a new image and adds it to the list of images for the specified language and image type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
    String imageType = "featureGraphic"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ImagesUploadResponse result = apiInstance.androidpublisherEditsImagesUpload(packageName, editId, language, imageType, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsImagesUpload");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **imageType** | **String**|  | [enum: featureGraphic, icon, phoneScreenshots, promoGraphic, sevenInchScreenshots, tenInchScreenshots, tvBanner, tvScreenshots, wearScreenshots] |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ImagesUploadResponse**](ImagesUploadResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsInsert"></a>
# **androidpublisherEditsInsert**
> AppEdit androidpublisherEditsInsert(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, appEdit)



Creates a new edit for an app, populated with the app&#39;s current state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    AppEdit appEdit = new AppEdit(); // AppEdit | 
    try {
      AppEdit result = apiInstance.androidpublisherEditsInsert(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, appEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsInsert");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **appEdit** | [**AppEdit**](AppEdit.md)|  | [optional] |

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsListingsDelete"></a>
# **androidpublisherEditsListingsDelete**
> androidpublisherEditsListingsDelete(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes the specified localized store listing from an edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherEditsListingsDelete(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsListingsDelete");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsListingsDeleteall"></a>
# **androidpublisherEditsListingsDeleteall**
> androidpublisherEditsListingsDeleteall(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Deletes all localized listings from an edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherEditsListingsDeleteall(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsListingsDeleteall");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsListingsGet"></a>
# **androidpublisherEditsListingsGet**
> Listing androidpublisherEditsListingsGet(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Fetches information about a localized store listing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Listing result = apiInstance.androidpublisherEditsListingsGet(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsListingsGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Listing**](Listing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsListingsList"></a>
# **androidpublisherEditsListingsList**
> ListingsListResponse androidpublisherEditsListingsList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Returns all of the localized store listings attached to this edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ListingsListResponse result = apiInstance.androidpublisherEditsListingsList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsListingsList");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ListingsListResponse**](ListingsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsListingsPatch"></a>
# **androidpublisherEditsListingsPatch**
> Listing androidpublisherEditsListingsPatch(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, listing)



Creates or updates a localized store listing. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Listing listing = new Listing(); // Listing | 
    try {
      Listing result = apiInstance.androidpublisherEditsListingsPatch(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, listing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsListingsPatch");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **listing** | [**Listing**](Listing.md)|  | [optional] |

### Return type

[**Listing**](Listing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsListingsUpdate"></a>
# **androidpublisherEditsListingsUpdate**
> Listing androidpublisherEditsListingsUpdate(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, listing)



Creates or updates a localized store listing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Listing listing = new Listing(); // Listing | 
    try {
      Listing result = apiInstance.androidpublisherEditsListingsUpdate(packageName, editId, language, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, listing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsListingsUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **listing** | [**Listing**](Listing.md)|  | [optional] |

### Return type

[**Listing**](Listing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTestersGet"></a>
# **androidpublisherEditsTestersGet**
> Testers androidpublisherEditsTestersGet(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String track = "track_example"; // String | The track to read or modify.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Testers result = apiInstance.androidpublisherEditsTestersGet(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTestersGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **track** | **String**| The track to read or modify. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Testers**](Testers.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTestersPatch"></a>
# **androidpublisherEditsTestersPatch**
> Testers androidpublisherEditsTestersPatch(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, testers)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String track = "track_example"; // String | The track to read or modify.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Testers testers = new Testers(); // Testers | 
    try {
      Testers result = apiInstance.androidpublisherEditsTestersPatch(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, testers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTestersPatch");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **track** | **String**| The track to read or modify. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **testers** | [**Testers**](Testers.md)|  | [optional] |

### Return type

[**Testers**](Testers.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTestersUpdate"></a>
# **androidpublisherEditsTestersUpdate**
> Testers androidpublisherEditsTestersUpdate(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, testers)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String track = "track_example"; // String | The track to read or modify.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Testers testers = new Testers(); // Testers | 
    try {
      Testers result = apiInstance.androidpublisherEditsTestersUpdate(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, testers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTestersUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **track** | **String**| The track to read or modify. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **testers** | [**Testers**](Testers.md)|  | [optional] |

### Return type

[**Testers**](Testers.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTracksGet"></a>
# **androidpublisherEditsTracksGet**
> Track androidpublisherEditsTracksGet(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Fetches the track configuration for the specified track type. Includes the APK version codes that are in this track.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String track = "track_example"; // String | The track to read or modify.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Track result = apiInstance.androidpublisherEditsTracksGet(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTracksGet");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **track** | **String**| The track to read or modify. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Track**](Track.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTracksList"></a>
# **androidpublisherEditsTracksList**
> TracksListResponse androidpublisherEditsTracksList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Lists all the track configurations for this edit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      TracksListResponse result = apiInstance.androidpublisherEditsTracksList(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTracksList");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**TracksListResponse**](TracksListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTracksPatch"></a>
# **androidpublisherEditsTracksPatch**
> Track androidpublisherEditsTracksPatch(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, track2)



Updates the track configuration for the specified track type. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String track = "track_example"; // String | The track to read or modify.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Track track2 = new Track(); // Track | 
    try {
      Track result = apiInstance.androidpublisherEditsTracksPatch(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, track2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTracksPatch");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **track** | **String**| The track to read or modify. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **track2** | [**Track**](Track.md)|  | [optional] |

### Return type

[**Track**](Track.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsTracksUpdate"></a>
# **androidpublisherEditsTracksUpdate**
> Track androidpublisherEditsTracksUpdate(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, track2)



Updates the track configuration for the specified track type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String track = "track_example"; // String | The track to read or modify.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Track track2 = new Track(); // Track | 
    try {
      Track result = apiInstance.androidpublisherEditsTracksUpdate(packageName, editId, track, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, track2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsTracksUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **track** | **String**| The track to read or modify. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **track2** | [**Track**](Track.md)|  | [optional] |

### Return type

[**Track**](Track.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherEditsValidate"></a>
# **androidpublisherEditsValidate**
> AppEdit androidpublisherEditsValidate(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Checks that the edit can be successfully committed. The edit&#39;s changes are not applied to the live app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EditsApi apiInstance = new EditsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
    String editId = "editId_example"; // String | Unique identifier for this edit.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AppEdit result = apiInstance.androidpublisherEditsValidate(packageName, editId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#androidpublisherEditsValidate");
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
| **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | |
| **editId** | **String**| Unique identifier for this edit. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

