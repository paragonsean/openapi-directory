

# HistoryKey

Key defines all the dimensions that identify this record as unique.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formFactor** | [**FormFactorEnum**](#FormFactorEnum) | The form factor is the device class that all users used to access the site for this record. If the form factor is unspecified, then aggregated data over all form factors will be returned. |  [optional] |
|**origin** | **String** | Origin specifies the origin that this record is for. Note: When specifying an origin, data for loads under this origin over all pages are aggregated into origin level user experience data. |  [optional] |
|**url** | **String** | Url specifies a specific url that this record is for. This url should be normalized, following the normalization actions taken in the request to increase the chances of successful lookup. Note: When specifying a \&quot;url\&quot; only data for that specific url will be aggregated. |  [optional] |



## Enum: FormFactorEnum

| Name | Value |
|---- | -----|
| ALL_FORM_FACTORS | &quot;ALL_FORM_FACTORS&quot; |
| PHONE | &quot;PHONE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| TABLET | &quot;TABLET&quot; |



