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
import org.openapitools.client.model.ApprovalRuleOriginApprovalRuleTemplate;

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
 * UpdatePullRequestApprovalRuleContentOutputApprovalRule
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:12:31.970171-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdatePullRequestApprovalRuleContentOutputApprovalRule {
  public static final String SERIALIZED_NAME_APPROVAL_RULE_ID = "approvalRuleId";
  @SerializedName(SERIALIZED_NAME_APPROVAL_RULE_ID)
  private String approvalRuleId;

  public static final String SERIALIZED_NAME_APPROVAL_RULE_NAME = "approvalRuleName";
  @SerializedName(SERIALIZED_NAME_APPROVAL_RULE_NAME)
  private String approvalRuleName;

  public static final String SERIALIZED_NAME_APPROVAL_RULE_CONTENT = "approvalRuleContent";
  @SerializedName(SERIALIZED_NAME_APPROVAL_RULE_CONTENT)
  private String approvalRuleContent;

  public static final String SERIALIZED_NAME_RULE_CONTENT_SHA256 = "ruleContentSha256";
  @SerializedName(SERIALIZED_NAME_RULE_CONTENT_SHA256)
  private String ruleContentSha256;

  public static final String SERIALIZED_NAME_LAST_MODIFIED_DATE = "lastModifiedDate";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED_DATE)
  private OffsetDateTime lastModifiedDate;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private OffsetDateTime creationDate;

  public static final String SERIALIZED_NAME_LAST_MODIFIED_USER = "lastModifiedUser";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED_USER)
  private String lastModifiedUser;

  public static final String SERIALIZED_NAME_ORIGIN_APPROVAL_RULE_TEMPLATE = "originApprovalRuleTemplate";
  @SerializedName(SERIALIZED_NAME_ORIGIN_APPROVAL_RULE_TEMPLATE)
  private ApprovalRuleOriginApprovalRuleTemplate originApprovalRuleTemplate;

  public UpdatePullRequestApprovalRuleContentOutputApprovalRule() {
  }

  public UpdatePullRequestApprovalRuleContentOutputApprovalRule approvalRuleId(String approvalRuleId) {
    this.approvalRuleId = approvalRuleId;
    return this;
  }

  /**
   * Get approvalRuleId
   * @return approvalRuleId
   */
  @javax.annotation.Nullable
  public String getApprovalRuleId() {
    return approvalRuleId;
  }

  public void setApprovalRuleId(String approvalRuleId) {
    this.approvalRuleId = approvalRuleId;
  }


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule approvalRuleName(String approvalRuleName) {
    this.approvalRuleName = approvalRuleName;
    return this;
  }

  /**
   * Get approvalRuleName
   * @return approvalRuleName
   */
  @javax.annotation.Nullable
  public String getApprovalRuleName() {
    return approvalRuleName;
  }

  public void setApprovalRuleName(String approvalRuleName) {
    this.approvalRuleName = approvalRuleName;
  }


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule approvalRuleContent(String approvalRuleContent) {
    this.approvalRuleContent = approvalRuleContent;
    return this;
  }

  /**
   * Get approvalRuleContent
   * @return approvalRuleContent
   */
  @javax.annotation.Nullable
  public String getApprovalRuleContent() {
    return approvalRuleContent;
  }

  public void setApprovalRuleContent(String approvalRuleContent) {
    this.approvalRuleContent = approvalRuleContent;
  }


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule ruleContentSha256(String ruleContentSha256) {
    this.ruleContentSha256 = ruleContentSha256;
    return this;
  }

  /**
   * Get ruleContentSha256
   * @return ruleContentSha256
   */
  @javax.annotation.Nullable
  public String getRuleContentSha256() {
    return ruleContentSha256;
  }

  public void setRuleContentSha256(String ruleContentSha256) {
    this.ruleContentSha256 = ruleContentSha256;
  }


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule lastModifiedDate(OffsetDateTime lastModifiedDate) {
    this.lastModifiedDate = lastModifiedDate;
    return this;
  }

  /**
   * Get lastModifiedDate
   * @return lastModifiedDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastModifiedDate() {
    return lastModifiedDate;
  }

  public void setLastModifiedDate(OffsetDateTime lastModifiedDate) {
    this.lastModifiedDate = lastModifiedDate;
  }


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule creationDate(OffsetDateTime creationDate) {
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


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule lastModifiedUser(String lastModifiedUser) {
    this.lastModifiedUser = lastModifiedUser;
    return this;
  }

  /**
   * Get lastModifiedUser
   * @return lastModifiedUser
   */
  @javax.annotation.Nullable
  public String getLastModifiedUser() {
    return lastModifiedUser;
  }

  public void setLastModifiedUser(String lastModifiedUser) {
    this.lastModifiedUser = lastModifiedUser;
  }


  public UpdatePullRequestApprovalRuleContentOutputApprovalRule originApprovalRuleTemplate(ApprovalRuleOriginApprovalRuleTemplate originApprovalRuleTemplate) {
    this.originApprovalRuleTemplate = originApprovalRuleTemplate;
    return this;
  }

  /**
   * Get originApprovalRuleTemplate
   * @return originApprovalRuleTemplate
   */
  @javax.annotation.Nullable
  public ApprovalRuleOriginApprovalRuleTemplate getOriginApprovalRuleTemplate() {
    return originApprovalRuleTemplate;
  }

  public void setOriginApprovalRuleTemplate(ApprovalRuleOriginApprovalRuleTemplate originApprovalRuleTemplate) {
    this.originApprovalRuleTemplate = originApprovalRuleTemplate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdatePullRequestApprovalRuleContentOutputApprovalRule updatePullRequestApprovalRuleContentOutputApprovalRule = (UpdatePullRequestApprovalRuleContentOutputApprovalRule) o;
    return Objects.equals(this.approvalRuleId, updatePullRequestApprovalRuleContentOutputApprovalRule.approvalRuleId) &&
        Objects.equals(this.approvalRuleName, updatePullRequestApprovalRuleContentOutputApprovalRule.approvalRuleName) &&
        Objects.equals(this.approvalRuleContent, updatePullRequestApprovalRuleContentOutputApprovalRule.approvalRuleContent) &&
        Objects.equals(this.ruleContentSha256, updatePullRequestApprovalRuleContentOutputApprovalRule.ruleContentSha256) &&
        Objects.equals(this.lastModifiedDate, updatePullRequestApprovalRuleContentOutputApprovalRule.lastModifiedDate) &&
        Objects.equals(this.creationDate, updatePullRequestApprovalRuleContentOutputApprovalRule.creationDate) &&
        Objects.equals(this.lastModifiedUser, updatePullRequestApprovalRuleContentOutputApprovalRule.lastModifiedUser) &&
        Objects.equals(this.originApprovalRuleTemplate, updatePullRequestApprovalRuleContentOutputApprovalRule.originApprovalRuleTemplate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(approvalRuleId, approvalRuleName, approvalRuleContent, ruleContentSha256, lastModifiedDate, creationDate, lastModifiedUser, originApprovalRuleTemplate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdatePullRequestApprovalRuleContentOutputApprovalRule {\n");
    sb.append("    approvalRuleId: ").append(toIndentedString(approvalRuleId)).append("\n");
    sb.append("    approvalRuleName: ").append(toIndentedString(approvalRuleName)).append("\n");
    sb.append("    approvalRuleContent: ").append(toIndentedString(approvalRuleContent)).append("\n");
    sb.append("    ruleContentSha256: ").append(toIndentedString(ruleContentSha256)).append("\n");
    sb.append("    lastModifiedDate: ").append(toIndentedString(lastModifiedDate)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    lastModifiedUser: ").append(toIndentedString(lastModifiedUser)).append("\n");
    sb.append("    originApprovalRuleTemplate: ").append(toIndentedString(originApprovalRuleTemplate)).append("\n");
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
    openapiFields.add("approvalRuleId");
    openapiFields.add("approvalRuleName");
    openapiFields.add("approvalRuleContent");
    openapiFields.add("ruleContentSha256");
    openapiFields.add("lastModifiedDate");
    openapiFields.add("creationDate");
    openapiFields.add("lastModifiedUser");
    openapiFields.add("originApprovalRuleTemplate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdatePullRequestApprovalRuleContentOutputApprovalRule
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdatePullRequestApprovalRuleContentOutputApprovalRule.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdatePullRequestApprovalRuleContentOutputApprovalRule is not found in the empty JSON string", UpdatePullRequestApprovalRuleContentOutputApprovalRule.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdatePullRequestApprovalRuleContentOutputApprovalRule.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdatePullRequestApprovalRuleContentOutputApprovalRule` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `approvalRuleId`
      if (jsonObj.get("approvalRuleId") != null && !jsonObj.get("approvalRuleId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("approvalRuleId"));
      }
      // validate the optional field `approvalRuleName`
      if (jsonObj.get("approvalRuleName") != null && !jsonObj.get("approvalRuleName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("approvalRuleName"));
      }
      // validate the optional field `approvalRuleContent`
      if (jsonObj.get("approvalRuleContent") != null && !jsonObj.get("approvalRuleContent").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("approvalRuleContent"));
      }
      // validate the optional field `ruleContentSha256`
      if (jsonObj.get("ruleContentSha256") != null && !jsonObj.get("ruleContentSha256").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("ruleContentSha256"));
      }
      // validate the optional field `lastModifiedDate`
      if (jsonObj.get("lastModifiedDate") != null && !jsonObj.get("lastModifiedDate").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("lastModifiedDate"));
      }
      // validate the optional field `creationDate`
      if (jsonObj.get("creationDate") != null && !jsonObj.get("creationDate").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("creationDate"));
      }
      // validate the optional field `lastModifiedUser`
      if (jsonObj.get("lastModifiedUser") != null && !jsonObj.get("lastModifiedUser").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("lastModifiedUser"));
      }
      // validate the optional field `originApprovalRuleTemplate`
      if (jsonObj.get("originApprovalRuleTemplate") != null && !jsonObj.get("originApprovalRuleTemplate").isJsonNull()) {
        ApprovalRuleOriginApprovalRuleTemplate.validateJsonElement(jsonObj.get("originApprovalRuleTemplate"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdatePullRequestApprovalRuleContentOutputApprovalRule.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdatePullRequestApprovalRuleContentOutputApprovalRule' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdatePullRequestApprovalRuleContentOutputApprovalRule> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdatePullRequestApprovalRuleContentOutputApprovalRule.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdatePullRequestApprovalRuleContentOutputApprovalRule>() {
           @Override
           public void write(JsonWriter out, UpdatePullRequestApprovalRuleContentOutputApprovalRule value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdatePullRequestApprovalRuleContentOutputApprovalRule read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdatePullRequestApprovalRuleContentOutputApprovalRule given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdatePullRequestApprovalRuleContentOutputApprovalRule
   * @throws IOException if the JSON string is invalid with respect to UpdatePullRequestApprovalRuleContentOutputApprovalRule
   */
  public static UpdatePullRequestApprovalRuleContentOutputApprovalRule fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdatePullRequestApprovalRuleContentOutputApprovalRule.class);
  }

  /**
   * Convert an instance of UpdatePullRequestApprovalRuleContentOutputApprovalRule to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

