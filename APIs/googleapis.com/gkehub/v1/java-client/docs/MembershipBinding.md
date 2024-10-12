

# MembershipBinding

MembershipBinding is a subresource of a Membership, representing what Fleet Scopes (or other, future Fleet resources) a Membership is bound to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. When the membership binding was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. When the membership binding was deleted. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels for this MembershipBinding. |  [optional] |
|**name** | **String** | The resource name for the membershipbinding itself &#x60;projects/{project}/locations/{location}/memberships/{membership}/bindings/{membershipbinding}&#x60; |  [optional] |
|**scope** | **String** | A Scope resource name in the format &#x60;projects/_*_/locations/_*_/scopes/_*&#x60;. |  [optional] |
|**state** | [**MembershipBindingLifecycleState**](MembershipBindingLifecycleState.md) |  |  [optional] |
|**uid** | **String** | Output only. Google-generated UUID for this resource. This is unique across all membershipbinding resources. If a membershipbinding resource is deleted and another resource with the same name is created, it gets a different uid. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. When the membership binding was last updated. |  [optional] [readonly] |



