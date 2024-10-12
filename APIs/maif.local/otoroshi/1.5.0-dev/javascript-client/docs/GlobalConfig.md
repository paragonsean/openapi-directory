# OtoroshiAdminApi.GlobalConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertsEmails** | **[String]** | Email addresses that will receive all Otoroshi alert events | 
**alertsWebhooks** | [**[Webhook]**](Webhook.md) | Webhook that will receive all Otoroshi alert events | 
**analyticsWebhooks** | [**[Webhook]**](Webhook.md) | Webhook that will receive all internal Otoroshi events | 
**apiReadOnly** | **Boolean** | If enabled, Admin API won&#39;t be able to write/update/delete entities | 
**autoLinkToDefaultGroup** | **Boolean** | If not defined, every new service descriptor will be added to the default group | 
**backofficeAuth0Config** | [**Auth0Config**](Auth0Config.md) |  | [optional] 
**cleverSettings** | [**CleverSettings**](CleverSettings.md) |  | [optional] 
**elasticReadsConfig** | [**ElasticConfig**](ElasticConfig.md) |  | [optional] 
**elasticWritesConfigs** | [**[ElasticConfig]**](ElasticConfig.md) | Configs. for Elastic writes | [optional] 
**endlessIpAddresses** | **[String]** | IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros | 
**ipFiltering** | [**IpFiltering**](IpFiltering.md) |  | 
**limitConcurrentRequests** | **Boolean** | If enabled, Otoroshi will reject new request if too much at the same time | 
**lines** | **[String]** | Possibles lines for Otoroshi | [optional] 
**mailerSettings** | [**MailerSettings**](MailerSettings.md) |  | [optional] 
**maxConcurrentRequests** | **Number** | The number of authorized request processed at the same time | 
**maxHttp10ResponseSize** | **Number** | The max size in bytes of an HTTP 1.0 response | [optional] 
**maxLogsSize** | **Number** | Number of events kept locally | [optional] 
**middleFingers** | **Boolean** | Use middle finger emoji as a response character for endless HTTP responses | [optional] 
**perIpThrottlingQuota** | **Number** | Authorized number of calls per second globally per IP address, measured on 10 seconds | 
**privateAppsAuth0Config** | [**Auth0Config**](Auth0Config.md) |  | [optional] 
**streamEntityOnly** | **Boolean** | HTTP will be streamed only. Doesn&#39;t work with old browsers | 
**throttlingQuota** | **Number** | Authorized number of calls per second globally, measured on 10 seconds | 
**u2fLoginOnly** | **Boolean** | If enabled, login to backoffice through Auth0 will be disabled | 
**useCircuitBreakers** | **Boolean** | If enabled, services will be authorized to use circuit breakers | 


