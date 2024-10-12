/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
 * BasketItemOption
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BasketItemOption {
  public static final String SERIALIZED_NAME_ADDITIONAL_FIELDS = "additional_fields";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_FIELDS)
  private Object additionalFields;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_USED_IN_COMBINATION = "used_in_combination";
  @SerializedName(SERIALIZED_NAME_USED_IN_COMBINATION)
  private Boolean usedInCombination;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public static final String SERIALIZED_NAME_VALUE_ID = "value_id";
  @SerializedName(SERIALIZED_NAME_VALUE_ID)
  private String valueId;

  public BasketItemOption() {
  }

  public BasketItemOption additionalFields(Object additionalFields) {
    this.additionalFields = additionalFields;
    return this;
  }

  /**
   * Get additionalFields
   * @return additionalFields
   */
  @javax.annotation.Nullable
  public Object getAdditionalFields() {
    return additionalFields;
  }

  public void setAdditionalFields(Object additionalFields) {
    this.additionalFields = additionalFields;
  }


  public BasketItemOption customFields(Object customFields) {
    this.customFields = customFields;
    return this;
  }

  /**
   * Get customFields
   * @return customFields
   */
  @javax.annotation.Nullable
  public Object getCustomFields() {
    return customFields;
  }

  public void setCustomFields(Object customFields) {
    this.customFields = customFields;
  }


  public BasketItemOption id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public BasketItemOption name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public BasketItemOption usedInCombination(Boolean usedInCombination) {
    this.usedInCombination = usedInCombination;
    return this;
  }

  /**
   * Get usedInCombination
   * @return usedInCombination
   */
  @javax.annotation.Nullable
  public Boolean getUsedInCombination() {
    return usedInCombination;
  }

  public void setUsedInCombination(Boolean usedInCombination) {
    this.usedInCombination = usedInCombination;
  }


  public BasketItemOption value(String value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
   */
  @javax.annotation.Nullable
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }


  public BasketItemOption valueId(String valueId) {
    this.valueId = valueId;
    return this;
  }

  /**
   * Get valueId
   * @return valueId
   */
  @javax.annotation.Nullable
  public String getValueId() {
    return valueId;
  }

  public void setValueId(String valueId) {
    this.valueId = valueId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BasketItemOption basketItemOption = (BasketItemOption) o;
    return Objects.equals(this.additionalFields, basketItemOption.additionalFields) &&
        Objects.equals(this.customFields, basketItemOption.customFields) &&
        Objects.equals(this.id, basketItemOption.id) &&
        Objects.equals(this.name, basketItemOption.name) &&
        Objects.equals(this.usedInCombination, basketItemOption.usedInCombination) &&
        Objects.equals(this.value, basketItemOption.value) &&
        Objects.equals(this.valueId, basketItemOption.valueId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalFields, customFields, id, name, usedInCombination, value, valueId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BasketItemOption {\n");
    sb.append("    additionalFields: ").append(toIndentedString(additionalFields)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    usedInCombination: ").append(toIndentedString(usedInCombination)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    valueId: ").append(toIndentedString(valueId)).append("\n");
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
    openapiFields.add("additional_fields");
    openapiFields.add("custom_fields");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("used_in_combination");
    openapiFields.add("value");
    openapiFields.add("value_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BasketItemOption
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BasketItemOption.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BasketItemOption is not found in the empty JSON string", BasketItemOption.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BasketItemOption.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BasketItemOption` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
      if ((jsonObj.get("value_id") != null && !jsonObj.get("value_id").isJsonNull()) && !jsonObj.get("value_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BasketItemOption.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BasketItemOption' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BasketItemOption> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BasketItemOption.class));

       return (TypeAdapter<T>) new TypeAdapter<BasketItemOption>() {
           @Override
           public void write(JsonWriter out, BasketItemOption value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BasketItemOption read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BasketItemOption given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BasketItemOption
   * @throws IOException if the JSON string is invalid with respect to BasketItemOption
   */
  public static BasketItemOption fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BasketItemOption.class);
  }

  /**
   * Convert an instance of BasketItemOption to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

