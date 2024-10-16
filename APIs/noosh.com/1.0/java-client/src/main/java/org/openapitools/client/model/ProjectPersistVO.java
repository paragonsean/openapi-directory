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
 * Java type: com.noosh.domain.nooshapi.persist.vo.ProjectPersistVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectPersistVO {
  public static final String SERIALIZED_NAME_CLIENT_ACCOUNT = "client_account";
  @SerializedName(SERIALIZED_NAME_CLIENT_ACCOUNT)
  private String clientAccount;

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

  public static final String SERIALIZED_NAME_IS_PAPER_DIRECT = "is_paper_direct";
  @SerializedName(SERIALIZED_NAME_IS_PAPER_DIRECT)
  private Boolean isPaperDirect;

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

  public static final String SERIALIZED_NAME_PROJECT_OWNER_USER_ID = "project_owner_user_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_OWNER_USER_ID)
  private Long projectOwnerUserId;

  public static final String SERIALIZED_NAME_PROJECT_STATUS_ID = "project_status_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_STATUS_ID)
  private Long projectStatusId;

  public ProjectPersistVO() {
  }

  public ProjectPersistVO clientAccount(String clientAccount) {
    this.clientAccount = clientAccount;
    return this;
  }

  /**
   * 
   * @return clientAccount
   */
  @javax.annotation.Nullable
  public String getClientAccount() {
    return clientAccount;
  }

  public void setClientAccount(String clientAccount) {
    this.clientAccount = clientAccount;
  }


  public ProjectPersistVO clientUserId(Long clientUserId) {
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


  public ProjectPersistVO clientWorkgroupId(Long clientWorkgroupId) {
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


  public ProjectPersistVO comments(String comments) {
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


  public ProjectPersistVO completionDate(LocalDate completionDate) {
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


  public ProjectPersistVO customFields(List<CustomFieldPersistVO> customFields) {
    this.customFields = customFields;
    return this;
  }

  public ProjectPersistVO addCustomFieldsItem(CustomFieldPersistVO customFieldsItem) {
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


  public ProjectPersistVO deactivationReasonId(Long deactivationReasonId) {
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


  public ProjectPersistVO isActive(Boolean isActive) {
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


  public ProjectPersistVO isHot(Boolean isHot) {
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


  public ProjectPersistVO isPaperDirect(Boolean isPaperDirect) {
    this.isPaperDirect = isPaperDirect;
    return this;
  }

  /**
   * 
   * @return isPaperDirect
   */
  @javax.annotation.Nullable
  public Boolean getIsPaperDirect() {
    return isPaperDirect;
  }

  public void setIsPaperDirect(Boolean isPaperDirect) {
    this.isPaperDirect = isPaperDirect;
  }


  public ProjectPersistVO projectCategoryId(Long projectCategoryId) {
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


  public ProjectPersistVO projectDescription(String projectDescription) {
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


  public ProjectPersistVO projectName(String projectName) {
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


  public ProjectPersistVO projectNumber(String projectNumber) {
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


  public ProjectPersistVO projectOwnerUserId(Long projectOwnerUserId) {
    this.projectOwnerUserId = projectOwnerUserId;
    return this;
  }

  /**
   * 
   * @return projectOwnerUserId
   */
  @javax.annotation.Nullable
  public Long getProjectOwnerUserId() {
    return projectOwnerUserId;
  }

  public void setProjectOwnerUserId(Long projectOwnerUserId) {
    this.projectOwnerUserId = projectOwnerUserId;
  }


  public ProjectPersistVO projectStatusId(Long projectStatusId) {
    this.projectStatusId = projectStatusId;
    return this;
  }

  /**
   * 
   * @return projectStatusId
   */
  @javax.annotation.Nonnull
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
    ProjectPersistVO projectPersistVO = (ProjectPersistVO) o;
    return Objects.equals(this.clientAccount, projectPersistVO.clientAccount) &&
        Objects.equals(this.clientUserId, projectPersistVO.clientUserId) &&
        Objects.equals(this.clientWorkgroupId, projectPersistVO.clientWorkgroupId) &&
        Objects.equals(this.comments, projectPersistVO.comments) &&
        Objects.equals(this.completionDate, projectPersistVO.completionDate) &&
        Objects.equals(this.customFields, projectPersistVO.customFields) &&
        Objects.equals(this.deactivationReasonId, projectPersistVO.deactivationReasonId) &&
        Objects.equals(this.isActive, projectPersistVO.isActive) &&
        Objects.equals(this.isHot, projectPersistVO.isHot) &&
        Objects.equals(this.isPaperDirect, projectPersistVO.isPaperDirect) &&
        Objects.equals(this.projectCategoryId, projectPersistVO.projectCategoryId) &&
        Objects.equals(this.projectDescription, projectPersistVO.projectDescription) &&
        Objects.equals(this.projectName, projectPersistVO.projectName) &&
        Objects.equals(this.projectNumber, projectPersistVO.projectNumber) &&
        Objects.equals(this.projectOwnerUserId, projectPersistVO.projectOwnerUserId) &&
        Objects.equals(this.projectStatusId, projectPersistVO.projectStatusId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(clientAccount, clientUserId, clientWorkgroupId, comments, completionDate, customFields, deactivationReasonId, isActive, isHot, isPaperDirect, projectCategoryId, projectDescription, projectName, projectNumber, projectOwnerUserId, projectStatusId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectPersistVO {\n");
    sb.append("    clientAccount: ").append(toIndentedString(clientAccount)).append("\n");
    sb.append("    clientUserId: ").append(toIndentedString(clientUserId)).append("\n");
    sb.append("    clientWorkgroupId: ").append(toIndentedString(clientWorkgroupId)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    completionDate: ").append(toIndentedString(completionDate)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    deactivationReasonId: ").append(toIndentedString(deactivationReasonId)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isHot: ").append(toIndentedString(isHot)).append("\n");
    sb.append("    isPaperDirect: ").append(toIndentedString(isPaperDirect)).append("\n");
    sb.append("    projectCategoryId: ").append(toIndentedString(projectCategoryId)).append("\n");
    sb.append("    projectDescription: ").append(toIndentedString(projectDescription)).append("\n");
    sb.append("    projectName: ").append(toIndentedString(projectName)).append("\n");
    sb.append("    projectNumber: ").append(toIndentedString(projectNumber)).append("\n");
    sb.append("    projectOwnerUserId: ").append(toIndentedString(projectOwnerUserId)).append("\n");
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
    openapiFields.add("client_account");
    openapiFields.add("client_user_id");
    openapiFields.add("client_workgroup_id");
    openapiFields.add("comments");
    openapiFields.add("completion_date");
    openapiFields.add("custom_fields");
    openapiFields.add("deactivation_reason_id");
    openapiFields.add("is_active");
    openapiFields.add("is_hot");
    openapiFields.add("is_paper_direct");
    openapiFields.add("project_category_id");
    openapiFields.add("project_description");
    openapiFields.add("project_name");
    openapiFields.add("project_number");
    openapiFields.add("project_owner_user_id");
    openapiFields.add("project_status_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("project_status_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectPersistVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectPersistVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectPersistVO is not found in the empty JSON string", ProjectPersistVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectPersistVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectPersistVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProjectPersistVO.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("client_account") != null && !jsonObj.get("client_account").isJsonNull()) && !jsonObj.get("client_account").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client_account` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client_account").toString()));
      }
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
       if (!ProjectPersistVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectPersistVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectPersistVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectPersistVO.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectPersistVO>() {
           @Override
           public void write(JsonWriter out, ProjectPersistVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectPersistVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectPersistVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectPersistVO
   * @throws IOException if the JSON string is invalid with respect to ProjectPersistVO
   */
  public static ProjectPersistVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectPersistVO.class);
  }

  /**
   * Convert an instance of ProjectPersistVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

