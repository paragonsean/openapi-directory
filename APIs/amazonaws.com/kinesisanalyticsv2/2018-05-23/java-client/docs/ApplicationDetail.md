

# ApplicationDetail

Describes the application, including the application Amazon Resource Name (ARN), status, latest version, and input and output configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationARN** | [**String**](String.md) |  |  |
|**applicationDescription** | [**String**](String.md) |  |  [optional] |
|**applicationName** | [**String**](String.md) |  |  |
|**runtimeEnvironment** | [**RuntimeEnvironment**](RuntimeEnvironment.md) |  |  |
|**serviceExecutionRole** | [**String**](String.md) |  |  [optional] |
|**applicationStatus** | [**ApplicationStatus**](ApplicationStatus.md) |  |  |
|**applicationVersionId** | [**Integer**](Integer.md) |  |  |
|**createTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdateTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**applicationConfigurationDescription** | [**ApplicationDetailApplicationConfigurationDescription**](ApplicationDetailApplicationConfigurationDescription.md) |  |  [optional] |
|**cloudWatchLoggingOptionDescriptions** | [**List**](List.md) |  |  [optional] |
|**applicationMaintenanceConfigurationDescription** | [**ApplicationDetailApplicationMaintenanceConfigurationDescription**](ApplicationDetailApplicationMaintenanceConfigurationDescription.md) |  |  [optional] |
|**applicationVersionUpdatedFrom** | [**Integer**](Integer.md) |  |  [optional] |
|**applicationVersionRolledBackFrom** | [**Integer**](Integer.md) |  |  [optional] |
|**conditionalToken** | [**String**](String.md) |  |  [optional] |
|**applicationVersionRolledBackTo** | [**Integer**](Integer.md) |  |  [optional] |
|**applicationMode** | [**ApplicationMode**](ApplicationMode.md) |  |  [optional] |



