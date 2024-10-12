# CloudIdentityApi.OrgMembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **String** | Immutable. Org member id as full resource name. Format for shared drive resource: //drive.googleapis.com/drives/{$memberId} where &#x60;$memberId&#x60; is the &#x60;id&#x60; from [Drive API (V3) &#x60;Drive&#x60; resource](https://developers.google.com/drive/api/v3/reference/drives#resource). | [optional] 
**memberUri** | **String** | Uri with which you can read the member. This follows https://aip.dev/122 Format for shared drive resource: https://drive.googleapis.com/drive/v3/drives/{$memberId} where &#x60;$memberId&#x60; is the &#x60;id&#x60; from [Drive API (V3) &#x60;Drive&#x60; resource](https://developers.google.com/drive/api/v3/reference/drives#resource). | [optional] 
**name** | **String** | Required. Immutable. The [resource name](https://cloud.google.com/apis/design/resource_names) of the OrgMembership. Format: orgUnits/{$orgUnitId}/memberships/{$membership} The &#x60;$orgUnitId&#x60; is the &#x60;orgUnitId&#x60; from the [Admin SDK &#x60;OrgUnit&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits). The &#x60;$membership&#x60; shall be of the form &#x60;{$entityType};{$memberId}&#x60;, where &#x60;$entityType&#x60; is the enum value of [OrgMembership.EntityType], and &#x60;memberId&#x60; is the &#x60;id&#x60; from [Drive API (V3) &#x60;Drive&#x60; resource](https://developers.google.com/drive/api/v3/reference/drives#resource) for OrgMembership.EntityType.SHARED_DRIVE. | [optional] 
**type** | **String** | Immutable. Entity type for the org member. | [optional] 



## Enum: TypeEnum


* `ENTITY_TYPE_UNSPECIFIED` (value: `"ENTITY_TYPE_UNSPECIFIED"`)

* `SHARED_DRIVE` (value: `"SHARED_DRIVE"`)




