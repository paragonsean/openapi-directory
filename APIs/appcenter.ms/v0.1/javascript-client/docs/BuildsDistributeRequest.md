# AppCenterClient.BuildsDistributeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**[BuildsDistributeRequestDestinationsInner]**](BuildsDistributeRequestDestinationsInner.md) | Array of objects {id:string, type:string} with \&quot;id\&quot; being the distribution group ID, store ID, or tester email, and \&quot;type\&quot; being \&quot;group\&quot;, \&quot;store\&quot;, or \&quot;tester\&quot; | [optional] 
**mandatoryUpdate** | **Boolean** |  | [optional] 
**notifyTesters** | **Boolean** |  | [optional] [default to true]
**releaseNotes** | **String** | The release notes | [optional] 


