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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ProjectMemberDetails;
import org.openapitools.client.model.ProjectSectionDetails;
import org.openapitools.client.model.ProjectTagItem;

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
 * ProjectDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectDetails {
  public static final String SERIALIZED_NAME_BUDGET_AMOUNT = "BudgetAmount";
  @SerializedName(SERIALIZED_NAME_BUDGET_AMOUNT)
  private Double budgetAmount;

  public static final String SERIALIZED_NAME_BUDGET_HOURS = "BudgetHours";
  @SerializedName(SERIALIZED_NAME_BUDGET_HOURS)
  private Double budgetHours;

  public static final String SERIALIZED_NAME_COMPANY_I_D_F_K = "CompanyIDFK";
  @SerializedName(SERIALIZED_NAME_COMPANY_I_D_F_K)
  private Integer companyIDFK;

  public static final String SERIALIZED_NAME_COMPANY_NAME = "CompanyName";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  public static final String SERIALIZED_NAME_DATE_CREATED = "DateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_UPDATED = "DateUpdated";
  @SerializedName(SERIALIZED_NAME_DATE_UPDATED)
  private OffsetDateTime dateUpdated;

  public static final String SERIALIZED_NAME_DEFAULT_ACCOUNT_TASK_TYPE_I_D_F_K = "DefaultAccountTaskTypeIDFK";
  @SerializedName(SERIALIZED_NAME_DEFAULT_ACCOUNT_TASK_TYPE_I_D_F_K)
  private Integer defaultAccountTaskTypeIDFK;

  public static final String SERIALIZED_NAME_DEFAULT_ACCOUNT_TASK_TYPE_NAME = "DefaultAccountTaskTypeName";
  @SerializedName(SERIALIZED_NAME_DEFAULT_ACCOUNT_TASK_TYPE_NAME)
  private String defaultAccountTaskTypeName;

  public static final String SERIALIZED_NAME_END_DATE = "EndDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private OffsetDateTime endDate;

  public static final String SERIALIZED_NAME_MEMBERS = "Members";
  @SerializedName(SERIALIZED_NAME_MEMBERS)
  private List<ProjectMemberDetails> members = new ArrayList<>();

  public static final String SERIALIZED_NAME_NOTES = "Notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PROJECT_BILLABLE_TYPE_CODE = "ProjectBillableTypeCode";
  @SerializedName(SERIALIZED_NAME_PROJECT_BILLABLE_TYPE_CODE)
  private String projectBillableTypeCode;

  public static final String SERIALIZED_NAME_PROJECT_BUDGET_TYPE_CODE = "ProjectBudgetTypeCode";
  @SerializedName(SERIALIZED_NAME_PROJECT_BUDGET_TYPE_CODE)
  private String projectBudgetTypeCode;

  public static final String SERIALIZED_NAME_PROJECT_CATEGORY_COLOR = "ProjectCategoryColor";
  @SerializedName(SERIALIZED_NAME_PROJECT_CATEGORY_COLOR)
  private String projectCategoryColor;

  public static final String SERIALIZED_NAME_PROJECT_CATEGORY_I_D_F_K = "ProjectCategoryIDFK";
  @SerializedName(SERIALIZED_NAME_PROJECT_CATEGORY_I_D_F_K)
  private Integer projectCategoryIDFK;

  public static final String SERIALIZED_NAME_PROJECT_CATEGORY_NAME = "ProjectCategoryName";
  @SerializedName(SERIALIZED_NAME_PROJECT_CATEGORY_NAME)
  private String projectCategoryName;

  public static final String SERIALIZED_NAME_PROJECT_CODE = "ProjectCode";
  @SerializedName(SERIALIZED_NAME_PROJECT_CODE)
  private String projectCode;

  public static final String SERIALIZED_NAME_PROJECT_HOURLY_RATE = "ProjectHourlyRate";
  @SerializedName(SERIALIZED_NAME_PROJECT_HOURLY_RATE)
  private Double projectHourlyRate;

  public static final String SERIALIZED_NAME_PROJECT_I_D = "ProjectID";
  @SerializedName(SERIALIZED_NAME_PROJECT_I_D)
  private Integer projectID;

  public static final String SERIALIZED_NAME_PROJECT_OWNER_USER_I_D_F_K = "ProjectOwnerUserIDFK";
  @SerializedName(SERIALIZED_NAME_PROJECT_OWNER_USER_I_D_F_K)
  private Integer projectOwnerUserIDFK;

  public static final String SERIALIZED_NAME_PROJECT_STATUS_CODE = "ProjectStatusCode";
  @SerializedName(SERIALIZED_NAME_PROJECT_STATUS_CODE)
  private String projectStatusCode;

  public static final String SERIALIZED_NAME_PROJECT_TAGS = "ProjectTags";
  @SerializedName(SERIALIZED_NAME_PROJECT_TAGS)
  private List<ProjectTagItem> projectTags = new ArrayList<>();

  public static final String SERIALIZED_NAME_SECTIONS = "Sections";
  @SerializedName(SERIALIZED_NAME_SECTIONS)
  private List<ProjectSectionDetails> sections = new ArrayList<>();

  public static final String SERIALIZED_NAME_START_DATE = "StartDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_IS_ARCHIVED = "isArchived";
  @SerializedName(SERIALIZED_NAME_IS_ARCHIVED)
  private Boolean isArchived;

  public static final String SERIALIZED_NAME_IS_TASK_REQUIRED_ON_TIMESHEET = "isTaskRequiredOnTimesheet";
  @SerializedName(SERIALIZED_NAME_IS_TASK_REQUIRED_ON_TIMESHEET)
  private Boolean isTaskRequiredOnTimesheet;

  public ProjectDetails() {
  }

  public ProjectDetails budgetAmount(Double budgetAmount) {
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


  public ProjectDetails budgetHours(Double budgetHours) {
    this.budgetHours = budgetHours;
    return this;
  }

  /**
   * Get budgetHours
   * @return budgetHours
   */
  @javax.annotation.Nullable
  public Double getBudgetHours() {
    return budgetHours;
  }

  public void setBudgetHours(Double budgetHours) {
    this.budgetHours = budgetHours;
  }


  public ProjectDetails companyIDFK(Integer companyIDFK) {
    this.companyIDFK = companyIDFK;
    return this;
  }

  /**
   * Get companyIDFK
   * @return companyIDFK
   */
  @javax.annotation.Nullable
  public Integer getCompanyIDFK() {
    return companyIDFK;
  }

  public void setCompanyIDFK(Integer companyIDFK) {
    this.companyIDFK = companyIDFK;
  }


  public ProjectDetails companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * Get companyName
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  public ProjectDetails dateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
    return this;
  }

  /**
   * Get dateCreated
   * @return dateCreated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateCreated() {
    return dateCreated;
  }

  public void setDateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
  }


  public ProjectDetails dateUpdated(OffsetDateTime dateUpdated) {
    this.dateUpdated = dateUpdated;
    return this;
  }

  /**
   * Get dateUpdated
   * @return dateUpdated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateUpdated() {
    return dateUpdated;
  }

  public void setDateUpdated(OffsetDateTime dateUpdated) {
    this.dateUpdated = dateUpdated;
  }


  public ProjectDetails defaultAccountTaskTypeIDFK(Integer defaultAccountTaskTypeIDFK) {
    this.defaultAccountTaskTypeIDFK = defaultAccountTaskTypeIDFK;
    return this;
  }

  /**
   * Get defaultAccountTaskTypeIDFK
   * @return defaultAccountTaskTypeIDFK
   */
  @javax.annotation.Nullable
  public Integer getDefaultAccountTaskTypeIDFK() {
    return defaultAccountTaskTypeIDFK;
  }

  public void setDefaultAccountTaskTypeIDFK(Integer defaultAccountTaskTypeIDFK) {
    this.defaultAccountTaskTypeIDFK = defaultAccountTaskTypeIDFK;
  }


  public ProjectDetails defaultAccountTaskTypeName(String defaultAccountTaskTypeName) {
    this.defaultAccountTaskTypeName = defaultAccountTaskTypeName;
    return this;
  }

  /**
   * Get defaultAccountTaskTypeName
   * @return defaultAccountTaskTypeName
   */
  @javax.annotation.Nullable
  public String getDefaultAccountTaskTypeName() {
    return defaultAccountTaskTypeName;
  }

  public void setDefaultAccountTaskTypeName(String defaultAccountTaskTypeName) {
    this.defaultAccountTaskTypeName = defaultAccountTaskTypeName;
  }


  public ProjectDetails endDate(OffsetDateTime endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndDate() {
    return endDate;
  }

  public void setEndDate(OffsetDateTime endDate) {
    this.endDate = endDate;
  }


  public ProjectDetails members(List<ProjectMemberDetails> members) {
    this.members = members;
    return this;
  }

  public ProjectDetails addMembersItem(ProjectMemberDetails membersItem) {
    if (this.members == null) {
      this.members = new ArrayList<>();
    }
    this.members.add(membersItem);
    return this;
  }

  /**
   * Get members
   * @return members
   */
  @javax.annotation.Nullable
  public List<ProjectMemberDetails> getMembers() {
    return members;
  }

  public void setMembers(List<ProjectMemberDetails> members) {
    this.members = members;
  }


  public ProjectDetails notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Get notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public ProjectDetails projectBillableTypeCode(String projectBillableTypeCode) {
    this.projectBillableTypeCode = projectBillableTypeCode;
    return this;
  }

  /**
   * Possible values: CategoryHourly, NoRate, NotBillable, PersonHourly, ProjectHourly
   * @return projectBillableTypeCode
   */
  @javax.annotation.Nullable
  public String getProjectBillableTypeCode() {
    return projectBillableTypeCode;
  }

  public void setProjectBillableTypeCode(String projectBillableTypeCode) {
    this.projectBillableTypeCode = projectBillableTypeCode;
  }


  public ProjectDetails projectBudgetTypeCode(String projectBudgetTypeCode) {
    this.projectBudgetTypeCode = projectBudgetTypeCode;
    return this;
  }

  /**
   * Possible Values: CategoryHours, NoBudget, PersonHours, ProjectFees, ProjectHours
   * @return projectBudgetTypeCode
   */
  @javax.annotation.Nullable
  public String getProjectBudgetTypeCode() {
    return projectBudgetTypeCode;
  }

  public void setProjectBudgetTypeCode(String projectBudgetTypeCode) {
    this.projectBudgetTypeCode = projectBudgetTypeCode;
  }


  public ProjectDetails projectCategoryColor(String projectCategoryColor) {
    this.projectCategoryColor = projectCategoryColor;
    return this;
  }

  /**
   * Html Hex Color Code starting with #
   * @return projectCategoryColor
   */
  @javax.annotation.Nullable
  public String getProjectCategoryColor() {
    return projectCategoryColor;
  }

  public void setProjectCategoryColor(String projectCategoryColor) {
    this.projectCategoryColor = projectCategoryColor;
  }


  public ProjectDetails projectCategoryIDFK(Integer projectCategoryIDFK) {
    this.projectCategoryIDFK = projectCategoryIDFK;
    return this;
  }

  /**
   * Get projectCategoryIDFK
   * @return projectCategoryIDFK
   */
  @javax.annotation.Nullable
  public Integer getProjectCategoryIDFK() {
    return projectCategoryIDFK;
  }

  public void setProjectCategoryIDFK(Integer projectCategoryIDFK) {
    this.projectCategoryIDFK = projectCategoryIDFK;
  }


  public ProjectDetails projectCategoryName(String projectCategoryName) {
    this.projectCategoryName = projectCategoryName;
    return this;
  }

  /**
   * Get projectCategoryName
   * @return projectCategoryName
   */
  @javax.annotation.Nullable
  public String getProjectCategoryName() {
    return projectCategoryName;
  }

  public void setProjectCategoryName(String projectCategoryName) {
    this.projectCategoryName = projectCategoryName;
  }


  public ProjectDetails projectCode(String projectCode) {
    this.projectCode = projectCode;
    return this;
  }

  /**
   * Get projectCode
   * @return projectCode
   */
  @javax.annotation.Nullable
  public String getProjectCode() {
    return projectCode;
  }

  public void setProjectCode(String projectCode) {
    this.projectCode = projectCode;
  }


  public ProjectDetails projectHourlyRate(Double projectHourlyRate) {
    this.projectHourlyRate = projectHourlyRate;
    return this;
  }

  /**
   * Get projectHourlyRate
   * @return projectHourlyRate
   */
  @javax.annotation.Nullable
  public Double getProjectHourlyRate() {
    return projectHourlyRate;
  }

  public void setProjectHourlyRate(Double projectHourlyRate) {
    this.projectHourlyRate = projectHourlyRate;
  }


  public ProjectDetails projectID(Integer projectID) {
    this.projectID = projectID;
    return this;
  }

  /**
   * Get projectID
   * @return projectID
   */
  @javax.annotation.Nullable
  public Integer getProjectID() {
    return projectID;
  }

  public void setProjectID(Integer projectID) {
    this.projectID = projectID;
  }


  public ProjectDetails projectOwnerUserIDFK(Integer projectOwnerUserIDFK) {
    this.projectOwnerUserIDFK = projectOwnerUserIDFK;
    return this;
  }

  /**
   * Get projectOwnerUserIDFK
   * @return projectOwnerUserIDFK
   */
  @javax.annotation.Nullable
  public Integer getProjectOwnerUserIDFK() {
    return projectOwnerUserIDFK;
  }

  public void setProjectOwnerUserIDFK(Integer projectOwnerUserIDFK) {
    this.projectOwnerUserIDFK = projectOwnerUserIDFK;
  }


  public ProjectDetails projectStatusCode(String projectStatusCode) {
    this.projectStatusCode = projectStatusCode;
    return this;
  }

  /**
   * Possible values: NotStarted, InProgress, Complete
   * @return projectStatusCode
   */
  @javax.annotation.Nullable
  public String getProjectStatusCode() {
    return projectStatusCode;
  }

  public void setProjectStatusCode(String projectStatusCode) {
    this.projectStatusCode = projectStatusCode;
  }


  public ProjectDetails projectTags(List<ProjectTagItem> projectTags) {
    this.projectTags = projectTags;
    return this;
  }

  public ProjectDetails addProjectTagsItem(ProjectTagItem projectTagsItem) {
    if (this.projectTags == null) {
      this.projectTags = new ArrayList<>();
    }
    this.projectTags.add(projectTagsItem);
    return this;
  }

  /**
   * Get projectTags
   * @return projectTags
   */
  @javax.annotation.Nullable
  public List<ProjectTagItem> getProjectTags() {
    return projectTags;
  }

  public void setProjectTags(List<ProjectTagItem> projectTags) {
    this.projectTags = projectTags;
  }


  public ProjectDetails sections(List<ProjectSectionDetails> sections) {
    this.sections = sections;
    return this;
  }

  public ProjectDetails addSectionsItem(ProjectSectionDetails sectionsItem) {
    if (this.sections == null) {
      this.sections = new ArrayList<>();
    }
    this.sections.add(sectionsItem);
    return this;
  }

  /**
   * Get sections
   * @return sections
   */
  @javax.annotation.Nullable
  public List<ProjectSectionDetails> getSections() {
    return sections;
  }

  public void setSections(List<ProjectSectionDetails> sections) {
    this.sections = sections;
  }


  public ProjectDetails startDate(OffsetDateTime startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartDate() {
    return startDate;
  }

  public void setStartDate(OffsetDateTime startDate) {
    this.startDate = startDate;
  }


  public ProjectDetails title(String title) {
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


  public ProjectDetails isArchived(Boolean isArchived) {
    this.isArchived = isArchived;
    return this;
  }

  /**
   * Get isArchived
   * @return isArchived
   */
  @javax.annotation.Nullable
  public Boolean getIsArchived() {
    return isArchived;
  }

  public void setIsArchived(Boolean isArchived) {
    this.isArchived = isArchived;
  }


  public ProjectDetails isTaskRequiredOnTimesheet(Boolean isTaskRequiredOnTimesheet) {
    this.isTaskRequiredOnTimesheet = isTaskRequiredOnTimesheet;
    return this;
  }

  /**
   * Get isTaskRequiredOnTimesheet
   * @return isTaskRequiredOnTimesheet
   */
  @javax.annotation.Nullable
  public Boolean getIsTaskRequiredOnTimesheet() {
    return isTaskRequiredOnTimesheet;
  }

  public void setIsTaskRequiredOnTimesheet(Boolean isTaskRequiredOnTimesheet) {
    this.isTaskRequiredOnTimesheet = isTaskRequiredOnTimesheet;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectDetails projectDetails = (ProjectDetails) o;
    return Objects.equals(this.budgetAmount, projectDetails.budgetAmount) &&
        Objects.equals(this.budgetHours, projectDetails.budgetHours) &&
        Objects.equals(this.companyIDFK, projectDetails.companyIDFK) &&
        Objects.equals(this.companyName, projectDetails.companyName) &&
        Objects.equals(this.dateCreated, projectDetails.dateCreated) &&
        Objects.equals(this.dateUpdated, projectDetails.dateUpdated) &&
        Objects.equals(this.defaultAccountTaskTypeIDFK, projectDetails.defaultAccountTaskTypeIDFK) &&
        Objects.equals(this.defaultAccountTaskTypeName, projectDetails.defaultAccountTaskTypeName) &&
        Objects.equals(this.endDate, projectDetails.endDate) &&
        Objects.equals(this.members, projectDetails.members) &&
        Objects.equals(this.notes, projectDetails.notes) &&
        Objects.equals(this.projectBillableTypeCode, projectDetails.projectBillableTypeCode) &&
        Objects.equals(this.projectBudgetTypeCode, projectDetails.projectBudgetTypeCode) &&
        Objects.equals(this.projectCategoryColor, projectDetails.projectCategoryColor) &&
        Objects.equals(this.projectCategoryIDFK, projectDetails.projectCategoryIDFK) &&
        Objects.equals(this.projectCategoryName, projectDetails.projectCategoryName) &&
        Objects.equals(this.projectCode, projectDetails.projectCode) &&
        Objects.equals(this.projectHourlyRate, projectDetails.projectHourlyRate) &&
        Objects.equals(this.projectID, projectDetails.projectID) &&
        Objects.equals(this.projectOwnerUserIDFK, projectDetails.projectOwnerUserIDFK) &&
        Objects.equals(this.projectStatusCode, projectDetails.projectStatusCode) &&
        Objects.equals(this.projectTags, projectDetails.projectTags) &&
        Objects.equals(this.sections, projectDetails.sections) &&
        Objects.equals(this.startDate, projectDetails.startDate) &&
        Objects.equals(this.title, projectDetails.title) &&
        Objects.equals(this.isArchived, projectDetails.isArchived) &&
        Objects.equals(this.isTaskRequiredOnTimesheet, projectDetails.isTaskRequiredOnTimesheet);
  }

  @Override
  public int hashCode() {
    return Objects.hash(budgetAmount, budgetHours, companyIDFK, companyName, dateCreated, dateUpdated, defaultAccountTaskTypeIDFK, defaultAccountTaskTypeName, endDate, members, notes, projectBillableTypeCode, projectBudgetTypeCode, projectCategoryColor, projectCategoryIDFK, projectCategoryName, projectCode, projectHourlyRate, projectID, projectOwnerUserIDFK, projectStatusCode, projectTags, sections, startDate, title, isArchived, isTaskRequiredOnTimesheet);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectDetails {\n");
    sb.append("    budgetAmount: ").append(toIndentedString(budgetAmount)).append("\n");
    sb.append("    budgetHours: ").append(toIndentedString(budgetHours)).append("\n");
    sb.append("    companyIDFK: ").append(toIndentedString(companyIDFK)).append("\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateUpdated: ").append(toIndentedString(dateUpdated)).append("\n");
    sb.append("    defaultAccountTaskTypeIDFK: ").append(toIndentedString(defaultAccountTaskTypeIDFK)).append("\n");
    sb.append("    defaultAccountTaskTypeName: ").append(toIndentedString(defaultAccountTaskTypeName)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    members: ").append(toIndentedString(members)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    projectBillableTypeCode: ").append(toIndentedString(projectBillableTypeCode)).append("\n");
    sb.append("    projectBudgetTypeCode: ").append(toIndentedString(projectBudgetTypeCode)).append("\n");
    sb.append("    projectCategoryColor: ").append(toIndentedString(projectCategoryColor)).append("\n");
    sb.append("    projectCategoryIDFK: ").append(toIndentedString(projectCategoryIDFK)).append("\n");
    sb.append("    projectCategoryName: ").append(toIndentedString(projectCategoryName)).append("\n");
    sb.append("    projectCode: ").append(toIndentedString(projectCode)).append("\n");
    sb.append("    projectHourlyRate: ").append(toIndentedString(projectHourlyRate)).append("\n");
    sb.append("    projectID: ").append(toIndentedString(projectID)).append("\n");
    sb.append("    projectOwnerUserIDFK: ").append(toIndentedString(projectOwnerUserIDFK)).append("\n");
    sb.append("    projectStatusCode: ").append(toIndentedString(projectStatusCode)).append("\n");
    sb.append("    projectTags: ").append(toIndentedString(projectTags)).append("\n");
    sb.append("    sections: ").append(toIndentedString(sections)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    isArchived: ").append(toIndentedString(isArchived)).append("\n");
    sb.append("    isTaskRequiredOnTimesheet: ").append(toIndentedString(isTaskRequiredOnTimesheet)).append("\n");
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
    openapiFields.add("BudgetHours");
    openapiFields.add("CompanyIDFK");
    openapiFields.add("CompanyName");
    openapiFields.add("DateCreated");
    openapiFields.add("DateUpdated");
    openapiFields.add("DefaultAccountTaskTypeIDFK");
    openapiFields.add("DefaultAccountTaskTypeName");
    openapiFields.add("EndDate");
    openapiFields.add("Members");
    openapiFields.add("Notes");
    openapiFields.add("ProjectBillableTypeCode");
    openapiFields.add("ProjectBudgetTypeCode");
    openapiFields.add("ProjectCategoryColor");
    openapiFields.add("ProjectCategoryIDFK");
    openapiFields.add("ProjectCategoryName");
    openapiFields.add("ProjectCode");
    openapiFields.add("ProjectHourlyRate");
    openapiFields.add("ProjectID");
    openapiFields.add("ProjectOwnerUserIDFK");
    openapiFields.add("ProjectStatusCode");
    openapiFields.add("ProjectTags");
    openapiFields.add("Sections");
    openapiFields.add("StartDate");
    openapiFields.add("Title");
    openapiFields.add("isArchived");
    openapiFields.add("isTaskRequiredOnTimesheet");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectDetails is not found in the empty JSON string", ProjectDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("CompanyName") != null && !jsonObj.get("CompanyName").isJsonNull()) && !jsonObj.get("CompanyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyName").toString()));
      }
      if ((jsonObj.get("DefaultAccountTaskTypeName") != null && !jsonObj.get("DefaultAccountTaskTypeName").isJsonNull()) && !jsonObj.get("DefaultAccountTaskTypeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DefaultAccountTaskTypeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DefaultAccountTaskTypeName").toString()));
      }
      if (jsonObj.get("Members") != null && !jsonObj.get("Members").isJsonNull()) {
        JsonArray jsonArraymembers = jsonObj.getAsJsonArray("Members");
        if (jsonArraymembers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Members").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Members` to be an array in the JSON string but got `%s`", jsonObj.get("Members").toString()));
          }

          // validate the optional field `Members` (array)
          for (int i = 0; i < jsonArraymembers.size(); i++) {
            ProjectMemberDetails.validateJsonElement(jsonArraymembers.get(i));
          };
        }
      }
      if ((jsonObj.get("Notes") != null && !jsonObj.get("Notes").isJsonNull()) && !jsonObj.get("Notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Notes").toString()));
      }
      if ((jsonObj.get("ProjectBillableTypeCode") != null && !jsonObj.get("ProjectBillableTypeCode").isJsonNull()) && !jsonObj.get("ProjectBillableTypeCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectBillableTypeCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectBillableTypeCode").toString()));
      }
      if ((jsonObj.get("ProjectBudgetTypeCode") != null && !jsonObj.get("ProjectBudgetTypeCode").isJsonNull()) && !jsonObj.get("ProjectBudgetTypeCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectBudgetTypeCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectBudgetTypeCode").toString()));
      }
      if ((jsonObj.get("ProjectCategoryColor") != null && !jsonObj.get("ProjectCategoryColor").isJsonNull()) && !jsonObj.get("ProjectCategoryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectCategoryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectCategoryColor").toString()));
      }
      if ((jsonObj.get("ProjectCategoryName") != null && !jsonObj.get("ProjectCategoryName").isJsonNull()) && !jsonObj.get("ProjectCategoryName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectCategoryName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectCategoryName").toString()));
      }
      if ((jsonObj.get("ProjectCode") != null && !jsonObj.get("ProjectCode").isJsonNull()) && !jsonObj.get("ProjectCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectCode").toString()));
      }
      if ((jsonObj.get("ProjectStatusCode") != null && !jsonObj.get("ProjectStatusCode").isJsonNull()) && !jsonObj.get("ProjectStatusCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectStatusCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectStatusCode").toString()));
      }
      if (jsonObj.get("ProjectTags") != null && !jsonObj.get("ProjectTags").isJsonNull()) {
        JsonArray jsonArrayprojectTags = jsonObj.getAsJsonArray("ProjectTags");
        if (jsonArrayprojectTags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("ProjectTags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `ProjectTags` to be an array in the JSON string but got `%s`", jsonObj.get("ProjectTags").toString()));
          }

          // validate the optional field `ProjectTags` (array)
          for (int i = 0; i < jsonArrayprojectTags.size(); i++) {
            ProjectTagItem.validateJsonElement(jsonArrayprojectTags.get(i));
          };
        }
      }
      if (jsonObj.get("Sections") != null && !jsonObj.get("Sections").isJsonNull()) {
        JsonArray jsonArraysections = jsonObj.getAsJsonArray("Sections");
        if (jsonArraysections != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Sections").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Sections` to be an array in the JSON string but got `%s`", jsonObj.get("Sections").toString()));
          }

          // validate the optional field `Sections` (array)
          for (int i = 0; i < jsonArraysections.size(); i++) {
            ProjectSectionDetails.validateJsonElement(jsonArraysections.get(i));
          };
        }
      }
      if ((jsonObj.get("Title") != null && !jsonObj.get("Title").isJsonNull()) && !jsonObj.get("Title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectDetails>() {
           @Override
           public void write(JsonWriter out, ProjectDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectDetails
   * @throws IOException if the JSON string is invalid with respect to ProjectDetails
   */
  public static ProjectDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectDetails.class);
  }

  /**
   * Convert an instance of ProjectDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

