# ContentApiForShopping.SettlementReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endDate** | **String** | The end date on which all transactions are included in the report, in ISO 8601 format. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#settlementReport&#x60;\&quot; | [optional] 
**previousBalance** | [**Price**](Price.md) |  | [optional] 
**settlementId** | **String** | The ID of the settlement report. | [optional] 
**startDate** | **String** | The start date on which all transactions are included in the report, in ISO 8601 format. | [optional] 
**transferAmount** | [**Price**](Price.md) |  | [optional] 
**transferDate** | **String** | Date on which transfer for this payment was initiated by Google, in ISO 8601 format. | [optional] 
**transferIds** | **[String]** | The list of bank identifiers used for the transfer. For example, Trace ID for Federal Automated Clearing House (ACH). This may also be known as the Wire ID. | [optional] 


