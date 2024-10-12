

# GeneralDistributionGroupDetailsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The name of the distribution group |  [optional] |
|**id** | **UUID** | The unique ID of the distribution group |  |
|**isPublic** | **Boolean** | Whether the distribution group is public |  |
|**name** | **String** | The name of the distribution group used in URLs |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this distribution group |  |
|**isShared** | **Boolean** | Whether the distribution group is shared group or not |  |
|**ownerAppId** | **UUID** | If distribution group is owned by an app, this is the unique app ID |  [optional] |
|**ownerOrgId** | **UUID** | If distribution group is owned by an org, this is the unique org ID |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |



