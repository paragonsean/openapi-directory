

# ThreeDSecureResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticated** | [**AuthenticatedEnum**](#AuthenticatedEnum) | 3D Secure authentication response status. |  |
|**enrolled** | [**EnrolledEnum**](#EnrolledEnum) | Is the cardholder enrolled in 3D Secure. |  |
|**flow** | [**FlowEnum**](#FlowEnum) | 3D Secure 2 authentication flow. |  [optional] |
|**isDowngraded** | **Boolean** | If 3D Secure 2 was attempted but downgraded to 3D Secure 1. |  |
|**liability** | [**LiabilityEnum**](#LiabilityEnum) |  |  |
|**version** | [**VersionEnum**](#VersionEnum) | 3D Secure version. |  [optional] |



## Enum: AuthenticatedEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| NOT_APPLICABLE | &quot;not applicable&quot; |
| ATTEMPTED | &quot;attempted&quot; |



## Enum: EnrolledEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| INVALID_CARD_TIMEOUT | &quot;invalid card/timeout&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: FlowEnum

| Name | Value |
|---- | -----|
| FRICTIONLESS | &quot;frictionless&quot; |
| CHALLENGE | &quot;challenge&quot; |



## Enum: LiabilityEnum

| Name | Value |
|---- | -----|
| PROTECTED | &quot;protected&quot; |
| NOT_PROTECTED | &quot;not protected&quot; |
| PROTECTED_ATTEMPT_ | &quot;protected (attempt)&quot; |



## Enum: VersionEnum

| Name | Value |
|---- | -----|
| _1_0_2 | &quot;1.0.2&quot; |
| _2_1_0 | &quot;2.1.0&quot; |
| _2_2_0 | &quot;2.2.0&quot; |



