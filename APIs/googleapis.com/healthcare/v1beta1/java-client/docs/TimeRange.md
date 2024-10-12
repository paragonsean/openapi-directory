

# TimeRange

Apply consents given by patients whose most recent consent changes are in the time range. Note that after identifying these patients, the server applies all Consent resources given by those patients, not just the Consent resources within the timestamp in the range.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**end** | **String** | Optional. The latest consent change time, in format YYYY-MM-DDThh:mm:ss.sss+zz:zz If not specified, the system uses the time when ApplyConsents was called. |  [optional] |
|**start** | **String** | Optional. The earliest consent change time, in format YYYY-MM-DDThh:mm:ss.sss+zz:zz If not specified, the system uses the FHIR store creation time. |  [optional] |



