# PaylocityApi.DirectDepositMainDirectDeposit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | Account number, entered without special characters and spaces. &lt;br  /&gt;Max length: 17 | [optional] 
**accountType** | **String** | Account type. Valid values are *C* (Checking), *S* (Saving), *P* (Pay Card). &lt;br   /&gt;Max length: 1 | [optional] 
**blockSpecial** | **Boolean** | Indicates if direct deposit should be blocked when special check types such as Bonus are processed.&lt;br /&gt; | [optional] 
**isSkipPreNote** | **Boolean** | Indicates if account will not pre-note. | [optional] 
**nameOnAccount** | **String** | Name on the bank account. Defaults to employee&#39;s name. &lt;br  /&gt;Max length: 30&lt;br /&gt; | [optional] 
**preNoteDate** | **String** | Date to end the pre-note of the account. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. | [optional] 
**routingNumber** | **String** | ABA Transit Routing Number, entered without dashes or spaces. &lt;br  /&gt;Max length: 9 | [optional] 


