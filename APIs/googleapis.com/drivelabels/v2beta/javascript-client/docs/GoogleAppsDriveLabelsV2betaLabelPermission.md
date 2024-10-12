# DriveLabelsApi.GoogleAppsDriveLabelsV2betaLabelPermission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **String** | Audience to grant a role to. The magic value of &#x60;audiences/default&#x60; may be used to apply the role to the default audience in the context of the organization that owns the Label. | [optional] 
**email** | **String** | Specifies the email address for a user or group pricinpal. Not populated for audience principals. User and Group permissions may only be inserted using email address. On update requests, if email address is specified, no principal should be specified. | [optional] 
**group** | **String** | Group resource name. | [optional] 
**name** | **String** | Resource name of this permission. | [optional] 
**person** | **String** | Person resource name. | [optional] 
**role** | **String** | The role the principal should have. | [optional] 



## Enum: RoleEnum


* `LABEL_ROLE_UNSPECIFIED` (value: `"LABEL_ROLE_UNSPECIFIED"`)

* `READER` (value: `"READER"`)

* `APPLIER` (value: `"APPLIER"`)

* `ORGANIZER` (value: `"ORGANIZER"`)

* `EDITOR` (value: `"EDITOR"`)




