# CloudLoggingApi.UpdateBucketRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | [**LogBucket**](LogBucket.md) |  | [optional] 
**name** | **String** | Required. The full resource name of the bucket to update. \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; \&quot;organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; \&quot;billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; \&quot;folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; For example:\&quot;projects/my-project/locations/global/buckets/my-bucket\&quot; | [optional] 
**updateMask** | **String** | Required. Field mask that specifies the fields in bucket that need an update. A bucket field will be overwritten if, and only if, it is in the update mask. name and output only fields cannot be updated.For a detailed FieldMask definition, see: https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMaskFor example: updateMask&#x3D;retention_days | [optional] 


