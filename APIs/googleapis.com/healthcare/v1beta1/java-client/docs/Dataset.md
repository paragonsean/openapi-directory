

# Dataset

A message representing a health dataset. A health dataset represents a collection of healthcare data pertaining to one or more patients. This may include multiple modalities of healthcare data, such as electronic medical records or medical imaging data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Identifier. Resource name of the dataset, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}&#x60;. |  [optional] |
|**timeZone** | **String** | The default timezone used by this dataset. Must be a either a valid IANA time zone name such as \&quot;America/New_York\&quot; or empty, which defaults to UTC. This is used for parsing times in resources, such as HL7 messages, where no explicit timezone is specified. |  [optional] |



