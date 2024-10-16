/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner {
  /**
   * Reason for the rollback
   */
  @JsonAdapter(CategoryEnum.Adapter.class)
  public enum CategoryEnum {
    BROKE_OLD_FEATURES("broke old features"),
    
    OTHER("other"),
    
    PERFORMANCE("performance"),
    
    STABILITY("stability"),
    
    TESTING("testing"),
    
    UNIFYING_NETWORKS_VERSIONS("unifying networks versions");

    private String value;

    CategoryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CategoryEnum fromValue(String value) {
      for (CategoryEnum b : CategoryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CategoryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CategoryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CategoryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CategoryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CategoryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private CategoryEnum category;

  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner() {
  }

  public CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner category(CategoryEnum category) {
    this.category = category;
    return this;
  }

  /**
   * Reason for the rollback
   * @return category
   */
  @javax.annotation.Nullable
  public CategoryEnum getCategory() {
    return category;
  }

  public void setCategory(CategoryEnum category) {
    this.category = category;
  }


  public CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner comment(String comment) {
    this.comment = comment;
    return this;
  }

  /**
   * Additional comment about the rollback
   * @return comment
   */
  @javax.annotation.Nullable
  public String getComment() {
    return comment;
  }

  public void setComment(String comment) {
    this.comment = comment;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner createNetworkFirmwareUpgradesRollback200ResponseReasonsInner = (CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner) o;
    return Objects.equals(this.category, createNetworkFirmwareUpgradesRollback200ResponseReasonsInner.category) &&
        Objects.equals(this.comment, createNetworkFirmwareUpgradesRollback200ResponseReasonsInner.comment);
  }

  @Override
  public int hashCode() {
    return Objects.hash(category, comment);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner {\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
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
    openapiFields.add("category");
    openapiFields.add("comment");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner is not found in the empty JSON string", CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("category") != null && !jsonObj.get("category").isJsonNull()) && !jsonObj.get("category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("category").toString()));
      }
      // validate the optional field `category`
      if (jsonObj.get("category") != null && !jsonObj.get("category").isJsonNull()) {
        CategoryEnum.validateJsonElement(jsonObj.get("category"));
      }
      if ((jsonObj.get("comment") != null && !jsonObj.get("comment").isJsonNull()) && !jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner>() {
           @Override
           public void write(JsonWriter out, CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner
   */
  public static CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.class);
  }

  /**
   * Convert an instance of CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

