# SimplyRets.Property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **String** |  | [optional] 
**additionalRooms** | **String** | Additional room information. This is a textual description of additional rooms for the listing.  | [optional] 
**area** | **Number** | Square footage of the building associated with a listing | [optional] 
**areaSource** | **String** |  | [optional] 
**bathsFull** | **Number** | Number of full bathrooms | [optional] 
**bathsHalf** | **Number** | Number of half bathrooms | [optional] 
**bathsThreeQuarter** | **Number** | Number of 3/4 bathrooms | [optional] 
**bedrooms** | **Number** | Number of bedrooms | [optional] 
**construction** | **String** | The materials that were used in the construction of the property. | [optional] 
**cooling** | **String** | A description of the cooling or air conditioning features of the property. | [optional] 
**exteriorFeatures** | **String** | Exterior Features for the listing  | [optional] 
**fireplaces** | **Number** | Number of fireplaces | [optional] 
**flooring** | **String** | The type(s) of flooring found within the property. | [optional] 
**foundation** | **String** |  | [optional] 
**garageSpaces** | **Number** | Number of garage spaces | [optional] 
**heating** | **String** | Heating description or short string | [optional] 
**interiorFeatures** | **String** | The properties interior features | [optional] 
**laundryFeatures** | **String** |  | [optional] 
**lotDescription** | **String** |  | [optional] 
**lotSize** | **String** | Lot size dimensions or square footage as a text. This field is generally used to show the pretty formatted lot size.  | [optional] 
**lotSizeAcres** | **Number** | Lot size in acres  **Added on 2016/05/04 - Not available for all RETS vendors**  | [optional] 
**lotSizeArea** | **Number** | The total area of the lot.  See &#x60;lotSizeUnits&#x60; for the units of measurement (Square Feet, Square Meters, Acres, etc.).  **Added on 2016/05/04 - Not available for all RETS vendors**  | [optional] 
**lotSizeAreaUnits** | **String** | Unit of measurement for the lotSizeArea field.  e.g. Square Feet, Square Meters, Acres, etc.  If this field is &#x60;null&#x60; the units is the default unit of measure specified by your RETS provider.  **Added on 2016/05/04 - Not available for all RETS vendors**  | [optional] 
**maintenanceExpense** | **Number** | Yearly maintenance expense | [optional] 
**occupantName** | **String** |  | [optional] 
**occupantType** | **String** |  | [optional] 
**ownerName** | **String** |  | [optional] 
**parking** | [**Parking**](Parking.md) |  | [optional] 
**poolFeatures** | **String** |  | [optional] 
**roof** | **String** | Property roof description | [optional] 
**stories** | **Number** | Number of stories or levels. Represented as a &#x60;double&#39; to account for half stories.  | [optional] 
**style** | **String** | Property style description or short string | [optional] 
**subType** | **String** | A normalized representation of the listings sub-type.  | [optional] 
**subTypeRaw** | **String** | The raw text representation of the property sub type.  | [optional] 
**subdivision** | **String** | The subdivision or community name | [optional] 
**type** | **String** | Abbreviated property type. RES is Residential, CND is CondoOrTownhome, RNT is Rental, MLF is Multi-Family, CRE is Commercial, LND is Land, FRM is Farm. See the &#x60;propertySubType&#x60; field for more information.  | [optional] 
**view** | **String** | View details and description | [optional] 
**water** | **String** | The name, if known, of the body of water on which the property is located. (E.g., lake name, river name, ocean name, sea name, canal name). Otherwise, this field will contain features of the waterfront on which the property is located.  | [optional] 
**yearBuilt** | **Number** | Year the property was built | [optional] 



## Enum: SubTypeEnum


* `Apartment` (value: `"Apartment"`)

* `BoatSlip` (value: `"BoatSlip"`)

* `SingleFamilyResidence` (value: `"SingleFamilyResidence"`)

* `DeededParking` (value: `"DeededParking"`)

* `Cabin` (value: `"Cabin"`)

* `Condominium` (value: `"Condominium"`)

* `Duplex` (value: `"Duplex"`)

* `ManufacturedHome` (value: `"ManufacturedHome"`)

* `Quadruplex` (value: `"Quadruplex"`)

* `StockCooperative` (value: `"StockCooperative"`)

* `Townhouse` (value: `"Townhouse"`)

* `Timeshare` (value: `"Timeshare"`)

* `Triplex` (value: `"Triplex"`)

* `ManufacturedOnLand` (value: `"ManufacturedOnLand"`)





## Enum: TypeEnum


* `RES` (value: `"RES"`)

* `CND` (value: `"CND"`)

* `RNT` (value: `"RNT"`)

* `MLF` (value: `"MLF"`)

* `CRE` (value: `"CRE"`)

* `LND` (value: `"LND"`)

* `FRM` (value: `"FRM"`)




