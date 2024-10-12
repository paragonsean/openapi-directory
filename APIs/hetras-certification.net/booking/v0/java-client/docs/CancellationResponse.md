

# CancellationResponse

Result of cancel operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**warnings** | **List&lt;String&gt;** | Warnings that came up when your request was processed. Your request will still be processed successfull when              you see such warnings in your response |  [optional] |
|**balance** | **Double** | The current balance on the reservations folio without the cancellation fee |  [optional] |
|**cancellationFee** | **Double** | The fee that might be charged to the folio of the reservation. The cancelled reservation will              show up in the cancellation and no show processing screen and the hotel staff will either charge              the fee or waive it. |  [optional] |
|**cancellationId** | **String** | The id of the successful cancellation. With this id the hotel staff will be able to find the reservation |  [optional] |



