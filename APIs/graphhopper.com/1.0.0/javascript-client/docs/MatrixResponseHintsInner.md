# GraphHopperDirectionsApi.MatrixResponseHintsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **String** | Details of this hint | [optional] 
**invalidFromPoints** | **[Number]** | Optional. An array of from_point indices of points that could not be found. Will only be added if &#x60;fail_fast&#x3D;false&#x60; and some &#x60;from_point&#x60;s were not found.&#x60; | [optional] 
**invalidToPoints** | **[Number]** | Optional. An array of to_point indices of points that could not be found. Will only be added if &#x60;fail_fast&#x3D;false&#x60; and some &#x60;to_point&#x60;s were not found.&#x60; | [optional] 
**message** | **String** | Short description of this hint | [optional] 
**pointPairs** | **[[Number]]** | Optional. An array of two-element arrays representing the from/to_point indices of points for which no connection could be found. Will only be added if &#x60;fail_fast&#x3D;false&#x60; and some connections were not found. | [optional] 


