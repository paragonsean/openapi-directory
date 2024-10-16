/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BuildSystemSharedDTOActivityStep;
import org.openapitools.client.model.BuildSystemSharedDTOParameter;

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
 * A DTO for an IActivity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BuildSystemSharedDTOActivity {
  public static final String SERIALIZED_NAME_ACTIVITY_I_D = "ActivityID";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_I_D)
  private Integer activityID;

  public static final String SERIALIZED_NAME_DELETED = "Deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PARAMETERS = "Parameters";
  @SerializedName(SERIALIZED_NAME_PARAMETERS)
  private List<BuildSystemSharedDTOParameter> parameters = new ArrayList<>();

  public static final String SERIALIZED_NAME_STEPS = "Steps";
  @SerializedName(SERIALIZED_NAME_STEPS)
  private List<BuildSystemSharedDTOActivityStep> steps = new ArrayList<>();

  public BuildSystemSharedDTOActivity() {
  }

  public BuildSystemSharedDTOActivity(
     List<BuildSystemSharedDTOParameter> parameters, 
     List<BuildSystemSharedDTOActivityStep> steps
  ) {
    this();
    this.parameters = parameters;
    this.steps = steps;
  }

  public BuildSystemSharedDTOActivity activityID(Integer activityID) {
    this.activityID = activityID;
    return this;
  }

  /**
   * The ID of the activity
   * @return activityID
   */
  @javax.annotation.Nullable
  public Integer getActivityID() {
    return activityID;
  }

  public void setActivityID(Integer activityID) {
    this.activityID = activityID;
  }


  public BuildSystemSharedDTOActivity deleted(Boolean deleted) {
    this.deleted = deleted;
    return this;
  }

  /**
   * 
   * @return deleted
   */
  @javax.annotation.Nullable
  public Boolean getDeleted() {
    return deleted;
  }

  public void setDeleted(Boolean deleted) {
    this.deleted = deleted;
  }


  public BuildSystemSharedDTOActivity name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the activity
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  /**
   * The parameters for this activity
   * @return parameters
   */
  @javax.annotation.Nullable
  public List<BuildSystemSharedDTOParameter> getParameters() {
    return parameters;
  }



  /**
   * The steps which are performed for this activity
   * @return steps
   */
  @javax.annotation.Nullable
  public List<BuildSystemSharedDTOActivityStep> getSteps() {
    return steps;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BuildSystemSharedDTOActivity buildSystemSharedDTOActivity = (BuildSystemSharedDTOActivity) o;
    return Objects.equals(this.activityID, buildSystemSharedDTOActivity.activityID) &&
        Objects.equals(this.deleted, buildSystemSharedDTOActivity.deleted) &&
        Objects.equals(this.name, buildSystemSharedDTOActivity.name) &&
        Objects.equals(this.parameters, buildSystemSharedDTOActivity.parameters) &&
        Objects.equals(this.steps, buildSystemSharedDTOActivity.steps);
  }

  @Override
  public int hashCode() {
    return Objects.hash(activityID, deleted, name, parameters, steps);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BuildSystemSharedDTOActivity {\n");
    sb.append("    activityID: ").append(toIndentedString(activityID)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    parameters: ").append(toIndentedString(parameters)).append("\n");
    sb.append("    steps: ").append(toIndentedString(steps)).append("\n");
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
    openapiFields.add("ActivityID");
    openapiFields.add("Deleted");
    openapiFields.add("Name");
    openapiFields.add("Parameters");
    openapiFields.add("Steps");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BuildSystemSharedDTOActivity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BuildSystemSharedDTOActivity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BuildSystemSharedDTOActivity is not found in the empty JSON string", BuildSystemSharedDTOActivity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BuildSystemSharedDTOActivity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BuildSystemSharedDTOActivity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if (jsonObj.get("Parameters") != null && !jsonObj.get("Parameters").isJsonNull()) {
        JsonArray jsonArrayparameters = jsonObj.getAsJsonArray("Parameters");
        if (jsonArrayparameters != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Parameters").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Parameters` to be an array in the JSON string but got `%s`", jsonObj.get("Parameters").toString()));
          }

          // validate the optional field `Parameters` (array)
          for (int i = 0; i < jsonArrayparameters.size(); i++) {
            BuildSystemSharedDTOParameter.validateJsonElement(jsonArrayparameters.get(i));
          };
        }
      }
      if (jsonObj.get("Steps") != null && !jsonObj.get("Steps").isJsonNull()) {
        JsonArray jsonArraysteps = jsonObj.getAsJsonArray("Steps");
        if (jsonArraysteps != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Steps").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Steps` to be an array in the JSON string but got `%s`", jsonObj.get("Steps").toString()));
          }

          // validate the optional field `Steps` (array)
          for (int i = 0; i < jsonArraysteps.size(); i++) {
            BuildSystemSharedDTOActivityStep.validateJsonElement(jsonArraysteps.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BuildSystemSharedDTOActivity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BuildSystemSharedDTOActivity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BuildSystemSharedDTOActivity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BuildSystemSharedDTOActivity.class));

       return (TypeAdapter<T>) new TypeAdapter<BuildSystemSharedDTOActivity>() {
           @Override
           public void write(JsonWriter out, BuildSystemSharedDTOActivity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BuildSystemSharedDTOActivity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BuildSystemSharedDTOActivity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BuildSystemSharedDTOActivity
   * @throws IOException if the JSON string is invalid with respect to BuildSystemSharedDTOActivity
   */
  public static BuildSystemSharedDTOActivity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BuildSystemSharedDTOActivity.class);
  }

  /**
   * Convert an instance of BuildSystemSharedDTOActivity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

