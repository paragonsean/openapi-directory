

# ConsentHeaderHandling

How the server handles the consent header.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profile** | [**ProfileEnum**](#ProfileEnum) | Optional. Specifies the default server behavior when the header is empty. If not specified, the &#x60;ScopeProfile.PERMIT_EMPTY_SCOPE&#x60; option is used. |  [optional] |



## Enum: ProfileEnum

| Name | Value |
|---- | -----|
| SCOPE_PROFILE_UNSPECIFIED | &quot;SCOPE_PROFILE_UNSPECIFIED&quot; |
| PERMIT_EMPTY_SCOPE | &quot;PERMIT_EMPTY_SCOPE&quot; |
| REQUIRED_ON_READ | &quot;REQUIRED_ON_READ&quot; |



