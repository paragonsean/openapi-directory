

# BillbeeInterfacesBillbeeAPIModelOrder

A class that represents the Billbee data model of a single order

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptLossOfReturnRight** | **Boolean** | Customer accepts loss due to withdrawal |  [optional] |
|**adjustmentCost** | **Double** |  |  [optional] |
|**adjustmentReason** | **String** |  |  [optional] |
|**apiAccountId** | **Long** | Id of the account, this order belongs to |  [optional] |
|**apiAccountName** | **String** | The name of the account, this order belongs to. Will be ignored on order creation. |  [optional] |
|**archivedAt** | **OffsetDateTime** | If set, the order was already archived at the given date. Further modification is disabled. |  [optional] |
|**billBeeOrderId** | **Long** | The Order.Id from the Billbee database |  [optional] |
|**billBeeParentOrderId** | **Long** | The Id of the parent order in the Billbee database |  [optional] |
|**buyer** | [**BillbeeInterfacesBillbeeAPIModelOrderUser**](BillbeeInterfacesBillbeeAPIModelOrderUser.md) |  |  [optional] |
|**comments** | [**List&lt;BillbeeInterfacesBillbeeAPIModelCommentApiModel&gt;**](BillbeeInterfacesBillbeeAPIModelCommentApiModel.md) | All messages / comments of the order |  [optional] |
|**confirmedAt** | **OffsetDateTime** | The date on which the order was confirmed |  [optional] |
|**createdAt** | **OffsetDateTime** | The date on which the order was created |  [optional] |
|**currency** | **String** | The three letter currency code. |  [optional] |
|**customInvoiceNote** | **String** | An optional multiline text which is printed on the invoice |  [optional] |
|**customer** | [**BillbeeInterfacesBillbeeAPIModelCustomerApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerApiModel.md) |  |  [optional] |
|**customerNumber** | **String** | The customer number (not to be confused with the id of the customer) |  [optional] |
|**customerVatId** | **String** | The vat-id, that was given by the customer to fulfill this order |  [optional] |
|**deliverySourceCountryCode** | **String** | An optional Country ISO2 Code of the country where order is shipped from (FBA) |  [optional] |
|**distributionCenter** | **String** | An optional code for the distribution center delivering this order |  [optional] |
|**history** | [**List&lt;BillbeeInterfacesOrderHistoryEntry&gt;**](BillbeeInterfacesOrderHistoryEntry.md) |  |  [optional] |
|**id** | **String** | Id of the order in the external system (marketplace) |  [optional] |
|**invoiceAddress** | [**BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel**](BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel.md) |  |  [optional] |
|**invoiceDate** | **OffsetDateTime** | The date on which the invoice was created |  [optional] |
|**invoiceNumber** | **Integer** | The invoice number |  [optional] |
|**invoiceNumberPostfix** | **String** | The postfix of the invoice number |  [optional] |
|**invoiceNumberPrefix** | **String** | The prefix of the invoice number |  [optional] |
|**isCancelationFor** | **String** | An optional Order Id (externalid) for an order if this is a cancel order (shopify only at the moment) |  [optional] |
|**isFromBillbeeApi** | **Boolean** | Indicates whether the order was created through the Billbee-Api or not. |  [optional] |
|**languageCode** | **String** | The two-letter language code of the customer |  [optional] |
|**lastModifiedAt** | **OffsetDateTime** | Date of the last update, the order got |  [optional] |
|**merchantVatId** | **String** | The vat-id, that should be displayed on the invoice and other order documents |  [optional] |
|**orderItems** | [**List&lt;BillbeeInterfacesBillbeeAPIModelOrderItem&gt;**](BillbeeInterfacesBillbeeAPIModelOrderItem.md) | The list of items purchased like shirt, pant, toys etc |  [optional] |
|**orderNumber** | **String** | Order number of the order in the external system (marketplace) |  [optional] |
|**paidAmount** | **Double** |  |  [optional] |
|**payedAt** | **OffsetDateTime** | The date on which the order was paid |  [optional] |
|**paymentInstruction** | **String** | A textfield optionaly filled with a payment instruction text for printout on the invoice (z.B. Ebay Kauf auf Rechnung) |  [optional] |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | The payment method |  [optional] |
|**paymentReference** | **String** | A payment reference. Should not be used any more. Please use &#39;Payments&#39; instead. |  [optional] |
|**paymentTransactionId** | **String** | The id of the payment transaction. For example the transaction id of PayPal payment. Should not be used any more. Please use &#39;Payments&#39; instead. |  [optional] |
|**payments** | [**List&lt;BillbeeInterfacesBillbeeAPIModelsOrderPayment&gt;**](BillbeeInterfacesBillbeeAPIModelsOrderPayment.md) |  |  [optional] |
|**rebateDifference** | **Double** |  |  [optional] [readonly] |
|**restoredAt** | **OffsetDateTime** | If set, the order was restored from the archive at the given date. |  [optional] |
|**seller** | [**BillbeeInterfacesBillbeeAPIModelOrderUser**](BillbeeInterfacesBillbeeAPIModelOrderUser.md) |  |  [optional] |
|**sellerComment** | **String** | An internal seller comment |  [optional] |
|**shipWeightKg** | **Double** | The total weight of the shipment(s) |  [optional] |
|**shippedAt** | **OffsetDateTime** | The date on which the order was shipped |  [optional] |
|**shippingAddress** | [**BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel**](BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel.md) |  |  [optional] |
|**shippingCost** | **Double** | The shipping cost |  [optional] |
|**shippingIds** | [**List&lt;BillbeeInterfacesBillbeeAPIModelShipment&gt;**](BillbeeInterfacesBillbeeAPIModelShipment.md) | The shipments of the order |  [optional] |
|**shippingProfileId** | **String** | Internal Id for the shipping profile for that order |  [optional] |
|**shippingProfileName** | **String** | Display Name of Shipping profile, if available |  [optional] |
|**shippingProviderId** | **Long** | Internal Id for the used shipping provider |  [optional] |
|**shippingProviderName** | **String** | The Name for of used shipping provider |  [optional] |
|**shippingProviderProductId** | **Long** | Internal Id for the used shipping product |  [optional] |
|**shippingProviderProductName** | **String** | The Name of the used shipping product |  [optional] |
|**shippingServices** | [**List&lt;BillbeeInterfacesShippingProductService&gt;**](BillbeeInterfacesShippingProductService.md) | Additional services for the shipment |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the order |  [optional] |
|**tags** | **List&lt;String&gt;** | The Tags of the order |  [optional] |
|**taxRate1** | **Double** | The regular tax rate |  [optional] |
|**taxRate2** | **Double** | The reduced tax rate |  [optional] |
|**totalCost** | **Double** | The total cost excluding shipping cost |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date on which the order was last updated |  [optional] |
|**vatId** | **String** | The customers vat id |  [optional] |
|**vatMode** | [**VatModeEnum**](#VatModeEnum) | The vat mode of the order |  [optional] |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_6 | 6 |
| NUMBER_19 | 19 |
| NUMBER_20 | 20 |
| NUMBER_21 | 21 |
| NUMBER_22 | 22 |
| NUMBER_23 | 23 |
| NUMBER_24 | 24 |
| NUMBER_25 | 25 |
| NUMBER_26 | 26 |
| NUMBER_27 | 27 |
| NUMBER_28 | 28 |
| NUMBER_29 | 29 |
| NUMBER_30 | 30 |
| NUMBER_31 | 31 |
| NUMBER_32 | 32 |
| NUMBER_33 | 33 |
| NUMBER_34 | 34 |
| NUMBER_35 | 35 |
| NUMBER_36 | 36 |
| NUMBER_37 | 37 |
| NUMBER_38 | 38 |
| NUMBER_39 | 39 |
| NUMBER_40 | 40 |
| NUMBER_41 | 41 |
| NUMBER_42 | 42 |
| NUMBER_43 | 43 |
| NUMBER_44 | 44 |
| NUMBER_45 | 45 |
| NUMBER_46 | 46 |
| NUMBER_47 | 47 |
| NUMBER_48 | 48 |
| NUMBER_49 | 49 |
| NUMBER_50 | 50 |
| NUMBER_51 | 51 |
| NUMBER_52 | 52 |
| NUMBER_53 | 53 |
| NUMBER_54 | 54 |
| NUMBER_55 | 55 |
| NUMBER_56 | 56 |
| NUMBER_57 | 57 |
| NUMBER_58 | 58 |
| NUMBER_59 | 59 |
| NUMBER_60 | 60 |
| NUMBER_61 | 61 |
| NUMBER_62 | 62 |
| NUMBER_63 | 63 |
| NUMBER_64 | 64 |
| NUMBER_65 | 65 |
| NUMBER_66 | 66 |
| NUMBER_67 | 67 |
| NUMBER_68 | 68 |
| NUMBER_69 | 69 |
| NUMBER_70 | 70 |
| NUMBER_71 | 71 |
| NUMBER_72 | 72 |
| NUMBER_73 | 73 |
| NUMBER_74 | 74 |
| NUMBER_75 | 75 |
| NUMBER_76 | 76 |
| NUMBER_77 | 77 |
| NUMBER_78 | 78 |
| NUMBER_79 | 79 |
| NUMBER_80 | 80 |
| NUMBER_81 | 81 |
| NUMBER_82 | 82 |
| NUMBER_83 | 83 |
| NUMBER_84 | 84 |
| NUMBER_85 | 85 |
| NUMBER_86 | 86 |
| NUMBER_87 | 87 |
| NUMBER_88 | 88 |
| NUMBER_89 | 89 |
| NUMBER_90 | 90 |
| NUMBER_91 | 91 |
| NUMBER_92 | 92 |
| NUMBER_93 | 93 |
| NUMBER_94 | 94 |
| NUMBER_95 | 95 |
| NUMBER_96 | 96 |
| NUMBER_97 | 97 |
| NUMBER_98 | 98 |
| NUMBER_99 | 99 |
| NUMBER_100 | 100 |
| NUMBER_101 | 101 |
| NUMBER_102 | 102 |
| NUMBER_103 | 103 |
| NUMBER_104 | 104 |
| NUMBER_105 | 105 |
| NUMBER_106 | 106 |
| NUMBER_107 | 107 |
| NUMBER_108 | 108 |
| NUMBER_109 | 109 |
| NUMBER_110 | 110 |
| NUMBER_111 | 111 |
| NUMBER_112 | 112 |
| NUMBER_113 | 113 |
| NUMBER_114 | 114 |
| NUMBER_115 | 115 |
| NUMBER_116 | 116 |
| NUMBER_117 | 117 |
| NUMBER_118 | 118 |
| NUMBER_119 | 119 |
| NUMBER_120 | 120 |
| NUMBER_121 | 121 |
| NUMBER_122 | 122 |
| NUMBER_123 | 123 |
| NUMBER_124 | 124 |
| NUMBER_125 | 125 |
| NUMBER_126 | 126 |
| NUMBER_127 | 127 |
| NUMBER_128 | 128 |
| NUMBER_129 | 129 |
| NUMBER_130 | 130 |
| NUMBER_131 | 131 |
| NUMBER_132 | 132 |
| NUMBER_133 | 133 |
| NUMBER_134 | 134 |
| NUMBER_135 | 135 |
| NUMBER_136 | 136 |
| NUMBER_137 | 137 |
| NUMBER_138 | 138 |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_8 | 8 |
| NUMBER_9 | 9 |
| NUMBER_10 | 10 |
| NUMBER_11 | 11 |
| NUMBER_12 | 12 |
| NUMBER_13 | 13 |
| NUMBER_14 | 14 |
| NUMBER_15 | 15 |
| NUMBER_16 | 16 |



## Enum: VatModeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |



