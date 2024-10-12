# RubrikRestApi.SlaConflictsSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicts** | [**[ManagedHierarchyObjectSummary]**](ManagedHierarchyObjectSummary.md) |  | 
**id** | **String** | managedId. | 
**isPossiblyInconsistent** | **Boolean** | Indicates if the results returned are inconsistent due to an ongoing SLA assignment operation within this object&#39;s hierarchy. This endpoint does not consider the results of in flight SLA operations since they have not yet completed. Because the results may change once the operation completes, Rubrik advises waiting until all SLA assignments have completed on this hierarchy before reassigning, unless changing the childrens&#39; SLAs directly with this assignment is unacceptable.  | 


