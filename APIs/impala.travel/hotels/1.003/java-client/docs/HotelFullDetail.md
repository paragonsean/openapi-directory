

# HotelFullDetail

Full details on a hotel, including its room types and available rates

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  |
|**amenities** | [**List&lt;Amenity&gt;**](Amenity.md) |  |  |
|**checkIn** | [**TimeRange**](TimeRange.md) |  |  |
|**checkOut** | [**TimeRange**](TimeRange.md) |  |  |
|**contractable** | **Boolean** | This determines if you can negotiate directly with the hotel.  |  |
|**createdAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the hotel&#39;s stable content (i.e. all the details of the hotel excluding its rates) was created. |  [optional] |
|**currency** | **String** | The standard currency code used by the hotel. |  |
|**description** | [**HotelFullDetailDescription**](HotelFullDetailDescription.md) |  |  [optional] |
|**emails** | **List&lt;String&gt;** |  |  |
|**externalUrls** | [**List&lt;ExternalUrl&gt;**](ExternalUrl.md) |  |  |
|**hotelId** | **UUID** | Unique identifier for this hotel within the Impala platform. |  |
|**images** | [**List&lt;Image&gt;**](Image.md) | Photos of the hotel, sorted in the recommended display order (e.g. for photo galleries) starting with the recommended hero image. |  |
|**location** | [**Location**](Location.md) |  |  |
|**name** | **String** | Name of the hotel. |  |
|**phoneNumbers** | **List&lt;String&gt;** | The hotel&#39;s phone number(s) |  |
|**roomCount** | **BigDecimal** | The number of rooms at the hotel. |  |
|**roomTypes** | [**List&lt;RoomType&gt;**](RoomType.md) | List of room types available at this hotel. |  |
|**starRating** | **Double** | The star rating (or star-equivalent rating) |  |
|**termsAndConditions** | **String** | Rules and terms that apply to this hotel and have to be shown to your guest before the make their booking. |  |
|**timezone** | **String** | The timezone the hotel is in - e.g AST |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the hotel&#39;s stable content (i.e. all the details of the hotel excluding its rates)  was last updated. |  [optional] |
|**websiteUrl** | **String** | The URL to the hotel&#39;s website. |  |



