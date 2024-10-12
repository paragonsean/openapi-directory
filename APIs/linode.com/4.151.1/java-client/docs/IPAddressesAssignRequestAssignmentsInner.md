

# IPAddressesAssignRequestAssignmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The IPv4 address or IPv6 range for this assignment. * Must be an IPv4 address or an IPv6 range you can access in the Region specified. * IPv6 ranges must include a prefix length of &#x60;/56&#x60; or &#x60;/64&#x60;, for example: &#x60;2001:db8:3c4d:15::/64&#x60;. * Assignment of an IPv6 range to a Linode updates the route target of the range to the assigned Linode&#39;s SLAAC address. * May be a public or private address.  |  [optional] |
|**linodeId** | **Integer** | The ID of the Linode to assign this address to. The IP&#39;s previous Linode will lose this address, and must end up with at least one public address and no more than one private address once all assignments have been made.  |  [optional] |



