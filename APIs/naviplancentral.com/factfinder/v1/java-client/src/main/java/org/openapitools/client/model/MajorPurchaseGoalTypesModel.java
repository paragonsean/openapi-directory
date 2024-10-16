/*
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import org.openapitools.client.model.MajorPurchaseGoalTypeModel;

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
 * MajorPurchaseGoalTypesModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MajorPurchaseGoalTypesModel {
  public static final String SERIALIZED_NAME_MAJOR_PURCHASE_GOAL_TYPES = "majorPurchaseGoalTypes";
  @SerializedName(SERIALIZED_NAME_MAJOR_PURCHASE_GOAL_TYPES)
  private List<MajorPurchaseGoalTypeModel> majorPurchaseGoalTypes = new ArrayList<>();

  public MajorPurchaseGoalTypesModel() {
  }

  public MajorPurchaseGoalTypesModel majorPurchaseGoalTypes(List<MajorPurchaseGoalTypeModel> majorPurchaseGoalTypes) {
    this.majorPurchaseGoalTypes = majorPurchaseGoalTypes;
    return this;
  }

  public MajorPurchaseGoalTypesModel addMajorPurchaseGoalTypesItem(MajorPurchaseGoalTypeModel majorPurchaseGoalTypesItem) {
    if (this.majorPurchaseGoalTypes == null) {
      this.majorPurchaseGoalTypes = new ArrayList<>();
    }
    this.majorPurchaseGoalTypes.add(majorPurchaseGoalTypesItem);
    return this;
  }

  /**
   * Get majorPurchaseGoalTypes
   * @return majorPurchaseGoalTypes
   */
  @javax.annotation.Nullable
  public List<MajorPurchaseGoalTypeModel> getMajorPurchaseGoalTypes() {
    return majorPurchaseGoalTypes;
  }

  public void setMajorPurchaseGoalTypes(List<MajorPurchaseGoalTypeModel> majorPurchaseGoalTypes) {
    this.majorPurchaseGoalTypes = majorPurchaseGoalTypes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MajorPurchaseGoalTypesModel majorPurchaseGoalTypesModel = (MajorPurchaseGoalTypesModel) o;
    return Objects.equals(this.majorPurchaseGoalTypes, majorPurchaseGoalTypesModel.majorPurchaseGoalTypes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(majorPurchaseGoalTypes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MajorPurchaseGoalTypesModel {\n");
    sb.append("    majorPurchaseGoalTypes: ").append(toIndentedString(majorPurchaseGoalTypes)).append("\n");
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
    openapiFields.add("majorPurchaseGoalTypes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MajorPurchaseGoalTypesModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MajorPurchaseGoalTypesModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MajorPurchaseGoalTypesModel is not found in the empty JSON string", MajorPurchaseGoalTypesModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MajorPurchaseGoalTypesModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MajorPurchaseGoalTypesModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("majorPurchaseGoalTypes") != null && !jsonObj.get("majorPurchaseGoalTypes").isJsonNull()) {
        JsonArray jsonArraymajorPurchaseGoalTypes = jsonObj.getAsJsonArray("majorPurchaseGoalTypes");
        if (jsonArraymajorPurchaseGoalTypes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("majorPurchaseGoalTypes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `majorPurchaseGoalTypes` to be an array in the JSON string but got `%s`", jsonObj.get("majorPurchaseGoalTypes").toString()));
          }

          // validate the optional field `majorPurchaseGoalTypes` (array)
          for (int i = 0; i < jsonArraymajorPurchaseGoalTypes.size(); i++) {
            MajorPurchaseGoalTypeModel.validateJsonElement(jsonArraymajorPurchaseGoalTypes.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MajorPurchaseGoalTypesModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MajorPurchaseGoalTypesModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MajorPurchaseGoalTypesModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MajorPurchaseGoalTypesModel.class));

       return (TypeAdapter<T>) new TypeAdapter<MajorPurchaseGoalTypesModel>() {
           @Override
           public void write(JsonWriter out, MajorPurchaseGoalTypesModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MajorPurchaseGoalTypesModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MajorPurchaseGoalTypesModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MajorPurchaseGoalTypesModel
   * @throws IOException if the JSON string is invalid with respect to MajorPurchaseGoalTypesModel
   */
  public static MajorPurchaseGoalTypesModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MajorPurchaseGoalTypesModel.class);
  }

  /**
   * Convert an instance of MajorPurchaseGoalTypesModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

