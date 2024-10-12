# NetlifysApiDocumentation.SetEnvVarValueRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **String** | The deploy context in which this value will be used. &#x60;dev&#x60; refers to local development when running &#x60;netlify dev&#x60;. | [optional] 
**value** | **String** | The environment variable&#39;s unencrypted value | [optional] 



## Enum: ContextEnum


* `dev` (value: `"dev"`)

* `branch-deploy` (value: `"branch-deploy"`)

* `deploy-preview` (value: `"deploy-preview"`)

* `production` (value: `"production"`)




