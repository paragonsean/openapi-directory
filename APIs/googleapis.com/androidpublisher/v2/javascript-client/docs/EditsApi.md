# GooglePlayDeveloper.EditsApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherEditsApklistingsDelete**](EditsApi.md#androidpublisherEditsApklistingsDelete) | **DELETE** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} | 
[**androidpublisherEditsApklistingsDeleteall**](EditsApi.md#androidpublisherEditsApklistingsDeleteall) | **DELETE** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings | 
[**androidpublisherEditsApklistingsGet**](EditsApi.md#androidpublisherEditsApklistingsGet) | **GET** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} | 
[**androidpublisherEditsApklistingsList**](EditsApi.md#androidpublisherEditsApklistingsList) | **GET** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings | 
[**androidpublisherEditsApklistingsPatch**](EditsApi.md#androidpublisherEditsApklistingsPatch) | **PATCH** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} | 
[**androidpublisherEditsApklistingsUpdate**](EditsApi.md#androidpublisherEditsApklistingsUpdate) | **PUT** /{packageName}/edits/{editId}/apks/{apkVersionCode}/listings/{language} | 
[**androidpublisherEditsApksAddexternallyhosted**](EditsApi.md#androidpublisherEditsApksAddexternallyhosted) | **POST** /{packageName}/edits/{editId}/apks/externallyHosted | 
[**androidpublisherEditsApksList**](EditsApi.md#androidpublisherEditsApksList) | **GET** /{packageName}/edits/{editId}/apks | 
[**androidpublisherEditsApksUpload**](EditsApi.md#androidpublisherEditsApksUpload) | **POST** /{packageName}/edits/{editId}/apks | 
[**androidpublisherEditsBundlesList**](EditsApi.md#androidpublisherEditsBundlesList) | **GET** /{packageName}/edits/{editId}/bundles | 
[**androidpublisherEditsBundlesUpload**](EditsApi.md#androidpublisherEditsBundlesUpload) | **POST** /{packageName}/edits/{editId}/bundles | 
[**androidpublisherEditsCommit**](EditsApi.md#androidpublisherEditsCommit) | **POST** /{packageName}/edits/{editId}:commit | 
[**androidpublisherEditsDelete**](EditsApi.md#androidpublisherEditsDelete) | **DELETE** /{packageName}/edits/{editId} | 
[**androidpublisherEditsDeobfuscationfilesUpload**](EditsApi.md#androidpublisherEditsDeobfuscationfilesUpload) | **POST** /{packageName}/edits/{editId}/apks/{apkVersionCode}/deobfuscationFiles/{deobfuscationFileType} | 
[**androidpublisherEditsDetailsGet**](EditsApi.md#androidpublisherEditsDetailsGet) | **GET** /{packageName}/edits/{editId}/details | 
[**androidpublisherEditsDetailsPatch**](EditsApi.md#androidpublisherEditsDetailsPatch) | **PATCH** /{packageName}/edits/{editId}/details | 
[**androidpublisherEditsDetailsUpdate**](EditsApi.md#androidpublisherEditsDetailsUpdate) | **PUT** /{packageName}/edits/{editId}/details | 
[**androidpublisherEditsExpansionfilesGet**](EditsApi.md#androidpublisherEditsExpansionfilesGet) | **GET** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} | 
[**androidpublisherEditsExpansionfilesPatch**](EditsApi.md#androidpublisherEditsExpansionfilesPatch) | **PATCH** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} | 
[**androidpublisherEditsExpansionfilesUpdate**](EditsApi.md#androidpublisherEditsExpansionfilesUpdate) | **PUT** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} | 
[**androidpublisherEditsExpansionfilesUpload**](EditsApi.md#androidpublisherEditsExpansionfilesUpload) | **POST** /{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType} | 
[**androidpublisherEditsGet**](EditsApi.md#androidpublisherEditsGet) | **GET** /{packageName}/edits/{editId} | 
[**androidpublisherEditsImagesDelete**](EditsApi.md#androidpublisherEditsImagesDelete) | **DELETE** /{packageName}/edits/{editId}/listings/{language}/{imageType}/{imageId} | 
[**androidpublisherEditsImagesDeleteall**](EditsApi.md#androidpublisherEditsImagesDeleteall) | **DELETE** /{packageName}/edits/{editId}/listings/{language}/{imageType} | 
[**androidpublisherEditsImagesList**](EditsApi.md#androidpublisherEditsImagesList) | **GET** /{packageName}/edits/{editId}/listings/{language}/{imageType} | 
[**androidpublisherEditsImagesUpload**](EditsApi.md#androidpublisherEditsImagesUpload) | **POST** /{packageName}/edits/{editId}/listings/{language}/{imageType} | 
[**androidpublisherEditsInsert**](EditsApi.md#androidpublisherEditsInsert) | **POST** /{packageName}/edits | 
[**androidpublisherEditsListingsDelete**](EditsApi.md#androidpublisherEditsListingsDelete) | **DELETE** /{packageName}/edits/{editId}/listings/{language} | 
[**androidpublisherEditsListingsDeleteall**](EditsApi.md#androidpublisherEditsListingsDeleteall) | **DELETE** /{packageName}/edits/{editId}/listings | 
[**androidpublisherEditsListingsGet**](EditsApi.md#androidpublisherEditsListingsGet) | **GET** /{packageName}/edits/{editId}/listings/{language} | 
[**androidpublisherEditsListingsList**](EditsApi.md#androidpublisherEditsListingsList) | **GET** /{packageName}/edits/{editId}/listings | 
[**androidpublisherEditsListingsPatch**](EditsApi.md#androidpublisherEditsListingsPatch) | **PATCH** /{packageName}/edits/{editId}/listings/{language} | 
[**androidpublisherEditsListingsUpdate**](EditsApi.md#androidpublisherEditsListingsUpdate) | **PUT** /{packageName}/edits/{editId}/listings/{language} | 
[**androidpublisherEditsTestersGet**](EditsApi.md#androidpublisherEditsTestersGet) | **GET** /{packageName}/edits/{editId}/testers/{track} | 
[**androidpublisherEditsTestersPatch**](EditsApi.md#androidpublisherEditsTestersPatch) | **PATCH** /{packageName}/edits/{editId}/testers/{track} | 
[**androidpublisherEditsTestersUpdate**](EditsApi.md#androidpublisherEditsTestersUpdate) | **PUT** /{packageName}/edits/{editId}/testers/{track} | 
[**androidpublisherEditsTracksGet**](EditsApi.md#androidpublisherEditsTracksGet) | **GET** /{packageName}/edits/{editId}/tracks/{track} | 
[**androidpublisherEditsTracksList**](EditsApi.md#androidpublisherEditsTracksList) | **GET** /{packageName}/edits/{editId}/tracks | 
[**androidpublisherEditsTracksPatch**](EditsApi.md#androidpublisherEditsTracksPatch) | **PATCH** /{packageName}/edits/{editId}/tracks/{track} | 
[**androidpublisherEditsTracksUpdate**](EditsApi.md#androidpublisherEditsTracksUpdate) | **PUT** /{packageName}/edits/{editId}/tracks/{track} | 
[**androidpublisherEditsValidate**](EditsApi.md#androidpublisherEditsValidate) | **POST** /{packageName}/edits/{editId}:validate | 



## androidpublisherEditsApklistingsDelete

> androidpublisherEditsApklistingsDelete(packageName, editId, apkVersionCode, language, opts)



Deletes the APK-specific localized listing for a specified APK and language code.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The APK version code whose APK-specific listings should be read or modified.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsApklistingsDelete(packageName, editId, apkVersionCode, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The APK version code whose APK-specific listings should be read or modified. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherEditsApklistingsDeleteall

> androidpublisherEditsApklistingsDeleteall(packageName, editId, apkVersionCode, opts)



Deletes all the APK-specific localized listings for a specified APK.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The APK version code whose APK-specific listings should be read or modified.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsApklistingsDeleteall(packageName, editId, apkVersionCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The APK version code whose APK-specific listings should be read or modified. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherEditsApklistingsGet

> ApkListing androidpublisherEditsApklistingsGet(packageName, editId, apkVersionCode, language, opts)



Fetches the APK-specific localized listing for a specified APK and language code.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The APK version code whose APK-specific listings should be read or modified.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsApklistingsGet(packageName, editId, apkVersionCode, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The APK version code whose APK-specific listings should be read or modified. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ApkListing**](ApkListing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsApklistingsList

> ApkListingsListResponse androidpublisherEditsApklistingsList(packageName, editId, apkVersionCode, opts)



Lists all the APK-specific localized listings for a specified APK.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The APK version code whose APK-specific listings should be read or modified.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsApklistingsList(packageName, editId, apkVersionCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The APK version code whose APK-specific listings should be read or modified. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ApkListingsListResponse**](ApkListingsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsApklistingsPatch

> ApkListing androidpublisherEditsApklistingsPatch(packageName, editId, apkVersionCode, language, opts)



Updates or creates the APK-specific localized listing for a specified APK and language code. This method supports patch semantics.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The APK version code whose APK-specific listings should be read or modified.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'apkListing': new GooglePlayDeveloper.ApkListing() // ApkListing | 
};
apiInstance.androidpublisherEditsApklistingsPatch(packageName, editId, apkVersionCode, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The APK version code whose APK-specific listings should be read or modified. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **apkListing** | [**ApkListing**](ApkListing.md)|  | [optional] 

### Return type

[**ApkListing**](ApkListing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsApklistingsUpdate

> ApkListing androidpublisherEditsApklistingsUpdate(packageName, editId, apkVersionCode, language, opts)



Updates or creates the APK-specific localized listing for a specified APK and language code.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The APK version code whose APK-specific listings should be read or modified.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'apkListing': new GooglePlayDeveloper.ApkListing() // ApkListing | 
};
apiInstance.androidpublisherEditsApklistingsUpdate(packageName, editId, apkVersionCode, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The APK version code whose APK-specific listings should be read or modified. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **apkListing** | [**ApkListing**](ApkListing.md)|  | [optional] 

### Return type

[**ApkListing**](ApkListing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsApksAddexternallyhosted

> ApksAddExternallyHostedResponse androidpublisherEditsApksAddexternallyhosted(packageName, editId, opts)



Creates a new APK without uploading the APK itself to Google Play, instead hosting the APK at a specified URL. This function is only available to enterprises using Google Play for Work whose application is configured to restrict distribution to the enterprise domain.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'apksAddExternallyHostedRequest': new GooglePlayDeveloper.ApksAddExternallyHostedRequest() // ApksAddExternallyHostedRequest | 
};
apiInstance.androidpublisherEditsApksAddexternallyhosted(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **apksAddExternallyHostedRequest** | [**ApksAddExternallyHostedRequest**](ApksAddExternallyHostedRequest.md)|  | [optional] 

### Return type

[**ApksAddExternallyHostedResponse**](ApksAddExternallyHostedResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsApksList

> ApksListResponse androidpublisherEditsApksList(packageName, editId, opts)



### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsApksList(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ApksListResponse**](ApksListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsApksUpload

> Apk androidpublisherEditsApksUpload(packageName, editId, opts)



### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsApksUpload(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Apk**](Apk.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsBundlesList

> BundlesListResponse androidpublisherEditsBundlesList(packageName, editId, opts)



### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsBundlesList(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**BundlesListResponse**](BundlesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsBundlesUpload

> Bundle androidpublisherEditsBundlesUpload(packageName, editId, opts)



Uploads a new Android App Bundle to this edit. If you are using the Google API client libraries, please increase the timeout of the http request before calling this endpoint (a timeout of 2 minutes is recommended). See: https://developers.google.com/api-client-library/java/google-api-java-client/errors for an example in java.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ackBundleInstallationWarning': true // Boolean | Must be set to true if the bundle installation may trigger a warning on user devices (for example, if installation size may be over a threshold, typically 100 MB).
};
apiInstance.androidpublisherEditsBundlesUpload(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ackBundleInstallationWarning** | **Boolean**| Must be set to true if the bundle installation may trigger a warning on user devices (for example, if installation size may be over a threshold, typically 100 MB). | [optional] 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsCommit

> AppEdit androidpublisherEditsCommit(packageName, editId, opts)



Commits/applies the changes made in this edit back to the app.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsCommit(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsDelete

> androidpublisherEditsDelete(packageName, editId, opts)



Deletes an edit for an app. Creating a new edit will automatically delete any of your previous edits so this method need only be called if you want to preemptively abandon an edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsDelete(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherEditsDeobfuscationfilesUpload

> DeobfuscationFilesUploadResponse androidpublisherEditsDeobfuscationfilesUpload(packageName, editId, apkVersionCode, deobfuscationFileType, opts)



Uploads the deobfuscation file of the specified APK. If a deobfuscation or symbolication file already exists, it will be replaced. See https://developer.android.com/studio/build/shrink-code to learn more about deobfuscation files.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier of the Android app for which the deobfuscation files are being uploaded; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The version code of the APK whose deobfuscation file is being uploaded.
let deobfuscationFileType = "deobfuscationFileType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsDeobfuscationfilesUpload(packageName, editId, apkVersionCode, deobfuscationFileType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier of the Android app for which the deobfuscation files are being uploaded; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The version code of the APK whose deobfuscation file is being uploaded. | 
 **deobfuscationFileType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**DeobfuscationFilesUploadResponse**](DeobfuscationFilesUploadResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsDetailsGet

> AppDetails androidpublisherEditsDetailsGet(packageName, editId, opts)



Fetches app details for this edit. This includes the default language and developer support contact information.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsDetailsGet(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AppDetails**](AppDetails.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsDetailsPatch

> AppDetails androidpublisherEditsDetailsPatch(packageName, editId, opts)



Updates app details for this edit. This method supports patch semantics.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'appDetails': new GooglePlayDeveloper.AppDetails() // AppDetails | 
};
apiInstance.androidpublisherEditsDetailsPatch(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **appDetails** | [**AppDetails**](AppDetails.md)|  | [optional] 

### Return type

[**AppDetails**](AppDetails.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsDetailsUpdate

> AppDetails androidpublisherEditsDetailsUpdate(packageName, editId, opts)



Updates app details for this edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'appDetails': new GooglePlayDeveloper.AppDetails() // AppDetails | 
};
apiInstance.androidpublisherEditsDetailsUpdate(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **appDetails** | [**AppDetails**](AppDetails.md)|  | [optional] 

### Return type

[**AppDetails**](AppDetails.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsExpansionfilesGet

> ExpansionFile androidpublisherEditsExpansionfilesGet(packageName, editId, apkVersionCode, expansionFileType, opts)



Fetches the Expansion File configuration for the APK specified.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The version code of the APK whose Expansion File configuration is being read or modified.
let expansionFileType = "expansionFileType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsExpansionfilesGet(packageName, editId, apkVersionCode, expansionFileType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The version code of the APK whose Expansion File configuration is being read or modified. | 
 **expansionFileType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ExpansionFile**](ExpansionFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsExpansionfilesPatch

> ExpansionFile androidpublisherEditsExpansionfilesPatch(packageName, editId, apkVersionCode, expansionFileType, opts)



Updates the APK&#39;s Expansion File configuration to reference another APK&#39;s Expansion Files. To add a new Expansion File use the Upload method. This method supports patch semantics.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The version code of the APK whose Expansion File configuration is being read or modified.
let expansionFileType = "expansionFileType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'expansionFile': new GooglePlayDeveloper.ExpansionFile() // ExpansionFile | 
};
apiInstance.androidpublisherEditsExpansionfilesPatch(packageName, editId, apkVersionCode, expansionFileType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The version code of the APK whose Expansion File configuration is being read or modified. | 
 **expansionFileType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **expansionFile** | [**ExpansionFile**](ExpansionFile.md)|  | [optional] 

### Return type

[**ExpansionFile**](ExpansionFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsExpansionfilesUpdate

> ExpansionFile androidpublisherEditsExpansionfilesUpdate(packageName, editId, apkVersionCode, expansionFileType, opts)



Updates the APK&#39;s Expansion File configuration to reference another APK&#39;s Expansion Files. To add a new Expansion File use the Upload method.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The version code of the APK whose Expansion File configuration is being read or modified.
let expansionFileType = "expansionFileType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'expansionFile': new GooglePlayDeveloper.ExpansionFile() // ExpansionFile | 
};
apiInstance.androidpublisherEditsExpansionfilesUpdate(packageName, editId, apkVersionCode, expansionFileType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The version code of the APK whose Expansion File configuration is being read or modified. | 
 **expansionFileType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **expansionFile** | [**ExpansionFile**](ExpansionFile.md)|  | [optional] 

### Return type

[**ExpansionFile**](ExpansionFile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsExpansionfilesUpload

> ExpansionFilesUploadResponse androidpublisherEditsExpansionfilesUpload(packageName, editId, apkVersionCode, expansionFileType, opts)



Uploads and attaches a new Expansion File to the APK specified.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let apkVersionCode = 56; // Number | The version code of the APK whose Expansion File configuration is being read or modified.
let expansionFileType = "expansionFileType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsExpansionfilesUpload(packageName, editId, apkVersionCode, expansionFileType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **apkVersionCode** | **Number**| The version code of the APK whose Expansion File configuration is being read or modified. | 
 **expansionFileType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ExpansionFilesUploadResponse**](ExpansionFilesUploadResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsGet

> AppEdit androidpublisherEditsGet(packageName, editId, opts)



Returns information about the edit specified. Calls will fail if the edit is no long active (e.g. has been deleted, superseded or expired).

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsGet(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsImagesDelete

> androidpublisherEditsImagesDelete(packageName, editId, language, imageType, imageId, opts)



Deletes the image (specified by id) from the edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
let imageType = "imageType_example"; // String | 
let imageId = "imageId_example"; // String | Unique identifier an image within the set of images attached to this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsImagesDelete(packageName, editId, language, imageType, imageId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **imageType** | **String**|  | 
 **imageId** | **String**| Unique identifier an image within the set of images attached to this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherEditsImagesDeleteall

> ImagesDeleteAllResponse androidpublisherEditsImagesDeleteall(packageName, editId, language, imageType, opts)



Deletes all images for the specified language and image type.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
let imageType = "imageType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsImagesDeleteall(packageName, editId, language, imageType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **imageType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ImagesDeleteAllResponse**](ImagesDeleteAllResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsImagesList

> ImagesListResponse androidpublisherEditsImagesList(packageName, editId, language, imageType, opts)



Lists all images for the specified language and image type.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
let imageType = "imageType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsImagesList(packageName, editId, language, imageType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **imageType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ImagesListResponse**](ImagesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsImagesUpload

> ImagesUploadResponse androidpublisherEditsImagesUpload(packageName, editId, language, imageType, opts)



Uploads a new image and adds it to the list of images for the specified language and image type.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \"de-AT\".
let imageType = "imageType_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsImagesUpload(packageName, editId, language, imageType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **imageType** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ImagesUploadResponse**](ImagesUploadResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsInsert

> AppEdit androidpublisherEditsInsert(packageName, opts)



Creates a new edit for an app, populated with the app&#39;s current state.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'appEdit': new GooglePlayDeveloper.AppEdit() // AppEdit | 
};
apiInstance.androidpublisherEditsInsert(packageName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **appEdit** | [**AppEdit**](AppEdit.md)|  | [optional] 

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsListingsDelete

> androidpublisherEditsListingsDelete(packageName, editId, language, opts)



Deletes the specified localized store listing from an edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsListingsDelete(packageName, editId, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherEditsListingsDeleteall

> androidpublisherEditsListingsDeleteall(packageName, editId, opts)



Deletes all localized listings from an edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsListingsDeleteall(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherEditsListingsGet

> Listing androidpublisherEditsListingsGet(packageName, editId, language, opts)



Fetches information about a localized store listing.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsListingsGet(packageName, editId, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Listing**](Listing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsListingsList

> ListingsListResponse androidpublisherEditsListingsList(packageName, editId, opts)



Returns all of the localized store listings attached to this edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsListingsList(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ListingsListResponse**](ListingsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsListingsPatch

> Listing androidpublisherEditsListingsPatch(packageName, editId, language, opts)



Creates or updates a localized store listing. This method supports patch semantics.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'listing': new GooglePlayDeveloper.Listing() // Listing | 
};
apiInstance.androidpublisherEditsListingsPatch(packageName, editId, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **listing** | [**Listing**](Listing.md)|  | [optional] 

### Return type

[**Listing**](Listing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsListingsUpdate

> Listing androidpublisherEditsListingsUpdate(packageName, editId, language, opts)



Creates or updates a localized store listing.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let language = "language_example"; // String | The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \"de-AT\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'listing': new GooglePlayDeveloper.Listing() // Listing | 
};
apiInstance.androidpublisherEditsListingsUpdate(packageName, editId, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **language** | **String**| The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **listing** | [**Listing**](Listing.md)|  | [optional] 

### Return type

[**Listing**](Listing.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsTestersGet

> Testers androidpublisherEditsTestersGet(packageName, editId, track, opts)



### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let track = "track_example"; // String | The track to read or modify.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsTestersGet(packageName, editId, track, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **track** | **String**| The track to read or modify. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Testers**](Testers.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsTestersPatch

> Testers androidpublisherEditsTestersPatch(packageName, editId, track, opts)



### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let track = "track_example"; // String | The track to read or modify.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'testers': new GooglePlayDeveloper.Testers() // Testers | 
};
apiInstance.androidpublisherEditsTestersPatch(packageName, editId, track, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **track** | **String**| The track to read or modify. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **testers** | [**Testers**](Testers.md)|  | [optional] 

### Return type

[**Testers**](Testers.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsTestersUpdate

> Testers androidpublisherEditsTestersUpdate(packageName, editId, track, opts)



### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let track = "track_example"; // String | The track to read or modify.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'testers': new GooglePlayDeveloper.Testers() // Testers | 
};
apiInstance.androidpublisherEditsTestersUpdate(packageName, editId, track, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **track** | **String**| The track to read or modify. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **testers** | [**Testers**](Testers.md)|  | [optional] 

### Return type

[**Testers**](Testers.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsTracksGet

> Track androidpublisherEditsTracksGet(packageName, editId, track, opts)



Fetches the track configuration for the specified track type. Includes the APK version codes that are in this track.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let track = "track_example"; // String | The track to read or modify.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsTracksGet(packageName, editId, track, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **track** | **String**| The track to read or modify. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Track**](Track.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsTracksList

> TracksListResponse androidpublisherEditsTracksList(packageName, editId, opts)



Lists all the track configurations for this edit.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsTracksList(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**TracksListResponse**](TracksListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherEditsTracksPatch

> Track androidpublisherEditsTracksPatch(packageName, editId, track, opts)



Updates the track configuration for the specified track type. This method supports patch semantics.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let track = "track_example"; // String | The track to read or modify.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'track2': new GooglePlayDeveloper.Track() // Track | 
};
apiInstance.androidpublisherEditsTracksPatch(packageName, editId, track, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **track** | **String**| The track to read or modify. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **track2** | [**Track**](Track.md)|  | [optional] 

### Return type

[**Track**](Track.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsTracksUpdate

> Track androidpublisherEditsTracksUpdate(packageName, editId, track, opts)



Updates the track configuration for the specified track type.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let track = "track_example"; // String | The track to read or modify.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'track2': new GooglePlayDeveloper.Track() // Track | 
};
apiInstance.androidpublisherEditsTracksUpdate(packageName, editId, track, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **track** | **String**| The track to read or modify. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **track2** | [**Track**](Track.md)|  | [optional] 

### Return type

[**Track**](Track.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherEditsValidate

> AppEdit androidpublisherEditsValidate(packageName, editId, opts)



Checks that the edit can be successfully committed. The edit&#39;s changes are not applied to the live app.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.EditsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app that is being updated; for example, \"com.spiffygame\".
let editId = "editId_example"; // String | Unique identifier for this edit.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherEditsValidate(packageName, editId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;. | 
 **editId** | **String**| Unique identifier for this edit. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AppEdit**](AppEdit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

