

# StagedEmployeeAdditionalDirectDepositInner

The additional direct deposit model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | Account number, entered without special characters and spaces. &lt;br  /&gt;Max length: 17&lt;br /&gt; |  [optional] |
|**accountType** | **String** | Account type. Valid values are *C* (Checking), *S* (Saving), *P* (Pay Card). &lt;br   /&gt;Max length: 1&lt;br /&gt; |  [optional] |
|**amount** | **BigDecimal** | Amount value to be deposited to the account.&lt;br  /&gt;Decimal (12,2)&lt;br /&gt; |  [optional] |
|**amountType** | **String** | Amount type to indicate the context of the amount. Common values are *F* (FLAT), *F-* (Net Minus), *P* (Percent). &lt;br  /&gt; Max length: 5&lt;br /&gt; |  [optional] |
|**isSkipPreNote** | **Boolean** | Indicates if account will not pre-note.&lt;br /&gt; |  [optional] |
|**preNoteDate** | **String** | Date to end the pre-note of the account. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.&lt;br /&gt; |  [optional] |
|**routingNumber** | **String** | ABA Transit Routing Number, entered without dashes or spaces. &lt;br  /&gt;Max length: 9&lt;br /&gt; |  [optional] |



