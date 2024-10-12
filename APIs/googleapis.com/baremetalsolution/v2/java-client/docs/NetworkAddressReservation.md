

# NetworkAddressReservation

A reservation of one or more addresses in a network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endAddress** | **String** | The last address of this reservation block, inclusive. I.e., for cases when reservations are only single addresses, end_address and start_address will be the same. Must be specified as a single IPv4 address, e.g. 10.1.2.2. |  [optional] |
|**note** | **String** | A note about this reservation, intended for human consumption. |  [optional] |
|**startAddress** | **String** | The first address of this reservation block. Must be specified as a single IPv4 address, e.g. 10.1.2.2. |  [optional] |



