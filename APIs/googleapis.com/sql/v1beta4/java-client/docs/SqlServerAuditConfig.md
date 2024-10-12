

# SqlServerAuditConfig

SQL Server specific audit configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | **String** | The name of the destination bucket (e.g., gs://mybucket). |  [optional] |
|**kind** | **String** | This is always sql#sqlServerAuditConfig |  [optional] |
|**retentionInterval** | **String** | How long to keep generated audit files. |  [optional] |
|**uploadInterval** | **String** | How often to upload generated audit files. |  [optional] |



