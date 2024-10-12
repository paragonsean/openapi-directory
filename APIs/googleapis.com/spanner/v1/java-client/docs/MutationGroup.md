

# MutationGroup

A group of mutations to be committed together. Related mutations should be placed in a group. For example, two mutations inserting rows with the same primary key prefix in both parent and child tables are related.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mutations** | [**List&lt;Mutation&gt;**](Mutation.md) | Required. The mutations in this group. |  [optional] |



