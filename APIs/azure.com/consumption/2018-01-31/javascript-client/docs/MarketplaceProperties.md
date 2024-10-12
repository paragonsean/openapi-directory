# ConsumptionManagementClient.MarketplaceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | Account name. | [optional] [readonly] 
**additionalProperties** | **String** | Additional details of this usage item. By default this is not populated, unless it&#39;s specified in $expand. | [optional] [readonly] 
**billingPeriodId** | **String** | The id of the billing period resource that the usage belongs to. | [optional] [readonly] 
**consumedQuantity** | **Number** | The quantity of usage. | [optional] [readonly] 
**consumedService** | **String** | Consumed service name. | [optional] [readonly] 
**costCenter** | **String** | The cost center of this department if it is a department and a costcenter exists | [optional] [readonly] 
**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. | [optional] [readonly] 
**departmentName** | **String** | Department name. | [optional] [readonly] 
**instanceId** | **String** | The uri of the resource instance that the usage is about. | [optional] [readonly] 
**instanceName** | **String** | The name of the resource instance that the usage is about. | [optional] [readonly] 
**isEstimated** | **Boolean** | The estimated usage is subject to change. | [optional] [readonly] 
**meterId** | **String** | The meter id. | [optional] [readonly] 
**offerName** | **String** | The type of offer. | [optional] [readonly] 
**orderNumber** | **String** | The order number. | [optional] [readonly] 
**planName** | **String** | The name of plan. | [optional] [readonly] 
**pretaxCost** | **Number** | The amount of cost before tax. | [optional] [readonly] 
**publisherName** | **String** | The name of publisher. | [optional] [readonly] 
**resourceGroup** | **String** | The name of resource group. | [optional] [readonly] 
**resourceRate** | **Number** | The marketplace resource rate. | [optional] [readonly] 
**subscriptionGuid** | **String** | Subscription guid. | [optional] [readonly] 
**subscriptionName** | **String** | Subscription name. | [optional] [readonly] 
**unitOfMeasure** | **String** | The unit of measure. | [optional] [readonly] 
**usageEnd** | **Date** | The end of the date time range covered by the usage detail. | [optional] [readonly] 
**usageStart** | **Date** | The start of the date time range covered by the usage detail. | [optional] [readonly] 


