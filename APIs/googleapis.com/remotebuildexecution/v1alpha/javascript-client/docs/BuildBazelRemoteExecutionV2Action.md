# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2Action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandDigest** | [**BuildBazelRemoteExecutionV2Digest**](BuildBazelRemoteExecutionV2Digest.md) |  | [optional] 
**doNotCache** | **Boolean** | If true, then the &#x60;Action&#x60;&#39;s result cannot be cached, and in-flight requests for the same &#x60;Action&#x60; may not be merged. | [optional] 
**inputRootDigest** | [**BuildBazelRemoteExecutionV2Digest**](BuildBazelRemoteExecutionV2Digest.md) |  | [optional] 
**platform** | [**BuildBazelRemoteExecutionV2Platform**](BuildBazelRemoteExecutionV2Platform.md) |  | [optional] 
**salt** | **Blob** | An optional additional salt value used to place this &#x60;Action&#x60; into a separate cache namespace from other instances having the same field contents. This salt typically comes from operational configuration specific to sources such as repo and service configuration, and allows disowning an entire set of ActionResults that might have been poisoned by buggy software or tool failures. | [optional] 
**timeout** | **String** | A timeout after which the execution should be killed. If the timeout is absent, then the client is specifying that the execution should continue as long as the server will let it. The server SHOULD impose a timeout if the client does not specify one, however, if the client does specify a timeout that is longer than the server&#39;s maximum timeout, the server MUST reject the request. The timeout is only intended to cover the \&quot;execution\&quot; of the specified action and not time in queue nor any overheads before or after execution such as marshalling inputs/outputs. The server SHOULD avoid including time spent the client doesn&#39;t have control over, and MAY extend or reduce the timeout to account for delays or speedups that occur during execution itself (e.g., lazily loading data from the Content Addressable Storage, live migration of virtual machines, emulation overhead). The timeout is a part of the Action message, and therefore two &#x60;Actions&#x60; with different timeouts are different, even if they are otherwise identical. This is because, if they were not, running an &#x60;Action&#x60; with a lower timeout than is required might result in a cache hit from an execution run with a longer timeout, hiding the fact that the timeout is too short. By encoding it directly in the &#x60;Action&#x60;, a lower timeout will result in a cache miss and the execution timeout will fail immediately, rather than whenever the cache entry gets evicted. | [optional] 


