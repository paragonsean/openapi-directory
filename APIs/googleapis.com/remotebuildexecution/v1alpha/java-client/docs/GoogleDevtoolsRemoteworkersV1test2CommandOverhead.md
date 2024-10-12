

# GoogleDevtoolsRemoteworkersV1test2CommandOverhead

DEPRECATED - use CommandResult instead. Can be used as part of CompleteRequest.metadata, or are part of a more sophisticated message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **String** | The elapsed time between calling Accept and Complete. The server will also have its own idea of what this should be, but this excludes the overhead of the RPCs and the bot response time. |  [optional] |
|**overhead** | **String** | The amount of time *not* spent executing the command (ie uploading/downloading files). |  [optional] |



