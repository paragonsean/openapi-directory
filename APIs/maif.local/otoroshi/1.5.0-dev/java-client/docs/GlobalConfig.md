

# GlobalConfig

The global config object of Otoroshi, used to customize settings of the current Otoroshi instance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertsEmails** | **List&lt;String&gt;** | Email addresses that will receive all Otoroshi alert events |  |
|**alertsWebhooks** | [**List&lt;Webhook&gt;**](Webhook.md) | Webhook that will receive all Otoroshi alert events |  |
|**analyticsWebhooks** | [**List&lt;Webhook&gt;**](Webhook.md) | Webhook that will receive all internal Otoroshi events |  |
|**apiReadOnly** | **Boolean** | If enabled, Admin API won&#39;t be able to write/update/delete entities |  |
|**autoLinkToDefaultGroup** | **Boolean** | If not defined, every new service descriptor will be added to the default group |  |
|**backofficeAuth0Config** | [**Auth0Config**](Auth0Config.md) |  |  [optional] |
|**cleverSettings** | [**CleverSettings**](CleverSettings.md) |  |  [optional] |
|**elasticReadsConfig** | [**ElasticConfig**](ElasticConfig.md) |  |  [optional] |
|**elasticWritesConfigs** | [**List&lt;ElasticConfig&gt;**](ElasticConfig.md) | Configs. for Elastic writes |  [optional] |
|**endlessIpAddresses** | **List&lt;String&gt;** | IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros |  |
|**ipFiltering** | [**IpFiltering**](IpFiltering.md) |  |  |
|**limitConcurrentRequests** | **Boolean** | If enabled, Otoroshi will reject new request if too much at the same time |  |
|**lines** | **List&lt;String&gt;** | Possibles lines for Otoroshi |  [optional] |
|**mailerSettings** | [**MailerSettings**](MailerSettings.md) |  |  [optional] |
|**maxConcurrentRequests** | **Long** | The number of authorized request processed at the same time |  |
|**maxHttp10ResponseSize** | **Long** | The max size in bytes of an HTTP 1.0 response |  [optional] |
|**maxLogsSize** | **Integer** | Number of events kept locally |  [optional] |
|**middleFingers** | **Boolean** | Use middle finger emoji as a response character for endless HTTP responses |  [optional] |
|**perIpThrottlingQuota** | **Long** | Authorized number of calls per second globally per IP address, measured on 10 seconds |  |
|**privateAppsAuth0Config** | [**Auth0Config**](Auth0Config.md) |  |  [optional] |
|**streamEntityOnly** | **Boolean** | HTTP will be streamed only. Doesn&#39;t work with old browsers |  |
|**throttlingQuota** | **Long** | Authorized number of calls per second globally, measured on 10 seconds |  |
|**u2fLoginOnly** | **Boolean** | If enabled, login to backoffice through Auth0 will be disabled |  |
|**useCircuitBreakers** | **Boolean** | If enabled, services will be authorized to use circuit breakers |  |



