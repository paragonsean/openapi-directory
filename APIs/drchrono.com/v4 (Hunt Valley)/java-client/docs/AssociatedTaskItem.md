

# AssociatedTaskItem



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**task** | **Integer** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Can be one of &#x60;\&quot;Appointment\&quot;&#x60;, &#x60;\&quot;Patient\&quot;&#x60;, &#x60;\&quot;Message\&quot;&#x60;, &#x60;\&quot;Document\&quot;&#x60;, &#x60;\&quot;Lab order\&quot;&#x60; |  [optional] |
|**value** | **Integer** | ID of the specified type object |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PATIENT | &quot;Patient&quot; |
| APPOINTMENT | &quot;Appointment&quot; |
| LAB_ORDER | &quot;Lab order&quot; |
| DOCUMENT | &quot;Document&quot; |
| MESSAGE | &quot;Message&quot; |
| LAB_DOCUMENT | &quot;Lab document&quot; |
| LAB_RESULT | &quot;Lab result&quot; |
| COMMUNICATION | &quot;Communication&quot; |



