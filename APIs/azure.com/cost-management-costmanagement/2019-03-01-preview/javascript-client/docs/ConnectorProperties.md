# CostManagementClient.ConnectorProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingModel** | **String** | Connector billing model | [optional] 
**collectionInfo** | [**ConnectorCollectionInfo**](ConnectorCollectionInfo.md) |  | [optional] 
**createdOn** | **Date** | Connector definition creation datetime | [optional] [readonly] 
**credentialsKey** | **String** | Credentials authentication key (eg AWS ARN) | [optional] 
**credentialsSecret** | **String** | Credentials secret (eg AWS ExternalId) | [optional] 
**daysTrialRemaining** | **Number** | Number of days remaining of trial | [optional] [readonly] 
**defaultManagementGroupId** | **String** | Default ManagementGroupId | [optional] 
**displayName** | **String** | Connector DisplayName | [optional] 
**externalBillingAccountId** | **String** | Associated ExternalBillingAccountId | [optional] [readonly] 
**modifiedOn** | **Date** | Connector last modified datetime | [optional] [readonly] 
**providerBillingAccountDisplayName** | **String** | The display name of the providerBillingAccountId as defined on the external provider | [optional] [readonly] 
**providerBillingAccountId** | **String** | Connector providerBillingAccountId, determined from credentials (eg AWS Consolidated account number) | [optional] [readonly] 
**reportId** | **String** | Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources) | [optional] 
**status** | **String** | Connector status | [optional] [readonly] 
**subscriptionId** | **String** | Billing SubscriptionId | [optional] 



## Enum: BillingModelEnum


* `trial` (value: `"trial"`)

* `autoUpgrade` (value: `"autoUpgrade"`)

* `premium` (value: `"premium"`)

* `expired` (value: `"expired"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `error` (value: `"error"`)

* `expired` (value: `"expired"`)

* `warning` (value: `"warning"`)




