

# DiaryAppointmentTypeModel

Represents a diary appointment type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**name** | **String** | The appointment type name. |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**systemType** | [**SystemTypeEnum**](#SystemTypeEnum) | The appointment system type. |  [optional] |



## Enum: SystemTypeEnum

| Name | Value |
|---- | -----|
| VIEWING | &quot;Viewing&quot; |
| VIEW_AND_VALUE | &quot;ViewAndValue&quot; |
| OPENING_INSPECTION | &quot;OpeningInspection&quot; |
| INTERIM_INSPECTION | &quot;InterimInspection&quot; |
| CLOSING_INSPECTION | &quot;ClosingInspection&quot; |
| SALES_APPRAISAL | &quot;SalesAppraisal&quot; |
| CUSTOM | &quot;Custom&quot; |



