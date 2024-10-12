

# BucketIamConfigurationUniformBucketLevelAccess

The bucket's uniform bucket-level access configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | If set, access is controlled only by bucket-level or above IAM policies. |  [optional] |
|**lockedTime** | **OffsetDateTime** | The deadline for changing iamConfiguration.uniformBucketLevelAccess.enabled from true to false in RFC 3339  format. iamConfiguration.uniformBucketLevelAccess.enabled may be changed from true to false until the locked time, after which the field is immutable. |  [optional] |



