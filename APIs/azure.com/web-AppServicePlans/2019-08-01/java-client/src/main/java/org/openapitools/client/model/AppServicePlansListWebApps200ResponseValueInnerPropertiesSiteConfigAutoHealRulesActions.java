/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
import org.openapitools.client.model.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction;

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
 * Actions which to take by the auto-heal module when a rule is triggered.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:54.768221-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions {
  /**
   * Predefined action to be taken.
   */
  @JsonAdapter(ActionTypeEnum.Adapter.class)
  public enum ActionTypeEnum {
    RECYCLE("Recycle"),
    
    LOG_EVENT("LogEvent"),
    
    CUSTOM_ACTION("CustomAction");

    private String value;

    ActionTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ActionTypeEnum fromValue(String value) {
      for (ActionTypeEnum b : ActionTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ActionTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ActionTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ActionTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ActionTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ActionTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACTION_TYPE = "actionType";
  @SerializedName(SERIALIZED_NAME_ACTION_TYPE)
  private ActionTypeEnum actionType;

  public static final String SERIALIZED_NAME_CUSTOM_ACTION = "customAction";
  @SerializedName(SERIALIZED_NAME_CUSTOM_ACTION)
  private AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction customAction;

  public static final String SERIALIZED_NAME_MIN_PROCESS_EXECUTION_TIME = "minProcessExecutionTime";
  @SerializedName(SERIALIZED_NAME_MIN_PROCESS_EXECUTION_TIME)
  private String minProcessExecutionTime;

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions() {
  }

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions actionType(ActionTypeEnum actionType) {
    this.actionType = actionType;
    return this;
  }

  /**
   * Predefined action to be taken.
   * @return actionType
   */
  @javax.annotation.Nullable
  public ActionTypeEnum getActionType() {
    return actionType;
  }

  public void setActionType(ActionTypeEnum actionType) {
    this.actionType = actionType;
  }


  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions customAction(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction customAction) {
    this.customAction = customAction;
    return this;
  }

  /**
   * Get customAction
   * @return customAction
   */
  @javax.annotation.Nullable
  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction getCustomAction() {
    return customAction;
  }

  public void setCustomAction(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction customAction) {
    this.customAction = customAction;
  }


  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions minProcessExecutionTime(String minProcessExecutionTime) {
    this.minProcessExecutionTime = minProcessExecutionTime;
    return this;
  }

  /**
   * Minimum time the process must execute before taking the action
   * @return minProcessExecutionTime
   */
  @javax.annotation.Nullable
  public String getMinProcessExecutionTime() {
    return minProcessExecutionTime;
  }

  public void setMinProcessExecutionTime(String minProcessExecutionTime) {
    this.minProcessExecutionTime = minProcessExecutionTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions = (AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions) o;
    return Objects.equals(this.actionType, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.actionType) &&
        Objects.equals(this.customAction, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.customAction) &&
        Objects.equals(this.minProcessExecutionTime, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.minProcessExecutionTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actionType, customAction, minProcessExecutionTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions {\n");
    sb.append("    actionType: ").append(toIndentedString(actionType)).append("\n");
    sb.append("    customAction: ").append(toIndentedString(customAction)).append("\n");
    sb.append("    minProcessExecutionTime: ").append(toIndentedString(minProcessExecutionTime)).append("\n");
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
    openapiFields.add("actionType");
    openapiFields.add("customAction");
    openapiFields.add("minProcessExecutionTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions is not found in the empty JSON string", AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("actionType") != null && !jsonObj.get("actionType").isJsonNull()) && !jsonObj.get("actionType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `actionType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("actionType").toString()));
      }
      // validate the optional field `actionType`
      if (jsonObj.get("actionType") != null && !jsonObj.get("actionType").isJsonNull()) {
        ActionTypeEnum.validateJsonElement(jsonObj.get("actionType"));
      }
      // validate the optional field `customAction`
      if (jsonObj.get("customAction") != null && !jsonObj.get("customAction").isJsonNull()) {
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction.validateJsonElement(jsonObj.get("customAction"));
      }
      if ((jsonObj.get("minProcessExecutionTime") != null && !jsonObj.get("minProcessExecutionTime").isJsonNull()) && !jsonObj.get("minProcessExecutionTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `minProcessExecutionTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("minProcessExecutionTime").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions>() {
           @Override
           public void write(JsonWriter out, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions
   */
  public static AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.class);
  }

  /**
   * Convert an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

