# SpaceRadiationApi.TrappedApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiEndpointsTrappedRadiationCalculateFluxMean**](TrappedApi.md#appApiEndpointsTrappedRadiationCalculateFluxMean) | **GET** /trapped/flux_mean | Calculate mean particle flux 
[**appApiEndpointsTrappedRadiationCalculateFluxPercentile**](TrappedApi.md#appApiEndpointsTrappedRadiationCalculateFluxPercentile) | **GET** /trapped/flux_percentile | Calculate percentile particle flux 



## appApiEndpointsTrappedRadiationCalculateFluxMean

> Flux appApiEndpointsTrappedRadiationCalculateFluxMean(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second)

Calculate mean particle flux 

at given coordinates and date-time. 

### Example

```javascript
import SpaceRadiationApi from 'space_radiation_api';

let apiInstance = new SpaceRadiationApi.TrappedApi();
let model = "AE9"; // String | <br>Which model to use: <br><br> - Energetic electrons (AE9) <br> - Energetic protons (AP9)  <br> - Space plasma model for electrons (SPME) <br> - for hydrogen (SPMH) <br> - for helium (SPMHE) <br> - for oxygen (SPMO)  
let coordSys = "GEI"; // String | <br>Coordinate system to use:  <br><br> - Geodetic/WGS84 (GDZ) <br> - Geocentric Cartesian (GEO) <br> - Geocentric Earth Inertial (GEI) <br> See \"Bhavnani, K. H., & Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\"  for coord system definitions. 
let coordUnits = "KM"; // String | <br>Coordinate units to use: km (KM) or Earth Radii (RE) 
let coord1 = 3216.6; // Number | <br>First coordinate value to specify position. <br><br> Ordering for GEI, GEO coords:X, Y, Z<br> Ordering for GDZ coords: Alt, Lat, Long<br>  Valid ranges for latitude: -90, 90<br>  Valid ranges for longitude: 0, 360<br>  
let coord2 = 35426; // Number | <br>Second coordinate value.
let coord3 = 603.4; // Number | <br>Third coordinate value.
let year = 2017; // Number | <br>
let month = 1; // Number | <br>
let day = 1; // Number | <br>
let hour = 0; // Number | <br>
let minute = 0; // Number | <br>
let second = 0; // Number | <br>
apiInstance.appApiEndpointsTrappedRadiationCalculateFluxMean(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **String**| &lt;br&gt;Which model to use: &lt;br&gt;&lt;br&gt; - Energetic electrons (AE9) &lt;br&gt; - Energetic protons (AP9)  &lt;br&gt; - Space plasma model for electrons (SPME) &lt;br&gt; - for hydrogen (SPMH) &lt;br&gt; - for helium (SPMHE) &lt;br&gt; - for oxygen (SPMO)   | 
 **coordSys** | **String**| &lt;br&gt;Coordinate system to use:  &lt;br&gt;&lt;br&gt; - Geodetic/WGS84 (GDZ) &lt;br&gt; - Geocentric Cartesian (GEO) &lt;br&gt; - Geocentric Earth Inertial (GEI) &lt;br&gt; See \&quot;Bhavnani, K. H., &amp; Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\&quot;  for coord system definitions.  | 
 **coordUnits** | **String**| &lt;br&gt;Coordinate units to use: km (KM) or Earth Radii (RE)  | 
 **coord1** | **Number**| &lt;br&gt;First coordinate value to specify position. &lt;br&gt;&lt;br&gt; Ordering for GEI, GEO coords:X, Y, Z&lt;br&gt; Ordering for GDZ coords: Alt, Lat, Long&lt;br&gt;  Valid ranges for latitude: -90, 90&lt;br&gt;  Valid ranges for longitude: 0, 360&lt;br&gt;   | 
 **coord2** | **Number**| &lt;br&gt;Second coordinate value. | 
 **coord3** | **Number**| &lt;br&gt;Third coordinate value. | 
 **year** | **Number**| &lt;br&gt; | 
 **month** | **Number**| &lt;br&gt; | 
 **day** | **Number**| &lt;br&gt; | 
 **hour** | **Number**| &lt;br&gt; | 
 **minute** | **Number**| &lt;br&gt; | 
 **second** | **Number**| &lt;br&gt; | 

### Return type

[**Flux**](Flux.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiEndpointsTrappedRadiationCalculateFluxPercentile

> Flux appApiEndpointsTrappedRadiationCalculateFluxPercentile(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second, percentile)

Calculate percentile particle flux 

at given coordinates and date-time. 

### Example

```javascript
import SpaceRadiationApi from 'space_radiation_api';

let apiInstance = new SpaceRadiationApi.TrappedApi();
let model = "AE9"; // String | <br>Which model to use: <br><br> - Energetic electrons (AE9) <br> - Energetic protons (AP9)  <br> - Space plasma model for electrons (SPME) <br> - for hydrogen (SPMH) <br> - for helium (SPMHE) <br> - for oxygen (SPMO)  
let coordSys = "GEI"; // String | <br>Coordinate system to use:  <br><br> - Geodetic/WGS84 (GDZ) <br> - Geocentric Cartesian (GEO) <br> - Geocentric Earth Inertial (GEI) <br> See \"Bhavnani, K. H., & Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\"  for coord system definitions. 
let coordUnits = "KM"; // String | <br>Coordinate units to use: km (KM) or Earth Radii (RE) 
let coord1 = 3216.6; // Number | <br>First coordinate value to specify position. <br><br> Ordering for GEI, GEO coords:X, Y, Z<br> Ordering for GDZ coords: Alt, Lat, Long<br>  Valid ranges for latitude: -90, 90<br>  Valid ranges for longitude: 0, 360<br>  
let coord2 = 35426; // Number | <br>Second coordinate value.
let coord3 = 603.4; // Number | <br>Third coordinate value.
let year = 2017; // Number | <br>
let month = 1; // Number | <br>
let day = 1; // Number | <br>
let hour = 0; // Number | <br>
let minute = 0; // Number | <br>
let second = 0; // Number | <br>
let percentile = 50; // Number | <br>Integer percentile at which to calc flux (50 is the median value). 
apiInstance.appApiEndpointsTrappedRadiationCalculateFluxPercentile(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second, percentile, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **String**| &lt;br&gt;Which model to use: &lt;br&gt;&lt;br&gt; - Energetic electrons (AE9) &lt;br&gt; - Energetic protons (AP9)  &lt;br&gt; - Space plasma model for electrons (SPME) &lt;br&gt; - for hydrogen (SPMH) &lt;br&gt; - for helium (SPMHE) &lt;br&gt; - for oxygen (SPMO)   | 
 **coordSys** | **String**| &lt;br&gt;Coordinate system to use:  &lt;br&gt;&lt;br&gt; - Geodetic/WGS84 (GDZ) &lt;br&gt; - Geocentric Cartesian (GEO) &lt;br&gt; - Geocentric Earth Inertial (GEI) &lt;br&gt; See \&quot;Bhavnani, K. H., &amp; Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\&quot;  for coord system definitions.  | 
 **coordUnits** | **String**| &lt;br&gt;Coordinate units to use: km (KM) or Earth Radii (RE)  | 
 **coord1** | **Number**| &lt;br&gt;First coordinate value to specify position. &lt;br&gt;&lt;br&gt; Ordering for GEI, GEO coords:X, Y, Z&lt;br&gt; Ordering for GDZ coords: Alt, Lat, Long&lt;br&gt;  Valid ranges for latitude: -90, 90&lt;br&gt;  Valid ranges for longitude: 0, 360&lt;br&gt;   | 
 **coord2** | **Number**| &lt;br&gt;Second coordinate value. | 
 **coord3** | **Number**| &lt;br&gt;Third coordinate value. | 
 **year** | **Number**| &lt;br&gt; | 
 **month** | **Number**| &lt;br&gt; | 
 **day** | **Number**| &lt;br&gt; | 
 **hour** | **Number**| &lt;br&gt; | 
 **minute** | **Number**| &lt;br&gt; | 
 **second** | **Number**| &lt;br&gt; | 
 **percentile** | **Number**| &lt;br&gt;Integer percentile at which to calc flux (50 is the median value).  | 

### Return type

[**Flux**](Flux.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

