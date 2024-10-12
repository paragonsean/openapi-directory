# ConsumptionManagementClient.UsageDetailProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | Account name. | [optional] [readonly] 
**additionalProperties** | **String** | Additional details of this usage item. By default this is not populated, unless it&#39;s specified in $expand. | [optional] [readonly] 
**billableQuantity** | **Number** | The billable usage quantity. | [optional] [readonly] 
**billingPeriodId** | **String** | The id of the billing period resource that the usage belongs to. | [optional] [readonly] 
**chargesBilledSeparately** | **Boolean** | Charges billed separately | [optional] [readonly] 
**consumedService** | **String** | Consumed service name. | [optional] [readonly] 
**costCenter** | **String** | The cost center of this department if it is a department and a costcenter exists | [optional] [readonly] 
**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. | [optional] [readonly] 
**departmentName** | **String** | Department name. | [optional] [readonly] 
**instanceId** | **String** | The uri of the resource instance that the usage is about. | [optional] [readonly] 
**instanceLocation** | **String** | The location of the resource instance that the usage is about. | [optional] [readonly] 
**instanceName** | **String** | The name of the resource instance that the usage is about. | [optional] [readonly] 
**invoiceId** | **String** | The id of the invoice resource that the usage belongs to. | [optional] [readonly] 
**isEstimated** | **Boolean** | The estimated usage is subject to change. | [optional] [readonly] 
**meterDetails** | [**MeterDetails**](MeterDetails.md) |  | [optional] 
**meterId** | **String** | The meter id (GUID). | [optional] [readonly] 
**offerId** | **String** | Offer Id | [optional] [readonly] 
**partNumber** | **String** | Part Number | [optional] [readonly] 
**pretaxCost** | **Number** | The amount of cost before tax. | [optional] [readonly] 
**product** | **String** | Product name. | [optional] [readonly] 
**resourceGuid** | **String** | Resource Guid | [optional] [readonly] 
**subscriptionGuid** | **String** | Subscription guid. | [optional] [readonly] 
**subscriptionName** | **String** | Subscription name. | [optional] [readonly] 
**usageEnd** | **Date** | The end of the date time range covered by the usage detail. | [optional] [readonly] 
**usageQuantity** | **Number** | The quantity of usage. | [optional] [readonly] 
**usageStart** | **Date** | The start of the date time range covered by the usage detail. | [optional] [readonly] 


