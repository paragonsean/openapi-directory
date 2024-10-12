# RemoteBuildExecutionApi.GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directories** | **[String]** | A list of expected directories, relative to the execution root. All paths MUST be delimited by forward slashes. | [optional] 
**files** | **[String]** | A list of expected files, relative to the execution root. All paths MUST be delimited by forward slashes. | [optional] 
**stderrDestination** | **String** | The destination to which any stderr should be sent. The method by which the bot should send the stream contents to that destination is not defined in this API. As examples, the destination could be a file referenced in the &#x60;files&#x60; field in this message, or it could be a URI that must be written via the ByteStream API. | [optional] 
**stdoutDestination** | **String** | The destination to which any stdout should be sent. The method by which the bot should send the stream contents to that destination is not defined in this API. As examples, the destination could be a file referenced in the &#x60;files&#x60; field in this message, or it could be a URI that must be written via the ByteStream API. | [optional] 


