/*
 * Hotel Booking
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).   **Warning: Do not perform test booking in production**. All requests are sent and processed by hotel providers. An excessive amount of fake/canceled reservation will make you blacklisted by hotel providers. 
 *
 * The version of the OpenAPI document: 1.1.3
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
 * Associated Record (Flight Booking Record)
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:13.978744-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AssociatedRecord {
  /**
   * * GDS: Associated Amadeus GDS Flight Booking PNR Record
   */
  @JsonAdapter(OriginSystemCodeEnum.Adapter.class)
  public enum OriginSystemCodeEnum {
    GDS("GDS");

    private String value;

    OriginSystemCodeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OriginSystemCodeEnum fromValue(String value) {
      for (OriginSystemCodeEnum b : OriginSystemCodeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OriginSystemCodeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OriginSystemCodeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OriginSystemCodeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OriginSystemCodeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OriginSystemCodeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ORIGIN_SYSTEM_CODE = "originSystemCode";
  @SerializedName(SERIALIZED_NAME_ORIGIN_SYSTEM_CODE)
  private OriginSystemCodeEnum originSystemCode;

  public static final String SERIALIZED_NAME_REFERENCE = "reference";
  @SerializedName(SERIALIZED_NAME_REFERENCE)
  private String reference;

  public AssociatedRecord() {
  }

  public AssociatedRecord originSystemCode(OriginSystemCodeEnum originSystemCode) {
    this.originSystemCode = originSystemCode;
    return this;
  }

  /**
   * * GDS: Associated Amadeus GDS Flight Booking PNR Record
   * @return originSystemCode
   */
  @javax.annotation.Nonnull
  public OriginSystemCodeEnum getOriginSystemCode() {
    return originSystemCode;
  }

  public void setOriginSystemCode(OriginSystemCodeEnum originSystemCode) {
    this.originSystemCode = originSystemCode;
  }


  public AssociatedRecord reference(String reference) {
    this.reference = reference;
    return this;
  }

  /**
   * Amadeus GDS Record
   * @return reference
   */
  @javax.annotation.Nonnull
  public String getReference() {
    return reference;
  }

  public void setReference(String reference) {
    this.reference = reference;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AssociatedRecord associatedRecord = (AssociatedRecord) o;
    return Objects.equals(this.originSystemCode, associatedRecord.originSystemCode) &&
        Objects.equals(this.reference, associatedRecord.reference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(originSystemCode, reference);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AssociatedRecord {\n");
    sb.append("    originSystemCode: ").append(toIndentedString(originSystemCode)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
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
    openapiFields.add("originSystemCode");
    openapiFields.add("reference");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("originSystemCode");
    openapiRequiredFields.add("reference");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AssociatedRecord
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AssociatedRecord.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AssociatedRecord is not found in the empty JSON string", AssociatedRecord.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AssociatedRecord.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AssociatedRecord` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AssociatedRecord.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("originSystemCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `originSystemCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("originSystemCode").toString()));
      }
      // validate the required field `originSystemCode`
      OriginSystemCodeEnum.validateJsonElement(jsonObj.get("originSystemCode"));
      if (!jsonObj.get("reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AssociatedRecord.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AssociatedRecord' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AssociatedRecord> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AssociatedRecord.class));

       return (TypeAdapter<T>) new TypeAdapter<AssociatedRecord>() {
           @Override
           public void write(JsonWriter out, AssociatedRecord value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AssociatedRecord read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AssociatedRecord given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AssociatedRecord
   * @throws IOException if the JSON string is invalid with respect to AssociatedRecord
   */
  public static AssociatedRecord fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AssociatedRecord.class);
  }

  /**
   * Convert an instance of AssociatedRecord to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

