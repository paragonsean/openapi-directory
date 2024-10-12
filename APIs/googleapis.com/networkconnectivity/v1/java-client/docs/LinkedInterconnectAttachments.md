

# LinkedInterconnectAttachments

A collection of VLAN attachment resources. These resources should be redundant attachments that all advertise the same prefixes to Google Cloud. Alternatively, in active/passive configurations, all attachments should be capable of advertising the same prefixes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**siteToSiteDataTransfer** | **Boolean** | A value that controls whether site-to-site data transfer is enabled for these resources. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). |  [optional] |
|**uris** | **List&lt;String&gt;** | The URIs of linked interconnect attachment resources |  [optional] |
|**vpcNetwork** | **String** | Output only. The VPC network where these VLAN attachments are located. |  [optional] [readonly] |



