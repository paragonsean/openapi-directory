# CloudDataFusionApi.DataResidencyAugmentedView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crGopoGuris** | **[String]** | Cloud resource to Google owned production object mapping in the form of GURIs. The GURIs should be available in DG KB storage/cns tables. This is the preferred way of providing cloud resource mappings. For further details please read go/cloud-resource-monitoring_sig | [optional] 
**crGopoPrefixes** | **[String]** | Cloud resource to Google owned production object mapping in the form of prefixes. These should be available in DG KB storage/cns tables. The entity type, which is the part of the string before the first colon in the GURI, must be completely specified in prefix. For details about GURI please read go/guri. For further details about the field please read go/cloud-resource-monitoring_sig. | [optional] 
**serviceData** | [**ServiceData**](ServiceData.md) |  | [optional] 
**tpIds** | **[String]** | The list of project_id&#39;s of the tenant projects in the &#39;google.com&#39; org which serve the Cloud Resource. See go/drz-mst-sig for more details. | [optional] 


