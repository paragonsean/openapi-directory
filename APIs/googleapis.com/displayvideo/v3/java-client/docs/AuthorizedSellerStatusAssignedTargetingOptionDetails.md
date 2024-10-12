

# AuthorizedSellerStatusAssignedTargetingOptionDetails

Represents an assigned authorized seller status. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_AUTHORIZED_SELLER_STATUS`. If a resource does not have an `TARGETING_TYPE_AUTHORIZED_SELLER_STATUS` assigned targeting option, it is using the \"Authorized Direct Sellers and Resellers\" option.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedSellerStatus** | [**AuthorizedSellerStatusEnum**](#AuthorizedSellerStatusEnum) | Output only. The authorized seller status to target. |  [optional] [readonly] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60;. |  [optional] |



## Enum: AuthorizedSellerStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTHORIZED_SELLER_STATUS_UNSPECIFIED&quot; |
| AUTHORIZED_DIRECT_SELLERS_ONLY | &quot;AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY&quot; |
| AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS | &quot;AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS&quot; |



