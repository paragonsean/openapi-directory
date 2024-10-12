

# ConnectorProperties

The properties of a Connector

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingModel** | [**BillingModelEnum**](#BillingModelEnum) | Connector billing model |  [optional] |
|**collectionInfo** | [**ConnectorCollectionInfo**](ConnectorCollectionInfo.md) |  |  [optional] |
|**createdOn** | **OffsetDateTime** | Connector definition creation datetime |  [optional] [readonly] |
|**credentialsKey** | **String** | Credentials authentication key (eg AWS ARN) |  [optional] |
|**credentialsSecret** | **String** | Credentials secret (eg AWS ExternalId) |  [optional] |
|**daysTrialRemaining** | **Integer** | Number of days remaining of trial |  [optional] [readonly] |
|**defaultManagementGroupId** | **String** | Default ManagementGroupId |  [optional] |
|**displayName** | **String** | Connector DisplayName |  [optional] |
|**externalBillingAccountId** | **String** | Associated ExternalBillingAccountId |  [optional] [readonly] |
|**modifiedOn** | **OffsetDateTime** | Connector last modified datetime |  [optional] [readonly] |
|**providerBillingAccountDisplayName** | **String** | The display name of the providerBillingAccountId as defined on the external provider |  [optional] [readonly] |
|**providerBillingAccountId** | **String** | Connector providerBillingAccountId, determined from credentials (eg AWS Consolidated account number) |  [optional] [readonly] |
|**reportId** | **String** | Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Connector status |  [optional] [readonly] |
|**subscriptionId** | **String** | Billing SubscriptionId |  [optional] |



## Enum: BillingModelEnum

| Name | Value |
|---- | -----|
| TRIAL | &quot;trial&quot; |
| AUTO_UPGRADE | &quot;autoUpgrade&quot; |
| PREMIUM | &quot;premium&quot; |
| EXPIRED | &quot;expired&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ERROR | &quot;error&quot; |
| EXPIRED | &quot;expired&quot; |
| WARNING | &quot;warning&quot; |



