

# CreateAccessLogSubscriptionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. |  [optional] |
|**destinationArn** | **String** | The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets. |  |
|**resourceIdentifier** | **String** | The ID or Amazon Resource Name (ARN) of the service network or service. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags for the access log subscription. |  [optional] |



