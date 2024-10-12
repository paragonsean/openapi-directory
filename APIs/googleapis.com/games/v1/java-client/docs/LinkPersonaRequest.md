

# LinkPersonaRequest

Request to link an in-game account with a PGS principal (encoded in the session id).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardinalityConstraint** | [**CardinalityConstraintEnum**](#CardinalityConstraintEnum) | Required. Cardinality constraint to observe when linking a persona to a player in the scope of a game. |  [optional] |
|**conflictingLinksResolutionPolicy** | [**ConflictingLinksResolutionPolicyEnum**](#ConflictingLinksResolutionPolicyEnum) | Required. Resolution policy to apply when the linking of a persona to a player would result in violating the specified cardinality constraint. |  [optional] |
|**expireTime** | **String** | Input only. Optional expiration time. |  [optional] |
|**persona** | **String** | Required. Stable identifier of the in-game account. Please refrain from re-using the same persona for different games. |  [optional] |
|**sessionId** | **String** | Required. Opaque server-generated string that encodes all the necessary information to identify the PGS player / Google user and application. |  [optional] |
|**token** | **String** | Required. Value of the token to create. Opaque to Play Games and assumed to be non-stable (encrypted with key rotation). |  [optional] |
|**ttl** | **String** | Input only. Optional time-to-live. |  [optional] |



## Enum: CardinalityConstraintEnum

| Name | Value |
|---- | -----|
| ONE_PERSONA_TO_ONE_PLAYER | &quot;ONE_PERSONA_TO_ONE_PLAYER&quot; |



## Enum: ConflictingLinksResolutionPolicyEnum

| Name | Value |
|---- | -----|
| KEEP_EXISTING_LINKS | &quot;KEEP_EXISTING_LINKS&quot; |
| CREATE_NEW_LINK | &quot;CREATE_NEW_LINK&quot; |



