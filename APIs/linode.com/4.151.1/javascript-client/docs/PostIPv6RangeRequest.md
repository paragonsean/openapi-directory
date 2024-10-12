# LinodeApi.PostIPv6RangeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodeId** | **Number** | The ID of the Linode to assign this range to. The SLAAC address for the provided Linode is used as the range&#39;s &#x60;route_target&#x60;.  * **Required** if &#x60;route_target&#x60; is omitted from the request.  * Mutually exclusive with &#x60;route_target&#x60;. Submitting values for both properties in a request results in an error.  | [optional] 
**prefixLength** | **Number** | The prefix length of the IPv6 range.  | 
**routeTarget** | **String** | The IPv6 SLAAC address to assign this range to.  * **Required** if &#x60;linode_id&#x60; is omitted from the request.  * Mutually exclusive with &#x60;linode_id&#x60;. Submitting values for both properties in a request results in an error.  * **Note**: Omit the &#x60;/128&#x60; prefix length of the SLAAC address when using this property.  | [optional] 



## Enum: PrefixLengthEnum


* `56` (value: `56`)

* `64` (value: `64`)




