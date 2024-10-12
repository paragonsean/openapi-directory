

# TargetsPresentCondition

`TargetsPresentCondition` contains information on any Targets referenced in the Delivery Pipeline that do not actually exist.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**missingTargets** | **List&lt;String&gt;** | The list of Target names that do not exist. For example, &#x60;projects/{project_id}/locations/{location_name}/targets/{target_name}&#x60;. |  [optional] |
|**status** | **Boolean** | True if there aren&#39;t any missing Targets. |  [optional] |
|**updateTime** | **String** | Last time the condition was updated. |  [optional] |



