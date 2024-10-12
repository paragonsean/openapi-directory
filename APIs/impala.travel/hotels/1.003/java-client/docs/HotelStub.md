

# HotelStub

Essential information on a hotel returned as part of other resources, linking to the full resource within its `href` field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  |
|**checkIn** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**checkOut** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**emails** | **List&lt;String&gt;** |  |  [optional] |
|**hotelId** | **UUID** | Unique identifier for this hotel within the Impala platform. |  |
|**href** | **String** | URI that allows access to the full hotel information. |  [optional] |
|**images** | [**List&lt;Image&gt;**](Image.md) | Photos of the hotel, sorted in the recommended display order (e.g. for photo galleries) starting with the recommended hero image. |  |
|**location** | [**Location**](Location.md) |  |  |
|**name** | **String** | Name of the hotel. |  |
|**phoneNumbers** | **List&lt;String&gt;** | The hotel&#39;s phone number(s) |  [optional] |
|**starRating** | **Double** | The star rating (or star-equivalent rating) |  |
|**timezone** | **String** | The timezone the hotel is in - e.g AST |  [optional] |



