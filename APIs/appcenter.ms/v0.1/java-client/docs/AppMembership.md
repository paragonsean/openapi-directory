

# AppMembership


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** |  |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) |  |  [optional] |
|**permissions** | **List&lt;String&gt;** |  |  [optional] |
|**sourceId** | **String** |  |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) |  |  [optional] |
|**userId** | **String** |  |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |
| CODEPUSH | &quot;codepush&quot; |
| TESTCLOUD | &quot;testcloud&quot; |
| HOCKEYAPP_DOGFOOD | &quot;hockeyapp-dogfood&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| ORG | &quot;org&quot; |
| DISTRIBUTION_GROUP | &quot;distribution_group&quot; |
| TEAM | &quot;team&quot; |
| RELEASE | &quot;release&quot; |



