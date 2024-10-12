

# BulkPaymentInitiationJson

Generic Body for a bulk payment initation via JSON.  paymentInformationId is contained in code but commented since it is n.a. and not all ASPSP are able to support this field now. In a later version the field will be mandatory. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchBookingPreferred** | **Boolean** | If this element equals &#39;true&#39;, the PSU prefers only one booking entry. If this element equals &#39;false&#39;, the PSU prefers individual booking of all contained individual transactions.  The ASPSP will follow this preference according to contracts agreed on with the PSU.  |  [optional] |
|**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**debtorAgent** | [**DebtorAgent7CH**](DebtorAgent7CH.md) |  |  |
|**payments** | [**List&lt;PaymentInitiationBulkElementJson&gt;**](PaymentInitiationBulkElementJson.md) | A list of generic JSON bodies payment initations for bulk payments via JSON.  Note: Some fields from single payments do not occcur in a bulk payment element  |  |
|**requestedExecutionDate** | **LocalDate** |  |  [optional] |
|**requestedExecutionTime** | **OffsetDateTime** |  |  [optional] |



