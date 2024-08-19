

# GoogleCloudAiplatformV1ImportDataConfig

Describes the location from where we import data into a Dataset, together with the labels that will be applied to the DataItems and the Annotations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationLabels** | **Map&lt;String, String&gt;** | Labels that will be applied to newly imported Annotations. If two Annotations are identical, one of them will be deduped. Two Annotations are considered identical if their payload, payload_schema_uri and all of their labels are the same. These labels will be overridden by Annotation labels specified inside index file referenced by import_schema_uri, e.g. jsonl file. |  [optional] |
|**dataItemLabels** | **Map&lt;String, String&gt;** | Labels that will be applied to newly imported DataItems. If an identical DataItem as one being imported already exists in the Dataset, then these labels will be appended to these of the already existing one, and if labels with identical key is imported before, the old label value will be overwritten. If two DataItems are identical in the same import data operation, the labels will be combined and if key collision happens in this case, one of the values will be picked randomly. Two DataItems are considered identical if their content bytes are identical (e.g. image bytes or pdf bytes). These labels will be overridden by Annotation labels specified inside index file referenced by import_schema_uri, e.g. jsonl file. |  [optional] |
|**gcsSource** | [**GoogleCloudAiplatformV1GcsSource**](GoogleCloudAiplatformV1GcsSource.md) |  |  [optional] |
|**importSchemaUri** | **String** | Required. Points to a YAML file stored on Google Cloud Storage describing the import format. Validation will be done against the schema. The schema is defined as an [OpenAPI 3.0.2 Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). |  [optional] |



