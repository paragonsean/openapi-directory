

# CodeGenConfigurationNode

 <code>CodeGenConfigurationNode</code> enumerates all valid Node types. One and only one of its member variables can be populated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**athenaConnectorSource** | [**CodeGenConfigurationNodeAthenaConnectorSource**](CodeGenConfigurationNodeAthenaConnectorSource.md) |  |  [optional] |
|**jdBCConnectorSource** | [**CodeGenConfigurationNodeJDBCConnectorSource**](CodeGenConfigurationNodeJDBCConnectorSource.md) |  |  [optional] |
|**sparkConnectorSource** | [**CodeGenConfigurationNodeSparkConnectorSource**](CodeGenConfigurationNodeSparkConnectorSource.md) |  |  [optional] |
|**catalogSource** | [**CodeGenConfigurationNodeCatalogSource**](CodeGenConfigurationNodeCatalogSource.md) |  |  [optional] |
|**redshiftSource** | [**CodeGenConfigurationNodeRedshiftSource**](CodeGenConfigurationNodeRedshiftSource.md) |  |  [optional] |
|**s3CatalogSource** | [**CodeGenConfigurationNodeS3CatalogSource**](CodeGenConfigurationNodeS3CatalogSource.md) |  |  [optional] |
|**s3CsvSource** | [**CodeGenConfigurationNodeS3CsvSource**](CodeGenConfigurationNodeS3CsvSource.md) |  |  [optional] |
|**s3JsonSource** | [**CodeGenConfigurationNodeS3JsonSource**](CodeGenConfigurationNodeS3JsonSource.md) |  |  [optional] |
|**s3ParquetSource** | [**CodeGenConfigurationNodeS3ParquetSource**](CodeGenConfigurationNodeS3ParquetSource.md) |  |  [optional] |
|**relationalCatalogSource** | [**CodeGenConfigurationNodeRelationalCatalogSource**](CodeGenConfigurationNodeRelationalCatalogSource.md) |  |  [optional] |
|**dynamoDBCatalogSource** | [**CodeGenConfigurationNodeDynamoDBCatalogSource**](CodeGenConfigurationNodeDynamoDBCatalogSource.md) |  |  [optional] |
|**jdBCConnectorTarget** | [**CodeGenConfigurationNodeJDBCConnectorTarget**](CodeGenConfigurationNodeJDBCConnectorTarget.md) |  |  [optional] |
|**sparkConnectorTarget** | [**CodeGenConfigurationNodeSparkConnectorTarget**](CodeGenConfigurationNodeSparkConnectorTarget.md) |  |  [optional] |
|**catalogTarget** | [**CodeGenConfigurationNodeCatalogTarget**](CodeGenConfigurationNodeCatalogTarget.md) |  |  [optional] |
|**redshiftTarget** | [**CodeGenConfigurationNodeRedshiftTarget**](CodeGenConfigurationNodeRedshiftTarget.md) |  |  [optional] |
|**s3CatalogTarget** | [**CodeGenConfigurationNodeS3CatalogTarget**](CodeGenConfigurationNodeS3CatalogTarget.md) |  |  [optional] |
|**s3GlueParquetTarget** | [**CodeGenConfigurationNodeS3GlueParquetTarget**](CodeGenConfigurationNodeS3GlueParquetTarget.md) |  |  [optional] |
|**s3DirectTarget** | [**CodeGenConfigurationNodeS3DirectTarget**](CodeGenConfigurationNodeS3DirectTarget.md) |  |  [optional] |
|**applyMapping** | [**CodeGenConfigurationNodeApplyMapping**](CodeGenConfigurationNodeApplyMapping.md) |  |  [optional] |
|**selectFields** | [**CodeGenConfigurationNodeSelectFields**](CodeGenConfigurationNodeSelectFields.md) |  |  [optional] |
|**dropFields** | [**CodeGenConfigurationNodeDropFields**](CodeGenConfigurationNodeDropFields.md) |  |  [optional] |
|**renameField** | [**CodeGenConfigurationNodeRenameField**](CodeGenConfigurationNodeRenameField.md) |  |  [optional] |
|**spigot** | [**CodeGenConfigurationNodeSpigot**](CodeGenConfigurationNodeSpigot.md) |  |  [optional] |
|**join** | [**CodeGenConfigurationNodeJoin**](CodeGenConfigurationNodeJoin.md) |  |  [optional] |
|**splitFields** | [**CodeGenConfigurationNodeSplitFields**](CodeGenConfigurationNodeSplitFields.md) |  |  [optional] |
|**selectFromCollection** | [**CodeGenConfigurationNodeSelectFromCollection**](CodeGenConfigurationNodeSelectFromCollection.md) |  |  [optional] |
|**fillMissingValues** | [**CodeGenConfigurationNodeFillMissingValues**](CodeGenConfigurationNodeFillMissingValues.md) |  |  [optional] |
|**filter** | [**CodeGenConfigurationNodeFilter**](CodeGenConfigurationNodeFilter.md) |  |  [optional] |
|**customCode** | [**CodeGenConfigurationNodeCustomCode**](CodeGenConfigurationNodeCustomCode.md) |  |  [optional] |
|**sparkSQL** | [**CodeGenConfigurationNodeSparkSQL**](CodeGenConfigurationNodeSparkSQL.md) |  |  [optional] |
|**directKinesisSource** | [**CodeGenConfigurationNodeDirectKinesisSource**](CodeGenConfigurationNodeDirectKinesisSource.md) |  |  [optional] |
|**directKafkaSource** | [**CodeGenConfigurationNodeDirectKafkaSource**](CodeGenConfigurationNodeDirectKafkaSource.md) |  |  [optional] |
|**catalogKinesisSource** | [**CodeGenConfigurationNodeCatalogKinesisSource**](CodeGenConfigurationNodeCatalogKinesisSource.md) |  |  [optional] |
|**catalogKafkaSource** | [**CodeGenConfigurationNodeCatalogKafkaSource**](CodeGenConfigurationNodeCatalogKafkaSource.md) |  |  [optional] |
|**dropNullFields** | [**CodeGenConfigurationNodeDropNullFields**](CodeGenConfigurationNodeDropNullFields.md) |  |  [optional] |
|**merge** | [**CodeGenConfigurationNodeMerge**](CodeGenConfigurationNodeMerge.md) |  |  [optional] |
|**union** | [**CodeGenConfigurationNodeUnion**](CodeGenConfigurationNodeUnion.md) |  |  [optional] |
|**piIDetection** | [**CodeGenConfigurationNodePIIDetection**](CodeGenConfigurationNodePIIDetection.md) |  |  [optional] |
|**aggregate** | [**CodeGenConfigurationNodeAggregate**](CodeGenConfigurationNodeAggregate.md) |  |  [optional] |
|**dropDuplicates** | [**CodeGenConfigurationNodeDropDuplicates**](CodeGenConfigurationNodeDropDuplicates.md) |  |  [optional] |
|**governedCatalogTarget** | [**CodeGenConfigurationNodeGovernedCatalogTarget**](CodeGenConfigurationNodeGovernedCatalogTarget.md) |  |  [optional] |
|**governedCatalogSource** | [**CodeGenConfigurationNodeGovernedCatalogSource**](CodeGenConfigurationNodeGovernedCatalogSource.md) |  |  [optional] |
|**microsoftSQLServerCatalogSource** | [**CodeGenConfigurationNodeMicrosoftSQLServerCatalogSource**](CodeGenConfigurationNodeMicrosoftSQLServerCatalogSource.md) |  |  [optional] |
|**mySQLCatalogSource** | [**CodeGenConfigurationNodeMySQLCatalogSource**](CodeGenConfigurationNodeMySQLCatalogSource.md) |  |  [optional] |
|**oracleSQLCatalogSource** | [**CodeGenConfigurationNodeOracleSQLCatalogSource**](CodeGenConfigurationNodeOracleSQLCatalogSource.md) |  |  [optional] |
|**postgreSQLCatalogSource** | [**CodeGenConfigurationNodePostgreSQLCatalogSource**](CodeGenConfigurationNodePostgreSQLCatalogSource.md) |  |  [optional] |
|**microsoftSQLServerCatalogTarget** | [**CodeGenConfigurationNodeMicrosoftSQLServerCatalogTarget**](CodeGenConfigurationNodeMicrosoftSQLServerCatalogTarget.md) |  |  [optional] |
|**mySQLCatalogTarget** | [**CodeGenConfigurationNodeMySQLCatalogTarget**](CodeGenConfigurationNodeMySQLCatalogTarget.md) |  |  [optional] |
|**oracleSQLCatalogTarget** | [**CodeGenConfigurationNodeOracleSQLCatalogTarget**](CodeGenConfigurationNodeOracleSQLCatalogTarget.md) |  |  [optional] |
|**postgreSQLCatalogTarget** | [**CodeGenConfigurationNodePostgreSQLCatalogTarget**](CodeGenConfigurationNodePostgreSQLCatalogTarget.md) |  |  [optional] |
|**dynamicTransform** | [**CodeGenConfigurationNodeDynamicTransform**](CodeGenConfigurationNodeDynamicTransform.md) |  |  [optional] |
|**evaluateDataQuality** | [**CodeGenConfigurationNodeEvaluateDataQuality**](CodeGenConfigurationNodeEvaluateDataQuality.md) |  |  [optional] |
|**s3CatalogHudiSource** | [**CodeGenConfigurationNodeS3CatalogHudiSource**](CodeGenConfigurationNodeS3CatalogHudiSource.md) |  |  [optional] |
|**catalogHudiSource** | [**CodeGenConfigurationNodeCatalogHudiSource**](CodeGenConfigurationNodeCatalogHudiSource.md) |  |  [optional] |
|**s3HudiSource** | [**CodeGenConfigurationNodeS3HudiSource**](CodeGenConfigurationNodeS3HudiSource.md) |  |  [optional] |
|**s3HudiCatalogTarget** | [**CodeGenConfigurationNodeS3HudiCatalogTarget**](CodeGenConfigurationNodeS3HudiCatalogTarget.md) |  |  [optional] |
|**s3HudiDirectTarget** | [**CodeGenConfigurationNodeS3HudiDirectTarget**](CodeGenConfigurationNodeS3HudiDirectTarget.md) |  |  [optional] |
|**directJDBCSource** | [**DirectJDBCSource**](DirectJDBCSource.md) |  |  [optional] |
|**s3CatalogDeltaSource** | [**CodeGenConfigurationNodeS3CatalogDeltaSource**](CodeGenConfigurationNodeS3CatalogDeltaSource.md) |  |  [optional] |
|**catalogDeltaSource** | [**CodeGenConfigurationNodeCatalogDeltaSource**](CodeGenConfigurationNodeCatalogDeltaSource.md) |  |  [optional] |
|**s3DeltaSource** | [**CodeGenConfigurationNodeS3DeltaSource**](CodeGenConfigurationNodeS3DeltaSource.md) |  |  [optional] |
|**s3DeltaCatalogTarget** | [**CodeGenConfigurationNodeS3DeltaCatalogTarget**](CodeGenConfigurationNodeS3DeltaCatalogTarget.md) |  |  [optional] |
|**s3DeltaDirectTarget** | [**CodeGenConfigurationNodeS3DeltaDirectTarget**](CodeGenConfigurationNodeS3DeltaDirectTarget.md) |  |  [optional] |
|**amazonRedshiftSource** | [**CodeGenConfigurationNodeAmazonRedshiftSource**](CodeGenConfigurationNodeAmazonRedshiftSource.md) |  |  [optional] |
|**amazonRedshiftTarget** | [**CodeGenConfigurationNodeAmazonRedshiftTarget**](CodeGenConfigurationNodeAmazonRedshiftTarget.md) |  |  [optional] |
|**evaluateDataQualityMultiFrame** | [**CodeGenConfigurationNodeEvaluateDataQualityMultiFrame**](CodeGenConfigurationNodeEvaluateDataQualityMultiFrame.md) |  |  [optional] |
|**recipe** | [**CodeGenConfigurationNodeRecipe**](CodeGenConfigurationNodeRecipe.md) |  |  [optional] |
|**snowflakeSource** | [**CodeGenConfigurationNodeSnowflakeSource**](CodeGenConfigurationNodeSnowflakeSource.md) |  |  [optional] |
|**snowflakeTarget** | [**CodeGenConfigurationNodeSnowflakeTarget**](CodeGenConfigurationNodeSnowflakeTarget.md) |  |  [optional] |



