

# CardReaderAPDURequest

It contains the APDU request to send to the chip of the card, and a possible invitation message to display on the CashierInterface or the CustomerInterface. Content of the Card Reader APDU Request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apDUClass** | **String** | Class field of the APDU command (CLA). |  |
|**apDUData** | **String** | Data field of the APDU command (Lc + Data). |  [optional] |
|**apDUExpectedLength** | **String** | Expected length of the data field of the APDU response to the command (Le). |  [optional] |
|**apDUInstruction** | **String** | Instruction field of the APDU command (INS). |  |
|**apDUPar1** | **String** | Parameter 1 field of the APDU command (P1). |  |
|**apDUPar2** | **String** | Parameter 2 field of the APDU command(P2). |  |



