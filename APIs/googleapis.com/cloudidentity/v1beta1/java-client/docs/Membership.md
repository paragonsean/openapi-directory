

# Membership

A membership within the Cloud Identity Groups API. A `Membership` defines a relationship between a `Group` and an entity belonging to that `Group`, referred to as a \"member\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the &#x60;Membership&#x60; was created. |  [optional] [readonly] |
|**deliverySetting** | [**DeliverySettingEnum**](#DeliverySettingEnum) | Output only. Delivery setting associated with the membership. |  [optional] [readonly] |
|**memberKey** | [**EntityKey**](EntityKey.md) |  |  [optional] |
|**name** | **String** | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Membership&#x60;. Shall be of the form &#x60;groups/{group_id}/memberships/{membership_id}&#x60;. |  [optional] [readonly] |
|**preferredMemberKey** | [**EntityKey**](EntityKey.md) |  |  [optional] |
|**roles** | [**List&lt;MembershipRole&gt;**](MembershipRole.md) | The &#x60;MembershipRole&#x60;s that apply to the &#x60;Membership&#x60;. If unspecified, defaults to a single &#x60;MembershipRole&#x60; with &#x60;name&#x60; &#x60;MEMBER&#x60;. Must not contain duplicate &#x60;MembershipRole&#x60;s with the same &#x60;name&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the membership. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the &#x60;Membership&#x60; was last updated. |  [optional] [readonly] |



## Enum: DeliverySettingEnum

| Name | Value |
|---- | -----|
| DELIVERY_SETTING_UNSPECIFIED | &quot;DELIVERY_SETTING_UNSPECIFIED&quot; |
| ALL_MAIL | &quot;ALL_MAIL&quot; |
| DIGEST | &quot;DIGEST&quot; |
| DAILY | &quot;DAILY&quot; |
| NONE | &quot;NONE&quot; |
| DISABLED | &quot;DISABLED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| USER | &quot;USER&quot; |
| SERVICE_ACCOUNT | &quot;SERVICE_ACCOUNT&quot; |
| GROUP | &quot;GROUP&quot; |
| SHARED_DRIVE | &quot;SHARED_DRIVE&quot; |
| OTHER | &quot;OTHER&quot; |



