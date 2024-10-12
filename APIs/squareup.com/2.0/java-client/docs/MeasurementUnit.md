

# MeasurementUnit

Represents a unit of measurement to use with a quantity, such as ounces or inches. Exactly one of the following fields are required: `custom_unit`, `area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areaUnit** | **String** | Represents a standard area unit. |  [optional] |
|**customUnit** | [**MeasurementUnitCustom**](MeasurementUnitCustom.md) |  |  [optional] |
|**genericUnit** | **String** | Reserved for API integrations that lack the ability to specify a real measurement unit |  [optional] |
|**lengthUnit** | **String** | Represents a standard length unit. |  [optional] |
|**timeUnit** | **String** | Represents a standard unit of time. |  [optional] |
|**type** | **String** | Represents the type of the measurement unit. |  [optional] |
|**volumeUnit** | **String** | Represents a standard volume unit. |  [optional] |
|**weightUnit** | **String** | Represents a standard unit of weight or mass. |  [optional] |



