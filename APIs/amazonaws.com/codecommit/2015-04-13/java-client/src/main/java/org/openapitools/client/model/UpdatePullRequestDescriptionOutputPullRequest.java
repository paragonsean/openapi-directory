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
import java.util.List;
import org.openapitools.client.model.PullRequestStatusEnum;

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
 * UpdatePullRequestDescriptionOutputPullRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:12:31.970171-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdatePullRequestDescriptionOutputPullRequest {
  public static final String SERIALIZED_NAME_PULL_REQUEST_ID = "pullRequestId";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_ID)
  private String pullRequestId;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_LAST_ACTIVITY_DATE = "lastActivityDate";
  @SerializedName(SERIALIZED_NAME_LAST_ACTIVITY_DATE)
  private OffsetDateTime lastActivityDate;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private OffsetDateTime creationDate;

  public static final String SERIALIZED_NAME_PULL_REQUEST_STATUS = "pullRequestStatus";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_STATUS)
  private PullRequestStatusEnum pullRequestStatus;

  public static final String SERIALIZED_NAME_AUTHOR_ARN = "authorArn";
  @SerializedName(SERIALIZED_NAME_AUTHOR_ARN)
  private String authorArn;

  public static final String SERIALIZED_NAME_PULL_REQUEST_TARGETS = "pullRequestTargets";
  @SerializedName(SERIALIZED_NAME_PULL_REQUEST_TARGETS)
  private List pullRequestTargets;

  public static final String SERIALIZED_NAME_CLIENT_REQUEST_TOKEN = "clientRequestToken";
  @SerializedName(SERIALIZED_NAME_CLIENT_REQUEST_TOKEN)
  private String clientRequestToken;

  public static final String SERIALIZED_NAME_REVISION_ID = "revisionId";
  @SerializedName(SERIALIZED_NAME_REVISION_ID)
  private String revisionId;

  public static final String SERIALIZED_NAME_APPROVAL_RULES = "approvalRules";
  @SerializedName(SERIALIZED_NAME_APPROVAL_RULES)
  private List approvalRules;

  public UpdatePullRequestDescriptionOutputPullRequest() {
  }

  public UpdatePullRequestDescriptionOutputPullRequest pullRequestId(String pullRequestId) {
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


  public UpdatePullRequestDescriptionOutputPullRequest title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public UpdatePullRequestDescriptionOutputPullRequest description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public UpdatePullRequestDescriptionOutputPullRequest lastActivityDate(OffsetDateTime lastActivityDate) {
    this.lastActivityDate = lastActivityDate;
    return this;
  }

  /**
   * Get lastActivityDate
   * @return lastActivityDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastActivityDate() {
    return lastActivityDate;
  }

  public void setLastActivityDate(OffsetDateTime lastActivityDate) {
    this.lastActivityDate = lastActivityDate;
  }


  public UpdatePullRequestDescriptionOutputPullRequest creationDate(OffsetDateTime creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * Get creationDate
   * @return creationDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(OffsetDateTime creationDate) {
    this.creationDate = creationDate;
  }


  public UpdatePullRequestDescriptionOutputPullRequest pullRequestStatus(PullRequestStatusEnum pullRequestStatus) {
    this.pullRequestStatus = pullRequestStatus;
    return this;
  }

  /**
   * Get pullRequestStatus
   * @return pullRequestStatus
   */
  @javax.annotation.Nullable
  public PullRequestStatusEnum getPullRequestStatus() {
    return pullRequestStatus;
  }

  public void setPullRequestStatus(PullRequestStatusEnum pullRequestStatus) {
    this.pullRequestStatus = pullRequestStatus;
  }


  public UpdatePullRequestDescriptionOutputPullRequest authorArn(String authorArn) {
    this.authorArn = authorArn;
    return this;
  }

  /**
   * Get authorArn
   * @return authorArn
   */
  @javax.annotation.Nullable
  public String getAuthorArn() {
    return authorArn;
  }

  public void setAuthorArn(String authorArn) {
    this.authorArn = authorArn;
  }


  public UpdatePullRequestDescriptionOutputPullRequest pullRequestTargets(List pullRequestTargets) {
    this.pullRequestTargets = pullRequestTargets;
    return this;
  }

  /**
   * Get pullRequestTargets
   * @return pullRequestTargets
   */
  @javax.annotation.Nullable
  public List getPullRequestTargets() {
    return pullRequestTargets;
  }

  public void setPullRequestTargets(List pullRequestTargets) {
    this.pullRequestTargets = pullRequestTargets;
  }


  public UpdatePullRequestDescriptionOutputPullRequest clientRequestToken(String clientRequestToken) {
    this.clientRequestToken = clientRequestToken;
    return this;
  }

  /**
   * Get clientRequestToken
   * @return clientRequestToken
   */
  @javax.annotation.Nullable
  public String getClientRequestToken() {
    return clientRequestToken;
  }

  public void setClientRequestToken(String clientRequestToken) {
    this.clientRequestToken = clientRequestToken;
  }


  public UpdatePullRequestDescriptionOutputPullRequest revisionId(String revisionId) {
    this.revisionId = revisionId;
    return this;
  }

  /**
   * Get revisionId
   * @return revisionId
   */
  @javax.annotation.Nullable
  public String getRevisionId() {
    return revisionId;
  }

  public void setRevisionId(String revisionId) {
    this.revisionId = revisionId;
  }


  public UpdatePullRequestDescriptionOutputPullRequest approvalRules(List approvalRules) {
    this.approvalRules = approvalRules;
    return this;
  }

  /**
   * Get approvalRules
   * @return approvalRules
   */
  @javax.annotation.Nullable
  public List getApprovalRules() {
    return approvalRules;
  }

  public void setApprovalRules(List approvalRules) {
    this.approvalRules = approvalRules;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdatePullRequestDescriptionOutputPullRequest updatePullRequestDescriptionOutputPullRequest = (UpdatePullRequestDescriptionOutputPullRequest) o;
    return Objects.equals(this.pullRequestId, updatePullRequestDescriptionOutputPullRequest.pullRequestId) &&
        Objects.equals(this.title, updatePullRequestDescriptionOutputPullRequest.title) &&
        Objects.equals(this.description, updatePullRequestDescriptionOutputPullRequest.description) &&
        Objects.equals(this.lastActivityDate, updatePullRequestDescriptionOutputPullRequest.lastActivityDate) &&
        Objects.equals(this.creationDate, updatePullRequestDescriptionOutputPullRequest.creationDate) &&
        Objects.equals(this.pullRequestStatus, updatePullRequestDescriptionOutputPullRequest.pullRequestStatus) &&
        Objects.equals(this.authorArn, updatePullRequestDescriptionOutputPullRequest.authorArn) &&
        Objects.equals(this.pullRequestTargets, updatePullRequestDescriptionOutputPullRequest.pullRequestTargets) &&
        Objects.equals(this.clientRequestToken, updatePullRequestDescriptionOutputPullRequest.clientRequestToken) &&
        Objects.equals(this.revisionId, updatePullRequestDescriptionOutputPullRequest.revisionId) &&
        Objects.equals(this.approvalRules, updatePullRequestDescriptionOutputPullRequest.approvalRules);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pullRequestId, title, description, lastActivityDate, creationDate, pullRequestStatus, authorArn, pullRequestTargets, clientRequestToken, revisionId, approvalRules);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdatePullRequestDescriptionOutputPullRequest {\n");
    sb.append("    pullRequestId: ").append(toIndentedString(pullRequestId)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    lastActivityDate: ").append(toIndentedString(lastActivityDate)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    pullRequestStatus: ").append(toIndentedString(pullRequestStatus)).append("\n");
    sb.append("    authorArn: ").append(toIndentedString(authorArn)).append("\n");
    sb.append("    pullRequestTargets: ").append(toIndentedString(pullRequestTargets)).append("\n");
    sb.append("    clientRequestToken: ").append(toIndentedString(clientRequestToken)).append("\n");
    sb.append("    revisionId: ").append(toIndentedString(revisionId)).append("\n");
    sb.append("    approvalRules: ").append(toIndentedString(approvalRules)).append("\n");
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
    openapiFields.add("title");
    openapiFields.add("description");
    openapiFields.add("lastActivityDate");
    openapiFields.add("creationDate");
    openapiFields.add("pullRequestStatus");
    openapiFields.add("authorArn");
    openapiFields.add("pullRequestTargets");
    openapiFields.add("clientRequestToken");
    openapiFields.add("revisionId");
    openapiFields.add("approvalRules");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdatePullRequestDescriptionOutputPullRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdatePullRequestDescriptionOutputPullRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdatePullRequestDescriptionOutputPullRequest is not found in the empty JSON string", UpdatePullRequestDescriptionOutputPullRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdatePullRequestDescriptionOutputPullRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdatePullRequestDescriptionOutputPullRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `pullRequestId`
      if (jsonObj.get("pullRequestId") != null && !jsonObj.get("pullRequestId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("pullRequestId"));
      }
      // validate the optional field `title`
      if (jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("title"));
      }
      // validate the optional field `description`
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("description"));
      }
      // validate the optional field `lastActivityDate`
      if (jsonObj.get("lastActivityDate") != null && !jsonObj.get("lastActivityDate").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("lastActivityDate"));
      }
      // validate the optional field `creationDate`
      if (jsonObj.get("creationDate") != null && !jsonObj.get("creationDate").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("creationDate"));
      }
      // validate the optional field `pullRequestStatus`
      if (jsonObj.get("pullRequestStatus") != null && !jsonObj.get("pullRequestStatus").isJsonNull()) {
        PullRequestStatusEnum.validateJsonElement(jsonObj.get("pullRequestStatus"));
      }
      // validate the optional field `authorArn`
      if (jsonObj.get("authorArn") != null && !jsonObj.get("authorArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("authorArn"));
      }
      // validate the optional field `pullRequestTargets`
      if (jsonObj.get("pullRequestTargets") != null && !jsonObj.get("pullRequestTargets").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("pullRequestTargets"));
      }
      // validate the optional field `clientRequestToken`
      if (jsonObj.get("clientRequestToken") != null && !jsonObj.get("clientRequestToken").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("clientRequestToken"));
      }
      // validate the optional field `revisionId`
      if (jsonObj.get("revisionId") != null && !jsonObj.get("revisionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("revisionId"));
      }
      // validate the optional field `approvalRules`
      if (jsonObj.get("approvalRules") != null && !jsonObj.get("approvalRules").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("approvalRules"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdatePullRequestDescriptionOutputPullRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdatePullRequestDescriptionOutputPullRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdatePullRequestDescriptionOutputPullRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdatePullRequestDescriptionOutputPullRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdatePullRequestDescriptionOutputPullRequest>() {
           @Override
           public void write(JsonWriter out, UpdatePullRequestDescriptionOutputPullRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdatePullRequestDescriptionOutputPullRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdatePullRequestDescriptionOutputPullRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdatePullRequestDescriptionOutputPullRequest
   * @throws IOException if the JSON string is invalid with respect to UpdatePullRequestDescriptionOutputPullRequest
   */
  public static UpdatePullRequestDescriptionOutputPullRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdatePullRequestDescriptionOutputPullRequest.class);
  }

  /**
   * Convert an instance of UpdatePullRequestDescriptionOutputPullRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

