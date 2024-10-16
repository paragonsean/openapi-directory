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
import org.openapitools.client.model.LifeInsurancePolicyTypeModel;

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
 * LifeInsurancePolicyTypesModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LifeInsurancePolicyTypesModel {
  public static final String SERIALIZED_NAME_INSURANCE_POLICY_TYPES = "insurancePolicyTypes";
  @SerializedName(SERIALIZED_NAME_INSURANCE_POLICY_TYPES)
  private List<LifeInsurancePolicyTypeModel> insurancePolicyTypes = new ArrayList<>();

  public LifeInsurancePolicyTypesModel() {
  }

  public LifeInsurancePolicyTypesModel insurancePolicyTypes(List<LifeInsurancePolicyTypeModel> insurancePolicyTypes) {
    this.insurancePolicyTypes = insurancePolicyTypes;
    return this;
  }

  public LifeInsurancePolicyTypesModel addInsurancePolicyTypesItem(LifeInsurancePolicyTypeModel insurancePolicyTypesItem) {
    if (this.insurancePolicyTypes == null) {
      this.insurancePolicyTypes = new ArrayList<>();
    }
    this.insurancePolicyTypes.add(insurancePolicyTypesItem);
    return this;
  }

  /**
   * Get insurancePolicyTypes
   * @return insurancePolicyTypes
   */
  @javax.annotation.Nullable
  public List<LifeInsurancePolicyTypeModel> getInsurancePolicyTypes() {
    return insurancePolicyTypes;
  }

  public void setInsurancePolicyTypes(List<LifeInsurancePolicyTypeModel> insurancePolicyTypes) {
    this.insurancePolicyTypes = insurancePolicyTypes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LifeInsurancePolicyTypesModel lifeInsurancePolicyTypesModel = (LifeInsurancePolicyTypesModel) o;
    return Objects.equals(this.insurancePolicyTypes, lifeInsurancePolicyTypesModel.insurancePolicyTypes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(insurancePolicyTypes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LifeInsurancePolicyTypesModel {\n");
    sb.append("    insurancePolicyTypes: ").append(toIndentedString(insurancePolicyTypes)).append("\n");
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
    openapiFields.add("insurancePolicyTypes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LifeInsurancePolicyTypesModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LifeInsurancePolicyTypesModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LifeInsurancePolicyTypesModel is not found in the empty JSON string", LifeInsurancePolicyTypesModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LifeInsurancePolicyTypesModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LifeInsurancePolicyTypesModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("insurancePolicyTypes") != null && !jsonObj.get("insurancePolicyTypes").isJsonNull()) {
        JsonArray jsonArrayinsurancePolicyTypes = jsonObj.getAsJsonArray("insurancePolicyTypes");
        if (jsonArrayinsurancePolicyTypes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("insurancePolicyTypes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `insurancePolicyTypes` to be an array in the JSON string but got `%s`", jsonObj.get("insurancePolicyTypes").toString()));
          }

          // validate the optional field `insurancePolicyTypes` (array)
          for (int i = 0; i < jsonArrayinsurancePolicyTypes.size(); i++) {
            LifeInsurancePolicyTypeModel.validateJsonElement(jsonArrayinsurancePolicyTypes.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LifeInsurancePolicyTypesModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LifeInsurancePolicyTypesModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LifeInsurancePolicyTypesModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LifeInsurancePolicyTypesModel.class));

       return (TypeAdapter<T>) new TypeAdapter<LifeInsurancePolicyTypesModel>() {
           @Override
           public void write(JsonWriter out, LifeInsurancePolicyTypesModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LifeInsurancePolicyTypesModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LifeInsurancePolicyTypesModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LifeInsurancePolicyTypesModel
   * @throws IOException if the JSON string is invalid with respect to LifeInsurancePolicyTypesModel
   */
  public static LifeInsurancePolicyTypesModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LifeInsurancePolicyTypesModel.class);
  }

  /**
   * Convert an instance of LifeInsurancePolicyTypesModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

