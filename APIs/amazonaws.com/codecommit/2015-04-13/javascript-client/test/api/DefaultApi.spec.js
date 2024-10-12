/**
 * AWS CodeCommit
 * <fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>
 *
 * The version of the OpenAPI document: 2015-04-13
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.AwsCodeCommit);
  }
}(this, function(expect, AwsCodeCommit) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AwsCodeCommit.DefaultApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('DefaultApi', function() {
    describe('associateApprovalRuleTemplateWithRepository', function() {
      it('should call associateApprovalRuleTemplateWithRepository successfully', function(done) {
        //uncomment below and update the code to test associateApprovalRuleTemplateWithRepository
        //instance.associateApprovalRuleTemplateWithRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('batchAssociateApprovalRuleTemplateWithRepositories', function() {
      it('should call batchAssociateApprovalRuleTemplateWithRepositories successfully', function(done) {
        //uncomment below and update the code to test batchAssociateApprovalRuleTemplateWithRepositories
        //instance.batchAssociateApprovalRuleTemplateWithRepositories(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('batchDescribeMergeConflicts', function() {
      it('should call batchDescribeMergeConflicts successfully', function(done) {
        //uncomment below and update the code to test batchDescribeMergeConflicts
        //instance.batchDescribeMergeConflicts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('batchDisassociateApprovalRuleTemplateFromRepositories', function() {
      it('should call batchDisassociateApprovalRuleTemplateFromRepositories successfully', function(done) {
        //uncomment below and update the code to test batchDisassociateApprovalRuleTemplateFromRepositories
        //instance.batchDisassociateApprovalRuleTemplateFromRepositories(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('batchGetCommits', function() {
      it('should call batchGetCommits successfully', function(done) {
        //uncomment below and update the code to test batchGetCommits
        //instance.batchGetCommits(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('batchGetRepositories', function() {
      it('should call batchGetRepositories successfully', function(done) {
        //uncomment below and update the code to test batchGetRepositories
        //instance.batchGetRepositories(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createApprovalRuleTemplate', function() {
      it('should call createApprovalRuleTemplate successfully', function(done) {
        //uncomment below and update the code to test createApprovalRuleTemplate
        //instance.createApprovalRuleTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createBranch', function() {
      it('should call createBranch successfully', function(done) {
        //uncomment below and update the code to test createBranch
        //instance.createBranch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createCommit', function() {
      it('should call createCommit successfully', function(done) {
        //uncomment below and update the code to test createCommit
        //instance.createCommit(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createPullRequest', function() {
      it('should call createPullRequest successfully', function(done) {
        //uncomment below and update the code to test createPullRequest
        //instance.createPullRequest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createPullRequestApprovalRule', function() {
      it('should call createPullRequestApprovalRule successfully', function(done) {
        //uncomment below and update the code to test createPullRequestApprovalRule
        //instance.createPullRequestApprovalRule(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createRepository', function() {
      it('should call createRepository successfully', function(done) {
        //uncomment below and update the code to test createRepository
        //instance.createRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createUnreferencedMergeCommit', function() {
      it('should call createUnreferencedMergeCommit successfully', function(done) {
        //uncomment below and update the code to test createUnreferencedMergeCommit
        //instance.createUnreferencedMergeCommit(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteApprovalRuleTemplate', function() {
      it('should call deleteApprovalRuleTemplate successfully', function(done) {
        //uncomment below and update the code to test deleteApprovalRuleTemplate
        //instance.deleteApprovalRuleTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteBranch', function() {
      it('should call deleteBranch successfully', function(done) {
        //uncomment below and update the code to test deleteBranch
        //instance.deleteBranch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteCommentContent', function() {
      it('should call deleteCommentContent successfully', function(done) {
        //uncomment below and update the code to test deleteCommentContent
        //instance.deleteCommentContent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteFile', function() {
      it('should call deleteFile successfully', function(done) {
        //uncomment below and update the code to test deleteFile
        //instance.deleteFile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deletePullRequestApprovalRule', function() {
      it('should call deletePullRequestApprovalRule successfully', function(done) {
        //uncomment below and update the code to test deletePullRequestApprovalRule
        //instance.deletePullRequestApprovalRule(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteRepository', function() {
      it('should call deleteRepository successfully', function(done) {
        //uncomment below and update the code to test deleteRepository
        //instance.deleteRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('describeMergeConflicts', function() {
      it('should call describeMergeConflicts successfully', function(done) {
        //uncomment below and update the code to test describeMergeConflicts
        //instance.describeMergeConflicts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('describePullRequestEvents', function() {
      it('should call describePullRequestEvents successfully', function(done) {
        //uncomment below and update the code to test describePullRequestEvents
        //instance.describePullRequestEvents(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('disassociateApprovalRuleTemplateFromRepository', function() {
      it('should call disassociateApprovalRuleTemplateFromRepository successfully', function(done) {
        //uncomment below and update the code to test disassociateApprovalRuleTemplateFromRepository
        //instance.disassociateApprovalRuleTemplateFromRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('evaluatePullRequestApprovalRules', function() {
      it('should call evaluatePullRequestApprovalRules successfully', function(done) {
        //uncomment below and update the code to test evaluatePullRequestApprovalRules
        //instance.evaluatePullRequestApprovalRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getApprovalRuleTemplate', function() {
      it('should call getApprovalRuleTemplate successfully', function(done) {
        //uncomment below and update the code to test getApprovalRuleTemplate
        //instance.getApprovalRuleTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBlob', function() {
      it('should call getBlob successfully', function(done) {
        //uncomment below and update the code to test getBlob
        //instance.getBlob(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBranch', function() {
      it('should call getBranch successfully', function(done) {
        //uncomment below and update the code to test getBranch
        //instance.getBranch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getComment', function() {
      it('should call getComment successfully', function(done) {
        //uncomment below and update the code to test getComment
        //instance.getComment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCommentReactions', function() {
      it('should call getCommentReactions successfully', function(done) {
        //uncomment below and update the code to test getCommentReactions
        //instance.getCommentReactions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCommentsForComparedCommit', function() {
      it('should call getCommentsForComparedCommit successfully', function(done) {
        //uncomment below and update the code to test getCommentsForComparedCommit
        //instance.getCommentsForComparedCommit(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCommentsForPullRequest', function() {
      it('should call getCommentsForPullRequest successfully', function(done) {
        //uncomment below and update the code to test getCommentsForPullRequest
        //instance.getCommentsForPullRequest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCommit', function() {
      it('should call getCommit successfully', function(done) {
        //uncomment below and update the code to test getCommit
        //instance.getCommit(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDifferences', function() {
      it('should call getDifferences successfully', function(done) {
        //uncomment below and update the code to test getDifferences
        //instance.getDifferences(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getFile', function() {
      it('should call getFile successfully', function(done) {
        //uncomment below and update the code to test getFile
        //instance.getFile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getFolder', function() {
      it('should call getFolder successfully', function(done) {
        //uncomment below and update the code to test getFolder
        //instance.getFolder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getMergeCommit', function() {
      it('should call getMergeCommit successfully', function(done) {
        //uncomment below and update the code to test getMergeCommit
        //instance.getMergeCommit(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getMergeConflicts', function() {
      it('should call getMergeConflicts successfully', function(done) {
        //uncomment below and update the code to test getMergeConflicts
        //instance.getMergeConflicts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getMergeOptions', function() {
      it('should call getMergeOptions successfully', function(done) {
        //uncomment below and update the code to test getMergeOptions
        //instance.getMergeOptions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPullRequest', function() {
      it('should call getPullRequest successfully', function(done) {
        //uncomment below and update the code to test getPullRequest
        //instance.getPullRequest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPullRequestApprovalStates', function() {
      it('should call getPullRequestApprovalStates successfully', function(done) {
        //uncomment below and update the code to test getPullRequestApprovalStates
        //instance.getPullRequestApprovalStates(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPullRequestOverrideState', function() {
      it('should call getPullRequestOverrideState successfully', function(done) {
        //uncomment below and update the code to test getPullRequestOverrideState
        //instance.getPullRequestOverrideState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getRepository', function() {
      it('should call getRepository successfully', function(done) {
        //uncomment below and update the code to test getRepository
        //instance.getRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getRepositoryTriggers', function() {
      it('should call getRepositoryTriggers successfully', function(done) {
        //uncomment below and update the code to test getRepositoryTriggers
        //instance.getRepositoryTriggers(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listApprovalRuleTemplates', function() {
      it('should call listApprovalRuleTemplates successfully', function(done) {
        //uncomment below and update the code to test listApprovalRuleTemplates
        //instance.listApprovalRuleTemplates(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listAssociatedApprovalRuleTemplatesForRepository', function() {
      it('should call listAssociatedApprovalRuleTemplatesForRepository successfully', function(done) {
        //uncomment below and update the code to test listAssociatedApprovalRuleTemplatesForRepository
        //instance.listAssociatedApprovalRuleTemplatesForRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listBranches', function() {
      it('should call listBranches successfully', function(done) {
        //uncomment below and update the code to test listBranches
        //instance.listBranches(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listPullRequests', function() {
      it('should call listPullRequests successfully', function(done) {
        //uncomment below and update the code to test listPullRequests
        //instance.listPullRequests(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listRepositories', function() {
      it('should call listRepositories successfully', function(done) {
        //uncomment below and update the code to test listRepositories
        //instance.listRepositories(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listRepositoriesForApprovalRuleTemplate', function() {
      it('should call listRepositoriesForApprovalRuleTemplate successfully', function(done) {
        //uncomment below and update the code to test listRepositoriesForApprovalRuleTemplate
        //instance.listRepositoriesForApprovalRuleTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listTagsForResource', function() {
      it('should call listTagsForResource successfully', function(done) {
        //uncomment below and update the code to test listTagsForResource
        //instance.listTagsForResource(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('mergeBranchesByFastForward', function() {
      it('should call mergeBranchesByFastForward successfully', function(done) {
        //uncomment below and update the code to test mergeBranchesByFastForward
        //instance.mergeBranchesByFastForward(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('mergeBranchesBySquash', function() {
      it('should call mergeBranchesBySquash successfully', function(done) {
        //uncomment below and update the code to test mergeBranchesBySquash
        //instance.mergeBranchesBySquash(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('mergeBranchesByThreeWay', function() {
      it('should call mergeBranchesByThreeWay successfully', function(done) {
        //uncomment below and update the code to test mergeBranchesByThreeWay
        //instance.mergeBranchesByThreeWay(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('mergePullRequestByFastForward', function() {
      it('should call mergePullRequestByFastForward successfully', function(done) {
        //uncomment below and update the code to test mergePullRequestByFastForward
        //instance.mergePullRequestByFastForward(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('mergePullRequestBySquash', function() {
      it('should call mergePullRequestBySquash successfully', function(done) {
        //uncomment below and update the code to test mergePullRequestBySquash
        //instance.mergePullRequestBySquash(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('mergePullRequestByThreeWay', function() {
      it('should call mergePullRequestByThreeWay successfully', function(done) {
        //uncomment below and update the code to test mergePullRequestByThreeWay
        //instance.mergePullRequestByThreeWay(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('overridePullRequestApprovalRules', function() {
      it('should call overridePullRequestApprovalRules successfully', function(done) {
        //uncomment below and update the code to test overridePullRequestApprovalRules
        //instance.overridePullRequestApprovalRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postCommentForComparedCommit', function() {
      it('should call postCommentForComparedCommit successfully', function(done) {
        //uncomment below and update the code to test postCommentForComparedCommit
        //instance.postCommentForComparedCommit(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postCommentForPullRequest', function() {
      it('should call postCommentForPullRequest successfully', function(done) {
        //uncomment below and update the code to test postCommentForPullRequest
        //instance.postCommentForPullRequest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postCommentReply', function() {
      it('should call postCommentReply successfully', function(done) {
        //uncomment below and update the code to test postCommentReply
        //instance.postCommentReply(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putCommentReaction', function() {
      it('should call putCommentReaction successfully', function(done) {
        //uncomment below and update the code to test putCommentReaction
        //instance.putCommentReaction(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putFile', function() {
      it('should call putFile successfully', function(done) {
        //uncomment below and update the code to test putFile
        //instance.putFile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putRepositoryTriggers', function() {
      it('should call putRepositoryTriggers successfully', function(done) {
        //uncomment below and update the code to test putRepositoryTriggers
        //instance.putRepositoryTriggers(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('tagResource', function() {
      it('should call tagResource successfully', function(done) {
        //uncomment below and update the code to test tagResource
        //instance.tagResource(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('testRepositoryTriggers', function() {
      it('should call testRepositoryTriggers successfully', function(done) {
        //uncomment below and update the code to test testRepositoryTriggers
        //instance.testRepositoryTriggers(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('untagResource', function() {
      it('should call untagResource successfully', function(done) {
        //uncomment below and update the code to test untagResource
        //instance.untagResource(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateApprovalRuleTemplateContent', function() {
      it('should call updateApprovalRuleTemplateContent successfully', function(done) {
        //uncomment below and update the code to test updateApprovalRuleTemplateContent
        //instance.updateApprovalRuleTemplateContent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateApprovalRuleTemplateDescription', function() {
      it('should call updateApprovalRuleTemplateDescription successfully', function(done) {
        //uncomment below and update the code to test updateApprovalRuleTemplateDescription
        //instance.updateApprovalRuleTemplateDescription(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateApprovalRuleTemplateName', function() {
      it('should call updateApprovalRuleTemplateName successfully', function(done) {
        //uncomment below and update the code to test updateApprovalRuleTemplateName
        //instance.updateApprovalRuleTemplateName(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateComment', function() {
      it('should call updateComment successfully', function(done) {
        //uncomment below and update the code to test updateComment
        //instance.updateComment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateDefaultBranch', function() {
      it('should call updateDefaultBranch successfully', function(done) {
        //uncomment below and update the code to test updateDefaultBranch
        //instance.updateDefaultBranch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updatePullRequestApprovalRuleContent', function() {
      it('should call updatePullRequestApprovalRuleContent successfully', function(done) {
        //uncomment below and update the code to test updatePullRequestApprovalRuleContent
        //instance.updatePullRequestApprovalRuleContent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updatePullRequestApprovalState', function() {
      it('should call updatePullRequestApprovalState successfully', function(done) {
        //uncomment below and update the code to test updatePullRequestApprovalState
        //instance.updatePullRequestApprovalState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updatePullRequestDescription', function() {
      it('should call updatePullRequestDescription successfully', function(done) {
        //uncomment below and update the code to test updatePullRequestDescription
        //instance.updatePullRequestDescription(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updatePullRequestStatus', function() {
      it('should call updatePullRequestStatus successfully', function(done) {
        //uncomment below and update the code to test updatePullRequestStatus
        //instance.updatePullRequestStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updatePullRequestTitle', function() {
      it('should call updatePullRequestTitle successfully', function(done) {
        //uncomment below and update the code to test updatePullRequestTitle
        //instance.updatePullRequestTitle(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateRepositoryDescription', function() {
      it('should call updateRepositoryDescription successfully', function(done) {
        //uncomment below and update the code to test updateRepositoryDescription
        //instance.updateRepositoryDescription(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateRepositoryName', function() {
      it('should call updateRepositoryName successfully', function(done) {
        //uncomment below and update the code to test updateRepositoryName
        //instance.updateRepositoryName(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
