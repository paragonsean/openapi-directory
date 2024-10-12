

# DistributionGroupDetailsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The name of the distribution group |  [optional] |
|**id** | **UUID** | The unique ID of the distribution group |  |
|**isPublic** | **Boolean** | Whether the distribution group is public |  |
|**name** | **String** | The name of the distribution group used in URLs |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this distribution group |  |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) | Type of group (Default, HockeyAppDefault or MicrosoftDogfooding) |  [optional] |
|**isShared** | **Boolean** | Whether the distribution group is shared group or not |  |
|**notifiedUserCount** | **BigDecimal** | The count of non-pending users in the distribution group who will be notified by new releases |  |
|**totalAppsCount** | **BigDecimal** | The count of apps associated with this distribution group |  |
|**totalUserCount** | **BigDecimal** | The count of users in the distribution group |  |
|**users** | [**List&lt;DistributionGroupsListUsers200ResponseInner&gt;**](DistributionGroupsListUsers200ResponseInner.md) | The distribution group users |  |



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



