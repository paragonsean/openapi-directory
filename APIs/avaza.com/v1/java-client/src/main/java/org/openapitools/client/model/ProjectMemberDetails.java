/*
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 * 
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
import java.util.Arrays;

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
 * ProjectMemberDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectMemberDetails {
  public static final String SERIALIZED_NAME_BUDGET_AMOUNT = "BudgetAmount";
  @SerializedName(SERIALIZED_NAME_BUDGET_AMOUNT)
  private Double budgetAmount;

  public static final String SERIALIZED_NAME_COST_AMOUNT = "CostAmount";
  @SerializedName(SERIALIZED_NAME_COST_AMOUNT)
  private Double costAmount;

  public static final String SERIALIZED_NAME_EMAIL = "Email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FIRSTNAME = "Firstname";
  @SerializedName(SERIALIZED_NAME_FIRSTNAME)
  private String firstname;

  public static final String SERIALIZED_NAME_FULLNAME = "Fullname";
  @SerializedName(SERIALIZED_NAME_FULLNAME)
  private String fullname;

  public static final String SERIALIZED_NAME_LASTNAME = "Lastname";
  @SerializedName(SERIALIZED_NAME_LASTNAME)
  private String lastname;

  public static final String SERIALIZED_NAME_PROJECT_I_D_F_K = "ProjectIDFK";
  @SerializedName(SERIALIZED_NAME_PROJECT_I_D_F_K)
  private Integer projectIDFK;

  public static final String SERIALIZED_NAME_RATE_AMOUNT = "RateAmount";
  @SerializedName(SERIALIZED_NAME_RATE_AMOUNT)
  private Double rateAmount;

  public static final String SERIALIZED_NAME_USER_I_D_F_K = "UserIDFK";
  @SerializedName(SERIALIZED_NAME_USER_I_D_F_K)
  private Integer userIDFK;

  public static final String SERIALIZED_NAME_CAN_COMMENT_ON_TASKS = "canCommentOnTasks";
  @SerializedName(SERIALIZED_NAME_CAN_COMMENT_ON_TASKS)
  private Boolean canCommentOnTasks;

  public static final String SERIALIZED_NAME_CAN_CREATE_TASKS = "canCreateTasks";
  @SerializedName(SERIALIZED_NAME_CAN_CREATE_TASKS)
  private Boolean canCreateTasks;

  public static final String SERIALIZED_NAME_CAN_DELETE_TASKS = "canDeleteTasks";
  @SerializedName(SERIALIZED_NAME_CAN_DELETE_TASKS)
  private Boolean canDeleteTasks;

  public static final String SERIALIZED_NAME_CAN_UPDATE_TASKS = "canUpdateTasks";
  @SerializedName(SERIALIZED_NAME_CAN_UPDATE_TASKS)
  private Boolean canUpdateTasks;

  public static final String SERIALIZED_NAME_IS_MEMBER_DISABLED = "isMemberDisabled";
  @SerializedName(SERIALIZED_NAME_IS_MEMBER_DISABLED)
  private Boolean isMemberDisabled;

  public static final String SERIALIZED_NAME_IS_TIMESHEET_ALLOWED = "isTimesheetAllowed";
  @SerializedName(SERIALIZED_NAME_IS_TIMESHEET_ALLOWED)
  private Boolean isTimesheetAllowed;

  public static final String SERIALIZED_NAME_IS_TIMESHEET_APPROVAL_REQUIRED = "isTimesheetApprovalRequired";
  @SerializedName(SERIALIZED_NAME_IS_TIMESHEET_APPROVAL_REQUIRED)
  private Boolean isTimesheetApprovalRequired;

  public static final String SERIALIZED_NAME_IS_TIMESHEET_APPROVER = "isTimesheetApprover";
  @SerializedName(SERIALIZED_NAME_IS_TIMESHEET_APPROVER)
  private Boolean isTimesheetApprover;

  public ProjectMemberDetails() {
  }

  public ProjectMemberDetails budgetAmount(Double budgetAmount) {
    this.budgetAmount = budgetAmount;
    return this;
  }

  /**
   * Get budgetAmount
   * @return budgetAmount
   */
  @javax.annotation.Nullable
  public Double getBudgetAmount() {
    return budgetAmount;
  }

  public void setBudgetAmount(Double budgetAmount) {
    this.budgetAmount = budgetAmount;
  }


  public ProjectMemberDetails costAmount(Double costAmount) {
    this.costAmount = costAmount;
    return this;
  }

  /**
   * Get costAmount
   * @return costAmount
   */
  @javax.annotation.Nullable
  public Double getCostAmount() {
    return costAmount;
  }

  public void setCostAmount(Double costAmount) {
    this.costAmount = costAmount;
  }


  public ProjectMemberDetails email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public ProjectMemberDetails firstname(String firstname) {
    this.firstname = firstname;
    return this;
  }

  /**
   * Get firstname
   * @return firstname
   */
  @javax.annotation.Nullable
  public String getFirstname() {
    return firstname;
  }

  public void setFirstname(String firstname) {
    this.firstname = firstname;
  }


  public ProjectMemberDetails fullname(String fullname) {
    this.fullname = fullname;
    return this;
  }

  /**
   * Get fullname
   * @return fullname
   */
  @javax.annotation.Nullable
  public String getFullname() {
    return fullname;
  }

  public void setFullname(String fullname) {
    this.fullname = fullname;
  }


  public ProjectMemberDetails lastname(String lastname) {
    this.lastname = lastname;
    return this;
  }

  /**
   * Get lastname
   * @return lastname
   */
  @javax.annotation.Nullable
  public String getLastname() {
    return lastname;
  }

  public void setLastname(String lastname) {
    this.lastname = lastname;
  }


  public ProjectMemberDetails projectIDFK(Integer projectIDFK) {
    this.projectIDFK = projectIDFK;
    return this;
  }

  /**
   * Get projectIDFK
   * @return projectIDFK
   */
  @javax.annotation.Nullable
  public Integer getProjectIDFK() {
    return projectIDFK;
  }

  public void setProjectIDFK(Integer projectIDFK) {
    this.projectIDFK = projectIDFK;
  }


  public ProjectMemberDetails rateAmount(Double rateAmount) {
    this.rateAmount = rateAmount;
    return this;
  }

  /**
   * Get rateAmount
   * @return rateAmount
   */
  @javax.annotation.Nullable
  public Double getRateAmount() {
    return rateAmount;
  }

  public void setRateAmount(Double rateAmount) {
    this.rateAmount = rateAmount;
  }


  public ProjectMemberDetails userIDFK(Integer userIDFK) {
    this.userIDFK = userIDFK;
    return this;
  }

  /**
   * Get userIDFK
   * @return userIDFK
   */
  @javax.annotation.Nullable
  public Integer getUserIDFK() {
    return userIDFK;
  }

  public void setUserIDFK(Integer userIDFK) {
    this.userIDFK = userIDFK;
  }


  public ProjectMemberDetails canCommentOnTasks(Boolean canCommentOnTasks) {
    this.canCommentOnTasks = canCommentOnTasks;
    return this;
  }

  /**
   * Get canCommentOnTasks
   * @return canCommentOnTasks
   */
  @javax.annotation.Nullable
  public Boolean getCanCommentOnTasks() {
    return canCommentOnTasks;
  }

  public void setCanCommentOnTasks(Boolean canCommentOnTasks) {
    this.canCommentOnTasks = canCommentOnTasks;
  }


  public ProjectMemberDetails canCreateTasks(Boolean canCreateTasks) {
    this.canCreateTasks = canCreateTasks;
    return this;
  }

  /**
   * Get canCreateTasks
   * @return canCreateTasks
   */
  @javax.annotation.Nullable
  public Boolean getCanCreateTasks() {
    return canCreateTasks;
  }

  public void setCanCreateTasks(Boolean canCreateTasks) {
    this.canCreateTasks = canCreateTasks;
  }


  public ProjectMemberDetails canDeleteTasks(Boolean canDeleteTasks) {
    this.canDeleteTasks = canDeleteTasks;
    return this;
  }

  /**
   * Get canDeleteTasks
   * @return canDeleteTasks
   */
  @javax.annotation.Nullable
  public Boolean getCanDeleteTasks() {
    return canDeleteTasks;
  }

  public void setCanDeleteTasks(Boolean canDeleteTasks) {
    this.canDeleteTasks = canDeleteTasks;
  }


  public ProjectMemberDetails canUpdateTasks(Boolean canUpdateTasks) {
    this.canUpdateTasks = canUpdateTasks;
    return this;
  }

  /**
   * Get canUpdateTasks
   * @return canUpdateTasks
   */
  @javax.annotation.Nullable
  public Boolean getCanUpdateTasks() {
    return canUpdateTasks;
  }

  public void setCanUpdateTasks(Boolean canUpdateTasks) {
    this.canUpdateTasks = canUpdateTasks;
  }


  public ProjectMemberDetails isMemberDisabled(Boolean isMemberDisabled) {
    this.isMemberDisabled = isMemberDisabled;
    return this;
  }

  /**
   * Get isMemberDisabled
   * @return isMemberDisabled
   */
  @javax.annotation.Nullable
  public Boolean getIsMemberDisabled() {
    return isMemberDisabled;
  }

  public void setIsMemberDisabled(Boolean isMemberDisabled) {
    this.isMemberDisabled = isMemberDisabled;
  }


  public ProjectMemberDetails isTimesheetAllowed(Boolean isTimesheetAllowed) {
    this.isTimesheetAllowed = isTimesheetAllowed;
    return this;
  }

  /**
   * Get isTimesheetAllowed
   * @return isTimesheetAllowed
   */
  @javax.annotation.Nullable
  public Boolean getIsTimesheetAllowed() {
    return isTimesheetAllowed;
  }

  public void setIsTimesheetAllowed(Boolean isTimesheetAllowed) {
    this.isTimesheetAllowed = isTimesheetAllowed;
  }


  public ProjectMemberDetails isTimesheetApprovalRequired(Boolean isTimesheetApprovalRequired) {
    this.isTimesheetApprovalRequired = isTimesheetApprovalRequired;
    return this;
  }

  /**
   * Get isTimesheetApprovalRequired
   * @return isTimesheetApprovalRequired
   */
  @javax.annotation.Nullable
  public Boolean getIsTimesheetApprovalRequired() {
    return isTimesheetApprovalRequired;
  }

  public void setIsTimesheetApprovalRequired(Boolean isTimesheetApprovalRequired) {
    this.isTimesheetApprovalRequired = isTimesheetApprovalRequired;
  }


  public ProjectMemberDetails isTimesheetApprover(Boolean isTimesheetApprover) {
    this.isTimesheetApprover = isTimesheetApprover;
    return this;
  }

  /**
   * Get isTimesheetApprover
   * @return isTimesheetApprover
   */
  @javax.annotation.Nullable
  public Boolean getIsTimesheetApprover() {
    return isTimesheetApprover;
  }

  public void setIsTimesheetApprover(Boolean isTimesheetApprover) {
    this.isTimesheetApprover = isTimesheetApprover;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectMemberDetails projectMemberDetails = (ProjectMemberDetails) o;
    return Objects.equals(this.budgetAmount, projectMemberDetails.budgetAmount) &&
        Objects.equals(this.costAmount, projectMemberDetails.costAmount) &&
        Objects.equals(this.email, projectMemberDetails.email) &&
        Objects.equals(this.firstname, projectMemberDetails.firstname) &&
        Objects.equals(this.fullname, projectMemberDetails.fullname) &&
        Objects.equals(this.lastname, projectMemberDetails.lastname) &&
        Objects.equals(this.projectIDFK, projectMemberDetails.projectIDFK) &&
        Objects.equals(this.rateAmount, projectMemberDetails.rateAmount) &&
        Objects.equals(this.userIDFK, projectMemberDetails.userIDFK) &&
        Objects.equals(this.canCommentOnTasks, projectMemberDetails.canCommentOnTasks) &&
        Objects.equals(this.canCreateTasks, projectMemberDetails.canCreateTasks) &&
        Objects.equals(this.canDeleteTasks, projectMemberDetails.canDeleteTasks) &&
        Objects.equals(this.canUpdateTasks, projectMemberDetails.canUpdateTasks) &&
        Objects.equals(this.isMemberDisabled, projectMemberDetails.isMemberDisabled) &&
        Objects.equals(this.isTimesheetAllowed, projectMemberDetails.isTimesheetAllowed) &&
        Objects.equals(this.isTimesheetApprovalRequired, projectMemberDetails.isTimesheetApprovalRequired) &&
        Objects.equals(this.isTimesheetApprover, projectMemberDetails.isTimesheetApprover);
  }

  @Override
  public int hashCode() {
    return Objects.hash(budgetAmount, costAmount, email, firstname, fullname, lastname, projectIDFK, rateAmount, userIDFK, canCommentOnTasks, canCreateTasks, canDeleteTasks, canUpdateTasks, isMemberDisabled, isTimesheetAllowed, isTimesheetApprovalRequired, isTimesheetApprover);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectMemberDetails {\n");
    sb.append("    budgetAmount: ").append(toIndentedString(budgetAmount)).append("\n");
    sb.append("    costAmount: ").append(toIndentedString(costAmount)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    firstname: ").append(toIndentedString(firstname)).append("\n");
    sb.append("    fullname: ").append(toIndentedString(fullname)).append("\n");
    sb.append("    lastname: ").append(toIndentedString(lastname)).append("\n");
    sb.append("    projectIDFK: ").append(toIndentedString(projectIDFK)).append("\n");
    sb.append("    rateAmount: ").append(toIndentedString(rateAmount)).append("\n");
    sb.append("    userIDFK: ").append(toIndentedString(userIDFK)).append("\n");
    sb.append("    canCommentOnTasks: ").append(toIndentedString(canCommentOnTasks)).append("\n");
    sb.append("    canCreateTasks: ").append(toIndentedString(canCreateTasks)).append("\n");
    sb.append("    canDeleteTasks: ").append(toIndentedString(canDeleteTasks)).append("\n");
    sb.append("    canUpdateTasks: ").append(toIndentedString(canUpdateTasks)).append("\n");
    sb.append("    isMemberDisabled: ").append(toIndentedString(isMemberDisabled)).append("\n");
    sb.append("    isTimesheetAllowed: ").append(toIndentedString(isTimesheetAllowed)).append("\n");
    sb.append("    isTimesheetApprovalRequired: ").append(toIndentedString(isTimesheetApprovalRequired)).append("\n");
    sb.append("    isTimesheetApprover: ").append(toIndentedString(isTimesheetApprover)).append("\n");
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
    openapiFields.add("BudgetAmount");
    openapiFields.add("CostAmount");
    openapiFields.add("Email");
    openapiFields.add("Firstname");
    openapiFields.add("Fullname");
    openapiFields.add("Lastname");
    openapiFields.add("ProjectIDFK");
    openapiFields.add("RateAmount");
    openapiFields.add("UserIDFK");
    openapiFields.add("canCommentOnTasks");
    openapiFields.add("canCreateTasks");
    openapiFields.add("canDeleteTasks");
    openapiFields.add("canUpdateTasks");
    openapiFields.add("isMemberDisabled");
    openapiFields.add("isTimesheetAllowed");
    openapiFields.add("isTimesheetApprovalRequired");
    openapiFields.add("isTimesheetApprover");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectMemberDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectMemberDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectMemberDetails is not found in the empty JSON string", ProjectMemberDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectMemberDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectMemberDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Email") != null && !jsonObj.get("Email").isJsonNull()) && !jsonObj.get("Email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Email").toString()));
      }
      if ((jsonObj.get("Firstname") != null && !jsonObj.get("Firstname").isJsonNull()) && !jsonObj.get("Firstname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Firstname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Firstname").toString()));
      }
      if ((jsonObj.get("Fullname") != null && !jsonObj.get("Fullname").isJsonNull()) && !jsonObj.get("Fullname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Fullname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Fullname").toString()));
      }
      if ((jsonObj.get("Lastname") != null && !jsonObj.get("Lastname").isJsonNull()) && !jsonObj.get("Lastname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Lastname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Lastname").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectMemberDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectMemberDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectMemberDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectMemberDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectMemberDetails>() {
           @Override
           public void write(JsonWriter out, ProjectMemberDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectMemberDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectMemberDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectMemberDetails
   * @throws IOException if the JSON string is invalid with respect to ProjectMemberDetails
   */
  public static ProjectMemberDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectMemberDetails.class);
  }

  /**
   * Convert an instance of ProjectMemberDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

