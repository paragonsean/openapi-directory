

# StartViewerSessionRevocationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelArn** | **String** | The ARN of the channel associated with the viewer session to revoke. |  |
|**viewerId** | **String** | The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information. |  |
|**viewerSessionVersionsLessThanOrEqualTo** | **Integer** | An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0. |  [optional] |



