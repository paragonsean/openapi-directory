

# DistributionGroupPrivateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The name of the distribution group |  [optional] |
|**id** | **UUID** | The unique ID of the distribution group |  |
|**isPublic** | **Boolean** | Whether the distribution group is public |  |
|**name** | **String** | The name of the distribution group used in URLs |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this distribution group |  |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) | Type of group |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |



## Enum: GroupTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| HOCKEY_APP_DEFAULT | &quot;HockeyAppDefault&quot; |
| MICROSOFT_DOGFOODING | &quot;MicrosoftDogfooding&quot; |



