# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsListAppServicePlans200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminSiteName** | **String** | App Service plan administration site. | [optional] 
**geoRegion** | **String** | Geographical location for the App Service plan. | [optional] [readonly] 
**hostingEnvironmentProfile** | [**AppServiceEnvironmentsResume200ResponseValueInnerPropertiesHostingEnvironmentProfile**](AppServiceEnvironmentsResume200ResponseValueInnerPropertiesHostingEnvironmentProfile.md) |  | [optional] 
**isSpot** | **Boolean** | If &lt;code&gt;true&lt;/code&gt;, this App Service Plan owns spot instances. | [optional] 
**maximumNumberOfWorkers** | **Number** | Maximum number of instances that can be assigned to this App Service plan. | [optional] [readonly] 
**name** | **String** | Name for the App Service plan. | 
**numberOfSites** | **Number** | Number of apps assigned to this App Service plan. | [optional] [readonly] 
**perSiteScaling** | **Boolean** | If &lt;code&gt;true&lt;/code&gt;, apps assigned to this App Service plan can be scaled independently. If &lt;code&gt;false&lt;/code&gt;, apps assigned to this App Service plan will scale to all instances of the plan. | [optional] [default to false]
**provisioningState** | **String** | Provisioning state of the App Service Environment. | [optional] [readonly] 
**reserved** | **Boolean** | If Linux app service plan &lt;code&gt;true&lt;/code&gt;, &lt;code&gt;false&lt;/code&gt; otherwise. | [optional] [default to false]
**resourceGroup** | **String** | Resource group of the App Service plan. | [optional] [readonly] 
**spotExpirationTime** | **Date** | The time when the server farm expires. Valid only if it is a spot server farm. | [optional] 
**status** | **String** | App Service plan status. | [optional] [readonly] 
**subscription** | **String** | App Service plan subscription. | [optional] [readonly] 
**targetWorkerCount** | **Number** | Scaling worker count. | [optional] 
**targetWorkerSizeId** | **Number** | Scaling worker size ID. | [optional] 
**workerTierName** | **String** | Target worker tier assigned to the App Service plan. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `InProgress` (value: `"InProgress"`)

* `Deleting` (value: `"Deleting"`)





## Enum: StatusEnum


* `Ready` (value: `"Ready"`)

* `Pending` (value: `"Pending"`)

* `Creating` (value: `"Creating"`)




