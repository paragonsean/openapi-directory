

# GeofenceGeometry

<p>Contains the geofence geometry details.</p> <p>A geofence geometry is made up of either a polygon or a circle. Can be either a polygon or a circle. Including both will return a validation error.</p> <note> <p>Amazon Location doesn't currently support polygons with holes, multipolygons, polygons that are wound clockwise, or that cross the antimeridian. </p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**circle** | [**PutGeofenceRequestGeometryCircle**](PutGeofenceRequestGeometryCircle.md) |  |  [optional] |
|**polygon** | [**List**](List.md) |  |  [optional] |



