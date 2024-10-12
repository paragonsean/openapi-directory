

# ModifyMembershipRolesRequest

The request message for MembershipsService.ModifyMembershipRoles.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addRoles** | [**List&lt;MembershipRole&gt;**](MembershipRole.md) | The &#x60;MembershipRole&#x60;s to be added. Adding or removing roles in the same request as updating roles is not supported. Must not be set if &#x60;update_roles_params&#x60; is set. |  [optional] |
|**removeRoles** | **List&lt;String&gt;** | The &#x60;name&#x60;s of the &#x60;MembershipRole&#x60;s to be removed. Adding or removing roles in the same request as updating roles is not supported. It is not possible to remove the &#x60;MEMBER&#x60; &#x60;MembershipRole&#x60;. If you wish to delete a &#x60;Membership&#x60;, call MembershipsService.DeleteMembership instead. Must not contain &#x60;MEMBER&#x60;. Must not be set if &#x60;update_roles_params&#x60; is set. |  [optional] |
|**updateRolesParams** | [**List&lt;UpdateMembershipRolesParams&gt;**](UpdateMembershipRolesParams.md) | The &#x60;MembershipRole&#x60;s to be updated. Updating roles in the same request as adding or removing roles is not supported. Must not be set if either &#x60;add_roles&#x60; or &#x60;remove_roles&#x60; is set. |  [optional] |



