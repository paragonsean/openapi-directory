# AwsBackup.DefaultApi

All URIs are relative to *http://backup.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelLegalHold**](DefaultApi.md#cancelLegalHold) | **DELETE** /legal-holds/{legalHoldId}#cancelDescription | 
[**createBackupPlan**](DefaultApi.md#createBackupPlan) | **PUT** /backup/plans/ | 
[**createBackupSelection**](DefaultApi.md#createBackupSelection) | **PUT** /backup/plans/{backupPlanId}/selections/ | 
[**createBackupVault**](DefaultApi.md#createBackupVault) | **PUT** /backup-vaults/{backupVaultName} | 
[**createFramework**](DefaultApi.md#createFramework) | **POST** /audit/frameworks | 
[**createLegalHold**](DefaultApi.md#createLegalHold) | **POST** /legal-holds/ | 
[**createReportPlan**](DefaultApi.md#createReportPlan) | **POST** /audit/report-plans | 
[**deleteBackupPlan**](DefaultApi.md#deleteBackupPlan) | **DELETE** /backup/plans/{backupPlanId} | 
[**deleteBackupSelection**](DefaultApi.md#deleteBackupSelection) | **DELETE** /backup/plans/{backupPlanId}/selections/{selectionId} | 
[**deleteBackupVault**](DefaultApi.md#deleteBackupVault) | **DELETE** /backup-vaults/{backupVaultName} | 
[**deleteBackupVaultAccessPolicy**](DefaultApi.md#deleteBackupVaultAccessPolicy) | **DELETE** /backup-vaults/{backupVaultName}/access-policy | 
[**deleteBackupVaultLockConfiguration**](DefaultApi.md#deleteBackupVaultLockConfiguration) | **DELETE** /backup-vaults/{backupVaultName}/vault-lock | 
[**deleteBackupVaultNotifications**](DefaultApi.md#deleteBackupVaultNotifications) | **DELETE** /backup-vaults/{backupVaultName}/notification-configuration | 
[**deleteFramework**](DefaultApi.md#deleteFramework) | **DELETE** /audit/frameworks/{frameworkName} | 
[**deleteRecoveryPoint**](DefaultApi.md#deleteRecoveryPoint) | **DELETE** /backup-vaults/{backupVaultName}/recovery-points/{recoveryPointArn} | 
[**deleteReportPlan**](DefaultApi.md#deleteReportPlan) | **DELETE** /audit/report-plans/{reportPlanName} | 
[**describeBackupJob**](DefaultApi.md#describeBackupJob) | **GET** /backup-jobs/{backupJobId} | 
[**describeBackupVault**](DefaultApi.md#describeBackupVault) | **GET** /backup-vaults/{backupVaultName} | 
[**describeCopyJob**](DefaultApi.md#describeCopyJob) | **GET** /copy-jobs/{copyJobId} | 
[**describeFramework**](DefaultApi.md#describeFramework) | **GET** /audit/frameworks/{frameworkName} | 
[**describeGlobalSettings**](DefaultApi.md#describeGlobalSettings) | **GET** /global-settings | 
[**describeProtectedResource**](DefaultApi.md#describeProtectedResource) | **GET** /resources/{resourceArn} | 
[**describeRecoveryPoint**](DefaultApi.md#describeRecoveryPoint) | **GET** /backup-vaults/{backupVaultName}/recovery-points/{recoveryPointArn} | 
[**describeRegionSettings**](DefaultApi.md#describeRegionSettings) | **GET** /account-settings | 
[**describeReportJob**](DefaultApi.md#describeReportJob) | **GET** /audit/report-jobs/{reportJobId} | 
[**describeReportPlan**](DefaultApi.md#describeReportPlan) | **GET** /audit/report-plans/{reportPlanName} | 
[**describeRestoreJob**](DefaultApi.md#describeRestoreJob) | **GET** /restore-jobs/{restoreJobId} | 
[**disassociateRecoveryPoint**](DefaultApi.md#disassociateRecoveryPoint) | **POST** /backup-vaults/{backupVaultName}/recovery-points/{recoveryPointArn}/disassociate | 
[**disassociateRecoveryPointFromParent**](DefaultApi.md#disassociateRecoveryPointFromParent) | **DELETE** /backup-vaults/{backupVaultName}/recovery-points/{recoveryPointArn}/parentAssociation | 
[**exportBackupPlanTemplate**](DefaultApi.md#exportBackupPlanTemplate) | **GET** /backup/plans/{backupPlanId}/toTemplate/ | 
[**getBackupPlan**](DefaultApi.md#getBackupPlan) | **GET** /backup/plans/{backupPlanId}/ | 
[**getBackupPlanFromJSON**](DefaultApi.md#getBackupPlanFromJSON) | **POST** /backup/template/json/toPlan | 
[**getBackupPlanFromTemplate**](DefaultApi.md#getBackupPlanFromTemplate) | **GET** /backup/template/plans/{templateId}/toPlan | 
[**getBackupSelection**](DefaultApi.md#getBackupSelection) | **GET** /backup/plans/{backupPlanId}/selections/{selectionId} | 
[**getBackupVaultAccessPolicy**](DefaultApi.md#getBackupVaultAccessPolicy) | **GET** /backup-vaults/{backupVaultName}/access-policy | 
[**getBackupVaultNotifications**](DefaultApi.md#getBackupVaultNotifications) | **GET** /backup-vaults/{backupVaultName}/notification-configuration | 
[**getLegalHold**](DefaultApi.md#getLegalHold) | **GET** /legal-holds/{legalHoldId}/ | 
[**getRecoveryPointRestoreMetadata**](DefaultApi.md#getRecoveryPointRestoreMetadata) | **GET** /backup-vaults/{backupVaultName}/recovery-points/{recoveryPointArn}/restore-metadata | 
[**getSupportedResourceTypes**](DefaultApi.md#getSupportedResourceTypes) | **GET** /supported-resource-types | 
[**listBackupJobs**](DefaultApi.md#listBackupJobs) | **GET** /backup-jobs/ | 
[**listBackupPlanTemplates**](DefaultApi.md#listBackupPlanTemplates) | **GET** /backup/template/plans | 
[**listBackupPlanVersions**](DefaultApi.md#listBackupPlanVersions) | **GET** /backup/plans/{backupPlanId}/versions/ | 
[**listBackupPlans**](DefaultApi.md#listBackupPlans) | **GET** /backup/plans/ | 
[**listBackupSelections**](DefaultApi.md#listBackupSelections) | **GET** /backup/plans/{backupPlanId}/selections/ | 
[**listBackupVaults**](DefaultApi.md#listBackupVaults) | **GET** /backup-vaults/ | 
[**listCopyJobs**](DefaultApi.md#listCopyJobs) | **GET** /copy-jobs/ | 
[**listFrameworks**](DefaultApi.md#listFrameworks) | **GET** /audit/frameworks | 
[**listLegalHolds**](DefaultApi.md#listLegalHolds) | **GET** /legal-holds/ | 
[**listProtectedResources**](DefaultApi.md#listProtectedResources) | **GET** /resources/ | 
[**listRecoveryPointsByBackupVault**](DefaultApi.md#listRecoveryPointsByBackupVault) | **GET** /backup-vaults/{backupVaultName}/recovery-points/ | 
[**listRecoveryPointsByLegalHold**](DefaultApi.md#listRecoveryPointsByLegalHold) | **GET** /legal-holds/{legalHoldId}/recovery-points | 
[**listRecoveryPointsByResource**](DefaultApi.md#listRecoveryPointsByResource) | **GET** /resources/{resourceArn}/recovery-points/ | 
[**listReportJobs**](DefaultApi.md#listReportJobs) | **GET** /audit/report-jobs | 
[**listReportPlans**](DefaultApi.md#listReportPlans) | **GET** /audit/report-plans | 
[**listRestoreJobs**](DefaultApi.md#listRestoreJobs) | **GET** /restore-jobs/ | 
[**listTags**](DefaultApi.md#listTags) | **GET** /tags/{resourceArn}/ | 
[**putBackupVaultAccessPolicy**](DefaultApi.md#putBackupVaultAccessPolicy) | **PUT** /backup-vaults/{backupVaultName}/access-policy | 
[**putBackupVaultLockConfiguration**](DefaultApi.md#putBackupVaultLockConfiguration) | **PUT** /backup-vaults/{backupVaultName}/vault-lock | 
[**putBackupVaultNotifications**](DefaultApi.md#putBackupVaultNotifications) | **PUT** /backup-vaults/{backupVaultName}/notification-configuration | 
[**startBackupJob**](DefaultApi.md#startBackupJob) | **PUT** /backup-jobs | 
[**startCopyJob**](DefaultApi.md#startCopyJob) | **PUT** /copy-jobs | 
[**startReportJob**](DefaultApi.md#startReportJob) | **POST** /audit/report-jobs/{reportPlanName} | 
[**startRestoreJob**](DefaultApi.md#startRestoreJob) | **PUT** /restore-jobs | 
[**stopBackupJob**](DefaultApi.md#stopBackupJob) | **POST** /backup-jobs/{backupJobId} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /untag/{resourceArn} | 
[**updateBackupPlan**](DefaultApi.md#updateBackupPlan) | **POST** /backup/plans/{backupPlanId} | 
[**updateFramework**](DefaultApi.md#updateFramework) | **PUT** /audit/frameworks/{frameworkName} | 
[**updateGlobalSettings**](DefaultApi.md#updateGlobalSettings) | **PUT** /global-settings | 
[**updateRecoveryPointLifecycle**](DefaultApi.md#updateRecoveryPointLifecycle) | **POST** /backup-vaults/{backupVaultName}/recovery-points/{recoveryPointArn} | 
[**updateRegionSettings**](DefaultApi.md#updateRegionSettings) | **PUT** /account-settings | 
[**updateReportPlan**](DefaultApi.md#updateReportPlan) | **PUT** /audit/report-plans/{reportPlanName} | 



## cancelLegalHold

> Object cancelLegalHold(legalHoldId, cancelDescription, opts)



This action removes the specified legal hold on a recovery point. This action can only be performed by a user with sufficient permissions.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let legalHoldId = "legalHoldId_example"; // String | Legal hold ID required to remove the specified legal hold on a recovery point.
let cancelDescription = "cancelDescription_example"; // String | String describing the reason for removing the legal hold.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'retainRecordInDays': 56 // Number | The integer amount in days specifying amount of days after this API operation to remove legal hold.
};
apiInstance.cancelLegalHold(legalHoldId, cancelDescription, opts, (error, data, response) => {
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
 **legalHoldId** | **String**| Legal hold ID required to remove the specified legal hold on a recovery point. | 
 **cancelDescription** | **String**| String describing the reason for removing the legal hold. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **retainRecordInDays** | **Number**| The integer amount in days specifying amount of days after this API operation to remove legal hold. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createBackupPlan

> CreateBackupPlanOutput createBackupPlan(createBackupPlanRequest, opts)



&lt;p&gt;Creates a backup plan using a backup plan name and backup rules. A backup plan is a document that contains information that Backup uses to schedule tasks that create recovery points for resources.&lt;/p&gt; &lt;p&gt;If you call &lt;code&gt;CreateBackupPlan&lt;/code&gt; with a plan that already exists, you receive an &lt;code&gt;AlreadyExistsException&lt;/code&gt; exception.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let createBackupPlanRequest = new AwsBackup.CreateBackupPlanRequest(); // CreateBackupPlanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackupPlan(createBackupPlanRequest, opts, (error, data, response) => {
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
 **createBackupPlanRequest** | [**CreateBackupPlanRequest**](CreateBackupPlanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackupPlanOutput**](CreateBackupPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackupSelection

> CreateBackupSelectionOutput createBackupSelection(backupPlanId, createBackupSelectionRequest, opts)



Creates a JSON document that specifies a set of resources to assign to a backup plan. For examples, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-json\&quot;&gt;Assigning resources programmatically&lt;/a&gt;. 

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies the backup plan to be associated with the selection of resources.
let createBackupSelectionRequest = new AwsBackup.CreateBackupSelectionRequest(); // CreateBackupSelectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackupSelection(backupPlanId, createBackupSelectionRequest, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies the backup plan to be associated with the selection of resources. | 
 **createBackupSelectionRequest** | [**CreateBackupSelectionRequest**](CreateBackupSelectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackupSelectionOutput**](CreateBackupSelectionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBackupVault

> CreateBackupVaultOutput createBackupVault(backupVaultName, createBackupVaultRequest, opts)



&lt;p&gt;Creates a logical container where backups are stored. A &lt;code&gt;CreateBackupVault&lt;/code&gt; request includes a name, optionally one or more resource tags, an encryption key, and a request ID.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Do not include sensitive data, such as passport numbers, in the name of a backup vault.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of letters, numbers, and hyphens.
let createBackupVaultRequest = new AwsBackup.CreateBackupVaultRequest(); // CreateBackupVaultRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBackupVault(backupVaultName, createBackupVaultRequest, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of letters, numbers, and hyphens. | 
 **createBackupVaultRequest** | [**CreateBackupVaultRequest**](CreateBackupVaultRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBackupVaultOutput**](CreateBackupVaultOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFramework

> CreateFrameworkOutput createFramework(createFrameworkRequest, opts)



Creates a framework with one or more controls. A framework is a collection of controls that you can use to evaluate your backup practices. By using pre-built customizable controls to define your policies, you can evaluate whether your backup practices comply with your policies and which resources are not yet in compliance.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let createFrameworkRequest = new AwsBackup.CreateFrameworkRequest(); // CreateFrameworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFramework(createFrameworkRequest, opts, (error, data, response) => {
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
 **createFrameworkRequest** | [**CreateFrameworkRequest**](CreateFrameworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateFrameworkOutput**](CreateFrameworkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLegalHold

> CreateLegalHoldOutput createLegalHold(createLegalHoldRequest, opts)



This action creates a legal hold on a recovery point (backup). A legal hold is a restraint on altering or deleting a backup until an authorized user cancels the legal hold. Any actions to delete or disassociate a recovery point will fail with an error if one or more active legal holds are on the recovery point.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let createLegalHoldRequest = new AwsBackup.CreateLegalHoldRequest(); // CreateLegalHoldRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLegalHold(createLegalHoldRequest, opts, (error, data, response) => {
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
 **createLegalHoldRequest** | [**CreateLegalHoldRequest**](CreateLegalHoldRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLegalHoldOutput**](CreateLegalHoldOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReportPlan

> CreateReportPlanOutput createReportPlan(createReportPlanRequest, opts)



&lt;p&gt;Creates a report plan. A report plan is a document that contains information about the contents of the report and where Backup will deliver it.&lt;/p&gt; &lt;p&gt;If you call &lt;code&gt;CreateReportPlan&lt;/code&gt; with a plan that already exists, you receive an &lt;code&gt;AlreadyExistsException&lt;/code&gt; exception.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let createReportPlanRequest = new AwsBackup.CreateReportPlanRequest(); // CreateReportPlanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createReportPlan(createReportPlanRequest, opts, (error, data, response) => {
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
 **createReportPlanRequest** | [**CreateReportPlanRequest**](CreateReportPlanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateReportPlanOutput**](CreateReportPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBackupPlan

> DeleteBackupPlanOutput deleteBackupPlan(backupPlanId, opts)



Deletes a backup plan. A backup plan can only be deleted after all associated selections of resources have been deleted. Deleting a backup plan deletes the current version of a backup plan. Previous versions, if any, will still exist.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackupPlan(backupPlanId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBackupPlanOutput**](DeleteBackupPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBackupSelection

> deleteBackupSelection(backupPlanId, selectionId, opts)



Deletes the resource selection associated with a backup plan that is specified by the &lt;code&gt;SelectionId&lt;/code&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let selectionId = "selectionId_example"; // String | Uniquely identifies the body of a request to assign a set of resources to a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackupSelection(backupPlanId, selectionId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **selectionId** | **String**| Uniquely identifies the body of a request to assign a set of resources to a backup plan. | 
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


## deleteBackupVault

> deleteBackupVault(backupVaultName, opts)



Deletes the backup vault identified by its name. A vault can be deleted only if it is empty.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackupVault(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
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


## deleteBackupVaultAccessPolicy

> deleteBackupVaultAccessPolicy(backupVaultName, opts)



Deletes the policy document that manages permissions on a backup vault.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackupVaultAccessPolicy(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
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


## deleteBackupVaultLockConfiguration

> deleteBackupVaultLockConfiguration(backupVaultName, opts)



&lt;p&gt;Deletes Backup Vault Lock from a backup vault specified by a backup vault name.&lt;/p&gt; &lt;p&gt;If the Vault Lock configuration is immutable, then you cannot delete Vault Lock using API operations, and you will receive an &lt;code&gt;InvalidRequestException&lt;/code&gt; if you attempt to do so. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html\&quot;&gt;Vault Lock&lt;/a&gt; in the &lt;i&gt;Backup Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of the backup vault from which to delete Backup Vault Lock.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackupVaultLockConfiguration(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of the backup vault from which to delete Backup Vault Lock. | 
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


## deleteBackupVaultNotifications

> deleteBackupVaultNotifications(backupVaultName, opts)



Deletes event notifications for the specified backup vault.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBackupVaultNotifications(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
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


## deleteFramework

> deleteFramework(frameworkName, opts)



Deletes the framework specified by a framework name.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let frameworkName = "frameworkName_example"; // String | The unique name of a framework.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteFramework(frameworkName, opts, (error, data, response) => {
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
 **frameworkName** | **String**| The unique name of a framework. | 
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


## deleteRecoveryPoint

> deleteRecoveryPoint(backupVaultName, recoveryPointArn, opts)



&lt;p&gt;Deletes the recovery point specified by a recovery point ID.&lt;/p&gt; &lt;p&gt;If the recovery point ID belongs to a continuous backup, calling this endpoint deletes the existing continuous backup and stops future continuous backup.&lt;/p&gt; &lt;p&gt;When an IAM role&#39;s permissions are insufficient to call this API, the service sends back an HTTP 200 response with an empty HTTP body, but the recovery point is not deleted. Instead, it enters an &lt;code&gt;EXPIRED&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt; &lt;code&gt;EXPIRED&lt;/code&gt; recovery points can be deleted with this API once the IAM role has the &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; action. To learn more about adding this role, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html#deleting-backups-troubleshooting\&quot;&gt; Troubleshooting manual deletions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the user or role is deleted or the permission within the role is removed, the deletion will not be successful and will enter an &lt;code&gt;EXPIRED&lt;/code&gt; state.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let recoveryPointArn = "recoveryPointArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRecoveryPoint(backupVaultName, recoveryPointArn, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **recoveryPointArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;. | 
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


## deleteReportPlan

> deleteReportPlan(reportPlanName, opts)



Deletes the report plan specified by a report plan name.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let reportPlanName = "reportPlanName_example"; // String | The unique name of a report plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteReportPlan(reportPlanName, opts, (error, data, response) => {
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
 **reportPlanName** | **String**| The unique name of a report plan. | 
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


## describeBackupJob

> DescribeBackupJobOutput describeBackupJob(backupJobId, opts)



Returns backup job details for the specified &lt;code&gt;BackupJobId&lt;/code&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupJobId = "backupJobId_example"; // String | Uniquely identifies a request to Backup to back up a resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBackupJob(backupJobId, opts, (error, data, response) => {
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
 **backupJobId** | **String**| Uniquely identifies a request to Backup to back up a resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBackupJobOutput**](DescribeBackupJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBackupVault

> DescribeBackupVaultOutput describeBackupVault(backupVaultName, opts)



Returns metadata about a backup vault specified by its name.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBackupVault(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBackupVaultOutput**](DescribeBackupVaultOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeCopyJob

> DescribeCopyJobOutput describeCopyJob(copyJobId, opts)



Returns metadata associated with creating a copy of a resource.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let copyJobId = "copyJobId_example"; // String | Uniquely identifies a copy job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeCopyJob(copyJobId, opts, (error, data, response) => {
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
 **copyJobId** | **String**| Uniquely identifies a copy job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeCopyJobOutput**](DescribeCopyJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeFramework

> DescribeFrameworkOutput describeFramework(frameworkName, opts)



Returns the framework details for the specified &lt;code&gt;FrameworkName&lt;/code&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let frameworkName = "frameworkName_example"; // String | The unique name of a framework.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeFramework(frameworkName, opts, (error, data, response) => {
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
 **frameworkName** | **String**| The unique name of a framework. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeFrameworkOutput**](DescribeFrameworkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeGlobalSettings

> DescribeGlobalSettingsOutput describeGlobalSettings(opts)



Describes whether the Amazon Web Services account is opted in to cross-account backup. Returns an error if the account is not a member of an Organizations organization. Example: &lt;code&gt;describe-global-settings --region us-west-2&lt;/code&gt; 

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeGlobalSettings(opts, (error, data, response) => {
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

[**DescribeGlobalSettingsOutput**](DescribeGlobalSettingsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeProtectedResource

> DescribeProtectedResourceOutput describeProtectedResource(resourceArn, opts)



Returns information about a saved resource, including the last time it was backed up, its Amazon Resource Name (ARN), and the Amazon Web Services service type of the saved resource.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let resourceArn = "resourceArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeProtectedResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeProtectedResourceOutput**](DescribeProtectedResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRecoveryPoint

> DescribeRecoveryPointOutput describeRecoveryPoint(backupVaultName, recoveryPointArn, opts)



Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let recoveryPointArn = "recoveryPointArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRecoveryPoint(backupVaultName, recoveryPointArn, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **recoveryPointArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRecoveryPointOutput**](DescribeRecoveryPointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRegionSettings

> DescribeRegionSettingsOutput describeRegionSettings(opts)



Returns the current service opt-in settings for the Region. If service opt-in is enabled for a service, Backup tries to protect that service&#39;s resources in this Region, when the resource is included in an on-demand backup or scheduled backup plan. Otherwise, Backup does not try to protect that service&#39;s resources in this Region.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRegionSettings(opts, (error, data, response) => {
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

[**DescribeRegionSettingsOutput**](DescribeRegionSettingsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeReportJob

> DescribeReportJobOutput describeReportJob(reportJobId, opts)



Returns the details associated with creating a report as specified by its &lt;code&gt;ReportJobId&lt;/code&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let reportJobId = "reportJobId_example"; // String | The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeReportJob(reportJobId, opts, (error, data, response) => {
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
 **reportJobId** | **String**| The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeReportJobOutput**](DescribeReportJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeReportPlan

> DescribeReportPlanOutput describeReportPlan(reportPlanName, opts)



Returns a list of all report plans for an Amazon Web Services account and Amazon Web Services Region.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let reportPlanName = "reportPlanName_example"; // String | The unique name of a report plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeReportPlan(reportPlanName, opts, (error, data, response) => {
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
 **reportPlanName** | **String**| The unique name of a report plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeReportPlanOutput**](DescribeReportPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRestoreJob

> DescribeRestoreJobOutput describeRestoreJob(restoreJobId, opts)



Returns metadata associated with a restore job that is specified by a job ID.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let restoreJobId = "restoreJobId_example"; // String | Uniquely identifies the job that restores a recovery point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRestoreJob(restoreJobId, opts, (error, data, response) => {
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
 **restoreJobId** | **String**| Uniquely identifies the job that restores a recovery point. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRestoreJobOutput**](DescribeRestoreJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateRecoveryPoint

> disassociateRecoveryPoint(backupVaultName, recoveryPointArn, opts)



&lt;p&gt;Deletes the specified continuous backup recovery point from Backup and releases control of that continuous backup to the source service, such as Amazon RDS. The source service will continue to create and retain continuous backups using the lifecycle that you specified in your original backup plan.&lt;/p&gt; &lt;p&gt;Does not support snapshot backup recovery points.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The unique name of an Backup vault.
let recoveryPointArn = "recoveryPointArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies an Backup recovery point.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateRecoveryPoint(backupVaultName, recoveryPointArn, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The unique name of an Backup vault. | 
 **recoveryPointArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies an Backup recovery point. | 
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


## disassociateRecoveryPointFromParent

> disassociateRecoveryPointFromParent(backupVaultName, recoveryPointArn, opts)



This action to a specific child (nested) recovery point removes the relationship between the specified recovery point and its parent (composite) recovery point.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | This is the name of a logical container where the child (nested) recovery point is stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let recoveryPointArn = "recoveryPointArn_example"; // String | This is the Amazon Resource Name (ARN) that uniquely identifies the child (nested) recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.</code> 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateRecoveryPointFromParent(backupVaultName, recoveryPointArn, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| This is the name of a logical container where the child (nested) recovery point is stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **recoveryPointArn** | **String**| This is the Amazon Resource Name (ARN) that uniquely identifies the child (nested) recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.&lt;/code&gt;  | 
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


## exportBackupPlanTemplate

> ExportBackupPlanTemplateOutput exportBackupPlanTemplate(backupPlanId, opts)



Returns the backup plan that is specified by the plan ID as a backup template.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.exportBackupPlanTemplate(backupPlanId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ExportBackupPlanTemplateOutput**](ExportBackupPlanTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupPlan

> GetBackupPlanOutput getBackupPlan(backupPlanId, opts)



Returns &lt;code&gt;BackupPlan&lt;/code&gt; details for the specified &lt;code&gt;BackupPlanId&lt;/code&gt;. The details are the body of a backup plan in JSON format, in addition to plan metadata.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'versionId': "versionId_example" // String | Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
};
apiInstance.getBackupPlan(backupPlanId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **versionId** | **String**| Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited. | [optional] 

### Return type

[**GetBackupPlanOutput**](GetBackupPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupPlanFromJSON

> GetBackupPlanFromJSONOutput getBackupPlanFromJSON(getBackupPlanFromJSONRequest, opts)



Returns a valid JSON document specifying a backup plan or an error.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let getBackupPlanFromJSONRequest = new AwsBackup.GetBackupPlanFromJSONRequest(); // GetBackupPlanFromJSONRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackupPlanFromJSON(getBackupPlanFromJSONRequest, opts, (error, data, response) => {
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
 **getBackupPlanFromJSONRequest** | [**GetBackupPlanFromJSONRequest**](GetBackupPlanFromJSONRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackupPlanFromJSONOutput**](GetBackupPlanFromJSONOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackupPlanFromTemplate

> GetBackupPlanFromTemplateOutput getBackupPlanFromTemplate(templateId, opts)



Returns the template specified by its &lt;code&gt;templateId&lt;/code&gt; as a backup plan.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let templateId = "templateId_example"; // String | Uniquely identifies a stored backup plan template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackupPlanFromTemplate(templateId, opts, (error, data, response) => {
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
 **templateId** | **String**| Uniquely identifies a stored backup plan template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackupPlanFromTemplateOutput**](GetBackupPlanFromTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupSelection

> GetBackupSelectionOutput getBackupSelection(backupPlanId, selectionId, opts)



Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let selectionId = "selectionId_example"; // String | Uniquely identifies the body of a request to assign a set of resources to a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackupSelection(backupPlanId, selectionId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **selectionId** | **String**| Uniquely identifies the body of a request to assign a set of resources to a backup plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackupSelectionOutput**](GetBackupSelectionOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupVaultAccessPolicy

> GetBackupVaultAccessPolicyOutput getBackupVaultAccessPolicy(backupVaultName, opts)



Returns the access policy document that is associated with the named backup vault.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackupVaultAccessPolicy(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackupVaultAccessPolicyOutput**](GetBackupVaultAccessPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupVaultNotifications

> GetBackupVaultNotificationsOutput getBackupVaultNotifications(backupVaultName, opts)



Returns event notifications for the specified backup vault.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBackupVaultNotifications(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBackupVaultNotificationsOutput**](GetBackupVaultNotificationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLegalHold

> GetLegalHoldOutput getLegalHold(legalHoldId, opts)



This action returns details for a specified legal hold. The details are the body of a legal hold in JSON format, in addition to metadata.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let legalHoldId = "legalHoldId_example"; // String | This is the ID required to use <code>GetLegalHold</code>. This unique ID is associated with a specific legal hold.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLegalHold(legalHoldId, opts, (error, data, response) => {
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
 **legalHoldId** | **String**| This is the ID required to use &lt;code&gt;GetLegalHold&lt;/code&gt;. This unique ID is associated with a specific legal hold. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLegalHoldOutput**](GetLegalHoldOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecoveryPointRestoreMetadata

> GetRecoveryPointRestoreMetadataOutput getRecoveryPointRestoreMetadata(backupVaultName, recoveryPointArn, opts)



Returns a set of metadata key-value pairs that were used to create the backup.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let recoveryPointArn = "recoveryPointArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRecoveryPointRestoreMetadata(backupVaultName, recoveryPointArn, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **recoveryPointArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRecoveryPointRestoreMetadataOutput**](GetRecoveryPointRestoreMetadataOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSupportedResourceTypes

> GetSupportedResourceTypesOutput getSupportedResourceTypes(opts)



Returns the Amazon Web Services resource types supported by Backup.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSupportedResourceTypes(opts, (error, data, response) => {
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

[**GetSupportedResourceTypesOutput**](GetSupportedResourceTypesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackupJobs

> ListBackupJobsOutput listBackupJobs(opts)



Returns a list of existing backup jobs for an authenticated account for the last 30 days. For a longer period of time, consider using these &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html\&quot;&gt;monitoring tools&lt;/a&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'resourceArn': "resourceArn_example", // String | Returns only backup jobs that match the specified resource Amazon Resource Name (ARN).
  'state': "state_example", // String | Returns only backup jobs that are in the specified state.
  'backupVaultName': "backupVaultName_example", // String | Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only backup jobs that were created before the specified date.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only backup jobs that were created after the specified date.
  'resourceType': "resourceType_example", // String | <p>Returns only backup jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>S3</code> for Amazon S3</p> </li> <li> <p> <code>VirtualMachine</code> for virtual machines</p> </li> </ul>
  'accountId': "accountId_example", // String | <p>The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.</p> <p>If used from an Organizations management account, passing <code>*</code> returns all jobs across the organization.</p>
  'completeAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only backup jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).
  'completeBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).
  'parentJobId': "parentJobId_example", // String | This is a filter to list child (nested) jobs based on parent job ID.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBackupJobs(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **resourceArn** | **String**| Returns only backup jobs that match the specified resource Amazon Resource Name (ARN). | [optional] 
 **state** | **String**| Returns only backup jobs that are in the specified state. | [optional] 
 **backupVaultName** | **String**| Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | [optional] 
 **createdBefore** | **Date**| Returns only backup jobs that were created before the specified date. | [optional] 
 **createdAfter** | **Date**| Returns only backup jobs that were created after the specified date. | [optional] 
 **resourceType** | **String**| &lt;p&gt;Returns only backup jobs for the specified resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Aurora&lt;/code&gt; for Amazon Aurora&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DocumentDB&lt;/code&gt; for Amazon DocumentDB (with MongoDB compatibility)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DynamoDB&lt;/code&gt; for Amazon DynamoDB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EBS&lt;/code&gt; for Amazon Elastic Block Store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EC2&lt;/code&gt; for Amazon Elastic Compute Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EFS&lt;/code&gt; for Amazon Elastic File System&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FSx&lt;/code&gt; for Amazon FSx&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Neptune&lt;/code&gt; for Amazon Neptune&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RDS&lt;/code&gt; for Amazon Relational Database Service&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Storage Gateway&lt;/code&gt; for Storage Gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;S3&lt;/code&gt; for Amazon S3&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;VirtualMachine&lt;/code&gt; for virtual machines&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **accountId** | **String**| &lt;p&gt;The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.&lt;/p&gt; &lt;p&gt;If used from an Organizations management account, passing &lt;code&gt;*&lt;/code&gt; returns all jobs across the organization.&lt;/p&gt; | [optional] 
 **completeAfter** | **Date**| Returns only backup jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC). | [optional] 
 **completeBefore** | **Date**| Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC). | [optional] 
 **parentJobId** | **String**| This is a filter to list child (nested) jobs based on parent job ID. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBackupJobsOutput**](ListBackupJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackupPlanTemplates

> ListBackupPlanTemplatesOutput listBackupPlanTemplates(opts)



Returns metadata of your saved backup plan templates, including the template ID, name, and the creation and deletion dates.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBackupPlanTemplates(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBackupPlanTemplatesOutput**](ListBackupPlanTemplatesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackupPlanVersions

> ListBackupPlanVersionsOutput listBackupPlanVersions(backupPlanId, opts)



Returns version metadata of your backup plans, including Amazon Resource Names (ARNs), backup plan IDs, creation and deletion dates, plan names, and version IDs.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBackupPlanVersions(backupPlanId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBackupPlanVersionsOutput**](ListBackupPlanVersionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackupPlans

> ListBackupPlansOutput listBackupPlans(opts)



Returns a list of all active backup plans for an authenticated account. The list contains information such as Amazon Resource Names (ARNs), plan IDs, creation and deletion dates, version IDs, plan names, and creator request IDs.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'includeDeleted': true, // Boolean | A Boolean value with a default value of <code>FALSE</code> that returns deleted backup plans when set to <code>TRUE</code>.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBackupPlans(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **includeDeleted** | **Boolean**| A Boolean value with a default value of &lt;code&gt;FALSE&lt;/code&gt; that returns deleted backup plans when set to &lt;code&gt;TRUE&lt;/code&gt;. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBackupPlansOutput**](ListBackupPlansOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackupSelections

> ListBackupSelectionsOutput listBackupSelections(backupPlanId, opts)



Returns an array containing metadata of the resources associated with the target backup plan.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBackupSelections(backupPlanId, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBackupSelectionsOutput**](ListBackupSelectionsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackupVaults

> ListBackupVaultsOutput listBackupVaults(opts)



Returns a list of recovery point storage containers along with information about them.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBackupVaults(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBackupVaultsOutput**](ListBackupVaultsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCopyJobs

> ListCopyJobsOutput listCopyJobs(opts)



Returns metadata about your copy jobs.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token. 
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'resourceArn': "resourceArn_example", // String | Returns only copy jobs that match the specified resource Amazon Resource Name (ARN). 
  'state': "state_example", // String | Returns only copy jobs that are in the specified state.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only copy jobs that were created before the specified date.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only copy jobs that were created after the specified date.
  'resourceType': "resourceType_example", // String | <p>Returns only backup jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>S3</code> for Amazon S3</p> </li> <li> <p> <code>VirtualMachine</code> for virtual machines</p> </li> </ul>
  'destinationVaultArn': "destinationVaultArn_example", // String | An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, <code>arn:aws:backup:us-east-1:123456789012:vault:aBackupVault</code>. 
  'accountId': "accountId_example", // String | The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID.
  'completeBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).
  'completeAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).
  'parentJobId': "parentJobId_example", // String | This is a filter to list child (nested) jobs based on parent job ID.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listCopyJobs(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.  | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **resourceArn** | **String**| Returns only copy jobs that match the specified resource Amazon Resource Name (ARN).  | [optional] 
 **state** | **String**| Returns only copy jobs that are in the specified state. | [optional] 
 **createdBefore** | **Date**| Returns only copy jobs that were created before the specified date. | [optional] 
 **createdAfter** | **Date**| Returns only copy jobs that were created after the specified date. | [optional] 
 **resourceType** | **String**| &lt;p&gt;Returns only backup jobs for the specified resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Aurora&lt;/code&gt; for Amazon Aurora&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DocumentDB&lt;/code&gt; for Amazon DocumentDB (with MongoDB compatibility)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DynamoDB&lt;/code&gt; for Amazon DynamoDB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EBS&lt;/code&gt; for Amazon Elastic Block Store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EC2&lt;/code&gt; for Amazon Elastic Compute Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EFS&lt;/code&gt; for Amazon Elastic File System&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FSx&lt;/code&gt; for Amazon FSx&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Neptune&lt;/code&gt; for Amazon Neptune&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RDS&lt;/code&gt; for Amazon Relational Database Service&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Storage Gateway&lt;/code&gt; for Storage Gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;S3&lt;/code&gt; for Amazon S3&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;VirtualMachine&lt;/code&gt; for virtual machines&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
 **destinationVaultArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:vault:aBackupVault&lt;/code&gt;.  | [optional] 
 **accountId** | **String**| The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID. | [optional] 
 **completeBefore** | **Date**| Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC). | [optional] 
 **completeAfter** | **Date**| Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC). | [optional] 
 **parentJobId** | **String**| This is a filter to list child (nested) jobs based on parent job ID. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListCopyJobsOutput**](ListCopyJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFrameworks

> ListFrameworksOutput listFrameworks(opts)



Returns a list of all frameworks for an Amazon Web Services account and Amazon Web Services Region.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
  'nextToken': "nextToken_example" // String | An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
};
apiInstance.listFrameworks(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data. | [optional] 
 **nextToken** | **String**| An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. | [optional] 

### Return type

[**ListFrameworksOutput**](ListFrameworksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLegalHolds

> ListLegalHoldsOutput listLegalHolds(opts)



This action returns metadata about active and previous legal holds.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of resource list items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listLegalHolds(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned resources. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of resources, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of resource list items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListLegalHoldsOutput**](ListLegalHoldsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProtectedResources

> ListProtectedResourcesOutput listProtectedResources(opts)



Returns an array of resources successfully backed up by Backup, including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listProtectedResources(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListProtectedResourcesOutput**](ListProtectedResourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecoveryPointsByBackupVault

> ListRecoveryPointsByBackupVaultOutput listRecoveryPointsByBackupVault(backupVaultName, opts)



Returns detailed information about the recovery points stored in a backup vault.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.</p> <note> <p>Backup vault name might not be available when a supported service creates the backup.</p> </note>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'resourceArn': "resourceArn_example", // String | Returns only recovery points that match the specified resource Amazon Resource Name (ARN).
  'resourceType': "resourceType_example", // String | Returns only recovery points that match the specified resource type.
  'backupPlanId': "backupPlanId_example", // String | Returns only recovery points that match the specified backup plan ID.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only recovery points that were created before the specified timestamp.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only recovery points that were created after the specified timestamp.
  'parentRecoveryPointArn': "parentRecoveryPointArn_example", // String | This returns only recovery points that match the specified parent (composite) recovery point Amazon Resource Name (ARN).
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRecoveryPointsByBackupVault(backupVaultName, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| &lt;p&gt;The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Backup vault name might not be available when a supported service creates the backup.&lt;/p&gt; &lt;/note&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **resourceArn** | **String**| Returns only recovery points that match the specified resource Amazon Resource Name (ARN). | [optional] 
 **resourceType** | **String**| Returns only recovery points that match the specified resource type. | [optional] 
 **backupPlanId** | **String**| Returns only recovery points that match the specified backup plan ID. | [optional] 
 **createdBefore** | **Date**| Returns only recovery points that were created before the specified timestamp. | [optional] 
 **createdAfter** | **Date**| Returns only recovery points that were created after the specified timestamp. | [optional] 
 **parentRecoveryPointArn** | **String**| This returns only recovery points that match the specified parent (composite) recovery point Amazon Resource Name (ARN). | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRecoveryPointsByBackupVaultOutput**](ListRecoveryPointsByBackupVaultOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecoveryPointsByLegalHold

> ListRecoveryPointsByLegalHoldOutput listRecoveryPointsByLegalHold(legalHoldId, opts)



This action returns recovery point ARNs (Amazon Resource Names) of the specified legal hold.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let legalHoldId = "legalHoldId_example"; // String | This is the ID of the legal hold.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | This is the next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | This is the maximum number of resource list items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRecoveryPointsByLegalHold(legalHoldId, opts, (error, data, response) => {
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
 **legalHoldId** | **String**| This is the ID of the legal hold. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| This is the next item following a partial list of returned resources. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of resources, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| This is the maximum number of resource list items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRecoveryPointsByLegalHoldOutput**](ListRecoveryPointsByLegalHoldOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecoveryPointsByResource

> ListRecoveryPointsByResourceOutput listRecoveryPointsByResource(resourceArn, opts)



&lt;p&gt;Returns detailed information about all the recovery points of the type specified by a resource Amazon Resource Name (ARN).&lt;/p&gt; &lt;note&gt; &lt;p&gt;For Amazon EFS and Amazon EC2, this action only lists recovery points created by Backup.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let resourceArn = "resourceArn_example"; // String | An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | <p>The maximum number of items to be returned.</p> <note> <p>Amazon RDS requires a value of at least 20.</p> </note>
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRecoveryPointsByResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of items to be returned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon RDS requires a value of at least 20.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRecoveryPointsByResourceOutput**](ListRecoveryPointsByResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listReportJobs

> ListReportJobsOutput listReportJobs(opts)



Returns details about your report jobs.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'reportPlanName': "reportPlanName_example", // String | Returns only report jobs with the specified report plan name.
  'creationBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only report jobs that were created before the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.
  'creationAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only report jobs that were created after the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.
  'status': "status_example", // String | <p>Returns only report jobs that are in the specified status. The statuses are:</p> <p> <code>CREATED | RUNNING | COMPLETED | FAILED</code> </p>
  'maxResults': 56, // Number | The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
  'nextToken': "nextToken_example" // String | An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
};
apiInstance.listReportJobs(opts, (error, data, response) => {
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
 **reportPlanName** | **String**| Returns only report jobs with the specified report plan name. | [optional] 
 **creationBefore** | **Date**| Returns only report jobs that were created before the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM. | [optional] 
 **creationAfter** | **Date**| Returns only report jobs that were created after the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM. | [optional] 
 **status** | **String**| &lt;p&gt;Returns only report jobs that are in the specified status. The statuses are:&lt;/p&gt; &lt;p&gt; &lt;code&gt;CREATED | RUNNING | COMPLETED | FAILED&lt;/code&gt; &lt;/p&gt; | [optional] 
 **maxResults** | **Number**| The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data. | [optional] 
 **nextToken** | **String**| An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. | [optional] 

### Return type

[**ListReportJobsOutput**](ListReportJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listReportPlans

> ListReportPlansOutput listReportPlans(opts)



Returns a list of your report plans. For detailed information about a single report plan, use &lt;code&gt;DescribeReportPlan&lt;/code&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
  'nextToken': "nextToken_example" // String | An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
};
apiInstance.listReportPlans(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data. | [optional] 
 **nextToken** | **String**| An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list. | [optional] 

### Return type

[**ListReportPlansOutput**](ListReportPlansOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRestoreJobs

> ListRestoreJobsOutput listRestoreJobs(opts)



Returns a list of jobs that Backup initiated to restore a saved resource, including details about the recovery process.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'accountId': "accountId_example", // String | The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only restore jobs that were created before the specified date.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only restore jobs that were created after the specified date.
  'status': "status_example", // String | Returns only restore jobs associated with the specified job status.
  'completeBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).
  'completeAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRestoreJobs(opts, (error, data, response) => {
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
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **accountId** | **String**| The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID. | [optional] 
 **createdBefore** | **Date**| Returns only restore jobs that were created before the specified date. | [optional] 
 **createdAfter** | **Date**| Returns only restore jobs that were created after the specified date. | [optional] 
 **status** | **String**| Returns only restore jobs associated with the specified job status. | [optional] 
 **completeBefore** | **Date**| Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC). | [optional] 
 **completeAfter** | **Date**| Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC). | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRestoreJobsOutput**](ListRestoreJobsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTags

> ListTagsOutput listTags(resourceArn, opts)



&lt;p&gt;Returns a list of key-value pairs assigned to a target recovery point, backup plan, or backup vault.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListTags&lt;/code&gt; only works for resource types that support full Backup management of their backups. Those resource types are listed in the \&quot;Full Backup management\&quot; section of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource\&quot;&gt; Feature availability by resource&lt;/a&gt; table.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let resourceArn = "resourceArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the type of resource. Valid targets for <code>ListTags</code> are recovery points, backup plans, and backup vaults.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The next item following a partial list of returned items. For example, if a request is made to return <code>maxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.
  'maxResults': 56, // Number | The maximum number of items to be returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listTags(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the type of resource. Valid targets for &lt;code&gt;ListTags&lt;/code&gt; are recovery points, backup plans, and backup vaults. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token. | [optional] 
 **maxResults** | **Number**| The maximum number of items to be returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListTagsOutput**](ListTagsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putBackupVaultAccessPolicy

> putBackupVaultAccessPolicy(backupVaultName, putBackupVaultAccessPolicyRequest, opts)



Sets a resource-based policy that is used to manage access permissions on the target backup vault. Requires a backup vault name and an access policy document in JSON format.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let putBackupVaultAccessPolicyRequest = new AwsBackup.PutBackupVaultAccessPolicyRequest(); // PutBackupVaultAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBackupVaultAccessPolicy(backupVaultName, putBackupVaultAccessPolicyRequest, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **putBackupVaultAccessPolicyRequest** | [**PutBackupVaultAccessPolicyRequest**](PutBackupVaultAccessPolicyRequest.md)|  | 
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


## putBackupVaultLockConfiguration

> putBackupVaultLockConfiguration(backupVaultName, putBackupVaultLockConfigurationRequest, opts)



&lt;p&gt;Applies Backup Vault Lock to a backup vault, preventing attempts to delete any recovery point stored in or created in a backup vault. Vault Lock also prevents attempts to update the lifecycle policy that controls the retention period of any recovery point currently stored in a backup vault. If specified, Vault Lock enforces a minimum and maximum retention period for future backup and copy jobs that target a backup vault.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Backup Vault Lock has been assessed by Cohasset Associates for use in environments that are subject to SEC 17a-4, CFTC, and FINRA regulations. For more information about how Backup Vault Lock relates to these regulations, see the &lt;a href&#x3D;\&quot;samples/cohassetreport.zip\&quot;&gt;Cohasset Associates Compliance Assessment.&lt;/a&gt; &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The Backup Vault Lock configuration that specifies the name of the backup vault it protects.
let putBackupVaultLockConfigurationRequest = new AwsBackup.PutBackupVaultLockConfigurationRequest(); // PutBackupVaultLockConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBackupVaultLockConfiguration(backupVaultName, putBackupVaultLockConfigurationRequest, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The Backup Vault Lock configuration that specifies the name of the backup vault it protects. | 
 **putBackupVaultLockConfigurationRequest** | [**PutBackupVaultLockConfigurationRequest**](PutBackupVaultLockConfigurationRequest.md)|  | 
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


## putBackupVaultNotifications

> putBackupVaultNotifications(backupVaultName, putBackupVaultNotificationsRequest, opts)



Turns on notifications on a backup vault for the specified topic and events.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let putBackupVaultNotificationsRequest = new AwsBackup.PutBackupVaultNotificationsRequest(); // PutBackupVaultNotificationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBackupVaultNotifications(backupVaultName, putBackupVaultNotificationsRequest, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **putBackupVaultNotificationsRequest** | [**PutBackupVaultNotificationsRequest**](PutBackupVaultNotificationsRequest.md)|  | 
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


## startBackupJob

> StartBackupJobOutput startBackupJob(startBackupJobRequest, opts)



Starts an on-demand backup job for the specified resource.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let startBackupJobRequest = new AwsBackup.StartBackupJobRequest(); // StartBackupJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startBackupJob(startBackupJobRequest, opts, (error, data, response) => {
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
 **startBackupJobRequest** | [**StartBackupJobRequest**](StartBackupJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartBackupJobOutput**](StartBackupJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startCopyJob

> StartCopyJobOutput startCopyJob(startCopyJobRequest, opts)



&lt;p&gt;Starts a job to create a one-time copy of the specified resource.&lt;/p&gt; &lt;p&gt;Does not support continuous backups.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let startCopyJobRequest = new AwsBackup.StartCopyJobRequest(); // StartCopyJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startCopyJob(startCopyJobRequest, opts, (error, data, response) => {
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
 **startCopyJobRequest** | [**StartCopyJobRequest**](StartCopyJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartCopyJobOutput**](StartCopyJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startReportJob

> StartReportJobOutput startReportJob(reportPlanName, startReportJobRequest, opts)



Starts an on-demand report job for the specified report plan.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let reportPlanName = "reportPlanName_example"; // String | The unique name of a report plan.
let startReportJobRequest = new AwsBackup.StartReportJobRequest(); // StartReportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startReportJob(reportPlanName, startReportJobRequest, opts, (error, data, response) => {
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
 **reportPlanName** | **String**| The unique name of a report plan. | 
 **startReportJobRequest** | [**StartReportJobRequest**](StartReportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartReportJobOutput**](StartReportJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startRestoreJob

> StartRestoreJobOutput startRestoreJob(startRestoreJobRequest, opts)



Recovers the saved resource identified by an Amazon Resource Name (ARN).

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let startRestoreJobRequest = new AwsBackup.StartRestoreJobRequest(); // StartRestoreJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startRestoreJob(startRestoreJobRequest, opts, (error, data, response) => {
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
 **startRestoreJobRequest** | [**StartRestoreJobRequest**](StartRestoreJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartRestoreJobOutput**](StartRestoreJobOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopBackupJob

> stopBackupJob(backupJobId, opts)



&lt;p&gt;Attempts to cancel a job to create a one-time backup of a resource.&lt;/p&gt; &lt;p&gt;This action is not supported for the following services: Amazon FSx for Windows File Server, Amazon FSx for Lustre, FSx for ONTAP , Amazon FSx for OpenZFS, Amazon DocumentDB (with MongoDB compatibility), Amazon RDS, Amazon Aurora, and Amazon Neptune.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupJobId = "backupJobId_example"; // String | Uniquely identifies a request to Backup to back up a resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopBackupJob(backupJobId, opts, (error, data, response) => {
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
 **backupJobId** | **String**| Uniquely identifies a request to Backup to back up a resource. | 
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


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



Assigns a set of key-value pairs to a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN).

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let resourceArn = "resourceArn_example"; // String | An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
let tagResourceRequest = new AwsBackup.TagResourceRequest(); // TagResourceRequest | 
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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


## untagResource

> untagResource(resourceArn, untagResourceRequest, opts)



Removes a set of key-value pairs from a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN)

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let resourceArn = "resourceArn_example"; // String | An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
let untagResourceRequest = new AwsBackup.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, untagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource. | 
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
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


## updateBackupPlan

> UpdateBackupPlanOutput updateBackupPlan(backupPlanId, updateBackupPlanRequest, opts)



Updates an existing backup plan identified by its &lt;code&gt;backupPlanId&lt;/code&gt; with the input document in JSON format. The new version is uniquely identified by a &lt;code&gt;VersionId&lt;/code&gt;.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupPlanId = "backupPlanId_example"; // String | Uniquely identifies a backup plan.
let updateBackupPlanRequest = new AwsBackup.UpdateBackupPlanRequest(); // UpdateBackupPlanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBackupPlan(backupPlanId, updateBackupPlanRequest, opts, (error, data, response) => {
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
 **backupPlanId** | **String**| Uniquely identifies a backup plan. | 
 **updateBackupPlanRequest** | [**UpdateBackupPlanRequest**](UpdateBackupPlanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBackupPlanOutput**](UpdateBackupPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFramework

> UpdateFrameworkOutput updateFramework(frameworkName, updateFrameworkRequest, opts)



Updates an existing framework identified by its &lt;code&gt;FrameworkName&lt;/code&gt; with the input document in JSON format.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let frameworkName = "frameworkName_example"; // String | The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
let updateFrameworkRequest = new AwsBackup.UpdateFrameworkRequest(); // UpdateFrameworkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateFramework(frameworkName, updateFrameworkRequest, opts, (error, data, response) => {
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
 **frameworkName** | **String**| The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_). | 
 **updateFrameworkRequest** | [**UpdateFrameworkRequest**](UpdateFrameworkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateFrameworkOutput**](UpdateFrameworkOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGlobalSettings

> updateGlobalSettings(updateGlobalSettingsRequest, opts)



Updates whether the Amazon Web Services account is opted in to cross-account backup. Returns an error if the account is not an Organizations management account. Use the &lt;code&gt;DescribeGlobalSettings&lt;/code&gt; API to determine the current settings.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let updateGlobalSettingsRequest = new AwsBackup.UpdateGlobalSettingsRequest(); // UpdateGlobalSettingsRequest | 
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


## updateRecoveryPointLifecycle

> UpdateRecoveryPointLifecycleOutput updateRecoveryPointLifecycle(backupVaultName, recoveryPointArn, updateRecoveryPointLifecycleRequest, opts)



&lt;p&gt;Sets the transition lifecycle of a recovery point.&lt;/p&gt; &lt;p&gt;The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.&lt;/p&gt; &lt;p&gt;Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.&lt;/p&gt; &lt;p&gt;Resource types that are able to be transitioned to cold storage are listed in the \&quot;Lifecycle to cold storage\&quot; section of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource\&quot;&gt; Feature availability by resource&lt;/a&gt; table. Backup ignores this expression for other resource types.&lt;/p&gt; &lt;p&gt;This operation does not support continuous backups.&lt;/p&gt;

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let backupVaultName = "backupVaultName_example"; // String | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
let recoveryPointArn = "recoveryPointArn_example"; // String | An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.
let updateRecoveryPointLifecycleRequest = new AwsBackup.UpdateRecoveryPointLifecycleRequest(); // UpdateRecoveryPointLifecycleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRecoveryPointLifecycle(backupVaultName, recoveryPointArn, updateRecoveryPointLifecycleRequest, opts, (error, data, response) => {
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
 **backupVaultName** | **String**| The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
 **recoveryPointArn** | **String**| An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;. | 
 **updateRecoveryPointLifecycleRequest** | [**UpdateRecoveryPointLifecycleRequest**](UpdateRecoveryPointLifecycleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRecoveryPointLifecycleOutput**](UpdateRecoveryPointLifecycleOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRegionSettings

> updateRegionSettings(updateRegionSettingsRequest, opts)



Updates the current service opt-in settings for the Region. If service-opt-in is enabled for a service, Backup tries to protect that service&#39;s resources in this Region, when the resource is included in an on-demand backup or scheduled backup plan. Otherwise, Backup does not try to protect that service&#39;s resources in this Region. Use the &lt;code&gt;DescribeRegionSettings&lt;/code&gt; API to determine the resource types that are supported.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let updateRegionSettingsRequest = new AwsBackup.UpdateRegionSettingsRequest(); // UpdateRegionSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRegionSettings(updateRegionSettingsRequest, opts, (error, data, response) => {
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
 **updateRegionSettingsRequest** | [**UpdateRegionSettingsRequest**](UpdateRegionSettingsRequest.md)|  | 
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


## updateReportPlan

> UpdateReportPlanOutput updateReportPlan(reportPlanName, updateReportPlanRequest, opts)



Updates an existing report plan identified by its &lt;code&gt;ReportPlanName&lt;/code&gt; with the input document in JSON format.

### Example

```javascript
import AwsBackup from 'aws_backup';
let defaultClient = AwsBackup.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsBackup.DefaultApi();
let reportPlanName = "reportPlanName_example"; // String | The unique name of the report plan. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
let updateReportPlanRequest = new AwsBackup.UpdateReportPlanRequest(); // UpdateReportPlanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateReportPlan(reportPlanName, updateReportPlanRequest, opts, (error, data, response) => {
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
 **reportPlanName** | **String**| The unique name of the report plan. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_). | 
 **updateReportPlanRequest** | [**UpdateReportPlanRequest**](UpdateReportPlanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateReportPlanOutput**](UpdateReportPlanOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

