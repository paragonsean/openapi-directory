

# ProjectsList200ResponseValueInnerProperties

Project-specific properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | UTC Date and time when project was created |  [optional] [readonly] |
|**databasesInfo** | [**List&lt;ProjectsList200ResponseValueInnerPropertiesDatabasesInfoInner&gt;**](ProjectsList200ResponseValueInnerPropertiesDatabasesInfoInner.md) | List of DatabaseInfo |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The project&#39;s provisioning state |  [optional] [readonly] |
|**sourceConnectionInfo** | [**ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo**](ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo.md) |  |  [optional] |
|**sourcePlatform** | [**SourcePlatformEnum**](#SourcePlatformEnum) | Source platform of the project |  |
|**targetConnectionInfo** | [**ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo**](ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo.md) |  |  [optional] |
|**targetPlatform** | [**TargetPlatformEnum**](#TargetPlatformEnum) | Target platform of the project |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: SourcePlatformEnum

| Name | Value |
|---- | -----|
| SQL | &quot;SQL&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: TargetPlatformEnum

| Name | Value |
|---- | -----|
| SQLDB | &quot;SQLDB&quot; |
| UNKNOWN | &quot;Unknown&quot; |



