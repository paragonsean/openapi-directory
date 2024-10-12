# AmazonCodeGuruReviewer.CreateCodeReviewRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the code review. The name of each code review in your Amazon Web Services account must be unique. | 
**repositoryAssociationArn** | **String** | &lt;p&gt;The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A code review can only be created on an associated repository. This is the ARN of the associated repository.&lt;/p&gt; | 
**type** | [**CreateCodeReviewRequestType**](CreateCodeReviewRequestType.md) |  | 
**clientRequestToken** | **String** | Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate code reviews if there are failures and retries. | [optional] 


