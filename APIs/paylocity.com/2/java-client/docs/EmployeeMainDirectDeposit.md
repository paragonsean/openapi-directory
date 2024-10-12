

# EmployeeMainDirectDeposit

Add the main direct deposit account. After deposits are made to any additional direct deposit accounts, the remaining net check is deposited in the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with what is provided on the request. GET API will not return direct deposit data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | Account number, entered without special characters and spaces. &lt;br  /&gt;Max length: 17 |  [optional] |
|**accountType** | **String** | Account type. Valid values are *C* (Checking), *S* (Saving), *P* (Pay Card). &lt;br   /&gt;Max length: 1 |  [optional] |
|**blockSpecial** | **Boolean** | Indicates if direct deposit should be blocked when special check types such as Bonus are processed.&lt;br /&gt; |  [optional] |
|**isSkipPreNote** | **Boolean** | Indicates if account will not pre-note. |  [optional] |
|**nameOnAccount** | **String** | Name on the bank account. Defaults to employee&#39;s name. &lt;br  /&gt;Max length: 30&lt;br /&gt; |  [optional] |
|**preNoteDate** | **String** | Date to end the pre-note of the account. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**routingNumber** | **String** | ABA Transit Routing Number, entered without dashes or spaces. &lt;br  /&gt;Max length: 9 |  [optional] |



