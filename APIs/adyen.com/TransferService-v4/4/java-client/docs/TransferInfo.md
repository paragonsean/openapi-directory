

# TransferInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount of the transfer. |  |
|**balanceAccountId** | **String** | The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The type of transfer.  Possible values:   - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account.  - **internal**: Transfer to another [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) within your platform.  - **issuedCard**: Transfer initiated by a Adyen-issued card.  - **platformPayment**: Fund movements related to payments that are acquired for your users. |  |
|**counterparty** | [**CounterpartyInfoV3**](CounterpartyInfoV3.md) | The recipient of the funds transfer. A bank account, a balance account, or a transfer instrument is required. |  |
|**description** | **String** | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.  Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , &#39; + Space**  Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] &amp; $ % # @** **~ &#x3D; + - _ &#39; \&quot; ! ?** |  [optional] |
|**paymentInstrumentId** | **String** | The unique identifier of the source [payment instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments__resParam_id). |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with &#x60;category&#x60; **bank**.  Possible values:  * **regular**: For normal, low-value transactions.  * **fast**: Faster way to transfer funds but has higher fees. Recommended for high-priority, low-value transactions.  * **wire**: Fastest way to transfer funds but has the highest fees. Recommended for high-priority, high-value transactions.  * **instant**: Instant way to transfer funds in [SEPA countries](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  * **crossBorder**: High-value transfer to a recipient in a different country.  * **internal**: Transfer to an Adyen-issued business bank account (by bank account number/IBAN). |  [optional] |
|**reference** | **String** | Your reference for the transfer, used internally within your platform. If you don&#39;t provide this in the request, Adyen generates a unique reference. |  [optional] |
|**referenceForBeneficiary** | **String** |  A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.   Supported characters: **a-z**, **A-Z**, **0-9**. The maximum length depends on the &#x60;category&#x60;.  - **internal**: 80 characters  - **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |  [optional] |
|**ultimateParty** | [**UltimatePartyIdentification**](UltimatePartyIdentification.md) | The ultimate sender of the funds of the transfer (ultimate debtor). |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| INTERNAL | &quot;internal&quot; |
| ISSUED_CARD | &quot;issuedCard&quot; |
| PLATFORM_PAYMENT | &quot;platformPayment&quot; |
| CARD | &quot;card&quot; |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| CROSS_BORDER | &quot;crossBorder&quot; |
| FAST | &quot;fast&quot; |
| INSTANT | &quot;instant&quot; |
| INTERNAL | &quot;internal&quot; |
| REGULAR | &quot;regular&quot; |
| WIRE | &quot;wire&quot; |



