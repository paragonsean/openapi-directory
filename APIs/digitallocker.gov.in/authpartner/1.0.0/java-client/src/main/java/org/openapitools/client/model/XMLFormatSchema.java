/*
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
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
import org.openapitools.client.model.XMLFormatSchemaSignature;

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
 * XMLFormatSchema
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:03.399628-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class XMLFormatSchema {
  public static final String SERIALIZED_NAME_CERTIFICATE_DATA = "CertificateData";
  @SerializedName(SERIALIZED_NAME_CERTIFICATE_DATA)
  private List<Object> certificateData = new ArrayList<>();

  public static final String SERIALIZED_NAME_SIGNATURE = "Signature";
  @SerializedName(SERIALIZED_NAME_SIGNATURE)
  private XMLFormatSchemaSignature signature;

  public XMLFormatSchema() {
  }

  public XMLFormatSchema certificateData(List<Object> certificateData) {
    this.certificateData = certificateData;
    return this;
  }

  public XMLFormatSchema addCertificateDataItem(Object certificateDataItem) {
    if (this.certificateData == null) {
      this.certificateData = new ArrayList<>();
    }
    this.certificateData.add(certificateDataItem);
    return this;
  }

  /**
   * Get certificateData
   * @return certificateData
   */
  @javax.annotation.Nonnull
  public List<Object> getCertificateData() {
    return certificateData;
  }

  public void setCertificateData(List<Object> certificateData) {
    this.certificateData = certificateData;
  }


  public XMLFormatSchema signature(XMLFormatSchemaSignature signature) {
    this.signature = signature;
    return this;
  }

  /**
   * Get signature
   * @return signature
   */
  @javax.annotation.Nonnull
  public XMLFormatSchemaSignature getSignature() {
    return signature;
  }

  public void setSignature(XMLFormatSchemaSignature signature) {
    this.signature = signature;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    XMLFormatSchema xmLFormatSchema = (XMLFormatSchema) o;
    return Objects.equals(this.certificateData, xmLFormatSchema.certificateData) &&
        Objects.equals(this.signature, xmLFormatSchema.signature);
  }

  @Override
  public int hashCode() {
    return Objects.hash(certificateData, signature);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class XMLFormatSchema {\n");
    sb.append("    certificateData: ").append(toIndentedString(certificateData)).append("\n");
    sb.append("    signature: ").append(toIndentedString(signature)).append("\n");
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
    openapiFields.add("CertificateData");
    openapiFields.add("Signature");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("CertificateData");
    openapiRequiredFields.add("Signature");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to XMLFormatSchema
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!XMLFormatSchema.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in XMLFormatSchema is not found in the empty JSON string", XMLFormatSchema.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!XMLFormatSchema.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `XMLFormatSchema` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : XMLFormatSchema.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("CertificateData") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("CertificateData").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `CertificateData` to be an array in the JSON string but got `%s`", jsonObj.get("CertificateData").toString()));
      }
      // validate the required field `Signature`
      XMLFormatSchemaSignature.validateJsonElement(jsonObj.get("Signature"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!XMLFormatSchema.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'XMLFormatSchema' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<XMLFormatSchema> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(XMLFormatSchema.class));

       return (TypeAdapter<T>) new TypeAdapter<XMLFormatSchema>() {
           @Override
           public void write(JsonWriter out, XMLFormatSchema value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public XMLFormatSchema read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of XMLFormatSchema given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of XMLFormatSchema
   * @throws IOException if the JSON string is invalid with respect to XMLFormatSchema
   */
  public static XMLFormatSchema fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, XMLFormatSchema.class);
  }

  /**
   * Convert an instance of XMLFormatSchema to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

