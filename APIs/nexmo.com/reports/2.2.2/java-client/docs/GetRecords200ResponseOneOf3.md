

# GetRecords200ResponseOneOf3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**ReportResponseTopLevelLinks**](ReportResponseTopLevelLinks.md) |  |  [optional] |
|**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. |  [optional] |
|**currency** | **String** | Currency of the price of the request. |  [optional] |
|**idsNotFound** | **String** | If you request multiple records using a comma-separated list of UUIDs, then the UUIDs of any records not found are listed in this field. |  [optional] |
|**price** | **String** | Price of the request. |  [optional] |
|**receivedAt** | **LocalDate** | Time at which the report request was received by the service. |  [optional] |
|**requestId** | **String** | UUID of the request. |  [optional] |
|**requestStatus** | **RequestStatus** |  |  [optional] |
|**itemsCount** | **Integer** | The number of returned records |  [optional] |
|**product** | **ProductInAppVoice** |  |  [optional] |
|**records** | [**List&lt;CsvInAppVoice&gt;**](CsvInAppVoice.md) | Records in JSON format |  [optional] |



