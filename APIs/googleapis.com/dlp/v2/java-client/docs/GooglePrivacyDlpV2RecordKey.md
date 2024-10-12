

# GooglePrivacyDlpV2RecordKey

Message for a unique key indicating a record that contains a finding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigQueryKey** | [**GooglePrivacyDlpV2BigQueryKey**](GooglePrivacyDlpV2BigQueryKey.md) |  |  [optional] |
|**datastoreKey** | [**GooglePrivacyDlpV2DatastoreKey**](GooglePrivacyDlpV2DatastoreKey.md) |  |  [optional] |
|**idValues** | **List&lt;String&gt;** | Values of identifying columns in the given row. Order of values matches the order of &#x60;identifying_fields&#x60; specified in the scanning request. |  [optional] |



