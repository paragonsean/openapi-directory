# AwsSigner.DefaultApi

All URIs are relative to *http://signer.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addProfilePermission**](DefaultApi.md#addProfilePermission) | **POST** /signing-profiles/{profileName}/permissions | 
[**cancelSigningProfile**](DefaultApi.md#cancelSigningProfile) | **DELETE** /signing-profiles/{profileName} | 
[**describeSigningJob**](DefaultApi.md#describeSigningJob) | **GET** /signing-jobs/{jobId} | 
[**getRevocationStatus**](DefaultApi.md#getRevocationStatus) | **GET** /revocations#signatureTimestamp&amp;platformId&amp;profileVersionArn&amp;jobArn&amp;certificateHashes | 
[**getSigningPlatform**](DefaultApi.md#getSigningPlatform) | **GET** /signing-platforms/{platformId} | 
[**getSigningProfile**](DefaultApi.md#getSigningProfile) | **GET** /signing-profiles/{profileName} | 
[**listProfilePermissions**](DefaultApi.md#listProfilePermissions) | **GET** /signing-profiles/{profileName}/permissions | 
[**listSigningJobs**](DefaultApi.md#listSigningJobs) | **GET** /signing-jobs | 
[**listSigningPlatforms**](DefaultApi.md#listSigningPlatforms) | **GET** /signing-platforms | 
[**listSigningProfiles**](DefaultApi.md#listSigningProfiles) | **GET** /signing-profiles | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**putSigningProfile**](DefaultApi.md#putSigningProfile) | **PUT** /signing-profiles/{profileName} | 
[**removeProfilePermission**](DefaultApi.md#removeProfilePermission) | **DELETE** /signing-profiles/{profileName}/permissions/{statementId}#revisionId | 
[**revokeSignature**](DefaultApi.md#revokeSignature) | **PUT** /signing-jobs/{jobId}/revoke | 
[**revokeSigningProfile**](DefaultApi.md#revokeSigningProfile) | **PUT** /signing-profiles/{profileName}/revoke | 
[**signPayload**](DefaultApi.md#signPayload) | **POST** /signing-jobs/with-payload | 
[**startSigningJob**](DefaultApi.md#startSigningJob) | **POST** /signing-jobs | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 



## addProfilePermission

> AddProfilePermissionResponse addProfilePermission(profileName, addProfilePermissionRequest, opts)



Adds cross-account permissions to a signing profile.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | The human-readable name of the signing profile.
let addProfilePermissionRequest = new AwsSigner.AddProfilePermissionRequest(); // AddProfilePermissionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addProfilePermission(profileName, addProfilePermissionRequest, opts, (error, data, response) => {
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
 **profileName** | **String**| The human-readable name of the signing profile. | 
 **addProfilePermissionRequest** | [**AddProfilePermissionRequest**](AddProfilePermissionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddProfilePermissionResponse**](AddProfilePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelSigningProfile

> cancelSigningProfile(profileName, opts)



Changes the state of an &lt;code&gt;ACTIVE&lt;/code&gt; signing profile to &lt;code&gt;CANCELED&lt;/code&gt;. A canceled profile is still viewable with the &lt;code&gt;ListSigningProfiles&lt;/code&gt; operation, but it cannot perform new signing jobs, and is deleted two years after cancelation.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | The name of the signing profile to be canceled.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelSigningProfile(profileName, opts, (error, data, response) => {
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
 **profileName** | **String**| The name of the signing profile to be canceled. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeSigningJob

> DescribeSigningJobResponse describeSigningJob(jobId, opts)



Returns information about a specific code signing job. You specify the job by using the &lt;code&gt;jobId&lt;/code&gt; value that is returned by the &lt;a&gt;StartSigningJob&lt;/a&gt; operation. 

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let jobId = "jobId_example"; // String | The ID of the signing job on input.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSigningJob(jobId, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the signing job on input. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSigningJobResponse**](DescribeSigningJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRevocationStatus

> GetRevocationStatusResponse getRevocationStatus(signatureTimestamp, platformId, profileVersionArn, jobArn, certificateHashes, opts)



Retrieves the revocation status of one or more of the signing profile, signing job, and signing certificate.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let signatureTimestamp = new Date("2013-10-20T19:20:30+01:00"); // Date | The timestamp of the signature that validates the profile or job.
let platformId = "platformId_example"; // String | The ID of a signing platform. 
let profileVersionArn = "profileVersionArn_example"; // String | The version of a signing profile.
let jobArn = "jobArn_example"; // String | The ARN of a signing job.
let certificateHashes = ["null"]; // [String] | <p>A list of composite signed hashes that identify certificates.</p> <p>A certificate identifier consists of a subject certificate TBS hash (signed by the parent CA) combined with a parent CA TBS hash (signed by the parent CA’s CA). Root certificates are defined as their own CA.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRevocationStatus(signatureTimestamp, platformId, profileVersionArn, jobArn, certificateHashes, opts, (error, data, response) => {
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
 **signatureTimestamp** | **Date**| The timestamp of the signature that validates the profile or job. | 
 **platformId** | **String**| The ID of a signing platform.  | 
 **profileVersionArn** | **String**| The version of a signing profile. | 
 **jobArn** | **String**| The ARN of a signing job. | 
 **certificateHashes** | [**[String]**](String.md)| &lt;p&gt;A list of composite signed hashes that identify certificates.&lt;/p&gt; &lt;p&gt;A certificate identifier consists of a subject certificate TBS hash (signed by the parent CA) combined with a parent CA TBS hash (signed by the parent CA’s CA). Root certificates are defined as their own CA.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRevocationStatusResponse**](GetRevocationStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSigningPlatform

> GetSigningPlatformResponse getSigningPlatform(platformId, opts)



Returns information on a specific signing platform.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let platformId = "platformId_example"; // String | The ID of the target signing platform.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSigningPlatform(platformId, opts, (error, data, response) => {
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
 **platformId** | **String**| The ID of the target signing platform. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSigningPlatformResponse**](GetSigningPlatformResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSigningProfile

> GetSigningProfileResponse getSigningProfile(profileName, opts)



Returns information on a specific signing profile.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | The name of the target signing profile.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'profileOwner': "profileOwner_example" // String | The AWS account ID of the profile owner.
};
apiInstance.getSigningProfile(profileName, opts, (error, data, response) => {
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
 **profileName** | **String**| The name of the target signing profile. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **profileOwner** | **String**| The AWS account ID of the profile owner. | [optional] 

### Return type

[**GetSigningProfileResponse**](GetSigningProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProfilePermissions

> ListProfilePermissionsResponse listProfilePermissions(profileName, opts)



Lists the cross-account permissions associated with a signing profile.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | Name of the signing profile containing the cross-account permissions.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | String for specifying the next set of paginated results.
};
apiInstance.listProfilePermissions(profileName, opts, (error, data, response) => {
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
 **profileName** | **String**| Name of the signing profile containing the cross-account permissions. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| String for specifying the next set of paginated results. | [optional] 

### Return type

[**ListProfilePermissionsResponse**](ListProfilePermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSigningJobs

> ListSigningJobsResponse listSigningJobs(opts)



Lists all your signing jobs. You can use the &lt;code&gt;maxResults&lt;/code&gt; parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, code signing returns a &lt;code&gt;nextToken&lt;/code&gt; value. Use this value in subsequent calls to &lt;code&gt;ListSigningJobs&lt;/code&gt; to fetch the remaining values. You can continue calling &lt;code&gt;ListSigningJobs&lt;/code&gt; with your &lt;code&gt;maxResults&lt;/code&gt; parameter and with new values that code signing returns in the &lt;code&gt;nextToken&lt;/code&gt; parameter until all of your signing jobs have been returned. 

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'status': "status_example", // String | A status value with which to filter your results.
  'platformId': "platformId_example", // String | The ID of microcontroller platform that you specified for the distribution of your code image.
  'requestedBy': "requestedBy_example", // String | The IAM principal that requested the signing job.
  'maxResults': 56, // Number | Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the <code>nextToken</code> element is set in the response. Use the <code>nextToken</code> value in a subsequent request to retrieve additional items. 
  'nextToken': "nextToken_example", // String | String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.
  'isRevoked': true, // Boolean | Filters results to return only signing jobs with revoked signatures.
  'signatureExpiresBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filters results to return only signing jobs with signatures expiring before a specified timestamp.
  'signatureExpiresAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filters results to return only signing jobs with signatures expiring after a specified timestamp.
  'jobInvoker': "jobInvoker_example" // String | Filters results to return only signing jobs initiated by a specified IAM entity.
};
apiInstance.listSigningJobs(opts, (error, data, response) => {
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
 **status** | **String**| A status value with which to filter your results. | [optional] 
 **platformId** | **String**| The ID of microcontroller platform that you specified for the distribution of your code image. | [optional] 
 **requestedBy** | **String**| The IAM principal that requested the signing job. | [optional] 
 **maxResults** | **Number**| Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is set in the response. Use the &lt;code&gt;nextToken&lt;/code&gt; value in a subsequent request to retrieve additional items.  | [optional] 
 **nextToken** | **String**| String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of &lt;code&gt;nextToken&lt;/code&gt; from the response that you just received. | [optional] 
 **isRevoked** | **Boolean**| Filters results to return only signing jobs with revoked signatures. | [optional] 
 **signatureExpiresBefore** | **Date**| Filters results to return only signing jobs with signatures expiring before a specified timestamp. | [optional] 
 **signatureExpiresAfter** | **Date**| Filters results to return only signing jobs with signatures expiring after a specified timestamp. | [optional] 
 **jobInvoker** | **String**| Filters results to return only signing jobs initiated by a specified IAM entity. | [optional] 

### Return type

[**ListSigningJobsResponse**](ListSigningJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSigningPlatforms

> ListSigningPlatformsResponse listSigningPlatforms(opts)



Lists all signing platforms available in code signing that match the request parameters. If additional jobs remain to be listed, code signing returns a &lt;code&gt;nextToken&lt;/code&gt; value. Use this value in subsequent calls to &lt;code&gt;ListSigningJobs&lt;/code&gt; to fetch the remaining values. You can continue calling &lt;code&gt;ListSigningJobs&lt;/code&gt; with your &lt;code&gt;maxResults&lt;/code&gt; parameter and with new values that code signing returns in the &lt;code&gt;nextToken&lt;/code&gt; parameter until all of your signing jobs have been returned.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'category': "category_example", // String | The category type of a signing platform.
  'partner': "partner_example", // String | Any partner entities connected to a signing platform.
  'target': "target_example", // String | The validation template that is used by the target signing platform.
  'maxResults': 56, // Number | The maximum number of results to be returned by this operation.
  'nextToken': "nextToken_example" // String | Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.
};
apiInstance.listSigningPlatforms(opts, (error, data, response) => {
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
 **category** | **String**| The category type of a signing platform. | [optional] 
 **partner** | **String**| Any partner entities connected to a signing platform. | [optional] 
 **target** | **String**| The validation template that is used by the target signing platform. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned by this operation. | [optional] 
 **nextToken** | **String**| Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of &lt;code&gt;nextToken&lt;/code&gt; from the response that you just received. | [optional] 

### Return type

[**ListSigningPlatformsResponse**](ListSigningPlatformsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSigningProfiles

> ListSigningProfilesResponse listSigningProfiles(opts)



Lists all available signing profiles in your AWS account. Returns only profiles with an &lt;code&gt;ACTIVE&lt;/code&gt; status unless the &lt;code&gt;includeCanceled&lt;/code&gt; request field is set to &lt;code&gt;true&lt;/code&gt;. If additional jobs remain to be listed, code signing returns a &lt;code&gt;nextToken&lt;/code&gt; value. Use this value in subsequent calls to &lt;code&gt;ListSigningJobs&lt;/code&gt; to fetch the remaining values. You can continue calling &lt;code&gt;ListSigningJobs&lt;/code&gt; with your &lt;code&gt;maxResults&lt;/code&gt; parameter and with new values that code signing returns in the &lt;code&gt;nextToken&lt;/code&gt; parameter until all of your signing jobs have been returned.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'includeCanceled': true, // Boolean | Designates whether to include profiles with the status of <code>CANCELED</code>.
  'maxResults': 56, // Number | The maximum number of profiles to be returned.
  'nextToken': "nextToken_example", // String | Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.
  'platformId': "platformId_example", // String | Filters results to return only signing jobs initiated for a specified signing platform.
  'statuses': [new AwsSigner.SigningProfileStatus()] // [SigningProfileStatus] | Filters results to return only signing jobs with statuses in the specified list.
};
apiInstance.listSigningProfiles(opts, (error, data, response) => {
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
 **includeCanceled** | **Boolean**| Designates whether to include profiles with the status of &lt;code&gt;CANCELED&lt;/code&gt;. | [optional] 
 **maxResults** | **Number**| The maximum number of profiles to be returned. | [optional] 
 **nextToken** | **String**| Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of &lt;code&gt;nextToken&lt;/code&gt; from the response that you just received. | [optional] 
 **platformId** | **String**| Filters results to return only signing jobs initiated for a specified signing platform. | [optional] 
 **statuses** | [**[SigningProfileStatus]**](SigningProfileStatus.md)| Filters results to return only signing jobs with statuses in the specified list. | [optional] 

### Return type

[**ListSigningProfilesResponse**](ListSigningProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Returns a list of the tags associated with a signing profile resource.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) for the signing profile.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) for the signing profile. | 
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


## putSigningProfile

> PutSigningProfileResponse putSigningProfile(profileName, putSigningProfileRequest, opts)



Creates a signing profile. A signing profile is a code signing template that can be used to carry out a pre-defined signing job. 

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | The name of the signing profile to be created.
let putSigningProfileRequest = new AwsSigner.PutSigningProfileRequest(); // PutSigningProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSigningProfile(profileName, putSigningProfileRequest, opts, (error, data, response) => {
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
 **profileName** | **String**| The name of the signing profile to be created. | 
 **putSigningProfileRequest** | [**PutSigningProfileRequest**](PutSigningProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutSigningProfileResponse**](PutSigningProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeProfilePermission

> RemoveProfilePermissionResponse removeProfilePermission(profileName, revisionId, statementId, opts)



Removes cross-account permissions from a signing profile.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | A human-readable name for the signing profile with permissions to be removed.
let revisionId = "revisionId_example"; // String | An identifier for the current revision of the signing profile permissions.
let statementId = "statementId_example"; // String | A unique identifier for the cross-account permissions statement.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeProfilePermission(profileName, revisionId, statementId, opts, (error, data, response) => {
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
 **profileName** | **String**| A human-readable name for the signing profile with permissions to be removed. | 
 **revisionId** | **String**| An identifier for the current revision of the signing profile permissions. | 
 **statementId** | **String**| A unique identifier for the cross-account permissions statement. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveProfilePermissionResponse**](RemoveProfilePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## revokeSignature

> revokeSignature(jobId, revokeSignatureRequest, opts)



Changes the state of a signing job to REVOKED. This indicates that the signature is no longer valid.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let jobId = "jobId_example"; // String | ID of the signing job to be revoked.
let revokeSignatureRequest = new AwsSigner.RevokeSignatureRequest(); // RevokeSignatureRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.revokeSignature(jobId, revokeSignatureRequest, opts, (error, data, response) => {
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
 **jobId** | **String**| ID of the signing job to be revoked. | 
 **revokeSignatureRequest** | [**RevokeSignatureRequest**](RevokeSignatureRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeSigningProfile

> revokeSigningProfile(profileName, revokeSigningProfileRequest, opts)



Changes the state of a signing profile to REVOKED. This indicates that signatures generated using the signing profile after an effective start date are no longer valid.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let profileName = "profileName_example"; // String | The name of the signing profile to be revoked.
let revokeSigningProfileRequest = new AwsSigner.RevokeSigningProfileRequest(); // RevokeSigningProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.revokeSigningProfile(profileName, revokeSigningProfileRequest, opts, (error, data, response) => {
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
 **profileName** | **String**| The name of the signing profile to be revoked. | 
 **revokeSigningProfileRequest** | [**RevokeSigningProfileRequest**](RevokeSigningProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signPayload

> SignPayloadResponse signPayload(signPayloadRequest, opts)



Signs a binary payload and returns a signature envelope.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let signPayloadRequest = new AwsSigner.SignPayloadRequest(); // SignPayloadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.signPayload(signPayloadRequest, opts, (error, data, response) => {
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
 **signPayloadRequest** | [**SignPayloadRequest**](SignPayloadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SignPayloadResponse**](SignPayloadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startSigningJob

> StartSigningJobResponse startSigningJob(startSigningJobRequest, opts)



&lt;p&gt;Initiates a signing job to be performed on the code provided. Signing jobs are viewable by the &lt;code&gt;ListSigningJobs&lt;/code&gt; operation for two years after they are performed. Note the following requirements: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; You must create an Amazon S3 source bucket. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html\&quot;&gt;Creating a Bucket&lt;/a&gt; in the &lt;i&gt;Amazon S3 Getting Started Guide&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your S3 source bucket must be version enabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must create an S3 destination bucket. Code signing uses your S3 destination bucket to write your signed code.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You specify the name of the source and destination buckets when calling the &lt;code&gt;StartSigningJob&lt;/code&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must also specify a request token that identifies your request to code signing.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can call the &lt;a&gt;DescribeSigningJob&lt;/a&gt; and the &lt;a&gt;ListSigningJobs&lt;/a&gt; actions after you call &lt;code&gt;StartSigningJob&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a Java example that shows how to use this action, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/signer/latest/developerguide/api-startsigningjob.html\&quot;&gt;StartSigningJob&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let startSigningJobRequest = new AwsSigner.StartSigningJobRequest(); // StartSigningJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSigningJob(startSigningJobRequest, opts, (error, data, response) => {
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
 **startSigningJobRequest** | [**StartSigningJobRequest**](StartSigningJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSigningJobResponse**](StartSigningJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds one or more tags to a signing profile. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value. To specify the signing profile, use its Amazon Resource Name (ARN). To specify the tag, use a key-value pair.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) for the signing profile.
let tagResourceRequest = new AwsSigner.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) for the signing profile. | 
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



Removes one or more tags from a signing profile. To remove the tags, specify a list of tag keys.

### Example

```javascript
import AwsSigner from 'aws_signer';
let defaultClient = AwsSigner.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSigner.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) for the signing profile.
let tagKeys = ["null"]; // [String] | A list of tag keys to be removed from the signing profile.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) for the signing profile. | 
 **tagKeys** | [**[String]**](String.md)| A list of tag keys to be removed from the signing profile. | 
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

