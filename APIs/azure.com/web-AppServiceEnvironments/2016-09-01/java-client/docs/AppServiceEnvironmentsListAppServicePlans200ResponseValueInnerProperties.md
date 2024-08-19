

# AppServiceEnvironmentsListAppServicePlans200ResponseValueInnerProperties

AppServicePlan resource specific properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminSiteName** | **String** | App Service plan administration site. |  [optional] |
|**geoRegion** | **String** | Geographical location for the App Service plan. |  [optional] [readonly] |
|**hostingEnvironmentProfile** | [**AppServiceEnvironmentsResume200ResponseValueInnerPropertiesHostingEnvironmentProfile**](AppServiceEnvironmentsResume200ResponseValueInnerPropertiesHostingEnvironmentProfile.md) |  |  [optional] |
|**isSpot** | **Boolean** | If &lt;code&gt;true&lt;/code&gt;, this App Service Plan owns spot instances. |  [optional] |
|**maximumNumberOfWorkers** | **Integer** | Maximum number of instances that can be assigned to this App Service plan. |  [optional] [readonly] |
|**name** | **String** | Name for the App Service plan. |  |
|**numberOfSites** | **Integer** | Number of apps assigned to this App Service plan. |  [optional] [readonly] |
|**perSiteScaling** | **Boolean** | If &lt;code&gt;true&lt;/code&gt;, apps assigned to this App Service plan can be scaled independently. If &lt;code&gt;false&lt;/code&gt;, apps assigned to this App Service plan will scale to all instances of the plan. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the App Service Environment. |  [optional] [readonly] |
|**reserved** | **Boolean** | If Linux app service plan &lt;code&gt;true&lt;/code&gt;, &lt;code&gt;false&lt;/code&gt; otherwise. |  [optional] |
|**resourceGroup** | **String** | Resource group of the App Service plan. |  [optional] [readonly] |
|**spotExpirationTime** | **OffsetDateTime** | The time when the server farm expires. Valid only if it is a spot server farm. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | App Service plan status. |  [optional] [readonly] |
|**subscription** | **String** | App Service plan subscription. |  [optional] [readonly] |
|**targetWorkerCount** | **Integer** | Scaling worker count. |  [optional] |
|**targetWorkerSizeId** | **Integer** | Scaling worker size ID. |  [optional] |
|**workerTierName** | **String** | Target worker tier assigned to the App Service plan. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| DELETING | &quot;Deleting&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| PENDING | &quot;Pending&quot; |
| CREATING | &quot;Creating&quot; |



