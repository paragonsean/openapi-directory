# RubrikRestApi.ComplianceSummarySLAV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numberOfInComplianceSnapshots** | **Number** | Number of objects in compliance based on the snapshot range filter. | [optional] 
**numberOfOutOfComplianceSnapshots** | **Number** | Number of objects out of compliance based on the snapshot range filter. | [optional] 
**percentOfInComplianceSnapshots** | **Number** | Percent of objects in compliance based on the snapshot range filter. | [optional] 
**percentOfOutOfComplianceSnapshots** | **Number** | Percent of objects out of compliance based on the snapshot range filter. | [optional] 
**snapshotRange** | [**ComplianceRangeFilter**](ComplianceRangeFilter.md) |  | 
**totalProtected** | **Number** | Total number of protected objects based on the snapshot range filter. | [optional] 
**updatedStatus** | [**ComplianceSummaryStatus**](ComplianceSummaryStatus.md) |  | 
**updatedTime** | **Date** | The timestamp of the most recent successful update to the compliance summary stats. | [optional] 


