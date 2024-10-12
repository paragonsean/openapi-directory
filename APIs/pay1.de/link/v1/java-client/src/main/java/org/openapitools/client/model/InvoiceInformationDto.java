/*
 * PAYONE Link API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * Contact: info@payone.com
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
 * relevant information for the invoice module
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:05.527924-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InvoiceInformationDto {
  public static final String SERIALIZED_NAME_INVOICE_ID = "invoiceId";
  @SerializedName(SERIALIZED_NAME_INVOICE_ID)
  private String invoiceId;

  public static final String SERIALIZED_NAME_INVOICE_TEXT = "invoiceText";
  @SerializedName(SERIALIZED_NAME_INVOICE_TEXT)
  private String invoiceText;

  public InvoiceInformationDto() {
  }

  public InvoiceInformationDto invoiceId(String invoiceId) {
    this.invoiceId = invoiceId;
    return this;
  }

  /**
   * id that should be put on the invoice
   * @return invoiceId
   */
  @javax.annotation.Nullable
  public String getInvoiceId() {
    return invoiceId;
  }

  public void setInvoiceId(String invoiceId) {
    this.invoiceId = invoiceId;
  }


  public InvoiceInformationDto invoiceText(String invoiceText) {
    this.invoiceText = invoiceText;
    return this;
  }

  /**
   * short text that should be put after the invoice
   * @return invoiceText
   */
  @javax.annotation.Nullable
  public String getInvoiceText() {
    return invoiceText;
  }

  public void setInvoiceText(String invoiceText) {
    this.invoiceText = invoiceText;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InvoiceInformationDto invoiceInformationDto = (InvoiceInformationDto) o;
    return Objects.equals(this.invoiceId, invoiceInformationDto.invoiceId) &&
        Objects.equals(this.invoiceText, invoiceInformationDto.invoiceText);
  }

  @Override
  public int hashCode() {
    return Objects.hash(invoiceId, invoiceText);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InvoiceInformationDto {\n");
    sb.append("    invoiceId: ").append(toIndentedString(invoiceId)).append("\n");
    sb.append("    invoiceText: ").append(toIndentedString(invoiceText)).append("\n");
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
    openapiFields.add("invoiceId");
    openapiFields.add("invoiceText");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InvoiceInformationDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InvoiceInformationDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InvoiceInformationDto is not found in the empty JSON string", InvoiceInformationDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InvoiceInformationDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InvoiceInformationDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("invoiceId") != null && !jsonObj.get("invoiceId").isJsonNull()) && !jsonObj.get("invoiceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoiceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoiceId").toString()));
      }
      if ((jsonObj.get("invoiceText") != null && !jsonObj.get("invoiceText").isJsonNull()) && !jsonObj.get("invoiceText").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoiceText` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoiceText").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InvoiceInformationDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InvoiceInformationDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InvoiceInformationDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InvoiceInformationDto.class));

       return (TypeAdapter<T>) new TypeAdapter<InvoiceInformationDto>() {
           @Override
           public void write(JsonWriter out, InvoiceInformationDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InvoiceInformationDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InvoiceInformationDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InvoiceInformationDto
   * @throws IOException if the JSON string is invalid with respect to InvoiceInformationDto
   */
  public static InvoiceInformationDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InvoiceInformationDto.class);
  }

  /**
   * Convert an instance of InvoiceInformationDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

