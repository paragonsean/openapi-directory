

# ApplicationSource

Defines the source application for a VSTS pipeline.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationConfiguration** | **Map&lt;String, String&gt;** | Application specific properties. |  [optional] |
|**applicationType** | [**ApplicationTypeEnum**](#ApplicationTypeEnum) | Type of application. |  |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Type of application source. |  |



## Enum: ApplicationTypeEnum

| Name | Value |
|---- | -----|
| ASP_DOT_NET | &quot;AspDotNet&quot; |
| ASP_DOT_NET_CORE | &quot;AspDotNetCore&quot; |
| NODE_JS | &quot;NodeJs&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| CODE_TEMPLATE | &quot;CodeTemplate&quot; |
| CODE_REPOSITORY | &quot;CodeRepository&quot; |



