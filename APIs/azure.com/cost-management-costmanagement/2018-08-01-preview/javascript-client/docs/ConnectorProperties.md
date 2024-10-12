# CostManagementClient.ConnectorProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**ConnectorCollectionInfo**](ConnectorCollectionInfo.md) |  | [optional] 
**createdOn** | **Date** | Connector definition creation datetime | [optional] [readonly] 
**credentialsKey** | **String** | Credentials authentication key (eg AWS ARN) | [optional] 
**credentialsSecret** | **String** | Credentials secret (eg AWS ExternalId) | [optional] 
**displayName** | **String** | Connector DisplayName (defaults to Name) | [optional] 
**modifiedOn** | **Date** | Connector last modified datetime | [optional] [readonly] 
**providerAccountId** | **String** | Connector providerAccountId (determined from credentials) | [optional] [readonly] 
**reportId** | **String** | Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources) | [optional] 
**status** | **String** | Connector status | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `error` (value: `"error"`)

* `suspended` (value: `"suspended"`)




