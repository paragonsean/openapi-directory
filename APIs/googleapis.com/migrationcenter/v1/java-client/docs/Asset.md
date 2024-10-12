

# Asset

An asset represents a resource in your environment. Asset types include virtual machines and databases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedGroups** | **List&lt;String&gt;** | Output only. The list of groups that the asset is assigned to. |  [optional] [readonly] |
|**attributes** | **Map&lt;String, String&gt;** | Generic asset attributes. |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the asset was created. |  [optional] [readonly] |
|**insightList** | [**InsightList**](InsightList.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs. |  [optional] |
|**machineDetails** | [**MachineDetails**](MachineDetails.md) |  |  [optional] |
|**name** | **String** | Output only. The full name of the asset. |  [optional] [readonly] |
|**performanceData** | [**AssetPerformanceData**](AssetPerformanceData.md) |  |  [optional] |
|**sources** | **List&lt;String&gt;** | Output only. The list of sources contributing to the asset. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the asset was last updated. |  [optional] [readonly] |



