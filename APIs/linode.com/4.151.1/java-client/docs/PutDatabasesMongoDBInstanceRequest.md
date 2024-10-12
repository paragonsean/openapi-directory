

# PutDatabasesMongoDBInstanceRequest

Updated information for the Managed MongoDB Database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowList** | **List&lt;String&gt;** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  |  [optional] |
|**label** | **String** | A unique, user-defined string referring to the Managed Database. |  [optional] |
|**updates** | [**DatabaseUpdates**](DatabaseUpdates.md) |  |  [optional] |



