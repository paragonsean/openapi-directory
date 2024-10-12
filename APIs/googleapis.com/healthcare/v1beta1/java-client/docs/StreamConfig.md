

# StreamConfig

Contains configuration for streaming FHIR export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDestination** | [**GoogleCloudHealthcareV1beta1FhirBigQueryDestination**](GoogleCloudHealthcareV1beta1FhirBigQueryDestination.md) |  |  [optional] |
|**deidentifiedStoreDestination** | [**DeidentifiedStoreDestination**](DeidentifiedStoreDestination.md) |  |  [optional] |
|**resourceTypes** | **List&lt;String&gt;** | Supply a FHIR resource type (such as \&quot;Patient\&quot; or \&quot;Observation\&quot;). See https://www.hl7.org/fhir/valueset-resource-types.html for a list of all FHIR resource types. The server treats an empty list as an intent to stream all the supported resource types in this FHIR store. |  [optional] |



