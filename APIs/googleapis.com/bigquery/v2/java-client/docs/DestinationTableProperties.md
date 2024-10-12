

# DestinationTableProperties

Properties for the destination table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. The description for the destination table. This will only be used if the destination table is newly created. If the table already exists and a value different than the current description is provided, the job will fail. |  [optional] |
|**expirationTime** | **OffsetDateTime** | Internal use only. |  [optional] |
|**friendlyName** | **String** | Optional. Friendly name for the destination table. If the table already exists, it should be same as the existing friendly name. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels associated with this table. You can use these to organize and group your tables. This will only be used if the destination table is newly created. If the table already exists and labels are different than the current labels are provided, the job will fail. |  [optional] |



