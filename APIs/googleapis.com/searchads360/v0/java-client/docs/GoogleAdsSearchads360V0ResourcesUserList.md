

# GoogleAdsSearchads360V0ResourcesUserList

A user list. This is a list of users a customer may target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Output only. Id of the user list. |  [optional] [readonly] |
|**name** | **String** | Name of this user list. Depending on its access_reason, the user list name may not be unique (for example, if access_reason&#x3D;SHARED) |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the user list. User list resource names have the form: &#x60;customers/{customer_id}/userLists/{user_list_id}&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Type of this list. This field is read-only. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| REMARKETING | &quot;REMARKETING&quot; |
| LOGICAL | &quot;LOGICAL&quot; |
| EXTERNAL_REMARKETING | &quot;EXTERNAL_REMARKETING&quot; |
| RULE_BASED | &quot;RULE_BASED&quot; |
| SIMILAR | &quot;SIMILAR&quot; |
| CRM_BASED | &quot;CRM_BASED&quot; |



