# DatabaseMigrationApi.ApplyConversionWorkspaceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoCommit** | **Boolean** | Optional. Specifies whether the conversion workspace is to be committed automatically after the apply. | [optional] 
**connectionProfile** | **String** | Optional. Fully qualified (Uri) name of the destination connection profile. | [optional] 
**dryRun** | **Boolean** | Optional. Only validates the apply process, but doesn&#39;t change the destination database. Only works for PostgreSQL destination connection profile. | [optional] 
**filter** | **String** | Filter which entities to apply. Leaving this field empty will apply all of the entities. Supports Google AIP 160 based filtering. | [optional] 


