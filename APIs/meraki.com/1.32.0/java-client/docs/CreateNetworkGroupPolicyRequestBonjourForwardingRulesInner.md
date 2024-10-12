

# CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description for your Bonjour forwarding rule. Optional. |  [optional] |
|**services** | [**List&lt;ServicesEnum&gt;**](#List&lt;ServicesEnum&gt;) | A list of Bonjour services. At least one service must be specified. Available services are &#39;All Services&#39;, &#39;AirPlay&#39;, &#39;AFP&#39;, &#39;BitTorrent&#39;, &#39;FTP&#39;, &#39;iChat&#39;, &#39;iTunes&#39;, &#39;Printers&#39;, &#39;Samba&#39;, &#39;Scanners&#39; and &#39;SSH&#39; |  |
|**vlanId** | **String** | The ID of the service VLAN. Required. |  |



## Enum: List&lt;ServicesEnum&gt;

| Name | Value |
|---- | -----|
| AFP | &quot;AFP&quot; |
| AIR_PLAY | &quot;AirPlay&quot; |
| ALL_SERVICES | &quot;All Services&quot; |
| BIT_TORRENT | &quot;BitTorrent&quot; |
| FTP | &quot;FTP&quot; |
| PRINTERS | &quot;Printers&quot; |
| SSH | &quot;SSH&quot; |
| SAMBA | &quot;Samba&quot; |
| SCANNERS | &quot;Scanners&quot; |
| I_CHAT | &quot;iChat&quot; |
| I_TUNES | &quot;iTunes&quot; |



