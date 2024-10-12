

# GoogleAdsSearchads360V0ResourcesCustomerManagerLink

Represents customer-manager link relationship.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managerCustomer** | **String** | Output only. The manager customer linked to the customer. |  [optional] [readonly] |
|**managerLinkId** | **String** | Output only. ID of the customer-manager link. This field is read only. |  [optional] [readonly] |
|**resourceName** | **String** | Immutable. Name of the resource. CustomerManagerLink resource names have the form: &#x60;customers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the link between the customer and the manager. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| PENDING | &quot;PENDING&quot; |
| REFUSED | &quot;REFUSED&quot; |
| CANCELED | &quot;CANCELED&quot; |



