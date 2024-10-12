# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2RequestMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionId** | **String** | An identifier that ties multiple requests to the same action. For example, multiple requests to the CAS, Action Cache, and Execution API are used in order to compile foo.cc. | [optional] 
**actionMnemonic** | **String** | A brief description of the kind of action, for example, CppCompile or GoLink. There is no standard agreed set of values for this, and they are expected to vary between different client tools. | [optional] 
**configurationId** | **String** | An identifier for the configuration in which the target was built, e.g. for differentiating building host tools or different target platforms. There is no expectation that this value will have any particular structure, or equality across invocations, though some client tools may offer these guarantees. | [optional] 
**correlatedInvocationsId** | **String** | An identifier to tie multiple tool invocations together. For example, runs of foo_test, bar_test and baz_test on a post-submit of a given patch. | [optional] 
**targetId** | **String** | An identifier for the target which produced this action. No guarantees are made around how many actions may relate to a single target. | [optional] 
**toolDetails** | [**BuildBazelRemoteExecutionV2ToolDetails**](BuildBazelRemoteExecutionV2ToolDetails.md) |  | [optional] 
**toolInvocationId** | **String** | An identifier that ties multiple actions together to a final result. For example, multiple actions are required to build and run foo_test. | [optional] 


