

# RevocationDetails

Describes fields that are relavent to the revocation of a Certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**revocationState** | [**RevocationStateEnum**](#RevocationStateEnum) | Indicates why a Certificate was revoked. |  [optional] |
|**revocationTime** | **String** | The time at which this Certificate was revoked. |  [optional] |



## Enum: RevocationStateEnum

| Name | Value |
|---- | -----|
| REVOCATION_REASON_UNSPECIFIED | &quot;REVOCATION_REASON_UNSPECIFIED&quot; |
| KEY_COMPROMISE | &quot;KEY_COMPROMISE&quot; |
| CERTIFICATE_AUTHORITY_COMPROMISE | &quot;CERTIFICATE_AUTHORITY_COMPROMISE&quot; |
| AFFILIATION_CHANGED | &quot;AFFILIATION_CHANGED&quot; |
| SUPERSEDED | &quot;SUPERSEDED&quot; |
| CESSATION_OF_OPERATION | &quot;CESSATION_OF_OPERATION&quot; |
| CERTIFICATE_HOLD | &quot;CERTIFICATE_HOLD&quot; |
| PRIVILEGE_WITHDRAWN | &quot;PRIVILEGE_WITHDRAWN&quot; |
| ATTRIBUTE_AUTHORITY_COMPROMISE | &quot;ATTRIBUTE_AUTHORITY_COMPROMISE&quot; |



