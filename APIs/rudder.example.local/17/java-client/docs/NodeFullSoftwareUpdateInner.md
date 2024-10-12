

# NodeFullSoftwareUpdateInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arch** | **String** | CPU architecture of the update |  [optional] |
|**description** | **String** | details about the content of the update, if available |  [optional] |
|**from** | **String** | tool that discovered that update |  [optional] |
|**ids** | **List&lt;String&gt;** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | if available, kind of patch provided by that update, else none |  [optional] |
|**name** | **String** | name of software that can be updated |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | if available, the severity of the update |  [optional] |
|**source** | **String** | information about the source providing that update |  [optional] |
|**version** | **String** | available version for software |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| SECURITY | &quot;security&quot; |
| DEFECT | &quot;defect&quot; |
| ENHANCEMENT | &quot;enhancement&quot; |
| OTHER | &quot;other&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| CRITICAL | &quot;critical&quot; |
| HIGH | &quot;high&quot; |
| MODERATE | &quot;moderate&quot; |
| LOW | &quot;low&quot; |
| OTHER | &quot;other&quot; |



