# aws_code_commit

AwsCodeCommit - JavaScript client for aws_code_commit
<fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2015-04-13
- Package version: 2015-04-13
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install aws_code_commit --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your aws_code_commit from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var AwsCodeCommit = require('aws_code_commit');

var defaultClient = AwsCodeCommit.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new AwsCodeCommit.DefaultApi()
var xAmzTarget = "xAmzTarget_example"; // {String} 
var associateApprovalRuleTemplateWithRepositoryInput = new AwsCodeCommit.AssociateApprovalRuleTemplateWithRepositoryInput(); // {AssociateApprovalRuleTemplateWithRepositoryInput} 
var opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // {String} 
  'xAmzDate': "xAmzDate_example", // {String} 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // {String} 
  'xAmzCredential': "xAmzCredential_example", // {String} 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // {String} 
  'xAmzSignature': "xAmzSignature_example", // {String} 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.associateApprovalRuleTemplateWithRepository(xAmzTarget, associateApprovalRuleTemplateWithRepositoryInput, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://codecommit.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AwsCodeCommit.DefaultApi* | [**associateApprovalRuleTemplateWithRepository**](docs/DefaultApi.md#associateApprovalRuleTemplateWithRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.AssociateApprovalRuleTemplateWithRepository | 
*AwsCodeCommit.DefaultApi* | [**batchAssociateApprovalRuleTemplateWithRepositories**](docs/DefaultApi.md#batchAssociateApprovalRuleTemplateWithRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchAssociateApprovalRuleTemplateWithRepositories | 
*AwsCodeCommit.DefaultApi* | [**batchDescribeMergeConflicts**](docs/DefaultApi.md#batchDescribeMergeConflicts) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchDescribeMergeConflicts | 
*AwsCodeCommit.DefaultApi* | [**batchDisassociateApprovalRuleTemplateFromRepositories**](docs/DefaultApi.md#batchDisassociateApprovalRuleTemplateFromRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchDisassociateApprovalRuleTemplateFromRepositories | 
*AwsCodeCommit.DefaultApi* | [**batchGetCommits**](docs/DefaultApi.md#batchGetCommits) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchGetCommits | 
*AwsCodeCommit.DefaultApi* | [**batchGetRepositories**](docs/DefaultApi.md#batchGetRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.BatchGetRepositories | 
*AwsCodeCommit.DefaultApi* | [**createApprovalRuleTemplate**](docs/DefaultApi.md#createApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateApprovalRuleTemplate | 
*AwsCodeCommit.DefaultApi* | [**createBranch**](docs/DefaultApi.md#createBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateBranch | 
*AwsCodeCommit.DefaultApi* | [**createCommit**](docs/DefaultApi.md#createCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateCommit | 
*AwsCodeCommit.DefaultApi* | [**createPullRequest**](docs/DefaultApi.md#createPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreatePullRequest | 
*AwsCodeCommit.DefaultApi* | [**createPullRequestApprovalRule**](docs/DefaultApi.md#createPullRequestApprovalRule) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreatePullRequestApprovalRule | 
*AwsCodeCommit.DefaultApi* | [**createRepository**](docs/DefaultApi.md#createRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateRepository | 
*AwsCodeCommit.DefaultApi* | [**createUnreferencedMergeCommit**](docs/DefaultApi.md#createUnreferencedMergeCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.CreateUnreferencedMergeCommit | 
*AwsCodeCommit.DefaultApi* | [**deleteApprovalRuleTemplate**](docs/DefaultApi.md#deleteApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteApprovalRuleTemplate | 
*AwsCodeCommit.DefaultApi* | [**deleteBranch**](docs/DefaultApi.md#deleteBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteBranch | 
*AwsCodeCommit.DefaultApi* | [**deleteCommentContent**](docs/DefaultApi.md#deleteCommentContent) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteCommentContent | 
*AwsCodeCommit.DefaultApi* | [**deleteFile**](docs/DefaultApi.md#deleteFile) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteFile | 
*AwsCodeCommit.DefaultApi* | [**deletePullRequestApprovalRule**](docs/DefaultApi.md#deletePullRequestApprovalRule) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeletePullRequestApprovalRule | 
*AwsCodeCommit.DefaultApi* | [**deleteRepository**](docs/DefaultApi.md#deleteRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DeleteRepository | 
*AwsCodeCommit.DefaultApi* | [**describeMergeConflicts**](docs/DefaultApi.md#describeMergeConflicts) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DescribeMergeConflicts | 
*AwsCodeCommit.DefaultApi* | [**describePullRequestEvents**](docs/DefaultApi.md#describePullRequestEvents) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DescribePullRequestEvents | 
*AwsCodeCommit.DefaultApi* | [**disassociateApprovalRuleTemplateFromRepository**](docs/DefaultApi.md#disassociateApprovalRuleTemplateFromRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.DisassociateApprovalRuleTemplateFromRepository | 
*AwsCodeCommit.DefaultApi* | [**evaluatePullRequestApprovalRules**](docs/DefaultApi.md#evaluatePullRequestApprovalRules) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.EvaluatePullRequestApprovalRules | 
*AwsCodeCommit.DefaultApi* | [**getApprovalRuleTemplate**](docs/DefaultApi.md#getApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetApprovalRuleTemplate | 
*AwsCodeCommit.DefaultApi* | [**getBlob**](docs/DefaultApi.md#getBlob) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetBlob | 
*AwsCodeCommit.DefaultApi* | [**getBranch**](docs/DefaultApi.md#getBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetBranch | 
*AwsCodeCommit.DefaultApi* | [**getComment**](docs/DefaultApi.md#getComment) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetComment | 
*AwsCodeCommit.DefaultApi* | [**getCommentReactions**](docs/DefaultApi.md#getCommentReactions) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommentReactions | 
*AwsCodeCommit.DefaultApi* | [**getCommentsForComparedCommit**](docs/DefaultApi.md#getCommentsForComparedCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommentsForComparedCommit | 
*AwsCodeCommit.DefaultApi* | [**getCommentsForPullRequest**](docs/DefaultApi.md#getCommentsForPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommentsForPullRequest | 
*AwsCodeCommit.DefaultApi* | [**getCommit**](docs/DefaultApi.md#getCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetCommit | 
*AwsCodeCommit.DefaultApi* | [**getDifferences**](docs/DefaultApi.md#getDifferences) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetDifferences | 
*AwsCodeCommit.DefaultApi* | [**getFile**](docs/DefaultApi.md#getFile) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetFile | 
*AwsCodeCommit.DefaultApi* | [**getFolder**](docs/DefaultApi.md#getFolder) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetFolder | 
*AwsCodeCommit.DefaultApi* | [**getMergeCommit**](docs/DefaultApi.md#getMergeCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetMergeCommit | 
*AwsCodeCommit.DefaultApi* | [**getMergeConflicts**](docs/DefaultApi.md#getMergeConflicts) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetMergeConflicts | 
*AwsCodeCommit.DefaultApi* | [**getMergeOptions**](docs/DefaultApi.md#getMergeOptions) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetMergeOptions | 
*AwsCodeCommit.DefaultApi* | [**getPullRequest**](docs/DefaultApi.md#getPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetPullRequest | 
*AwsCodeCommit.DefaultApi* | [**getPullRequestApprovalStates**](docs/DefaultApi.md#getPullRequestApprovalStates) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetPullRequestApprovalStates | 
*AwsCodeCommit.DefaultApi* | [**getPullRequestOverrideState**](docs/DefaultApi.md#getPullRequestOverrideState) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetPullRequestOverrideState | 
*AwsCodeCommit.DefaultApi* | [**getRepository**](docs/DefaultApi.md#getRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetRepository | 
*AwsCodeCommit.DefaultApi* | [**getRepositoryTriggers**](docs/DefaultApi.md#getRepositoryTriggers) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.GetRepositoryTriggers | 
*AwsCodeCommit.DefaultApi* | [**listApprovalRuleTemplates**](docs/DefaultApi.md#listApprovalRuleTemplates) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListApprovalRuleTemplates | 
*AwsCodeCommit.DefaultApi* | [**listAssociatedApprovalRuleTemplatesForRepository**](docs/DefaultApi.md#listAssociatedApprovalRuleTemplatesForRepository) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListAssociatedApprovalRuleTemplatesForRepository | 
*AwsCodeCommit.DefaultApi* | [**listBranches**](docs/DefaultApi.md#listBranches) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListBranches | 
*AwsCodeCommit.DefaultApi* | [**listPullRequests**](docs/DefaultApi.md#listPullRequests) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListPullRequests | 
*AwsCodeCommit.DefaultApi* | [**listRepositories**](docs/DefaultApi.md#listRepositories) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListRepositories | 
*AwsCodeCommit.DefaultApi* | [**listRepositoriesForApprovalRuleTemplate**](docs/DefaultApi.md#listRepositoriesForApprovalRuleTemplate) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListRepositoriesForApprovalRuleTemplate | 
*AwsCodeCommit.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.ListTagsForResource | 
*AwsCodeCommit.DefaultApi* | [**mergeBranchesByFastForward**](docs/DefaultApi.md#mergeBranchesByFastForward) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergeBranchesByFastForward | 
*AwsCodeCommit.DefaultApi* | [**mergeBranchesBySquash**](docs/DefaultApi.md#mergeBranchesBySquash) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergeBranchesBySquash | 
*AwsCodeCommit.DefaultApi* | [**mergeBranchesByThreeWay**](docs/DefaultApi.md#mergeBranchesByThreeWay) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergeBranchesByThreeWay | 
*AwsCodeCommit.DefaultApi* | [**mergePullRequestByFastForward**](docs/DefaultApi.md#mergePullRequestByFastForward) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergePullRequestByFastForward | 
*AwsCodeCommit.DefaultApi* | [**mergePullRequestBySquash**](docs/DefaultApi.md#mergePullRequestBySquash) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergePullRequestBySquash | 
*AwsCodeCommit.DefaultApi* | [**mergePullRequestByThreeWay**](docs/DefaultApi.md#mergePullRequestByThreeWay) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.MergePullRequestByThreeWay | 
*AwsCodeCommit.DefaultApi* | [**overridePullRequestApprovalRules**](docs/DefaultApi.md#overridePullRequestApprovalRules) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.OverridePullRequestApprovalRules | 
*AwsCodeCommit.DefaultApi* | [**postCommentForComparedCommit**](docs/DefaultApi.md#postCommentForComparedCommit) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PostCommentForComparedCommit | 
*AwsCodeCommit.DefaultApi* | [**postCommentForPullRequest**](docs/DefaultApi.md#postCommentForPullRequest) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PostCommentForPullRequest | 
*AwsCodeCommit.DefaultApi* | [**postCommentReply**](docs/DefaultApi.md#postCommentReply) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PostCommentReply | 
*AwsCodeCommit.DefaultApi* | [**putCommentReaction**](docs/DefaultApi.md#putCommentReaction) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PutCommentReaction | 
*AwsCodeCommit.DefaultApi* | [**putFile**](docs/DefaultApi.md#putFile) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PutFile | 
*AwsCodeCommit.DefaultApi* | [**putRepositoryTriggers**](docs/DefaultApi.md#putRepositoryTriggers) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.PutRepositoryTriggers | 
*AwsCodeCommit.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.TagResource | 
*AwsCodeCommit.DefaultApi* | [**testRepositoryTriggers**](docs/DefaultApi.md#testRepositoryTriggers) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.TestRepositoryTriggers | 
*AwsCodeCommit.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UntagResource | 
*AwsCodeCommit.DefaultApi* | [**updateApprovalRuleTemplateContent**](docs/DefaultApi.md#updateApprovalRuleTemplateContent) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateApprovalRuleTemplateContent | 
*AwsCodeCommit.DefaultApi* | [**updateApprovalRuleTemplateDescription**](docs/DefaultApi.md#updateApprovalRuleTemplateDescription) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateApprovalRuleTemplateDescription | 
*AwsCodeCommit.DefaultApi* | [**updateApprovalRuleTemplateName**](docs/DefaultApi.md#updateApprovalRuleTemplateName) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateApprovalRuleTemplateName | 
*AwsCodeCommit.DefaultApi* | [**updateComment**](docs/DefaultApi.md#updateComment) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateComment | 
*AwsCodeCommit.DefaultApi* | [**updateDefaultBranch**](docs/DefaultApi.md#updateDefaultBranch) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateDefaultBranch | 
*AwsCodeCommit.DefaultApi* | [**updatePullRequestApprovalRuleContent**](docs/DefaultApi.md#updatePullRequestApprovalRuleContent) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestApprovalRuleContent | 
*AwsCodeCommit.DefaultApi* | [**updatePullRequestApprovalState**](docs/DefaultApi.md#updatePullRequestApprovalState) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestApprovalState | 
*AwsCodeCommit.DefaultApi* | [**updatePullRequestDescription**](docs/DefaultApi.md#updatePullRequestDescription) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestDescription | 
*AwsCodeCommit.DefaultApi* | [**updatePullRequestStatus**](docs/DefaultApi.md#updatePullRequestStatus) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestStatus | 
*AwsCodeCommit.DefaultApi* | [**updatePullRequestTitle**](docs/DefaultApi.md#updatePullRequestTitle) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdatePullRequestTitle | 
*AwsCodeCommit.DefaultApi* | [**updateRepositoryDescription**](docs/DefaultApi.md#updateRepositoryDescription) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateRepositoryDescription | 
*AwsCodeCommit.DefaultApi* | [**updateRepositoryName**](docs/DefaultApi.md#updateRepositoryName) | **POST** /#X-Amz-Target&#x3D;CodeCommit_20150413.UpdateRepositoryName | 


## Documentation for Models

 - [AwsCodeCommit.Approval](docs/Approval.md)
 - [AwsCodeCommit.ApprovalRule](docs/ApprovalRule.md)
 - [AwsCodeCommit.ApprovalRuleEventMetadata](docs/ApprovalRuleEventMetadata.md)
 - [AwsCodeCommit.ApprovalRuleOriginApprovalRuleTemplate](docs/ApprovalRuleOriginApprovalRuleTemplate.md)
 - [AwsCodeCommit.ApprovalRuleOverriddenEventMetadata](docs/ApprovalRuleOverriddenEventMetadata.md)
 - [AwsCodeCommit.ApprovalRuleTemplate](docs/ApprovalRuleTemplate.md)
 - [AwsCodeCommit.ApprovalState](docs/ApprovalState.md)
 - [AwsCodeCommit.ApprovalStateChangedEventMetadata](docs/ApprovalStateChangedEventMetadata.md)
 - [AwsCodeCommit.AssociateApprovalRuleTemplateWithRepositoryInput](docs/AssociateApprovalRuleTemplateWithRepositoryInput.md)
 - [AwsCodeCommit.BatchAssociateApprovalRuleTemplateWithRepositoriesError](docs/BatchAssociateApprovalRuleTemplateWithRepositoriesError.md)
 - [AwsCodeCommit.BatchAssociateApprovalRuleTemplateWithRepositoriesInput](docs/BatchAssociateApprovalRuleTemplateWithRepositoriesInput.md)
 - [AwsCodeCommit.BatchAssociateApprovalRuleTemplateWithRepositoriesOutput](docs/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput.md)
 - [AwsCodeCommit.BatchDescribeMergeConflictsError](docs/BatchDescribeMergeConflictsError.md)
 - [AwsCodeCommit.BatchDescribeMergeConflictsInput](docs/BatchDescribeMergeConflictsInput.md)
 - [AwsCodeCommit.BatchDescribeMergeConflictsOutput](docs/BatchDescribeMergeConflictsOutput.md)
 - [AwsCodeCommit.BatchDisassociateApprovalRuleTemplateFromRepositoriesError](docs/BatchDisassociateApprovalRuleTemplateFromRepositoriesError.md)
 - [AwsCodeCommit.BatchDisassociateApprovalRuleTemplateFromRepositoriesInput](docs/BatchDisassociateApprovalRuleTemplateFromRepositoriesInput.md)
 - [AwsCodeCommit.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput](docs/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput.md)
 - [AwsCodeCommit.BatchGetCommitsError](docs/BatchGetCommitsError.md)
 - [AwsCodeCommit.BatchGetCommitsInput](docs/BatchGetCommitsInput.md)
 - [AwsCodeCommit.BatchGetCommitsOutput](docs/BatchGetCommitsOutput.md)
 - [AwsCodeCommit.BatchGetRepositoriesInput](docs/BatchGetRepositoriesInput.md)
 - [AwsCodeCommit.BatchGetRepositoriesOutput](docs/BatchGetRepositoriesOutput.md)
 - [AwsCodeCommit.BlobMetadata](docs/BlobMetadata.md)
 - [AwsCodeCommit.BranchInfo](docs/BranchInfo.md)
 - [AwsCodeCommit.ChangeTypeEnum](docs/ChangeTypeEnum.md)
 - [AwsCodeCommit.Comment](docs/Comment.md)
 - [AwsCodeCommit.CommentsForComparedCommit](docs/CommentsForComparedCommit.md)
 - [AwsCodeCommit.CommentsForComparedCommitLocation](docs/CommentsForComparedCommitLocation.md)
 - [AwsCodeCommit.CommentsForPullRequest](docs/CommentsForPullRequest.md)
 - [AwsCodeCommit.CommentsForPullRequestLocation](docs/CommentsForPullRequestLocation.md)
 - [AwsCodeCommit.Commit](docs/Commit.md)
 - [AwsCodeCommit.CommitAuthor](docs/CommitAuthor.md)
 - [AwsCodeCommit.CommitCommitter](docs/CommitCommitter.md)
 - [AwsCodeCommit.Conflict](docs/Conflict.md)
 - [AwsCodeCommit.ConflictConflictMetadata](docs/ConflictConflictMetadata.md)
 - [AwsCodeCommit.ConflictDetailLevelTypeEnum](docs/ConflictDetailLevelTypeEnum.md)
 - [AwsCodeCommit.ConflictMetadata](docs/ConflictMetadata.md)
 - [AwsCodeCommit.ConflictMetadataFileModes](docs/ConflictMetadataFileModes.md)
 - [AwsCodeCommit.ConflictMetadataFileSizes](docs/ConflictMetadataFileSizes.md)
 - [AwsCodeCommit.ConflictMetadataIsBinaryFile](docs/ConflictMetadataIsBinaryFile.md)
 - [AwsCodeCommit.ConflictMetadataMergeOperations](docs/ConflictMetadataMergeOperations.md)
 - [AwsCodeCommit.ConflictMetadataObjectTypes](docs/ConflictMetadataObjectTypes.md)
 - [AwsCodeCommit.ConflictResolution](docs/ConflictResolution.md)
 - [AwsCodeCommit.ConflictResolutionStrategyTypeEnum](docs/ConflictResolutionStrategyTypeEnum.md)
 - [AwsCodeCommit.CreateApprovalRuleTemplateInput](docs/CreateApprovalRuleTemplateInput.md)
 - [AwsCodeCommit.CreateApprovalRuleTemplateOutput](docs/CreateApprovalRuleTemplateOutput.md)
 - [AwsCodeCommit.CreateApprovalRuleTemplateOutputApprovalRuleTemplate](docs/CreateApprovalRuleTemplateOutputApprovalRuleTemplate.md)
 - [AwsCodeCommit.CreateBranchInput](docs/CreateBranchInput.md)
 - [AwsCodeCommit.CreateCommitInput](docs/CreateCommitInput.md)
 - [AwsCodeCommit.CreateCommitOutput](docs/CreateCommitOutput.md)
 - [AwsCodeCommit.CreatePullRequestApprovalRuleInput](docs/CreatePullRequestApprovalRuleInput.md)
 - [AwsCodeCommit.CreatePullRequestApprovalRuleOutput](docs/CreatePullRequestApprovalRuleOutput.md)
 - [AwsCodeCommit.CreatePullRequestApprovalRuleOutputApprovalRule](docs/CreatePullRequestApprovalRuleOutputApprovalRule.md)
 - [AwsCodeCommit.CreatePullRequestInput](docs/CreatePullRequestInput.md)
 - [AwsCodeCommit.CreatePullRequestOutput](docs/CreatePullRequestOutput.md)
 - [AwsCodeCommit.CreatePullRequestOutputPullRequest](docs/CreatePullRequestOutputPullRequest.md)
 - [AwsCodeCommit.CreateRepositoryInput](docs/CreateRepositoryInput.md)
 - [AwsCodeCommit.CreateRepositoryOutput](docs/CreateRepositoryOutput.md)
 - [AwsCodeCommit.CreateRepositoryOutputRepositoryMetadata](docs/CreateRepositoryOutputRepositoryMetadata.md)
 - [AwsCodeCommit.CreateUnreferencedMergeCommitInput](docs/CreateUnreferencedMergeCommitInput.md)
 - [AwsCodeCommit.CreateUnreferencedMergeCommitInputConflictResolution](docs/CreateUnreferencedMergeCommitInputConflictResolution.md)
 - [AwsCodeCommit.CreateUnreferencedMergeCommitOutput](docs/CreateUnreferencedMergeCommitOutput.md)
 - [AwsCodeCommit.DeleteApprovalRuleTemplateInput](docs/DeleteApprovalRuleTemplateInput.md)
 - [AwsCodeCommit.DeleteApprovalRuleTemplateOutput](docs/DeleteApprovalRuleTemplateOutput.md)
 - [AwsCodeCommit.DeleteBranchInput](docs/DeleteBranchInput.md)
 - [AwsCodeCommit.DeleteBranchOutput](docs/DeleteBranchOutput.md)
 - [AwsCodeCommit.DeleteBranchOutputDeletedBranch](docs/DeleteBranchOutputDeletedBranch.md)
 - [AwsCodeCommit.DeleteCommentContentInput](docs/DeleteCommentContentInput.md)
 - [AwsCodeCommit.DeleteCommentContentOutput](docs/DeleteCommentContentOutput.md)
 - [AwsCodeCommit.DeleteCommentContentOutputComment](docs/DeleteCommentContentOutputComment.md)
 - [AwsCodeCommit.DeleteFileEntry](docs/DeleteFileEntry.md)
 - [AwsCodeCommit.DeleteFileInput](docs/DeleteFileInput.md)
 - [AwsCodeCommit.DeleteFileOutput](docs/DeleteFileOutput.md)
 - [AwsCodeCommit.DeletePullRequestApprovalRuleInput](docs/DeletePullRequestApprovalRuleInput.md)
 - [AwsCodeCommit.DeletePullRequestApprovalRuleOutput](docs/DeletePullRequestApprovalRuleOutput.md)
 - [AwsCodeCommit.DeleteRepositoryInput](docs/DeleteRepositoryInput.md)
 - [AwsCodeCommit.DeleteRepositoryOutput](docs/DeleteRepositoryOutput.md)
 - [AwsCodeCommit.DescribeMergeConflictsInput](docs/DescribeMergeConflictsInput.md)
 - [AwsCodeCommit.DescribeMergeConflictsOutput](docs/DescribeMergeConflictsOutput.md)
 - [AwsCodeCommit.DescribeMergeConflictsOutputConflictMetadata](docs/DescribeMergeConflictsOutputConflictMetadata.md)
 - [AwsCodeCommit.DescribePullRequestEventsInput](docs/DescribePullRequestEventsInput.md)
 - [AwsCodeCommit.DescribePullRequestEventsOutput](docs/DescribePullRequestEventsOutput.md)
 - [AwsCodeCommit.Difference](docs/Difference.md)
 - [AwsCodeCommit.DifferenceAfterBlob](docs/DifferenceAfterBlob.md)
 - [AwsCodeCommit.DifferenceBeforeBlob](docs/DifferenceBeforeBlob.md)
 - [AwsCodeCommit.DisassociateApprovalRuleTemplateFromRepositoryInput](docs/DisassociateApprovalRuleTemplateFromRepositoryInput.md)
 - [AwsCodeCommit.EvaluatePullRequestApprovalRulesInput](docs/EvaluatePullRequestApprovalRulesInput.md)
 - [AwsCodeCommit.EvaluatePullRequestApprovalRulesOutput](docs/EvaluatePullRequestApprovalRulesOutput.md)
 - [AwsCodeCommit.EvaluatePullRequestApprovalRulesOutputEvaluation](docs/EvaluatePullRequestApprovalRulesOutputEvaluation.md)
 - [AwsCodeCommit.Evaluation](docs/Evaluation.md)
 - [AwsCodeCommit.File](docs/File.md)
 - [AwsCodeCommit.FileMetadata](docs/FileMetadata.md)
 - [AwsCodeCommit.FileModeTypeEnum](docs/FileModeTypeEnum.md)
 - [AwsCodeCommit.FileModes](docs/FileModes.md)
 - [AwsCodeCommit.FileSizes](docs/FileSizes.md)
 - [AwsCodeCommit.Folder](docs/Folder.md)
 - [AwsCodeCommit.GetApprovalRuleTemplateInput](docs/GetApprovalRuleTemplateInput.md)
 - [AwsCodeCommit.GetApprovalRuleTemplateOutput](docs/GetApprovalRuleTemplateOutput.md)
 - [AwsCodeCommit.GetApprovalRuleTemplateOutputApprovalRuleTemplate](docs/GetApprovalRuleTemplateOutputApprovalRuleTemplate.md)
 - [AwsCodeCommit.GetBlobInput](docs/GetBlobInput.md)
 - [AwsCodeCommit.GetBlobOutput](docs/GetBlobOutput.md)
 - [AwsCodeCommit.GetBranchInput](docs/GetBranchInput.md)
 - [AwsCodeCommit.GetBranchOutput](docs/GetBranchOutput.md)
 - [AwsCodeCommit.GetBranchOutputBranch](docs/GetBranchOutputBranch.md)
 - [AwsCodeCommit.GetCommentInput](docs/GetCommentInput.md)
 - [AwsCodeCommit.GetCommentOutput](docs/GetCommentOutput.md)
 - [AwsCodeCommit.GetCommentOutputComment](docs/GetCommentOutputComment.md)
 - [AwsCodeCommit.GetCommentReactionsInput](docs/GetCommentReactionsInput.md)
 - [AwsCodeCommit.GetCommentReactionsOutput](docs/GetCommentReactionsOutput.md)
 - [AwsCodeCommit.GetCommentsForComparedCommitInput](docs/GetCommentsForComparedCommitInput.md)
 - [AwsCodeCommit.GetCommentsForComparedCommitOutput](docs/GetCommentsForComparedCommitOutput.md)
 - [AwsCodeCommit.GetCommentsForPullRequestInput](docs/GetCommentsForPullRequestInput.md)
 - [AwsCodeCommit.GetCommentsForPullRequestOutput](docs/GetCommentsForPullRequestOutput.md)
 - [AwsCodeCommit.GetCommitInput](docs/GetCommitInput.md)
 - [AwsCodeCommit.GetCommitOutput](docs/GetCommitOutput.md)
 - [AwsCodeCommit.GetCommitOutputCommit](docs/GetCommitOutputCommit.md)
 - [AwsCodeCommit.GetDifferencesInput](docs/GetDifferencesInput.md)
 - [AwsCodeCommit.GetDifferencesOutput](docs/GetDifferencesOutput.md)
 - [AwsCodeCommit.GetFileInput](docs/GetFileInput.md)
 - [AwsCodeCommit.GetFileOutput](docs/GetFileOutput.md)
 - [AwsCodeCommit.GetFolderInput](docs/GetFolderInput.md)
 - [AwsCodeCommit.GetFolderOutput](docs/GetFolderOutput.md)
 - [AwsCodeCommit.GetMergeCommitInput](docs/GetMergeCommitInput.md)
 - [AwsCodeCommit.GetMergeCommitOutput](docs/GetMergeCommitOutput.md)
 - [AwsCodeCommit.GetMergeConflictsInput](docs/GetMergeConflictsInput.md)
 - [AwsCodeCommit.GetMergeConflictsOutput](docs/GetMergeConflictsOutput.md)
 - [AwsCodeCommit.GetMergeOptionsInput](docs/GetMergeOptionsInput.md)
 - [AwsCodeCommit.GetMergeOptionsOutput](docs/GetMergeOptionsOutput.md)
 - [AwsCodeCommit.GetPullRequestApprovalStatesInput](docs/GetPullRequestApprovalStatesInput.md)
 - [AwsCodeCommit.GetPullRequestApprovalStatesOutput](docs/GetPullRequestApprovalStatesOutput.md)
 - [AwsCodeCommit.GetPullRequestInput](docs/GetPullRequestInput.md)
 - [AwsCodeCommit.GetPullRequestOutput](docs/GetPullRequestOutput.md)
 - [AwsCodeCommit.GetPullRequestOutputPullRequest](docs/GetPullRequestOutputPullRequest.md)
 - [AwsCodeCommit.GetPullRequestOverrideStateInput](docs/GetPullRequestOverrideStateInput.md)
 - [AwsCodeCommit.GetPullRequestOverrideStateOutput](docs/GetPullRequestOverrideStateOutput.md)
 - [AwsCodeCommit.GetRepositoryInput](docs/GetRepositoryInput.md)
 - [AwsCodeCommit.GetRepositoryOutput](docs/GetRepositoryOutput.md)
 - [AwsCodeCommit.GetRepositoryOutputRepositoryMetadata](docs/GetRepositoryOutputRepositoryMetadata.md)
 - [AwsCodeCommit.GetRepositoryTriggersInput](docs/GetRepositoryTriggersInput.md)
 - [AwsCodeCommit.GetRepositoryTriggersOutput](docs/GetRepositoryTriggersOutput.md)
 - [AwsCodeCommit.IsBinaryFile](docs/IsBinaryFile.md)
 - [AwsCodeCommit.ListApprovalRuleTemplatesInput](docs/ListApprovalRuleTemplatesInput.md)
 - [AwsCodeCommit.ListApprovalRuleTemplatesOutput](docs/ListApprovalRuleTemplatesOutput.md)
 - [AwsCodeCommit.ListAssociatedApprovalRuleTemplatesForRepositoryInput](docs/ListAssociatedApprovalRuleTemplatesForRepositoryInput.md)
 - [AwsCodeCommit.ListAssociatedApprovalRuleTemplatesForRepositoryOutput](docs/ListAssociatedApprovalRuleTemplatesForRepositoryOutput.md)
 - [AwsCodeCommit.ListBranchesInput](docs/ListBranchesInput.md)
 - [AwsCodeCommit.ListBranchesOutput](docs/ListBranchesOutput.md)
 - [AwsCodeCommit.ListPullRequestsInput](docs/ListPullRequestsInput.md)
 - [AwsCodeCommit.ListPullRequestsOutput](docs/ListPullRequestsOutput.md)
 - [AwsCodeCommit.ListRepositoriesForApprovalRuleTemplateInput](docs/ListRepositoriesForApprovalRuleTemplateInput.md)
 - [AwsCodeCommit.ListRepositoriesForApprovalRuleTemplateOutput](docs/ListRepositoriesForApprovalRuleTemplateOutput.md)
 - [AwsCodeCommit.ListRepositoriesInput](docs/ListRepositoriesInput.md)
 - [AwsCodeCommit.ListRepositoriesOutput](docs/ListRepositoriesOutput.md)
 - [AwsCodeCommit.ListTagsForResourceInput](docs/ListTagsForResourceInput.md)
 - [AwsCodeCommit.ListTagsForResourceOutput](docs/ListTagsForResourceOutput.md)
 - [AwsCodeCommit.Location](docs/Location.md)
 - [AwsCodeCommit.MergeBranchesByFastForwardInput](docs/MergeBranchesByFastForwardInput.md)
 - [AwsCodeCommit.MergeBranchesByFastForwardOutput](docs/MergeBranchesByFastForwardOutput.md)
 - [AwsCodeCommit.MergeBranchesBySquashInput](docs/MergeBranchesBySquashInput.md)
 - [AwsCodeCommit.MergeBranchesBySquashOutput](docs/MergeBranchesBySquashOutput.md)
 - [AwsCodeCommit.MergeBranchesByThreeWayInput](docs/MergeBranchesByThreeWayInput.md)
 - [AwsCodeCommit.MergeBranchesByThreeWayOutput](docs/MergeBranchesByThreeWayOutput.md)
 - [AwsCodeCommit.MergeHunk](docs/MergeHunk.md)
 - [AwsCodeCommit.MergeHunkBase](docs/MergeHunkBase.md)
 - [AwsCodeCommit.MergeHunkDestination](docs/MergeHunkDestination.md)
 - [AwsCodeCommit.MergeHunkDetail](docs/MergeHunkDetail.md)
 - [AwsCodeCommit.MergeHunkSource](docs/MergeHunkSource.md)
 - [AwsCodeCommit.MergeMetadata](docs/MergeMetadata.md)
 - [AwsCodeCommit.MergeOperations](docs/MergeOperations.md)
 - [AwsCodeCommit.MergeOptionTypeEnum](docs/MergeOptionTypeEnum.md)
 - [AwsCodeCommit.MergePullRequestByFastForwardInput](docs/MergePullRequestByFastForwardInput.md)
 - [AwsCodeCommit.MergePullRequestByFastForwardOutput](docs/MergePullRequestByFastForwardOutput.md)
 - [AwsCodeCommit.MergePullRequestByFastForwardOutputPullRequest](docs/MergePullRequestByFastForwardOutputPullRequest.md)
 - [AwsCodeCommit.MergePullRequestBySquashInput](docs/MergePullRequestBySquashInput.md)
 - [AwsCodeCommit.MergePullRequestBySquashOutput](docs/MergePullRequestBySquashOutput.md)
 - [AwsCodeCommit.MergePullRequestByThreeWayInput](docs/MergePullRequestByThreeWayInput.md)
 - [AwsCodeCommit.MergePullRequestByThreeWayOutput](docs/MergePullRequestByThreeWayOutput.md)
 - [AwsCodeCommit.ObjectTypeEnum](docs/ObjectTypeEnum.md)
 - [AwsCodeCommit.ObjectTypes](docs/ObjectTypes.md)
 - [AwsCodeCommit.OrderEnum](docs/OrderEnum.md)
 - [AwsCodeCommit.OriginApprovalRuleTemplate](docs/OriginApprovalRuleTemplate.md)
 - [AwsCodeCommit.OverridePullRequestApprovalRulesInput](docs/OverridePullRequestApprovalRulesInput.md)
 - [AwsCodeCommit.OverrideStatus](docs/OverrideStatus.md)
 - [AwsCodeCommit.PostCommentForComparedCommitInput](docs/PostCommentForComparedCommitInput.md)
 - [AwsCodeCommit.PostCommentForComparedCommitInputLocation](docs/PostCommentForComparedCommitInputLocation.md)
 - [AwsCodeCommit.PostCommentForComparedCommitOutput](docs/PostCommentForComparedCommitOutput.md)
 - [AwsCodeCommit.PostCommentForComparedCommitOutputComment](docs/PostCommentForComparedCommitOutputComment.md)
 - [AwsCodeCommit.PostCommentForComparedCommitOutputLocation](docs/PostCommentForComparedCommitOutputLocation.md)
 - [AwsCodeCommit.PostCommentForPullRequestInput](docs/PostCommentForPullRequestInput.md)
 - [AwsCodeCommit.PostCommentForPullRequestInputLocation](docs/PostCommentForPullRequestInputLocation.md)
 - [AwsCodeCommit.PostCommentForPullRequestOutput](docs/PostCommentForPullRequestOutput.md)
 - [AwsCodeCommit.PostCommentForPullRequestOutputLocation](docs/PostCommentForPullRequestOutputLocation.md)
 - [AwsCodeCommit.PostCommentReplyInput](docs/PostCommentReplyInput.md)
 - [AwsCodeCommit.PostCommentReplyOutput](docs/PostCommentReplyOutput.md)
 - [AwsCodeCommit.PostCommentReplyOutputComment](docs/PostCommentReplyOutputComment.md)
 - [AwsCodeCommit.PullRequest](docs/PullRequest.md)
 - [AwsCodeCommit.PullRequestCreatedEventMetadata](docs/PullRequestCreatedEventMetadata.md)
 - [AwsCodeCommit.PullRequestEvent](docs/PullRequestEvent.md)
 - [AwsCodeCommit.PullRequestEventApprovalRuleEventMetadata](docs/PullRequestEventApprovalRuleEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventApprovalRuleOverriddenEventMetadata](docs/PullRequestEventApprovalRuleOverriddenEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventApprovalStateChangedEventMetadata](docs/PullRequestEventApprovalStateChangedEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventPullRequestCreatedEventMetadata](docs/PullRequestEventPullRequestCreatedEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventPullRequestMergedStateChangedEventMetadata](docs/PullRequestEventPullRequestMergedStateChangedEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata](docs/PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventPullRequestStatusChangedEventMetadata](docs/PullRequestEventPullRequestStatusChangedEventMetadata.md)
 - [AwsCodeCommit.PullRequestEventType](docs/PullRequestEventType.md)
 - [AwsCodeCommit.PullRequestMergedStateChangedEventMetadata](docs/PullRequestMergedStateChangedEventMetadata.md)
 - [AwsCodeCommit.PullRequestMergedStateChangedEventMetadataMergeMetadata](docs/PullRequestMergedStateChangedEventMetadataMergeMetadata.md)
 - [AwsCodeCommit.PullRequestSourceReferenceUpdatedEventMetadata](docs/PullRequestSourceReferenceUpdatedEventMetadata.md)
 - [AwsCodeCommit.PullRequestStatusChangedEventMetadata](docs/PullRequestStatusChangedEventMetadata.md)
 - [AwsCodeCommit.PullRequestStatusEnum](docs/PullRequestStatusEnum.md)
 - [AwsCodeCommit.PullRequestTarget](docs/PullRequestTarget.md)
 - [AwsCodeCommit.PullRequestTargetMergeMetadata](docs/PullRequestTargetMergeMetadata.md)
 - [AwsCodeCommit.PutCommentReactionInput](docs/PutCommentReactionInput.md)
 - [AwsCodeCommit.PutFileEntry](docs/PutFileEntry.md)
 - [AwsCodeCommit.PutFileEntrySourceFile](docs/PutFileEntrySourceFile.md)
 - [AwsCodeCommit.PutFileInput](docs/PutFileInput.md)
 - [AwsCodeCommit.PutFileOutput](docs/PutFileOutput.md)
 - [AwsCodeCommit.PutRepositoryTriggersInput](docs/PutRepositoryTriggersInput.md)
 - [AwsCodeCommit.PutRepositoryTriggersOutput](docs/PutRepositoryTriggersOutput.md)
 - [AwsCodeCommit.ReactionForComment](docs/ReactionForComment.md)
 - [AwsCodeCommit.ReactionForCommentReaction](docs/ReactionForCommentReaction.md)
 - [AwsCodeCommit.ReactionValueFormats](docs/ReactionValueFormats.md)
 - [AwsCodeCommit.RelativeFileVersionEnum](docs/RelativeFileVersionEnum.md)
 - [AwsCodeCommit.ReplaceContentEntry](docs/ReplaceContentEntry.md)
 - [AwsCodeCommit.ReplacementTypeEnum](docs/ReplacementTypeEnum.md)
 - [AwsCodeCommit.RepositoryMetadata](docs/RepositoryMetadata.md)
 - [AwsCodeCommit.RepositoryNameIdPair](docs/RepositoryNameIdPair.md)
 - [AwsCodeCommit.RepositoryTrigger](docs/RepositoryTrigger.md)
 - [AwsCodeCommit.RepositoryTriggerEventEnum](docs/RepositoryTriggerEventEnum.md)
 - [AwsCodeCommit.RepositoryTriggerExecutionFailure](docs/RepositoryTriggerExecutionFailure.md)
 - [AwsCodeCommit.SetFileModeEntry](docs/SetFileModeEntry.md)
 - [AwsCodeCommit.SortByEnum](docs/SortByEnum.md)
 - [AwsCodeCommit.SourceFileSpecifier](docs/SourceFileSpecifier.md)
 - [AwsCodeCommit.SubModule](docs/SubModule.md)
 - [AwsCodeCommit.SymbolicLink](docs/SymbolicLink.md)
 - [AwsCodeCommit.TagResourceInput](docs/TagResourceInput.md)
 - [AwsCodeCommit.Target](docs/Target.md)
 - [AwsCodeCommit.TestRepositoryTriggersInput](docs/TestRepositoryTriggersInput.md)
 - [AwsCodeCommit.TestRepositoryTriggersOutput](docs/TestRepositoryTriggersOutput.md)
 - [AwsCodeCommit.UntagResourceInput](docs/UntagResourceInput.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateContentInput](docs/UpdateApprovalRuleTemplateContentInput.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateContentOutput](docs/UpdateApprovalRuleTemplateContentOutput.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateDescriptionInput](docs/UpdateApprovalRuleTemplateDescriptionInput.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateDescriptionOutput](docs/UpdateApprovalRuleTemplateDescriptionOutput.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate](docs/UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateNameInput](docs/UpdateApprovalRuleTemplateNameInput.md)
 - [AwsCodeCommit.UpdateApprovalRuleTemplateNameOutput](docs/UpdateApprovalRuleTemplateNameOutput.md)
 - [AwsCodeCommit.UpdateCommentInput](docs/UpdateCommentInput.md)
 - [AwsCodeCommit.UpdateCommentOutput](docs/UpdateCommentOutput.md)
 - [AwsCodeCommit.UpdateCommentOutputComment](docs/UpdateCommentOutputComment.md)
 - [AwsCodeCommit.UpdateDefaultBranchInput](docs/UpdateDefaultBranchInput.md)
 - [AwsCodeCommit.UpdatePullRequestApprovalRuleContentInput](docs/UpdatePullRequestApprovalRuleContentInput.md)
 - [AwsCodeCommit.UpdatePullRequestApprovalRuleContentOutput](docs/UpdatePullRequestApprovalRuleContentOutput.md)
 - [AwsCodeCommit.UpdatePullRequestApprovalRuleContentOutputApprovalRule](docs/UpdatePullRequestApprovalRuleContentOutputApprovalRule.md)
 - [AwsCodeCommit.UpdatePullRequestApprovalStateInput](docs/UpdatePullRequestApprovalStateInput.md)
 - [AwsCodeCommit.UpdatePullRequestDescriptionInput](docs/UpdatePullRequestDescriptionInput.md)
 - [AwsCodeCommit.UpdatePullRequestDescriptionOutput](docs/UpdatePullRequestDescriptionOutput.md)
 - [AwsCodeCommit.UpdatePullRequestDescriptionOutputPullRequest](docs/UpdatePullRequestDescriptionOutputPullRequest.md)
 - [AwsCodeCommit.UpdatePullRequestStatusInput](docs/UpdatePullRequestStatusInput.md)
 - [AwsCodeCommit.UpdatePullRequestStatusOutput](docs/UpdatePullRequestStatusOutput.md)
 - [AwsCodeCommit.UpdatePullRequestStatusOutputPullRequest](docs/UpdatePullRequestStatusOutputPullRequest.md)
 - [AwsCodeCommit.UpdatePullRequestTitleInput](docs/UpdatePullRequestTitleInput.md)
 - [AwsCodeCommit.UpdatePullRequestTitleOutput](docs/UpdatePullRequestTitleOutput.md)
 - [AwsCodeCommit.UpdateRepositoryDescriptionInput](docs/UpdateRepositoryDescriptionInput.md)
 - [AwsCodeCommit.UpdateRepositoryNameInput](docs/UpdateRepositoryNameInput.md)
 - [AwsCodeCommit.UserInfo](docs/UserInfo.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

