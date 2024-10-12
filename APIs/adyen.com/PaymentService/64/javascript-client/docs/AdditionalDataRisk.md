# AdyenPaymentApi.AdditionalDataRisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**riskdataCustomFieldName** | **String** | The data for your custom risk field. For more information, refer to [Create custom risk fields](https://docs.adyen.com/risk-management/configure-custom-risk-rules#step-1-create-custom-risk-fields). | [optional] 
**riskdataBasketItemItemNrAmountPerItem** | **String** | The price of item in the basket, represented in [minor units](https://docs.adyen.com/development-resources/currency-codes). | [optional] 
**riskdataBasketItemItemNrBrand** | **String** | Brand of the item. | [optional] 
**riskdataBasketItemItemNrCategory** | **String** | Category of the item. | [optional] 
**riskdataBasketItemItemNrColor** | **String** | Color of the item. | [optional] 
**riskdataBasketItemItemNrCurrency** | **String** | The three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). | [optional] 
**riskdataBasketItemItemNrItemID** | **String** | ID of the item. | [optional] 
**riskdataBasketItemItemNrManufacturer** | **String** | Manufacturer of the item. | [optional] 
**riskdataBasketItemItemNrProductTitle** | **String** | A text description of the product the invoice line refers to. | [optional] 
**riskdataBasketItemItemNrQuantity** | **String** | Quantity of the item purchased. | [optional] 
**riskdataBasketItemItemNrReceiverEmail** | **String** | Email associated with the given product in the basket (usually in electronic gift cards). | [optional] 
**riskdataBasketItemItemNrSize** | **String** | Size of the item. | [optional] 
**riskdataBasketItemItemNrSku** | **String** | [Stock keeping unit](https://en.wikipedia.org/wiki/Stock_keeping_unit). | [optional] 
**riskdataBasketItemItemNrUpc** | **String** | [Universal Product Code](https://en.wikipedia.org/wiki/Universal_Product_Code). | [optional] 
**riskdataPromotionsPromotionItemNrPromotionCode** | **String** | Code of the promotion. | [optional] 
**riskdataPromotionsPromotionItemNrPromotionDiscountAmount** | **String** | The discount amount of the promotion, represented in [minor units](https://docs.adyen.com/development-resources/currency-codes). | [optional] 
**riskdataPromotionsPromotionItemNrPromotionDiscountCurrency** | **String** | The three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). | [optional] 
**riskdataPromotionsPromotionItemNrPromotionDiscountPercentage** | **String** | Promotion&#39;s percentage discount. It is represented in percentage value and there is no need to include the &#39;%&#39; sign.  e.g. for a promotion discount of 30%, the value of the field should be 30. | [optional] 
**riskdataPromotionsPromotionItemNrPromotionName** | **String** | Name of the promotion. | [optional] 
**riskdataRiskProfileReference** | **String** | Reference number of the risk profile that you want to apply to the payment. If not provided or left blank, the merchant-level account&#39;s default risk profile will be applied to the payment. For more information, see [dynamically assign a risk profile to a payment](https://docs.adyen.com/risk-management/create-and-use-risk-profiles#dynamically-assign-a-risk-profile-to-a-payment). | [optional] 
**riskdataSkipRisk** | **String** | If this parameter is provided with the value **true**, risk checks for the payment request are skipped and the transaction will not get a risk score. | [optional] 


