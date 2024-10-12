

# ImportationMonitoring

Describe the reporting of the catalog importation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beginUtcDate** | **OffsetDateTime** | The start date of the importation |  |
|**errors** | [**List&lt;BeezUPCommonUserErrorMessage&gt;**](BeezUPCommonUserErrorMessage.md) | In case of error a description will be indicated |  [optional] |
|**executionId** | **String** | The execution identifier of the catalog importation |  |
|**lastUpdateUtcDate** | **OffsetDateTime** | The last update of the reporting |  |
|**links** | [**ImportationMonitoringLinks**](ImportationMonitoringLinks.md) |  |  [optional] |
|**steps** | **Map&lt;String, Boolean&gt;** | Contains all steps of the importation process with a boolean. If true the step has been passed, false the step is not complete |  |
|**success** | **Boolean** | Indicates if the importation was successfully completed or not |  |
|**userId** | **String** | The user identifier |  [optional] |



