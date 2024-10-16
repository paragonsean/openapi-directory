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
import org.openapitools.client.model.ObjectLink;

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
 * FactFinderModuleWithIdModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FactFinderModuleWithIdModel {
  public static final String SERIALIZED_NAME_AVAILABLE = "available";
  @SerializedName(SERIALIZED_NAME_AVAILABLE)
  private Boolean available;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<ObjectLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODULE_ID = "moduleId";
  @SerializedName(SERIALIZED_NAME_MODULE_ID)
  private Integer moduleId;

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

  public FactFinderModuleWithIdModel() {
  }

  public FactFinderModuleWithIdModel available(Boolean available) {
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


  public FactFinderModuleWithIdModel factFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
    return this;
  }

  /**
   * Get factFinderId
   * @return factFinderId
   */
  @javax.annotation.Nullable
  public Integer getFactFinderId() {
    return factFinderId;
  }

  public void setFactFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
  }


  public FactFinderModuleWithIdModel links(List<ObjectLink> links) {
    this.links = links;
    return this;
  }

  public FactFinderModuleWithIdModel addLinksItem(ObjectLink linksItem) {
    if (this.links == null) {
      this.links = new ArrayList<>();
    }
    this.links.add(linksItem);
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nullable
  public List<ObjectLink> getLinks() {
    return links;
  }

  public void setLinks(List<ObjectLink> links) {
    this.links = links;
  }


  public FactFinderModuleWithIdModel moduleId(Integer moduleId) {
    this.moduleId = moduleId;
    return this;
  }

  /**
   * Get moduleId
   * @return moduleId
   */
  @javax.annotation.Nullable
  public Integer getModuleId() {
    return moduleId;
  }

  public void setModuleId(Integer moduleId) {
    this.moduleId = moduleId;
  }


  public FactFinderModuleWithIdModel moduleName(ModuleNameEnum moduleName) {
    this.moduleName = moduleName;
    return this;
  }

  /**
   * Get moduleName
   * @return moduleName
   */
  @javax.annotation.Nullable
  public ModuleNameEnum getModuleName() {
    return moduleName;
  }

  public void setModuleName(ModuleNameEnum moduleName) {
    this.moduleName = moduleName;
  }


  public FactFinderModuleWithIdModel visited(Boolean visited) {
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
    FactFinderModuleWithIdModel factFinderModuleWithIdModel = (FactFinderModuleWithIdModel) o;
    return Objects.equals(this.available, factFinderModuleWithIdModel.available) &&
        Objects.equals(this.factFinderId, factFinderModuleWithIdModel.factFinderId) &&
        Objects.equals(this.links, factFinderModuleWithIdModel.links) &&
        Objects.equals(this.moduleId, factFinderModuleWithIdModel.moduleId) &&
        Objects.equals(this.moduleName, factFinderModuleWithIdModel.moduleName) &&
        Objects.equals(this.visited, factFinderModuleWithIdModel.visited);
  }

  @Override
  public int hashCode() {
    return Objects.hash(available, factFinderId, links, moduleId, moduleName, visited);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FactFinderModuleWithIdModel {\n");
    sb.append("    available: ").append(toIndentedString(available)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    moduleId: ").append(toIndentedString(moduleId)).append("\n");
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
    openapiFields.add("factFinderId");
    openapiFields.add("links");
    openapiFields.add("moduleId");
    openapiFields.add("moduleName");
    openapiFields.add("visited");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FactFinderModuleWithIdModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FactFinderModuleWithIdModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FactFinderModuleWithIdModel is not found in the empty JSON string", FactFinderModuleWithIdModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FactFinderModuleWithIdModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FactFinderModuleWithIdModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("links") != null && !jsonObj.get("links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `links` to be an array in the JSON string but got `%s`", jsonObj.get("links").toString()));
          }

          // validate the optional field `links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            ObjectLink.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("moduleName") != null && !jsonObj.get("moduleName").isJsonNull()) && !jsonObj.get("moduleName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moduleName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moduleName").toString()));
      }
      // validate the optional field `moduleName`
      if (jsonObj.get("moduleName") != null && !jsonObj.get("moduleName").isJsonNull()) {
        ModuleNameEnum.validateJsonElement(jsonObj.get("moduleName"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FactFinderModuleWithIdModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FactFinderModuleWithIdModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FactFinderModuleWithIdModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FactFinderModuleWithIdModel.class));

       return (TypeAdapter<T>) new TypeAdapter<FactFinderModuleWithIdModel>() {
           @Override
           public void write(JsonWriter out, FactFinderModuleWithIdModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FactFinderModuleWithIdModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FactFinderModuleWithIdModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FactFinderModuleWithIdModel
   * @throws IOException if the JSON string is invalid with respect to FactFinderModuleWithIdModel
   */
  public static FactFinderModuleWithIdModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FactFinderModuleWithIdModel.class);
  }

  /**
   * Convert an instance of FactFinderModuleWithIdModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

