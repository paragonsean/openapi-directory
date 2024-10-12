

# Job

A job creating reports of a specific type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The creation date/time of the job. |  [optional] |
|**expireTime** | **String** | The date/time when this job will expire/expired. After a job expired, no new reports are generated. |  [optional] |
|**id** | **String** | The server-generated ID of the job (max. 40 characters). |  [optional] |
|**name** | **String** | The name of the job (max. 100 characters). |  [optional] |
|**reportTypeId** | **String** | The type of reports this job creates. Corresponds to the ID of a ReportType. |  [optional] |
|**systemManaged** | **Boolean** | True if this a system-managed job that cannot be modified by the user; otherwise false. |  [optional] |



