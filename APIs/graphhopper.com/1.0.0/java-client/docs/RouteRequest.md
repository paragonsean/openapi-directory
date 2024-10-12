

# RouteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | Rather than looking for the shortest or fastest path, this lets you solve two different problems related to routing: With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. This requires &#x60;ch.disable&#x3D;true&#x60;. With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other. You can control both of these features with additional parameters, see below.  |  [optional] |
|**alternativeRouteMaxPaths** | **Integer** | If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives.  |  [optional] |
|**alternativeRouteMaxShareFactor** | **BigDecimal** | If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives.  |  [optional] |
|**alternativeRouteMaxWeightFactor** | **BigDecimal** | If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives.  |  [optional] |
|**avoid** | **String** | Specify which road classes and environments you would like to avoid. Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |
|**blockArea** | **String** | Block road access via a point with the format &#x60;latitude,longitude&#x60; or an area defined by a circle &#x60;lat,lon,radius&#x60; or a rectangle &#x60;lat1,lon1,lat2,lon2&#x60;. Separate several values with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |
|**calcPoints** | **Boolean** | If the points for the route should be calculated at all.  |  [optional] |
|**chDisable** | **Boolean** | Use this parameter in combination with one or more parameters from below.  |  [optional] |
|**curbsides** | [**List&lt;CurbsidesEnum&gt;**](#List&lt;CurbsidesEnum&gt;) | Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap. |  [optional] |
|**debug** | **Boolean** | If &#x60;true&#x60;, the output will be formatted.  |  [optional] |
|**details** | **List&lt;String&gt;** | Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;, &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539).  |  [optional] |
|**elevation** | **Boolean** | If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile.  |  [optional] |
|**headingPenalty** | **Integer** | Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |
|**headings** | **List&lt;Integer&gt;** | Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |
|**instructions** | **Boolean** | If instructions should be calculated and returned  |  [optional] |
|**locale** | **String** | The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German.  |  [optional] |
|**optimize** | **String** | Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits.  |  [optional] |
|**passThrough** | **Boolean** | If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |
|**pointHints** | **List&lt;String&gt;** | Optional parameter. Specifies a hint for each point in the &#x60;points&#x60; array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up. |  [optional] |
|**points** | **List&lt;List&lt;Double&gt;&gt;** | The points for the route in an array of &#x60;[longitude,latitude]&#x60;. For instance, if you want to calculate a route from point A to B to C then you specify &#x60;points: [ [A_longitude, A_latitude], [B_longitude, B_latitude], [C_longitude, C_latitude]]  |  [optional] |
|**pointsEncoded** | **Boolean** | Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information.  |  [optional] |
|**roundTripDistance** | **Integer** | If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |
|**roundTripSeed** | **Long** | If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value.  |  [optional] |
|**snapPreventions** | **List&lt;String&gt;** | Optional parameter to avoid snapping to a certain road class or road environment. Current supported values &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60; |  [optional] |
|**vehicle** | [**VehicleProfileId**](VehicleProfileId.md) |  |  [optional] |
|**weighting** | **String** | Determines the way the &#39;&#39;best&#39;&#39; route is calculated. Default is &#x60;fastest&#x60;. Other options are &#x60;shortest&#x60; (e.g. for &#x60;vehicle&#x3D;foot&#x60; or &#x60;bike&#x60;) and &#x60;short_fastest&#x60; which finds a reasonable balance between &#x60;shortest&#x60; and &#x60;fastest&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| ROUND_TRIP | &quot;round_trip&quot; |
| ALTERNATIVE_ROUTE | &quot;alternative_route&quot; |



## Enum: List&lt;CurbsidesEnum&gt;

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| RIGHT | &quot;right&quot; |
| LEFT | &quot;left&quot; |



