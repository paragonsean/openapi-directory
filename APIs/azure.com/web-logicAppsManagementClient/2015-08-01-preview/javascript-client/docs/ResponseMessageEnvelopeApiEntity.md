# LogicAppsManagementClient.ResponseMessageEnvelopeApiEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Resource Id. Typically id is populated only for responses to GET requests. Caller is responsible for passing in this              value for GET requests only.              For example: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupId}/providers/Microsoft.Web/sites/{sitename} | [optional] 
**location** | **String** | Geo region resource belongs to e.g. SouthCentralUS, SouthEastAsia | [optional] 
**name** | **String** | Name of resource | [optional] 
**plan** | [**ArmPlan**](ArmPlan.md) |  | [optional] 
**properties** | [**ApiEntity**](ApiEntity.md) |  | [optional] 
**sku** | [**SkuDescription**](SkuDescription.md) |  | [optional] 
**tags** | **{String: String}** | Tags associated with resource | [optional] 
**type** | **String** | Type of resource e.g Microsoft.Web/sites | [optional] 


