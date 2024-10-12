

# UpdateNetworkAppliancePortRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicy** | **String** | The name of the policy. Only applicable to Access ports. Valid values are: &#39;open&#39;, &#39;8021x-radius&#39;, &#39;mac-radius&#39;, &#39;hybris-radius&#39; for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, &#39;open&#39; is the only valid value and &#39;open&#39; is the default value if the field is missing. |  [optional] |
|**allowedVlans** | **String** | Comma-delimited list of the VLAN ID&#39;s allowed on the port, or &#39;all&#39; to permit all VLAN&#39;s on the port. |  [optional] |
|**dropUntaggedTraffic** | **Boolean** | Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true. |  [optional] |
|**enabled** | **Boolean** | The status of the port |  [optional] |
|**type** | **String** | The type of the port: &#39;access&#39; or &#39;trunk&#39;. |  [optional] |
|**vlan** | **Integer** | Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode. |  [optional] |



