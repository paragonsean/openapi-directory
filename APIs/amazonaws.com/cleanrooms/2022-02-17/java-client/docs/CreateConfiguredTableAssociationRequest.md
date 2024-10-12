

# CreateConfiguredTableAssociationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the configured table association. This name is used to query the underlying configured table. |  |
|**description** | **String** | A description for the configured table association. |  [optional] |
|**configuredTableIdentifier** | **String** | A unique identifier for the configured table to be associated to. Currently accepts a configured table ID. |  |
|**roleArn** | **String** | The service will assume this role to access catalog metadata and query the table. |  |
|**tags** | **Map&lt;String, String&gt;** | Map of tags assigned to a resource |  [optional] |



