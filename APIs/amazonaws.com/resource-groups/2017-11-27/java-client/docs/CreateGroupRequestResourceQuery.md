

# CreateGroupRequestResourceQuery

<p>The query you can use to define a resource group or a search for resources. A <code>ResourceQuery</code> specifies both a query <code>Type</code> and a <code>Query</code> string as JSON string objects. See the examples section for example JSON strings. For more information about creating a resource group with a resource query, see <a href=\"https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html\">Build queries and groups in Resource Groups</a> in the <i>Resource Groups User Guide</i> </p> <p>When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\\). For example, a complete <code>ResourceQuery</code> parameter must be formatted like the following CLI parameter example:</p> <p> <code>--resource-query '{\"Type\":\"TAG_FILTERS_1_0\",\"Query\":\"{\\\"ResourceTypeFilters\\\":[\\\"AWS::AllSupported\\\"],\\\"TagFilters\\\":[{\\\"Key\\\":\\\"Stage\\\",\\\"Values\\\":[\\\"Test\\\"]}]}\"}'</code> </p> <p>In the preceding example, all of the double quote characters in the value part of the <code>Query</code> element must be escaped because the value itself is surrounded by double quotes. For more information, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html\">Quoting strings</a> in the <i>Command Line Interface User Guide</i>.</p> <p>For the complete list of resource types that you can use in the array value for <code>ResourceTypeFilters</code>, see <a href=\"https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html\">Resources you can use with Resource Groups and Tag Editor</a> in the <i>Resource Groups User Guide</i>. For example:</p> <p> <code>\"ResourceTypeFilters\":[\"AWS::S3::Bucket\", \"AWS::EC2::Instance\"]</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**QueryType**](QueryType.md) |  |  [optional] |
|**query** | [**String**](String.md) |  |  [optional] |



