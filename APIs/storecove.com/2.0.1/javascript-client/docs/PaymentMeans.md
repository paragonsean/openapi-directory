# StorecoveApi.PaymentMeans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | The account number. | [optional] 
**amount** | **Number** | The amount to be paid for this category. Only used for Dutch G-Account invoices. The amount nl_ga_beneficiary + amount nl_ga_gaccount must add up to the amountExcludingVat | [optional] 
**brancheCode** | **String** | The bank branch code. Not required for IBAN numbers. Often referred to as Swift or Bic code. | [optional] 
**code** | **String** | How the invoice has been / will be paid. The code determines which type of PaymentMeans is used and which fields are mandatory. ++++ &lt;ul&gt;    &lt;li&gt;        &lt;strong&gt;cash&lt;/strong&gt;&lt;br/&gt;        The invoice was/is paid in cash.&lt;br/&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;bank_cheque&lt;/strong&gt;&lt;br/&gt;        The invoice was/is paid via a bank cheque.&lt;br/&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;cashiers_cheque&lt;/strong&gt;&lt;br/&gt;        The invoice was/is paid via a cashiers cheque.&lt;br/&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;credit_transfer&lt;/strong&gt;&lt;br/&gt;        The amount is to be transfered into a bank account. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The account number. For New Zealand, this should hold the full 16 digit bank account number. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;branche_code&lt;/strong&gt;&lt;br/&gt;                In case of an IBAN, the account alone number is sufficient. In other cases, like a BBAN, a BIC code or other additional identifier is required. For Australia, the BSB goes here. Optional.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;debit_transfer&lt;/strong&gt;&lt;br/&gt;        Used for CreditNotes. The amount is to be transfered by the sender of the document into the bank account of the receiver of the document. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The account number. For New Zealand, this should hold the full 16 digit bank account number. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;branche_code&lt;/strong&gt;&lt;br/&gt;                In case of an IBAN, the account alone number is sufficient. In other cases, like a BBAN, a BIC code or other additional identifier is required. For Australia, the BSB goes here. Optional.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;direct_debit&lt;/strong&gt;&lt;br/&gt;        Direct debit. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The account number from which the funds will be debited. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;mandate&lt;/strong&gt;&lt;br/&gt;                The direct debit mandate id. Mandatory.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;card, credit_card, bank_card (credit_card, bank_card are deprecated)&lt;/strong&gt;&lt;br/&gt;        E.g. credit or debit card. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The card number, but never more than the last four digits. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;network&lt;/strong&gt;&lt;br/&gt;                The payment network, e.g. VISA, SEPA. Optional, but recommended since a default of \&quot;N/A\&quot; may be used if not provided.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;online_payment_service&lt;/strong&gt;&lt;br/&gt;        An online payment service has been or will be used. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;network&lt;/strong&gt;&lt;br/&gt;                The payment network, e.g. PayPal. &lt;strong&gt;Mandatory unless url is provided&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;url&lt;/strong&gt;&lt;br/&gt;                The URL to execute the payment. &lt;strong&gt;Mandatory unless network is provided&lt;/strong&gt;.            &lt;/li&gt;        &lt;/ul&gt;        It is possible to provide both url and network. Note that for UBL, in countries where this payment means is not allowed, this will translate into an AdditionalDocumentReference.Attachment.ExternalReference element.    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;standing_agreement&lt;/strong&gt;&lt;br/&gt;        The payment means has been agreed out of band. Relevant additional fields: none.    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;aunz_npp_payid, aunz_npp (aunz_npp is deprecated)&lt;/strong&gt;&lt;br/&gt;        Australia/New Zealand New Payments Platform. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                PayID. May be an email address, ABN, mobile phone number etc. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;aunz_npp_payto&lt;/strong&gt;&lt;br/&gt;        Australia/New Zealand New Payments Platform. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                Account number. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;mandate&lt;/strong&gt;&lt;br/&gt;                Mandate/direct debit authority reference/PayTo Agreement. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;aunz_bpay&lt;/strong&gt;&lt;br/&gt;        Australia/New Zealand New Payments Platform. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                Biller code. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;aunz_postbillpay&lt;/strong&gt;&lt;br/&gt;        Australia/New Zealand New Payments Platform. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                Biller code. &lt;strong&gt;Mandatory.&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;aunz_uri&lt;/strong&gt;&lt;br/&gt;        Australia/New Zealand URI. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                Payment URI. &lt;strong&gt;Mandatory.&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;se_bankgiro&lt;/strong&gt;&lt;br/&gt;        Swedish Bankgiro. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The account number from which the funds will be debited, 7 or 8 digits. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;        &lt;br/&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;se_plusgiro&lt;/strong&gt;&lt;br/&gt;        Swedish Plusgiro. Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The account number from which the funds will be debited, 2 - 8 digits. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;            &lt;li&gt;                &lt;strong&gt;holder&lt;/strong&gt;&lt;br/&gt;                The account holder name. Optional.            &lt;/li&gt;        &lt;/ul&gt;        &lt;br/&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;sg_giro&lt;/strong&gt;&lt;br/&gt;        Singapore GIRO-system (direct debit). Relevant additional fields: none.    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;sg_card&lt;/strong&gt;&lt;br/&gt;        Singapore CreditCard payment. Relevant additional fields: none.    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;sg_paynow&lt;/strong&gt;&lt;br/&gt;        Singapore PayNow Corporate.  Relevant additional fields:&lt;br/&gt;        &lt;ul&gt;            &lt;li&gt;                &lt;strong&gt;account&lt;/strong&gt;&lt;br/&gt;                The UEN, format: UENxxxxxxxxxx. &lt;strong&gt;Mandatory&lt;/strong&gt;.            &lt;/li&gt;        &lt;/ul&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;it_mav&lt;/strong&gt;&lt;br/&gt;        Italy MAV payment.    &lt;/li&gt;    &lt;li&gt;        &lt;strong&gt;it_pagopa&lt;/strong&gt;&lt;br/&gt;        Italy PagoPA payment.    &lt;/li&gt;&lt;/ul&gt; ++++  | 
**holder** | **String** | The name of the account holder. | [optional] 
**mandate** | **String** | The direct debit mandate code. | [optional] 
**network** | **String** | The name of the card network, e.g. VISA. | [optional] 
**paymentId** | **String** | The payment id that you will use to match the payment against the invoice. | [optional] 



## Enum: CodeEnum


* `credit_transfer` (value: `"credit_transfer"`)

* `debit_transfer` (value: `"debit_transfer"`)

* `direct_debit` (value: `"direct_debit"`)

* `card` (value: `"card"`)

* `bank_card` (value: `"bank_card"`)

* `credit_card` (value: `"credit_card"`)

* `online_payment_service` (value: `"online_payment_service"`)

* `cash` (value: `"cash"`)

* `bank_cheque` (value: `"bank_cheque"`)

* `cashiers_cheque` (value: `"cashiers_cheque"`)

* `standing_agreement` (value: `"standing_agreement"`)

* `aunz_npp` (value: `"aunz_npp"`)

* `aunz_npp_payid` (value: `"aunz_npp_payid"`)

* `aunz_npp_payto` (value: `"aunz_npp_payto"`)

* `aunz_bpay` (value: `"aunz_bpay"`)

* `aunz_postbillpay` (value: `"aunz_postbillpay"`)

* `aunz_uri` (value: `"aunz_uri"`)

* `se_bankgiro` (value: `"se_bankgiro"`)

* `se_plusgiro` (value: `"se_plusgiro"`)

* `sg_giro` (value: `"sg_giro"`)

* `sg_card` (value: `"sg_card"`)

* `sg_paynow` (value: `"sg_paynow"`)

* `it_mav` (value: `"it_mav"`)

* `it_pagopa` (value: `"it_pagopa"`)

* `nl_ga_beneficiary` (value: `"nl_ga_beneficiary"`)

* `nl_ga_gaccount` (value: `"nl_ga_gaccount"`)

* `undefined` (value: `"undefined"`)




