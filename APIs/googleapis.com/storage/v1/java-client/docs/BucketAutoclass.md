

# BucketAutoclass

The bucket's Autoclass configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether or not Autoclass is enabled on this bucket |  [optional] |
|**terminalStorageClass** | **String** | The storage class that objects in the bucket eventually transition to if they are not read for a certain length of time. Valid values are NEARLINE and ARCHIVE. |  [optional] |
|**terminalStorageClassUpdateTime** | **OffsetDateTime** | A date and time in RFC 3339 format representing the time of the most recent update to \&quot;terminalStorageClass\&quot;. |  [optional] |
|**toggleTime** | **OffsetDateTime** | A date and time in RFC 3339 format representing the instant at which \&quot;enabled\&quot; was last toggled. |  [optional] |



