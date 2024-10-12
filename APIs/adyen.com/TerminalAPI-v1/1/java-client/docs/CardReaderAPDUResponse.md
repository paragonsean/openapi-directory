

# CardReaderAPDUResponse

It contains the result of the requested service, APDU response sent by the chip of the card in response to the APDU request. Content of the Card Reader APDU Response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apDUData** | **String** | Data field of the APDU command (Lc + Data). |  [optional] |
|**cardStatusWords** | **String** | Status of a smartcard response to a command (SW1-SW2). |  |
|**response** | [**Response**](Response.md) |  |  |



