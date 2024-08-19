

# MacAddressRequestPartial

MAC-Address Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Unicast MAC address, formatted hexadecimal values with colons.  |  [optional] |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  [optional] |
|**validNotAfter** | **OffsetDateTime** |  |  [optional] |
|**validNotBefore** | **OffsetDateTime** |  |  [optional] |



