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
 * FactFinderModuleModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FactFinderModuleModel {
  public static final String SERIALIZED_NAME_AVAILABLE = "available";
  @SerializedName(SERIALIZED_NAME_AVAILABLE)
  private Boolean available;

  /**
   * Gets or Sets moduleName
   */
  @JsonAdapter(ModuleNameEnum.Adapter.class)
  public enum ModuleNameEnum {
    DEMOGRAPHICS("Demographics"),
    
    ASSETS("Assets"),
    
    LIABILITIES("Liabilities"),
    
    INCOMES("Incomes"),
    
    EXPENSES("Expenses"),
    
    INSURANCE("Insurance"),
    
    RETIREMENT("Retirement"),
    
    EDUCATION("Education"),
    
    MAJOR_PURCHASE("MajorPurchase");

    private String value;

    ModuleNameEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ModuleNameEnum fromValue(String value) {
      for (ModuleNameEnum b : ModuleNameEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ModuleNameEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ModuleNameEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ModuleNameEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ModuleNameEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ModuleNameEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MODULE_NAME = "moduleName";
  @SerializedName(SERIALIZED_NAME_MODULE_NAME)
  private ModuleNameEnum moduleName;

  public static final String SERIALIZED_NAME_VISITED = "visited";
  @SerializedName(SERIALIZED_NAME_VISITED)
  private Boolean visited;

  public FactFinderModuleModel() {
  }

  public FactFinderModuleModel available(Boolean available) {
    this.available = available;
    return this;
  }

  /**
   * Get available
   * @return available
   */
  @javax.annotation.Nullable
  public Boolean getAvailable() {
    return available;
  }

  public void setAvailable(Boolean available) {
    this.available = available;
  }


  public FactFinderModuleModel moduleName(ModuleNameEnum moduleName) {
    this.moduleName = moduleName;
    return this;
  }

  /**
   * Get moduleName
   * @return moduleName
   */
  @javax.annotation.Nonnull
  public ModuleNameEnum getModuleName() {
    return moduleName;
  }

  public void setModuleName(ModuleNameEnum moduleName) {
    this.moduleName = moduleName;
  }


  public FactFinderModuleModel visited(Boolean visited) {
    this.visited = visited;
    return this;
  }

  /**
   * Get visited
   * @return visited
   */
  @javax.annotation.Nullable
  public Boolean getVisited() {
    return visited;
  }

  public void setVisited(Boolean visited) {
    this.visited = visited;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FactFinderModuleModel factFinderModuleModel = (FactFinderModuleModel) o;
    return Objects.equals(this.available, factFinderModuleModel.available) &&
        Objects.equals(this.moduleName, factFinderModuleModel.moduleName) &&
        Objects.equals(this.visited, factFinderModuleModel.visited);
  }

  @Override
  public int hashCode() {
    return Objects.hash(available, moduleName, visited);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FactFinderModuleModel {\n");
    sb.append("    available: ").append(toIndentedString(available)).append("\n");
    sb.append("    moduleName: ").append(toIndentedString(moduleName)).append("\n");
    sb.append("    visited: ").append(toIndentedString(visited)).append("\n");
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
    openapiFields.add("available");
    openapiFields.add("moduleName");
    openapiFields.add("visited");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("moduleName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FactFinderModuleModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FactFinderModuleModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FactFinderModuleModel is not found in the empty JSON string", FactFinderModuleModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FactFinderModuleModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FactFinderModuleModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FactFinderModuleModel.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("moduleName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moduleName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moduleName").toString()));
      }
      // validate the required field `moduleName`
      ModuleNameEnum.validateJsonElement(jsonObj.get("moduleName"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FactFinderModuleModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FactFinderModuleModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FactFinderModuleModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FactFinderModuleModel.class));

       return (TypeAdapter<T>) new TypeAdapter<FactFinderModuleModel>() {
           @Override
           public void write(JsonWriter out, FactFinderModuleModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FactFinderModuleModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FactFinderModuleModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FactFinderModuleModel
   * @throws IOException if the JSON string is invalid with respect to FactFinderModuleModel
   */
  public static FactFinderModuleModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FactFinderModuleModel.class);
  }

  /**
   * Convert an instance of FactFinderModuleModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

