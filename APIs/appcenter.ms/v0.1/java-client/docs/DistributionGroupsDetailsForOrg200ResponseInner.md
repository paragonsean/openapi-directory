

# DistributionGroupsDetailsForOrg200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The name of the distribution group |  [optional] |
|**id** | **UUID** | The unique ID of the distribution group |  |
|**isPublic** | **Boolean** | Whether the distribution group is public |  |
|**name** | **String** | The name of the distribution group used in URLs |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this distribution group |  |
|**apps** | [**List&lt;AppsList200ResponseInner&gt;**](AppsList200ResponseInner.md) | The apps associated with the distribution group |  |
|**totalAppsCount** | **BigDecimal** | The count of apps associated with this distribution group |  |
|**totalUsersCount** | **BigDecimal** | The count of users in the distribution group |  |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |



