

# Repower5

Response details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountBalance** | [**Accountbalance9**](Accountbalance9.md) |  |  [optional] |
|**icCEMVData** | **String** |  Integrated Circuit Card (ICC) System related data. It must be present for EMV transactions. Required DE 55 Subelements in /0200 and /0220 Messages. Details- Conditional, String, 255 |  [optional] |
|**paNMappingFileInformation** | **String** | PAN Mapping File Information will be avalable when the PAN is MDES token. Details- Conditional, String, 33 |  [optional] |
|**personPresentIndicator** | **String** | Person Present Indicator values is populated in repower response. Where the repower requests are  a. PaymentPosEntryMode (07*_/09*)  b. CardSequenceNumber &gt; 0  c. Transaction Amount &gt; 0 It is a number value and size 2 digit |  [optional] |
|**requestId** | **String** | This is the unique identifier for API Web service request. Details- Numeric value, variable length between 1 and 19 digits, without zero padding |  [optional] |
|**transactionHistory** | [**Transactionhistory6**](Transactionhistory6.md) |  |  [optional] |
|**transactionReference** | **String** | This value represents the unique reference number for the rePower transaction provided by the merchant or acquiring institution. Details- Alphanumeric value, 19 |  [optional] |



