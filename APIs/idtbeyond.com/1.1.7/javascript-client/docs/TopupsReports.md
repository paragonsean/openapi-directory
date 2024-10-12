# ActiveDocumentationForV1.TopupsReports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientTransactionId** | **String** | The UNIQUE 15 char ID used to track topups. &#39;trans0123456789&#39; | [optional] [default to &#39;trans0123456789&#39;]
**dateFrom** | **String** | The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). Not used in query by to_service_number. &#39;2016-01-28&#39; | [optional] [default to &#39;2016-01-28&#39;]
**dateTo** | **String** | The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). Not used in query by to_service_number. &#39;2016-01-28&#39; | [optional] [default to &#39;2016-01-28&#39;]
**toServiceNumber** | **String** | Enter the to_service_number returned in the response to track the current transaction status. &#39;0123456789&#39; | [optional] [default to &#39;123456789&#39;]
**typeOfReport** | **String** | The type of query you would like to search by. | [optional] [default to &#39;client_transaction_id or to_service_number&#39;]


