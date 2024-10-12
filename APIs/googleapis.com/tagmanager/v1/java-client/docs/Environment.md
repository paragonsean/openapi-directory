

# Environment

Represents a Google Tag Manager Environment. Note that a user can create, delete and update environments of type USER, but can only update the enable_debug and url fields of environments of other types.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**authorizationCode** | **String** | The environment authorization code. |  [optional] |
|**authorizationTimestampMs** | **String** | The last update time-stamp for the authorization code. |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**containerVersionId** | **String** |  |  [optional] |
|**description** | **String** | The environment description. Can be set or changed only on USER type environments. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |  [optional] |
|**enableDebug** | **Boolean** | Whether or not to enable debug by default on for the environment. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |  [optional] |
|**environmentId** | **String** | GTM Environment ID uniquely identifies the GTM Environment. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM environment as computed at storage time. This value is recomputed whenever the environment is modified. |  [optional] |
|**name** | **String** | The environment display name. Can be set or changed only on USER type environments. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this environment. |  [optional] |
|**url** | **String** | Default preview page url for the environment. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| LIVE | &quot;live&quot; |
| LATEST | &quot;latest&quot; |
| DRAFT | &quot;draft&quot; |



