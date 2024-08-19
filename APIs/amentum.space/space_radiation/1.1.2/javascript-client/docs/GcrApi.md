# SpaceRadiationApi.GcrApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiEndpointsGCRCalculateDlrFlux**](GcrApi.md#appApiEndpointsGCRCalculateDlrFlux) | **GET** /gcr/flux_dlr | Calculate particle flux  



## appApiEndpointsGCRCalculateDlrFlux

> FluxAtEnergy appApiEndpointsGCRCalculateDlrFlux(year, month, day, z, energy)

Calculate particle flux  

for the given energy, atomic number, and date. 

### Example

```javascript
import SpaceRadiationApi from 'space_radiation_api';

let apiInstance = new SpaceRadiationApi.GcrApi();
let year = 2017; // Number | <br>
let month = 1; // Number | <br>
let day = 1; // Number | <br>
let z = 6; // Number | <br>Particle atomic number
let energy = 100; // Number | <br>Particle energy in MeV/n<br> Valid range: [0, 10<sup>6</sup>] MeV/n<br>  
apiInstance.appApiEndpointsGCRCalculateDlrFlux(year, month, day, z, energy, (error, data, response) => {
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
 **year** | **Number**| &lt;br&gt; | 
 **month** | **Number**| &lt;br&gt; | 
 **day** | **Number**| &lt;br&gt; | 
 **z** | **Number**| &lt;br&gt;Particle atomic number | 
 **energy** | **Number**| &lt;br&gt;Particle energy in MeV/n&lt;br&gt; Valid range: [0, 10&lt;sup&gt;6&lt;/sup&gt;] MeV/n&lt;br&gt;   | 

### Return type

[**FluxAtEnergy**](FluxAtEnergy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

