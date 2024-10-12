

# FindPlacesModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**admArea1** | **String** | first-level administrative area (a US state, for example) |  [optional] |
|**admArea2** | **String** | second-level administrative area (a US county, for example) |  [optional] |
|**country** | **String** | name of the country |  [optional] |
|**lat** | **String** | Latitude of the point, always in the format \\&lt;float&gt;&lt;N/S&gt;, for example &#x60;&#x60;23.5S&#x60;&#x60; |  [optional] |
|**lon** | **String** | Longitude of the point, always in format \\&lt;float&gt;&lt;E/W&gt;, for example &#x60;&#x60;23.5W&#x60;&#x60; |  [optional] |
|**name** | **String** | name of the place |  [optional] |
|**placeId** | **String** | unique identifier of the place, which can be used in /point and /map endpoints |  [optional] |
|**timezone** | **String** | Timezone of the point in tzinfo format. |  [optional] |
|**type** | **String** | The character of the place. May be one of the following values:  * administrative areas (states, counties, districts...): &#x60;&#x60;administrative_area&#x60;&#x60; * country: &#x60;&#x60;country&#x60;&#x60; * a different political entity from a country (for example, a dependent teritory): &#x60;&#x60;political_entity&#x60;&#x60; * villages, towns and cities: &#x60;&#x60;settlement&#x60;&#x60; * air industry locations: &#x60;&#x60;airbase&#x60;&#x60;, &#x60;&#x60;airfield&#x60;&#x60;, &#x60;&#x60;heliport&#x60;&#x60;, &#x60;&#x60;airport&#x60;&#x60;, &#x60;&#x60;airport_terminal&#x60;&#x60; * places related to water: &#x60;&#x60;bay&#x60;&#x60;, &#x60;&#x60;channel&#x60;&#x60;, &#x60;&#x60;fjord&#x60;&#x60;, &#x60;&#x60;lake&#x60;&#x60;, &#x60;&#x60;pond&#x60;&#x60;, &#x60;&#x60;falls&#x60;&#x60;, &#x60;&#x60;gulf&#x60;&#x60;,     &#x60;&#x60;harbor&#x60;&#x60;, &#x60;&#x60;reservoir&#x60;&#x60;, &#x60;&#x60;sea&#x60;&#x60;, &#x60;&#x60;dam&#x60;&#x60;, &#x60;&#x60;cape&#x60;&#x60;, &#x60;&#x60;island&#x60;&#x60;, &#x60;&#x60;peninsula&#x60;&#x60; * places related to mountain areas: &#x60;&#x60;hill&#x60;&#x60;, &#x60;&#x60;mountain&#x60;&#x60;, &#x60;&#x60;peak&#x60;&#x60;, &#x60;&#x60;valley&#x60;&#x60;, &#x60;&#x60;volcano&#x60;&#x60;, &#x60;&#x60;canyon&#x60;&#x60; * other places related to nature: &#x60;&#x60;park&#x60;&#x60;, &#x60;&#x60;reserve&#x60;&#x60;, &#x60;&#x60;resort&#x60;&#x60;, &#x60;&#x60;desert&#x60;&#x60; * places based on postcodes: &#x60;&#x60;postcode&#x60;&#x60;          |  [optional] |



