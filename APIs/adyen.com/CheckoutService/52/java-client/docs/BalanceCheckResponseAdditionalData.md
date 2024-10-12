

# BalanceCheckResponseAdditionalData

Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardHolderInfo** | **String** | Information provided by the issuer to the cardholder. If this field is present, you need to display this information to the cardholder.  |  [optional] |
|**cavv** | **String** | The Cardholder Authentication Verification Value (CAVV) for the 3D Secure authentication session, as a Base64-encoded 20-byte array. |  [optional] |
|**cavvAlgorithm** | **String** | The CAVV algorithm used. |  [optional] |
|**scaExemptionRequested** | **String** | Shows the [exemption type](https://docs.adyen.com/payments-fundamentals/psd2-sca-compliance-and-implementation-guide#specifypreferenceinyourapirequest) that Adyen requested for the payment.   Possible values: * **lowValue**  * **secureCorporate**  * **trustedBeneficiary**  * **transactionRiskAnalysis**  |  [optional] |
|**threeds2CardEnrolled** | **Boolean** | Indicates whether a card is enrolled for 3D Secure 2. |  [optional] |
|**billingAddressCity** | **String** | The billing address city passed in the payment request. |  [optional] |
|**billingAddressCountry** | **String** | The billing address country passed in the payment request.  Example: NL |  [optional] |
|**billingAddressHouseNumberOrName** | **String** | The billing address house number or name passed in the payment request. |  [optional] |
|**billingAddressPostalCode** | **String** | The billing address postal code passed in the payment request.  Example: 1011 DJ |  [optional] |
|**billingAddressStateOrProvince** | **String** | The billing address state or province passed in the payment request.  Example: NH |  [optional] |
|**billingAddressStreet** | **String** | The billing address street passed in the payment request. |  [optional] |
|**cardBin** | **String** | The first six digits of the card number.  This is the [Bank Identification Number (BIN)](https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin) for card numbers with a six-digit BIN.  Example: 521234 |  [optional] |
|**cardHolderName** | **String** | The cardholder name passed in the payment request. |  [optional] |
|**cardIssuingBank** | **String** | The bank or the financial institution granting lines of credit through card association branded payment cards. This information can be included when available. |  [optional] |
|**cardIssuingCountry** | **String** | The country where the card was issued.  Example: US |  [optional] |
|**cardIssuingCurrency** | **String** | The currency in which the card is issued, if this information is available. Provided as the currency code or currency number from the ISO-4217 standard.   Example: USD |  [optional] |
|**cardPaymentMethod** | **String** | The card payment method used for the transaction.  Example: amex |  [optional] |
|**cardSummary** | **String** | The last four digits of a card number.  &gt; Returned only in case of a card payment. |  [optional] |
|**issuerBin** | **String** | The first eight digits of the card number. Only returned if the card number is 16 digits or more.  This is the [Bank Identification Number (BIN)](https://docs.adyen.com/get-started-with-adyen/payment-glossary#bank-identification-number-bin) for card numbers with an eight-digit BIN.  Example: 52123423 |  [optional] |
|**acquirerAccountCode** | **String** | The name of the Adyen acquirer account.  Example: PayPalSandbox_TestAcquirer  &gt; Only relevant for PayPal transactions. |  [optional] |
|**acquirerCode** | **String** | The name of the acquirer processing the payment request.  Example: TestPmmAcquirer |  [optional] |
|**acquirerReference** | **String** | The reference number that can be used for reconciliation in case a non-Adyen acquirer is used for settlement.  Example: 7C9N3FNBKT9 |  [optional] |
|**alias** | **String** | The Adyen alias of the card.  Example: H167852639363479 |  [optional] |
|**aliasType** | **String** | The type of the card alias.  Example: Default |  [optional] |
|**authCode** | **String** | Authorisation code: * When the payment is authorised successfully, this field holds the authorisation code for the payment. * When the payment is not authorised, this field is empty.  Example: 58747 |  [optional] |
|**authorisationMid** | **String** | Merchant ID known by the acquirer. |  [optional] |
|**authorisedAmountCurrency** | **String** | The currency of the authorised amount, as a three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |  [optional] |
|**authorisedAmountValue** | **String** | Value of the amount authorised.  This amount is represented in minor units according to the [following table](https://docs.adyen.com/development-resources/currency-codes). |  [optional] |
|**avsResult** | **String** | The AVS result code of the payment, which provides information about the outcome of the AVS check.  For possible values, see [AVS](https://docs.adyen.com/risk-management/configure-standard-risk-rules/consistency-rules#billing-address-does-not-match-cardholder-address-avs). |  [optional] |
|**avsResultRaw** | **String** | Raw AVS result received from the acquirer, where available.  Example: D |  [optional] |
|**bic** | **String** | BIC of a bank account.  Example: TESTNL01  &gt; Only relevant for SEPA Direct Debit transactions. |  [optional] |
|**coBrandedWith** | **String** | Includes the co-branded card information. |  [optional] |
|**cvcResult** | **String** | The result of CVC verification. |  [optional] |
|**cvcResultRaw** | **String** | The raw result of CVC verification. |  [optional] |
|**dsTransID** | **String** | Supported for 3D Secure 2. The unique transaction identifier assigned by the DS to identify a single transaction. |  [optional] |
|**eci** | **String** | The Electronic Commerce Indicator returned from the schemes for the 3DS payment session.  Example: 02 |  [optional] |
|**expiryDate** | **String** | The expiry date on the card.  Example: 6/2016  &gt; Returned only in case of a card payment. |  [optional] |
|**extraCostsCurrency** | **String** | The currency of the extra amount charged due to additional amounts set in the skin used in the HPP payment request.  Example: EUR |  [optional] |
|**extraCostsValue** | **String** | The value of the extra amount charged due to additional amounts set in the skin used in the HPP payment request. The amount is in minor units. |  [optional] |
|**fraudCheckItemNrFraudCheckname** | **String** | The fraud score due to a particular fraud check. The fraud check name is found in the key of the key-value pair. |  [optional] |
|**fraudManualReview** | **String** | Indicates if the payment is sent to manual review. |  [optional] |
|**fraudResultType** | [**FraudResultTypeEnum**](#FraudResultTypeEnum) | The fraud result properties of the payment. |  [optional] |
|**fundingSource** | **String** | Information regarding the funding type of the card. The possible return values are: * CHARGE * CREDIT * DEBIT * PREPAID * PREPAID_RELOADABLE  * PREPAID_NONRELOADABLE * DEFFERED_DEBIT  &gt; This functionality requires additional configuration on Adyen&#39;s end. To enable it, contact the Support Team.  For receiving this field in the notification, enable **Include Funding Source** in **Notifications** &gt; **Additional settings**. |  [optional] |
|**fundsAvailability** | **String** | Indicates availability of funds.  Visa: * \&quot;I\&quot; (fast funds are supported) * \&quot;N\&quot; (otherwise)  Mastercard: * \&quot;I\&quot; (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list) * \&quot;N\&quot; (otherwise)  &gt; Returned when you verify a card BIN or estimate costs, and only if payoutEligible is \&quot;Y\&quot; or \&quot;D\&quot;. |  [optional] |
|**inferredRefusalReason** | **String** | Provides the more granular indication of why a transaction was refused. When a transaction fails with either \&quot;Refused\&quot;, \&quot;Restricted Card\&quot;, \&quot;Transaction Not Permitted\&quot;, \&quot;Not supported\&quot; or \&quot;DeclinedNon Generic\&quot; refusalReason from the issuer, Adyen cross references its PSP-wide data for extra insight into the refusal reason. If an inferred refusal reason is available, the &#x60;inferredRefusalReason&#x60;, field is populated and the &#x60;refusalReason&#x60;, is set to \&quot;Not Supported\&quot;.  Possible values:  * 3D Secure Mandated * Closed Account * ContAuth Not Supported * CVC Mandated * Ecommerce Not Allowed * Crossborder Not Supported * Card Updated  * Low Authrate Bin * Non-reloadable prepaid card |  [optional] |
|**isCardCommercial** | **String** | Indicates if the card is used for business purposes only. |  [optional] |
|**issuerCountry** | **String** | The issuing country of the card based on the BIN list that Adyen maintains.  Example: JP |  [optional] |
|**liabilityShift** | **String** | A Boolean value indicating whether a liability shift was offered for this payment. |  [optional] |
|**mcBankNetReferenceNumber** | **String** | The &#x60;mcBankNetReferenceNumber&#x60;, is a minimum of six characters and a maximum of nine characters long.  &gt; Contact Support Team to enable this field. |  [optional] |
|**merchantAdviceCode** | **String** | The Merchant Advice Code (MAC) can be returned by Mastercard issuers for refused payments. If present, the MAC contains information about why the payment failed, and whether it can be retried.  For more information see [Mastercard Merchant Advice Codes](https://docs.adyen.com/development-resources/raw-acquirer-responses#mastercard-merchant-advice-codes). |  [optional] |
|**merchantReference** | **String** | The reference provided for the transaction. |  [optional] |
|**networkTxReference** | **String** | Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.  This contains either the Mastercard Trace ID or the Visa Transaction ID. |  [optional] |
|**nonSchemeTransactionLimit** | **String** | The maximum spendable value for a single transaction. Applicable to some gift cards. |  [optional] |
|**nonSchemeTransactionLimitCcy** | **String** | The currency of the transaction limit. |  [optional] |
|**ownerName** | **String** | The owner name of a bank account.  Only relevant for SEPA Direct Debit transactions. |  [optional] |
|**paymentAccountReference** | **String** | The Payment Account Reference (PAR) value links a network token with the underlying primary account number (PAN). The PAR value consists of 29 uppercase alphanumeric characters. |  [optional] |
|**paymentMethod** | **String** | The payment method used in the transaction. |  [optional] |
|**paymentMethodVariant** | **String** | The Adyen sub-variant of the payment method used for the payment request.  For more information, refer to [PaymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant).  Example: mcpro |  [optional] |
|**payoutEligible** | **String** | Indicates whether a payout is eligible or not for this card.  Visa: * \&quot;Y\&quot; * \&quot;N\&quot;  Mastercard: * \&quot;Y\&quot; (domestic and cross-border)  * \&quot;D\&quot; (only domestic) * \&quot;N\&quot; (no MoneySend) * \&quot;U\&quot; (unknown) |  [optional] |
|**realtimeAccountUpdaterStatus** | **String** | The response code from the Real Time Account Updater service.  Possible return values are: * CardChanged * CardExpiryChanged * CloseAccount  * ContactCardAccountHolder |  [optional] |
|**receiptFreeText** | **String** | Message to be displayed on the terminal. |  [optional] |
|**recurringContractTypes** | **String** | The recurring contract types applicable to the transaction. |  [optional] |
|**recurringFirstPspReference** | **String** | The &#x60;pspReference&#x60;, of the first recurring payment that created the recurring detail.  This functionality requires additional configuration on Adyen&#39;s end. To enable it, contact the Support Team. |  [optional] |
|**recurringRecurringDetailReference** | **String** | The reference that uniquely identifies the recurring transaction. |  [optional] |
|**recurringShopperReference** | **String** | The provided reference of the shopper for a recurring transaction. |  [optional] |
|**recurringProcessingModel** | [**RecurringProcessingModelEnum**](#RecurringProcessingModelEnum) | The processing model used for the recurring transaction. |  [optional] |
|**referred** | **String** | If the payment is referred, this field is set to true.  This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions.  Example: true |  [optional] |
|**refusalReasonRaw** | **String** | Raw refusal reason received from the acquirer, where available.  Example: AUTHORISED |  [optional] |
|**requestAmount** | **String** | The amount of the payment request. |  [optional] |
|**requestCurrencyCode** | **String** | The currency of the payment request. |  [optional] |
|**shopperInteraction** | **String** | The shopper interaction type of the payment request.  Example: Ecommerce |  [optional] |
|**shopperReference** | **String** | The shopperReference passed in the payment request.  Example: AdyenTestShopperXX |  [optional] |
|**terminalId** | **String** | The terminal ID used in a point-of-sale payment.  Example: 06022622 |  [optional] |
|**threeDAuthenticated** | **String** | A Boolean value indicating whether 3DS authentication was completed on this payment.  Example: true |  [optional] |
|**threeDAuthenticatedResponse** | **String** | The raw 3DS authentication result from the card issuer.  Example: N |  [optional] |
|**threeDOffered** | **String** | A Boolean value indicating whether 3DS was offered for this payment.  Example: true |  [optional] |
|**threeDOfferedResponse** | **String** | The raw enrollment result from the 3DS directory services of the card schemes.  Example: Y |  [optional] |
|**threeDSVersion** | **String** | The 3D Secure 2 version. |  [optional] |
|**visaTransactionId** | **String** | The &#x60;visaTransactionId&#x60;, has a fixed length of 15 numeric characters.  &gt; Contact Support Team to enable this field. |  [optional] |
|**xid** | **String** | The 3DS transaction ID of the 3DS session sent in notifications. The value is Base64-encoded and is returned for transactions with directoryResponse &#39;N&#39; or &#39;Y&#39;. If you want to submit the xid in your 3D Secure 1 request, use the &#x60;mpiData.xid&#x60;, field.  Example: ODgxNDc2MDg2MDExODk5MAAAAAA&#x3D; |  [optional] |
|**domesticRefusalReasonRaw** | **String** | The reason the transaction was declined, given by the local issuer.  Currently available for merchants in Japan. |  [optional] |
|**domesticShopperAdvice** | **String** | The action the shopper should take, in a local language.  Currently available in Japanese, for merchants in Japan. |  [optional] |
|**installmentPaymentDataInstallmentType** | **String** | Type of installment. The value of &#x60;installmentType&#x60; should be **IssuerFinanced**. |  [optional] |
|**installmentPaymentDataOptionItemNrAnnualPercentageRate** | **String** | Annual interest rate. |  [optional] |
|**installmentPaymentDataOptionItemNrFirstInstallmentAmount** | **String** | First Installment Amount in minor units. |  [optional] |
|**installmentPaymentDataOptionItemNrInstallmentFee** | **String** | Installment fee amount in minor units. |  [optional] |
|**installmentPaymentDataOptionItemNrInterestRate** | **String** | Interest rate for the installment period. |  [optional] |
|**installmentPaymentDataOptionItemNrMaximumNumberOfInstallments** | **String** | Maximum number of installments possible for this payment. |  [optional] |
|**installmentPaymentDataOptionItemNrMinimumNumberOfInstallments** | **String** | Minimum number of installments possible for this payment. |  [optional] |
|**installmentPaymentDataOptionItemNrNumberOfInstallments** | **String** | Total number of installments possible for this payment. |  [optional] |
|**installmentPaymentDataOptionItemNrSubsequentInstallmentAmount** | **String** | Subsequent Installment Amount in minor units. |  [optional] |
|**installmentPaymentDataOptionItemNrTotalAmountDue** | **String** | Total amount in minor units. |  [optional] |
|**installmentPaymentDataPaymentOptions** | **String** | Possible values: * PayInInstallmentsOnly * PayInFullOnly * PayInFullOrInstallments |  [optional] |
|**installmentsValue** | **String** | The number of installments that the payment amount should be charged with.  Example: 5 &gt; Only relevant for card payments in countries that support installments. |  [optional] |
|**networkTokenAvailable** | **String** | Indicates whether a network token is available for the specified card. |  [optional] |
|**networkTokenBin** | **String** | The Bank Identification Number of a tokenized card, which is the first six digits of a card number. |  [optional] |
|**networkTokenTokenSummary** | **String** | The last four digits of a network token. |  [optional] |
|**opiTransToken** | **String** | Returned in the response if you included &#x60;opi.includeTransToken: true&#x60; in an ecommerce payment request. This contains an Oracle Payment Interface token that you can store in your Oracle Opera database to identify tokenized ecommerce transactions. For more information and required settings, see [Oracle Opera](https://docs.adyen.com/plugins/oracle-opera#opi-token-ecommerce). |  [optional] |
|**sepadirectdebitDateOfSignature** | **String** | The transaction signature date.  Format: yyyy-MM-dd |  [optional] |
|**sepadirectdebitMandateId** | **String** | Its value corresponds to the pspReference value of the transaction. |  [optional] |
|**sepadirectdebitSequenceType** | **String** | This field can take one of the following values: * OneOff: (OOFF) Direct debit instruction to initiate exactly one direct debit transaction.  * First: (FRST) Initial/first collection in a series of direct debit instructions. * Recurring: (RCUR) Direct debit instruction to carry out regular direct debit transactions initiated by the creditor. * Final: (FNAL) Last/final collection in a series of direct debit instructions.  Example: OOFF |  [optional] |



## Enum: FraudResultTypeEnum

| Name | Value |
|---- | -----|
| GREEN | &quot;GREEN&quot; |
| FRAUD | &quot;FRAUD&quot; |



## Enum: RecurringProcessingModelEnum

| Name | Value |
|---- | -----|
| CARD_ON_FILE | &quot;CardOnFile&quot; |
| SUBSCRIPTION | &quot;Subscription&quot; |
| UNSCHEDULED_CARD_ON_FILE | &quot;UnscheduledCardOnFile&quot; |



