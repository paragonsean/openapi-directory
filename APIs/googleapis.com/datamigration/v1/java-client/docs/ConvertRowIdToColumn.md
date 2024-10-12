

# ConvertRowIdToColumn

Options to configure rule type ConvertROWIDToColumn. The rule is used to add column rowid to destination tables based on an Oracle rowid function/property. The rule filter field can refer to one or more entities. The rule scope can be one of: Table. This rule requires additional filter to be specified beyond the basic rule filter field, which is whether or not to work on tables which already have a primary key defined.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**onlyIfNoPrimaryKey** | **Boolean** | Required. Only work on tables without primary key defined |  [optional] |



