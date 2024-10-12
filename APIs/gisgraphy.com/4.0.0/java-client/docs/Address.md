

# Address


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**poBox** | **String** | Post office box, Boite postale, Casilla de Correo,... |  [optional] |
|**poBoxAgency** | **String** | Agency where the office box, Boite postale, Casilla de Correo is |  [optional] |
|**poBoxInfo** | **String** | extra info on post office box, Boite postale, Casilla de Correo,.. |  [optional] |
|**adm1NameAlternatesLocalized** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**adm2NameAlternatesLocalized** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**block** | **String** | The block in an address (Brasilia only) the block in austria, singapore,... address |  [optional] |
|**city** | **String** | The city or locality, a small town or village name sometimes is included in an address when the Delivery Point is outside the boundary of the main Post Town that serves it. |  [optional] |
|**citySubdivision** | **String** | A sub division of a city |  [optional] |
|**civicNumberSuffix** | **String** | The number that follows the house number (Canada only) |  [optional] |
|**confidence** | **String** | An indicator that mesure how the parser is confident for the result |  [optional] |
|**country** | **String** | The country name |  [optional] |
|**countryNameAlternatesLocalized** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**countrycode** | **String** | The countrycode given in the request |  [optional] |
|**dependentLocality** | **String** | &#39;Sub&#39; city atached to a big city |  [optional] |
|**distance** | **Double** | The distance of the address for the given parameter location in the query |  [optional] |
|**district** | **String** | The district, mainly use for Russia |  [optional] |
|**extraInfo** | **String** | Informations on floor, unit, and sometimes POBOX,... |  [optional] |
|**floor** | **String** | The floor in an address, not a floor number in a unit (Brasilia only) |  [optional] |
|**geocodinglevel** | [**GeocodinglevelEnum**](#GeocodinglevelEnum) |  |  [optional] |
|**houseNumber** | **String** | Official number assigned to an address by the municipality, several languages supported |  [optional] |
|**houseNumberInfo** | **String** | All information that give extra information on the house number |  [optional] |
|**id** | **Long** | An internal ID to identify the address |  [optional] |
|**lat** | **Double** | The latitude of the address |  [optional] |
|**lng** | **Double** | The longitude of the address |  [optional] |
|**lote** | **String** | Lote in Brazilian address |  [optional] |
|**name** | **String** | Name of the place, it is null in case of address but filled if common place. Name is different than recipient name |  [optional] |
|**nameAlternatesLocalized** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**postDirection** | **String** | The cardinal direction after the name of the street |  [optional] |
|**postDirectionIntersection** | **String** | The cardinal direction after the name of the intersection street |  [optional] |
|**postTown** | **String** | a city is a required part of all postal addresses in the United Kingdom |  [optional] |
|**preDirection** | **String** | The cardinal direction before the name of the street |  [optional] |
|**preDirectionIntersection** | **String** | The cardinal direction before the name of the intersection street |  [optional] |
|**prefecture** | **String** | prefecture of China |  [optional] |
|**quadrant** | **String** | The quadrant in an address (Brasilia only) |  [optional] |
|**quarter** | **String** | A section of an urban settlement |  [optional] |
|**recipientName** | **String** | Name of the organisation or person at the given address |  [optional] |
|**sector** | **String** | The sector in an address (Brasilia only) |  [optional] |
|**state** | **String** | The state or county when applicable, can be fullname or abbreviation |  [optional] |
|**streetName** | **String** | The official name of the street or the ordinal number |  [optional] |
|**streetNameIntersection** | **String** | The official name of the intersection street |  [optional] |
|**streetType** | **String** | The type of the street |  [optional] |
|**streetTypeIntersection** | **String** | The type of the intersection street |  [optional] |
|**suiteNumber** | **String** | Informations on the unit, mainly used and filled by standardizer |  [optional] |
|**suiteType** | **String** | Informations on the unit, mainly used and filled by standardizer |  [optional] |
|**ward** | **String** | Ward in japanese address |  [optional] |
|**zipCode** | **String** | The zip or post code |  [optional] |



## Enum: GeocodinglevelEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| HOUSE_NUMBER | &quot;HOUSE_NUMBER&quot; |
| STREET | &quot;STREET&quot; |
| CITY | &quot;CITY&quot; |
| STATE | &quot;STATE&quot; |
| COUNTRY | &quot;COUNTRY&quot; |



