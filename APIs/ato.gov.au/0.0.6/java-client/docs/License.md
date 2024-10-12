

# License

The License resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**id** | **String** | The resource&#39;s unique identifier. |  [optional] [readonly] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type. |  [optional] |
|**lifecycleState** | [**LifecycleStateEnum**](#LifecycleStateEnum) | The business name&#39;s lifecycle state. |  [optional] |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| AUSTRALIAN_FINANCIAL_SERVICES_LICENSE | &quot;Australian Financial Services License&quot; |
| LICENSE_2_B | &quot;License 2B&quot; |



## Enum: LifecycleStateEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;Approved&quot; |
| EXPIRED | &quot;Expired&quot; |
| ISSUED | &quot;Issued&quot; |
| PENDING_APPROVAL | &quot;Pending Approval&quot; |
| SUSPENDED | &quot;Suspended&quot; |



