

# Write

Arguments to insert, update, insert_or_update, and replace operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** | The names of the columns in table to be written. The list of columns must contain enough columns to allow Cloud Spanner to derive values for all primary key columns in the row(s) to be modified. |  [optional] |
|**table** | **String** | Required. The table whose rows will be written. |  [optional] |
|**values** | **List&lt;List&lt;Object&gt;&gt;** | The values to be written. &#x60;values&#x60; can contain more than one list of values. If it does, then multiple rows are written, one for each entry in &#x60;values&#x60;. Each list in &#x60;values&#x60; must have exactly as many entries as there are entries in columns above. Sending multiple lists is equivalent to sending multiple &#x60;Mutation&#x60;s, each containing one &#x60;values&#x60; entry and repeating table and columns. Individual values in each list are encoded as described here. |  [optional] |



