# Inspector2.UpdateEc2DeepInspectionConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activateDeepInspection** | **Boolean** | Specify &lt;code&gt;TRUE&lt;/code&gt; to activate Amazon Inspector deep inspection in your account, or &lt;code&gt;FALSE&lt;/code&gt; to deactivate. Member accounts in an organization cannot deactivate deep inspection, instead the delegated administrator for the organization can deactivate a member account using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html\&quot;&gt;BatchUpdateMemberEc2DeepInspectionStatus&lt;/a&gt;. | [optional] 
**packagePaths** | **[String]** | The Amazon Inspector deep inspection custom paths you are adding for your account. | [optional] 


