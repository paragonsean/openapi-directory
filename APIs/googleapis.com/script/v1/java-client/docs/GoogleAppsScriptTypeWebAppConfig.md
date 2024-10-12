

# GoogleAppsScriptTypeWebAppConfig

Web app entry point configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Who has permission to run the web app. |  [optional] |
|**executeAs** | [**ExecuteAsEnum**](#ExecuteAsEnum) | Who to execute the web app as. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| UNKNOWN_ACCESS | &quot;UNKNOWN_ACCESS&quot; |
| MYSELF | &quot;MYSELF&quot; |
| DOMAIN | &quot;DOMAIN&quot; |
| ANYONE | &quot;ANYONE&quot; |
| ANYONE_ANONYMOUS | &quot;ANYONE_ANONYMOUS&quot; |



## Enum: ExecuteAsEnum

| Name | Value |
|---- | -----|
| UNKNOWN_EXECUTE_AS | &quot;UNKNOWN_EXECUTE_AS&quot; |
| USER_ACCESSING | &quot;USER_ACCESSING&quot; |
| USER_DEPLOYING | &quot;USER_DEPLOYING&quot; |



