# MigrationCenterApi.Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignedGroups** | **[String]** | Output only. The list of groups that the asset is assigned to. | [optional] [readonly] 
**attributes** | **{String: String}** | Generic asset attributes. | [optional] 
**createTime** | **String** | Output only. The timestamp when the asset was created. | [optional] [readonly] 
**hidden** | **Boolean** | Optional. Indicates if the asset is hidden. | [optional] 
**hideReason** | **String** | Optional. An optional reason for marking this asset as hidden. | [optional] 
**hideTime** | **String** | Output only. The timestamp when the asset was marked as hidden. | [optional] [readonly] 
**insightList** | [**InsightList**](InsightList.md) |  | [optional] 
**labels** | **{String: String}** | Labels as key value pairs. | [optional] 
**name** | **String** | Output only. The full name of the asset. | [optional] [readonly] 
**performanceData** | [**AssetPerformanceData**](AssetPerformanceData.md) |  | [optional] 
**sources** | **[String]** | Output only. The list of sources contributing to the asset. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the asset was last updated. | [optional] [readonly] 
**virtualMachineDetails** | [**VirtualMachineDetails**](VirtualMachineDetails.md) |  | [optional] 


