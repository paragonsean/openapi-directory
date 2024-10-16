/*
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CustomFieldPersistVO;

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
 * Java type: com.noosh.domain.nooshapi.persist.po.ProjectPatchPO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectPatchPO {
  public static final String SERIALIZED_NAME_CLIENT_USER_ID = "client_user_id";
  @SerializedName(SERIALIZED_NAME_CLIENT_USER_ID)
  private Long clientUserId;

  public static final String SERIALIZED_NAME_CLIENT_WORKGROUP_ID = "client_workgroup_id";
  @SerializedName(SERIALIZED_NAME_CLIENT_WORKGROUP_ID)
  private Long clientWorkgroupId;

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_COMPLETION_DATE = "completion_date";
  @SerializedName(SERIALIZED_NAME_COMPLETION_DATE)
  private LocalDate completionDate;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<CustomFieldPersistVO> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEACTIVATION_REASON_ID = "deactivation_reason_id";
  @SerializedName(SERIALIZED_NAME_DEACTIVATION_REASON_ID)
  private Long deactivationReasonId;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_HOT = "is_hot";
  @SerializedName(SERIALIZED_NAME_IS_HOT)
  private Boolean isHot;

  public static final String SERIALIZED_NAME_PROJECT_CATEGORY_ID = "project_category_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_CATEGORY_ID)
  private Long projectCategoryId;

  public static final String SERIALIZED_NAME_PROJECT_DESCRIPTION = "project_description";
  @SerializedName(SERIALIZED_NAME_PROJECT_DESCRIPTION)
  private String projectDescription;

  public static final String SERIALIZED_NAME_PROJECT_NAME = "project_name";
  @SerializedName(SERIALIZED_NAME_PROJECT_NAME)
  private String projectName;

  public static final String SERIALIZED_NAME_PROJECT_NUMBER = "project_number";
  @SerializedName(SERIALIZED_NAME_PROJECT_NUMBER)
  private String projectNumber;

  public static final String SERIALIZED_NAME_PROJECT_STATUS_ID = "project_status_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_STATUS_ID)
  private Long projectStatusId;

  public ProjectPatchPO() {
  }

  public ProjectPatchPO clientUserId(Long clientUserId) {
    this.clientUserId = clientUserId;
    return this;
  }

  /**
   * 
   * @return clientUserId
   */
  @javax.annotation.Nullable
  public Long getClientUserId() {
    return clientUserId;
  }

  public void setClientUserId(Long clientUserId) {
    this.clientUserId = clientUserId;
  }


  public ProjectPatchPO clientWorkgroupId(Long clientWorkgroupId) {
    this.clientWorkgroupId = clientWorkgroupId;
    return this;
  }

  /**
   * 
   * @return clientWorkgroupId
   */
  @javax.annotation.Nullable
  public Long getClientWorkgroupId() {
    return clientWorkgroupId;
  }

  public void setClientWorkgroupId(Long clientWorkgroupId) {
    this.clientWorkgroupId = clientWorkgroupId;
  }


  public ProjectPatchPO comments(String comments) {
    this.comments = comments;
    return this;
  }

  /**
   * 
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }

  public void setComments(String comments) {
    this.comments = comments;
  }


  public ProjectPatchPO completionDate(LocalDate completionDate) {
    this.completionDate = completionDate;
    return this;
  }

  /**
   * 
   * @return completionDate
   */
  @javax.annotation.Nullable
  public LocalDate getCompletionDate() {
    return completionDate;
  }

  public void setCompletionDate(LocalDate completionDate) {
    this.completionDate = completionDate;
  }


  public ProjectPatchPO customFields(List<CustomFieldPersistVO> customFields) {
    this.customFields = customFields;
    return this;
  }

  public ProjectPatchPO addCustomFieldsItem(CustomFieldPersistVO customFieldsItem) {
    if (this.customFields == null) {
      this.customFields = new ArrayList<>();
    }
    this.customFields.add(customFieldsItem);
    return this;
  }

  /**
   * 
   * @return customFields
   */
  @javax.annotation.Nullable
  public List<CustomFieldPersistVO> getCustomFields() {
    return customFields;
  }

  public void setCustomFields(List<CustomFieldPersistVO> customFields) {
    this.customFields = customFields;
  }


  public ProjectPatchPO deactivationReasonId(Long deactivationReasonId) {
    this.deactivationReasonId = deactivationReasonId;
    return this;
  }

  /**
   * 
   * @return deactivationReasonId
   */
  @javax.annotation.Nullable
  public Long getDeactivationReasonId() {
    return deactivationReasonId;
  }

  public void setDeactivationReasonId(Long deactivationReasonId) {
    this.deactivationReasonId = deactivationReasonId;
  }


  public ProjectPatchPO isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * 
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public ProjectPatchPO isHot(Boolean isHot) {
    this.isHot = isHot;
    return this;
  }

  /**
   * 
   * @return isHot
   */
  @javax.annotation.Nullable
  public Boolean getIsHot() {
    return isHot;
  }

  public void setIsHot(Boolean isHot) {
    this.isHot = isHot;
  }


  public ProjectPatchPO projectCategoryId(Long projectCategoryId) {
    this.projectCategoryId = projectCategoryId;
    return this;
  }

  /**
   * 
   * @return projectCategoryId
   */
  @javax.annotation.Nullable
  public Long getProjectCategoryId() {
    return projectCategoryId;
  }

  public void setProjectCategoryId(Long projectCategoryId) {
    this.projectCategoryId = projectCategoryId;
  }


  public ProjectPatchPO projectDescription(String projectDescription) {
    this.projectDescription = projectDescription;
    return this;
  }

  /**
   * 
   * @return projectDescription
   */
  @javax.annotation.Nullable
  public String getProjectDescription() {
    return projectDescription;
  }

  public void setProjectDescription(String projectDescription) {
    this.projectDescription = projectDescription;
  }


  public ProjectPatchPO projectName(String projectName) {
    this.projectName = projectName;
    return this;
  }

  /**
   * 
   * @return projectName
   */
  @javax.annotation.Nullable
  public String getProjectName() {
    return projectName;
  }

  public void setProjectName(String projectName) {
    this.projectName = projectName;
  }


  public ProjectPatchPO projectNumber(String projectNumber) {
    this.projectNumber = projectNumber;
    return this;
  }

  /**
   * 
   * @return projectNumber
   */
  @javax.annotation.Nullable
  public String getProjectNumber() {
    return projectNumber;
  }

  public void setProjectNumber(String projectNumber) {
    this.projectNumber = projectNumber;
  }


  public ProjectPatchPO projectStatusId(Long projectStatusId) {
    this.projectStatusId = projectStatusId;
    return this;
  }

  /**
   * 
   * @return projectStatusId
   */
  @javax.annotation.Nullable
  public Long getProjectStatusId() {
    return projectStatusId;
  }

  public void setProjectStatusId(Long projectStatusId) {
    this.projectStatusId = projectStatusId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectPatchPO projectPatchPO = (ProjectPatchPO) o;
    return Objects.equals(this.clientUserId, projectPatchPO.clientUserId) &&
        Objects.equals(this.clientWorkgroupId, projectPatchPO.clientWorkgroupId) &&
        Objects.equals(this.comments, projectPatchPO.comments) &&
        Objects.equals(this.completionDate, projectPatchPO.completionDate) &&
        Objects.equals(this.customFields, projectPatchPO.customFields) &&
        Objects.equals(this.deactivationReasonId, projectPatchPO.deactivationReasonId) &&
        Objects.equals(this.isActive, projectPatchPO.isActive) &&
        Objects.equals(this.isHot, projectPatchPO.isHot) &&
        Objects.equals(this.projectCategoryId, projectPatchPO.projectCategoryId) &&
        Objects.equals(this.projectDescription, projectPatchPO.projectDescription) &&
        Objects.equals(this.projectName, projectPatchPO.projectName) &&
        Objects.equals(this.projectNumber, projectPatchPO.projectNumber) &&
        Objects.equals(this.projectStatusId, projectPatchPO.projectStatusId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(clientUserId, clientWorkgroupId, comments, completionDate, customFields, deactivationReasonId, isActive, isHot, projectCategoryId, projectDescription, projectName, projectNumber, projectStatusId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectPatchPO {\n");
    sb.append("    clientUserId: ").append(toIndentedString(clientUserId)).append("\n");
    sb.append("    clientWorkgroupId: ").append(toIndentedString(clientWorkgroupId)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    completionDate: ").append(toIndentedString(completionDate)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    deactivationReasonId: ").append(toIndentedString(deactivationReasonId)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isHot: ").append(toIndentedString(isHot)).append("\n");
    sb.append("    projectCategoryId: ").append(toIndentedString(projectCategoryId)).append("\n");
    sb.append("    projectDescription: ").append(toIndentedString(projectDescription)).append("\n");
    sb.append("    projectName: ").append(toIndentedString(projectName)).append("\n");
    sb.append("    projectNumber: ").append(toIndentedString(projectNumber)).append("\n");
    sb.append("    projectStatusId: ").append(toIndentedString(projectStatusId)).append("\n");
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
    openapiFields.add("client_user_id");
    openapiFields.add("client_workgroup_id");
    openapiFields.add("comments");
    openapiFields.add("completion_date");
    openapiFields.add("custom_fields");
    openapiFields.add("deactivation_reason_id");
    openapiFields.add("is_active");
    openapiFields.add("is_hot");
    openapiFields.add("project_category_id");
    openapiFields.add("project_description");
    openapiFields.add("project_name");
    openapiFields.add("project_number");
    openapiFields.add("project_status_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectPatchPO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectPatchPO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectPatchPO is not found in the empty JSON string", ProjectPatchPO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectPatchPO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectPatchPO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if (jsonObj.get("custom_fields") != null && !jsonObj.get("custom_fields").isJsonNull()) {
        JsonArray jsonArraycustomFields = jsonObj.getAsJsonArray("custom_fields");
        if (jsonArraycustomFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_fields` to be an array in the JSON string but got `%s`", jsonObj.get("custom_fields").toString()));
          }

          // validate the optional field `custom_fields` (array)
          for (int i = 0; i < jsonArraycustomFields.size(); i++) {
            CustomFieldPersistVO.validateJsonElement(jsonArraycustomFields.get(i));
          };
        }
      }
      if ((jsonObj.get("project_description") != null && !jsonObj.get("project_description").isJsonNull()) && !jsonObj.get("project_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_description").toString()));
      }
      if ((jsonObj.get("project_name") != null && !jsonObj.get("project_name").isJsonNull()) && !jsonObj.get("project_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_name").toString()));
      }
      if ((jsonObj.get("project_number") != null && !jsonObj.get("project_number").isJsonNull()) && !jsonObj.get("project_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_number").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectPatchPO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectPatchPO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectPatchPO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectPatchPO.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectPatchPO>() {
           @Override
           public void write(JsonWriter out, ProjectPatchPO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectPatchPO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectPatchPO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectPatchPO
   * @throws IOException if the JSON string is invalid with respect to ProjectPatchPO
   */
  public static ProjectPatchPO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectPatchPO.class);
  }

  /**
   * Convert an instance of ProjectPatchPO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

