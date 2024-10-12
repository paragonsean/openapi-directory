

# BaseInfoAttributes

Attributes for Base URL Info endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | Presently used full version of the OPTIMADE API. The version number string MUST NOT be prefixed by, e.g., \&quot;v\&quot;. Examples: &#x60;1.0.0&#x60;, &#x60;1.0.0-rc.2&#x60;. |  |
|**availableApiVersions** | [**List&lt;AvailableApiVersion&gt;**](AvailableApiVersion.md) | A list of dictionaries of available API versions at other base URLs |  |
|**availableEndpoints** | **List&lt;String&gt;** | List of available endpoints (i.e., the string to be appended to the versioned base URL). |  |
|**entryTypesByFormat** | **Map&lt;String, List&lt;String&gt;&gt;** | Available entry endpoints as a function of output formats. |  |
|**formats** | **List&lt;String&gt;** | List of available output formats. |  [optional] |
|**isIndex** | **Boolean** | If true, this is an index meta-database base URL (see section Index Meta-Database). If this member is not provided, the client MUST assume this is not an index meta-database base URL (i.e., the default is for &#x60;is_index&#x60; to be &#x60;false&#x60;). |  [optional] |



