# MerakiDashboardApi.CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description for your Bonjour forwarding rule. Optional. | [optional] 
**services** | **[String]** | A list of Bonjour services. At least one service must be specified. Available services are &#39;All Services&#39;, &#39;AirPlay&#39;, &#39;AFP&#39;, &#39;BitTorrent&#39;, &#39;FTP&#39;, &#39;iChat&#39;, &#39;iTunes&#39;, &#39;Printers&#39;, &#39;Samba&#39;, &#39;Scanners&#39; and &#39;SSH&#39; | 
**vlanId** | **String** | The ID of the service VLAN. Required. | 



## Enum: [ServicesEnum]


* `AFP` (value: `"AFP"`)

* `AirPlay` (value: `"AirPlay"`)

* `All Services` (value: `"All Services"`)

* `BitTorrent` (value: `"BitTorrent"`)

* `FTP` (value: `"FTP"`)

* `Printers` (value: `"Printers"`)

* `SSH` (value: `"SSH"`)

* `Samba` (value: `"Samba"`)

* `Scanners` (value: `"Scanners"`)

* `iChat` (value: `"iChat"`)

* `iTunes` (value: `"iTunes"`)




