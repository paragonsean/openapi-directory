# SquareConnectApi.ListInvoicesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | When a response is truncated, it includes a cursor that you can use in a  subsequent request to retrieve the next set of invoices. If empty, this is the final  response.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
**errors** | [**[Error]**](Error.md) | Information about errors encountered during the request. | [optional] 
**invoices** | [**[Invoice]**](Invoice.md) | The invoices retrieved. | [optional] 


