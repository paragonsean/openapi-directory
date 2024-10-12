# CloudStorageJsonApi.BucketRetentionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveTime** | **Date** | Server-determined value that indicates the time from which policy was enforced and effective. This value is in RFC 3339 format. | [optional] 
**isLocked** | **Boolean** | Once locked, an object retention policy cannot be modified. | [optional] 
**retentionPeriod** | **String** | The duration in seconds that objects need to be retained. Retention duration must be greater than zero and less than 100 years. Note that enforcement of retention periods less than a day is not guaranteed. Such periods should only be used for testing purposes. | [optional] 


