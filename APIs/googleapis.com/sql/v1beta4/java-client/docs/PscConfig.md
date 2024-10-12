

# PscConfig

PSC settings for a Cloud SQL instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedConsumerProjects** | **List&lt;String&gt;** | Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects. Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric). |  [optional] |
|**pscEnabled** | **Boolean** | Whether PSC connectivity is enabled for this instance. |  [optional] |



