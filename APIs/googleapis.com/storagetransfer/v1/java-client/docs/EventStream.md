

# EventStream

Specifies the Event-driven transfer options. Event-driven transfers listen to an event stream to transfer updated files.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventStreamExpirationTime** | **String** | Specifies the data and time at which Storage Transfer Service stops listening for events from this stream. After this time, any transfers in progress will complete, but no new transfers are initiated. |  [optional] |
|**eventStreamStartTime** | **String** | Specifies the date and time that Storage Transfer Service starts listening for events from this stream. If no start time is specified or start time is in the past, Storage Transfer Service starts listening immediately. |  [optional] |
|**name** | **String** | Required. Specifies a unique name of the resource such as AWS SQS ARN in the form &#39;arn:aws:sqs:region:account_id:queue_name&#39;, or Pub/Sub subscription resource name in the form &#39;projects/{project}/subscriptions/{sub}&#39;. |  [optional] |



