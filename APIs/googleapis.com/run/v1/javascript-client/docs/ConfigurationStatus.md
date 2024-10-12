# CloudRunAdminApi.ConfigurationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[GoogleCloudRunV1Condition]**](GoogleCloudRunV1Condition.md) | Conditions communicate information about ongoing/complete reconciliation processes that bring the \&quot;spec\&quot; inline with the observed state of the world. | [optional] 
**latestCreatedRevisionName** | **String** | LatestCreatedRevisionName is the last revision that was created from this Configuration. It might not be ready yet, so for the latest ready revision, use LatestReadyRevisionName. | [optional] 
**latestReadyRevisionName** | **String** | LatestReadyRevisionName holds the name of the latest Revision stamped out from this Configuration that has had its \&quot;Ready\&quot; condition become \&quot;True\&quot;. | [optional] 
**observedGeneration** | **Number** | ObservedGeneration is the &#39;Generation&#39; of the Configuration that was last processed by the controller. The observed generation is updated even if the controller failed to process the spec and create the Revision. Clients polling for completed reconciliation should poll until observedGeneration &#x3D; metadata.generation, and the Ready condition&#39;s status is True or False. | [optional] 


