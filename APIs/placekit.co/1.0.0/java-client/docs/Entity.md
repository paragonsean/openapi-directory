

# Entity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administrative** | **String** | Administrative name (region). |  [optional] |
|**city** | **String** | City name. |  [optional] |
|**country** | **String** | Country name. |  [optional] |
|**countrycode** | **String** | [Two-letter ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).  |  [optional] |
|**county** | **String** | County name (department). |  [optional] |
|**highlight** | **String** | Name of the current entity with highlighted matched words. |  [optional] |
|**lat** | **BigDecimal** | Latitude. |  [optional] |
|**lng** | **BigDecimal** | Longitude. |  [optional] |
|**name** | **String** | Name of the current entity. |  [optional] |
|**population** | **Integer** | Population number of the entity city. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the entity. |  [optional] |
|**zipcode** | **List&lt;String&gt;** | Postcodes associated with the entity. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AIRPORT | &quot;airport&quot; |
| BUS | &quot;bus&quot; |
| CITY | &quot;city&quot; |
| COUNTRY | &quot;country&quot; |
| STREET | &quot;street&quot; |
| TOURISM | &quot;tourism&quot; |
| TOWNHALL | &quot;townhall&quot; |
| TRAIN | &quot;train&quot; |



