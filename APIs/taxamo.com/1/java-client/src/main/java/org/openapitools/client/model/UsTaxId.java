/*
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
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
 * UsTaxId
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UsTaxId {
  public static final String SERIALIZED_NAME_STATE_OF_ISSUE = "state_of_issue";
  @SerializedName(SERIALIZED_NAME_STATE_OF_ISSUE)
  private String stateOfIssue;

  public static final String SERIALIZED_NAME_TAX_ID = "tax_id";
  @SerializedName(SERIALIZED_NAME_TAX_ID)
  private String taxId;

  public static final String SERIALIZED_NAME_TAX_ID_TYPE = "tax_id_type";
  @SerializedName(SERIALIZED_NAME_TAX_ID_TYPE)
  private String taxIdType;

  public UsTaxId() {
  }

  public UsTaxId stateOfIssue(String stateOfIssue) {
    this.stateOfIssue = stateOfIssue;
    return this;
  }

  /**
   * State of issue
   * @return stateOfIssue
   */
  @javax.annotation.Nullable
  public String getStateOfIssue() {
    return stateOfIssue;
  }

  public void setStateOfIssue(String stateOfIssue) {
    this.stateOfIssue = stateOfIssue;
  }


  public UsTaxId taxId(String taxId) {
    this.taxId = taxId;
    return this;
  }

  /**
   * Tax ID
   * @return taxId
   */
  @javax.annotation.Nullable
  public String getTaxId() {
    return taxId;
  }

  public void setTaxId(String taxId) {
    this.taxId = taxId;
  }


  public UsTaxId taxIdType(String taxIdType) {
    this.taxIdType = taxIdType;
    return this;
  }

  /**
   * Tax id type.
   * @return taxIdType
   */
  @javax.annotation.Nonnull
  public String getTaxIdType() {
    return taxIdType;
  }

  public void setTaxIdType(String taxIdType) {
    this.taxIdType = taxIdType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UsTaxId usTaxId = (UsTaxId) o;
    return Objects.equals(this.stateOfIssue, usTaxId.stateOfIssue) &&
        Objects.equals(this.taxId, usTaxId.taxId) &&
        Objects.equals(this.taxIdType, usTaxId.taxIdType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(stateOfIssue, taxId, taxIdType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UsTaxId {\n");
    sb.append("    stateOfIssue: ").append(toIndentedString(stateOfIssue)).append("\n");
    sb.append("    taxId: ").append(toIndentedString(taxId)).append("\n");
    sb.append("    taxIdType: ").append(toIndentedString(taxIdType)).append("\n");
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
    openapiFields.add("state_of_issue");
    openapiFields.add("tax_id");
    openapiFields.add("tax_id_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("tax_id_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UsTaxId
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UsTaxId.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UsTaxId is not found in the empty JSON string", UsTaxId.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UsTaxId.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UsTaxId` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UsTaxId.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("state_of_issue") != null && !jsonObj.get("state_of_issue").isJsonNull()) && !jsonObj.get("state_of_issue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state_of_issue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state_of_issue").toString()));
      }
      if ((jsonObj.get("tax_id") != null && !jsonObj.get("tax_id").isJsonNull()) && !jsonObj.get("tax_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_id").toString()));
      }
      if (!jsonObj.get("tax_id_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_id_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_id_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UsTaxId.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UsTaxId' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UsTaxId> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UsTaxId.class));

       return (TypeAdapter<T>) new TypeAdapter<UsTaxId>() {
           @Override
           public void write(JsonWriter out, UsTaxId value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UsTaxId read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UsTaxId given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UsTaxId
   * @throws IOException if the JSON string is invalid with respect to UsTaxId
   */
  public static UsTaxId fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UsTaxId.class);
  }

  /**
   * Convert an instance of UsTaxId to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

