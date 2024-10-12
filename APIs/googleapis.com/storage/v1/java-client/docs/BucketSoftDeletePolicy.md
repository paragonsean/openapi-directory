

# BucketSoftDeletePolicy

The bucket's soft delete policy, which defines the period of time that soft-deleted objects will be retained, and cannot be permanently deleted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effectiveTime** | **OffsetDateTime** | Server-determined value that indicates the time from which the policy, or one with a greater retention, was effective. This value is in RFC 3339 format. |  [optional] |
|**retentionDurationSeconds** | **String** | The duration in seconds that soft-deleted objects in the bucket will be retained and cannot be permanently deleted. |  [optional] |



