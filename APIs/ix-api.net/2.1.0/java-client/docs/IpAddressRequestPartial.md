

# IpAddressRequestPartial

IP-Address / Prefix allocation Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IPv4 or IPv6 Address in the following format: - IPv4: [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) - IPv6: hexadecimal colon separated notation  |  [optional] |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**fqdn** | **String** |  |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  [optional] |
|**prefixLength** | **Integer** | The CIDR ip prefix length  |  [optional] |
|**validNotAfter** | **OffsetDateTime** |  |  [optional] |
|**validNotBefore** | **OffsetDateTime** |  |  [optional] |
|**version** | **Integer** | The version of the internet protocol.  |  [optional] |



