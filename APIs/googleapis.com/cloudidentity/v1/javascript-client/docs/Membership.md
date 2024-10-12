# CloudIdentityApi.Membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the &#x60;Membership&#x60; was created. | [optional] [readonly] 
**deliverySetting** | **String** | Output only. Delivery setting associated with the membership. | [optional] [readonly] 
**name** | **String** | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Membership&#x60;. Shall be of the form &#x60;groups/{group}/memberships/{membership}&#x60;. | [optional] [readonly] 
**preferredMemberKey** | [**EntityKey**](EntityKey.md) |  | [optional] 
**roles** | [**[MembershipRole]**](MembershipRole.md) | The &#x60;MembershipRole&#x60;s that apply to the &#x60;Membership&#x60;. If unspecified, defaults to a single &#x60;MembershipRole&#x60; with &#x60;name&#x60; &#x60;MEMBER&#x60;. Must not contain duplicate &#x60;MembershipRole&#x60;s with the same &#x60;name&#x60;. | [optional] 
**type** | **String** | Output only. The type of the membership. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the &#x60;Membership&#x60; was last updated. | [optional] [readonly] 



## Enum: DeliverySettingEnum


* `DELIVERY_SETTING_UNSPECIFIED` (value: `"DELIVERY_SETTING_UNSPECIFIED"`)

* `ALL_MAIL` (value: `"ALL_MAIL"`)

* `DIGEST` (value: `"DIGEST"`)

* `DAILY` (value: `"DAILY"`)

* `NONE` (value: `"NONE"`)

* `DISABLED` (value: `"DISABLED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `USER` (value: `"USER"`)

* `SERVICE_ACCOUNT` (value: `"SERVICE_ACCOUNT"`)

* `GROUP` (value: `"GROUP"`)

* `SHARED_DRIVE` (value: `"SHARED_DRIVE"`)

* `OTHER` (value: `"OTHER"`)




