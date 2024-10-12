

# NodeDeactivationInfo

Information about the node deactivation. This information is valid for a node that is undergoing deactivation or has already been deactivated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeDeactivationIntent** | **NodeDeactivationIntent** |  |  [optional] |
|**nodeDeactivationStatus** | **NodeDeactivationStatus** |  |  [optional] |
|**nodeDeactivationTask** | [**List&lt;NodeDeactivationTask&gt;**](NodeDeactivationTask.md) | List of tasks representing the deactivation operation on the node. |  [optional] |
|**pendingSafetyChecks** | [**List&lt;SafetyCheckWrapper&gt;**](SafetyCheckWrapper.md) | List of pending safety checks |  [optional] |



