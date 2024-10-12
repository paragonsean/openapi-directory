/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import org.openapitools.client.model.EavDataAttributeOptionInterface;

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
 * CatalogProductAttributeOptionManagementV1AddPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CatalogProductAttributeOptionManagementV1AddPostRequest {
  public static final String SERIALIZED_NAME_OPTION = "option";
  @SerializedName(SERIALIZED_NAME_OPTION)
  private EavDataAttributeOptionInterface option;

  public CatalogProductAttributeOptionManagementV1AddPostRequest() {
  }

  public CatalogProductAttributeOptionManagementV1AddPostRequest option(EavDataAttributeOptionInterface option) {
    this.option = option;
    return this;
  }

  /**
   * Get option
   * @return option
   */
  @javax.annotation.Nonnull
  public EavDataAttributeOptionInterface getOption() {
    return option;
  }

  public void setOption(EavDataAttributeOptionInterface option) {
    this.option = option;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CatalogProductAttributeOptionManagementV1AddPostRequest catalogProductAttributeOptionManagementV1AddPostRequest = (CatalogProductAttributeOptionManagementV1AddPostRequest) o;
    return Objects.equals(this.option, catalogProductAttributeOptionManagementV1AddPostRequest.option);
  }

  @Override
  public int hashCode() {
    return Objects.hash(option);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CatalogProductAttributeOptionManagementV1AddPostRequest {\n");
    sb.append("    option: ").append(toIndentedString(option)).append("\n");
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
    openapiFields.add("option");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("option");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CatalogProductAttributeOptionManagementV1AddPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CatalogProductAttributeOptionManagementV1AddPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CatalogProductAttributeOptionManagementV1AddPostRequest is not found in the empty JSON string", CatalogProductAttributeOptionManagementV1AddPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CatalogProductAttributeOptionManagementV1AddPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CatalogProductAttributeOptionManagementV1AddPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CatalogProductAttributeOptionManagementV1AddPostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `option`
      EavDataAttributeOptionInterface.validateJsonElement(jsonObj.get("option"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CatalogProductAttributeOptionManagementV1AddPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CatalogProductAttributeOptionManagementV1AddPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CatalogProductAttributeOptionManagementV1AddPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CatalogProductAttributeOptionManagementV1AddPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CatalogProductAttributeOptionManagementV1AddPostRequest>() {
           @Override
           public void write(JsonWriter out, CatalogProductAttributeOptionManagementV1AddPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CatalogProductAttributeOptionManagementV1AddPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CatalogProductAttributeOptionManagementV1AddPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CatalogProductAttributeOptionManagementV1AddPostRequest
   * @throws IOException if the JSON string is invalid with respect to CatalogProductAttributeOptionManagementV1AddPostRequest
   */
  public static CatalogProductAttributeOptionManagementV1AddPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CatalogProductAttributeOptionManagementV1AddPostRequest.class);
  }

  /**
   * Convert an instance of CatalogProductAttributeOptionManagementV1AddPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

