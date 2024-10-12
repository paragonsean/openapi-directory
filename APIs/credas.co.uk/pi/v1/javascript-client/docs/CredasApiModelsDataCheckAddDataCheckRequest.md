# CredasApi.CredasApiModelsDataCheckAddDataCheckRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkType** | **Number** | The value of checkType dictates what checks are performed. &lt;br/&gt;The StandardAml check (value &#x3D; 1) will check DOB &amp; Mortality. &lt;br/&gt;The InternationalPepSanctions check (value &#x3D; 3) will check just International PEP &amp; Sanctions. &lt;br/&gt;The EnhancedAml check (value &#x3D; 2) will perform both these checks and is equivalent to making two calls with values of 1 then 3 and will be charged accordingly. &lt;br /&gt;  values&#x3D;&gt; None &#x3D; 0, StandardAml &#x3D; 1, EnhancedAml &#x3D; 2, InternationalPepSanctions &#x3D; 3 | 
**currentAddress** | [**CredasApiModelsDataCheckAddress**](CredasApiModelsDataCheckAddress.md) |  | 
**person** | [**CredasApiModelsDataCheckPerson**](CredasApiModelsDataCheckPerson.md) |  | 
**regEntryId** | **String** |  | 



## Enum: CheckTypeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)




