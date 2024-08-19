# RePower.Repowerrequest1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalSenderInformation** | **String** |  Contains additional sender information in the Financial Transaction.The first 20 digits will be telephone number(n-20), the next 8 digits will be Date of Birth(n-8)(MMDDYYYY)and &#39;Check&#39; or &#39;Cash&#39; needs to be populated next based on check load or cash load.  Details- String, Min 32 characters, Max 65 characters in Length | [optional] 
**cardAcceptor** | [**Cardacceptor2**](Cardacceptor2.md) |  | [optional] 
**cardNumber** | **String** | Cardholder personal account number. Details- Numeric, 16 or 19, must pass LUHN MOD10 validation | 
**cardSequenceNumber** | **String** | Card Sequence Number as part of PaymentPOS Entry mode Integrated Circuit and contactless M/Chip. It must be present for EMV,MDES or PayPass transactions (where POS Entry Mode &#x3D; \&quot;05x\&quot; or \&quot;07x\&quot;). Details- Numeric, 3, The Possible values for Card Sequence Number are in the range 000–099 | [optional] 
**channel** | **String** | Origination channel for the rePower transaction as &#39;Attended POS&#39; (P) or &#39;Web&#39; (W).  Details- Alpha, 1, Constant P or W | 
**ICA** | **String** | ICA of acquiring institution. Details- Numeric, 4-6 | 
**iCCEMVData** | **String** | Integrated Circuit Card (ICC) System related data. It must be present for EMV(Including paypass/MDES EMV) transactions. Details- String, 255. Please refer section &#39;ICCEMVData&#39; for more details. | [optional] 
**localDate** | **String** | This is the local date for the location where the request is originating. Details- Numeric, 4, MMDD | 
**localTime** | **String** |  This is the local time for the location where the request is originating. The format is military or twenty-four hour clock time. Details- Numeric, HHMMSS | 
**merchantType** | **String** | Merchant&#39;s type of business or Service will be represented as a member financial institution initiated rePower transaction (6532), or merchant initiated rePower transaction (6533). Details- Numeric, 4, constant 6532 or 6533 | 
**pOSCardDataTerminalInputCapabilityIndicator** | **String** | Point of Service (POS) card data terminal input capability indicator. It must be present for EMV,MDES or PayPass transactions (where POS Entry Mode &#x3D; \&quot;05x\&quot; or \&quot;07x\&quot; or \&quot;91x\&quot;). Details- Conditional, numeric, 1, The Possible values for POS card data terminal input capability indicator is 3 or 4. | [optional] 
**paymentInitiationChannel** | **String** | Payment Initiation Channel is the device type used to identify mobile-initiated (m-commerce) or other non-card device initiated transactions. It&#39;s an option field for paypass transactions. Details-  Numeric, 2 digits. The possible values for Payment Initiation Channel is detailed out in section &#39;PaymentInitiationChannel&#39; | [optional] 
**paymentPosEntryMode** | **String** | PaymentPos Entry Mode to represent the POS Terminal PAN Entry Mode &amp; Terminal PIN Entry Mode. This is required for EMV transactions and Paypass/MDES magstripe transactions. The first two digits indicate PAN entry mode and the last digit indicate PIN entry mode. Details- Numeric, 3. For PAN/PIN Entry mode details refer section &#39;PaymentPosEntryMode&#39; | [optional] 
**processorId** | **String** | Processor Id. Details- Numeric, 10 | 
**receiverTrack2Data** | **String** | Contains 8 sub fields to enhance the repower API to support EMV scripting data fields.It must be present for EMV, MDES or PayPass transactions(where POS Entry Mode is other than 010 or 011 or 012). Details- Conditional, String, Max 37 characters in Length. Refer section &#39;ReceiverTrack2Data&#39; | [optional] 
**routingAndTransitNumber** | **String** | Routing and Transit number. Details- Numeric, 9 | 
**transactionAmount** | [**Transactionamount3**](Transactionamount3.md) |  | [optional] 
**transactionFee** | [**Transactionfee4**](Transactionfee4.md) |  | [optional] 
**transactionReference** | **String** | Repower Transaction Reference Number. Provided by the Client submitting the rePower transfer request. Must be \&quot;unique\&quot; across all rePower transfer requests. Details- Numeric, length 19 | 


