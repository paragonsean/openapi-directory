

# LongviewClient

A LongviewClient is a single monitor set up to track statistics about one of your servers. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKey** | **String** | The API key for this Client, used when configuring the Longview Client application on your Linode.  Returns as &#x60;[REDACTED]&#x60; if you do not have read-write access to this client.  |  [optional] [readonly] |
|**apps** | [**LongviewClientApps**](LongviewClientApps.md) |  |  [optional] |
|**created** | **OffsetDateTime** | When this Longview Client was created.  |  [optional] [readonly] |
|**id** | **Integer** | This Client&#39;s unique ID.  |  [optional] [readonly] |
|**installCode** | **String** | The install code for this Client, used when configuring the Longview Client application on your Linode.  Returns as &#x60;[REDACTED]&#x60; if you do not have read-write access to this client.  |  [optional] [readonly] |
|**label** | **String** | This Client&#39;s unique label. This is for display purposes only.  |  [optional] |
|**updated** | **OffsetDateTime** | When this Longview Client was last updated.  |  [optional] [readonly] |



