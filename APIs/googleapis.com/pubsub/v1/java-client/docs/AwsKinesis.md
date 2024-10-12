

# AwsKinesis

Ingestion settings for Amazon Kinesis Data Streams.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**awsRoleArn** | **String** | Required. AWS role ARN to be used for Federated Identity authentication with Kinesis. Check the Pub/Sub docs for how to set up this role and the required permissions that need to be attached to it. |  [optional] |
|**consumerArn** | **String** | Required. The Kinesis consumer ARN to used for ingestion in Enhanced Fan-Out mode. The consumer must be already created and ready to be used. |  [optional] |
|**gcpServiceAccount** | **String** | Required. The GCP service account to be used for Federated Identity authentication with Kinesis (via a &#x60;AssumeRoleWithWebIdentity&#x60; call for the provided role). The &#x60;aws_role_arn&#x60; must be set up with &#x60;accounts.google.com:sub&#x60; equals to this service account number. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. An output-only field that indicates the state of the Kinesis ingestion source. |  [optional] [readonly] |
|**streamArn** | **String** | Required. The Kinesis stream ARN to ingest data from. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| KINESIS_PERMISSION_DENIED | &quot;KINESIS_PERMISSION_DENIED&quot; |
| PUBLISH_PERMISSION_DENIED | &quot;PUBLISH_PERMISSION_DENIED&quot; |
| STREAM_NOT_FOUND | &quot;STREAM_NOT_FOUND&quot; |
| CONSUMER_NOT_FOUND | &quot;CONSUMER_NOT_FOUND&quot; |



