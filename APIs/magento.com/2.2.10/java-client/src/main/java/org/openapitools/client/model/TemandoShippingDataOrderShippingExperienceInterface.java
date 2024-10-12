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
import java.math.BigDecimal;
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
 * Temando Shipping Experience Interface Local representation of a shipping rate in checkout. A set of shipping experiences is the result of creating an order at the Temando platform. (!) Needs to reside in Api namespace because selected shipping experience is exposed to public as a ShippingInterface extension attribute.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TemandoShippingDataOrderShippingExperienceInterface {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_COST = "cost";
  @SerializedName(SERIALIZED_NAME_COST)
  private BigDecimal cost;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public TemandoShippingDataOrderShippingExperienceInterface() {
  }

  public TemandoShippingDataOrderShippingExperienceInterface code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Get code
   * @return code
   */
  @javax.annotation.Nonnull
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public TemandoShippingDataOrderShippingExperienceInterface cost(BigDecimal cost) {
    this.cost = cost;
    return this;
  }

  /**
   * Get cost
   * @return cost
   */
  @javax.annotation.Nonnull
  public BigDecimal getCost() {
    return cost;
  }

  public void setCost(BigDecimal cost) {
    this.cost = cost;
  }


  public TemandoShippingDataOrderShippingExperienceInterface label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Get label
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TemandoShippingDataOrderShippingExperienceInterface temandoShippingDataOrderShippingExperienceInterface = (TemandoShippingDataOrderShippingExperienceInterface) o;
    return Objects.equals(this.code, temandoShippingDataOrderShippingExperienceInterface.code) &&
        Objects.equals(this.cost, temandoShippingDataOrderShippingExperienceInterface.cost) &&
        Objects.equals(this.label, temandoShippingDataOrderShippingExperienceInterface.label);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, cost, label);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TemandoShippingDataOrderShippingExperienceInterface {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    cost: ").append(toIndentedString(cost)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("cost");
    openapiFields.add("label");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("code");
    openapiRequiredFields.add("cost");
    openapiRequiredFields.add("label");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TemandoShippingDataOrderShippingExperienceInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TemandoShippingDataOrderShippingExperienceInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TemandoShippingDataOrderShippingExperienceInterface is not found in the empty JSON string", TemandoShippingDataOrderShippingExperienceInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TemandoShippingDataOrderShippingExperienceInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TemandoShippingDataOrderShippingExperienceInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TemandoShippingDataOrderShippingExperienceInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TemandoShippingDataOrderShippingExperienceInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TemandoShippingDataOrderShippingExperienceInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TemandoShippingDataOrderShippingExperienceInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TemandoShippingDataOrderShippingExperienceInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<TemandoShippingDataOrderShippingExperienceInterface>() {
           @Override
           public void write(JsonWriter out, TemandoShippingDataOrderShippingExperienceInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TemandoShippingDataOrderShippingExperienceInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TemandoShippingDataOrderShippingExperienceInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TemandoShippingDataOrderShippingExperienceInterface
   * @throws IOException if the JSON string is invalid with respect to TemandoShippingDataOrderShippingExperienceInterface
   */
  public static TemandoShippingDataOrderShippingExperienceInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TemandoShippingDataOrderShippingExperienceInterface.class);
  }

  /**
   * Convert an instance of TemandoShippingDataOrderShippingExperienceInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

