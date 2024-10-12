# TransfersApi.TransferInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount of the transfer. | 
**balanceAccountId** | **String** | The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). | [optional] 
**bank** | [**Bank**](Bank.md) | Contains settings for bank transfers. If you are transferring funds to bank accounts and you don&#39;t provide this object, Adyen applies default settings. | [optional] 
**counterparty** | [**CounterpartyInfo**](CounterpartyInfo.md) | The recipient of the funds transfer. A bank account, a balance account, or a transfer instrument is required. | 
**description** | **String** | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.  Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , &#39; + Space**  Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] &amp; $ % # @** **~ &#x3D; + - _ &#39; \&quot; ! ?** | [optional] 
**paymentInstrumentId** | **String** | The unique identifier of the source [payment instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments__resParam_id). | [optional] 
**reference** | **String** | Your reference for the transfer, used internally within your platform. If you don&#39;t provide this in the request, Adyen generates a unique reference. | [optional] 
**referenceForBeneficiary** | **String** |  A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.   Supported characters: **a-z**, **A-Z**, **0-9**. Maximum length: 80 characters. | [optional] 


