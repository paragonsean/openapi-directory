

# MembershipRelation

Message containing membership relation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | An extended description to help users determine the purpose of a &#x60;Group&#x60;. |  [optional] |
|**displayName** | **String** | The display name of the &#x60;Group&#x60;. |  [optional] |
|**group** | **String** | The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Group&#x60;. Shall be of the form &#x60;groups/{group_id}&#x60;. |  [optional] |
|**groupKey** | [**EntityKey**](EntityKey.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. |  [optional] |
|**membership** | **String** | The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Membership&#x60;. Shall be of the form &#x60;groups/{group_id}/memberships/{membership_id}&#x60;. |  [optional] |
|**roles** | [**List&lt;MembershipRole&gt;**](MembershipRole.md) | The &#x60;MembershipRole&#x60;s that apply to the &#x60;Membership&#x60;. |  [optional] |



