

# Property

Rets MLS Listing Property

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessibility** | **String** |  |  [optional] |
|**additionalRooms** | **String** | Additional room information. This is a textual description of additional rooms for the listing.  |  [optional] |
|**area** | **Long** | Square footage of the building associated with a listing |  [optional] |
|**areaSource** | **String** |  |  [optional] |
|**bathsFull** | **Long** | Number of full bathrooms |  [optional] |
|**bathsHalf** | **Long** | Number of half bathrooms |  [optional] |
|**bathsThreeQuarter** | **Long** | Number of 3/4 bathrooms |  [optional] |
|**bedrooms** | **Long** | Number of bedrooms |  [optional] |
|**construction** | **String** | The materials that were used in the construction of the property. |  [optional] |
|**cooling** | **String** | A description of the cooling or air conditioning features of the property. |  [optional] |
|**exteriorFeatures** | **String** | Exterior Features for the listing  |  [optional] |
|**fireplaces** | **Long** | Number of fireplaces |  [optional] |
|**flooring** | **String** | The type(s) of flooring found within the property. |  [optional] |
|**foundation** | **String** |  |  [optional] |
|**garageSpaces** | **Float** | Number of garage spaces |  [optional] |
|**heating** | **String** | Heating description or short string |  [optional] |
|**interiorFeatures** | **String** | The properties interior features |  [optional] |
|**laundryFeatures** | **String** |  |  [optional] |
|**lotDescription** | **String** |  |  [optional] |
|**lotSize** | **String** | Lot size dimensions or square footage as a text. This field is generally used to show the pretty formatted lot size.  |  [optional] |
|**lotSizeAcres** | **Float** | Lot size in acres  **Added on 2016/05/04 - Not available for all RETS vendors**  |  [optional] |
|**lotSizeArea** | **Double** | The total area of the lot.  See &#x60;lotSizeUnits&#x60; for the units of measurement (Square Feet, Square Meters, Acres, etc.).  **Added on 2016/05/04 - Not available for all RETS vendors**  |  [optional] |
|**lotSizeAreaUnits** | **String** | Unit of measurement for the lotSizeArea field.  e.g. Square Feet, Square Meters, Acres, etc.  If this field is &#x60;null&#x60; the units is the default unit of measure specified by your RETS provider.  **Added on 2016/05/04 - Not available for all RETS vendors**  |  [optional] |
|**maintenanceExpense** | **Float** | Yearly maintenance expense |  [optional] |
|**occupantName** | **String** |  |  [optional] |
|**occupantType** | **String** |  |  [optional] |
|**ownerName** | **String** |  |  [optional] |
|**parking** | [**Parking**](Parking.md) |  |  [optional] |
|**poolFeatures** | **String** |  |  [optional] |
|**roof** | **String** | Property roof description |  [optional] |
|**stories** | **Float** | Number of stories or levels. Represented as a &#x60;double&#39; to account for half stories.  |  [optional] |
|**style** | **String** | Property style description or short string |  [optional] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | A normalized representation of the listings sub-type.  |  [optional] |
|**subTypeRaw** | **String** | The raw text representation of the property sub type.  |  [optional] |
|**subdivision** | **String** | The subdivision or community name |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Abbreviated property type. RES is Residential, CND is CondoOrTownhome, RNT is Rental, MLF is Multi-Family, CRE is Commercial, LND is Land, FRM is Farm. See the &#x60;propertySubType&#x60; field for more information.  |  [optional] |
|**view** | **String** | View details and description |  [optional] |
|**water** | **String** | The name, if known, of the body of water on which the property is located. (E.g., lake name, river name, ocean name, sea name, canal name). Otherwise, this field will contain features of the waterfront on which the property is located.  |  [optional] |
|**yearBuilt** | **Long** | Year the property was built |  [optional] |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| APARTMENT | &quot;Apartment&quot; |
| BOAT_SLIP | &quot;BoatSlip&quot; |
| SINGLE_FAMILY_RESIDENCE | &quot;SingleFamilyResidence&quot; |
| DEEDED_PARKING | &quot;DeededParking&quot; |
| CABIN | &quot;Cabin&quot; |
| CONDOMINIUM | &quot;Condominium&quot; |
| DUPLEX | &quot;Duplex&quot; |
| MANUFACTURED_HOME | &quot;ManufacturedHome&quot; |
| QUADRUPLEX | &quot;Quadruplex&quot; |
| STOCK_COOPERATIVE | &quot;StockCooperative&quot; |
| TOWNHOUSE | &quot;Townhouse&quot; |
| TIMESHARE | &quot;Timeshare&quot; |
| TRIPLEX | &quot;Triplex&quot; |
| MANUFACTURED_ON_LAND | &quot;ManufacturedOnLand&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RES | &quot;RES&quot; |
| CND | &quot;CND&quot; |
| RNT | &quot;RNT&quot; |
| MLF | &quot;MLF&quot; |
| CRE | &quot;CRE&quot; |
| LND | &quot;LND&quot; |
| FRM | &quot;FRM&quot; |



