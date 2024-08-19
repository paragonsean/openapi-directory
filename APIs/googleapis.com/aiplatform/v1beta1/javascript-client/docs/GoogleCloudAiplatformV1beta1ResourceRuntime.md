# VertexAiApi.GoogleCloudAiplatformV1beta1ResourceRuntime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessUris** | **{String: String}** | Output only. URIs for user to connect to the Cluster. Example: { \&quot;RAY_HEAD_NODE_INTERNAL_IP\&quot;: \&quot;head-node-IP:10001\&quot; \&quot;RAY_DASHBOARD_URI\&quot;: \&quot;ray-dashboard-address:8888\&quot; } | [optional] [readonly] 
**notebookRuntimeTemplate** | **String** | Output only. The resource name of NotebookRuntimeTemplate for the RoV Persistent Cluster The NotebokRuntimeTemplate is created in the same VPC (if set), and with the same Ray and Python version as the Persistent Cluster. Example: \&quot;projects/1000/locations/us-central1/notebookRuntimeTemplates/abc123\&quot; | [optional] [readonly] 


