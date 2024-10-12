

# AccountReport

JSON based account report. This account report contains transactions resulting from the query parameters.  'booked' shall be contained if bookingStatus parameter is set to \"booked\" or \"both\".  'pending' is not contained if the bookingStatus parameter is set to \"booked\" or \"information\".  'information' Only contained if the bookingStatus is set to \"information\" and if supported by ASPSP. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksAccountReport** |  |  |
|**booked** | [**List&lt;Transactions&gt;**](Transactions.md) | Array of transaction details. |  [optional] |
|**information** | [**List&lt;Transactions&gt;**](Transactions.md) | Array of transaction details. |  [optional] |
|**pending** | [**List&lt;Transactions&gt;**](Transactions.md) | Array of transaction details. |  [optional] |



