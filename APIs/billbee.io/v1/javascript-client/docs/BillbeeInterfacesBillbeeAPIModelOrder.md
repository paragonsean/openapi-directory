# BillbeeApi.BillbeeInterfacesBillbeeAPIModelOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptLossOfReturnRight** | **Boolean** | Customer accepts loss due to withdrawal | [optional] 
**adjustmentCost** | **Number** |  | [optional] 
**adjustmentReason** | **String** |  | [optional] 
**apiAccountId** | **Number** | Id of the account, this order belongs to | [optional] 
**apiAccountName** | **String** | The name of the account, this order belongs to. Will be ignored on order creation. | [optional] 
**archivedAt** | **Date** | If set, the order was already archived at the given date. Further modification is disabled. | [optional] 
**billBeeOrderId** | **Number** | The Order.Id from the Billbee database | [optional] 
**billBeeParentOrderId** | **Number** | The Id of the parent order in the Billbee database | [optional] 
**buyer** | [**BillbeeInterfacesBillbeeAPIModelOrderUser**](BillbeeInterfacesBillbeeAPIModelOrderUser.md) |  | [optional] 
**comments** | [**[BillbeeInterfacesBillbeeAPIModelCommentApiModel]**](BillbeeInterfacesBillbeeAPIModelCommentApiModel.md) | All messages / comments of the order | [optional] 
**confirmedAt** | **Date** | The date on which the order was confirmed | [optional] 
**createdAt** | **Date** | The date on which the order was created | [optional] 
**currency** | **String** | The three letter currency code. | [optional] 
**customInvoiceNote** | **String** | An optional multiline text which is printed on the invoice | [optional] 
**customer** | [**BillbeeInterfacesBillbeeAPIModelCustomerApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerApiModel.md) |  | [optional] 
**customerNumber** | **String** | The customer number (not to be confused with the id of the customer) | [optional] 
**customerVatId** | **String** | The vat-id, that was given by the customer to fulfill this order | [optional] 
**deliverySourceCountryCode** | **String** | An optional Country ISO2 Code of the country where order is shipped from (FBA) | [optional] 
**distributionCenter** | **String** | An optional code for the distribution center delivering this order | [optional] 
**history** | [**[BillbeeInterfacesOrderHistoryEntry]**](BillbeeInterfacesOrderHistoryEntry.md) |  | [optional] 
**id** | **String** | Id of the order in the external system (marketplace) | [optional] 
**invoiceAddress** | [**BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel**](BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel.md) |  | [optional] 
**invoiceDate** | **Date** | The date on which the invoice was created | [optional] 
**invoiceNumber** | **Number** | The invoice number | [optional] 
**invoiceNumberPostfix** | **String** | The postfix of the invoice number | [optional] 
**invoiceNumberPrefix** | **String** | The prefix of the invoice number | [optional] 
**isCancelationFor** | **String** | An optional Order Id (externalid) for an order if this is a cancel order (shopify only at the moment) | [optional] 
**isFromBillbeeApi** | **Boolean** | Indicates whether the order was created through the Billbee-Api or not. | [optional] 
**languageCode** | **String** | The two-letter language code of the customer | [optional] 
**lastModifiedAt** | **Date** | Date of the last update, the order got | [optional] 
**merchantVatId** | **String** | The vat-id, that should be displayed on the invoice and other order documents | [optional] 
**orderItems** | [**[BillbeeInterfacesBillbeeAPIModelOrderItem]**](BillbeeInterfacesBillbeeAPIModelOrderItem.md) | The list of items purchased like shirt, pant, toys etc | [optional] 
**orderNumber** | **String** | Order number of the order in the external system (marketplace) | [optional] 
**paidAmount** | **Number** |  | [optional] 
**payedAt** | **Date** | The date on which the order was paid | [optional] 
**paymentInstruction** | **String** | A textfield optionaly filled with a payment instruction text for printout on the invoice (z.B. Ebay Kauf auf Rechnung) | [optional] 
**paymentMethod** | **Number** | The payment method | [optional] 
**paymentReference** | **String** | A payment reference. Should not be used any more. Please use &#39;Payments&#39; instead. | [optional] 
**paymentTransactionId** | **String** | The id of the payment transaction. For example the transaction id of PayPal payment. Should not be used any more. Please use &#39;Payments&#39; instead. | [optional] 
**payments** | [**[BillbeeInterfacesBillbeeAPIModelsOrderPayment]**](BillbeeInterfacesBillbeeAPIModelsOrderPayment.md) |  | [optional] 
**rebateDifference** | **Number** |  | [optional] [readonly] 
**restoredAt** | **Date** | If set, the order was restored from the archive at the given date. | [optional] 
**seller** | [**BillbeeInterfacesBillbeeAPIModelOrderUser**](BillbeeInterfacesBillbeeAPIModelOrderUser.md) |  | [optional] 
**sellerComment** | **String** | An internal seller comment | [optional] 
**shipWeightKg** | **Number** | The total weight of the shipment(s) | [optional] 
**shippedAt** | **Date** | The date on which the order was shipped | [optional] 
**shippingAddress** | [**BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel**](BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel.md) |  | [optional] 
**shippingCost** | **Number** | The shipping cost | [optional] 
**shippingIds** | [**[BillbeeInterfacesBillbeeAPIModelShipment]**](BillbeeInterfacesBillbeeAPIModelShipment.md) | The shipments of the order | [optional] 
**shippingProfileId** | **String** | Internal Id for the shipping profile for that order | [optional] 
**shippingProfileName** | **String** | Display Name of Shipping profile, if available | [optional] 
**shippingProviderId** | **Number** | Internal Id for the used shipping provider | [optional] 
**shippingProviderName** | **String** | The Name for of used shipping provider | [optional] 
**shippingProviderProductId** | **Number** | Internal Id for the used shipping product | [optional] 
**shippingProviderProductName** | **String** | The Name of the used shipping product | [optional] 
**shippingServices** | [**[BillbeeInterfacesShippingProductService]**](BillbeeInterfacesShippingProductService.md) | Additional services for the shipment | [optional] 
**state** | **Number** | The current state of the order | [optional] 
**tags** | **[String]** | The Tags of the order | [optional] 
**taxRate1** | **Number** | The regular tax rate | [optional] 
**taxRate2** | **Number** | The reduced tax rate | [optional] 
**totalCost** | **Number** | The total cost excluding shipping cost | [optional] 
**updatedAt** | **Date** | The date on which the order was last updated | [optional] 
**vatId** | **String** | The customers vat id | [optional] 
**vatMode** | **Number** | The vat mode of the order | [optional] 



## Enum: PaymentMethodEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `6` (value: `6`)

* `19` (value: `19`)

* `20` (value: `20`)

* `21` (value: `21`)

* `22` (value: `22`)

* `23` (value: `23`)

* `24` (value: `24`)

* `25` (value: `25`)

* `26` (value: `26`)

* `27` (value: `27`)

* `28` (value: `28`)

* `29` (value: `29`)

* `30` (value: `30`)

* `31` (value: `31`)

* `32` (value: `32`)

* `33` (value: `33`)

* `34` (value: `34`)

* `35` (value: `35`)

* `36` (value: `36`)

* `37` (value: `37`)

* `38` (value: `38`)

* `39` (value: `39`)

* `40` (value: `40`)

* `41` (value: `41`)

* `42` (value: `42`)

* `43` (value: `43`)

* `44` (value: `44`)

* `45` (value: `45`)

* `46` (value: `46`)

* `47` (value: `47`)

* `48` (value: `48`)

* `49` (value: `49`)

* `50` (value: `50`)

* `51` (value: `51`)

* `52` (value: `52`)

* `53` (value: `53`)

* `54` (value: `54`)

* `55` (value: `55`)

* `56` (value: `56`)

* `57` (value: `57`)

* `58` (value: `58`)

* `59` (value: `59`)

* `60` (value: `60`)

* `61` (value: `61`)

* `62` (value: `62`)

* `63` (value: `63`)

* `64` (value: `64`)

* `65` (value: `65`)

* `66` (value: `66`)

* `67` (value: `67`)

* `68` (value: `68`)

* `69` (value: `69`)

* `70` (value: `70`)

* `71` (value: `71`)

* `72` (value: `72`)

* `73` (value: `73`)

* `74` (value: `74`)

* `75` (value: `75`)

* `76` (value: `76`)

* `77` (value: `77`)

* `78` (value: `78`)

* `79` (value: `79`)

* `80` (value: `80`)

* `81` (value: `81`)

* `82` (value: `82`)

* `83` (value: `83`)

* `84` (value: `84`)

* `85` (value: `85`)

* `86` (value: `86`)

* `87` (value: `87`)

* `88` (value: `88`)

* `89` (value: `89`)

* `90` (value: `90`)

* `91` (value: `91`)

* `92` (value: `92`)

* `93` (value: `93`)

* `94` (value: `94`)

* `95` (value: `95`)

* `96` (value: `96`)

* `97` (value: `97`)

* `98` (value: `98`)

* `99` (value: `99`)

* `100` (value: `100`)

* `101` (value: `101`)

* `102` (value: `102`)

* `103` (value: `103`)

* `104` (value: `104`)

* `105` (value: `105`)

* `106` (value: `106`)

* `107` (value: `107`)

* `108` (value: `108`)

* `109` (value: `109`)

* `110` (value: `110`)

* `111` (value: `111`)

* `112` (value: `112`)

* `113` (value: `113`)

* `114` (value: `114`)

* `115` (value: `115`)

* `116` (value: `116`)

* `117` (value: `117`)

* `118` (value: `118`)

* `119` (value: `119`)

* `120` (value: `120`)

* `121` (value: `121`)

* `122` (value: `122`)

* `123` (value: `123`)

* `124` (value: `124`)

* `125` (value: `125`)

* `126` (value: `126`)

* `127` (value: `127`)

* `128` (value: `128`)

* `129` (value: `129`)

* `130` (value: `130`)

* `131` (value: `131`)

* `132` (value: `132`)

* `133` (value: `133`)

* `134` (value: `134`)

* `135` (value: `135`)

* `136` (value: `136`)

* `137` (value: `137`)

* `138` (value: `138`)





## Enum: StateEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)

* `9` (value: `9`)

* `10` (value: `10`)

* `11` (value: `11`)

* `12` (value: `12`)

* `13` (value: `13`)

* `14` (value: `14`)

* `15` (value: `15`)

* `16` (value: `16`)





## Enum: VatModeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)




