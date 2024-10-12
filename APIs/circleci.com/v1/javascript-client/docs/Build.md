# CircleCiRestApi.Build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | commit message body | [optional] 
**branch** | **String** |  | [optional] 
**buildTimeMillis** | **Number** |  | [optional] 
**buildUrl** | **String** |  | [optional] 
**committerEmail** | **String** |  | [optional] 
**committerName** | **String** |  | [optional] 
**dontBuild** | **String** | reason why we didn&#39;t build, if we didn&#39;t build | [optional] 
**lifecycle** | [**Lifecycle**](Lifecycle.md) |  | [optional] 
**previous** | [**PreviousBuild**](PreviousBuild.md) |  | [optional] 
**queuedAt** | **Date** | time build was queued | [optional] 
**reponame** | **String** |  | [optional] 
**retryOf** | **Number** | build_num of the build this is a retry of | [optional] 
**startTime** | **Date** | time build started | [optional] 
**stopTime** | **Date** | time build finished | [optional] 
**subject** | **String** |  | [optional] 
**username** | **String** |  | [optional] 
**vcsUrl** | **String** |  | [optional] 
**why** | **String** | short string explaining the reason we built | [optional] 


