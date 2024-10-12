# DatabaseMigrationApi.ConstraintEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFeatures** | **{String: Object}** | Custom engine specific features. | [optional] 
**name** | **String** | The name of the table constraint. | [optional] 
**referenceColumns** | **[String]** | Reference columns which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full names of referenced columns by the foreign key. | [optional] 
**referenceTable** | **String** | Reference table which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full name of the referenced table by the foreign key. | [optional] 
**tableColumns** | **[String]** | Table columns used as part of the Constraint, for example primary key constraint should list the columns which constitutes the key. | [optional] 
**tableName** | **String** | Table which is associated with the constraint. In case the constraint is defined on a table, this field is left empty as this information is stored in parent_name. However, if constraint is defined on a view, this field stores the table name on which the view is defined. | [optional] 
**type** | **String** | Type of constraint, for example unique, primary key, foreign key (currently only primary key is supported). | [optional] 


