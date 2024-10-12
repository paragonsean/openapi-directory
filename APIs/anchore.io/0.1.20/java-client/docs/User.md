

# User

A username for authenticating with one or more types of credentials. User type defines the expected credentials allowed for the user. Native users have passwords, External users have no credential internally. Internal users are service/system users for inter-service communication.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The timestampt the user record was created |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The timestamp of the last update to this record |  [optional] |
|**source** | **String** | If the user is external, this is the source that the user was initialized from. All other user types have this set to null |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The user&#39;s type |  [optional] |
|**username** | **String** | The username to authenticate with |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NATIVE | &quot;native&quot; |
| INTERNAL | &quot;internal&quot; |
| EXTERNAL | &quot;external&quot; |



