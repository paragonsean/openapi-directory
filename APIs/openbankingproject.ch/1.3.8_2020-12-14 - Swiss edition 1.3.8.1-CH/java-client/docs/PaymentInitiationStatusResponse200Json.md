

# PaymentInitiationStatusResponse200Json

Body of the response for a successful payment initiation status request in case of an JSON based endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fundsAvailable** | **Boolean** | Equals true if sufficient funds are available at the time of the request, false otherwise.  This datalemenet is allways contained in a confirmation of funds response.  This data element is contained in a payment status response,  if supported by the ASPSP, if a funds check has been performed and  if the transactionStatus is \&quot;ACTC\&quot;, \&quot;ACWC\&quot; or \&quot;ACCP\&quot;.  |  [optional] |
|**psuMessage** | **String** | Text to be displayed to the PSU. |  [optional] |
|**transactionStatus** | **TransactionStatus** |  |  |



