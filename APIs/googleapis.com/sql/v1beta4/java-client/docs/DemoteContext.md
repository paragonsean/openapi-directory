

# DemoteContext

This context is used to demote an existing standalone instance to be a Cloud SQL read replica for an external database server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | This is always &#x60;sql#demoteContext&#x60;. |  [optional] |
|**sourceRepresentativeInstanceName** | **String** | Required. The name of the instance which acts as an on-premises primary instance in the replication setup. |  [optional] |



