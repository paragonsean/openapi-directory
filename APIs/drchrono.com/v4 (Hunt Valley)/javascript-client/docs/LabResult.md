# OpenapiJsClient.LabResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abnormalStatus** | **String** |  Value | Notes ----- | ----- &#x60;&#39;L&#39;&#x60; | &#x60;&#39;low&#39;&#x60; &#x60;&#39;LL&#39;&#x60; | &#x60;&#39;alert low&#39;&#x60; &#x60;&#39;H&#39;&#x60; | &#x60;&#39;high&#39;&#x60; &#x60;&#39;HH&#39;&#x60; | &#x60;&#39;alert high&#39;&#x60; &#x60;&#39;&lt;&#39;&#x60; | &#x60;&#39;panic low&#39;&#x60; &#x60;&#39;&gt;&#39;&#x60; | &#x60;&#39;panic high&#39;&#x60; &#x60;&#39;A&#39;&#x60; | &#x60;&#39;abnormal&#39;&#x60; &#x60;&#39;AA&#39;&#x60; | &#x60;&#39;very abnormal&#39;&#x60; &#x60;&#39;S&#39;&#x60; | &#x60;&#39;susceptible&#39;&#x60; &#x60;&#39;R&#39;&#x60; | &#x60;&#39;resistant&#39;&#x60; &#x60;&#39;I&#39;&#x60; | &#x60;&#39;intermediate&#39;&#x60; &#x60;&#39;NEG&#39;&#x60; | &#x60;&#39;negative&#39;&#x60; &#x60;&#39;POS&#39;&#x60; | &#x60;&#39;positive&#39;&#x60; &#x60;&#39;N&#39;&#x60; | &#x60;&#39;normal&#39;&#x60; &#x60;&#39;&#39;&#x60; | &#x60;&#39;no comment&#39;&#x60;  | [optional] 
**comments** | **String** |  | [optional] 
**document** | **Number** | ID of &#x60;/lab_documents&#x60; object for the result | 
**groupCode** | **String** | This is the code used for grouping result data. | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**isAbnormal** | **String** | If true, the result will be flagged for the doctor&#39;s attention | [optional] 
**labOrder** | **String** | ID of &#x60;/lab_orders&#x60; object the result belongs to | [optional] [readonly] 
**labTest** | **Number** | ID of &#x60;/lab_tests&#x60; object for the result | 
**normalRange** | **String** | When &#x60;&#x60;value_is_numeric&#x60;&#x60; is True, this parameter must be a string of the form &#x60;&#x60;\&quot;&lt;lower&gt; &lt;upper&gt;\&quot;, where both lower and upper are numerical&#x60;&#x60; | [optional] 
**observationCode** | **String** |  | [optional] 
**observationDescription** | **String** | For example, &#x60;&#x60;\&quot;Blood Urea Nitrogen (BUN)\&quot;&#x60;&#x60; | [optional] 
**specimenReceived** | **String** |  | [optional] 
**status** | **String** |  Value | Notes ----- | ----- &#x60;&#39;P&#39;&#x60; | &#x60;&#39;preliminary&#39;&#x60; &#x60;&#39;I&#39;&#x60; | &#x60;&#39;pending&#39;&#x60; &#x60;&#39;C&#39;&#x60; | &#x60;&#39;correction&#39;&#x60; &#x60;&#39;F&#39;&#x60; | &#x60;&#39;final&#39;&#x60; &#x60;&#39;X&#39;&#x60; | &#x60;&#39;canceled&#39;&#x60;  | 
**testPerformed** | **String** |  | 
**unit** | **String** | Unit used for the value | [optional] 
**value** | **String** |  | 
**valueIsNumeric** | **Boolean** | Default to &#x60;False&#x60; | [optional] 



## Enum: AbnormalStatusEnum


* `L` (value: `"L"`)

* `LL` (value: `"LL"`)

* `H` (value: `"H"`)

* `HH` (value: `"HH"`)

* `LESS_THAN` (value: `"<"`)

* `GREATER_THAN` (value: `">"`)

* `A` (value: `"A"`)

* `AA` (value: `"AA"`)

* `S` (value: `"S"`)

* `R` (value: `"R"`)

* `I` (value: `"I"`)

* `NEG` (value: `"NEG"`)

* `POS` (value: `"POS"`)

* `N` (value: `"N"`)

* `empty` (value: `""`)





## Enum: StatusEnum


* `P` (value: `"P"`)

* `I` (value: `"I"`)

* `C` (value: `"C"`)

* `F` (value: `"F"`)

* `X` (value: `"X"`)




