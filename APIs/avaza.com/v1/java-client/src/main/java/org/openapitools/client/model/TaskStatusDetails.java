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
 * TaskStatusDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TaskStatusDetails {
  public static final String SERIALIZED_NAME_ACCOUNT_TASK_TYPE_I_D_F_K = "AccountTaskTypeIDFK";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_TASK_TYPE_I_D_F_K)
  private Integer accountTaskTypeIDFK;

  public static final String SERIALIZED_NAME_COLOR = "Color";
  @SerializedName(SERIALIZED_NAME_COLOR)
  private String color;

  public static final String SERIALIZED_NAME_DISPLAY_ORDER = "DisplayOrder";
  @SerializedName(SERIALIZED_NAME_DISPLAY_ORDER)
  private Integer displayOrder;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TASK_STATUS_CODE = "TaskStatusCode";
  @SerializedName(SERIALIZED_NAME_TASK_STATUS_CODE)
  private String taskStatusCode;

  public static final String SERIALIZED_NAME_TASK_TYPE_NAME = "TaskTypeName";
  @SerializedName(SERIALIZED_NAME_TASK_TYPE_NAME)
  private String taskTypeName;

  public static final String SERIALIZED_NAME_IS_COMPLETE = "isComplete";
  @SerializedName(SERIALIZED_NAME_IS_COMPLETE)
  private Boolean isComplete;

  public TaskStatusDetails() {
  }

  public TaskStatusDetails accountTaskTypeIDFK(Integer accountTaskTypeIDFK) {
    this.accountTaskTypeIDFK = accountTaskTypeIDFK;
    return this;
  }

  /**
   * Get accountTaskTypeIDFK
   * @return accountTaskTypeIDFK
   */
  @javax.annotation.Nullable
  public Integer getAccountTaskTypeIDFK() {
    return accountTaskTypeIDFK;
  }

  public void setAccountTaskTypeIDFK(Integer accountTaskTypeIDFK) {
    this.accountTaskTypeIDFK = accountTaskTypeIDFK;
  }


  public TaskStatusDetails color(String color) {
    this.color = color;
    return this;
  }

  /**
   * Get color
   * @return color
   */
  @javax.annotation.Nullable
  public String getColor() {
    return color;
  }

  public void setColor(String color) {
    this.color = color;
  }


  public TaskStatusDetails displayOrder(Integer displayOrder) {
    this.displayOrder = displayOrder;
    return this;
  }

  /**
   * Get displayOrder
   * @return displayOrder
   */
  @javax.annotation.Nullable
  public Integer getDisplayOrder() {
    return displayOrder;
  }

  public void setDisplayOrder(Integer displayOrder) {
    this.displayOrder = displayOrder;
  }


  public TaskStatusDetails name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public TaskStatusDetails taskStatusCode(String taskStatusCode) {
    this.taskStatusCode = taskStatusCode;
    return this;
  }

  /**
   * Get taskStatusCode
   * @return taskStatusCode
   */
  @javax.annotation.Nullable
  public String getTaskStatusCode() {
    return taskStatusCode;
  }

  public void setTaskStatusCode(String taskStatusCode) {
    this.taskStatusCode = taskStatusCode;
  }


  public TaskStatusDetails taskTypeName(String taskTypeName) {
    this.taskTypeName = taskTypeName;
    return this;
  }

  /**
   * Get taskTypeName
   * @return taskTypeName
   */
  @javax.annotation.Nullable
  public String getTaskTypeName() {
    return taskTypeName;
  }

  public void setTaskTypeName(String taskTypeName) {
    this.taskTypeName = taskTypeName;
  }


  public TaskStatusDetails isComplete(Boolean isComplete) {
    this.isComplete = isComplete;
    return this;
  }

  /**
   * Get isComplete
   * @return isComplete
   */
  @javax.annotation.Nullable
  public Boolean getIsComplete() {
    return isComplete;
  }

  public void setIsComplete(Boolean isComplete) {
    this.isComplete = isComplete;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaskStatusDetails taskStatusDetails = (TaskStatusDetails) o;
    return Objects.equals(this.accountTaskTypeIDFK, taskStatusDetails.accountTaskTypeIDFK) &&
        Objects.equals(this.color, taskStatusDetails.color) &&
        Objects.equals(this.displayOrder, taskStatusDetails.displayOrder) &&
        Objects.equals(this.name, taskStatusDetails.name) &&
        Objects.equals(this.taskStatusCode, taskStatusDetails.taskStatusCode) &&
        Objects.equals(this.taskTypeName, taskStatusDetails.taskTypeName) &&
        Objects.equals(this.isComplete, taskStatusDetails.isComplete);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountTaskTypeIDFK, color, displayOrder, name, taskStatusCode, taskTypeName, isComplete);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaskStatusDetails {\n");
    sb.append("    accountTaskTypeIDFK: ").append(toIndentedString(accountTaskTypeIDFK)).append("\n");
    sb.append("    color: ").append(toIndentedString(color)).append("\n");
    sb.append("    displayOrder: ").append(toIndentedString(displayOrder)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    taskStatusCode: ").append(toIndentedString(taskStatusCode)).append("\n");
    sb.append("    taskTypeName: ").append(toIndentedString(taskTypeName)).append("\n");
    sb.append("    isComplete: ").append(toIndentedString(isComplete)).append("\n");
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
    openapiFields.add("AccountTaskTypeIDFK");
    openapiFields.add("Color");
    openapiFields.add("DisplayOrder");
    openapiFields.add("Name");
    openapiFields.add("TaskStatusCode");
    openapiFields.add("TaskTypeName");
    openapiFields.add("isComplete");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TaskStatusDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TaskStatusDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TaskStatusDetails is not found in the empty JSON string", TaskStatusDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TaskStatusDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TaskStatusDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Color") != null && !jsonObj.get("Color").isJsonNull()) && !jsonObj.get("Color").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Color` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Color").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("TaskStatusCode") != null && !jsonObj.get("TaskStatusCode").isJsonNull()) && !jsonObj.get("TaskStatusCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaskStatusCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaskStatusCode").toString()));
      }
      if ((jsonObj.get("TaskTypeName") != null && !jsonObj.get("TaskTypeName").isJsonNull()) && !jsonObj.get("TaskTypeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaskTypeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaskTypeName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TaskStatusDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TaskStatusDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TaskStatusDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TaskStatusDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<TaskStatusDetails>() {
           @Override
           public void write(JsonWriter out, TaskStatusDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TaskStatusDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TaskStatusDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TaskStatusDetails
   * @throws IOException if the JSON string is invalid with respect to TaskStatusDetails
   */
  public static TaskStatusDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TaskStatusDetails.class);
  }

  /**
   * Convert an instance of TaskStatusDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

