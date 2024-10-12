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
 * TimesheetDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TimesheetDetails {
  public static final String SERIALIZED_NAME_APPROVED_BY = "ApprovedBy";
  @SerializedName(SERIALIZED_NAME_APPROVED_BY)
  private String approvedBy;

  public static final String SERIALIZED_NAME_CATEGORY_NAME = "CategoryName";
  @SerializedName(SERIALIZED_NAME_CATEGORY_NAME)
  private String categoryName;

  public static final String SERIALIZED_NAME_CUSTOM_METADATA = "CustomMetadata";
  @SerializedName(SERIALIZED_NAME_CUSTOM_METADATA)
  private String customMetadata;

  public static final String SERIALIZED_NAME_CUSTOMER_I_D_F_K = "CustomerIDFK";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_I_D_F_K)
  private Integer customerIDFK;

  public static final String SERIALIZED_NAME_CUSTOMER_NAME = "CustomerName";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_NAME)
  private String customerName;

  public static final String SERIALIZED_NAME_DATE_APPROVED = "DateApproved";
  @SerializedName(SERIALIZED_NAME_DATE_APPROVED)
  private OffsetDateTime dateApproved;

  public static final String SERIALIZED_NAME_DATE_CREATED = "DateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_UPDATED = "DateUpdated";
  @SerializedName(SERIALIZED_NAME_DATE_UPDATED)
  private OffsetDateTime dateUpdated;

  public static final String SERIALIZED_NAME_DURATION = "Duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private Double duration;

  public static final String SERIALIZED_NAME_EMAIL = "Email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_END_TIME_LOCAL = "EndTimeLocal";
  @SerializedName(SERIALIZED_NAME_END_TIME_LOCAL)
  private OffsetDateTime endTimeLocal;

  public static final String SERIALIZED_NAME_END_TIME_U_T_C = "EndTimeUTC";
  @SerializedName(SERIALIZED_NAME_END_TIME_U_T_C)
  private OffsetDateTime endTimeUTC;

  public static final String SERIALIZED_NAME_ENTRY_DATE = "EntryDate";
  @SerializedName(SERIALIZED_NAME_ENTRY_DATE)
  private OffsetDateTime entryDate;

  public static final String SERIALIZED_NAME_FIRSTNAME = "Firstname";
  @SerializedName(SERIALIZED_NAME_FIRSTNAME)
  private String firstname;

  public static final String SERIALIZED_NAME_HAS_TIMER = "HasTimer";
  @SerializedName(SERIALIZED_NAME_HAS_TIMER)
  private Boolean hasTimer;

  public static final String SERIALIZED_NAME_INVOICE_I_D_F_K = "InvoiceIDFK";
  @SerializedName(SERIALIZED_NAME_INVOICE_I_D_F_K)
  private Long invoiceIDFK;

  public static final String SERIALIZED_NAME_INVOICE_LINE_ITEM_I_D_F_K = "InvoiceLineItemIDFK";
  @SerializedName(SERIALIZED_NAME_INVOICE_LINE_ITEM_I_D_F_K)
  private Long invoiceLineItemIDFK;

  public static final String SERIALIZED_NAME_LASTNAME = "Lastname";
  @SerializedName(SERIALIZED_NAME_LASTNAME)
  private String lastname;

  public static final String SERIALIZED_NAME_NOTES = "Notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PROJECT_CODE = "ProjectCode";
  @SerializedName(SERIALIZED_NAME_PROJECT_CODE)
  private String projectCode;

  public static final String SERIALIZED_NAME_PROJECT_I_D_F_K = "ProjectIDFK";
  @SerializedName(SERIALIZED_NAME_PROJECT_I_D_F_K)
  private Integer projectIDFK;

  public static final String SERIALIZED_NAME_PROJECT_TITLE = "ProjectTitle";
  @SerializedName(SERIALIZED_NAME_PROJECT_TITLE)
  private String projectTitle;

  public static final String SERIALIZED_NAME_START_TIME_LOCAL = "StartTimeLocal";
  @SerializedName(SERIALIZED_NAME_START_TIME_LOCAL)
  private OffsetDateTime startTimeLocal;

  public static final String SERIALIZED_NAME_START_TIME_U_T_C = "StartTimeUTC";
  @SerializedName(SERIALIZED_NAME_START_TIME_U_T_C)
  private OffsetDateTime startTimeUTC;

  public static final String SERIALIZED_NAME_TASK_I_D_F_K = "TaskIDFK";
  @SerializedName(SERIALIZED_NAME_TASK_I_D_F_K)
  private Integer taskIDFK;

  public static final String SERIALIZED_NAME_TASK_TITLE = "TaskTitle";
  @SerializedName(SERIALIZED_NAME_TASK_TITLE)
  private String taskTitle;

  public static final String SERIALIZED_NAME_TIMER_STARTED_AT_U_T_C = "TimerStartedAtUTC";
  @SerializedName(SERIALIZED_NAME_TIMER_STARTED_AT_U_T_C)
  private OffsetDateTime timerStartedAtUTC;

  public static final String SERIALIZED_NAME_TIMESHEET_CATEGORY_I_D_F_K = "TimesheetCategoryIDFK";
  @SerializedName(SERIALIZED_NAME_TIMESHEET_CATEGORY_I_D_F_K)
  private Integer timesheetCategoryIDFK;

  public static final String SERIALIZED_NAME_TIMESHEET_ENTRY_APPROVAL_STATUS_CODE = "TimesheetEntryApprovalStatusCode";
  @SerializedName(SERIALIZED_NAME_TIMESHEET_ENTRY_APPROVAL_STATUS_CODE)
  private String timesheetEntryApprovalStatusCode;

  public static final String SERIALIZED_NAME_TIMESHEET_ENTRY_I_D = "TimesheetEntryID";
  @SerializedName(SERIALIZED_NAME_TIMESHEET_ENTRY_I_D)
  private Long timesheetEntryID;

  public static final String SERIALIZED_NAME_TIMESHEET_USER_TIME_ZONE = "TimesheetUserTimeZone";
  @SerializedName(SERIALIZED_NAME_TIMESHEET_USER_TIME_ZONE)
  private String timesheetUserTimeZone;

  public static final String SERIALIZED_NAME_USER_I_D_F_K = "UserIDFK";
  @SerializedName(SERIALIZED_NAME_USER_I_D_F_K)
  private Integer userIDFK;

  public static final String SERIALIZED_NAME_IS_BILLABLE = "isBillable";
  @SerializedName(SERIALIZED_NAME_IS_BILLABLE)
  private Boolean isBillable;

  public static final String SERIALIZED_NAME_IS_INVOICED = "isInvoiced";
  @SerializedName(SERIALIZED_NAME_IS_INVOICED)
  private Boolean isInvoiced;

  public TimesheetDetails() {
  }

  public TimesheetDetails approvedBy(String approvedBy) {
    this.approvedBy = approvedBy;
    return this;
  }

  /**
   * Get approvedBy
   * @return approvedBy
   */
  @javax.annotation.Nullable
  public String getApprovedBy() {
    return approvedBy;
  }

  public void setApprovedBy(String approvedBy) {
    this.approvedBy = approvedBy;
  }


  public TimesheetDetails categoryName(String categoryName) {
    this.categoryName = categoryName;
    return this;
  }

  /**
   * Get categoryName
   * @return categoryName
   */
  @javax.annotation.Nullable
  public String getCategoryName() {
    return categoryName;
  }

  public void setCategoryName(String categoryName) {
    this.categoryName = categoryName;
  }


  public TimesheetDetails customMetadata(String customMetadata) {
    this.customMetadata = customMetadata;
    return this;
  }

  /**
   * Get customMetadata
   * @return customMetadata
   */
  @javax.annotation.Nullable
  public String getCustomMetadata() {
    return customMetadata;
  }

  public void setCustomMetadata(String customMetadata) {
    this.customMetadata = customMetadata;
  }


  public TimesheetDetails customerIDFK(Integer customerIDFK) {
    this.customerIDFK = customerIDFK;
    return this;
  }

  /**
   * Get customerIDFK
   * @return customerIDFK
   */
  @javax.annotation.Nullable
  public Integer getCustomerIDFK() {
    return customerIDFK;
  }

  public void setCustomerIDFK(Integer customerIDFK) {
    this.customerIDFK = customerIDFK;
  }


  public TimesheetDetails customerName(String customerName) {
    this.customerName = customerName;
    return this;
  }

  /**
   * Get customerName
   * @return customerName
   */
  @javax.annotation.Nullable
  public String getCustomerName() {
    return customerName;
  }

  public void setCustomerName(String customerName) {
    this.customerName = customerName;
  }


  public TimesheetDetails dateApproved(OffsetDateTime dateApproved) {
    this.dateApproved = dateApproved;
    return this;
  }

  /**
   * Get dateApproved
   * @return dateApproved
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateApproved() {
    return dateApproved;
  }

  public void setDateApproved(OffsetDateTime dateApproved) {
    this.dateApproved = dateApproved;
  }


  public TimesheetDetails dateCreated(OffsetDateTime dateCreated) {
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


  public TimesheetDetails dateUpdated(OffsetDateTime dateUpdated) {
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


  public TimesheetDetails duration(Double duration) {
    this.duration = duration;
    return this;
  }

  /**
   * Get duration
   * @return duration
   */
  @javax.annotation.Nullable
  public Double getDuration() {
    return duration;
  }

  public void setDuration(Double duration) {
    this.duration = duration;
  }


  public TimesheetDetails email(String email) {
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


  public TimesheetDetails endTimeLocal(OffsetDateTime endTimeLocal) {
    this.endTimeLocal = endTimeLocal;
    return this;
  }

  /**
   * Get endTimeLocal
   * @return endTimeLocal
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndTimeLocal() {
    return endTimeLocal;
  }

  public void setEndTimeLocal(OffsetDateTime endTimeLocal) {
    this.endTimeLocal = endTimeLocal;
  }


  public TimesheetDetails endTimeUTC(OffsetDateTime endTimeUTC) {
    this.endTimeUTC = endTimeUTC;
    return this;
  }

  /**
   * Get endTimeUTC
   * @return endTimeUTC
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndTimeUTC() {
    return endTimeUTC;
  }

  public void setEndTimeUTC(OffsetDateTime endTimeUTC) {
    this.endTimeUTC = endTimeUTC;
  }


  public TimesheetDetails entryDate(OffsetDateTime entryDate) {
    this.entryDate = entryDate;
    return this;
  }

  /**
   * Get entryDate
   * @return entryDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEntryDate() {
    return entryDate;
  }

  public void setEntryDate(OffsetDateTime entryDate) {
    this.entryDate = entryDate;
  }


  public TimesheetDetails firstname(String firstname) {
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


  public TimesheetDetails hasTimer(Boolean hasTimer) {
    this.hasTimer = hasTimer;
    return this;
  }

  /**
   * Get hasTimer
   * @return hasTimer
   */
  @javax.annotation.Nullable
  public Boolean getHasTimer() {
    return hasTimer;
  }

  public void setHasTimer(Boolean hasTimer) {
    this.hasTimer = hasTimer;
  }


  public TimesheetDetails invoiceIDFK(Long invoiceIDFK) {
    this.invoiceIDFK = invoiceIDFK;
    return this;
  }

  /**
   * Get invoiceIDFK
   * @return invoiceIDFK
   */
  @javax.annotation.Nullable
  public Long getInvoiceIDFK() {
    return invoiceIDFK;
  }

  public void setInvoiceIDFK(Long invoiceIDFK) {
    this.invoiceIDFK = invoiceIDFK;
  }


  public TimesheetDetails invoiceLineItemIDFK(Long invoiceLineItemIDFK) {
    this.invoiceLineItemIDFK = invoiceLineItemIDFK;
    return this;
  }

  /**
   * Get invoiceLineItemIDFK
   * @return invoiceLineItemIDFK
   */
  @javax.annotation.Nullable
  public Long getInvoiceLineItemIDFK() {
    return invoiceLineItemIDFK;
  }

  public void setInvoiceLineItemIDFK(Long invoiceLineItemIDFK) {
    this.invoiceLineItemIDFK = invoiceLineItemIDFK;
  }


  public TimesheetDetails lastname(String lastname) {
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


  public TimesheetDetails notes(String notes) {
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


  public TimesheetDetails projectCode(String projectCode) {
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


  public TimesheetDetails projectIDFK(Integer projectIDFK) {
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


  public TimesheetDetails projectTitle(String projectTitle) {
    this.projectTitle = projectTitle;
    return this;
  }

  /**
   * Get projectTitle
   * @return projectTitle
   */
  @javax.annotation.Nullable
  public String getProjectTitle() {
    return projectTitle;
  }

  public void setProjectTitle(String projectTitle) {
    this.projectTitle = projectTitle;
  }


  public TimesheetDetails startTimeLocal(OffsetDateTime startTimeLocal) {
    this.startTimeLocal = startTimeLocal;
    return this;
  }

  /**
   * Get startTimeLocal
   * @return startTimeLocal
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartTimeLocal() {
    return startTimeLocal;
  }

  public void setStartTimeLocal(OffsetDateTime startTimeLocal) {
    this.startTimeLocal = startTimeLocal;
  }


  public TimesheetDetails startTimeUTC(OffsetDateTime startTimeUTC) {
    this.startTimeUTC = startTimeUTC;
    return this;
  }

  /**
   * Get startTimeUTC
   * @return startTimeUTC
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartTimeUTC() {
    return startTimeUTC;
  }

  public void setStartTimeUTC(OffsetDateTime startTimeUTC) {
    this.startTimeUTC = startTimeUTC;
  }


  public TimesheetDetails taskIDFK(Integer taskIDFK) {
    this.taskIDFK = taskIDFK;
    return this;
  }

  /**
   * Get taskIDFK
   * @return taskIDFK
   */
  @javax.annotation.Nullable
  public Integer getTaskIDFK() {
    return taskIDFK;
  }

  public void setTaskIDFK(Integer taskIDFK) {
    this.taskIDFK = taskIDFK;
  }


  public TimesheetDetails taskTitle(String taskTitle) {
    this.taskTitle = taskTitle;
    return this;
  }

  /**
   * Get taskTitle
   * @return taskTitle
   */
  @javax.annotation.Nullable
  public String getTaskTitle() {
    return taskTitle;
  }

  public void setTaskTitle(String taskTitle) {
    this.taskTitle = taskTitle;
  }


  public TimesheetDetails timerStartedAtUTC(OffsetDateTime timerStartedAtUTC) {
    this.timerStartedAtUTC = timerStartedAtUTC;
    return this;
  }

  /**
   * Get timerStartedAtUTC
   * @return timerStartedAtUTC
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTimerStartedAtUTC() {
    return timerStartedAtUTC;
  }

  public void setTimerStartedAtUTC(OffsetDateTime timerStartedAtUTC) {
    this.timerStartedAtUTC = timerStartedAtUTC;
  }


  public TimesheetDetails timesheetCategoryIDFK(Integer timesheetCategoryIDFK) {
    this.timesheetCategoryIDFK = timesheetCategoryIDFK;
    return this;
  }

  /**
   * Get timesheetCategoryIDFK
   * @return timesheetCategoryIDFK
   */
  @javax.annotation.Nullable
  public Integer getTimesheetCategoryIDFK() {
    return timesheetCategoryIDFK;
  }

  public void setTimesheetCategoryIDFK(Integer timesheetCategoryIDFK) {
    this.timesheetCategoryIDFK = timesheetCategoryIDFK;
  }


  public TimesheetDetails timesheetEntryApprovalStatusCode(String timesheetEntryApprovalStatusCode) {
    this.timesheetEntryApprovalStatusCode = timesheetEntryApprovalStatusCode;
    return this;
  }

  /**
   * Get timesheetEntryApprovalStatusCode
   * @return timesheetEntryApprovalStatusCode
   */
  @javax.annotation.Nullable
  public String getTimesheetEntryApprovalStatusCode() {
    return timesheetEntryApprovalStatusCode;
  }

  public void setTimesheetEntryApprovalStatusCode(String timesheetEntryApprovalStatusCode) {
    this.timesheetEntryApprovalStatusCode = timesheetEntryApprovalStatusCode;
  }


  public TimesheetDetails timesheetEntryID(Long timesheetEntryID) {
    this.timesheetEntryID = timesheetEntryID;
    return this;
  }

  /**
   * Get timesheetEntryID
   * @return timesheetEntryID
   */
  @javax.annotation.Nullable
  public Long getTimesheetEntryID() {
    return timesheetEntryID;
  }

  public void setTimesheetEntryID(Long timesheetEntryID) {
    this.timesheetEntryID = timesheetEntryID;
  }


  public TimesheetDetails timesheetUserTimeZone(String timesheetUserTimeZone) {
    this.timesheetUserTimeZone = timesheetUserTimeZone;
    return this;
  }

  /**
   * Get timesheetUserTimeZone
   * @return timesheetUserTimeZone
   */
  @javax.annotation.Nullable
  public String getTimesheetUserTimeZone() {
    return timesheetUserTimeZone;
  }

  public void setTimesheetUserTimeZone(String timesheetUserTimeZone) {
    this.timesheetUserTimeZone = timesheetUserTimeZone;
  }


  public TimesheetDetails userIDFK(Integer userIDFK) {
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


  public TimesheetDetails isBillable(Boolean isBillable) {
    this.isBillable = isBillable;
    return this;
  }

  /**
   * Get isBillable
   * @return isBillable
   */
  @javax.annotation.Nullable
  public Boolean getIsBillable() {
    return isBillable;
  }

  public void setIsBillable(Boolean isBillable) {
    this.isBillable = isBillable;
  }


  public TimesheetDetails isInvoiced(Boolean isInvoiced) {
    this.isInvoiced = isInvoiced;
    return this;
  }

  /**
   * Get isInvoiced
   * @return isInvoiced
   */
  @javax.annotation.Nullable
  public Boolean getIsInvoiced() {
    return isInvoiced;
  }

  public void setIsInvoiced(Boolean isInvoiced) {
    this.isInvoiced = isInvoiced;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TimesheetDetails timesheetDetails = (TimesheetDetails) o;
    return Objects.equals(this.approvedBy, timesheetDetails.approvedBy) &&
        Objects.equals(this.categoryName, timesheetDetails.categoryName) &&
        Objects.equals(this.customMetadata, timesheetDetails.customMetadata) &&
        Objects.equals(this.customerIDFK, timesheetDetails.customerIDFK) &&
        Objects.equals(this.customerName, timesheetDetails.customerName) &&
        Objects.equals(this.dateApproved, timesheetDetails.dateApproved) &&
        Objects.equals(this.dateCreated, timesheetDetails.dateCreated) &&
        Objects.equals(this.dateUpdated, timesheetDetails.dateUpdated) &&
        Objects.equals(this.duration, timesheetDetails.duration) &&
        Objects.equals(this.email, timesheetDetails.email) &&
        Objects.equals(this.endTimeLocal, timesheetDetails.endTimeLocal) &&
        Objects.equals(this.endTimeUTC, timesheetDetails.endTimeUTC) &&
        Objects.equals(this.entryDate, timesheetDetails.entryDate) &&
        Objects.equals(this.firstname, timesheetDetails.firstname) &&
        Objects.equals(this.hasTimer, timesheetDetails.hasTimer) &&
        Objects.equals(this.invoiceIDFK, timesheetDetails.invoiceIDFK) &&
        Objects.equals(this.invoiceLineItemIDFK, timesheetDetails.invoiceLineItemIDFK) &&
        Objects.equals(this.lastname, timesheetDetails.lastname) &&
        Objects.equals(this.notes, timesheetDetails.notes) &&
        Objects.equals(this.projectCode, timesheetDetails.projectCode) &&
        Objects.equals(this.projectIDFK, timesheetDetails.projectIDFK) &&
        Objects.equals(this.projectTitle, timesheetDetails.projectTitle) &&
        Objects.equals(this.startTimeLocal, timesheetDetails.startTimeLocal) &&
        Objects.equals(this.startTimeUTC, timesheetDetails.startTimeUTC) &&
        Objects.equals(this.taskIDFK, timesheetDetails.taskIDFK) &&
        Objects.equals(this.taskTitle, timesheetDetails.taskTitle) &&
        Objects.equals(this.timerStartedAtUTC, timesheetDetails.timerStartedAtUTC) &&
        Objects.equals(this.timesheetCategoryIDFK, timesheetDetails.timesheetCategoryIDFK) &&
        Objects.equals(this.timesheetEntryApprovalStatusCode, timesheetDetails.timesheetEntryApprovalStatusCode) &&
        Objects.equals(this.timesheetEntryID, timesheetDetails.timesheetEntryID) &&
        Objects.equals(this.timesheetUserTimeZone, timesheetDetails.timesheetUserTimeZone) &&
        Objects.equals(this.userIDFK, timesheetDetails.userIDFK) &&
        Objects.equals(this.isBillable, timesheetDetails.isBillable) &&
        Objects.equals(this.isInvoiced, timesheetDetails.isInvoiced);
  }

  @Override
  public int hashCode() {
    return Objects.hash(approvedBy, categoryName, customMetadata, customerIDFK, customerName, dateApproved, dateCreated, dateUpdated, duration, email, endTimeLocal, endTimeUTC, entryDate, firstname, hasTimer, invoiceIDFK, invoiceLineItemIDFK, lastname, notes, projectCode, projectIDFK, projectTitle, startTimeLocal, startTimeUTC, taskIDFK, taskTitle, timerStartedAtUTC, timesheetCategoryIDFK, timesheetEntryApprovalStatusCode, timesheetEntryID, timesheetUserTimeZone, userIDFK, isBillable, isInvoiced);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TimesheetDetails {\n");
    sb.append("    approvedBy: ").append(toIndentedString(approvedBy)).append("\n");
    sb.append("    categoryName: ").append(toIndentedString(categoryName)).append("\n");
    sb.append("    customMetadata: ").append(toIndentedString(customMetadata)).append("\n");
    sb.append("    customerIDFK: ").append(toIndentedString(customerIDFK)).append("\n");
    sb.append("    customerName: ").append(toIndentedString(customerName)).append("\n");
    sb.append("    dateApproved: ").append(toIndentedString(dateApproved)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateUpdated: ").append(toIndentedString(dateUpdated)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    endTimeLocal: ").append(toIndentedString(endTimeLocal)).append("\n");
    sb.append("    endTimeUTC: ").append(toIndentedString(endTimeUTC)).append("\n");
    sb.append("    entryDate: ").append(toIndentedString(entryDate)).append("\n");
    sb.append("    firstname: ").append(toIndentedString(firstname)).append("\n");
    sb.append("    hasTimer: ").append(toIndentedString(hasTimer)).append("\n");
    sb.append("    invoiceIDFK: ").append(toIndentedString(invoiceIDFK)).append("\n");
    sb.append("    invoiceLineItemIDFK: ").append(toIndentedString(invoiceLineItemIDFK)).append("\n");
    sb.append("    lastname: ").append(toIndentedString(lastname)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    projectCode: ").append(toIndentedString(projectCode)).append("\n");
    sb.append("    projectIDFK: ").append(toIndentedString(projectIDFK)).append("\n");
    sb.append("    projectTitle: ").append(toIndentedString(projectTitle)).append("\n");
    sb.append("    startTimeLocal: ").append(toIndentedString(startTimeLocal)).append("\n");
    sb.append("    startTimeUTC: ").append(toIndentedString(startTimeUTC)).append("\n");
    sb.append("    taskIDFK: ").append(toIndentedString(taskIDFK)).append("\n");
    sb.append("    taskTitle: ").append(toIndentedString(taskTitle)).append("\n");
    sb.append("    timerStartedAtUTC: ").append(toIndentedString(timerStartedAtUTC)).append("\n");
    sb.append("    timesheetCategoryIDFK: ").append(toIndentedString(timesheetCategoryIDFK)).append("\n");
    sb.append("    timesheetEntryApprovalStatusCode: ").append(toIndentedString(timesheetEntryApprovalStatusCode)).append("\n");
    sb.append("    timesheetEntryID: ").append(toIndentedString(timesheetEntryID)).append("\n");
    sb.append("    timesheetUserTimeZone: ").append(toIndentedString(timesheetUserTimeZone)).append("\n");
    sb.append("    userIDFK: ").append(toIndentedString(userIDFK)).append("\n");
    sb.append("    isBillable: ").append(toIndentedString(isBillable)).append("\n");
    sb.append("    isInvoiced: ").append(toIndentedString(isInvoiced)).append("\n");
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
    openapiFields.add("ApprovedBy");
    openapiFields.add("CategoryName");
    openapiFields.add("CustomMetadata");
    openapiFields.add("CustomerIDFK");
    openapiFields.add("CustomerName");
    openapiFields.add("DateApproved");
    openapiFields.add("DateCreated");
    openapiFields.add("DateUpdated");
    openapiFields.add("Duration");
    openapiFields.add("Email");
    openapiFields.add("EndTimeLocal");
    openapiFields.add("EndTimeUTC");
    openapiFields.add("EntryDate");
    openapiFields.add("Firstname");
    openapiFields.add("HasTimer");
    openapiFields.add("InvoiceIDFK");
    openapiFields.add("InvoiceLineItemIDFK");
    openapiFields.add("Lastname");
    openapiFields.add("Notes");
    openapiFields.add("ProjectCode");
    openapiFields.add("ProjectIDFK");
    openapiFields.add("ProjectTitle");
    openapiFields.add("StartTimeLocal");
    openapiFields.add("StartTimeUTC");
    openapiFields.add("TaskIDFK");
    openapiFields.add("TaskTitle");
    openapiFields.add("TimerStartedAtUTC");
    openapiFields.add("TimesheetCategoryIDFK");
    openapiFields.add("TimesheetEntryApprovalStatusCode");
    openapiFields.add("TimesheetEntryID");
    openapiFields.add("TimesheetUserTimeZone");
    openapiFields.add("UserIDFK");
    openapiFields.add("isBillable");
    openapiFields.add("isInvoiced");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TimesheetDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TimesheetDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TimesheetDetails is not found in the empty JSON string", TimesheetDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TimesheetDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TimesheetDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ApprovedBy") != null && !jsonObj.get("ApprovedBy").isJsonNull()) && !jsonObj.get("ApprovedBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ApprovedBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ApprovedBy").toString()));
      }
      if ((jsonObj.get("CategoryName") != null && !jsonObj.get("CategoryName").isJsonNull()) && !jsonObj.get("CategoryName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CategoryName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CategoryName").toString()));
      }
      if ((jsonObj.get("CustomMetadata") != null && !jsonObj.get("CustomMetadata").isJsonNull()) && !jsonObj.get("CustomMetadata").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CustomMetadata` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CustomMetadata").toString()));
      }
      if ((jsonObj.get("CustomerName") != null && !jsonObj.get("CustomerName").isJsonNull()) && !jsonObj.get("CustomerName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CustomerName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CustomerName").toString()));
      }
      if ((jsonObj.get("Email") != null && !jsonObj.get("Email").isJsonNull()) && !jsonObj.get("Email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Email").toString()));
      }
      if ((jsonObj.get("Firstname") != null && !jsonObj.get("Firstname").isJsonNull()) && !jsonObj.get("Firstname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Firstname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Firstname").toString()));
      }
      if ((jsonObj.get("Lastname") != null && !jsonObj.get("Lastname").isJsonNull()) && !jsonObj.get("Lastname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Lastname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Lastname").toString()));
      }
      if ((jsonObj.get("Notes") != null && !jsonObj.get("Notes").isJsonNull()) && !jsonObj.get("Notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Notes").toString()));
      }
      if ((jsonObj.get("ProjectCode") != null && !jsonObj.get("ProjectCode").isJsonNull()) && !jsonObj.get("ProjectCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectCode").toString()));
      }
      if ((jsonObj.get("ProjectTitle") != null && !jsonObj.get("ProjectTitle").isJsonNull()) && !jsonObj.get("ProjectTitle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectTitle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectTitle").toString()));
      }
      if ((jsonObj.get("TaskTitle") != null && !jsonObj.get("TaskTitle").isJsonNull()) && !jsonObj.get("TaskTitle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaskTitle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaskTitle").toString()));
      }
      if ((jsonObj.get("TimesheetEntryApprovalStatusCode") != null && !jsonObj.get("TimesheetEntryApprovalStatusCode").isJsonNull()) && !jsonObj.get("TimesheetEntryApprovalStatusCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TimesheetEntryApprovalStatusCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TimesheetEntryApprovalStatusCode").toString()));
      }
      if ((jsonObj.get("TimesheetUserTimeZone") != null && !jsonObj.get("TimesheetUserTimeZone").isJsonNull()) && !jsonObj.get("TimesheetUserTimeZone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TimesheetUserTimeZone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TimesheetUserTimeZone").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TimesheetDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TimesheetDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TimesheetDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TimesheetDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<TimesheetDetails>() {
           @Override
           public void write(JsonWriter out, TimesheetDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TimesheetDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TimesheetDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TimesheetDetails
   * @throws IOException if the JSON string is invalid with respect to TimesheetDetails
   */
  public static TimesheetDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TimesheetDetails.class);
  }

  /**
   * Convert an instance of TimesheetDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

