# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesUserList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Output only. Id of the user list. | [optional] [readonly] 
**name** | **String** | Name of this user list. Depending on its access_reason, the user list name may not be unique (for example, if access_reason&#x3D;SHARED) | [optional] 
**resourceName** | **String** | Immutable. The resource name of the user list. User list resource names have the form: &#x60;customers/{customer_id}/userLists/{user_list_id}&#x60; | [optional] 
**type** | **String** | Output only. Type of this list. This field is read-only. | [optional] [readonly] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `REMARKETING` (value: `"REMARKETING"`)

* `LOGICAL` (value: `"LOGICAL"`)

* `EXTERNAL_REMARKETING` (value: `"EXTERNAL_REMARKETING"`)

* `RULE_BASED` (value: `"RULE_BASED"`)

* `SIMILAR` (value: `"SIMILAR"`)

* `CRM_BASED` (value: `"CRM_BASED"`)




