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
 * FixedAmountDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FixedAmountDetails {
  public static final String SERIALIZED_NAME_AMOUNT = "Amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_DATE_CREATED = "DateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_UPDATED = "DateUpdated";
  @SerializedName(SERIALIZED_NAME_DATE_UPDATED)
  private OffsetDateTime dateUpdated;

  public static final String SERIALIZED_NAME_FIXED_AMOUNT_I_D = "FixedAmountID";
  @SerializedName(SERIALIZED_NAME_FIXED_AMOUNT_I_D)
  private Integer fixedAmountID;

  public static final String SERIALIZED_NAME_INVENTORY_ITEM_I_D_F_K = "InventoryItemIDFK";
  @SerializedName(SERIALIZED_NAME_INVENTORY_ITEM_I_D_F_K)
  private Long inventoryItemIDFK;

  public static final String SERIALIZED_NAME_INVENTORY_ITEM_NAME = "InventoryItemName";
  @SerializedName(SERIALIZED_NAME_INVENTORY_ITEM_NAME)
  private String inventoryItemName;

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

  public static final String SERIALIZED_NAME_TASK_I_D_F_K = "TaskIDFK";
  @SerializedName(SERIALIZED_NAME_TASK_I_D_F_K)
  private Integer taskIDFK;

  public static final String SERIALIZED_NAME_TASK_TITLE = "TaskTitle";
  @SerializedName(SERIALIZED_NAME_TASK_TITLE)
  private String taskTitle;

  public static final String SERIALIZED_NAME_UPDATED_BY_USER_I_D_F_K = "UpdatedByUserIDFK";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY_USER_I_D_F_K)
  private Integer updatedByUserIDFK;

  public static final String SERIALIZED_NAME_IS_INVOICED = "isInvoiced";
  @SerializedName(SERIALIZED_NAME_IS_INVOICED)
  private Boolean isInvoiced;

  public FixedAmountDetails() {
  }

  public FixedAmountDetails amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public FixedAmountDetails dateCreated(OffsetDateTime dateCreated) {
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


  public FixedAmountDetails dateUpdated(OffsetDateTime dateUpdated) {
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


  public FixedAmountDetails fixedAmountID(Integer fixedAmountID) {
    this.fixedAmountID = fixedAmountID;
    return this;
  }

  /**
   * Get fixedAmountID
   * @return fixedAmountID
   */
  @javax.annotation.Nullable
  public Integer getFixedAmountID() {
    return fixedAmountID;
  }

  public void setFixedAmountID(Integer fixedAmountID) {
    this.fixedAmountID = fixedAmountID;
  }


  public FixedAmountDetails inventoryItemIDFK(Long inventoryItemIDFK) {
    this.inventoryItemIDFK = inventoryItemIDFK;
    return this;
  }

  /**
   * Get inventoryItemIDFK
   * @return inventoryItemIDFK
   */
  @javax.annotation.Nullable
  public Long getInventoryItemIDFK() {
    return inventoryItemIDFK;
  }

  public void setInventoryItemIDFK(Long inventoryItemIDFK) {
    this.inventoryItemIDFK = inventoryItemIDFK;
  }


  public FixedAmountDetails inventoryItemName(String inventoryItemName) {
    this.inventoryItemName = inventoryItemName;
    return this;
  }

  /**
   * Get inventoryItemName
   * @return inventoryItemName
   */
  @javax.annotation.Nullable
  public String getInventoryItemName() {
    return inventoryItemName;
  }

  public void setInventoryItemName(String inventoryItemName) {
    this.inventoryItemName = inventoryItemName;
  }


  public FixedAmountDetails notes(String notes) {
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


  public FixedAmountDetails projectCode(String projectCode) {
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


  public FixedAmountDetails projectIDFK(Integer projectIDFK) {
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


  public FixedAmountDetails projectTitle(String projectTitle) {
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


  public FixedAmountDetails taskIDFK(Integer taskIDFK) {
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


  public FixedAmountDetails taskTitle(String taskTitle) {
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


  public FixedAmountDetails updatedByUserIDFK(Integer updatedByUserIDFK) {
    this.updatedByUserIDFK = updatedByUserIDFK;
    return this;
  }

  /**
   * Get updatedByUserIDFK
   * @return updatedByUserIDFK
   */
  @javax.annotation.Nullable
  public Integer getUpdatedByUserIDFK() {
    return updatedByUserIDFK;
  }

  public void setUpdatedByUserIDFK(Integer updatedByUserIDFK) {
    this.updatedByUserIDFK = updatedByUserIDFK;
  }


  public FixedAmountDetails isInvoiced(Boolean isInvoiced) {
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
    FixedAmountDetails fixedAmountDetails = (FixedAmountDetails) o;
    return Objects.equals(this.amount, fixedAmountDetails.amount) &&
        Objects.equals(this.dateCreated, fixedAmountDetails.dateCreated) &&
        Objects.equals(this.dateUpdated, fixedAmountDetails.dateUpdated) &&
        Objects.equals(this.fixedAmountID, fixedAmountDetails.fixedAmountID) &&
        Objects.equals(this.inventoryItemIDFK, fixedAmountDetails.inventoryItemIDFK) &&
        Objects.equals(this.inventoryItemName, fixedAmountDetails.inventoryItemName) &&
        Objects.equals(this.notes, fixedAmountDetails.notes) &&
        Objects.equals(this.projectCode, fixedAmountDetails.projectCode) &&
        Objects.equals(this.projectIDFK, fixedAmountDetails.projectIDFK) &&
        Objects.equals(this.projectTitle, fixedAmountDetails.projectTitle) &&
        Objects.equals(this.taskIDFK, fixedAmountDetails.taskIDFK) &&
        Objects.equals(this.taskTitle, fixedAmountDetails.taskTitle) &&
        Objects.equals(this.updatedByUserIDFK, fixedAmountDetails.updatedByUserIDFK) &&
        Objects.equals(this.isInvoiced, fixedAmountDetails.isInvoiced);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, dateCreated, dateUpdated, fixedAmountID, inventoryItemIDFK, inventoryItemName, notes, projectCode, projectIDFK, projectTitle, taskIDFK, taskTitle, updatedByUserIDFK, isInvoiced);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FixedAmountDetails {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateUpdated: ").append(toIndentedString(dateUpdated)).append("\n");
    sb.append("    fixedAmountID: ").append(toIndentedString(fixedAmountID)).append("\n");
    sb.append("    inventoryItemIDFK: ").append(toIndentedString(inventoryItemIDFK)).append("\n");
    sb.append("    inventoryItemName: ").append(toIndentedString(inventoryItemName)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    projectCode: ").append(toIndentedString(projectCode)).append("\n");
    sb.append("    projectIDFK: ").append(toIndentedString(projectIDFK)).append("\n");
    sb.append("    projectTitle: ").append(toIndentedString(projectTitle)).append("\n");
    sb.append("    taskIDFK: ").append(toIndentedString(taskIDFK)).append("\n");
    sb.append("    taskTitle: ").append(toIndentedString(taskTitle)).append("\n");
    sb.append("    updatedByUserIDFK: ").append(toIndentedString(updatedByUserIDFK)).append("\n");
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
    openapiFields.add("Amount");
    openapiFields.add("DateCreated");
    openapiFields.add("DateUpdated");
    openapiFields.add("FixedAmountID");
    openapiFields.add("InventoryItemIDFK");
    openapiFields.add("InventoryItemName");
    openapiFields.add("Notes");
    openapiFields.add("ProjectCode");
    openapiFields.add("ProjectIDFK");
    openapiFields.add("ProjectTitle");
    openapiFields.add("TaskIDFK");
    openapiFields.add("TaskTitle");
    openapiFields.add("UpdatedByUserIDFK");
    openapiFields.add("isInvoiced");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FixedAmountDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FixedAmountDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FixedAmountDetails is not found in the empty JSON string", FixedAmountDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FixedAmountDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FixedAmountDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("InventoryItemName") != null && !jsonObj.get("InventoryItemName").isJsonNull()) && !jsonObj.get("InventoryItemName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `InventoryItemName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("InventoryItemName").toString()));
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
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FixedAmountDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FixedAmountDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FixedAmountDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FixedAmountDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<FixedAmountDetails>() {
           @Override
           public void write(JsonWriter out, FixedAmountDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FixedAmountDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FixedAmountDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FixedAmountDetails
   * @throws IOException if the JSON string is invalid with respect to FixedAmountDetails
   */
  public static FixedAmountDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FixedAmountDetails.class);
  }

  /**
   * Convert an instance of FixedAmountDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

