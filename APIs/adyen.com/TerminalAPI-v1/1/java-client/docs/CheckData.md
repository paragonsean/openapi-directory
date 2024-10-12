

# CheckData

Allows the check information to be provided by the Sale System before requesting the payment, or stored by the Sale System after processing of the payment. Information related to the paper check used for the transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | Mandatory if TrackData absent. |  [optional] |
|**bankID** | **String** | Mandatory if TrackData absent. |  [optional] |
|**checkCardNumber** | **String** | If provided by the customer. |  [optional] |
|**checkNumber** | **String** | Mandatory if TrackData absent. |  [optional] |
|**country** | **String** | Absent if country of the Sale system. |  [optional] |
|**trackData** | [**TrackData**](TrackData.md) |  |  [optional] |
|**typeCode** | **TypeCode** |  |  [optional] |



