

# ExtendedOriginDestinationLight


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationLocationCode** | **String** | Destination location, such as a city or an airport. Currently, only the locations defined in [IATA](http://www.iata.org/publications/Pages/code-search.aspx) are supported. |  [optional] |
|**excludedConnectionPoints** | **List&lt;String&gt;** | List of excluded connections points. Any FlightOffer with these connections points will be present in response. Currently, only the locations defined in IATA are supported. Used only by the AMADEUS provider |  [optional] |
|**id** | **String** |  |  [optional] |
|**includedConnectionPoints** | **List&lt;String&gt;** | List of included connections points. When an includedViaPoints option is specified, all FlightOffer returned must at least go via this Connecting Point. Currently, only the locations defined in IATA are supported. Used only by the AMADEUS provider |  [optional] |
|**originLocationCode** | **String** | Origin location, such as a city or an airport. Currently, only the locations defined in [IATA](http://www.iata.org/publications/Pages/code-search.aspx) are supported. |  [optional] |
|**arrivalDateTime** | [**DateTimeType**](DateTimeType.md) |  |  [optional] |
|**departureDateTime** | [**DateTimeType**](DateTimeType.md) |  |  [optional] |



