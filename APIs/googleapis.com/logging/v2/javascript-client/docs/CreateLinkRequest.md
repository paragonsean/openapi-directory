# CloudLoggingApi.CreateLinkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**Link**](Link.md) |  | [optional] 
**linkId** | **String** | Required. The ID to use for the link. The link_id can have up to 100 characters. A valid link_id must only have alphanumeric characters and underscores within it. | [optional] 
**parent** | **String** | Required. The full resource name of the bucket to create a link for. \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; \&quot;organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; \&quot;billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot; \&quot;folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]\&quot;  | [optional] 


