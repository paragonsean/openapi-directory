

# GetNetworkSettings200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientPrivacy** | [**GetNetworkSettings200ResponseClientPrivacy**](GetNetworkSettings200ResponseClientPrivacy.md) |  |  [optional] |
|**fips** | [**GetNetworkSettings200ResponseFips**](GetNetworkSettings200ResponseFips.md) |  |  [optional] |
|**localStatusPage** | [**GetNetworkSettings200ResponseLocalStatusPage**](GetNetworkSettings200ResponseLocalStatusPage.md) |  |  [optional] |
|**localStatusPageEnabled** | **Boolean** | Enables / disables the local device status pages (&lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;http://my.meraki.com/&#39;&gt;my.meraki.com, &lt;/a&gt;&lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;http://ap.meraki.com/&#39;&gt;ap.meraki.com, &lt;/a&gt;&lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;http://switch.meraki.com/&#39;&gt;switch.meraki.com, &lt;/a&gt;&lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;http://wired.meraki.com/&#39;&gt;wired.meraki.com&lt;/a&gt;). Optional (defaults to false) |  [optional] |
|**namedVlans** | [**GetNetworkSettings200ResponseNamedVlans**](GetNetworkSettings200ResponseNamedVlans.md) |  |  [optional] |
|**remoteStatusPageEnabled** | **Boolean** | Enables / disables access to the device status page (&lt;a target&#x3D;&#39;_blank&#39;&gt;http://[device&#39;s LAN IP])&lt;/a&gt;. Optional. Can only be set if localStatusPageEnabled is set to true |  [optional] |
|**securePort** | [**GetNetworkSettings200ResponseSecurePort**](GetNetworkSettings200ResponseSecurePort.md) |  |  [optional] |



