# YnabApiEndpoints.Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **Number** | Activity amount in milliunits format | 
**balance** | **Number** | Balance in milliunits format | 
**budgeted** | **Number** | Budgeted amount in milliunits format | 
**categoryGroupId** | **String** |  | 
**deleted** | **Boolean** | Whether or not the category has been deleted.  Deleted categories will only be included in delta requests. | 
**goalCadence** | **Number** | The goal cadence | [optional] 
**goalCadenceFrequency** | **Number** | The goal cadence frequency | [optional] 
**goalCreationMonth** | **Date** | The month a goal was created | [optional] 
**goalDay** | **Number** | The day of the goal | [optional] 
**goalMonthsToBudget** | **Number** | The number of months, including the current month, left in the current goal period. | [optional] 
**goalOverallFunded** | **Number** | The total amount funded towards the goal within the current goal period. | [optional] 
**goalOverallLeft** | **Number** | The amount of funding still needed to complete the goal within the current goal period. | [optional] 
**goalPercentageComplete** | **Number** | The percentage completion of the goal | [optional] 
**goalTarget** | **Number** | The goal target amount in milliunits | [optional] 
**goalTargetMonth** | **Date** | The original target month for the goal to be completed.  Only some goal types specify this date. | [optional] 
**goalType** | **String** | The type of goal, if the category has a goal (TB&#x3D;&#39;Target Category Balance&#39;, TBD&#x3D;&#39;Target Category Balance by Date&#39;, MF&#x3D;&#39;Monthly Funding&#39;, NEED&#x3D;&#39;Plan Your Spending&#39;) | [optional] 
**goalUnderFunded** | **Number** | The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period.  This amount will generally correspond to the &#39;Underfunded&#39; amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month. | [optional] 
**hidden** | **Boolean** | Whether or not the category is hidden | 
**id** | **String** |  | 
**name** | **String** |  | 
**note** | **String** |  | [optional] 
**originalCategoryGroupId** | **String** | DEPRECATED: No longer used.  Value will always be null. | [optional] 



## Enum: GoalTypeEnum


* `TB` (value: `"TB"`)

* `TBD` (value: `"TBD"`)

* `MF` (value: `"MF"`)

* `NEED` (value: `"NEED"`)

* `DEBT` (value: `"DEBT"`)




