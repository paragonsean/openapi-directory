

# Collaboration

Collaborations define access permissions for users and groups to files and folders, similar to access control lists. A collaboration object grants a user or group access to a file or folder with permissions defined by a specific role.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptanceRequirementsStatus** | [**CollaborationAcceptanceRequirementsStatus**](CollaborationAcceptanceRequirementsStatus.md) |  |  [optional] |
|**accessibleBy** | [**CollaborationAccessibleBy**](CollaborationAccessibleBy.md) |  |  [optional] |
|**acknowledgedAt** | **OffsetDateTime** | When the &#x60;status&#x60; of the collaboration object changed to &#x60;accepted&#x60; or &#x60;rejected&#x60;. |  [optional] |
|**createdAt** | **OffsetDateTime** | When the collaboration object was created. |  [optional] |
|**createdBy** | [**CollaborationCreatedBy**](CollaborationCreatedBy.md) |  |  [optional] |
|**expiresAt** | **OffsetDateTime** | When the collaboration will expire, or &#x60;null&#x60; if no expiration date is set. |  [optional] |
|**id** | **String** | The unique identifier for this collaboration. |  [optional] |
|**inviteEmail** | **String** | The email address used to invite an unregistered collaborator, if they are not a registered user. |  [optional] |
|**item** | [**CollaborationItem**](CollaborationItem.md) |  |  [optional] |
|**modifiedAt** | **OffsetDateTime** | When the collaboration object was last modified. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The level of access granted. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the collaboration invitation. If the status is &#x60;pending&#x60;, &#x60;login&#x60; and &#x60;name&#x60; return an empty string. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;collaboration&#x60; |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| EDITOR | &quot;editor&quot; |
| VIEWER | &quot;viewer&quot; |
| PREVIEWER | &quot;previewer&quot; |
| UPLOADER | &quot;uploader&quot; |
| PREVIEWER_UPLOADER | &quot;previewer uploader&quot; |
| VIEWER_UPLOADER | &quot;viewer uploader&quot; |
| CO_OWNER | &quot;co-owner&quot; |
| OWNER | &quot;owner&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| PENDING | &quot;pending&quot; |
| REJECTED | &quot;rejected&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COLLABORATION | &quot;collaboration&quot; |



