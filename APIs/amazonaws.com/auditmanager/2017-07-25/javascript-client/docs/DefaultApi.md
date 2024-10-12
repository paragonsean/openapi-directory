# AwsAuditManager.DefaultApi

All URIs are relative to *http://auditmanager.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateAssessmentReportEvidenceFolder**](DefaultApi.md#associateAssessmentReportEvidenceFolder) | **PUT** /assessments/{assessmentId}/associateToAssessmentReport | 
[**batchAssociateAssessmentReportEvidence**](DefaultApi.md#batchAssociateAssessmentReportEvidence) | **PUT** /assessments/{assessmentId}/batchAssociateToAssessmentReport | 
[**batchCreateDelegationByAssessment**](DefaultApi.md#batchCreateDelegationByAssessment) | **POST** /assessments/{assessmentId}/delegations | 
[**batchDeleteDelegationByAssessment**](DefaultApi.md#batchDeleteDelegationByAssessment) | **PUT** /assessments/{assessmentId}/delegations | 
[**batchDisassociateAssessmentReportEvidence**](DefaultApi.md#batchDisassociateAssessmentReportEvidence) | **PUT** /assessments/{assessmentId}/batchDisassociateFromAssessmentReport | 
[**batchImportEvidenceToAssessmentControl**](DefaultApi.md#batchImportEvidenceToAssessmentControl) | **POST** /assessments/{assessmentId}/controlSets/{controlSetId}/controls/{controlId}/evidence | 
[**createAssessment**](DefaultApi.md#createAssessment) | **POST** /assessments | 
[**createAssessmentFramework**](DefaultApi.md#createAssessmentFramework) | **POST** /assessmentFrameworks | 
[**createAssessmentReport**](DefaultApi.md#createAssessmentReport) | **POST** /assessments/{assessmentId}/reports | 
[**createControl**](DefaultApi.md#createControl) | **POST** /controls | 
[**deleteAssessment**](DefaultApi.md#deleteAssessment) | **DELETE** /assessments/{assessmentId} | 
[**deleteAssessmentFramework**](DefaultApi.md#deleteAssessmentFramework) | **DELETE** /assessmentFrameworks/{frameworkId} | 
[**deleteAssessmentFrameworkShare**](DefaultApi.md#deleteAssessmentFrameworkShare) | **DELETE** /assessmentFrameworkShareRequests/{requestId}#requestType | 
[**deleteAssessmentReport**](DefaultApi.md#deleteAssessmentReport) | **DELETE** /assessments/{assessmentId}/reports/{assessmentReportId} | 
[**deleteControl**](DefaultApi.md#deleteControl) | **DELETE** /controls/{controlId} | 
[**deregisterAccount**](DefaultApi.md#deregisterAccount) | **POST** /account/deregisterAccount | 
[**deregisterOrganizationAdminAccount**](DefaultApi.md#deregisterOrganizationAdminAccount) | **POST** /account/deregisterOrganizationAdminAccount | 
[**disassociateAssessmentReportEvidenceFolder**](DefaultApi.md#disassociateAssessmentReportEvidenceFolder) | **PUT** /assessments/{assessmentId}/disassociateFromAssessmentReport | 
[**getAccountStatus**](DefaultApi.md#getAccountStatus) | **GET** /account/status | 
[**getAssessment**](DefaultApi.md#getAssessment) | **GET** /assessments/{assessmentId} | 
[**getAssessmentFramework**](DefaultApi.md#getAssessmentFramework) | **GET** /assessmentFrameworks/{frameworkId} | 
[**getAssessmentReportUrl**](DefaultApi.md#getAssessmentReportUrl) | **GET** /assessments/{assessmentId}/reports/{assessmentReportId}/url | 
[**getChangeLogs**](DefaultApi.md#getChangeLogs) | **GET** /assessments/{assessmentId}/changelogs | 
[**getControl**](DefaultApi.md#getControl) | **GET** /controls/{controlId} | 
[**getDelegations**](DefaultApi.md#getDelegations) | **GET** /delegations | 
[**getEvidence**](DefaultApi.md#getEvidence) | **GET** /assessments/{assessmentId}/controlSets/{controlSetId}/evidenceFolders/{evidenceFolderId}/evidence/{evidenceId} | 
[**getEvidenceByEvidenceFolder**](DefaultApi.md#getEvidenceByEvidenceFolder) | **GET** /assessments/{assessmentId}/controlSets/{controlSetId}/evidenceFolders/{evidenceFolderId}/evidence | 
[**getEvidenceFileUploadUrl**](DefaultApi.md#getEvidenceFileUploadUrl) | **GET** /evidenceFileUploadUrl#fileName | 
[**getEvidenceFolder**](DefaultApi.md#getEvidenceFolder) | **GET** /assessments/{assessmentId}/controlSets/{controlSetId}/evidenceFolders/{evidenceFolderId} | 
[**getEvidenceFoldersByAssessment**](DefaultApi.md#getEvidenceFoldersByAssessment) | **GET** /assessments/{assessmentId}/evidenceFolders | 
[**getEvidenceFoldersByAssessmentControl**](DefaultApi.md#getEvidenceFoldersByAssessmentControl) | **GET** /assessments/{assessmentId}/evidenceFolders-by-assessment-control/{controlSetId}/{controlId} | 
[**getInsights**](DefaultApi.md#getInsights) | **GET** /insights | 
[**getInsightsByAssessment**](DefaultApi.md#getInsightsByAssessment) | **GET** /insights/assessments/{assessmentId} | 
[**getOrganizationAdminAccount**](DefaultApi.md#getOrganizationAdminAccount) | **GET** /account/organizationAdminAccount | 
[**getServicesInScope**](DefaultApi.md#getServicesInScope) | **GET** /services | 
[**getSettings**](DefaultApi.md#getSettings) | **GET** /settings/{attribute} | 
[**listAssessmentControlInsightsByControlDomain**](DefaultApi.md#listAssessmentControlInsightsByControlDomain) | **GET** /insights/controls-by-assessment#controlDomainId&amp;assessmentId | 
[**listAssessmentFrameworkShareRequests**](DefaultApi.md#listAssessmentFrameworkShareRequests) | **GET** /assessmentFrameworkShareRequests#requestType | 
[**listAssessmentFrameworks**](DefaultApi.md#listAssessmentFrameworks) | **GET** /assessmentFrameworks#frameworkType | 
[**listAssessmentReports**](DefaultApi.md#listAssessmentReports) | **GET** /assessmentReports | 
[**listAssessments**](DefaultApi.md#listAssessments) | **GET** /assessments | 
[**listControlDomainInsights**](DefaultApi.md#listControlDomainInsights) | **GET** /insights/control-domains | 
[**listControlDomainInsightsByAssessment**](DefaultApi.md#listControlDomainInsightsByAssessment) | **GET** /insights/control-domains-by-assessment#assessmentId | 
[**listControlInsightsByControlDomain**](DefaultApi.md#listControlInsightsByControlDomain) | **GET** /insights/controls#controlDomainId | 
[**listControls**](DefaultApi.md#listControls) | **GET** /controls#controlType | 
[**listKeywordsForDataSource**](DefaultApi.md#listKeywordsForDataSource) | **GET** /dataSourceKeywords#source | 
[**listNotifications**](DefaultApi.md#listNotifications) | **GET** /notifications | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**registerAccount**](DefaultApi.md#registerAccount) | **POST** /account/registerAccount | 
[**registerOrganizationAdminAccount**](DefaultApi.md#registerOrganizationAdminAccount) | **POST** /account/registerOrganizationAdminAccount | 
[**startAssessmentFrameworkShare**](DefaultApi.md#startAssessmentFrameworkShare) | **POST** /assessmentFrameworks/{frameworkId}/shareRequests | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateAssessment**](DefaultApi.md#updateAssessment) | **PUT** /assessments/{assessmentId} | 
[**updateAssessmentControl**](DefaultApi.md#updateAssessmentControl) | **PUT** /assessments/{assessmentId}/controlSets/{controlSetId}/controls/{controlId} | 
[**updateAssessmentControlSetStatus**](DefaultApi.md#updateAssessmentControlSetStatus) | **PUT** /assessments/{assessmentId}/controlSets/{controlSetId}/status | 
[**updateAssessmentFramework**](DefaultApi.md#updateAssessmentFramework) | **PUT** /assessmentFrameworks/{frameworkId} | 
[**updateAssessmentFrameworkShare**](DefaultApi.md#updateAssessmentFrameworkShare) | **PUT** /assessmentFrameworkShareRequests/{requestId} | 
[**updateAssessmentStatus**](DefaultApi.md#updateAssessmentStatus) | **PUT** /assessments/{assessmentId}/status | 
[**updateControl**](DefaultApi.md#updateControl) | **PUT** /controls/{controlId} | 
[**updateSettings**](DefaultApi.md#updateSettings) | **PUT** /settings | 
[**validateAssessmentReportIntegrity**](DefaultApi.md#validateAssessmentReportIntegrity) | **POST** /assessmentReports/integrity | 



## associateAssessmentReportEvidenceFolder

> Object associateAssessmentReportEvidenceFolder(assessmentId, associateAssessmentReportEvidenceFolderRequest, opts)



 Associates an evidence folder to an assessment report in an Audit Manager assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let associateAssessmentReportEvidenceFolderRequest = new AwsAuditManager.AssociateAssessmentReportEvidenceFolderRequest(); // AssociateAssessmentReportEvidenceFolderRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateAssessmentReportEvidenceFolder(assessmentId, associateAssessmentReportEvidenceFolderRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **associateAssessmentReportEvidenceFolderRequest** | [**AssociateAssessmentReportEvidenceFolderRequest**](AssociateAssessmentReportEvidenceFolderRequest.md)|  | 
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


## batchAssociateAssessmentReportEvidence

> BatchAssociateAssessmentReportEvidenceResponse batchAssociateAssessmentReportEvidence(assessmentId, batchAssociateAssessmentReportEvidenceRequest, opts)



 Associates a list of evidence to an assessment report in an Audit Manager assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let batchAssociateAssessmentReportEvidenceRequest = new AwsAuditManager.BatchAssociateAssessmentReportEvidenceRequest(); // BatchAssociateAssessmentReportEvidenceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchAssociateAssessmentReportEvidence(assessmentId, batchAssociateAssessmentReportEvidenceRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **batchAssociateAssessmentReportEvidenceRequest** | [**BatchAssociateAssessmentReportEvidenceRequest**](BatchAssociateAssessmentReportEvidenceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchAssociateAssessmentReportEvidenceResponse**](BatchAssociateAssessmentReportEvidenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchCreateDelegationByAssessment

> BatchCreateDelegationByAssessmentResponse batchCreateDelegationByAssessment(assessmentId, batchCreateDelegationByAssessmentRequest, opts)



 Creates a batch of delegations for an assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let batchCreateDelegationByAssessmentRequest = new AwsAuditManager.BatchCreateDelegationByAssessmentRequest(); // BatchCreateDelegationByAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCreateDelegationByAssessment(assessmentId, batchCreateDelegationByAssessmentRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **batchCreateDelegationByAssessmentRequest** | [**BatchCreateDelegationByAssessmentRequest**](BatchCreateDelegationByAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCreateDelegationByAssessmentResponse**](BatchCreateDelegationByAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteDelegationByAssessment

> BatchDeleteDelegationByAssessmentResponse batchDeleteDelegationByAssessment(assessmentId, batchDeleteDelegationByAssessmentRequest, opts)



 Deletes a batch of delegations for an assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let batchDeleteDelegationByAssessmentRequest = new AwsAuditManager.BatchDeleteDelegationByAssessmentRequest(); // BatchDeleteDelegationByAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteDelegationByAssessment(assessmentId, batchDeleteDelegationByAssessmentRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **batchDeleteDelegationByAssessmentRequest** | [**BatchDeleteDelegationByAssessmentRequest**](BatchDeleteDelegationByAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteDelegationByAssessmentResponse**](BatchDeleteDelegationByAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDisassociateAssessmentReportEvidence

> BatchDisassociateAssessmentReportEvidenceResponse batchDisassociateAssessmentReportEvidence(assessmentId, batchAssociateAssessmentReportEvidenceRequest, opts)



 Disassociates a list of evidence from an assessment report in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let batchAssociateAssessmentReportEvidenceRequest = new AwsAuditManager.BatchAssociateAssessmentReportEvidenceRequest(); // BatchAssociateAssessmentReportEvidenceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDisassociateAssessmentReportEvidence(assessmentId, batchAssociateAssessmentReportEvidenceRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **batchAssociateAssessmentReportEvidenceRequest** | [**BatchAssociateAssessmentReportEvidenceRequest**](BatchAssociateAssessmentReportEvidenceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDisassociateAssessmentReportEvidenceResponse**](BatchDisassociateAssessmentReportEvidenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchImportEvidenceToAssessmentControl

> BatchImportEvidenceToAssessmentControlResponse batchImportEvidenceToAssessmentControl(assessmentId, controlSetId, controlId, batchImportEvidenceToAssessmentControlRequest, opts)



&lt;p&gt;Adds one or more pieces of evidence to a control in an Audit Manager assessment. &lt;/p&gt; &lt;p&gt;You can import manual evidence from any S3 bucket by specifying the S3 URI of the object. You can also upload a file from your browser, or enter plain text in response to a risk assessment question. &lt;/p&gt; &lt;p&gt;The following restrictions apply to this action:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;manualEvidence&lt;/code&gt; can be only one of the following: &lt;code&gt;evidenceFileName&lt;/code&gt;, &lt;code&gt;s3ResourcePath&lt;/code&gt;, or &lt;code&gt;textResponse&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum size of an individual evidence file: 100 MB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Number of daily manual evidence uploads per control: 100&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Supported file formats: See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\&quot;&gt;Supported file types for manual evidence&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about Audit Manager service restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html\&quot;&gt;Quotas and restrictions for Audit Manager&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The identifier for the control set. 
let controlId = "controlId_example"; // String |  The identifier for the control. 
let batchImportEvidenceToAssessmentControlRequest = new AwsAuditManager.BatchImportEvidenceToAssessmentControlRequest(); // BatchImportEvidenceToAssessmentControlRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchImportEvidenceToAssessmentControl(assessmentId, controlSetId, controlId, batchImportEvidenceToAssessmentControlRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **controlSetId** | **String**|  The identifier for the control set.  | 
 **controlId** | **String**|  The identifier for the control.  | 
 **batchImportEvidenceToAssessmentControlRequest** | [**BatchImportEvidenceToAssessmentControlRequest**](BatchImportEvidenceToAssessmentControlRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchImportEvidenceToAssessmentControlResponse**](BatchImportEvidenceToAssessmentControlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssessment

> CreateAssessmentResponse createAssessment(createAssessmentRequest, opts)



 Creates an assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let createAssessmentRequest = new AwsAuditManager.CreateAssessmentRequest(); // CreateAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssessment(createAssessmentRequest, opts, (error, data, response) => {
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
 **createAssessmentRequest** | [**CreateAssessmentRequest**](CreateAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssessmentResponse**](CreateAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssessmentFramework

> CreateAssessmentFrameworkResponse createAssessmentFramework(createAssessmentFrameworkRequest, opts)



 Creates a custom framework in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let createAssessmentFrameworkRequest = new AwsAuditManager.CreateAssessmentFrameworkRequest(); // CreateAssessmentFrameworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssessmentFramework(createAssessmentFrameworkRequest, opts, (error, data, response) => {
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
 **createAssessmentFrameworkRequest** | [**CreateAssessmentFrameworkRequest**](CreateAssessmentFrameworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssessmentFrameworkResponse**](CreateAssessmentFrameworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssessmentReport

> CreateAssessmentReportResponse createAssessmentReport(assessmentId, createAssessmentReportRequest, opts)



 Creates an assessment report for the specified assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let createAssessmentReportRequest = new AwsAuditManager.CreateAssessmentReportRequest(); // CreateAssessmentReportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssessmentReport(assessmentId, createAssessmentReportRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **createAssessmentReportRequest** | [**CreateAssessmentReportRequest**](CreateAssessmentReportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssessmentReportResponse**](CreateAssessmentReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createControl

> CreateControlResponse createControl(createControlRequest, opts)



 Creates a new custom control in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let createControlRequest = new AwsAuditManager.CreateControlRequest(); // CreateControlRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createControl(createControlRequest, opts, (error, data, response) => {
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
 **createControlRequest** | [**CreateControlRequest**](CreateControlRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateControlResponse**](CreateControlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAssessment

> Object deleteAssessment(assessmentId, opts)



 Deletes an assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessment(assessmentId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
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


## deleteAssessmentFramework

> Object deleteAssessmentFramework(frameworkId, opts)



 Deletes a custom framework in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let frameworkId = "frameworkId_example"; // String |  The identifier for the custom framework. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessmentFramework(frameworkId, opts, (error, data, response) => {
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
 **frameworkId** | **String**|  The identifier for the custom framework.  | 
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


## deleteAssessmentFrameworkShare

> Object deleteAssessmentFrameworkShare(requestId, requestType, opts)



 Deletes a share request for a custom framework in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let requestId = "requestId_example"; // String | The unique identifier for the share request to be deleted.
let requestType = "requestType_example"; // String | Specifies whether the share request is a sent request or a received request.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessmentFrameworkShare(requestId, requestType, opts, (error, data, response) => {
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
 **requestId** | **String**| The unique identifier for the share request to be deleted. | 
 **requestType** | **String**| Specifies whether the share request is a sent request or a received request. | 
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


## deleteAssessmentReport

> Object deleteAssessmentReport(assessmentId, assessmentReportId, opts)



&lt;p&gt;Deletes an assessment report in Audit Manager. &lt;/p&gt; &lt;p&gt;When you run the &lt;code&gt;DeleteAssessmentReport&lt;/code&gt; operation, Audit Manager attempts to delete the following data:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;The specified assessment report that’s stored in your S3 bucket&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The associated metadata that’s stored in Audit Manager&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;If Audit Manager can’t access the assessment report in your S3 bucket, the report isn’t deleted. In this event, the &lt;code&gt;DeleteAssessmentReport&lt;/code&gt; operation doesn’t fail. Instead, it proceeds to delete the associated metadata only. You must then delete the assessment report from the S3 bucket yourself. &lt;/p&gt; &lt;p&gt;This scenario happens when Audit Manager receives a &lt;code&gt;403 (Forbidden)&lt;/code&gt; or &lt;code&gt;404 (Not Found)&lt;/code&gt; error from Amazon S3. To avoid this, make sure that your S3 bucket is available, and that you configured the correct permissions for Audit Manager to delete resources in your S3 bucket. For an example permissions policy that you can use, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#full-administrator-access-assessment-report-destination\&quot;&gt;Assessment report destination permissions&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;. For information about the issues that could cause a &lt;code&gt;403 (Forbidden)&lt;/code&gt; or &lt;code&gt;404 (Not Found&lt;/code&gt;) error from Amazon S3, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList\&quot;&gt;List of Error Codes&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service API Reference&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let assessmentReportId = "assessmentReportId_example"; // String |  The unique identifier for the assessment report. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssessmentReport(assessmentId, assessmentReportId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **assessmentReportId** | **String**|  The unique identifier for the assessment report.  | 
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


## deleteControl

> Object deleteControl(controlId, opts)



&lt;p&gt; Deletes a custom control in Audit Manager. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you invoke this operation, the custom control is deleted from any frameworks or assessments that it’s currently part of. As a result, Audit Manager will stop collecting evidence for that custom control in all of your assessments. This includes assessments that you previously created before you deleted the custom control.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let controlId = "controlId_example"; // String |  The unique identifier for the control. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteControl(controlId, opts, (error, data, response) => {
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
 **controlId** | **String**|  The unique identifier for the control.  | 
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


## deregisterAccount

> DeregisterAccountResponse deregisterAccount(opts)



&lt;p&gt; Deregisters an account in Audit Manager. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you deregister, you can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html\&quot;&gt;UpdateSettings&lt;/a&gt; API operation to set your preferred data retention policy. By default, Audit Manager retains your data. If you want to delete your data, you can use the &lt;code&gt;DeregistrationPolicy&lt;/code&gt; attribute to request the deletion of your data. &lt;/p&gt; &lt;p&gt;For more information about data retention, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/data-protection.html\&quot;&gt;Data Protection&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterAccount(opts, (error, data, response) => {
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

[**DeregisterAccountResponse**](DeregisterAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deregisterOrganizationAdminAccount

> Object deregisterOrganizationAdminAccount(deregisterOrganizationAdminAccountRequest, opts)



&lt;p&gt;Removes the specified Amazon Web Services account as a delegated administrator for Audit Manager. &lt;/p&gt; &lt;p&gt;When you remove a delegated administrator from your Audit Manager settings, you continue to have access to the evidence that you previously collected under that account. This is also the case when you deregister a delegated administrator from Organizations. However, Audit Manager stops collecting and attaching evidence to that delegated administrator account moving forward.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Keep in mind the following cleanup task if you use evidence finder:&lt;/p&gt; &lt;p&gt;Before you use your management account to remove a delegated administrator, make sure that the current delegated administrator account signs in to Audit Manager and disables evidence finder first. Disabling evidence finder automatically deletes the event data store that was created in their account when they enabled evidence finder. If this task isn’t completed, the event data store remains in their account. In this case, we recommend that the original delegated administrator goes to CloudTrail Lake and manually &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-disable-termination.html\&quot;&gt;deletes the event data store&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This cleanup task is necessary to ensure that you don&#39;t end up with multiple event data stores. Audit Manager ignores an unused event data store after you remove or change a delegated administrator account. However, the unused event data store continues to incur storage costs from CloudTrail Lake if you don&#39;t delete it.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;When you deregister a delegated administrator account for Audit Manager, the data for that account isn’t deleted. If you want to delete resource data for a delegated administrator account, you must perform that task separately before you deregister the account. Either, you can do this in the Audit Manager console. Or, you can use one of the delete API operations that are provided by Audit Manager. &lt;/p&gt; &lt;p&gt;To delete your Audit Manager resource data, see the following instructions: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessment.html\&quot;&gt;DeleteAssessment&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-assessment.html\&quot;&gt;Deleting an assessment&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html\&quot;&gt;DeleteAssessmentFramework&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html\&quot;&gt;Deleting a custom framework&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFrameworkShare.html\&quot;&gt;DeleteAssessmentFrameworkShare&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/deleting-shared-framework-requests.html\&quot;&gt;Deleting a share request&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html\&quot;&gt;DeleteAssessmentReport&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#delete-assessment-report-steps\&quot;&gt;Deleting an assessment report&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteControl.html\&quot;&gt;DeleteControl&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html\&quot;&gt;Deleting a custom control&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;At this time, Audit Manager doesn&#39;t provide an option to delete evidence for a specific delegated administrator. Instead, when your management account deregisters Audit Manager, we perform a cleanup for the current delegated administrator account at the time of deregistration.&lt;/p&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let deregisterOrganizationAdminAccountRequest = new AwsAuditManager.DeregisterOrganizationAdminAccountRequest(); // DeregisterOrganizationAdminAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterOrganizationAdminAccount(deregisterOrganizationAdminAccountRequest, opts, (error, data, response) => {
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
 **deregisterOrganizationAdminAccountRequest** | [**DeregisterOrganizationAdminAccountRequest**](DeregisterOrganizationAdminAccountRequest.md)|  | 
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


## disassociateAssessmentReportEvidenceFolder

> Object disassociateAssessmentReportEvidenceFolder(assessmentId, disassociateAssessmentReportEvidenceFolderRequest, opts)



 Disassociates an evidence folder from the specified assessment report in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let disassociateAssessmentReportEvidenceFolderRequest = new AwsAuditManager.DisassociateAssessmentReportEvidenceFolderRequest(); // DisassociateAssessmentReportEvidenceFolderRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateAssessmentReportEvidenceFolder(assessmentId, disassociateAssessmentReportEvidenceFolderRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **disassociateAssessmentReportEvidenceFolderRequest** | [**DisassociateAssessmentReportEvidenceFolderRequest**](DisassociateAssessmentReportEvidenceFolderRequest.md)|  | 
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


## getAccountStatus

> GetAccountStatusResponse getAccountStatus(opts)



 Gets the registration status of an account in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccountStatus(opts, (error, data, response) => {
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

[**GetAccountStatusResponse**](GetAccountStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssessment

> GetAssessmentResponse getAssessment(assessmentId, opts)



Gets information about a specified assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String | The unique identifier for the assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssessment(assessmentId, opts, (error, data, response) => {
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
 **assessmentId** | **String**| The unique identifier for the assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssessmentResponse**](GetAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssessmentFramework

> GetAssessmentFrameworkResponse getAssessmentFramework(frameworkId, opts)



Gets information about a specified framework.

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let frameworkId = "frameworkId_example"; // String |  The identifier for the framework. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssessmentFramework(frameworkId, opts, (error, data, response) => {
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
 **frameworkId** | **String**|  The identifier for the framework.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssessmentFrameworkResponse**](GetAssessmentFrameworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssessmentReportUrl

> GetAssessmentReportUrlResponse getAssessmentReportUrl(assessmentReportId, assessmentId, opts)



 Gets the URL of an assessment report in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentReportId = "assessmentReportId_example"; // String |  The unique identifier for the assessment report. 
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssessmentReportUrl(assessmentReportId, assessmentId, opts, (error, data, response) => {
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
 **assessmentReportId** | **String**|  The unique identifier for the assessment report.  | 
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssessmentReportUrlResponse**](GetAssessmentReportUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChangeLogs

> GetChangeLogsResponse getChangeLogs(assessmentId, opts)



 Gets a list of changelogs from Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String | The unique identifier for the assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'controlSetId': "controlSetId_example", // String |  The unique identifier for the control set. 
  'controlId': "controlId_example", // String |  The unique identifier for the control. 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number | Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.getChangeLogs(assessmentId, opts, (error, data, response) => {
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
 **assessmentId** | **String**| The unique identifier for the assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **controlSetId** | **String**|  The unique identifier for the control set.  | [optional] 
 **controlId** | **String**|  The unique identifier for the control.  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**| Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**GetChangeLogsResponse**](GetChangeLogsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getControl

> GetControlResponse getControl(controlId, opts)



 Gets information about a specified control.

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let controlId = "controlId_example"; // String |  The identifier for the control. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getControl(controlId, opts, (error, data, response) => {
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
 **controlId** | **String**|  The identifier for the control.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetControlResponse**](GetControlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDelegations

> GetDelegationsResponse getDelegations(opts)



 Gets a list of delegations from an audit owner to a delegate. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.getDelegations(opts, (error, data, response) => {
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
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**GetDelegationsResponse**](GetDelegationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidence

> GetEvidenceResponse getEvidence(assessmentId, controlSetId, evidenceFolderId, evidenceId, opts)



 Gets information about a specified evidence item.

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The unique identifier for the control set. 
let evidenceFolderId = "evidenceFolderId_example"; // String |  The unique identifier for the folder that the evidence is stored in. 
let evidenceId = "evidenceId_example"; // String |  The unique identifier for the evidence. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEvidence(assessmentId, controlSetId, evidenceFolderId, evidenceId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **controlSetId** | **String**|  The unique identifier for the control set.  | 
 **evidenceFolderId** | **String**|  The unique identifier for the folder that the evidence is stored in.  | 
 **evidenceId** | **String**|  The unique identifier for the evidence.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEvidenceResponse**](GetEvidenceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidenceByEvidenceFolder

> GetEvidenceByEvidenceFolderResponse getEvidenceByEvidenceFolder(assessmentId, controlSetId, evidenceFolderId, opts)



 Gets all evidence from a specified evidence folder in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The identifier for the control set. 
let evidenceFolderId = "evidenceFolderId_example"; // String |  The unique identifier for the folder that the evidence is stored in. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.getEvidenceByEvidenceFolder(assessmentId, controlSetId, evidenceFolderId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **controlSetId** | **String**|  The identifier for the control set.  | 
 **evidenceFolderId** | **String**|  The unique identifier for the folder that the evidence is stored in.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**GetEvidenceByEvidenceFolderResponse**](GetEvidenceByEvidenceFolderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidenceFileUploadUrl

> GetEvidenceFileUploadUrlResponse getEvidenceFileUploadUrl(fileName, opts)



&lt;p&gt;Creates a presigned Amazon S3 URL that can be used to upload a file as manual evidence. For instructions on how to use this operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#how-to-upload-manual-evidence-files\&quot;&gt;Upload a file from your browser &lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following restrictions apply to this operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum size of an individual evidence file: 100 MB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Number of daily manual evidence uploads per control: 100&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Supported file formats: See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\&quot;&gt;Supported file types for manual evidence&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about Audit Manager service restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html\&quot;&gt;Quotas and restrictions for Audit Manager&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let fileName = "fileName_example"; // String | The file that you want to upload. For a list of supported file formats, see <a href=\"https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\">Supported file types for manual evidence</a> in the <i>Audit Manager User Guide</i>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEvidenceFileUploadUrl(fileName, opts, (error, data, response) => {
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
 **fileName** | **String**| The file that you want to upload. For a list of supported file formats, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\&quot;&gt;Supported file types for manual evidence&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEvidenceFileUploadUrlResponse**](GetEvidenceFileUploadUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidenceFolder

> GetEvidenceFolderResponse getEvidenceFolder(assessmentId, controlSetId, evidenceFolderId, opts)



 Gets an evidence folder from a specified assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The unique identifier for the control set. 
let evidenceFolderId = "evidenceFolderId_example"; // String |  The unique identifier for the folder that the evidence is stored in. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEvidenceFolder(assessmentId, controlSetId, evidenceFolderId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **controlSetId** | **String**|  The unique identifier for the control set.  | 
 **evidenceFolderId** | **String**|  The unique identifier for the folder that the evidence is stored in.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEvidenceFolderResponse**](GetEvidenceFolderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidenceFoldersByAssessment

> GetEvidenceFoldersByAssessmentResponse getEvidenceFoldersByAssessment(assessmentId, opts)



 Gets the evidence folders from a specified assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.getEvidenceFoldersByAssessment(assessmentId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**GetEvidenceFoldersByAssessmentResponse**](GetEvidenceFoldersByAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidenceFoldersByAssessmentControl

> GetEvidenceFoldersByAssessmentControlResponse getEvidenceFoldersByAssessmentControl(assessmentId, controlSetId, controlId, opts)



 Gets a list of evidence folders that are associated with a specified control in an Audit Manager assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The identifier for the control set. 
let controlId = "controlId_example"; // String |  The identifier for the control. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.getEvidenceFoldersByAssessmentControl(assessmentId, controlSetId, controlId, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The identifier for the assessment.  | 
 **controlSetId** | **String**|  The identifier for the control set.  | 
 **controlId** | **String**|  The identifier for the control.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**GetEvidenceFoldersByAssessmentControlResponse**](GetEvidenceFoldersByAssessmentControlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInsights

> GetInsightsResponse getInsights(opts)



Gets the latest analytics data for all your current active assessments. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getInsights(opts, (error, data, response) => {
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

[**GetInsightsResponse**](GetInsightsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInsightsByAssessment

> GetInsightsByAssessmentResponse getInsightsByAssessment(assessmentId, opts)



Gets the latest analytics data for a specific active assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String | The unique identifier for the assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getInsightsByAssessment(assessmentId, opts, (error, data, response) => {
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
 **assessmentId** | **String**| The unique identifier for the assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetInsightsByAssessmentResponse**](GetInsightsByAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdminAccount

> GetOrganizationAdminAccountResponse getOrganizationAdminAccount(opts)



 Gets the name of the delegated Amazon Web Services administrator account for a specified organization. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOrganizationAdminAccount(opts, (error, data, response) => {
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

[**GetOrganizationAdminAccountResponse**](GetOrganizationAdminAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServicesInScope

> GetServicesInScopeResponse getServicesInScope(opts)



Gets a list of all of the Amazon Web Services that you can choose to include in your assessment. When you &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessment.html\&quot;&gt;create an assessment&lt;/a&gt;, specify which of these services you want to include to narrow the assessment&#39;s &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Scope.html\&quot;&gt;scope&lt;/a&gt;.

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServicesInScope(opts, (error, data, response) => {
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

[**GetServicesInScopeResponse**](GetServicesInScopeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSettings

> GetSettingsResponse getSettings(attribute, opts)



 Gets the settings for a specified Amazon Web Services account. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let attribute = "attribute_example"; // String |  The list of setting attribute enum values. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSettings(attribute, opts, (error, data, response) => {
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
 **attribute** | **String**|  The list of setting attribute enum values.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSettingsResponse**](GetSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssessmentControlInsightsByControlDomain

> ListAssessmentControlInsightsByControlDomainResponse listAssessmentControlInsightsByControlDomain(controlDomainId, assessmentId, opts)



&lt;p&gt;Lists the latest analytics data for controls within a specific control domain and a specific active assessment.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Control insights are listed only if the control belongs to the control domain and assessment that was specified. Moreover, the control must have collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlInsightsByAssessment&lt;/code&gt;. If neither of these conditions are met, no data is listed for that control. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let controlDomainId = "controlDomainId_example"; // String | The unique identifier for the control domain. 
let assessmentId = "assessmentId_example"; // String | The unique identifier for the active assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number | Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listAssessmentControlInsightsByControlDomain(controlDomainId, assessmentId, opts, (error, data, response) => {
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
 **controlDomainId** | **String**| The unique identifier for the control domain.  | 
 **assessmentId** | **String**| The unique identifier for the active assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**| Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListAssessmentControlInsightsByControlDomainResponse**](ListAssessmentControlInsightsByControlDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssessmentFrameworkShareRequests

> ListAssessmentFrameworkShareRequestsResponse listAssessmentFrameworkShareRequests(requestType, opts)



 Returns a list of sent or received share requests for custom frameworks in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let requestType = "requestType_example"; // String |  Specifies whether the share request is a sent request or a received request.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listAssessmentFrameworkShareRequests(requestType, opts, (error, data, response) => {
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
 **requestType** | **String**|  Specifies whether the share request is a sent request or a received request. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListAssessmentFrameworkShareRequestsResponse**](ListAssessmentFrameworkShareRequestsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssessmentFrameworks

> ListAssessmentFrameworksResponse listAssessmentFrameworks(frameworkType, opts)



 Returns a list of the frameworks that are available in the Audit Manager framework library. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let frameworkType = "frameworkType_example"; // String |  The type of framework, such as a standard framework or a custom framework. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listAssessmentFrameworks(frameworkType, opts, (error, data, response) => {
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
 **frameworkType** | **String**|  The type of framework, such as a standard framework or a custom framework.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListAssessmentFrameworksResponse**](ListAssessmentFrameworksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssessmentReports

> ListAssessmentReportsResponse listAssessmentReports(opts)



 Returns a list of assessment reports created in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listAssessmentReports(opts, (error, data, response) => {
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
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListAssessmentReportsResponse**](ListAssessmentReportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssessments

> ListAssessmentsResponse listAssessments(opts)



 Returns a list of current and past assessments from Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'status': "status_example", // String |  The current status of the assessment.
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listAssessments(opts, (error, data, response) => {
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
 **status** | **String**|  The current status of the assessment. | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListAssessmentsResponse**](ListAssessmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listControlDomainInsights

> ListControlDomainInsightsResponse listControlDomainInsights(opts)



&lt;p&gt;Lists the latest analytics data for control domains across all of your active assessments. &lt;/p&gt; &lt;note&gt; &lt;p&gt;A control domain is listed only if at least one of the controls within that domain collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlDomainInsights&lt;/code&gt;. If this condition isn’t met, no data is listed for that control domain.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number | Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listControlDomainInsights(opts, (error, data, response) => {
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
 **nextToken** | **String**| The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**| Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListControlDomainInsightsResponse**](ListControlDomainInsightsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listControlDomainInsightsByAssessment

> ListControlDomainInsightsByAssessmentResponse listControlDomainInsightsByAssessment(assessmentId, opts)



&lt;p&gt;Lists analytics data for control domains within a specified active assessment.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A control domain is listed only if at least one of the controls within that domain collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlDomainInsights&lt;/code&gt;. If this condition isn’t met, no data is listed for that domain.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String | The unique identifier for the active assessment. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number | Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listControlDomainInsightsByAssessment(assessmentId, opts, (error, data, response) => {
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
 **assessmentId** | **String**| The unique identifier for the active assessment.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**| Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListControlDomainInsightsByAssessmentResponse**](ListControlDomainInsightsByAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listControlInsightsByControlDomain

> ListControlInsightsByControlDomainResponse listControlInsightsByControlDomain(controlDomainId, opts)



&lt;p&gt;Lists the latest analytics data for controls within a specific control domain across all active assessments.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Control insights are listed only if the control belongs to the control domain that was specified and the control collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlInsightsMetadata&lt;/code&gt;. If neither of these conditions are met, no data is listed for that control. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let controlDomainId = "controlDomainId_example"; // String | The unique identifier for the control domain. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number | Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listControlInsightsByControlDomain(controlDomainId, opts, (error, data, response) => {
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
 **controlDomainId** | **String**| The unique identifier for the control domain.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**| Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListControlInsightsByControlDomainResponse**](ListControlInsightsByControlDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listControls

> ListControlsResponse listControls(controlType, opts)



 Returns a list of controls from Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let controlType = "controlType_example"; // String |  The type of control, such as a standard control or a custom control. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listControls(controlType, opts, (error, data, response) => {
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
 **controlType** | **String**|  The type of control, such as a standard control or a custom control.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListControlsResponse**](ListControlsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listKeywordsForDataSource

> ListKeywordsForDataSourceResponse listKeywordsForDataSource(source, opts)



 Returns a list of keywords that are pre-mapped to the specified control data source. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let source = "source_example"; // String |  The control mapping data source that the keywords apply to. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listKeywordsForDataSource(source, opts, (error, data, response) => {
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
 **source** | **String**|  The control mapping data source that the keywords apply to.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListKeywordsForDataSourceResponse**](ListKeywordsForDataSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNotifications

> ListNotificationsResponse listNotifications(opts)



 Returns a list of all Audit Manager notifications. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String |  The pagination token that's used to fetch the next set of results. 
  'maxResults': 56 // Number |  Represents the maximum number of results on a page or for an API request call. 
};
apiInstance.listNotifications(opts, (error, data, response) => {
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
 **nextToken** | **String**|  The pagination token that&#39;s used to fetch the next set of results.  | [optional] 
 **maxResults** | **Number**|  Represents the maximum number of results on a page or for an API request call.  | [optional] 

### Return type

[**ListNotificationsResponse**](ListNotificationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



 Returns a list of tags for the specified resource in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the resource. 
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
 **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the resource.  | 
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


## registerAccount

> RegisterAccountResponse registerAccount(registerAccountRequest, opts)



 Enables Audit Manager for the specified Amazon Web Services account. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let registerAccountRequest = new AwsAuditManager.RegisterAccountRequest(); // RegisterAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerAccount(registerAccountRequest, opts, (error, data, response) => {
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
 **registerAccountRequest** | [**RegisterAccountRequest**](RegisterAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterAccountResponse**](RegisterAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registerOrganizationAdminAccount

> RegisterOrganizationAdminAccountResponse registerOrganizationAdminAccount(registerOrganizationAdminAccountRequest, opts)



 Enables an Amazon Web Services account within the organization as the delegated administrator for Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let registerOrganizationAdminAccountRequest = new AwsAuditManager.RegisterOrganizationAdminAccountRequest(); // RegisterOrganizationAdminAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerOrganizationAdminAccount(registerOrganizationAdminAccountRequest, opts, (error, data, response) => {
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
 **registerOrganizationAdminAccountRequest** | [**RegisterOrganizationAdminAccountRequest**](RegisterOrganizationAdminAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterOrganizationAdminAccountResponse**](RegisterOrganizationAdminAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startAssessmentFrameworkShare

> StartAssessmentFrameworkShareResponse startAssessmentFrameworkShare(frameworkId, startAssessmentFrameworkShareRequest, opts)



&lt;p&gt; Creates a share request for a custom framework in Audit Manager. &lt;/p&gt; &lt;p&gt;The share request specifies a recipient and notifies them that a custom framework is available. Recipients have 120 days to accept or decline the request. If no action is taken, the share request expires.&lt;/p&gt; &lt;p&gt;When you create a share request, Audit Manager stores a snapshot of your custom framework in the US East (N. Virginia) Amazon Web Services Region. Audit Manager also stores a backup of the same snapshot in the US West (Oregon) Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;Audit Manager deletes the snapshot and the backup snapshot when one of the following events occurs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The sender revokes the share request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The recipient declines the share request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The recipient encounters an error and doesn&#39;t successfully accept the share request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The share request expires before the recipient responds to the request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When a sender &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend\&quot;&gt;resends a share request&lt;/a&gt;, the snapshot is replaced with an updated version that corresponds with the latest version of the custom framework. &lt;/p&gt; &lt;p&gt;When a recipient accepts a share request, the snapshot is replicated into their Amazon Web Services account under the Amazon Web Services Region that was specified in the share request. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you invoke the &lt;code&gt;StartAssessmentFrameworkShare&lt;/code&gt; API, you are about to share a custom framework with another Amazon Web Services account. You may not share a custom framework that is derived from a standard framework if the standard framework is designated as not eligible for sharing by Amazon Web Services, unless you have obtained permission to do so from the owner of the standard framework. To learn more about which standard frameworks are eligible for sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility\&quot;&gt;Framework sharing eligibility&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let frameworkId = "frameworkId_example"; // String |  The unique identifier for the custom framework to be shared. 
let startAssessmentFrameworkShareRequest = new AwsAuditManager.StartAssessmentFrameworkShareRequest(); // StartAssessmentFrameworkShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAssessmentFrameworkShare(frameworkId, startAssessmentFrameworkShareRequest, opts, (error, data, response) => {
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
 **frameworkId** | **String**|  The unique identifier for the custom framework to be shared.  | 
 **startAssessmentFrameworkShareRequest** | [**StartAssessmentFrameworkShareRequest**](StartAssessmentFrameworkShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartAssessmentFrameworkShareResponse**](StartAssessmentFrameworkShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



 Tags the specified resource in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the resource. 
let tagResourceRequest = new AwsAuditManager.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the resource.  | 
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



 Removes a tag from a resource in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the specified resource. 
let tagKeys = ["null"]; // [String] |  The name or key of the tag. 
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
 **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the specified resource.  | 
 **tagKeys** | [**[String]**](String.md)|  The name or key of the tag.  | 
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


## updateAssessment

> UpdateAssessmentResponse updateAssessment(assessmentId, updateAssessmentRequest, opts)



 Edits an Audit Manager assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let updateAssessmentRequest = new AwsAuditManager.UpdateAssessmentRequest(); // UpdateAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessment(assessmentId, updateAssessmentRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **updateAssessmentRequest** | [**UpdateAssessmentRequest**](UpdateAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssessmentResponse**](UpdateAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssessmentControl

> UpdateAssessmentControlResponse updateAssessmentControl(assessmentId, controlSetId, controlId, updateAssessmentControlRequest, opts)



 Updates a control within an assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The unique identifier for the control set. 
let controlId = "controlId_example"; // String |  The unique identifier for the control. 
let updateAssessmentControlRequest = new AwsAuditManager.UpdateAssessmentControlRequest(); // UpdateAssessmentControlRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessmentControl(assessmentId, controlSetId, controlId, updateAssessmentControlRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **controlSetId** | **String**|  The unique identifier for the control set.  | 
 **controlId** | **String**|  The unique identifier for the control.  | 
 **updateAssessmentControlRequest** | [**UpdateAssessmentControlRequest**](UpdateAssessmentControlRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssessmentControlResponse**](UpdateAssessmentControlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssessmentControlSetStatus

> UpdateAssessmentControlSetStatusResponse updateAssessmentControlSetStatus(assessmentId, controlSetId, updateAssessmentControlSetStatusRequest, opts)



 Updates the status of a control set in an Audit Manager assessment. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let controlSetId = "controlSetId_example"; // String |  The unique identifier for the control set. 
let updateAssessmentControlSetStatusRequest = new AwsAuditManager.UpdateAssessmentControlSetStatusRequest(); // UpdateAssessmentControlSetStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessmentControlSetStatus(assessmentId, controlSetId, updateAssessmentControlSetStatusRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **controlSetId** | **String**|  The unique identifier for the control set.  | 
 **updateAssessmentControlSetStatusRequest** | [**UpdateAssessmentControlSetStatusRequest**](UpdateAssessmentControlSetStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssessmentControlSetStatusResponse**](UpdateAssessmentControlSetStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssessmentFramework

> UpdateAssessmentFrameworkResponse updateAssessmentFramework(frameworkId, updateAssessmentFrameworkRequest, opts)



 Updates a custom framework in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let frameworkId = "frameworkId_example"; // String |  The unique identifier for the framework. 
let updateAssessmentFrameworkRequest = new AwsAuditManager.UpdateAssessmentFrameworkRequest(); // UpdateAssessmentFrameworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessmentFramework(frameworkId, updateAssessmentFrameworkRequest, opts, (error, data, response) => {
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
 **frameworkId** | **String**|  The unique identifier for the framework.  | 
 **updateAssessmentFrameworkRequest** | [**UpdateAssessmentFrameworkRequest**](UpdateAssessmentFrameworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssessmentFrameworkResponse**](UpdateAssessmentFrameworkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssessmentFrameworkShare

> UpdateAssessmentFrameworkShareResponse updateAssessmentFrameworkShare(requestId, updateAssessmentFrameworkShareRequest, opts)



 Updates a share request for a custom framework in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let requestId = "requestId_example"; // String |  The unique identifier for the share request. 
let updateAssessmentFrameworkShareRequest = new AwsAuditManager.UpdateAssessmentFrameworkShareRequest(); // UpdateAssessmentFrameworkShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessmentFrameworkShare(requestId, updateAssessmentFrameworkShareRequest, opts, (error, data, response) => {
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
 **requestId** | **String**|  The unique identifier for the share request.  | 
 **updateAssessmentFrameworkShareRequest** | [**UpdateAssessmentFrameworkShareRequest**](UpdateAssessmentFrameworkShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssessmentFrameworkShareResponse**](UpdateAssessmentFrameworkShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssessmentStatus

> UpdateAssessmentStatusResponse updateAssessmentStatus(assessmentId, updateAssessmentStatusRequest, opts)



 Updates the status of an assessment in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let assessmentId = "assessmentId_example"; // String |  The unique identifier for the assessment. 
let updateAssessmentStatusRequest = new AwsAuditManager.UpdateAssessmentStatusRequest(); // UpdateAssessmentStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAssessmentStatus(assessmentId, updateAssessmentStatusRequest, opts, (error, data, response) => {
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
 **assessmentId** | **String**|  The unique identifier for the assessment.  | 
 **updateAssessmentStatusRequest** | [**UpdateAssessmentStatusRequest**](UpdateAssessmentStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAssessmentStatusResponse**](UpdateAssessmentStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateControl

> UpdateControlResponse updateControl(controlId, updateControlRequest, opts)



 Updates a custom control in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let controlId = "controlId_example"; // String |  The identifier for the control. 
let updateControlRequest = new AwsAuditManager.UpdateControlRequest(); // UpdateControlRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateControl(controlId, updateControlRequest, opts, (error, data, response) => {
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
 **controlId** | **String**|  The identifier for the control.  | 
 **updateControlRequest** | [**UpdateControlRequest**](UpdateControlRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateControlResponse**](UpdateControlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSettings

> UpdateSettingsResponse updateSettings(updateSettingsRequest, opts)



 Updates Audit Manager settings for the current account. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let updateSettingsRequest = new AwsAuditManager.UpdateSettingsRequest(); // UpdateSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSettings(updateSettingsRequest, opts, (error, data, response) => {
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
 **updateSettingsRequest** | [**UpdateSettingsRequest**](UpdateSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSettingsResponse**](UpdateSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateAssessmentReportIntegrity

> ValidateAssessmentReportIntegrityResponse validateAssessmentReportIntegrity(validateAssessmentReportIntegrityRequest, opts)



 Validates the integrity of an assessment report in Audit Manager. 

### Example

```javascript
import AwsAuditManager from 'aws_audit_manager';
let defaultClient = AwsAuditManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAuditManager.DefaultApi();
let validateAssessmentReportIntegrityRequest = new AwsAuditManager.ValidateAssessmentReportIntegrityRequest(); // ValidateAssessmentReportIntegrityRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.validateAssessmentReportIntegrity(validateAssessmentReportIntegrityRequest, opts, (error, data, response) => {
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
 **validateAssessmentReportIntegrityRequest** | [**ValidateAssessmentReportIntegrityRequest**](ValidateAssessmentReportIntegrityRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ValidateAssessmentReportIntegrityResponse**](ValidateAssessmentReportIntegrityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

