# Superset.ChartDataRollingOptionsSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center** | **Boolean** | Should the label be at the center of the window. Default: &#x60;false&#x60; | [optional] 
**minPeriods** | **Number** | The minimum amount of periods required for a row to be included in the result set. | [optional] 
**rollingType** | **String** | Type of rolling window. Any numpy function will work. | 
**rollingTypeOptions** | **Object** |  | [optional] 
**winType** | **String** | Type of window function. See [SciPy window functions](https://docs.scipy.org/doc/scipy/reference/signal.windows.html#module-scipy.signal.windows) for more details. Some window functions require passing additional parameters to &#x60;rolling_type_options&#x60;. For instance, to use &#x60;gaussian&#x60;, the parameter &#x60;std&#x60; needs to be provided. | [optional] 
**window** | **Number** | Size of the rolling window in days. | 



## Enum: RollingTypeEnum


* `average` (value: `"average"`)

* `argmin` (value: `"argmin"`)

* `argmax` (value: `"argmax"`)

* `cumsum` (value: `"cumsum"`)

* `cumprod` (value: `"cumprod"`)

* `max` (value: `"max"`)

* `mean` (value: `"mean"`)

* `median` (value: `"median"`)

* `nansum` (value: `"nansum"`)

* `nanmin` (value: `"nanmin"`)

* `nanmax` (value: `"nanmax"`)

* `nanmean` (value: `"nanmean"`)

* `nanmedian` (value: `"nanmedian"`)

* `nanpercentile` (value: `"nanpercentile"`)

* `min` (value: `"min"`)

* `percentile` (value: `"percentile"`)

* `prod` (value: `"prod"`)

* `product` (value: `"product"`)

* `std` (value: `"std"`)

* `sum` (value: `"sum"`)

* `var` (value: `"var"`)





## Enum: WinTypeEnum


* `boxcar` (value: `"boxcar"`)

* `triang` (value: `"triang"`)

* `blackman` (value: `"blackman"`)

* `hamming` (value: `"hamming"`)

* `bartlett` (value: `"bartlett"`)

* `parzen` (value: `"parzen"`)

* `bohman` (value: `"bohman"`)

* `blackmanharris` (value: `"blackmanharris"`)

* `nuttall` (value: `"nuttall"`)

* `barthann` (value: `"barthann"`)

* `kaiser` (value: `"kaiser"`)

* `gaussian` (value: `"gaussian"`)

* `general_gaussian` (value: `"general_gaussian"`)

* `slepian` (value: `"slepian"`)

* `exponential` (value: `"exponential"`)




