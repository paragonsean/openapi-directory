

# CloneContext

Database instance clone context.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocatedIpRange** | **String** | The name of the allocated ip range for the private ip Cloud SQL instance. For example: \&quot;google-managed-services-default\&quot;. If set, the cloned instance ip will be created in the allocated range. The range name must comply with [RFC 1035](https://tools.ietf.org/html/rfc1035). Specifically, the name must be 1-63 characters long and match the regular expression [a-z]([-a-z0-9]*[a-z0-9])?. Reserved for future use. |  [optional] |
|**binLogCoordinates** | [**BinLogCoordinates**](BinLogCoordinates.md) |  |  [optional] |
|**databaseNames** | **List&lt;String&gt;** | (SQL Server only) Clone only the specified databases from the source instance. Clone all databases if empty. |  [optional] |
|**destinationInstanceName** | **String** | Name of the Cloud SQL instance to be created as a clone. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#cloneContext&#x60;. |  [optional] |
|**pitrTimestampMs** | **String** | Reserved for future use. |  [optional] |
|**pointInTime** | **String** | Timestamp, if specified, identifies the time to which the source instance is cloned. |  [optional] |
|**preferredZone** | **String** | Optional. (Point-in-time recovery for PostgreSQL only) Clone to an instance in the specified zone. If no zone is specified, clone to the same zone as the source instance. |  [optional] |



