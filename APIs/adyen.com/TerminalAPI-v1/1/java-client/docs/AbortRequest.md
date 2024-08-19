

# AbortRequest

It conveys Information requested for identification of the message request carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale System (DisplayOutput). Body of the Abort Request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abortReason** | **String** | Reason of aborting a transaction. |  |
|**displayOutput** | [**DisplayOutput**](DisplayOutput.md) |  |  [optional] |
|**messageReference** | [**MessageReference**](MessageReference.md) |  |  |



