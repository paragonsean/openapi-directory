

# GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecSliceConfig

Specification message containing the config for this SliceSpec. When `kind` is selected as `value` and/or `range`, only a single slice will be computed. When `all_values` is present, a separate slice will be computed for each possible label/value for the corresponding key in `config`. Examples, with feature zip_code with values 12345, 23334, 88888 and feature country with values \"US\", \"Canada\", \"Mexico\" in the dataset: Example 1: { \"zip_code\": { \"value\": { \"float_value\": 12345.0 } } } A single slice for any data with zip_code 12345 in the dataset. Example 2: { \"zip_code\": { \"range\": { \"low\": 12345, \"high\": 20000 } } } A single slice containing data where the zip_codes between 12345 and 20000 For this example, data with the zip_code of 12345 will be in this slice. Example 3: { \"zip_code\": { \"range\": { \"low\": 10000, \"high\": 20000 } }, \"country\": { \"value\": { \"string_value\": \"US\" } } } A single slice containing data where the zip_codes between 10000 and 20000 has the country \"US\". For this example, data with the zip_code of 12345 and country \"US\" will be in this slice. Example 4: { \"country\": {\"all_values\": { \"value\": true } } } Three slices are computed, one for each unique country in the dataset. Example 5: { \"country\": { \"all_values\": { \"value\": true } }, \"zip_code\": { \"value\": { \"float_value\": 12345.0 } } } Three slices are computed, one for each unique country in the dataset where the zip_code is also 12345. For this example, data with zip_code 12345 and country \"US\" will be in one slice, zip_code 12345 and country \"Canada\" in another slice, and zip_code 12345 and country \"Mexico\" in another slice, totaling 3 slices.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allValues** | **Boolean** | If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: &#x60;{\&quot;all_values\&quot;:{\&quot;value\&quot;:true}}&#x60; |  [optional] |
|**range** | [**GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange**](GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange.md) |  |  [optional] |
|**value** | [**GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue**](GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue.md) |  |  [optional] |



