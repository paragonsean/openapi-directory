

# Key

Key defines all the dimensions that identify this record as unique.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effectiveConnectionType** | **String** | The effective connection type is the general connection class that all users experienced for this record. This field uses the values [\&quot;offline\&quot;, \&quot;slow-2G\&quot;, \&quot;2G\&quot;, \&quot;3G\&quot;, \&quot;4G\&quot;] as specified in: https://wicg.github.io/netinfo/#effective-connection-types If the effective connection type is unspecified, then aggregated data over all effective connection types will be returned. |  [optional] |
|**formFactor** | [**FormFactorEnum**](#FormFactorEnum) | The form factor is the device class that all users used to access the site for this record. If the form factor is unspecified, then aggregated data over all form factors will be returned. |  [optional] |
|**origin** | **String** | Origin specifies the origin that this record is for. Note: When specifying an origin, data for loads under this origin over all pages are aggregated into origin level user experience data. |  [optional] |
|**url** | **String** | Url specifies a specific url that this record is for. Note: When specifying a \&quot;url\&quot; only data for that specific url will be aggregated. |  [optional] |



## Enum: FormFactorEnum

| Name | Value |
|---- | -----|
| ALL_FORM_FACTORS | &quot;ALL_FORM_FACTORS&quot; |
| PHONE | &quot;PHONE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| TABLET | &quot;TABLET&quot; |



