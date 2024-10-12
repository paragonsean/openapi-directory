

# SetEnvVarValueRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**ContextEnum**](#ContextEnum) | The deploy context in which this value will be used. &#x60;dev&#x60; refers to local development when running &#x60;netlify dev&#x60;. |  [optional] |
|**value** | **String** | The environment variable&#39;s unencrypted value |  [optional] |



## Enum: ContextEnum

| Name | Value |
|---- | -----|
| DEV | &quot;dev&quot; |
| BRANCH_DEPLOY | &quot;branch-deploy&quot; |
| DEPLOY_PREVIEW | &quot;deploy-preview&quot; |
| PRODUCTION | &quot;production&quot; |



