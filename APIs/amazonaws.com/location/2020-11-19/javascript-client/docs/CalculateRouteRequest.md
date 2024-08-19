# AmazonLocationService.CalculateRouteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carModeOptions** | [**CalculateRouteRequestCarModeOptions**](CalculateRouteRequestCarModeOptions.md) |  | [optional] 
**departNow** | **Boolean** | &lt;p&gt;Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.&lt;/p&gt; &lt;p&gt;Default Value: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;false&lt;/code&gt; | &lt;code&gt;true&lt;/code&gt; &lt;/p&gt; | [optional] 
**departurePosition** | **[Number]** | &lt;p&gt;The start position for the route. Defined in &lt;a href&#x3D;\&quot;https://earth-info.nga.mil/index.php?dir&#x3D;wgs84&amp;amp;action&#x3D;wgs84\&quot;&gt;World Geodetic System (WGS 84)&lt;/a&gt; format: &lt;code&gt;[longitude, latitude]&lt;/code&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For example, &lt;code&gt;[-123.115, 49.285]&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;If you specify a departure that&#39;s not located on a road, Amazon Location &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html\&quot;&gt;moves the position to the nearest road&lt;/a&gt;. If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a &lt;code&gt;400 RoutesValidationException&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid Values: &lt;code&gt;[-180 to 180,-90 to 90]&lt;/code&gt; &lt;/p&gt; | 
**departureTime** | **Date** | &lt;p&gt;Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Setting a departure time in the past returns a &lt;code&gt;400 ValidationException&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;In &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html\&quot;&gt;ISO 8601&lt;/a&gt; format: &lt;code&gt;YYYY-MM-DDThh:mm:ss.sssZ&lt;/code&gt;. For example, &lt;code&gt;2020–07-2T12:15:20.000Z+01:00&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**destinationPosition** | **[Number]** | &lt;p&gt;The finish position for the route. Defined in &lt;a href&#x3D;\&quot;https://earth-info.nga.mil/index.php?dir&#x3D;wgs84&amp;amp;action&#x3D;wgs84\&quot;&gt;World Geodetic System (WGS 84)&lt;/a&gt; format: &lt;code&gt;[longitude, latitude]&lt;/code&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; For example, &lt;code&gt;[-122.339, 47.615]&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;If you specify a destination that&#39;s not located on a road, Amazon Location &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html\&quot;&gt;moves the position to the nearest road&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid Values: &lt;code&gt;[-180 to 180,-90 to 90]&lt;/code&gt; &lt;/p&gt; | 
**distanceUnit** | **String** | &lt;p&gt;Set the unit system to specify the distance.&lt;/p&gt; &lt;p&gt;Default Value: &lt;code&gt;Kilometers&lt;/code&gt; &lt;/p&gt; | [optional] 
**includeLegGeometry** | **Boolean** | &lt;p&gt;Set to include the geometry details in the result for each path between a pair of positions.&lt;/p&gt; &lt;p&gt;Default Value: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;false&lt;/code&gt; | &lt;code&gt;true&lt;/code&gt; &lt;/p&gt; | [optional] 
**travelMode** | **String** | &lt;p&gt;Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose &lt;code&gt;Car&lt;/code&gt;, &lt;code&gt;Truck&lt;/code&gt;, &lt;code&gt;Walking&lt;/code&gt;, &lt;code&gt;Bicycle&lt;/code&gt; or &lt;code&gt;Motorcycle&lt;/code&gt; as options for the &lt;code&gt;TravelMode&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;Bicycle&lt;/code&gt; and &lt;code&gt;Motorcycle&lt;/code&gt; are only valid when using Grab as a data provider, and only within Southeast Asia.&lt;/p&gt; &lt;p&gt; &lt;code&gt;Truck&lt;/code&gt; is not available for Grab.&lt;/p&gt; &lt;p&gt;For more details on the using Grab for routing, including areas of coverage, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html\&quot;&gt;GrabMaps&lt;/a&gt; in the &lt;i&gt;Amazon Location Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The &lt;code&gt;TravelMode&lt;/code&gt; you specify also determines how you specify route preferences: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If traveling by &lt;code&gt;Car&lt;/code&gt; use the &lt;code&gt;CarModeOptions&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If traveling by &lt;code&gt;Truck&lt;/code&gt; use the &lt;code&gt;TruckModeOptions&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default Value: &lt;code&gt;Car&lt;/code&gt; &lt;/p&gt; | [optional] 
**truckModeOptions** | [**CalculateRouteRequestTruckModeOptions**](CalculateRouteRequestTruckModeOptions.md) |  | [optional] 
**waypointPositions** | **[Array]** | &lt;p&gt;Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For example, from the &lt;code&gt;DeparturePosition&lt;/code&gt; &lt;code&gt;[-123.115, 49.285]&lt;/code&gt;, the route follows the order that the waypoint positions are given &lt;code&gt;[[-122.757, 49.0021],[-122.349, 47.620]]&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;If you specify a waypoint position that&#39;s not located on a road, Amazon Location &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html\&quot;&gt;moves the position to the nearest road&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Specifying more than 23 waypoints returns a &lt;code&gt;400 ValidationException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a &lt;code&gt;400 RoutesValidationException&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid Values: &lt;code&gt;[-180 to 180,-90 to 90]&lt;/code&gt; &lt;/p&gt; | [optional] 



## Enum: DistanceUnitEnum


* `Kilometers` (value: `"Kilometers"`)

* `Miles` (value: `"Miles"`)





## Enum: TravelModeEnum


* `Car` (value: `"Car"`)

* `Truck` (value: `"Truck"`)

* `Walking` (value: `"Walking"`)

* `Bicycle` (value: `"Bicycle"`)

* `Motorcycle` (value: `"Motorcycle"`)




