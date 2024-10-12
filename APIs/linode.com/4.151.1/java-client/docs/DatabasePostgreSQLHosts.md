

# DatabasePostgreSQLHosts

The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primary** | **String** | The primary host for the Managed Database. |  [optional] |
|**secondary** | **String** | The secondary/private network host for the Managed Database.  A private network host and a private IP can only be used to access a Database Cluster from Linodes in the same data center and will not incur transfer costs.  **Note**: The secondary hostname is publicly viewable and accessible.  |  [optional] |



