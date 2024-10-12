

# VolumeSaleInfo

Any information about a volume related to the eBookstore and/or purchaseability. This information can depend on the country where the request originates from (i.e. books may not be for sale in certain countries).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buyLink** | **String** | URL to purchase this volume on the Google Books site. (In LITE projection) |  [optional] |
|**country** | **String** | The two-letter ISO_3166-1 country code for which this sale information is valid. (In LITE projection.) |  [optional] |
|**isEbook** | **Boolean** | Whether or not this volume is an eBook (can be added to the My eBooks shelf). |  [optional] |
|**listPrice** | [**VolumeSaleInfoListPrice**](VolumeSaleInfoListPrice.md) |  |  [optional] |
|**offers** | [**List&lt;VolumeSaleInfoOffersInner&gt;**](VolumeSaleInfoOffersInner.md) | Offers available for this volume (sales and rentals). |  [optional] |
|**onSaleDate** | **String** | The date on which this book is available for sale. |  [optional] |
|**retailPrice** | [**VolumeSaleInfoRetailPrice**](VolumeSaleInfoRetailPrice.md) |  |  [optional] |
|**saleability** | **String** | Whether or not this book is available for sale or offered for free in the Google eBookstore for the country listed above. Possible values are FOR_SALE, FOR_RENTAL_ONLY, FOR_SALE_AND_RENTAL, FREE, NOT_FOR_SALE, or FOR_PREORDER. |  [optional] |



