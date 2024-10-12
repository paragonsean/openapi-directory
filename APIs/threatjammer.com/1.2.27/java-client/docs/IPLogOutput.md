

# IPLogOutput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**cidr** | **String** |  |  [optional] |
|**dataset** | **String** |  |  |
|**lapse** | [**LapseEnum**](#LapseEnum) |  |  |
|**risk** | [**RiskEnum**](#RiskEnum) |  |  |
|**score** | **Integer** |  |  [optional] |
|**self** | **String** |  |  [optional] |
|**source** | **String** |  |  |
|**timestamp** | **Integer** |  |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ADD | &quot;ADD&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: LapseEnum

| Name | Value |
|---- | -----|
| _1_H | &quot;1H&quot; |
| _6_H | &quot;6H&quot; |
| _12_H | &quot;12H&quot; |
| _1_D | &quot;1D&quot; |
| _7_D | &quot;7D&quot; |
| _30_D | &quot;30D&quot; |
| _90_D | &quot;90D&quot; |
| _180_D | &quot;180D&quot; |
| _365_D | &quot;365D&quot; |



## Enum: RiskEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



