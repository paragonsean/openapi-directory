

# ApplicationInsightsComponentProperties

Properties that define an Application Insights component resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Application Insights Unique ID for your Application. |  [optional] [readonly] |
|**applicationId** | **String** | The unique ID of your application. This field mirrors the &#39;Name&#39; field and cannot be changed. |  [optional] [readonly] |
|**applicationType** | [**ApplicationTypeEnum**](#ApplicationTypeEnum) | Type of application being monitored. |  |
|**connectionString** | **String** | Application Insights component connection string. |  [optional] [readonly] |
|**creationDate** | **OffsetDateTime** | Creation Date for the Application Insights component, in ISO 8601 format. |  [optional] [readonly] |
|**disableIpMasking** | **Boolean** | Disable IP masking. |  [optional] |
|**flowType** | [**FlowTypeEnum**](#FlowTypeEnum) | Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to &#39;Bluefield&#39; when creating/updating a component via the REST API. |  [optional] |
|**hockeyAppId** | **String** | The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp. |  [optional] |
|**hockeyAppToken** | **String** | Token used to authenticate communications with between Application Insights and HockeyApp. |  [optional] [readonly] |
|**immediatePurgeDataOn30Days** | **Boolean** | Purge data immediately after 30 days. |  [optional] |
|**instrumentationKey** | **String** | Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component. |  [optional] [readonly] |
|**requestSource** | [**RequestSourceEnum**](#RequestSourceEnum) | Describes what tool created this Application Insights component. Customers using this API should set this to the default &#39;rest&#39;. |  [optional] |
|**retentionInDays** | **Integer** | Retention period in days. |  [optional] |
|**samplingPercentage** | **Double** | Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry. |  [optional] |
|**tenantId** | **String** | Azure Tenant Id. |  [optional] [readonly] |
|**provisioningState** | **String** | Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed. |  [optional] [readonly] |



## Enum: ApplicationTypeEnum

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| OTHER | &quot;other&quot; |



## Enum: FlowTypeEnum

| Name | Value |
|---- | -----|
| BLUEFIELD | &quot;Bluefield&quot; |



## Enum: RequestSourceEnum

| Name | Value |
|---- | -----|
| REST | &quot;rest&quot; |



