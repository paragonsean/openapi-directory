# AmazonNimbleStudio.DefaultApi

All URIs are relative to *http://nimble.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptEulas**](DefaultApi.md#acceptEulas) | **POST** /2020-08-01/studios/{studioId}/eula-acceptances | 
[**createLaunchProfile**](DefaultApi.md#createLaunchProfile) | **POST** /2020-08-01/studios/{studioId}/launch-profiles | 
[**createStreamingImage**](DefaultApi.md#createStreamingImage) | **POST** /2020-08-01/studios/{studioId}/streaming-images | 
[**createStreamingSession**](DefaultApi.md#createStreamingSession) | **POST** /2020-08-01/studios/{studioId}/streaming-sessions | 
[**createStreamingSessionStream**](DefaultApi.md#createStreamingSessionStream) | **POST** /2020-08-01/studios/{studioId}/streaming-sessions/{sessionId}/streams | 
[**createStudio**](DefaultApi.md#createStudio) | **POST** /2020-08-01/studios | 
[**createStudioComponent**](DefaultApi.md#createStudioComponent) | **POST** /2020-08-01/studios/{studioId}/studio-components | 
[**deleteLaunchProfile**](DefaultApi.md#deleteLaunchProfile) | **DELETE** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId} | 
[**deleteLaunchProfileMember**](DefaultApi.md#deleteLaunchProfileMember) | **DELETE** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/membership/{principalId} | 
[**deleteStreamingImage**](DefaultApi.md#deleteStreamingImage) | **DELETE** /2020-08-01/studios/{studioId}/streaming-images/{streamingImageId} | 
[**deleteStreamingSession**](DefaultApi.md#deleteStreamingSession) | **DELETE** /2020-08-01/studios/{studioId}/streaming-sessions/{sessionId} | 
[**deleteStudio**](DefaultApi.md#deleteStudio) | **DELETE** /2020-08-01/studios/{studioId} | 
[**deleteStudioComponent**](DefaultApi.md#deleteStudioComponent) | **DELETE** /2020-08-01/studios/{studioId}/studio-components/{studioComponentId} | 
[**deleteStudioMember**](DefaultApi.md#deleteStudioMember) | **DELETE** /2020-08-01/studios/{studioId}/membership/{principalId} | 
[**getEula**](DefaultApi.md#getEula) | **GET** /2020-08-01/eulas/{eulaId} | 
[**getLaunchProfile**](DefaultApi.md#getLaunchProfile) | **GET** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId} | 
[**getLaunchProfileDetails**](DefaultApi.md#getLaunchProfileDetails) | **GET** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/details | 
[**getLaunchProfileInitialization**](DefaultApi.md#getLaunchProfileInitialization) | **GET** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/init#launchProfileProtocolVersions&amp;launchPurpose&amp;platform | 
[**getLaunchProfileMember**](DefaultApi.md#getLaunchProfileMember) | **GET** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/membership/{principalId} | 
[**getStreamingImage**](DefaultApi.md#getStreamingImage) | **GET** /2020-08-01/studios/{studioId}/streaming-images/{streamingImageId} | 
[**getStreamingSession**](DefaultApi.md#getStreamingSession) | **GET** /2020-08-01/studios/{studioId}/streaming-sessions/{sessionId} | 
[**getStreamingSessionBackup**](DefaultApi.md#getStreamingSessionBackup) | **GET** /2020-08-01/studios/{studioId}/streaming-session-backups/{backupId} | 
[**getStreamingSessionStream**](DefaultApi.md#getStreamingSessionStream) | **GET** /2020-08-01/studios/{studioId}/streaming-sessions/{sessionId}/streams/{streamId} | 
[**getStudio**](DefaultApi.md#getStudio) | **GET** /2020-08-01/studios/{studioId} | 
[**getStudioComponent**](DefaultApi.md#getStudioComponent) | **GET** /2020-08-01/studios/{studioId}/studio-components/{studioComponentId} | 
[**getStudioMember**](DefaultApi.md#getStudioMember) | **GET** /2020-08-01/studios/{studioId}/membership/{principalId} | 
[**listEulaAcceptances**](DefaultApi.md#listEulaAcceptances) | **GET** /2020-08-01/studios/{studioId}/eula-acceptances | 
[**listEulas**](DefaultApi.md#listEulas) | **GET** /2020-08-01/eulas | 
[**listLaunchProfileMembers**](DefaultApi.md#listLaunchProfileMembers) | **GET** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/membership | 
[**listLaunchProfiles**](DefaultApi.md#listLaunchProfiles) | **GET** /2020-08-01/studios/{studioId}/launch-profiles | 
[**listStreamingImages**](DefaultApi.md#listStreamingImages) | **GET** /2020-08-01/studios/{studioId}/streaming-images | 
[**listStreamingSessionBackups**](DefaultApi.md#listStreamingSessionBackups) | **GET** /2020-08-01/studios/{studioId}/streaming-session-backups | 
[**listStreamingSessions**](DefaultApi.md#listStreamingSessions) | **GET** /2020-08-01/studios/{studioId}/streaming-sessions | 
[**listStudioComponents**](DefaultApi.md#listStudioComponents) | **GET** /2020-08-01/studios/{studioId}/studio-components | 
[**listStudioMembers**](DefaultApi.md#listStudioMembers) | **GET** /2020-08-01/studios/{studioId}/membership | 
[**listStudios**](DefaultApi.md#listStudios) | **GET** /2020-08-01/studios | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /2020-08-01/tags/{resourceArn} | 
[**putLaunchProfileMembers**](DefaultApi.md#putLaunchProfileMembers) | **POST** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/membership | 
[**putStudioMembers**](DefaultApi.md#putStudioMembers) | **POST** /2020-08-01/studios/{studioId}/membership | 
[**startStreamingSession**](DefaultApi.md#startStreamingSession) | **POST** /2020-08-01/studios/{studioId}/streaming-sessions/{sessionId}/start | 
[**startStudioSSOConfigurationRepair**](DefaultApi.md#startStudioSSOConfigurationRepair) | **PUT** /2020-08-01/studios/{studioId}/sso-configuration | 
[**stopStreamingSession**](DefaultApi.md#stopStreamingSession) | **POST** /2020-08-01/studios/{studioId}/streaming-sessions/{sessionId}/stop | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /2020-08-01/tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /2020-08-01/tags/{resourceArn}#tagKeys | 
[**updateLaunchProfile**](DefaultApi.md#updateLaunchProfile) | **PATCH** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId} | 
[**updateLaunchProfileMember**](DefaultApi.md#updateLaunchProfileMember) | **PATCH** /2020-08-01/studios/{studioId}/launch-profiles/{launchProfileId}/membership/{principalId} | 
[**updateStreamingImage**](DefaultApi.md#updateStreamingImage) | **PATCH** /2020-08-01/studios/{studioId}/streaming-images/{streamingImageId} | 
[**updateStudio**](DefaultApi.md#updateStudio) | **PATCH** /2020-08-01/studios/{studioId} | 
[**updateStudioComponent**](DefaultApi.md#updateStudioComponent) | **PATCH** /2020-08-01/studios/{studioId}/studio-components/{studioComponentId} | 



## acceptEulas

> AcceptEulasResponse acceptEulas(studioId, acceptEulasRequest, opts)



Accept EULAs.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID.
let acceptEulasRequest = new AmazonNimbleStudio.AcceptEulasRequest(); // AcceptEulasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.acceptEulas(studioId, acceptEulasRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID. | 
 **acceptEulasRequest** | [**AcceptEulasRequest**](AcceptEulasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**AcceptEulasResponse**](AcceptEulasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLaunchProfile

> CreateLaunchProfileResponse createLaunchProfile(studioId, createLaunchProfileRequest, opts)



Create a launch profile.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let createLaunchProfileRequest = new AmazonNimbleStudio.CreateLaunchProfileRequest(); // CreateLaunchProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.createLaunchProfile(studioId, createLaunchProfileRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **createLaunchProfileRequest** | [**CreateLaunchProfileRequest**](CreateLaunchProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**CreateLaunchProfileResponse**](CreateLaunchProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamingImage

> CreateStreamingImageResponse createStreamingImage(studioId, createStreamingImageRequest, opts)



Creates a streaming image resource in a studio.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let createStreamingImageRequest = new AmazonNimbleStudio.CreateStreamingImageRequest(); // CreateStreamingImageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.createStreamingImage(studioId, createStreamingImageRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **createStreamingImageRequest** | [**CreateStreamingImageRequest**](CreateStreamingImageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**CreateStreamingImageResponse**](CreateStreamingImageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamingSession

> CreateStreamingSessionResponse createStreamingSession(studioId, createStreamingSessionRequest, opts)



&lt;p&gt;Creates a streaming session in a studio.&lt;/p&gt; &lt;p&gt;After invoking this operation, you must poll GetStreamingSession until the streaming session is in the &lt;code&gt;READY&lt;/code&gt; state.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let createStreamingSessionRequest = new AmazonNimbleStudio.CreateStreamingSessionRequest(); // CreateStreamingSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.createStreamingSession(studioId, createStreamingSessionRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **createStreamingSessionRequest** | [**CreateStreamingSessionRequest**](CreateStreamingSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**CreateStreamingSessionResponse**](CreateStreamingSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamingSessionStream

> CreateStreamingSessionStreamResponse createStreamingSessionStream(sessionId, studioId, createStreamingSessionStreamRequest, opts)



&lt;p&gt;Creates a streaming session stream for a streaming session.&lt;/p&gt; &lt;p&gt;After invoking this API, invoke GetStreamingSessionStream with the returned streamId to poll the resource until it is in the &lt;code&gt;READY&lt;/code&gt; state.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let sessionId = "sessionId_example"; // String | The streaming session ID.
let studioId = "studioId_example"; // String | The studio ID. 
let createStreamingSessionStreamRequest = new AmazonNimbleStudio.CreateStreamingSessionStreamRequest(); // CreateStreamingSessionStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.createStreamingSessionStream(sessionId, studioId, createStreamingSessionStreamRequest, opts, (error, data, response) => {
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
 **sessionId** | **String**| The streaming session ID. | 
 **studioId** | **String**| The studio ID.  | 
 **createStreamingSessionStreamRequest** | [**CreateStreamingSessionStreamRequest**](CreateStreamingSessionStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**CreateStreamingSessionStreamResponse**](CreateStreamingSessionStreamResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStudio

> CreateStudioResponse createStudio(createStudioRequest, opts)



&lt;p&gt;Create a new studio.&lt;/p&gt; &lt;p&gt;When creating a studio, two IAM roles must be provided: the admin role and the user role. These roles are assumed by your users when they log in to the Nimble Studio portal.&lt;/p&gt; &lt;p&gt;The user role must have the &lt;code&gt;AmazonNimbleStudio-StudioUser&lt;/code&gt; managed policy attached for the portal to function properly.&lt;/p&gt; &lt;p&gt;The admin role must have the &lt;code&gt;AmazonNimbleStudio-StudioAdmin&lt;/code&gt; managed policy attached for the portal to function properly.&lt;/p&gt; &lt;p&gt;You may optionally specify a KMS key in the &lt;code&gt;StudioEncryptionConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;In Nimble Studio, resource names, descriptions, initialization scripts, and other data you provide are always encrypted at rest using an KMS key. By default, this key is owned by Amazon Web Services and managed on your behalf. You may provide your own KMS key when calling &lt;code&gt;CreateStudio&lt;/code&gt; to encrypt this data using a key you own and manage.&lt;/p&gt; &lt;p&gt;When providing an KMS key during studio creation, Nimble Studio creates KMS grants in your account to provide your studio user and admin roles access to these KMS keys.&lt;/p&gt; &lt;p&gt;If you delete this grant, the studio will no longer be accessible to your portal users.&lt;/p&gt; &lt;p&gt;If you delete the studio KMS key, your studio will no longer be accessible.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let createStudioRequest = new AmazonNimbleStudio.CreateStudioRequest(); // CreateStudioRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.createStudio(createStudioRequest, opts, (error, data, response) => {
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
 **createStudioRequest** | [**CreateStudioRequest**](CreateStudioRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**CreateStudioResponse**](CreateStudioResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStudioComponent

> CreateStudioComponentResponse createStudioComponent(studioId, createStudioComponentRequest, opts)



Creates a studio component resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let createStudioComponentRequest = new AmazonNimbleStudio.CreateStudioComponentRequest(); // CreateStudioComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.createStudioComponent(studioId, createStudioComponentRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **createStudioComponentRequest** | [**CreateStudioComponentRequest**](CreateStudioComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**CreateStudioComponentResponse**](CreateStudioComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLaunchProfile

> DeleteLaunchProfileResponse deleteLaunchProfile(launchProfileId, studioId, opts)



Permanently delete a launch profile.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteLaunchProfile(launchProfileId, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**DeleteLaunchProfileResponse**](DeleteLaunchProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLaunchProfileMember

> Object deleteLaunchProfileMember(launchProfileId, principalId, studioId, opts)



Delete a user from launch profile membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let principalId = "principalId_example"; // String | The principal ID. This currently supports a IAM Identity Center UserId. 
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteLaunchProfileMember(launchProfileId, principalId, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **principalId** | **String**| The principal ID. This currently supports a IAM Identity Center UserId.  | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStreamingImage

> DeleteStreamingImageResponse deleteStreamingImage(streamingImageId, studioId, opts)



Delete streaming image.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let streamingImageId = "streamingImageId_example"; // String | The streaming image ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteStreamingImage(streamingImageId, studioId, opts, (error, data, response) => {
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
 **streamingImageId** | **String**| The streaming image ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**DeleteStreamingImageResponse**](DeleteStreamingImageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStreamingSession

> DeleteStreamingSessionResponse deleteStreamingSession(sessionId, studioId, opts)



&lt;p&gt;Deletes streaming session resource.&lt;/p&gt; &lt;p&gt;After invoking this operation, use GetStreamingSession to poll the resource until it transitions to a &lt;code&gt;DELETED&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;A streaming session will count against your streaming session quota until it is marked &lt;code&gt;DELETED&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let sessionId = "sessionId_example"; // String | The streaming session ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteStreamingSession(sessionId, studioId, opts, (error, data, response) => {
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
 **sessionId** | **String**| The streaming session ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**DeleteStreamingSessionResponse**](DeleteStreamingSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStudio

> DeleteStudioResponse deleteStudio(studioId, opts)



Delete a studio resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteStudio(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**DeleteStudioResponse**](DeleteStudioResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStudioComponent

> DeleteStudioComponentResponse deleteStudioComponent(studioComponentId, studioId, opts)



Deletes a studio component resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioComponentId = "studioComponentId_example"; // String | The studio component ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteStudioComponent(studioComponentId, studioId, opts, (error, data, response) => {
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
 **studioComponentId** | **String**| The studio component ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**DeleteStudioComponentResponse**](DeleteStudioComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStudioMember

> Object deleteStudioMember(principalId, studioId, opts)



Delete a user from studio membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let principalId = "principalId_example"; // String | The principal ID. This currently supports a IAM Identity Center UserId. 
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.deleteStudioMember(principalId, studioId, opts, (error, data, response) => {
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
 **principalId** | **String**| The principal ID. This currently supports a IAM Identity Center UserId.  | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEula

> GetEulaResponse getEula(eulaId, opts)



Get EULA.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let eulaId = "eulaId_example"; // String | The EULA ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEula(eulaId, opts, (error, data, response) => {
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
 **eulaId** | **String**| The EULA ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEulaResponse**](GetEulaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLaunchProfile

> GetLaunchProfileResponse getLaunchProfile(launchProfileId, studioId, opts)



Get a launch profile.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLaunchProfile(launchProfileId, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLaunchProfileResponse**](GetLaunchProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLaunchProfileDetails

> GetLaunchProfileDetailsResponse getLaunchProfileDetails(launchProfileId, studioId, opts)



Launch profile details include the launch profile resource and summary information of resources that are used by, or available to, the launch profile. This includes the name and description of all studio components used by the launch profiles, and the name and description of streaming images that can be used with this launch profile.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLaunchProfileDetails(launchProfileId, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLaunchProfileDetailsResponse**](GetLaunchProfileDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLaunchProfileInitialization

> GetLaunchProfileInitializationResponse getLaunchProfileInitialization(launchProfileId, launchProfileProtocolVersions, launchPurpose, platform, studioId, opts)



Get a launch profile initialization.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let launchProfileProtocolVersions = ["null"]; // [String] | The launch profile protocol versions supported by the client.
let launchPurpose = "launchPurpose_example"; // String | The launch purpose.
let platform = "platform_example"; // String | The platform where this Launch Profile will be used, either Windows or Linux.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLaunchProfileInitialization(launchProfileId, launchProfileProtocolVersions, launchPurpose, platform, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **launchProfileProtocolVersions** | [**[String]**](String.md)| The launch profile protocol versions supported by the client. | 
 **launchPurpose** | **String**| The launch purpose. | 
 **platform** | **String**| The platform where this Launch Profile will be used, either Windows or Linux. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLaunchProfileInitializationResponse**](GetLaunchProfileInitializationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLaunchProfileMember

> GetLaunchProfileMemberResponse getLaunchProfileMember(launchProfileId, principalId, studioId, opts)



Get a user persona in launch profile membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let principalId = "principalId_example"; // String | The principal ID. This currently supports a IAM Identity Center UserId. 
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLaunchProfileMember(launchProfileId, principalId, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **principalId** | **String**| The principal ID. This currently supports a IAM Identity Center UserId.  | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLaunchProfileMemberResponse**](GetLaunchProfileMemberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStreamingImage

> GetStreamingImageResponse getStreamingImage(streamingImageId, studioId, opts)



Get streaming image.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let streamingImageId = "streamingImageId_example"; // String | The streaming image ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStreamingImage(streamingImageId, studioId, opts, (error, data, response) => {
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
 **streamingImageId** | **String**| The streaming image ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStreamingImageResponse**](GetStreamingImageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStreamingSession

> GetStreamingSessionResponse getStreamingSession(sessionId, studioId, opts)



&lt;p&gt;Gets StreamingSession resource.&lt;/p&gt; &lt;p&gt;Invoke this operation to poll for a streaming session state while creating or deleting a session.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let sessionId = "sessionId_example"; // String | The streaming session ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStreamingSession(sessionId, studioId, opts, (error, data, response) => {
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
 **sessionId** | **String**| The streaming session ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStreamingSessionResponse**](GetStreamingSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStreamingSessionBackup

> GetStreamingSessionBackupResponse getStreamingSessionBackup(backupId, studioId, opts)



&lt;p&gt;Gets &lt;code&gt;StreamingSessionBackup&lt;/code&gt; resource.&lt;/p&gt; &lt;p&gt;Invoke this operation to poll for a streaming session backup while stopping a streaming session.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let backupId = "backupId_example"; // String | The ID of the backup.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStreamingSessionBackup(backupId, studioId, opts, (error, data, response) => {
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
 **backupId** | **String**| The ID of the backup. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStreamingSessionBackupResponse**](GetStreamingSessionBackupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStreamingSessionStream

> GetStreamingSessionStreamResponse getStreamingSessionStream(sessionId, streamId, studioId, opts)



&lt;p&gt;Gets a StreamingSessionStream for a streaming session.&lt;/p&gt; &lt;p&gt;Invoke this operation to poll the resource after invoking &lt;code&gt;CreateStreamingSessionStream&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After the &lt;code&gt;StreamingSessionStream&lt;/code&gt; changes to the &lt;code&gt;READY&lt;/code&gt; state, the url property will contain a stream to be used with the DCV streaming client.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let sessionId = "sessionId_example"; // String | The streaming session ID.
let streamId = "streamId_example"; // String | The streaming session stream ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStreamingSessionStream(sessionId, streamId, studioId, opts, (error, data, response) => {
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
 **sessionId** | **String**| The streaming session ID. | 
 **streamId** | **String**| The streaming session stream ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStreamingSessionStreamResponse**](GetStreamingSessionStreamResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStudio

> GetStudioResponse getStudio(studioId, opts)



Get a studio resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStudio(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStudioResponse**](GetStudioResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStudioComponent

> GetStudioComponentResponse getStudioComponent(studioComponentId, studioId, opts)



Gets a studio component resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioComponentId = "studioComponentId_example"; // String | The studio component ID.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStudioComponent(studioComponentId, studioId, opts, (error, data, response) => {
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
 **studioComponentId** | **String**| The studio component ID. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStudioComponentResponse**](GetStudioComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStudioMember

> GetStudioMemberResponse getStudioMember(principalId, studioId, opts)



Get a user&#39;s membership in a studio.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let principalId = "principalId_example"; // String | The principal ID. This currently supports a IAM Identity Center UserId. 
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getStudioMember(principalId, studioId, opts, (error, data, response) => {
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
 **principalId** | **String**| The principal ID. This currently supports a IAM Identity Center UserId.  | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetStudioMemberResponse**](GetStudioMemberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEulaAcceptances

> ListEulaAcceptancesResponse listEulaAcceptances(studioId, opts)



List EULA acceptances.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'eulaIds': ["null"], // [String] | The list of EULA IDs that have been previously accepted.
  'nextToken': "nextToken_example" // String | The token for the next set of results, or null if there are no more results.
};
apiInstance.listEulaAcceptances(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **eulaIds** | [**[String]**](String.md)| The list of EULA IDs that have been previously accepted. | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 

### Return type

[**ListEulaAcceptancesResponse**](ListEulaAcceptancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEulas

> ListEulasResponse listEulas(opts)



List EULAs.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'eulaIds': ["null"], // [String] | The list of EULA IDs that should be returned
  'nextToken': "nextToken_example" // String | The token for the next set of results, or null if there are no more results.
};
apiInstance.listEulas(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **eulaIds** | [**[String]**](String.md)| The list of EULA IDs that should be returned | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 

### Return type

[**ListEulasResponse**](ListEulasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLaunchProfileMembers

> ListLaunchProfileMembersResponse listLaunchProfileMembers(launchProfileId, studioId, opts)



Get all users in a given launch profile membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The max number of results to return in the response.
  'nextToken': "nextToken_example" // String | The token for the next set of results, or null if there are no more results.
};
apiInstance.listLaunchProfileMembers(launchProfileId, studioId, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The max number of results to return in the response. | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 

### Return type

[**ListLaunchProfileMembersResponse**](ListLaunchProfileMembersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLaunchProfiles

> ListLaunchProfilesResponse listLaunchProfiles(studioId, opts)



List all the launch profiles a studio.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The max number of results to return in the response.
  'nextToken': "nextToken_example", // String | The token for the next set of results, or null if there are no more results.
  'principalId': "principalId_example", // String | The principal ID. This currently supports a IAM Identity Center UserId. 
  'states': [new AmazonNimbleStudio.LaunchProfileState()] // [LaunchProfileState] | Filter this request to launch profiles in any of the given states.
};
apiInstance.listLaunchProfiles(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The max number of results to return in the response. | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 
 **principalId** | **String**| The principal ID. This currently supports a IAM Identity Center UserId.  | [optional] 
 **states** | [**[LaunchProfileState]**](LaunchProfileState.md)| Filter this request to launch profiles in any of the given states. | [optional] 

### Return type

[**ListLaunchProfilesResponse**](ListLaunchProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStreamingImages

> ListStreamingImagesResponse listStreamingImages(studioId, opts)



&lt;p&gt;List the streaming image resources available to this studio.&lt;/p&gt; &lt;p&gt;This list will contain both images provided by Amazon Web Services, as well as streaming images that you have created in your studio.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results, or null if there are no more results.
  'owner': "owner_example" // String | Filter this request to streaming images with the given owner
};
apiInstance.listStreamingImages(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 
 **owner** | **String**| Filter this request to streaming images with the given owner | [optional] 

### Return type

[**ListStreamingImagesResponse**](ListStreamingImagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStreamingSessionBackups

> ListStreamingSessionBackupsResponse listStreamingSessionBackups(studioId, opts)



Lists the backups of a streaming session in a studio.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results, or null if there are no more results.
  'ownedBy': "ownedBy_example" // String | The user ID of the user that owns the streaming session.
};
apiInstance.listStreamingSessionBackups(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 
 **ownedBy** | **String**| The user ID of the user that owns the streaming session. | [optional] 

### Return type

[**ListStreamingSessionBackupsResponse**](ListStreamingSessionBackupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStreamingSessions

> ListStreamingSessionsResponse listStreamingSessions(studioId, opts)



Lists the streaming sessions in a studio.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'createdBy': "createdBy_example", // String | Filters the request to streaming sessions created by the given user.
  'nextToken': "nextToken_example", // String | The token for the next set of results, or null if there are no more results.
  'ownedBy': "ownedBy_example", // String | Filters the request to streaming session owned by the given user
  'sessionIds': "sessionIds_example" // String | Filters the request to only the provided session IDs.
};
apiInstance.listStreamingSessions(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **createdBy** | **String**| Filters the request to streaming sessions created by the given user. | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 
 **ownedBy** | **String**| Filters the request to streaming session owned by the given user | [optional] 
 **sessionIds** | **String**| Filters the request to only the provided session IDs. | [optional] 

### Return type

[**ListStreamingSessionsResponse**](ListStreamingSessionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStudioComponents

> ListStudioComponentsResponse listStudioComponents(studioId, opts)



Lists the &lt;code&gt;StudioComponents&lt;/code&gt; in a studio.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The max number of results to return in the response.
  'nextToken': "nextToken_example", // String | The token for the next set of results, or null if there are no more results.
  'states': [new AmazonNimbleStudio.StudioComponentState()], // [StudioComponentState] | Filters the request to studio components that are in one of the given states. 
  'types': [new AmazonNimbleStudio.StudioComponentType()] // [StudioComponentType] | Filters the request to studio components that are of one of the given types.
};
apiInstance.listStudioComponents(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The max number of results to return in the response. | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 
 **states** | [**[StudioComponentState]**](StudioComponentState.md)| Filters the request to studio components that are in one of the given states.  | [optional] 
 **types** | [**[StudioComponentType]**](StudioComponentType.md)| Filters the request to studio components that are of one of the given types. | [optional] 

### Return type

[**ListStudioComponentsResponse**](ListStudioComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStudioMembers

> ListStudioMembersResponse listStudioMembers(studioId, opts)



&lt;p&gt;Get all users in a given studio membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ListStudioMembers&lt;/code&gt; only returns admin members.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The max number of results to return in the response.
  'nextToken': "nextToken_example" // String | The token for the next set of results, or null if there are no more results.
};
apiInstance.listStudioMembers(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The max number of results to return in the response. | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 

### Return type

[**ListStudioMembersResponse**](ListStudioMembersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStudios

> ListStudiosResponse listStudios(opts)



List studios in your Amazon Web Services accounts in the requested Amazon Web Services Region.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | The token for the next set of results, or null if there are no more results.
};
apiInstance.listStudios(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results, or null if there are no more results. | [optional] 

### Return type

[**ListStudiosResponse**](ListStudiosResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



&lt;p&gt;Gets the tags for a resource, given its Amazon Resource Names (ARN).&lt;/p&gt; &lt;p&gt;This operation supports ARNs for all resource types in Nimble Studio that support tags, including studio, studio component, launch profile, streaming image, and streaming session. All resources that can be tagged will contain an ARN property, so you do not have to create this ARN yourself.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource for which you want to list tags.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource for which you want to list tags. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putLaunchProfileMembers

> Object putLaunchProfileMembers(launchProfileId, studioId, putLaunchProfileMembersRequest, opts)



Add/update users with given persona to launch profile membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let studioId = "studioId_example"; // String | The studio ID. 
let putLaunchProfileMembersRequest = new AmazonNimbleStudio.PutLaunchProfileMembersRequest(); // PutLaunchProfileMembersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.putLaunchProfileMembers(launchProfileId, studioId, putLaunchProfileMembersRequest, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **studioId** | **String**| The studio ID.  | 
 **putLaunchProfileMembersRequest** | [**PutLaunchProfileMembersRequest**](PutLaunchProfileMembersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putStudioMembers

> Object putStudioMembers(studioId, putStudioMembersRequest, opts)



Add/update users with given persona to studio membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let putStudioMembersRequest = new AmazonNimbleStudio.PutStudioMembersRequest(); // PutStudioMembersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.putStudioMembers(studioId, putStudioMembersRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **putStudioMembersRequest** | [**PutStudioMembersRequest**](PutStudioMembersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startStreamingSession

> StartStreamingSessionResponse startStreamingSession(sessionId, studioId, startStreamingSessionRequest, opts)



Transitions sessions from the &lt;code&gt;STOPPED&lt;/code&gt; state into the &lt;code&gt;READY&lt;/code&gt; state. The &lt;code&gt;START_IN_PROGRESS&lt;/code&gt; state is the intermediate state between the &lt;code&gt;STOPPED&lt;/code&gt; and &lt;code&gt;READY&lt;/code&gt; states.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let sessionId = "sessionId_example"; // String | The streaming session ID for the <code>StartStreamingSessionRequest</code>.
let studioId = "studioId_example"; // String | The studio ID for the StartStreamingSessionRequest.
let startStreamingSessionRequest = new AmazonNimbleStudio.StartStreamingSessionRequest(); // StartStreamingSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.startStreamingSession(sessionId, studioId, startStreamingSessionRequest, opts, (error, data, response) => {
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
 **sessionId** | **String**| The streaming session ID for the &lt;code&gt;StartStreamingSessionRequest&lt;/code&gt;. | 
 **studioId** | **String**| The studio ID for the StartStreamingSessionRequest. | 
 **startStreamingSessionRequest** | [**StartStreamingSessionRequest**](StartStreamingSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**StartStreamingSessionResponse**](StartStreamingSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startStudioSSOConfigurationRepair

> StartStudioSSOConfigurationRepairResponse startStudioSSOConfigurationRepair(studioId, opts)



&lt;p&gt;Repairs the IAM Identity Center configuration for a given studio.&lt;/p&gt; &lt;p&gt;If the studio has a valid IAM Identity Center configuration currently associated with it, this operation will fail with a validation error.&lt;/p&gt; &lt;p&gt;If the studio does not have a valid IAM Identity Center configuration currently associated with it, then a new IAM Identity Center application is created for the studio and the studio is changed to the &lt;code&gt;READY&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;After the IAM Identity Center application is repaired, you must use the Amazon Nimble Studio console to add administrators and users to your studio.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.startStudioSSOConfigurationRepair(studioId, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**StartStudioSSOConfigurationRepairResponse**](StartStudioSSOConfigurationRepairResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopStreamingSession

> StopStreamingSessionResponse stopStreamingSession(sessionId, studioId, stopStreamingSessionRequest, opts)



Transitions sessions from the &lt;code&gt;READY&lt;/code&gt; state into the &lt;code&gt;STOPPED&lt;/code&gt; state. The &lt;code&gt;STOP_IN_PROGRESS&lt;/code&gt; state is the intermediate state between the &lt;code&gt;READY&lt;/code&gt; and &lt;code&gt;STOPPED&lt;/code&gt; states.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let sessionId = "sessionId_example"; // String | The streaming session ID for the <code>StopStreamingSessionRequest</code>.
let studioId = "studioId_example"; // String | The studioId for the StopStreamingSessionRequest.
let stopStreamingSessionRequest = new AmazonNimbleStudio.StopStreamingSessionRequest(); // StopStreamingSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.stopStreamingSession(sessionId, studioId, stopStreamingSessionRequest, opts, (error, data, response) => {
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
 **sessionId** | **String**| The streaming session ID for the &lt;code&gt;StopStreamingSessionRequest&lt;/code&gt;. | 
 **studioId** | **String**| The studioId for the StopStreamingSessionRequest. | 
 **stopStreamingSessionRequest** | [**StopStreamingSessionRequest**](StopStreamingSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**StopStreamingSessionResponse**](StopStreamingSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Creates tags for a resource, given its ARN.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource you want to add tags to. 
let tagResourceRequest = new AmazonNimbleStudio.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource you want to add tags to.  | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Deletes the tags for a resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let resourceArn = "resourceArn_example"; // String | Identifies the Amazon Resource Name(ARN) key from which you are removing tags. 
let tagKeys = ["null"]; // [String] | One or more tag keys. Specify only the tag keys, not the tag values.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| Identifies the Amazon Resource Name(ARN) key from which you are removing tags.  | 
 **tagKeys** | [**[String]**](String.md)| One or more tag keys. Specify only the tag keys, not the tag values. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLaunchProfile

> UpdateLaunchProfileResponse updateLaunchProfile(launchProfileId, studioId, updateLaunchProfileRequest, opts)



Update a launch profile.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let studioId = "studioId_example"; // String | The studio ID. 
let updateLaunchProfileRequest = new AmazonNimbleStudio.UpdateLaunchProfileRequest(); // UpdateLaunchProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.updateLaunchProfile(launchProfileId, studioId, updateLaunchProfileRequest, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **studioId** | **String**| The studio ID.  | 
 **updateLaunchProfileRequest** | [**UpdateLaunchProfileRequest**](UpdateLaunchProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**UpdateLaunchProfileResponse**](UpdateLaunchProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLaunchProfileMember

> UpdateLaunchProfileMemberResponse updateLaunchProfileMember(launchProfileId, principalId, studioId, updateLaunchProfileMemberRequest, opts)



Update a user persona in launch profile membership.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let launchProfileId = "launchProfileId_example"; // String | The ID of the launch profile used to control access from the streaming session.
let principalId = "principalId_example"; // String | The principal ID. This currently supports a IAM Identity Center UserId. 
let studioId = "studioId_example"; // String | The studio ID. 
let updateLaunchProfileMemberRequest = new AmazonNimbleStudio.UpdateLaunchProfileMemberRequest(); // UpdateLaunchProfileMemberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.updateLaunchProfileMember(launchProfileId, principalId, studioId, updateLaunchProfileMemberRequest, opts, (error, data, response) => {
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
 **launchProfileId** | **String**| The ID of the launch profile used to control access from the streaming session. | 
 **principalId** | **String**| The principal ID. This currently supports a IAM Identity Center UserId.  | 
 **studioId** | **String**| The studio ID.  | 
 **updateLaunchProfileMemberRequest** | [**UpdateLaunchProfileMemberRequest**](UpdateLaunchProfileMemberRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**UpdateLaunchProfileMemberResponse**](UpdateLaunchProfileMemberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStreamingImage

> UpdateStreamingImageResponse updateStreamingImage(streamingImageId, studioId, updateStreamingImageRequest, opts)



Update streaming image.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let streamingImageId = "streamingImageId_example"; // String | The streaming image ID.
let studioId = "studioId_example"; // String | The studio ID. 
let updateStreamingImageRequest = new AmazonNimbleStudio.UpdateStreamingImageRequest(); // UpdateStreamingImageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.updateStreamingImage(streamingImageId, studioId, updateStreamingImageRequest, opts, (error, data, response) => {
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
 **streamingImageId** | **String**| The streaming image ID. | 
 **studioId** | **String**| The studio ID.  | 
 **updateStreamingImageRequest** | [**UpdateStreamingImageRequest**](UpdateStreamingImageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**UpdateStreamingImageResponse**](UpdateStreamingImageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStudio

> UpdateStudioResponse updateStudio(studioId, updateStudioRequest, opts)



&lt;p&gt;Update a Studio resource.&lt;/p&gt; &lt;p&gt;Currently, this operation only supports updating the displayName of your studio.&lt;/p&gt;

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioId = "studioId_example"; // String | The studio ID. 
let updateStudioRequest = new AmazonNimbleStudio.UpdateStudioRequest(); // UpdateStudioRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.updateStudio(studioId, updateStudioRequest, opts, (error, data, response) => {
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
 **studioId** | **String**| The studio ID.  | 
 **updateStudioRequest** | [**UpdateStudioRequest**](UpdateStudioRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**UpdateStudioResponse**](UpdateStudioResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStudioComponent

> UpdateStudioComponentResponse updateStudioComponent(studioComponentId, studioId, updateStudioComponentRequest, opts)



Updates a studio component resource.

### Example

```javascript
import AmazonNimbleStudio from 'amazon_nimble_studio';
let defaultClient = AmazonNimbleStudio.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonNimbleStudio.DefaultApi();
let studioComponentId = "studioComponentId_example"; // String | The studio component ID.
let studioId = "studioId_example"; // String | The studio ID. 
let updateStudioComponentRequest = new AmazonNimbleStudio.UpdateStudioComponentRequest(); // UpdateStudioComponentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientToken': "xAmzClientToken_example" // String | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency.
};
apiInstance.updateStudioComponent(studioComponentId, studioId, updateStudioComponentRequest, opts, (error, data, response) => {
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
 **studioComponentId** | **String**| The studio component ID. | 
 **studioId** | **String**| The studio ID.  | 
 **updateStudioComponentRequest** | [**UpdateStudioComponentRequest**](UpdateStudioComponentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientToken** | **String**| Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. | [optional] 

### Return type

[**UpdateStudioComponentResponse**](UpdateStudioComponentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

