# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCustomerManagerLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managerCustomer** | **String** | Output only. The manager customer linked to the customer. | [optional] [readonly] 
**managerLinkId** | **String** | Output only. ID of the customer-manager link. This field is read only. | [optional] [readonly] 
**resourceName** | **String** | Immutable. Name of the resource. CustomerManagerLink resource names have the form: &#x60;customers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}&#x60; | [optional] 
**status** | **String** | Status of the link between the customer and the manager. | [optional] 



## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `PENDING` (value: `"PENDING"`)

* `REFUSED` (value: `"REFUSED"`)

* `CANCELED` (value: `"CANCELED"`)




