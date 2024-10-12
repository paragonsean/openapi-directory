

# Condition

A condition to be met.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**iam** | [**IamEnum**](#IamEnum) | Trusted attributes supplied by the IAM system. |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | An operator to apply the subject with. |  [optional] |
|**svc** | **String** | Trusted attributes discharged by the service. |  [optional] |
|**sys** | [**SysEnum**](#SysEnum) | Trusted attributes supplied by any service that owns resources and uses the IAM system for access control. |  [optional] |
|**values** | **List&lt;String&gt;** | The objects of the condition. |  [optional] |



## Enum: IamEnum

| Name | Value |
|---- | -----|
| NO_ATTR | &quot;NO_ATTR&quot; |
| AUTHORITY | &quot;AUTHORITY&quot; |
| ATTRIBUTION | &quot;ATTRIBUTION&quot; |
| SECURITY_REALM | &quot;SECURITY_REALM&quot; |
| APPROVER | &quot;APPROVER&quot; |
| JUSTIFICATION_TYPE | &quot;JUSTIFICATION_TYPE&quot; |
| CREDENTIALS_TYPE | &quot;CREDENTIALS_TYPE&quot; |
| CREDS_ASSERTION | &quot;CREDS_ASSERTION&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| NO_OP | &quot;NO_OP&quot; |
| EQUALS | &quot;EQUALS&quot; |
| NOT_EQUALS | &quot;NOT_EQUALS&quot; |
| IN | &quot;IN&quot; |
| NOT_IN | &quot;NOT_IN&quot; |
| DISCHARGED | &quot;DISCHARGED&quot; |



## Enum: SysEnum

| Name | Value |
|---- | -----|
| NO_ATTR | &quot;NO_ATTR&quot; |
| REGION | &quot;REGION&quot; |
| SERVICE | &quot;SERVICE&quot; |
| NAME | &quot;NAME&quot; |
| IP | &quot;IP&quot; |



