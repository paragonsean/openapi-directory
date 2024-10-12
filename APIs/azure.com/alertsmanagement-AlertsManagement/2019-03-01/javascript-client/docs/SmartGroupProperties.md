# AzureAlertsManagementServiceResourceProvider.SmartGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertSeverities** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of alertSeverities in the smart group | [optional] 
**alertStates** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of alertStates in the smart group | [optional] 
**alertsCount** | **Number** | Total number of alerts in smart group | [optional] 
**lastModifiedDateTime** | **Date** | Last updated time of smart group. Date-Time in ISO-8601 format. | [optional] [readonly] 
**lastModifiedUserName** | **String** | Last modified by user name. | [optional] [readonly] 
**monitorConditions** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of monitorConditions in the smart group | [optional] 
**monitorServices** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of monitorServices in the smart group | [optional] 
**nextLink** | **String** | The URI to fetch the next page of alerts. Call ListNext() with this URI to fetch the next page alerts. | [optional] 
**resourceGroups** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of target resource groups in the smart group | [optional] 
**resourceTypes** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of target resource types in the smart group | [optional] 
**resources** | [**[SmartGroupAggregatedProperty]**](SmartGroupAggregatedProperty.md) | Summary of target resources in the smart group | [optional] 
**severity** | **String** | Severity of smart group is the highest(Sev0 &gt;... &gt; Sev4) severity of all the alerts in the group. | [optional] [readonly] 
**smartGroupState** | **String** | Smart group state | [optional] [readonly] 
**startDateTime** | **Date** | Creation time of smart group. Date-Time in ISO-8601 format. | [optional] [readonly] 



## Enum: SeverityEnum


* `Sev0` (value: `"Sev0"`)

* `Sev1` (value: `"Sev1"`)

* `Sev2` (value: `"Sev2"`)

* `Sev3` (value: `"Sev3"`)

* `Sev4` (value: `"Sev4"`)





## Enum: SmartGroupStateEnum


* `New` (value: `"New"`)

* `Acknowledged` (value: `"Acknowledged"`)

* `Closed` (value: `"Closed"`)




