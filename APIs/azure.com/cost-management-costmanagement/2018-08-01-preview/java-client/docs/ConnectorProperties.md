

# ConnectorProperties

The properties of a Connector

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collection** | [**ConnectorCollectionInfo**](ConnectorCollectionInfo.md) |  |  [optional] |
|**createdOn** | **OffsetDateTime** | Connector definition creation datetime |  [optional] [readonly] |
|**credentialsKey** | **String** | Credentials authentication key (eg AWS ARN) |  [optional] |
|**credentialsSecret** | **String** | Credentials secret (eg AWS ExternalId) |  [optional] |
|**displayName** | **String** | Connector DisplayName (defaults to Name) |  [optional] |
|**modifiedOn** | **OffsetDateTime** | Connector last modified datetime |  [optional] [readonly] |
|**providerAccountId** | **String** | Connector providerAccountId (determined from credentials) |  [optional] [readonly] |
|**reportId** | **String** | Identifying source report. (For AWS this is a CUR report name, defined with Daily and with Resources) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Connector status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ERROR | &quot;error&quot; |
| SUSPENDED | &quot;suspended&quot; |



