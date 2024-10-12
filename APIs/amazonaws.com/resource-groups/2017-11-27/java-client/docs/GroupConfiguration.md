

# GroupConfiguration

A service configuration associated with a resource group. The configuration options are determined by the Amazon Web Services service that defines the <code>Type</code>, and specifies which resources can be included in the group. You can add a service configuration when you create the group by using <a>CreateGroup</a>, or later by using the <a>PutGroupConfiguration</a> operation. For details about group service configuration syntax, see <a href=\"https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\">Service configurations for resource groups</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_configuration** | [**List**](List.md) |  |  [optional] |
|**proposedConfiguration** | [**List**](List.md) |  |  [optional] |
|**status** | [**GroupConfigurationStatus**](GroupConfigurationStatus.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |



