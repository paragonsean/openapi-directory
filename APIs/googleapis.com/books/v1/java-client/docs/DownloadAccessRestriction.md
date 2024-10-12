

# DownloadAccessRestriction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceAllowed** | **Boolean** | If restricted, whether access is granted for this (user, device, volume). |  [optional] |
|**downloadsAcquired** | **Integer** | If restricted, the number of content download licenses already acquired (including the requesting client, if licensed). |  [optional] |
|**justAcquired** | **Boolean** | If deviceAllowed, whether access was just acquired with this request. |  [optional] |
|**kind** | **String** | Resource type. |  [optional] |
|**maxDownloadDevices** | **Integer** | If restricted, the maximum number of content download licenses for this volume. |  [optional] |
|**message** | **String** | Error/warning message. |  [optional] |
|**nonce** | **String** | Client nonce for verification. Download access and client-validation only. |  [optional] |
|**reasonCode** | **String** | Error/warning reason code. Additional codes may be added in the future. 0 OK 100 ACCESS_DENIED_PUBLISHER_LIMIT 101 ACCESS_DENIED_LIMIT 200 WARNING_USED_LAST_ACCESS |  [optional] |
|**restricted** | **Boolean** | Whether this volume has any download access restrictions. |  [optional] |
|**signature** | **String** | Response signature. |  [optional] |
|**source** | **String** | Client app identifier for verification. Download access and client-validation only. |  [optional] |
|**volumeId** | **String** | Identifies the volume for which this entry applies. |  [optional] |



