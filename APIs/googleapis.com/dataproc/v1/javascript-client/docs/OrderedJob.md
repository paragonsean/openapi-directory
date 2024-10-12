# CloudDataprocApi.OrderedJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flinkJob** | [**FlinkJob**](FlinkJob.md) |  | [optional] 
**hadoopJob** | [**HadoopJob**](HadoopJob.md) |  | [optional] 
**hiveJob** | [**HiveJob**](HiveJob.md) |  | [optional] 
**labels** | **{String: String}** | Optional. The labels to associate with this job.Label keys must be between 1 and 63 characters long, and must conform to the following regular expression: \\p{Ll}\\p{Lo}{0,62}Label values must be between 1 and 63 characters long, and must conform to the following regular expression: \\p{Ll}\\p{Lo}\\p{N}_-{0,63}No more than 32 labels can be associated with a given job. | [optional] 
**pigJob** | [**PigJob**](PigJob.md) |  | [optional] 
**prerequisiteStepIds** | **[String]** | Optional. The optional list of prerequisite job step_ids. If not specified, the job will start at the beginning of workflow. | [optional] 
**prestoJob** | [**PrestoJob**](PrestoJob.md) |  | [optional] 
**pysparkJob** | [**PySparkJob**](PySparkJob.md) |  | [optional] 
**scheduling** | [**JobScheduling**](JobScheduling.md) |  | [optional] 
**sparkJob** | [**SparkJob**](SparkJob.md) |  | [optional] 
**sparkRJob** | [**SparkRJob**](SparkRJob.md) |  | [optional] 
**sparkSqlJob** | [**SparkSqlJob**](SparkSqlJob.md) |  | [optional] 
**stepId** | **String** | Required. The step id. The id must be unique among all jobs within the template.The step id is used as prefix for job id, as job goog-dataproc-workflow-step-id label, and in prerequisiteStepIds field from other steps.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. | [optional] 
**trinoJob** | [**TrinoJob**](TrinoJob.md) |  | [optional] 


