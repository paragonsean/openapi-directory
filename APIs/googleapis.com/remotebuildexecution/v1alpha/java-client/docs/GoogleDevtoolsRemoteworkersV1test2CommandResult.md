

# GoogleDevtoolsRemoteworkersV1test2CommandResult

All information about the execution of a command, suitable for providing as the Bots interface's `Lease.result` field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **String** | The elapsed time between calling Accept and Complete. The server will also have its own idea of what this should be, but this excludes the overhead of the RPCs and the bot response time. |  [optional] |
|**exitCode** | **Integer** | The exit code of the process. An exit code of \&quot;0\&quot; should only be trusted if &#x60;status&#x60; has a code of OK (otherwise it may simply be unset). |  [optional] |
|**metadata** | **List&lt;Map&lt;String, Object&gt;&gt;** | Implementation-dependent metadata about the task. Both servers and bots may define messages which can be encoded here; bots are free to provide metadata in multiple formats, and servers are free to choose one or more of the values to process and ignore others. In particular, it is *not* considered an error for the bot to provide the server with a field that it doesn&#39;t know about. |  [optional] |
|**outputs** | [**GoogleDevtoolsRemoteworkersV1test2Digest**](GoogleDevtoolsRemoteworkersV1test2Digest.md) |  |  [optional] |
|**overhead** | **String** | The amount of time *not* spent executing the command (ie uploading/downloading files). |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



