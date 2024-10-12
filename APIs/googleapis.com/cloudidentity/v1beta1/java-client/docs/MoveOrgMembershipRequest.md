

# MoveOrgMembershipRequest

The request message for OrgMembershipsService.MoveOrgMembership.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | **String** | Required. Immutable. Customer on whose membership change is made. All authorization will happen on the role assignments of this customer. Format: customers/{$customerId} where &#x60;$customerId&#x60; is the &#x60;id&#x60; from the [Admin SDK &#x60;Customer&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/customers). You may also use &#x60;customers/my_customer&#x60; to specify your own organization. |  [optional] |
|**destinationOrgUnit** | **String** | Required. Immutable. OrgUnit where the membership will be moved to. Format: orgUnits/{$orgUnitId} where &#x60;$orgUnitId&#x60; is the &#x60;orgUnitId&#x60; from the [Admin SDK &#x60;OrgUnit&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits). |  [optional] |



