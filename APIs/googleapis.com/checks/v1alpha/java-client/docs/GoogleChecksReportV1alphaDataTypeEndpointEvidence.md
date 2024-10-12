

# GoogleChecksReportV1alphaDataTypeEndpointEvidence

Evidence based on an endpoint that data was sent to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributedSdks** | [**List&lt;GoogleChecksReportV1alphaDataTypeEndpointEvidenceAttributedSdk&gt;**](GoogleChecksReportV1alphaDataTypeEndpointEvidenceAttributedSdk.md) | Set of SDKs that are attributed to the exfiltration. |  [optional] |
|**endpointDetails** | [**List&lt;GoogleChecksReportV1alphaDataTypeEndpointEvidenceEndpointDetails&gt;**](GoogleChecksReportV1alphaDataTypeEndpointEvidenceEndpointDetails.md) | Endpoints the data type was sent to. |  [optional] |
|**exfiltratedDataType** | [**ExfiltratedDataTypeEnum**](#ExfiltratedDataTypeEnum) | Type of data that was exfiltrated. |  [optional] |



## Enum: ExfiltratedDataTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EXFILTRATED_DATA_TYPE_UNSPECIFIED&quot; |
| PHONE_NUMBER | &quot;EXFILTRATED_DATA_TYPE_PHONE_NUMBER&quot; |
| PRECISE_LOCATION | &quot;EXFILTRATED_DATA_TYPE_PRECISE_LOCATION&quot; |
| CONTACT_NAME | &quot;EXFILTRATED_DATA_TYPE_CONTACT_NAME&quot; |
| CONTACT_EMAIL | &quot;EXFILTRATED_DATA_TYPE_CONTACT_EMAIL&quot; |
| CONTACT_PHONE_NUMBER | &quot;EXFILTRATED_DATA_TYPE_CONTACT_PHONE_NUMBER&quot; |
| INCOMING_TEXT_NUMBER | &quot;EXFILTRATED_DATA_TYPE_INCOMING_TEXT_NUMBER&quot; |
| INCOMING_TEXT_MESSAGE | &quot;EXFILTRATED_DATA_TYPE_INCOMING_TEXT_MESSAGE&quot; |
| OUTGOING_TEXT_NUMBER | &quot;EXFILTRATED_DATA_TYPE_OUTGOING_TEXT_NUMBER&quot; |
| OUTGOING_TEXT_MESSAGE | &quot;EXFILTRATED_DATA_TYPE_OUTGOING_TEXT_MESSAGE&quot; |
| ADVERTISING_ID | &quot;EXFILTRATED_DATA_TYPE_ADVERTISING_ID&quot; |
| ANDROID_ID | &quot;EXFILTRATED_DATA_TYPE_ANDROID_ID&quot; |
| IMEI | &quot;EXFILTRATED_DATA_TYPE_IMEI&quot; |
| IMSI | &quot;EXFILTRATED_DATA_TYPE_IMSI&quot; |
| SIM_SERIAL_NUMBER | &quot;EXFILTRATED_DATA_TYPE_SIM_SERIAL_NUMBER&quot; |
| SSID | &quot;EXFILTRATED_DATA_TYPE_SSID&quot; |
| ACCOUNT | &quot;EXFILTRATED_DATA_TYPE_ACCOUNT&quot; |
| EXTERNAL_ACCOUNT | &quot;EXFILTRATED_DATA_TYPE_EXTERNAL_ACCOUNT&quot; |
| INSTALLED_PACKAGES | &quot;EXFILTRATED_DATA_TYPE_INSTALLED_PACKAGES&quot; |



