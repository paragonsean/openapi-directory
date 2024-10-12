

# Destination


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Id of a distribution group / store. The release will be associated with this distribution group / store. If the distribution group / store doesn&#39;t exist a 400 is returned. If both distribution group / store name and id are passed, the id is taking precedence. |  |
|**name** | **String** | Name of a distribution group / distribution store. The release will be associated with this distribution group or store. If the distribution group / store doesn&#39;t exist a 400 is returned. If both distribution group / store name and id are passed, the id is taking precedence. |  [optional] |
|**isLatest** | **Boolean** | Is the containing release the latest one in this distribution store. |  [optional] |
|**publishingStatus** | **String** | publishing status of the release in the store. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | type of the distribution store currently stores type can be intune, googleplay or windows. |  [optional] |
|**destinationType** | [**DestinationTypeEnum**](#DestinationTypeEnum) | Destination can be either store or group. |  [optional] |
|**displayName** | **String** | Display name for the group or tester |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTUNE | &quot;intune&quot; |
| GOOGLEPLAY | &quot;googleplay&quot; |
| APPLE | &quot;apple&quot; |
| NONE | &quot;none&quot; |



## Enum: DestinationTypeEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| STORE | &quot;store&quot; |
| TESTER | &quot;tester&quot; |



