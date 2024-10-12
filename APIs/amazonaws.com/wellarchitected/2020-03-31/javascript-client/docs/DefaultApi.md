# AwsWellArchitectedTool.DefaultApi

All URIs are relative to *http://wellarchitected.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateLenses**](DefaultApi.md#associateLenses) | **PATCH** /workloads/{WorkloadId}/associateLenses | 
[**associateProfiles**](DefaultApi.md#associateProfiles) | **PATCH** /workloads/{WorkloadId}/associateProfiles | 
[**createLensShare**](DefaultApi.md#createLensShare) | **POST** /lenses/{LensAlias}/shares | 
[**createLensVersion**](DefaultApi.md#createLensVersion) | **POST** /lenses/{LensAlias}/versions | 
[**createMilestone**](DefaultApi.md#createMilestone) | **POST** /workloads/{WorkloadId}/milestones | 
[**createProfile**](DefaultApi.md#createProfile) | **POST** /profiles | 
[**createProfileShare**](DefaultApi.md#createProfileShare) | **POST** /profiles/{ProfileArn}/shares | 
[**createWorkload**](DefaultApi.md#createWorkload) | **POST** /workloads | 
[**createWorkloadShare**](DefaultApi.md#createWorkloadShare) | **POST** /workloads/{WorkloadId}/shares | 
[**deleteLens**](DefaultApi.md#deleteLens) | **DELETE** /lenses/{LensAlias}#ClientRequestToken&amp;LensStatus | 
[**deleteLensShare**](DefaultApi.md#deleteLensShare) | **DELETE** /lenses/{LensAlias}/shares/{ShareId}#ClientRequestToken | 
[**deleteProfile**](DefaultApi.md#deleteProfile) | **DELETE** /profiles/{ProfileArn}#ClientRequestToken | 
[**deleteProfileShare**](DefaultApi.md#deleteProfileShare) | **DELETE** /profiles/{ProfileArn}/shares/{ShareId}#ClientRequestToken | 
[**deleteWorkload**](DefaultApi.md#deleteWorkload) | **DELETE** /workloads/{WorkloadId}#ClientRequestToken | 
[**deleteWorkloadShare**](DefaultApi.md#deleteWorkloadShare) | **DELETE** /workloads/{WorkloadId}/shares/{ShareId}#ClientRequestToken | 
[**disassociateLenses**](DefaultApi.md#disassociateLenses) | **PATCH** /workloads/{WorkloadId}/disassociateLenses | 
[**disassociateProfiles**](DefaultApi.md#disassociateProfiles) | **PATCH** /workloads/{WorkloadId}/disassociateProfiles | 
[**exportLens**](DefaultApi.md#exportLens) | **GET** /lenses/{LensAlias}/export | 
[**getAnswer**](DefaultApi.md#getAnswer) | **GET** /workloads/{WorkloadId}/lensReviews/{LensAlias}/answers/{QuestionId} | 
[**getConsolidatedReport**](DefaultApi.md#getConsolidatedReport) | **GET** /consolidatedReport#Format | 
[**getLens**](DefaultApi.md#getLens) | **GET** /lenses/{LensAlias} | 
[**getLensReview**](DefaultApi.md#getLensReview) | **GET** /workloads/{WorkloadId}/lensReviews/{LensAlias} | 
[**getLensReviewReport**](DefaultApi.md#getLensReviewReport) | **GET** /workloads/{WorkloadId}/lensReviews/{LensAlias}/report | 
[**getLensVersionDifference**](DefaultApi.md#getLensVersionDifference) | **GET** /lenses/{LensAlias}/versionDifference | 
[**getMilestone**](DefaultApi.md#getMilestone) | **GET** /workloads/{WorkloadId}/milestones/{MilestoneNumber} | 
[**getProfile**](DefaultApi.md#getProfile) | **GET** /profiles/{ProfileArn} | 
[**getProfileTemplate**](DefaultApi.md#getProfileTemplate) | **GET** /profileTemplate | 
[**getWorkload**](DefaultApi.md#getWorkload) | **GET** /workloads/{WorkloadId} | 
[**importLens**](DefaultApi.md#importLens) | **PUT** /importLens | 
[**listAnswers**](DefaultApi.md#listAnswers) | **GET** /workloads/{WorkloadId}/lensReviews/{LensAlias}/answers | 
[**listCheckDetails**](DefaultApi.md#listCheckDetails) | **POST** /workloads/{WorkloadId}/checks | 
[**listCheckSummaries**](DefaultApi.md#listCheckSummaries) | **POST** /workloads/{WorkloadId}/checkSummaries | 
[**listLensReviewImprovements**](DefaultApi.md#listLensReviewImprovements) | **GET** /workloads/{WorkloadId}/lensReviews/{LensAlias}/improvements | 
[**listLensReviews**](DefaultApi.md#listLensReviews) | **GET** /workloads/{WorkloadId}/lensReviews | 
[**listLensShares**](DefaultApi.md#listLensShares) | **GET** /lenses/{LensAlias}/shares | 
[**listLenses**](DefaultApi.md#listLenses) | **GET** /lenses | 
[**listMilestones**](DefaultApi.md#listMilestones) | **POST** /workloads/{WorkloadId}/milestonesSummaries | 
[**listNotifications**](DefaultApi.md#listNotifications) | **POST** /notifications | 
[**listProfileNotifications**](DefaultApi.md#listProfileNotifications) | **GET** /profileNotifications/ | 
[**listProfileShares**](DefaultApi.md#listProfileShares) | **GET** /profiles/{ProfileArn}/shares | 
[**listProfiles**](DefaultApi.md#listProfiles) | **GET** /profileSummaries | 
[**listShareInvitations**](DefaultApi.md#listShareInvitations) | **GET** /shareInvitations | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{WorkloadArn} | 
[**listWorkloadShares**](DefaultApi.md#listWorkloadShares) | **GET** /workloads/{WorkloadId}/shares | 
[**listWorkloads**](DefaultApi.md#listWorkloads) | **POST** /workloadsSummaries | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{WorkloadArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{WorkloadArn}#tagKeys | 
[**updateAnswer**](DefaultApi.md#updateAnswer) | **PATCH** /workloads/{WorkloadId}/lensReviews/{LensAlias}/answers/{QuestionId} | 
[**updateGlobalSettings**](DefaultApi.md#updateGlobalSettings) | **PATCH** /global-settings | 
[**updateLensReview**](DefaultApi.md#updateLensReview) | **PATCH** /workloads/{WorkloadId}/lensReviews/{LensAlias} | 
[**updateProfile**](DefaultApi.md#updateProfile) | **PATCH** /profiles/{ProfileArn} | 
[**updateShareInvitation**](DefaultApi.md#updateShareInvitation) | **PATCH** /shareInvitations/{ShareInvitationId} | 
[**updateWorkload**](DefaultApi.md#updateWorkload) | **PATCH** /workloads/{WorkloadId} | 
[**updateWorkloadShare**](DefaultApi.md#updateWorkloadShare) | **PATCH** /workloads/{WorkloadId}/shares/{ShareId} | 
[**upgradeLensReview**](DefaultApi.md#upgradeLensReview) | **PUT** /workloads/{WorkloadId}/lensReviews/{LensAlias}/upgrade | 
[**upgradeProfileVersion**](DefaultApi.md#upgradeProfileVersion) | **PUT** /workloads/{WorkloadId}/profiles/{ProfileArn}/upgrade | 



## associateLenses

> associateLenses(workloadId, associateLensesRequest, opts)



&lt;p&gt;Associate a lens to a workload.&lt;/p&gt; &lt;p&gt;Up to 10 lenses can be associated with a workload in a single API operation. A maximum of 20 lenses can be associated with a workload.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By accessing and/or applying custom lenses created by another Amazon Web Services user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the Amazon Web Services Customer Agreement. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let associateLensesRequest = new AwsWellArchitectedTool.AssociateLensesRequest(); // AssociateLensesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateLenses(workloadId, associateLensesRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **associateLensesRequest** | [**AssociateLensesRequest**](AssociateLensesRequest.md)|  | 
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


## associateProfiles

> associateProfiles(workloadId, associateProfilesRequest, opts)



Associate a profile with a workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let associateProfilesRequest = new AwsWellArchitectedTool.AssociateProfilesRequest(); // AssociateProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateProfiles(workloadId, associateProfilesRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **associateProfilesRequest** | [**AssociateProfilesRequest**](AssociateProfilesRequest.md)|  | 
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


## createLensShare

> CreateLensShareOutput createLensShare(lensAlias, createLensShareRequest, opts)



&lt;p&gt;Create a lens share.&lt;/p&gt; &lt;p&gt;The owner of a lens can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be shared.&lt;/p&gt; &lt;p&gt; Shared access to a lens is not removed until the lens invitation is deleted.&lt;/p&gt; &lt;p&gt;If you share a lens with an organization or OU, all accounts in the organization or OU are granted access to the lens.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html\&quot;&gt;Sharing a custom lens&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let createLensShareRequest = new AwsWellArchitectedTool.CreateLensShareRequest(); // CreateLensShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLensShare(lensAlias, createLensShareRequest, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **createLensShareRequest** | [**CreateLensShareRequest**](CreateLensShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLensShareOutput**](CreateLensShareOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLensVersion

> CreateLensVersionOutput createLensVersion(lensAlias, createLensVersionRequest, opts)



&lt;p&gt;Create a new lens version.&lt;/p&gt; &lt;p&gt;A lens can have up to 100 versions.&lt;/p&gt; &lt;p&gt;Use this operation to publish a new lens version after you have imported a lens. The &lt;code&gt;LensAlias&lt;/code&gt; is used to identify the lens to be published. The owner of a lens can share the lens with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Only the owner of a lens can delete it. &lt;/p&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let createLensVersionRequest = new AwsWellArchitectedTool.CreateLensVersionRequest(); // CreateLensVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLensVersion(lensAlias, createLensVersionRequest, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **createLensVersionRequest** | [**CreateLensVersionRequest**](CreateLensVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLensVersionOutput**](CreateLensVersionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMilestone

> CreateMilestoneOutput createMilestone(workloadId, createMilestoneRequest, opts)



Create a milestone for an existing workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let createMilestoneRequest = new AwsWellArchitectedTool.CreateMilestoneRequest(); // CreateMilestoneRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMilestone(workloadId, createMilestoneRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **createMilestoneRequest** | [**CreateMilestoneRequest**](CreateMilestoneRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMilestoneOutput**](CreateMilestoneOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProfile

> CreateProfileOutput createProfile(createProfileRequest, opts)



Create a profile.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let createProfileRequest = new AwsWellArchitectedTool.CreateProfileRequest(); // CreateProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProfile(createProfileRequest, opts, (error, data, response) => {
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
 **createProfileRequest** | [**CreateProfileRequest**](CreateProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProfileOutput**](CreateProfileOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProfileShare

> CreateProfileShareOutput createProfileShare(profileArn, createLensShareRequest, opts)



Create a profile share.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let profileArn = "profileArn_example"; // String | The profile ARN.
let createLensShareRequest = new AwsWellArchitectedTool.CreateLensShareRequest(); // CreateLensShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProfileShare(profileArn, createLensShareRequest, opts, (error, data, response) => {
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
 **profileArn** | **String**| The profile ARN. | 
 **createLensShareRequest** | [**CreateLensShareRequest**](CreateLensShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProfileShareOutput**](CreateProfileShareOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWorkload

> CreateWorkloadOutput createWorkload(createWorkloadRequest, opts)



&lt;p&gt;Create a new workload.&lt;/p&gt; &lt;p&gt;The owner of a workload can share the workload with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Only the owner of a workload can delete it.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload.html\&quot;&gt;Defining a Workload&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Either &lt;code&gt;AwsRegions&lt;/code&gt;, &lt;code&gt;NonAwsRegions&lt;/code&gt;, or both must be specified when creating a workload.&lt;/p&gt; &lt;p&gt;You also must specify &lt;code&gt;ReviewOwner&lt;/code&gt;, even though the parameter is listed as not being required in the following section. &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let createWorkloadRequest = new AwsWellArchitectedTool.CreateWorkloadRequest(); // CreateWorkloadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWorkload(createWorkloadRequest, opts, (error, data, response) => {
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
 **createWorkloadRequest** | [**CreateWorkloadRequest**](CreateWorkloadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWorkloadOutput**](CreateWorkloadOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWorkloadShare

> CreateWorkloadShareOutput createWorkloadShare(workloadId, createWorkloadShareRequest, opts)



&lt;p&gt;Create a workload share.&lt;/p&gt; &lt;p&gt;The owner of a workload can share it with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Shared access to a workload is not removed until the workload invitation is deleted.&lt;/p&gt; &lt;p&gt;If you share a workload with an organization or OU, all accounts in the organization or OU are granted access to the workload.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html\&quot;&gt;Sharing a workload&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let createWorkloadShareRequest = new AwsWellArchitectedTool.CreateWorkloadShareRequest(); // CreateWorkloadShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWorkloadShare(workloadId, createWorkloadShareRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **createWorkloadShareRequest** | [**CreateWorkloadShareRequest**](CreateWorkloadShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWorkloadShareOutput**](CreateWorkloadShareOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLens

> deleteLens(lensAlias, clientRequestToken, lensStatus, opts)



&lt;p&gt;Delete an existing lens.&lt;/p&gt; &lt;p&gt;Only the owner of a lens can delete it. After the lens is deleted, Amazon Web Services accounts and users that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let clientRequestToken = "clientRequestToken_example"; // String | 
let lensStatus = "lensStatus_example"; // String | The status of the lens to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLens(lensAlias, clientRequestToken, lensStatus, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **clientRequestToken** | **String**|  | 
 **lensStatus** | **String**| The status of the lens to be deleted. | 
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


## deleteLensShare

> deleteLensShare(shareId, lensAlias, clientRequestToken, opts)



&lt;p&gt;Delete a lens share.&lt;/p&gt; &lt;p&gt;After the lens share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let shareId = "shareId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let clientRequestToken = "clientRequestToken_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLensShare(shareId, lensAlias, clientRequestToken, opts, (error, data, response) => {
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
 **shareId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **clientRequestToken** | **String**|  | 
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


## deleteProfile

> deleteProfile(profileArn, clientRequestToken, opts)



&lt;p&gt;Delete a profile.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your profile with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your profile available to those other accounts. Those other accounts may continue to access and use your shared profile even if you delete the profile from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let profileArn = "profileArn_example"; // String | The profile ARN.
let clientRequestToken = "clientRequestToken_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProfile(profileArn, clientRequestToken, opts, (error, data, response) => {
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
 **profileArn** | **String**| The profile ARN. | 
 **clientRequestToken** | **String**|  | 
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


## deleteProfileShare

> deleteProfileShare(shareId, profileArn, clientRequestToken, opts)



Delete a profile share.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let shareId = "shareId_example"; // String | 
let profileArn = "profileArn_example"; // String | The profile ARN.
let clientRequestToken = "clientRequestToken_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProfileShare(shareId, profileArn, clientRequestToken, opts, (error, data, response) => {
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
 **shareId** | **String**|  | 
 **profileArn** | **String**| The profile ARN. | 
 **clientRequestToken** | **String**|  | 
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


## deleteWorkload

> deleteWorkload(workloadId, clientRequestToken, opts)



Delete an existing workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let clientRequestToken = "clientRequestToken_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWorkload(workloadId, clientRequestToken, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **clientRequestToken** | **String**|  | 
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


## deleteWorkloadShare

> deleteWorkloadShare(shareId, workloadId, clientRequestToken, opts)



Delete a workload share.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let shareId = "shareId_example"; // String | 
let workloadId = "workloadId_example"; // String | 
let clientRequestToken = "clientRequestToken_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWorkloadShare(shareId, workloadId, clientRequestToken, opts, (error, data, response) => {
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
 **shareId** | **String**|  | 
 **workloadId** | **String**|  | 
 **clientRequestToken** | **String**|  | 
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


## disassociateLenses

> disassociateLenses(workloadId, associateLensesRequest, opts)



&lt;p&gt;Disassociate a lens from a workload.&lt;/p&gt; &lt;p&gt;Up to 10 lenses can be disassociated from a workload in a single API operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon Web Services Well-Architected Framework lens (&lt;code&gt;wellarchitected&lt;/code&gt;) cannot be removed from a workload.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let associateLensesRequest = new AwsWellArchitectedTool.AssociateLensesRequest(); // AssociateLensesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateLenses(workloadId, associateLensesRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **associateLensesRequest** | [**AssociateLensesRequest**](AssociateLensesRequest.md)|  | 
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


## disassociateProfiles

> disassociateProfiles(workloadId, disassociateProfilesRequest, opts)



Disassociate a profile from a workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let disassociateProfilesRequest = new AwsWellArchitectedTool.DisassociateProfilesRequest(); // DisassociateProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateProfiles(workloadId, disassociateProfilesRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **disassociateProfilesRequest** | [**DisassociateProfilesRequest**](DisassociateProfilesRequest.md)|  | 
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


## exportLens

> ExportLensOutput exportLens(lensAlias, opts)



&lt;p&gt;Export an existing lens.&lt;/p&gt; &lt;p&gt;Only the owner of a lens can export it. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be exported.&lt;/p&gt; &lt;p&gt;Lenses are defined in JSON. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\&quot;&gt;JSON format specification&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'lensVersion': "lensVersion_example" // String | The lens version to be exported.
};
apiInstance.exportLens(lensAlias, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **lensVersion** | **String**| The lens version to be exported. | [optional] 

### Return type

[**ExportLensOutput**](ExportLensOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnswer

> GetAnswerOutput getAnswer(workloadId, lensAlias, questionId, opts)



Get the answer to a specific question in a workload review.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let questionId = "questionId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'milestoneNumber': 56 // Number | 
};
apiInstance.getAnswer(workloadId, lensAlias, questionId, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **questionId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **milestoneNumber** | **Number**|  | [optional] 

### Return type

[**GetAnswerOutput**](GetAnswerOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConsolidatedReport

> GetConsolidatedReportOutput getConsolidatedReport(format, opts)



&lt;p&gt;Get a consolidated report of your workloads.&lt;/p&gt; &lt;p&gt;You can optionally choose to include workloads that have been shared with you.&lt;/p&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let format = "format_example"; // String | <p>The format of the consolidated report.</p> <p>For <code>PDF</code>, <code>Base64String</code> is returned. For <code>JSON</code>, <code>Metrics</code> is returned.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'includeSharedResources': true, // Boolean | Set to <code>true</code> to have shared resources included in the report.
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56 // Number | The maximum number of results to return for this request.
};
apiInstance.getConsolidatedReport(format, opts, (error, data, response) => {
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
 **format** | **String**| &lt;p&gt;The format of the consolidated report.&lt;/p&gt; &lt;p&gt;For &lt;code&gt;PDF&lt;/code&gt;, &lt;code&gt;Base64String&lt;/code&gt; is returned. For &lt;code&gt;JSON&lt;/code&gt;, &lt;code&gt;Metrics&lt;/code&gt; is returned.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **includeSharedResources** | **Boolean**| Set to &lt;code&gt;true&lt;/code&gt; to have shared resources included in the report. | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 

### Return type

[**GetConsolidatedReportOutput**](GetConsolidatedReportOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLens

> GetLensOutput getLens(lensAlias, opts)



Get an existing lens.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'lensVersion': "lensVersion_example" // String | The lens version to be retrieved.
};
apiInstance.getLens(lensAlias, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **lensVersion** | **String**| The lens version to be retrieved. | [optional] 

### Return type

[**GetLensOutput**](GetLensOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLensReview

> GetLensReviewOutput getLensReview(workloadId, lensAlias, opts)



Get lens review.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'milestoneNumber': 56 // Number | 
};
apiInstance.getLensReview(workloadId, lensAlias, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **milestoneNumber** | **Number**|  | [optional] 

### Return type

[**GetLensReviewOutput**](GetLensReviewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLensReviewReport

> GetLensReviewReportOutput getLensReviewReport(workloadId, lensAlias, opts)



Get lens review report.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'milestoneNumber': 56 // Number | 
};
apiInstance.getLensReviewReport(workloadId, lensAlias, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **milestoneNumber** | **Number**|  | [optional] 

### Return type

[**GetLensReviewReportOutput**](GetLensReviewReportOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLensVersionDifference

> GetLensVersionDifferenceOutput getLensVersionDifference(lensAlias, opts)



Get lens version differences.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'baseLensVersion': "baseLensVersion_example", // String | The base version of the lens.
  'targetLensVersion': "targetLensVersion_example" // String | The lens version to target a difference for.
};
apiInstance.getLensVersionDifference(lensAlias, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **baseLensVersion** | **String**| The base version of the lens. | [optional] 
 **targetLensVersion** | **String**| The lens version to target a difference for. | [optional] 

### Return type

[**GetLensVersionDifferenceOutput**](GetLensVersionDifferenceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMilestone

> GetMilestoneOutput getMilestone(workloadId, milestoneNumber, opts)



Get a milestone for an existing workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let milestoneNumber = 56; // Number | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMilestone(workloadId, milestoneNumber, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **milestoneNumber** | **Number**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMilestoneOutput**](GetMilestoneOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfile

> GetProfileOutput getProfile(profileArn, opts)



Get profile information.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let profileArn = "profileArn_example"; // String | The profile ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'profileVersion': "profileVersion_example" // String | The profile version.
};
apiInstance.getProfile(profileArn, opts, (error, data, response) => {
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
 **profileArn** | **String**| The profile ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **profileVersion** | **String**| The profile version. | [optional] 

### Return type

[**GetProfileOutput**](GetProfileOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileTemplate

> GetProfileTemplateOutput getProfileTemplate(opts)



Get profile template.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getProfileTemplate(opts, (error, data, response) => {
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

### Return type

[**GetProfileTemplateOutput**](GetProfileTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkload

> GetWorkloadOutput getWorkload(workloadId, opts)



Get an existing workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWorkload(workloadId, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWorkloadOutput**](GetWorkloadOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importLens

> ImportLensOutput importLens(importLensRequest, opts)



&lt;p&gt;Import a new custom lens or update an existing custom lens.&lt;/p&gt; &lt;p&gt;To update an existing custom lens, specify its ARN as the &lt;code&gt;LensAlias&lt;/code&gt;. If no ARN is specified, a new custom lens is created.&lt;/p&gt; &lt;p&gt;The new or updated lens will have a status of &lt;code&gt;DRAFT&lt;/code&gt;. The lens cannot be applied to workloads or shared with other Amazon Web Services accounts until it&#39;s published with &lt;a&gt;CreateLensVersion&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lenses are defined in JSON. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\&quot;&gt;JSON format specification&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A custom lens cannot exceed 500 KB in size.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let importLensRequest = new AwsWellArchitectedTool.ImportLensRequest(); // ImportLensRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.importLens(importLensRequest, opts, (error, data, response) => {
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
 **importLensRequest** | [**ImportLensRequest**](ImportLensRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ImportLensOutput**](ImportLensOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAnswers

> ListAnswersOutput listAnswers(workloadId, lensAlias, opts)



List of answers for a particular workload and lens.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pillarId': "pillarId_example", // String | 
  'milestoneNumber': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return for this request.
  'questionPriority': "questionPriority_example" // String | The priority of the question.
};
apiInstance.listAnswers(workloadId, lensAlias, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pillarId** | **String**|  | [optional] 
 **milestoneNumber** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 
 **questionPriority** | **String**| The priority of the question. | [optional] 

### Return type

[**ListAnswersOutput**](ListAnswersOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCheckDetails

> ListCheckDetailsOutput listCheckDetails(workloadId, listCheckDetailsRequest, opts)



List of Trusted Advisor check details by account related to the workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let listCheckDetailsRequest = new AwsWellArchitectedTool.ListCheckDetailsRequest(); // ListCheckDetailsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listCheckDetails(workloadId, listCheckDetailsRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **listCheckDetailsRequest** | [**ListCheckDetailsRequest**](ListCheckDetailsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListCheckDetailsOutput**](ListCheckDetailsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCheckSummaries

> ListCheckSummariesOutput listCheckSummaries(workloadId, listCheckDetailsRequest, opts)



List of Trusted Advisor checks summarized for all accounts related to the workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let listCheckDetailsRequest = new AwsWellArchitectedTool.ListCheckDetailsRequest(); // ListCheckDetailsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listCheckSummaries(workloadId, listCheckDetailsRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **listCheckDetailsRequest** | [**ListCheckDetailsRequest**](ListCheckDetailsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListCheckSummariesOutput**](ListCheckSummariesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLensReviewImprovements

> ListLensReviewImprovementsOutput listLensReviewImprovements(workloadId, lensAlias, opts)



List lens review improvements.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pillarId': "pillarId_example", // String | 
  'milestoneNumber': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return for this request.
  'questionPriority': "questionPriority_example" // String | The priority of the question.
};
apiInstance.listLensReviewImprovements(workloadId, lensAlias, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pillarId** | **String**|  | [optional] 
 **milestoneNumber** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 
 **questionPriority** | **String**| The priority of the question. | [optional] 

### Return type

[**ListLensReviewImprovementsOutput**](ListLensReviewImprovementsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLensReviews

> ListLensReviewsOutput listLensReviews(workloadId, opts)



List lens reviews for a particular workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'milestoneNumber': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56 // Number | 
};
apiInstance.listLensReviews(workloadId, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **milestoneNumber** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 

### Return type

[**ListLensReviewsOutput**](ListLensReviewsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLensShares

> ListLensSharesOutput listLensShares(lensAlias, opts)



List the lens shares associated with the lens.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let lensAlias = "lensAlias_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sharedWithPrefix': "sharedWithPrefix_example", // String | The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the lens is shared.
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return for this request.
  'status': "status_example" // String | 
};
apiInstance.listLensShares(lensAlias, opts, (error, data, response) => {
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
 **lensAlias** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sharedWithPrefix** | **String**| The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the lens is shared. | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 
 **status** | **String**|  | [optional] 

### Return type

[**ListLensSharesOutput**](ListLensSharesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLenses

> ListLensesOutput listLenses(opts)



List the available lenses.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | 
  'lensType': "lensType_example", // String | The type of lenses to be returned.
  'lensStatus': "lensStatus_example", // String | The status of lenses to be returned.
  'lensName': "lensName_example" // String | 
};
apiInstance.listLenses(opts, (error, data, response) => {
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
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **lensType** | **String**| The type of lenses to be returned. | [optional] 
 **lensStatus** | **String**| The status of lenses to be returned. | [optional] 
 **lensName** | **String**|  | [optional] 

### Return type

[**ListLensesOutput**](ListLensesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMilestones

> ListMilestonesOutput listMilestones(workloadId, listMilestonesRequest, opts)



List all milestones for an existing workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let listMilestonesRequest = new AwsWellArchitectedTool.ListMilestonesRequest(); // ListMilestonesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listMilestones(workloadId, listMilestonesRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **listMilestonesRequest** | [**ListMilestonesRequest**](ListMilestonesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListMilestonesOutput**](ListMilestonesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listNotifications

> ListNotificationsOutput listNotifications(listNotificationsRequest, opts)



List lens notifications.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let listNotificationsRequest = new AwsWellArchitectedTool.ListNotificationsRequest(); // ListNotificationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listNotifications(listNotificationsRequest, opts, (error, data, response) => {
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
 **listNotificationsRequest** | [**ListNotificationsRequest**](ListNotificationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListNotificationsOutput**](ListNotificationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listProfileNotifications

> ListProfileNotificationsOutput listProfileNotifications(opts)



List profile notifications.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'workloadId': "workloadId_example", // String | 
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56 // Number | 
};
apiInstance.listProfileNotifications(opts, (error, data, response) => {
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
 **workloadId** | **String**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 

### Return type

[**ListProfileNotificationsOutput**](ListProfileNotificationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProfileShares

> ListProfileSharesOutput listProfileShares(profileArn, opts)



List profile shares.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let profileArn = "profileArn_example"; // String | The profile ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sharedWithPrefix': "sharedWithPrefix_example", // String | The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the profile is shared.
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return for this request.
  'status': "status_example" // String | 
};
apiInstance.listProfileShares(profileArn, opts, (error, data, response) => {
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
 **profileArn** | **String**| The profile ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sharedWithPrefix** | **String**| The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the profile is shared. | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 
 **status** | **String**|  | [optional] 

### Return type

[**ListProfileSharesOutput**](ListProfileSharesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProfiles

> ListProfilesOutput listProfiles(opts)



List profiles.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'profileNamePrefix': "profileNamePrefix_example", // String | Prefix for profile name.
  'profileOwnerType': "profileOwnerType_example", // String | Profile owner type.
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56 // Number | 
};
apiInstance.listProfiles(opts, (error, data, response) => {
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
 **profileNamePrefix** | **String**| Prefix for profile name. | [optional] 
 **profileOwnerType** | **String**| Profile owner type. | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 

### Return type

[**ListProfilesOutput**](ListProfilesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listShareInvitations

> ListShareInvitationsOutput listShareInvitations(opts)



List the workload invitations.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'workloadNamePrefix': "workloadNamePrefix_example", // String | 
  'lensNamePrefix': "lensNamePrefix_example", // String | An optional string added to the beginning of each lens name returned in the results.
  'shareResourceType': "shareResourceType_example", // String | The type of share invitations to be returned.
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return for this request.
  'profileNamePrefix': "profileNamePrefix_example" // String | Profile name prefix.
};
apiInstance.listShareInvitations(opts, (error, data, response) => {
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
 **workloadNamePrefix** | **String**|  | [optional] 
 **lensNamePrefix** | **String**| An optional string added to the beginning of each lens name returned in the results. | [optional] 
 **shareResourceType** | **String**| The type of share invitations to be returned. | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 
 **profileNamePrefix** | **String**| Profile name prefix. | [optional] 

### Return type

[**ListShareInvitationsOutput**](ListShareInvitationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(workloadArn, opts)



&lt;p&gt;List the tags for a resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The WorkloadArn parameter can be a workload ARN, a custom lens ARN, or a profile ARN.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadArn = "workloadArn_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(workloadArn, opts, (error, data, response) => {
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
 **workloadArn** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkloadShares

> ListWorkloadSharesOutput listWorkloadShares(workloadId, opts)



List the workload shares associated with the workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sharedWithPrefix': "sharedWithPrefix_example", // String | The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the workload is shared.
  'nextToken': "nextToken_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return for this request.
  'status': "status_example" // String | 
};
apiInstance.listWorkloadShares(workloadId, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sharedWithPrefix** | **String**| The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the workload is shared. | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return for this request. | [optional] 
 **status** | **String**|  | [optional] 

### Return type

[**ListWorkloadSharesOutput**](ListWorkloadSharesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkloads

> ListWorkloadsOutput listWorkloads(listWorkloadsRequest, opts)



Paginated list of workloads.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let listWorkloadsRequest = new AwsWellArchitectedTool.ListWorkloadsRequest(); // ListWorkloadsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listWorkloads(listWorkloadsRequest, opts, (error, data, response) => {
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
 **listWorkloadsRequest** | [**ListWorkloadsRequest**](ListWorkloadsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListWorkloadsOutput**](ListWorkloadsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(workloadArn, tagResourceRequest, opts)



&lt;p&gt;Adds one or more tags to the specified resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The WorkloadArn parameter can be a workload ARN, a custom lens ARN, or a profile ARN.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadArn = "workloadArn_example"; // String | 
let tagResourceRequest = new AwsWellArchitectedTool.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(workloadArn, tagResourceRequest, opts, (error, data, response) => {
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
 **workloadArn** | **String**|  | 
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

> Object untagResource(workloadArn, tagKeys, opts)



&lt;p&gt;Deletes specified tags from a resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The WorkloadArn parameter can be a workload ARN, a custom lens ARN, or a profile ARN.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To specify multiple tags, use separate &lt;b&gt;tagKeys&lt;/b&gt; parameters, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;DELETE /tags/WorkloadArn?tagKeys&#x3D;key1&amp;amp;tagKeys&#x3D;key2&lt;/code&gt; &lt;/p&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadArn = "workloadArn_example"; // String | 
let tagKeys = ["null"]; // [String] | A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(workloadArn, tagKeys, opts, (error, data, response) => {
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
 **workloadArn** | **String**|  | 
 **tagKeys** | [**[String]**](String.md)| A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource. | 
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


## updateAnswer

> UpdateAnswerOutput updateAnswer(workloadId, lensAlias, questionId, updateAnswerRequest, opts)



Update the answer to a specific question in a workload review.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let questionId = "questionId_example"; // String | 
let updateAnswerRequest = new AwsWellArchitectedTool.UpdateAnswerRequest(); // UpdateAnswerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAnswer(workloadId, lensAlias, questionId, updateAnswerRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **questionId** | **String**|  | 
 **updateAnswerRequest** | [**UpdateAnswerRequest**](UpdateAnswerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAnswerOutput**](UpdateAnswerOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGlobalSettings

> updateGlobalSettings(updateGlobalSettingsRequest, opts)



Updates whether the Amazon Web Services account is opted into organization sharing and discovery integration features.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let updateGlobalSettingsRequest = new AwsWellArchitectedTool.UpdateGlobalSettingsRequest(); // UpdateGlobalSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGlobalSettings(updateGlobalSettingsRequest, opts, (error, data, response) => {
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
 **updateGlobalSettingsRequest** | [**UpdateGlobalSettingsRequest**](UpdateGlobalSettingsRequest.md)|  | 
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


## updateLensReview

> UpdateLensReviewOutput updateLensReview(workloadId, lensAlias, updateLensReviewRequest, opts)



Update lens review for a particular workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let updateLensReviewRequest = new AwsWellArchitectedTool.UpdateLensReviewRequest(); // UpdateLensReviewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLensReview(workloadId, lensAlias, updateLensReviewRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **updateLensReviewRequest** | [**UpdateLensReviewRequest**](UpdateLensReviewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateLensReviewOutput**](UpdateLensReviewOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProfile

> UpdateProfileOutput updateProfile(profileArn, updateProfileRequest, opts)



Update a profile.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let profileArn = "profileArn_example"; // String | The profile ARN.
let updateProfileRequest = new AwsWellArchitectedTool.UpdateProfileRequest(); // UpdateProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProfile(profileArn, updateProfileRequest, opts, (error, data, response) => {
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
 **profileArn** | **String**| The profile ARN. | 
 **updateProfileRequest** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProfileOutput**](UpdateProfileOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateShareInvitation

> UpdateShareInvitationOutput updateShareInvitation(shareInvitationId, updateShareInvitationRequest, opts)



&lt;p&gt;Update a workload or custom lens share invitation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation can be called independently of any resource. Previous documentation implied that a workload ARN must be specified.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let shareInvitationId = "shareInvitationId_example"; // String | The ID assigned to the share invitation.
let updateShareInvitationRequest = new AwsWellArchitectedTool.UpdateShareInvitationRequest(); // UpdateShareInvitationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateShareInvitation(shareInvitationId, updateShareInvitationRequest, opts, (error, data, response) => {
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
 **shareInvitationId** | **String**| The ID assigned to the share invitation. | 
 **updateShareInvitationRequest** | [**UpdateShareInvitationRequest**](UpdateShareInvitationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateShareInvitationOutput**](UpdateShareInvitationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkload

> UpdateWorkloadOutput updateWorkload(workloadId, updateWorkloadRequest, opts)



Update an existing workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let updateWorkloadRequest = new AwsWellArchitectedTool.UpdateWorkloadRequest(); // UpdateWorkloadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkload(workloadId, updateWorkloadRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **updateWorkloadRequest** | [**UpdateWorkloadRequest**](UpdateWorkloadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateWorkloadOutput**](UpdateWorkloadOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkloadShare

> UpdateWorkloadShareOutput updateWorkloadShare(shareId, workloadId, updateWorkloadShareRequest, opts)



Update a workload share.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let shareId = "shareId_example"; // String | 
let workloadId = "workloadId_example"; // String | 
let updateWorkloadShareRequest = new AwsWellArchitectedTool.UpdateWorkloadShareRequest(); // UpdateWorkloadShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkloadShare(shareId, workloadId, updateWorkloadShareRequest, opts, (error, data, response) => {
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
 **shareId** | **String**|  | 
 **workloadId** | **String**|  | 
 **updateWorkloadShareRequest** | [**UpdateWorkloadShareRequest**](UpdateWorkloadShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateWorkloadShareOutput**](UpdateWorkloadShareOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upgradeLensReview

> upgradeLensReview(workloadId, lensAlias, upgradeLensReviewRequest, opts)



Upgrade lens review for a particular workload.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let lensAlias = "lensAlias_example"; // String | 
let upgradeLensReviewRequest = new AwsWellArchitectedTool.UpgradeLensReviewRequest(); // UpgradeLensReviewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.upgradeLensReview(workloadId, lensAlias, upgradeLensReviewRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **lensAlias** | **String**|  | 
 **upgradeLensReviewRequest** | [**UpgradeLensReviewRequest**](UpgradeLensReviewRequest.md)|  | 
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


## upgradeProfileVersion

> upgradeProfileVersion(workloadId, profileArn, upgradeProfileVersionRequest, opts)



Upgrade a profile.

### Example

```javascript
import AwsWellArchitectedTool from 'aws_well_architected_tool';
let defaultClient = AwsWellArchitectedTool.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsWellArchitectedTool.DefaultApi();
let workloadId = "workloadId_example"; // String | 
let profileArn = "profileArn_example"; // String | The profile ARN.
let upgradeProfileVersionRequest = new AwsWellArchitectedTool.UpgradeProfileVersionRequest(); // UpgradeProfileVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.upgradeProfileVersion(workloadId, profileArn, upgradeProfileVersionRequest, opts, (error, data, response) => {
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
 **workloadId** | **String**|  | 
 **profileArn** | **String**| The profile ARN. | 
 **upgradeProfileVersionRequest** | [**UpgradeProfileVersionRequest**](UpgradeProfileVersionRequest.md)|  | 
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

