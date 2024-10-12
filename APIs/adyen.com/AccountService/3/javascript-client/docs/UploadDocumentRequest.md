# AccountApi.UploadDocumentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder, for which the document is submitted. | [optional] 
**bankAccountUUID** | **String** | The unique ID of the bank account, for which the document is submitted. &gt;Required if the document is being submitted in order to verify a bank account. | [optional] 
**documentContent** | **String** | The content of the document, in Base64-encoded string format.  To learn about document requirements, refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks). | 
**documentDetail** | [**DocumentDetail**](DocumentDetail.md) | Details of the document being submitted. | 
**shareholderCode** | **String** | The code of the shareholder, for which the document is submitted. &gt;Required if the document is being submitted in order to verify a shareholder. | [optional] 


