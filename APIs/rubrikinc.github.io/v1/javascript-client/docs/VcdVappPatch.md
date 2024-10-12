# RubrikRestApi.VcdVappPatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | ID assigned to the SLA Domain object that manages protection for the specified vApp object. Existing snapshots of the object will be retained with the configuration of the specified SLA Domain. | [optional] 
**isBestEffortSynchronizationEnabled** | **Boolean** | Boolean value that indicates whether the Rubrik cluster should attempt taking synchronized snapshots across all child virtual machines of the vApp. | [optional] 
**isPaused** | **Boolean** | Boolean value that indicates whether protection activity is paused for the specified vApp. Set to &#39;true&#39; when protection activity is paused and &#39;false&#39; when protection activity is not paused. Protection activity includes backup, replication, and archiving. | [optional] 
**vcdVmMoidsToExcludeFromSnapshot** | **[String]** | Array containing vCloud Director virtual machine moids that will be excluded from vApp snapshots. | [optional] 


