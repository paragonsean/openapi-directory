# ShipEngineApi.Package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentDescription** | **String** | A short description of the package content. Required for shipments moving to, from, and through Mexico.  | [optional] 
**dimensions** | [**Dimensions**](Dimensions.md) | The package dimensions | [optional] 
**externalPackageId** | **String** | An external package id. | [optional] 
**formDownload** | [**OptionalLink**](OptionalLink.md) | The form download for any customs that are needed | [optional] [readonly] 
**insuredValue** | [**MonetaryValue**](MonetaryValue.md) | The insured value of the package.  Requires the &#x60;insurance_provider&#x60; field of the shipment to be set.  | [optional] 
**labelDownload** | [**LabelDownload**](LabelDownload.md) | The label download for the package | [optional] [readonly] 
**labelMessages** | [**LabelMessages**](LabelMessages.md) |  | [optional] 
**packageCode** | **String** | The [package type](https://www.shipengine.com/docs/reference/list-carrier-packages/), such as &#x60;thick_envelope&#x60;, &#x60;small_flat_rate_box&#x60;, &#x60;large_package&#x60;, etc.  The code &#x60;package&#x60; indicates a custom or unknown package type.  | [optional] 
**packageId** | **String** | A string that uniquely identifies this [package type](https://www.shipengine.com/docs/reference/list-carrier-packages/) | [optional] 
**sequence** | **Number** | Package sequence | [optional] [readonly] 
**trackingNumber** | **String** | The tracking number for the package.  The format depends on the carrier.  | [optional] [readonly] 
**weight** | [**Weight**](Weight.md) | The package weight | 


