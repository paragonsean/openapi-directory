

# GetServicePointByIdResponseBodyServicePoint


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressLine1** | **String** |  |  [optional] |
|**carrierCode** | **String** |  |  [optional] |
|**cityLocality** | **String** |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**countryCode** | **String** |  |  [optional] |
|**features** | [**List&lt;FeaturesEnum&gt;**](#List&lt;FeaturesEnum&gt;) |  |  [optional] |
|**hoursOfOperation** | [**GetServicePointByIdResponseBodyServicePointHoursOfOperation**](GetServicePointByIdResponseBodyServicePointHoursOfOperation.md) |  |  [optional] |
|**lat** | **Double** |  |  [optional] |
|**_long** | **Double** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**postalCode** | **String** |  |  [optional] |
|**serviceCodes** | **List&lt;String&gt;** |  |  [optional] |
|**servicePointId** | **String** |  |  [optional] |
|**stateProvince** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: List&lt;FeaturesEnum&gt;

| Name | Value |
|---- | -----|
| DROP_OFF_POINT | &quot;drop_off_point&quot; |
| PICKUP_POINT | &quot;pickup_point&quot; |
| PRINT_SERVICES | &quot;print_services&quot; |
| AFTER_HOURS_LOCKER | &quot;after_hours_locker&quot; |
| AFTER_HOURS_DROPBOX | &quot;after_hours_dropbox&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PUDO | &quot;pudo&quot; |
| LOCKER | &quot;locker&quot; |



