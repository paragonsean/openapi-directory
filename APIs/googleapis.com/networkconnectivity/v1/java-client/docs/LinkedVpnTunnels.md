

# LinkedVpnTunnels

A collection of Cloud VPN tunnel resources. These resources should be redundant HA VPN tunnels that all advertise the same prefixes to Google Cloud. Alternatively, in a passive/active configuration, all tunnels should be capable of advertising the same prefixes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**siteToSiteDataTransfer** | **Boolean** | A value that controls whether site-to-site data transfer is enabled for these resources. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). |  [optional] |
|**uris** | **List&lt;String&gt;** | The URIs of linked VPN tunnel resources. |  [optional] |
|**vpcNetwork** | **String** | Output only. The VPC network where these VPN tunnels are located. |  [optional] [readonly] |



