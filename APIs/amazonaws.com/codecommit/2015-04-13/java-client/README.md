# openapi-java-client

AWS CodeCommit
- API version: 2015-04-13
  - Build date: 2024-10-12T12:12:31.970171-04:00[America/New_York]
  - Generator version: 7.9.0

<fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2015-04-13</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2015-04-13"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2015-04-13.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codecommit.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "CodeCommit_20150413.AssociateApprovalRuleTemplateWithRepository"; // String | 
    AssociateApprovalRuleTemplateWithRepositoryInput associateApprovalRuleTemplateWithRepositoryInput = new AssociateApprovalRuleTemplateWithRepositoryInput(); // AssociateApprovalRuleTemplateWithRepositoryInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.associateApprovalRuleTemplateWithRepository(xAmzTarget, associateApprovalRuleTemplateWithRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateApprovalRuleTemplateWithRepository");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://codecommit.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**associateApprovalRuleTemplateWithRepository**](docs/DefaultApi.md#associateApprovalRuleTemplateWithRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.AssociateApprovalRuleTemplateWithRepository | 
*DefaultApi* | [**batchAssociateApprovalRuleTemplateWithRepositories**](docs/DefaultApi.md#batchAssociateApprovalRuleTemplateWithRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchAssociateApprovalRuleTemplateWithRepositories | 
*DefaultApi* | [**batchDescribeMergeConflicts**](docs/DefaultApi.md#batchDescribeMergeConflicts) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchDescribeMergeConflicts | 
*DefaultApi* | [**batchDisassociateApprovalRuleTemplateFromRepositories**](docs/DefaultApi.md#batchDisassociateApprovalRuleTemplateFromRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchDisassociateApprovalRuleTemplateFromRepositories | 
*DefaultApi* | [**batchGetCommits**](docs/DefaultApi.md#batchGetCommits) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchGetCommits | 
*DefaultApi* | [**batchGetRepositories**](docs/DefaultApi.md#batchGetRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchGetRepositories | 
*DefaultApi* | [**createApprovalRuleTemplate**](docs/DefaultApi.md#createApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateApprovalRuleTemplate | 
*DefaultApi* | [**createBranch**](docs/DefaultApi.md#createBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateBranch | 
*DefaultApi* | [**createCommit**](docs/DefaultApi.md#createCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateCommit | 
*DefaultApi* | [**createPullRequest**](docs/DefaultApi.md#createPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreatePullRequest | 
*DefaultApi* | [**createPullRequestApprovalRule**](docs/DefaultApi.md#createPullRequestApprovalRule) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreatePullRequestApprovalRule | 
*DefaultApi* | [**createRepository**](docs/DefaultApi.md#createRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateRepository | 
*DefaultApi* | [**createUnreferencedMergeCommit**](docs/DefaultApi.md#createUnreferencedMergeCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateUnreferencedMergeCommit | 
*DefaultApi* | [**deleteApprovalRuleTemplate**](docs/DefaultApi.md#deleteApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteApprovalRuleTemplate | 
*DefaultApi* | [**deleteBranch**](docs/DefaultApi.md#deleteBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteBranch | 
*DefaultApi* | [**deleteCommentContent**](docs/DefaultApi.md#deleteCommentContent) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteCommentContent | 
*DefaultApi* | [**deleteFile**](docs/DefaultApi.md#deleteFile) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteFile | 
*DefaultApi* | [**deletePullRequestApprovalRule**](docs/DefaultApi.md#deletePullRequestApprovalRule) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeletePullRequestApprovalRule | 
*DefaultApi* | [**deleteRepository**](docs/DefaultApi.md#deleteRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteRepository | 
*DefaultApi* | [**describeMergeConflicts**](docs/DefaultApi.md#describeMergeConflicts) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DescribeMergeConflicts | 
*DefaultApi* | [**describePullRequestEvents**](docs/DefaultApi.md#describePullRequestEvents) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DescribePullRequestEvents | 
*DefaultApi* | [**disassociateApprovalRuleTemplateFromRepository**](docs/DefaultApi.md#disassociateApprovalRuleTemplateFromRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DisassociateApprovalRuleTemplateFromRepository | 
*DefaultApi* | [**evaluatePullRequestApprovalRules**](docs/DefaultApi.md#evaluatePullRequestApprovalRules) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.EvaluatePullRequestApprovalRules | 
*DefaultApi* | [**getApprovalRuleTemplate**](docs/DefaultApi.md#getApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetApprovalRuleTemplate | 
*DefaultApi* | [**getBlob**](docs/DefaultApi.md#getBlob) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetBlob | 
*DefaultApi* | [**getBranch**](docs/DefaultApi.md#getBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetBranch | 
*DefaultApi* | [**getComment**](docs/DefaultApi.md#getComment) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetComment | 
*DefaultApi* | [**getCommentReactions**](docs/DefaultApi.md#getCommentReactions) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommentReactions | 
*DefaultApi* | [**getCommentsForComparedCommit**](docs/DefaultApi.md#getCommentsForComparedCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommentsForComparedCommit | 
*DefaultApi* | [**getCommentsForPullRequest**](docs/DefaultApi.md#getCommentsForPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommentsForPullRequest | 
*DefaultApi* | [**getCommit**](docs/DefaultApi.md#getCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommit | 
*DefaultApi* | [**getDifferences**](docs/DefaultApi.md#getDifferences) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetDifferences | 
*DefaultApi* | [**getFile**](docs/DefaultApi.md#getFile) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetFile | 
*DefaultApi* | [**getFolder**](docs/DefaultApi.md#getFolder) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetFolder | 
*DefaultApi* | [**getMergeCommit**](docs/DefaultApi.md#getMergeCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetMergeCommit | 
*DefaultApi* | [**getMergeConflicts**](docs/DefaultApi.md#getMergeConflicts) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetMergeConflicts | 
*DefaultApi* | [**getMergeOptions**](docs/DefaultApi.md#getMergeOptions) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetMergeOptions | 
*DefaultApi* | [**getPullRequest**](docs/DefaultApi.md#getPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetPullRequest | 
*DefaultApi* | [**getPullRequestApprovalStates**](docs/DefaultApi.md#getPullRequestApprovalStates) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetPullRequestApprovalStates | 
*DefaultApi* | [**getPullRequestOverrideState**](docs/DefaultApi.md#getPullRequestOverrideState) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetPullRequestOverrideState | 
*DefaultApi* | [**getRepository**](docs/DefaultApi.md#getRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetRepository | 
*DefaultApi* | [**getRepositoryTriggers**](docs/DefaultApi.md#getRepositoryTriggers) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetRepositoryTriggers | 
*DefaultApi* | [**listApprovalRuleTemplates**](docs/DefaultApi.md#listApprovalRuleTemplates) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListApprovalRuleTemplates | 
*DefaultApi* | [**listAssociatedApprovalRuleTemplatesForRepository**](docs/DefaultApi.md#listAssociatedApprovalRuleTemplatesForRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListAssociatedApprovalRuleTemplatesForRepository | 
*DefaultApi* | [**listBranches**](docs/DefaultApi.md#listBranches) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListBranches | 
*DefaultApi* | [**listPullRequests**](docs/DefaultApi.md#listPullRequests) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListPullRequests | 
*DefaultApi* | [**listRepositories**](docs/DefaultApi.md#listRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListRepositories | 
*DefaultApi* | [**listRepositoriesForApprovalRuleTemplate**](docs/DefaultApi.md#listRepositoriesForApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListRepositoriesForApprovalRuleTemplate | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListTagsForResource | 
*DefaultApi* | [**mergeBranchesByFastForward**](docs/DefaultApi.md#mergeBranchesByFastForward) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergeBranchesByFastForward | 
*DefaultApi* | [**mergeBranchesBySquash**](docs/DefaultApi.md#mergeBranchesBySquash) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergeBranchesBySquash | 
*DefaultApi* | [**mergeBranchesByThreeWay**](docs/DefaultApi.md#mergeBranchesByThreeWay) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergeBranchesByThreeWay | 
*DefaultApi* | [**mergePullRequestByFastForward**](docs/DefaultApi.md#mergePullRequestByFastForward) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergePullRequestByFastForward | 
*DefaultApi* | [**mergePullRequestBySquash**](docs/DefaultApi.md#mergePullRequestBySquash) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergePullRequestBySquash | 
*DefaultApi* | [**mergePullRequestByThreeWay**](docs/DefaultApi.md#mergePullRequestByThreeWay) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergePullRequestByThreeWay | 
*DefaultApi* | [**overridePullRequestApprovalRules**](docs/DefaultApi.md#overridePullRequestApprovalRules) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.OverridePullRequestApprovalRules | 
*DefaultApi* | [**postCommentForComparedCommit**](docs/DefaultApi.md#postCommentForComparedCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PostCommentForComparedCommit | 
*DefaultApi* | [**postCommentForPullRequest**](docs/DefaultApi.md#postCommentForPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PostCommentForPullRequest | 
*DefaultApi* | [**postCommentReply**](docs/DefaultApi.md#postCommentReply) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PostCommentReply | 
*DefaultApi* | [**putCommentReaction**](docs/DefaultApi.md#putCommentReaction) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PutCommentReaction | 
*DefaultApi* | [**putFile**](docs/DefaultApi.md#putFile) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PutFile | 
*DefaultApi* | [**putRepositoryTriggers**](docs/DefaultApi.md#putRepositoryTriggers) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PutRepositoryTriggers | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.TagResource | 
*DefaultApi* | [**testRepositoryTriggers**](docs/DefaultApi.md#testRepositoryTriggers) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.TestRepositoryTriggers | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UntagResource | 
*DefaultApi* | [**updateApprovalRuleTemplateContent**](docs/DefaultApi.md#updateApprovalRuleTemplateContent) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateApprovalRuleTemplateContent | 
*DefaultApi* | [**updateApprovalRuleTemplateDescription**](docs/DefaultApi.md#updateApprovalRuleTemplateDescription) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateApprovalRuleTemplateDescription | 
*DefaultApi* | [**updateApprovalRuleTemplateName**](docs/DefaultApi.md#updateApprovalRuleTemplateName) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateApprovalRuleTemplateName | 
*DefaultApi* | [**updateComment**](docs/DefaultApi.md#updateComment) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateComment | 
*DefaultApi* | [**updateDefaultBranch**](docs/DefaultApi.md#updateDefaultBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateDefaultBranch | 
*DefaultApi* | [**updatePullRequestApprovalRuleContent**](docs/DefaultApi.md#updatePullRequestApprovalRuleContent) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestApprovalRuleContent | 
*DefaultApi* | [**updatePullRequestApprovalState**](docs/DefaultApi.md#updatePullRequestApprovalState) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestApprovalState | 
*DefaultApi* | [**updatePullRequestDescription**](docs/DefaultApi.md#updatePullRequestDescription) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestDescription | 
*DefaultApi* | [**updatePullRequestStatus**](docs/DefaultApi.md#updatePullRequestStatus) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestStatus | 
*DefaultApi* | [**updatePullRequestTitle**](docs/DefaultApi.md#updatePullRequestTitle) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestTitle | 
*DefaultApi* | [**updateRepositoryDescription**](docs/DefaultApi.md#updateRepositoryDescription) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateRepositoryDescription | 
*DefaultApi* | [**updateRepositoryName**](docs/DefaultApi.md#updateRepositoryName) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateRepositoryName | 


## Documentation for Models

 - [Approval](docs/Approval.md)
 - [ApprovalRule](docs/ApprovalRule.md)
 - [ApprovalRuleEventMetadata](docs/ApprovalRuleEventMetadata.md)
 - [ApprovalRuleOriginApprovalRuleTemplate](docs/ApprovalRuleOriginApprovalRuleTemplate.md)
 - [ApprovalRuleOverriddenEventMetadata](docs/ApprovalRuleOverriddenEventMetadata.md)
 - [ApprovalRuleTemplate](docs/ApprovalRuleTemplate.md)
 - [ApprovalState](docs/ApprovalState.md)
 - [ApprovalStateChangedEventMetadata](docs/ApprovalStateChangedEventMetadata.md)
 - [AssociateApprovalRuleTemplateWithRepositoryInput](docs/AssociateApprovalRuleTemplateWithRepositoryInput.md)
 - [BatchAssociateApprovalRuleTemplateWithRepositoriesError](docs/BatchAssociateApprovalRuleTemplateWithRepositoriesError.md)
 - [BatchAssociateApprovalRuleTemplateWithRepositoriesInput](docs/BatchAssociateApprovalRuleTemplateWithRepositoriesInput.md)
 - [BatchAssociateApprovalRuleTemplateWithRepositoriesOutput](docs/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput.md)
 - [BatchDescribeMergeConflictsError](docs/BatchDescribeMergeConflictsError.md)
 - [BatchDescribeMergeConflictsInput](docs/BatchDescribeMergeConflictsInput.md)
 - [BatchDescribeMergeConflictsOutput](docs/BatchDescribeMergeConflictsOutput.md)
 - [BatchDisassociateApprovalRuleTemplateFromRepositoriesError](docs/BatchDisassociateApprovalRuleTemplateFromRepositoriesError.md)
 - [BatchDisassociateApprovalRuleTemplateFromRepositoriesInput](docs/BatchDisassociateApprovalRuleTemplateFromRepositoriesInput.md)
 - [BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput](docs/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput.md)
 - [BatchGetCommitsError](docs/BatchGetCommitsError.md)
 - [BatchGetCommitsInput](docs/BatchGetCommitsInput.md)
 - [BatchGetCommitsOutput](docs/BatchGetCommitsOutput.md)
 - [BatchGetRepositoriesInput](docs/BatchGetRepositoriesInput.md)
 - [BatchGetRepositoriesOutput](docs/BatchGetRepositoriesOutput.md)
 - [BlobMetadata](docs/BlobMetadata.md)
 - [BranchInfo](docs/BranchInfo.md)
 - [ChangeTypeEnum](docs/ChangeTypeEnum.md)
 - [Comment](docs/Comment.md)
 - [CommentsForComparedCommit](docs/CommentsForComparedCommit.md)
 - [CommentsForComparedCommitLocation](docs/CommentsForComparedCommitLocation.md)
 - [CommentsForPullRequest](docs/CommentsForPullRequest.md)
 - [CommentsForPullRequestLocation](docs/CommentsForPullRequestLocation.md)
 - [Commit](docs/Commit.md)
 - [CommitAuthor](docs/CommitAuthor.md)
 - [CommitCommitter](docs/CommitCommitter.md)
 - [Conflict](docs/Conflict.md)
 - [ConflictConflictMetadata](docs/ConflictConflictMetadata.md)
 - [ConflictDetailLevelTypeEnum](docs/ConflictDetailLevelTypeEnum.md)
 - [ConflictMetadata](docs/ConflictMetadata.md)
 - [ConflictMetadataFileModes](docs/ConflictMetadataFileModes.md)
 - [ConflictMetadataFileSizes](docs/ConflictMetadataFileSizes.md)
 - [ConflictMetadataIsBinaryFile](docs/ConflictMetadataIsBinaryFile.md)
 - [ConflictMetadataMergeOperations](docs/ConflictMetadataMergeOperations.md)
 - [ConflictMetadataObjectTypes](docs/ConflictMetadataObjectTypes.md)
 - [ConflictResolution](docs/ConflictResolution.md)
 - [ConflictResolutionStrategyTypeEnum](docs/ConflictResolutionStrategyTypeEnum.md)
 - [CreateApprovalRuleTemplateInput](docs/CreateApprovalRuleTemplateInput.md)
 - [CreateApprovalRuleTemplateOutput](docs/CreateApprovalRuleTemplateOutput.md)
 - [CreateApprovalRuleTemplateOutputApprovalRuleTemplate](docs/CreateApprovalRuleTemplateOutputApprovalRuleTemplate.md)
 - [CreateBranchInput](docs/CreateBranchInput.md)
 - [CreateCommitInput](docs/CreateCommitInput.md)
 - [CreateCommitOutput](docs/CreateCommitOutput.md)
 - [CreatePullRequestApprovalRuleInput](docs/CreatePullRequestApprovalRuleInput.md)
 - [CreatePullRequestApprovalRuleOutput](docs/CreatePullRequestApprovalRuleOutput.md)
 - [CreatePullRequestApprovalRuleOutputApprovalRule](docs/CreatePullRequestApprovalRuleOutputApprovalRule.md)
 - [CreatePullRequestInput](docs/CreatePullRequestInput.md)
 - [CreatePullRequestOutput](docs/CreatePullRequestOutput.md)
 - [CreatePullRequestOutputPullRequest](docs/CreatePullRequestOutputPullRequest.md)
 - [CreateRepositoryInput](docs/CreateRepositoryInput.md)
 - [CreateRepositoryOutput](docs/CreateRepositoryOutput.md)
 - [CreateRepositoryOutputRepositoryMetadata](docs/CreateRepositoryOutputRepositoryMetadata.md)
 - [CreateUnreferencedMergeCommitInput](docs/CreateUnreferencedMergeCommitInput.md)
 - [CreateUnreferencedMergeCommitInputConflictResolution](docs/CreateUnreferencedMergeCommitInputConflictResolution.md)
 - [CreateUnreferencedMergeCommitOutput](docs/CreateUnreferencedMergeCommitOutput.md)
 - [DeleteApprovalRuleTemplateInput](docs/DeleteApprovalRuleTemplateInput.md)
 - [DeleteApprovalRuleTemplateOutput](docs/DeleteApprovalRuleTemplateOutput.md)
 - [DeleteBranchInput](docs/DeleteBranchInput.md)
 - [DeleteBranchOutput](docs/DeleteBranchOutput.md)
 - [DeleteBranchOutputDeletedBranch](docs/DeleteBranchOutputDeletedBranch.md)
 - [DeleteCommentContentInput](docs/DeleteCommentContentInput.md)
 - [DeleteCommentContentOutput](docs/DeleteCommentContentOutput.md)
 - [DeleteCommentContentOutputComment](docs/DeleteCommentContentOutputComment.md)
 - [DeleteFileEntry](docs/DeleteFileEntry.md)
 - [DeleteFileInput](docs/DeleteFileInput.md)
 - [DeleteFileOutput](docs/DeleteFileOutput.md)
 - [DeletePullRequestApprovalRuleInput](docs/DeletePullRequestApprovalRuleInput.md)
 - [DeletePullRequestApprovalRuleOutput](docs/DeletePullRequestApprovalRuleOutput.md)
 - [DeleteRepositoryInput](docs/DeleteRepositoryInput.md)
 - [DeleteRepositoryOutput](docs/DeleteRepositoryOutput.md)
 - [DescribeMergeConflictsInput](docs/DescribeMergeConflictsInput.md)
 - [DescribeMergeConflictsOutput](docs/DescribeMergeConflictsOutput.md)
 - [DescribeMergeConflictsOutputConflictMetadata](docs/DescribeMergeConflictsOutputConflictMetadata.md)
 - [DescribePullRequestEventsInput](docs/DescribePullRequestEventsInput.md)
 - [DescribePullRequestEventsOutput](docs/DescribePullRequestEventsOutput.md)
 - [Difference](docs/Difference.md)
 - [DifferenceAfterBlob](docs/DifferenceAfterBlob.md)
 - [DifferenceBeforeBlob](docs/DifferenceBeforeBlob.md)
 - [DisassociateApprovalRuleTemplateFromRepositoryInput](docs/DisassociateApprovalRuleTemplateFromRepositoryInput.md)
 - [EvaluatePullRequestApprovalRulesInput](docs/EvaluatePullRequestApprovalRulesInput.md)
 - [EvaluatePullRequestApprovalRulesOutput](docs/EvaluatePullRequestApprovalRulesOutput.md)
 - [EvaluatePullRequestApprovalRulesOutputEvaluation](docs/EvaluatePullRequestApprovalRulesOutputEvaluation.md)
 - [Evaluation](docs/Evaluation.md)
 - [FileMetadata](docs/FileMetadata.md)
 - [FileModeTypeEnum](docs/FileModeTypeEnum.md)
 - [FileModes](docs/FileModes.md)
 - [FileSizes](docs/FileSizes.md)
 - [Folder](docs/Folder.md)
 - [GetApprovalRuleTemplateInput](docs/GetApprovalRuleTemplateInput.md)
 - [GetApprovalRuleTemplateOutput](docs/GetApprovalRuleTemplateOutput.md)
 - [GetApprovalRuleTemplateOutputApprovalRuleTemplate](docs/GetApprovalRuleTemplateOutputApprovalRuleTemplate.md)
 - [GetBlobInput](docs/GetBlobInput.md)
 - [GetBlobOutput](docs/GetBlobOutput.md)
 - [GetBranchInput](docs/GetBranchInput.md)
 - [GetBranchOutput](docs/GetBranchOutput.md)
 - [GetBranchOutputBranch](docs/GetBranchOutputBranch.md)
 - [GetCommentInput](docs/GetCommentInput.md)
 - [GetCommentOutput](docs/GetCommentOutput.md)
 - [GetCommentOutputComment](docs/GetCommentOutputComment.md)
 - [GetCommentReactionsInput](docs/GetCommentReactionsInput.md)
 - [GetCommentReactionsOutput](docs/GetCommentReactionsOutput.md)
 - [GetCommentsForComparedCommitInput](docs/GetCommentsForComparedCommitInput.md)
 - [GetCommentsForComparedCommitOutput](docs/GetCommentsForComparedCommitOutput.md)
 - [GetCommentsForPullRequestInput](docs/GetCommentsForPullRequestInput.md)
 - [GetCommentsForPullRequestOutput](docs/GetCommentsForPullRequestOutput.md)
 - [GetCommitInput](docs/GetCommitInput.md)
 - [GetCommitOutput](docs/GetCommitOutput.md)
 - [GetCommitOutputCommit](docs/GetCommitOutputCommit.md)
 - [GetDifferencesInput](docs/GetDifferencesInput.md)
 - [GetDifferencesOutput](docs/GetDifferencesOutput.md)
 - [GetFileInput](docs/GetFileInput.md)
 - [GetFileOutput](docs/GetFileOutput.md)
 - [GetFolderInput](docs/GetFolderInput.md)
 - [GetFolderOutput](docs/GetFolderOutput.md)
 - [GetMergeCommitInput](docs/GetMergeCommitInput.md)
 - [GetMergeCommitOutput](docs/GetMergeCommitOutput.md)
 - [GetMergeConflictsInput](docs/GetMergeConflictsInput.md)
 - [GetMergeConflictsOutput](docs/GetMergeConflictsOutput.md)
 - [GetMergeOptionsInput](docs/GetMergeOptionsInput.md)
 - [GetMergeOptionsOutput](docs/GetMergeOptionsOutput.md)
 - [GetPullRequestApprovalStatesInput](docs/GetPullRequestApprovalStatesInput.md)
 - [GetPullRequestApprovalStatesOutput](docs/GetPullRequestApprovalStatesOutput.md)
 - [GetPullRequestInput](docs/GetPullRequestInput.md)
 - [GetPullRequestOutput](docs/GetPullRequestOutput.md)
 - [GetPullRequestOutputPullRequest](docs/GetPullRequestOutputPullRequest.md)
 - [GetPullRequestOverrideStateInput](docs/GetPullRequestOverrideStateInput.md)
 - [GetPullRequestOverrideStateOutput](docs/GetPullRequestOverrideStateOutput.md)
 - [GetRepositoryInput](docs/GetRepositoryInput.md)
 - [GetRepositoryOutput](docs/GetRepositoryOutput.md)
 - [GetRepositoryOutputRepositoryMetadata](docs/GetRepositoryOutputRepositoryMetadata.md)
 - [GetRepositoryTriggersInput](docs/GetRepositoryTriggersInput.md)
 - [GetRepositoryTriggersOutput](docs/GetRepositoryTriggersOutput.md)
 - [IsBinaryFile](docs/IsBinaryFile.md)
 - [ListApprovalRuleTemplatesInput](docs/ListApprovalRuleTemplatesInput.md)
 - [ListApprovalRuleTemplatesOutput](docs/ListApprovalRuleTemplatesOutput.md)
 - [ListAssociatedApprovalRuleTemplatesForRepositoryInput](docs/ListAssociatedApprovalRuleTemplatesForRepositoryInput.md)
 - [ListAssociatedApprovalRuleTemplatesForRepositoryOutput](docs/ListAssociatedApprovalRuleTemplatesForRepositoryOutput.md)
 - [ListBranchesInput](docs/ListBranchesInput.md)
 - [ListBranchesOutput](docs/ListBranchesOutput.md)
 - [ListPullRequestsInput](docs/ListPullRequestsInput.md)
 - [ListPullRequestsOutput](docs/ListPullRequestsOutput.md)
 - [ListRepositoriesForApprovalRuleTemplateInput](docs/ListRepositoriesForApprovalRuleTemplateInput.md)
 - [ListRepositoriesForApprovalRuleTemplateOutput](docs/ListRepositoriesForApprovalRuleTemplateOutput.md)
 - [ListRepositoriesInput](docs/ListRepositoriesInput.md)
 - [ListRepositoriesOutput](docs/ListRepositoriesOutput.md)
 - [ListTagsForResourceInput](docs/ListTagsForResourceInput.md)
 - [ListTagsForResourceOutput](docs/ListTagsForResourceOutput.md)
 - [Location](docs/Location.md)
 - [MergeBranchesByFastForwardInput](docs/MergeBranchesByFastForwardInput.md)
 - [MergeBranchesByFastForwardOutput](docs/MergeBranchesByFastForwardOutput.md)
 - [MergeBranchesBySquashInput](docs/MergeBranchesBySquashInput.md)
 - [MergeBranchesBySquashOutput](docs/MergeBranchesBySquashOutput.md)
 - [MergeBranchesByThreeWayInput](docs/MergeBranchesByThreeWayInput.md)
 - [MergeBranchesByThreeWayOutput](docs/MergeBranchesByThreeWayOutput.md)
 - [MergeHunk](docs/MergeHunk.md)
 - [MergeHunkBase](docs/MergeHunkBase.md)
 - [MergeHunkDestination](docs/MergeHunkDestination.md)
 - [MergeHunkDetail](docs/MergeHunkDetail.md)
 - [MergeHunkSource](docs/MergeHunkSource.md)
 - [MergeMetadata](docs/MergeMetadata.md)
 - [MergeOperations](docs/MergeOperations.md)
 - [MergeOptionTypeEnum](docs/MergeOptionTypeEnum.md)
 - [MergePullRequestByFastForwardInput](docs/MergePullRequestByFastForwardInput.md)
 - [MergePullRequestByFastForwardOutput](docs/MergePullRequestByFastForwardOutput.md)
 - [MergePullRequestByFastForwardOutputPullRequest](docs/MergePullRequestByFastForwardOutputPullRequest.md)
 - [MergePullRequestBySquashInput](docs/MergePullRequestBySquashInput.md)
 - [MergePullRequestBySquashOutput](docs/MergePullRequestBySquashOutput.md)
 - [MergePullRequestByThreeWayInput](docs/MergePullRequestByThreeWayInput.md)
 - [MergePullRequestByThreeWayOutput](docs/MergePullRequestByThreeWayOutput.md)
 - [ModelFile](docs/ModelFile.md)
 - [ObjectTypeEnum](docs/ObjectTypeEnum.md)
 - [ObjectTypes](docs/ObjectTypes.md)
 - [OrderEnum](docs/OrderEnum.md)
 - [OriginApprovalRuleTemplate](docs/OriginApprovalRuleTemplate.md)
 - [OverridePullRequestApprovalRulesInput](docs/OverridePullRequestApprovalRulesInput.md)
 - [OverrideStatus](docs/OverrideStatus.md)
 - [PostCommentForComparedCommitInput](docs/PostCommentForComparedCommitInput.md)
 - [PostCommentForComparedCommitInputLocation](docs/PostCommentForComparedCommitInputLocation.md)
 - [PostCommentForComparedCommitOutput](docs/PostCommentForComparedCommitOutput.md)
 - [PostCommentForComparedCommitOutputComment](docs/PostCommentForComparedCommitOutputComment.md)
 - [PostCommentForComparedCommitOutputLocation](docs/PostCommentForComparedCommitOutputLocation.md)
 - [PostCommentForPullRequestInput](docs/PostCommentForPullRequestInput.md)
 - [PostCommentForPullRequestInputLocation](docs/PostCommentForPullRequestInputLocation.md)
 - [PostCommentForPullRequestOutput](docs/PostCommentForPullRequestOutput.md)
 - [PostCommentForPullRequestOutputLocation](docs/PostCommentForPullRequestOutputLocation.md)
 - [PostCommentReplyInput](docs/PostCommentReplyInput.md)
 - [PostCommentReplyOutput](docs/PostCommentReplyOutput.md)
 - [PostCommentReplyOutputComment](docs/PostCommentReplyOutputComment.md)
 - [PullRequest](docs/PullRequest.md)
 - [PullRequestCreatedEventMetadata](docs/PullRequestCreatedEventMetadata.md)
 - [PullRequestEvent](docs/PullRequestEvent.md)
 - [PullRequestEventApprovalRuleEventMetadata](docs/PullRequestEventApprovalRuleEventMetadata.md)
 - [PullRequestEventApprovalRuleOverriddenEventMetadata](docs/PullRequestEventApprovalRuleOverriddenEventMetadata.md)
 - [PullRequestEventApprovalStateChangedEventMetadata](docs/PullRequestEventApprovalStateChangedEventMetadata.md)
 - [PullRequestEventPullRequestCreatedEventMetadata](docs/PullRequestEventPullRequestCreatedEventMetadata.md)
 - [PullRequestEventPullRequestMergedStateChangedEventMetadata](docs/PullRequestEventPullRequestMergedStateChangedEventMetadata.md)
 - [PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata](docs/PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata.md)
 - [PullRequestEventPullRequestStatusChangedEventMetadata](docs/PullRequestEventPullRequestStatusChangedEventMetadata.md)
 - [PullRequestEventType](docs/PullRequestEventType.md)
 - [PullRequestMergedStateChangedEventMetadata](docs/PullRequestMergedStateChangedEventMetadata.md)
 - [PullRequestMergedStateChangedEventMetadataMergeMetadata](docs/PullRequestMergedStateChangedEventMetadataMergeMetadata.md)
 - [PullRequestSourceReferenceUpdatedEventMetadata](docs/PullRequestSourceReferenceUpdatedEventMetadata.md)
 - [PullRequestStatusChangedEventMetadata](docs/PullRequestStatusChangedEventMetadata.md)
 - [PullRequestStatusEnum](docs/PullRequestStatusEnum.md)
 - [PullRequestTarget](docs/PullRequestTarget.md)
 - [PullRequestTargetMergeMetadata](docs/PullRequestTargetMergeMetadata.md)
 - [PutCommentReactionInput](docs/PutCommentReactionInput.md)
 - [PutFileEntry](docs/PutFileEntry.md)
 - [PutFileEntrySourceFile](docs/PutFileEntrySourceFile.md)
 - [PutFileInput](docs/PutFileInput.md)
 - [PutFileOutput](docs/PutFileOutput.md)
 - [PutRepositoryTriggersInput](docs/PutRepositoryTriggersInput.md)
 - [PutRepositoryTriggersOutput](docs/PutRepositoryTriggersOutput.md)
 - [ReactionForComment](docs/ReactionForComment.md)
 - [ReactionForCommentReaction](docs/ReactionForCommentReaction.md)
 - [ReactionValueFormats](docs/ReactionValueFormats.md)
 - [RelativeFileVersionEnum](docs/RelativeFileVersionEnum.md)
 - [ReplaceContentEntry](docs/ReplaceContentEntry.md)
 - [ReplacementTypeEnum](docs/ReplacementTypeEnum.md)
 - [RepositoryMetadata](docs/RepositoryMetadata.md)
 - [RepositoryNameIdPair](docs/RepositoryNameIdPair.md)
 - [RepositoryTrigger](docs/RepositoryTrigger.md)
 - [RepositoryTriggerEventEnum](docs/RepositoryTriggerEventEnum.md)
 - [RepositoryTriggerExecutionFailure](docs/RepositoryTriggerExecutionFailure.md)
 - [SetFileModeEntry](docs/SetFileModeEntry.md)
 - [SortByEnum](docs/SortByEnum.md)
 - [SourceFileSpecifier](docs/SourceFileSpecifier.md)
 - [SubModule](docs/SubModule.md)
 - [SymbolicLink](docs/SymbolicLink.md)
 - [TagResourceInput](docs/TagResourceInput.md)
 - [Target](docs/Target.md)
 - [TestRepositoryTriggersInput](docs/TestRepositoryTriggersInput.md)
 - [TestRepositoryTriggersOutput](docs/TestRepositoryTriggersOutput.md)
 - [UntagResourceInput](docs/UntagResourceInput.md)
 - [UpdateApprovalRuleTemplateContentInput](docs/UpdateApprovalRuleTemplateContentInput.md)
 - [UpdateApprovalRuleTemplateContentOutput](docs/UpdateApprovalRuleTemplateContentOutput.md)
 - [UpdateApprovalRuleTemplateDescriptionInput](docs/UpdateApprovalRuleTemplateDescriptionInput.md)
 - [UpdateApprovalRuleTemplateDescriptionOutput](docs/UpdateApprovalRuleTemplateDescriptionOutput.md)
 - [UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate](docs/UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate.md)
 - [UpdateApprovalRuleTemplateNameInput](docs/UpdateApprovalRuleTemplateNameInput.md)
 - [UpdateApprovalRuleTemplateNameOutput](docs/UpdateApprovalRuleTemplateNameOutput.md)
 - [UpdateCommentInput](docs/UpdateCommentInput.md)
 - [UpdateCommentOutput](docs/UpdateCommentOutput.md)
 - [UpdateCommentOutputComment](docs/UpdateCommentOutputComment.md)
 - [UpdateDefaultBranchInput](docs/UpdateDefaultBranchInput.md)
 - [UpdatePullRequestApprovalRuleContentInput](docs/UpdatePullRequestApprovalRuleContentInput.md)
 - [UpdatePullRequestApprovalRuleContentOutput](docs/UpdatePullRequestApprovalRuleContentOutput.md)
 - [UpdatePullRequestApprovalRuleContentOutputApprovalRule](docs/UpdatePullRequestApprovalRuleContentOutputApprovalRule.md)
 - [UpdatePullRequestApprovalStateInput](docs/UpdatePullRequestApprovalStateInput.md)
 - [UpdatePullRequestDescriptionInput](docs/UpdatePullRequestDescriptionInput.md)
 - [UpdatePullRequestDescriptionOutput](docs/UpdatePullRequestDescriptionOutput.md)
 - [UpdatePullRequestDescriptionOutputPullRequest](docs/UpdatePullRequestDescriptionOutputPullRequest.md)
 - [UpdatePullRequestStatusInput](docs/UpdatePullRequestStatusInput.md)
 - [UpdatePullRequestStatusOutput](docs/UpdatePullRequestStatusOutput.md)
 - [UpdatePullRequestStatusOutputPullRequest](docs/UpdatePullRequestStatusOutputPullRequest.md)
 - [UpdatePullRequestTitleInput](docs/UpdatePullRequestTitleInput.md)
 - [UpdatePullRequestTitleOutput](docs/UpdatePullRequestTitleOutput.md)
 - [UpdateRepositoryDescriptionInput](docs/UpdateRepositoryDescriptionInput.md)
 - [UpdateRepositoryNameInput](docs/UpdateRepositoryNameInput.md)
 - [UserInfo](docs/UserInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="hmac"></a>
### hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

mike.ralphson@gmail.com

