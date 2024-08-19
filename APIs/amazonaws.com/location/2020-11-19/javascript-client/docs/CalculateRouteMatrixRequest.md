# AmazonLocationService.CalculateRouteMatrixRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carModeOptions** | [**CalculateRouteRequestCarModeOptions**](CalculateRouteRequestCarModeOptions.md) |  | [optional] 
**departNow** | **Boolean** | &lt;p&gt;Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You can&#39;t set both &lt;code&gt;DepartureTime&lt;/code&gt; and &lt;code&gt;DepartNow&lt;/code&gt;. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.&lt;/p&gt; &lt;p&gt;Default Value: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;false&lt;/code&gt; | &lt;code&gt;true&lt;/code&gt; &lt;/p&gt; | [optional] 
**departurePositions** | **[Array]** | &lt;p&gt;The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in &lt;a href&#x3D;\&quot;https://earth-info.nga.mil/GandG/wgs84/index.html\&quot;&gt;WGS 84&lt;/a&gt; format: &lt;code&gt;[longitude, latitude]&lt;/code&gt;. For example, &lt;code&gt;[-123.115, 49.285]&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html#matrix-routing-position-limits\&quot;&gt; Position restrictions&lt;/a&gt; in the &lt;i&gt;Amazon Location Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;For route calculators that use Esri as the data provider, if you specify a departure that&#39;s not located on a road, Amazon Location &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html\&quot;&gt; moves the position to the nearest road&lt;/a&gt;. The snapped value is available in the result in &lt;code&gt;SnappedDeparturePositions&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid Values: &lt;code&gt;[-180 to 180,-90 to 90]&lt;/code&gt; &lt;/p&gt; | 
**departureTime** | **Date** | &lt;p&gt;Specifies the desired time of departure. Uses the given time to calculate the route matrix. You can&#39;t set both &lt;code&gt;DepartureTime&lt;/code&gt; and &lt;code&gt;DepartNow&lt;/code&gt;. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Setting a departure time in the past returns a &lt;code&gt;400 ValidationException&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;In &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html\&quot;&gt;ISO 8601&lt;/a&gt; format: &lt;code&gt;YYYY-MM-DDThh:mm:ss.sssZ&lt;/code&gt;. For example, &lt;code&gt;2020–07-2T12:15:20.000Z+01:00&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**destinationPositions** | **[Array]** | &lt;p&gt;The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in &lt;a href&#x3D;\&quot;https://earth-info.nga.mil/GandG/wgs84/index.html\&quot;&gt;WGS 84&lt;/a&gt; format: &lt;code&gt;[longitude, latitude]&lt;/code&gt;. For example, &lt;code&gt;[-122.339, 47.615]&lt;/code&gt; &lt;/p&gt; &lt;important&gt; &lt;p&gt;Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html#matrix-routing-position-limits\&quot;&gt; Position restrictions&lt;/a&gt; in the &lt;i&gt;Amazon Location Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;For route calculators that use Esri as the data provider, if you specify a destination that&#39;s not located on a road, Amazon Location &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html\&quot;&gt; moves the position to the nearest road&lt;/a&gt;. The snapped value is available in the result in &lt;code&gt;SnappedDestinationPositions&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid Values: &lt;code&gt;[-180 to 180,-90 to 90]&lt;/code&gt; &lt;/p&gt; | 
**distanceUnit** | **String** | &lt;p&gt;Set the unit system to specify the distance.&lt;/p&gt; &lt;p&gt;Default Value: &lt;code&gt;Kilometers&lt;/code&gt; &lt;/p&gt; | [optional] 
**travelMode** | **String** | &lt;p&gt;Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;TravelMode&lt;/code&gt; you specify also determines how you specify route preferences: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If traveling by &lt;code&gt;Car&lt;/code&gt; use the &lt;code&gt;CarModeOptions&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If traveling by &lt;code&gt;Truck&lt;/code&gt; use the &lt;code&gt;TruckModeOptions&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;Bicycle&lt;/code&gt; or &lt;code&gt;Motorcycle&lt;/code&gt; are only valid when using &lt;code&gt;Grab&lt;/code&gt; as a data provider, and only within Southeast Asia.&lt;/p&gt; &lt;p&gt; &lt;code&gt;Truck&lt;/code&gt; is not available for Grab.&lt;/p&gt; &lt;p&gt;For more information about using Grab as a data provider, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html\&quot;&gt;GrabMaps&lt;/a&gt; in the &lt;i&gt;Amazon Location Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default Value: &lt;code&gt;Car&lt;/code&gt; &lt;/p&gt; | [optional] 
**truckModeOptions** | [**CalculateRouteRequestTruckModeOptions**](CalculateRouteRequestTruckModeOptions.md) |  | [optional] 



## Enum: DistanceUnitEnum


* `Kilometers` (value: `"Kilometers"`)

* `Miles` (value: `"Miles"`)





## Enum: TravelModeEnum


* `Car` (value: `"Car"`)

* `Truck` (value: `"Truck"`)

* `Walking` (value: `"Walking"`)

* `Bicycle` (value: `"Bicycle"`)

* `Motorcycle` (value: `"Motorcycle"`)




