/*
 * AWS CodeCommit
 * <fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>
 *
 * The version of the OpenAPI document: 2015-04-13
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.PullRequestEventApprovalRuleEventMetadata;
import org.openapitools.client.model.PullRequestEventApprovalRuleOverriddenEventMetadata;
import org.openapitools.client.model.PullRequestEventApprovalStateChangedEventMetadata;
import org.openapitools.client.model.PullRequestEventPullRequestCreatedEventMetadata;
import org.openapitools.client.model.PullRequestEventPullRequestMergedStateChangedEventMetadata;
import org.openapitools.client.model.PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata;
import org.openapitools.client.model.PullRequestEventPullRequestStatusChangedEventMetadata;
import org.openapitools.client.model.PullRequestEventType;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Returns information about a pull request event.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:12:31.970171-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PullRequestEvent {
  public static final String SERIALIZED_NAME_PULL_REQUEST_ID = "pullRequestId";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_ID)
  private String pullRequestId;

  public static final String SERIALIZED_NAME_EVENT_DATE = "eventDate";
  @SerializedName(SERIALIZED_NAME_EVENT_DATE)
  private OffsetDateTime eventDate;

  public static final String SERIALIZED_NAME_PULL_REQUEST_EVENT_TYPE = "pullRequestEventType";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_EVENT_TYPE)
  private PullRequestEventType pullRequestEventType;

  public static final String SERIALIZED_NAME_ACTOR_ARN = "actorArn";
  @SerializedName(SERIALIZED_NAME_ACTOR_ARN)
  private String actorArn;

  public static final String SERIALIZED_NAME_PULL_REQUEST_CREATED_EVENT_METADATA = "pullRequestCreatedEventMetadata";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_CREATED_EVENT_METADATA)
  private PullRequestEventPullRequestCreatedEventMetadata pullRequestCreatedEventMetadata;

  public static final String SERIALIZED_NAME_PULL_REQUEST_STATUS_CHANGED_EVENT_METADATA = "pullRequestStatusChangedEventMetadata";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_STATUS_CHANGED_EVENT_METADATA)
  private PullRequestEventPullRequestStatusChangedEventMetadata pullRequestStatusChangedEventMetadata;

  public static final String SERIALIZED_NAME_PULL_REQUEST_SOURCE_REFERENCE_UPDATED_EVENT_METADATA = "pullRequestSourceReferenceUpdatedEventMetadata";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_SOURCE_REFERENCE_UPDATED_EVENT_METADATA)
  private PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata pullRequestSourceReferenceUpdatedEventMetadata;

  public static final String SERIALIZED_NAME_PULL_REQUEST_MERGED_STATE_CHANGED_EVENT_METADATA = "pullRequestMergedStateChangedEventMetadata";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_MERGED_STATE_CHANGED_EVENT_METADATA)
  private PullRequestEventPullRequestMergedStateChangedEventMetadata pullRequestMergedStateChangedEventMetadata;

  public static final String SERIALIZED_NAME_APPROVAL_RULE_EVENT_METADATA = "approvalRuleEventMetadata";
  @SerializedName(SERIALIZED_NAME_APPROVAL_RULE_EVENT_METADATA)
  private PullRequestEventApprovalRuleEventMetadata approvalRuleEventMetadata;

  public static final String SERIALIZED_NAME_APPROVAL_STATE_CHANGED_EVENT_METADATA = "approvalStateChangedEventMetadata";
  @SerializedName(SERIALIZED_NAME_APPROVAL_STATE_CHANGED_EVENT_METADATA)
  private PullRequestEventApprovalStateChangedEventMetadata approvalStateChangedEventMetadata;

  public static final String SERIALIZED_NAME_APPROVAL_RULE_OVERRIDDEN_EVENT_METADATA = "approvalRuleOverriddenEventMetadata";
  @SerializedName(SERIALIZED_NAME_APPROVAL_RULE_OVERRIDDEN_EVENT_METADATA)
  private PullRequestEventApprovalRuleOverriddenEventMetadata approvalRuleOverriddenEventMetadata;

  public PullRequestEvent() {
  }

  public PullRequestEvent pullRequestId(String pullRequestId) {
    this.pullRequestId = pullRequestId;
    return this;
  }

  /**
   * Get pullRequestId
   * @return pullRequestId
   */
  @javax.annotation.Nullable
  public String getPullRequestId() {
    return pullRequestId;
  }

  public void setPullRequestId(String pullRequestId) {
    this.pullRequestId = pullRequestId;
  }


  public PullRequestEvent eventDate(OffsetDateTime eventDate) {
    this.eventDate = eventDate;
    return this;
  }

  /**
   * Get eventDate
   * @return eventDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEventDate() {
    return eventDate;
  }

  public void setEventDate(OffsetDateTime eventDate) {
    this.eventDate = eventDate;
  }


  public PullRequestEvent pullRequestEventType(PullRequestEventType pullRequestEventType) {
    this.pullRequestEventType = pullRequestEventType;
    return this;
  }

  /**
   * Get pullRequestEventType
   * @return pullRequestEventType
   */
  @javax.annotation.Nullable
  public PullRequestEventType getPullRequestEventType() {
    return pullRequestEventType;
  }

  public void setPullRequestEventType(PullRequestEventType pullRequestEventType) {
    this.pullRequestEventType = pullRequestEventType;
  }


  public PullRequestEvent actorArn(String actorArn) {
    this.actorArn = actorArn;
    return this;
  }

  /**
   * Get actorArn
   * @return actorArn
   */
  @javax.annotation.Nullable
  public String getActorArn() {
    return actorArn;
  }

  public void setActorArn(String actorArn) {
    this.actorArn = actorArn;
  }


  public PullRequestEvent pullRequestCreatedEventMetadata(PullRequestEventPullRequestCreatedEventMetadata pullRequestCreatedEventMetadata) {
    this.pullRequestCreatedEventMetadata = pullRequestCreatedEventMetadata;
    return this;
  }

  /**
   * Get pullRequestCreatedEventMetadata
   * @return pullRequestCreatedEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventPullRequestCreatedEventMetadata getPullRequestCreatedEventMetadata() {
    return pullRequestCreatedEventMetadata;
  }

  public void setPullRequestCreatedEventMetadata(PullRequestEventPullRequestCreatedEventMetadata pullRequestCreatedEventMetadata) {
    this.pullRequestCreatedEventMetadata = pullRequestCreatedEventMetadata;
  }


  public PullRequestEvent pullRequestStatusChangedEventMetadata(PullRequestEventPullRequestStatusChangedEventMetadata pullRequestStatusChangedEventMetadata) {
    this.pullRequestStatusChangedEventMetadata = pullRequestStatusChangedEventMetadata;
    return this;
  }

  /**
   * Get pullRequestStatusChangedEventMetadata
   * @return pullRequestStatusChangedEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventPullRequestStatusChangedEventMetadata getPullRequestStatusChangedEventMetadata() {
    return pullRequestStatusChangedEventMetadata;
  }

  public void setPullRequestStatusChangedEventMetadata(PullRequestEventPullRequestStatusChangedEventMetadata pullRequestStatusChangedEventMetadata) {
    this.pullRequestStatusChangedEventMetadata = pullRequestStatusChangedEventMetadata;
  }


  public PullRequestEvent pullRequestSourceReferenceUpdatedEventMetadata(PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata pullRequestSourceReferenceUpdatedEventMetadata) {
    this.pullRequestSourceReferenceUpdatedEventMetadata = pullRequestSourceReferenceUpdatedEventMetadata;
    return this;
  }

  /**
   * Get pullRequestSourceReferenceUpdatedEventMetadata
   * @return pullRequestSourceReferenceUpdatedEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata getPullRequestSourceReferenceUpdatedEventMetadata() {
    return pullRequestSourceReferenceUpdatedEventMetadata;
  }

  public void setPullRequestSourceReferenceUpdatedEventMetadata(PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata pullRequestSourceReferenceUpdatedEventMetadata) {
    this.pullRequestSourceReferenceUpdatedEventMetadata = pullRequestSourceReferenceUpdatedEventMetadata;
  }


  public PullRequestEvent pullRequestMergedStateChangedEventMetadata(PullRequestEventPullRequestMergedStateChangedEventMetadata pullRequestMergedStateChangedEventMetadata) {
    this.pullRequestMergedStateChangedEventMetadata = pullRequestMergedStateChangedEventMetadata;
    return this;
  }

  /**
   * Get pullRequestMergedStateChangedEventMetadata
   * @return pullRequestMergedStateChangedEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventPullRequestMergedStateChangedEventMetadata getPullRequestMergedStateChangedEventMetadata() {
    return pullRequestMergedStateChangedEventMetadata;
  }

  public void setPullRequestMergedStateChangedEventMetadata(PullRequestEventPullRequestMergedStateChangedEventMetadata pullRequestMergedStateChangedEventMetadata) {
    this.pullRequestMergedStateChangedEventMetadata = pullRequestMergedStateChangedEventMetadata;
  }


  public PullRequestEvent approvalRuleEventMetadata(PullRequestEventApprovalRuleEventMetadata approvalRuleEventMetadata) {
    this.approvalRuleEventMetadata = approvalRuleEventMetadata;
    return this;
  }

  /**
   * Get approvalRuleEventMetadata
   * @return approvalRuleEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventApprovalRuleEventMetadata getApprovalRuleEventMetadata() {
    return approvalRuleEventMetadata;
  }

  public void setApprovalRuleEventMetadata(PullRequestEventApprovalRuleEventMetadata approvalRuleEventMetadata) {
    this.approvalRuleEventMetadata = approvalRuleEventMetadata;
  }


  public PullRequestEvent approvalStateChangedEventMetadata(PullRequestEventApprovalStateChangedEventMetadata approvalStateChangedEventMetadata) {
    this.approvalStateChangedEventMetadata = approvalStateChangedEventMetadata;
    return this;
  }

  /**
   * Get approvalStateChangedEventMetadata
   * @return approvalStateChangedEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventApprovalStateChangedEventMetadata getApprovalStateChangedEventMetadata() {
    return approvalStateChangedEventMetadata;
  }

  public void setApprovalStateChangedEventMetadata(PullRequestEventApprovalStateChangedEventMetadata approvalStateChangedEventMetadata) {
    this.approvalStateChangedEventMetadata = approvalStateChangedEventMetadata;
  }


  public PullRequestEvent approvalRuleOverriddenEventMetadata(PullRequestEventApprovalRuleOverriddenEventMetadata approvalRuleOverriddenEventMetadata) {
    this.approvalRuleOverriddenEventMetadata = approvalRuleOverriddenEventMetadata;
    return this;
  }

  /**
   * Get approvalRuleOverriddenEventMetadata
   * @return approvalRuleOverriddenEventMetadata
   */
  @javax.annotation.Nullable
  public PullRequestEventApprovalRuleOverriddenEventMetadata getApprovalRuleOverriddenEventMetadata() {
    return approvalRuleOverriddenEventMetadata;
  }

  public void setApprovalRuleOverriddenEventMetadata(PullRequestEventApprovalRuleOverriddenEventMetadata approvalRuleOverriddenEventMetadata) {
    this.approvalRuleOverriddenEventMetadata = approvalRuleOverriddenEventMetadata;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PullRequestEvent pullRequestEvent = (PullRequestEvent) o;
    return Objects.equals(this.pullRequestId, pullRequestEvent.pullRequestId) &&
        Objects.equals(this.eventDate, pullRequestEvent.eventDate) &&
        Objects.equals(this.pullRequestEventType, pullRequestEvent.pullRequestEventType) &&
        Objects.equals(this.actorArn, pullRequestEvent.actorArn) &&
        Objects.equals(this.pullRequestCreatedEventMetadata, pullRequestEvent.pullRequestCreatedEventMetadata) &&
        Objects.equals(this.pullRequestStatusChangedEventMetadata, pullRequestEvent.pullRequestStatusChangedEventMetadata) &&
        Objects.equals(this.pullRequestSourceReferenceUpdatedEventMetadata, pullRequestEvent.pullRequestSourceReferenceUpdatedEventMetadata) &&
        Objects.equals(this.pullRequestMergedStateChangedEventMetadata, pullRequestEvent.pullRequestMergedStateChangedEventMetadata) &&
        Objects.equals(this.approvalRuleEventMetadata, pullRequestEvent.approvalRuleEventMetadata) &&
        Objects.equals(this.approvalStateChangedEventMetadata, pullRequestEvent.approvalStateChangedEventMetadata) &&
        Objects.equals(this.approvalRuleOverriddenEventMetadata, pullRequestEvent.approvalRuleOverriddenEventMetadata);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pullRequestId, eventDate, pullRequestEventType, actorArn, pullRequestCreatedEventMetadata, pullRequestStatusChangedEventMetadata, pullRequestSourceReferenceUpdatedEventMetadata, pullRequestMergedStateChangedEventMetadata, approvalRuleEventMetadata, approvalStateChangedEventMetadata, approvalRuleOverriddenEventMetadata);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PullRequestEvent {\n");
    sb.append("    pullRequestId: ").append(toIndentedString(pullRequestId)).append("\n");
    sb.append("    eventDate: ").append(toIndentedString(eventDate)).append("\n");
    sb.append("    pullRequestEventType: ").append(toIndentedString(pullRequestEventType)).append("\n");
    sb.append("    actorArn: ").append(toIndentedString(actorArn)).append("\n");
    sb.append("    pullRequestCreatedEventMetadata: ").append(toIndentedString(pullRequestCreatedEventMetadata)).append("\n");
    sb.append("    pullRequestStatusChangedEventMetadata: ").append(toIndentedString(pullRequestStatusChangedEventMetadata)).append("\n");
    sb.append("    pullRequestSourceReferenceUpdatedEventMetadata: ").append(toIndentedString(pullRequestSourceReferenceUpdatedEventMetadata)).append("\n");
    sb.append("    pullRequestMergedStateChangedEventMetadata: ").append(toIndentedString(pullRequestMergedStateChangedEventMetadata)).append("\n");
    sb.append("    approvalRuleEventMetadata: ").append(toIndentedString(approvalRuleEventMetadata)).append("\n");
    sb.append("    approvalStateChangedEventMetadata: ").append(toIndentedString(approvalStateChangedEventMetadata)).append("\n");
    sb.append("    approvalRuleOverriddenEventMetadata: ").append(toIndentedString(approvalRuleOverriddenEventMetadata)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("pullRequestId");
    openapiFields.add("eventDate");
    openapiFields.add("pullRequestEventType");
    openapiFields.add("actorArn");
    openapiFields.add("pullRequestCreatedEventMetadata");
    openapiFields.add("pullRequestStatusChangedEventMetadata");
    openapiFields.add("pullRequestSourceReferenceUpdatedEventMetadata");
    openapiFields.add("pullRequestMergedStateChangedEventMetadata");
    openapiFields.add("approvalRuleEventMetadata");
    openapiFields.add("approvalStateChangedEventMetadata");
    openapiFields.add("approvalRuleOverriddenEventMetadata");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PullRequestEvent
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PullRequestEvent.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PullRequestEvent is not found in the empty JSON string", PullRequestEvent.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PullRequestEvent.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PullRequestEvent` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `pullRequestId`
      if (jsonObj.get("pullRequestId") != null && !jsonObj.get("pullRequestId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("pullRequestId"));
      }
      // validate the optional field `eventDate`
      if (jsonObj.get("eventDate") != null && !jsonObj.get("eventDate").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("eventDate"));
      }
      // validate the optional field `pullRequestEventType`
      if (jsonObj.get("pullRequestEventType") != null && !jsonObj.get("pullRequestEventType").isJsonNull()) {
        PullRequestEventType.validateJsonElement(jsonObj.get("pullRequestEventType"));
      }
      // validate the optional field `actorArn`
      if (jsonObj.get("actorArn") != null && !jsonObj.get("actorArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("actorArn"));
      }
      // validate the optional field `pullRequestCreatedEventMetadata`
      if (jsonObj.get("pullRequestCreatedEventMetadata") != null && !jsonObj.get("pullRequestCreatedEventMetadata").isJsonNull()) {
        PullRequestEventPullRequestCreatedEventMetadata.validateJsonElement(jsonObj.get("pullRequestCreatedEventMetadata"));
      }
      // validate the optional field `pullRequestStatusChangedEventMetadata`
      if (jsonObj.get("pullRequestStatusChangedEventMetadata") != null && !jsonObj.get("pullRequestStatusChangedEventMetadata").isJsonNull()) {
        PullRequestEventPullRequestStatusChangedEventMetadata.validateJsonElement(jsonObj.get("pullRequestStatusChangedEventMetadata"));
      }
      // validate the optional field `pullRequestSourceReferenceUpdatedEventMetadata`
      if (jsonObj.get("pullRequestSourceReferenceUpdatedEventMetadata") != null && !jsonObj.get("pullRequestSourceReferenceUpdatedEventMetadata").isJsonNull()) {
        PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata.validateJsonElement(jsonObj.get("pullRequestSourceReferenceUpdatedEventMetadata"));
      }
      // validate the optional field `pullRequestMergedStateChangedEventMetadata`
      if (jsonObj.get("pullRequestMergedStateChangedEventMetadata") != null && !jsonObj.get("pullRequestMergedStateChangedEventMetadata").isJsonNull()) {
        PullRequestEventPullRequestMergedStateChangedEventMetadata.validateJsonElement(jsonObj.get("pullRequestMergedStateChangedEventMetadata"));
      }
      // validate the optional field `approvalRuleEventMetadata`
      if (jsonObj.get("approvalRuleEventMetadata") != null && !jsonObj.get("approvalRuleEventMetadata").isJsonNull()) {
        PullRequestEventApprovalRuleEventMetadata.validateJsonElement(jsonObj.get("approvalRuleEventMetadata"));
      }
      // validate the optional field `approvalStateChangedEventMetadata`
      if (jsonObj.get("approvalStateChangedEventMetadata") != null && !jsonObj.get("approvalStateChangedEventMetadata").isJsonNull()) {
        PullRequestEventApprovalStateChangedEventMetadata.validateJsonElement(jsonObj.get("approvalStateChangedEventMetadata"));
      }
      // validate the optional field `approvalRuleOverriddenEventMetadata`
      if (jsonObj.get("approvalRuleOverriddenEventMetadata") != null && !jsonObj.get("approvalRuleOverriddenEventMetadata").isJsonNull()) {
        PullRequestEventApprovalRuleOverriddenEventMetadata.validateJsonElement(jsonObj.get("approvalRuleOverriddenEventMetadata"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PullRequestEvent.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PullRequestEvent' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PullRequestEvent> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PullRequestEvent.class));

       return (TypeAdapter<T>) new TypeAdapter<PullRequestEvent>() {
           @Override
           public void write(JsonWriter out, PullRequestEvent value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PullRequestEvent read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PullRequestEvent given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PullRequestEvent
   * @throws IOException if the JSON string is invalid with respect to PullRequestEvent
   */
  public static PullRequestEvent fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PullRequestEvent.class);
  }

  /**
   * Convert an instance of PullRequestEvent to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

