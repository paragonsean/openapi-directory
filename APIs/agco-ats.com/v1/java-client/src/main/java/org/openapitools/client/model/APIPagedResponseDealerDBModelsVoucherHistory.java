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
import org.openapitools.client.model.APIPagedResponseMetadata;
import org.openapitools.client.model.DealerDBModelsVoucherHistory;

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
 * A response containing a page of results and metadata concerning the results
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class APIPagedResponseDealerDBModelsVoucherHistory {
  public static final String SERIALIZED_NAME_ENTITIES = "Entities";
  @SerializedName(SERIALIZED_NAME_ENTITIES)
  private List<DealerDBModelsVoucherHistory> entities = new ArrayList<>();

  public static final String SERIALIZED_NAME_METADATA = "Metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private APIPagedResponseMetadata metadata;

  public APIPagedResponseDealerDBModelsVoucherHistory() {
  }

  public APIPagedResponseDealerDBModelsVoucherHistory(
     List<DealerDBModelsVoucherHistory> entities
  ) {
    this();
    this.entities = entities;
  }

  /**
   * Get entities
   * @return entities
   */
  @javax.annotation.Nonnull
  public List<DealerDBModelsVoucherHistory> getEntities() {
    return entities;
  }



  public APIPagedResponseDealerDBModelsVoucherHistory metadata(APIPagedResponseMetadata metadata) {
    this.metadata = metadata;
    return this;
  }

  /**
   * Get metadata
   * @return metadata
   */
  @javax.annotation.Nonnull
  public APIPagedResponseMetadata getMetadata() {
    return metadata;
  }

  public void setMetadata(APIPagedResponseMetadata metadata) {
    this.metadata = metadata;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    APIPagedResponseDealerDBModelsVoucherHistory apIPagedResponseDealerDBModelsVoucherHistory = (APIPagedResponseDealerDBModelsVoucherHistory) o;
    return Objects.equals(this.entities, apIPagedResponseDealerDBModelsVoucherHistory.entities) &&
        Objects.equals(this.metadata, apIPagedResponseDealerDBModelsVoucherHistory.metadata);
  }

  @Override
  public int hashCode() {
    return Objects.hash(entities, metadata);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class APIPagedResponseDealerDBModelsVoucherHistory {\n");
    sb.append("    entities: ").append(toIndentedString(entities)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
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
    openapiFields.add("Entities");
    openapiFields.add("Metadata");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("Entities");
    openapiRequiredFields.add("Metadata");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to APIPagedResponseDealerDBModelsVoucherHistory
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!APIPagedResponseDealerDBModelsVoucherHistory.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in APIPagedResponseDealerDBModelsVoucherHistory is not found in the empty JSON string", APIPagedResponseDealerDBModelsVoucherHistory.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!APIPagedResponseDealerDBModelsVoucherHistory.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `APIPagedResponseDealerDBModelsVoucherHistory` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : APIPagedResponseDealerDBModelsVoucherHistory.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("Entities").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Entities` to be an array in the JSON string but got `%s`", jsonObj.get("Entities").toString()));
      }

      JsonArray jsonArrayentities = jsonObj.getAsJsonArray("Entities");
      // validate the required field `Entities` (array)
      for (int i = 0; i < jsonArrayentities.size(); i++) {
        DealerDBModelsVoucherHistory.validateJsonElement(jsonArrayentities.get(i));
      };
      // validate the required field `Metadata`
      APIPagedResponseMetadata.validateJsonElement(jsonObj.get("Metadata"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!APIPagedResponseDealerDBModelsVoucherHistory.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'APIPagedResponseDealerDBModelsVoucherHistory' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<APIPagedResponseDealerDBModelsVoucherHistory> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(APIPagedResponseDealerDBModelsVoucherHistory.class));

       return (TypeAdapter<T>) new TypeAdapter<APIPagedResponseDealerDBModelsVoucherHistory>() {
           @Override
           public void write(JsonWriter out, APIPagedResponseDealerDBModelsVoucherHistory value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public APIPagedResponseDealerDBModelsVoucherHistory read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of APIPagedResponseDealerDBModelsVoucherHistory given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of APIPagedResponseDealerDBModelsVoucherHistory
   * @throws IOException if the JSON string is invalid with respect to APIPagedResponseDealerDBModelsVoucherHistory
   */
  public static APIPagedResponseDealerDBModelsVoucherHistory fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, APIPagedResponseDealerDBModelsVoucherHistory.class);
  }

  /**
   * Convert an instance of APIPagedResponseDealerDBModelsVoucherHistory to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

