# AwsRoboMaker.CreateRobotApplicationVersionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **String** | The application information for the robot application. | 
**currentRevisionId** | **String** | The current revision id for the robot application. If you provide a value and it matches the latest revision ID, a new version will be created. | [optional] 
**s3Etags** | **[String]** | The Amazon S3 identifier for the zip file bundle that you use for your robot application. | [optional] 
**imageDigest** | **String** | A SHA256 identifier for the Docker image that you use for your robot application. | [optional] 


