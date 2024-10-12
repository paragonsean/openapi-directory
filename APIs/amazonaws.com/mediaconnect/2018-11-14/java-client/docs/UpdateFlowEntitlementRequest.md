

# UpdateFlowEntitlementRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user. |  [optional] |
|**encryption** | [**UpdateFlowOutputRequestEncryption**](UpdateFlowOutputRequestEncryption.md) |  |  [optional] |
|**entitlementStatus** | [**EntitlementStatusEnum**](#EntitlementStatusEnum) | An indication of whether you want to enable the entitlement to allow access, or disable it to stop streaming content to the subscriber’s flow temporarily. If you don’t specify the entitlementStatus field in your request, MediaConnect leaves the value unchanged. |  [optional] |
|**subscribers** | **List&lt;String&gt;** | The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source. |  [optional] |



## Enum: EntitlementStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



