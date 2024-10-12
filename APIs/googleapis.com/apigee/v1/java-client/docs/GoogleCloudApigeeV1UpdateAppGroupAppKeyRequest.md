

# GoogleCloudApigeeV1UpdateAppGroupAppKeyRequest

Request for UpdateAppGroupAppKey

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Approve or revoke the consumer key by setting this value to &#x60;approve&#x60; or &#x60;revoke&#x60; respectively. The &#x60;Content-Type&#x60; header, if set, must be set to &#x60;application/octet-stream&#x60;, with empty body. |  [optional] |
|**apiProducts** | **List&lt;String&gt;** | The list of API products that will be associated with the credential. This list will be appended to the existing list of associated API Products for this App Key. Duplicates will be ignored. |  [optional] |
|**appGroupAppKey** | [**GoogleCloudApigeeV1AppGroupAppKey**](GoogleCloudApigeeV1AppGroupAppKey.md) |  |  [optional] |



