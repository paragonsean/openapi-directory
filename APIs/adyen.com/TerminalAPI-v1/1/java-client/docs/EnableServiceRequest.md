

# EnableServiceRequest

It conveys the services that will be enabled for the  POI Terminal without the request of the Sale System, and a possible invitation for the Customer to start the services. Content of the Enable Service Request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayOutput** | [**DisplayOutput**](DisplayOutput.md) |  |  [optional] |
|**servicesEnabled** | [**List&lt;ServicesEnabledEnum&gt;**](#List&lt;ServicesEnabledEnum&gt;) |  |  [optional] |
|**transactionAction** | **TransactionAction** |  |  |



## Enum: List&lt;ServicesEnabledEnum&gt;

| Name | Value |
|---- | -----|
| CARD_ACQUISITION | &quot;CardAcquisition&quot; |
| LOYALTY | &quot;Loyalty&quot; |
| PAYMENT | &quot;Payment&quot; |



