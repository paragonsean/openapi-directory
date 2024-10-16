/*
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Java type: com.noosh.nooshapi.vo.PropertyPaAndAttVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PropertyPaAndAttVO {
  public static final String SERIALIZED_NAME_DATE_VALUE = "date_value";
  @SerializedName(SERIALIZED_NAME_DATE_VALUE)
  private LocalDate dateValue;

  public static final String SERIALIZED_NAME_NUMBER_VALUE = "number_value";
  @SerializedName(SERIALIZED_NAME_NUMBER_VALUE)
  private Object numberValue = null;

  public static final String SERIALIZED_NAME_PARAM_ID = "param_id";
  @SerializedName(SERIALIZED_NAME_PARAM_ID)
  private Long paramId;

  public static final String SERIALIZED_NAME_PARAM_NAME = "param_name";
  @SerializedName(SERIALIZED_NAME_PARAM_NAME)
  private String paramName;

  public static final String SERIALIZED_NAME_PROPERTY_ATTRIBUTE_ID = "property_attribute_id";
  @SerializedName(SERIALIZED_NAME_PROPERTY_ATTRIBUTE_ID)
  private Long propertyAttributeId;

  public static final String SERIALIZED_NAME_STRING_VALUE = "string_value";
  @SerializedName(SERIALIZED_NAME_STRING_VALUE)
  private String stringValue;

  public PropertyPaAndAttVO() {
  }

  public PropertyPaAndAttVO dateValue(LocalDate dateValue) {
    this.dateValue = dateValue;
    return this;
  }

  /**
   * 
   * @return dateValue
   */
  @javax.annotation.Nullable
  public LocalDate getDateValue() {
    return dateValue;
  }

  public void setDateValue(LocalDate dateValue) {
    this.dateValue = dateValue;
  }


  public PropertyPaAndAttVO numberValue(Object numberValue) {
    this.numberValue = numberValue;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return numberValue
   */
  @javax.annotation.Nullable
  public Object getNumberValue() {
    return numberValue;
  }

  public void setNumberValue(Object numberValue) {
    this.numberValue = numberValue;
  }


  public PropertyPaAndAttVO paramId(Long paramId) {
    this.paramId = paramId;
    return this;
  }

  /**
   * 
   * @return paramId
   */
  @javax.annotation.Nullable
  public Long getParamId() {
    return paramId;
  }

  public void setParamId(Long paramId) {
    this.paramId = paramId;
  }


  public PropertyPaAndAttVO paramName(String paramName) {
    this.paramName = paramName;
    return this;
  }

  /**
   * 
   * @return paramName
   */
  @javax.annotation.Nullable
  public String getParamName() {
    return paramName;
  }

  public void setParamName(String paramName) {
    this.paramName = paramName;
  }


  public PropertyPaAndAttVO propertyAttributeId(Long propertyAttributeId) {
    this.propertyAttributeId = propertyAttributeId;
    return this;
  }

  /**
   * 
   * @return propertyAttributeId
   */
  @javax.annotation.Nullable
  public Long getPropertyAttributeId() {
    return propertyAttributeId;
  }

  public void setPropertyAttributeId(Long propertyAttributeId) {
    this.propertyAttributeId = propertyAttributeId;
  }


  public PropertyPaAndAttVO stringValue(String stringValue) {
    this.stringValue = stringValue;
    return this;
  }

  /**
   * 
   * @return stringValue
   */
  @javax.annotation.Nullable
  public String getStringValue() {
    return stringValue;
  }

  public void setStringValue(String stringValue) {
    this.stringValue = stringValue;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PropertyPaAndAttVO propertyPaAndAttVO = (PropertyPaAndAttVO) o;
    return Objects.equals(this.dateValue, propertyPaAndAttVO.dateValue) &&
        Objects.equals(this.numberValue, propertyPaAndAttVO.numberValue) &&
        Objects.equals(this.paramId, propertyPaAndAttVO.paramId) &&
        Objects.equals(this.paramName, propertyPaAndAttVO.paramName) &&
        Objects.equals(this.propertyAttributeId, propertyPaAndAttVO.propertyAttributeId) &&
        Objects.equals(this.stringValue, propertyPaAndAttVO.stringValue);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(dateValue, numberValue, paramId, paramName, propertyAttributeId, stringValue);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PropertyPaAndAttVO {\n");
    sb.append("    dateValue: ").append(toIndentedString(dateValue)).append("\n");
    sb.append("    numberValue: ").append(toIndentedString(numberValue)).append("\n");
    sb.append("    paramId: ").append(toIndentedString(paramId)).append("\n");
    sb.append("    paramName: ").append(toIndentedString(paramName)).append("\n");
    sb.append("    propertyAttributeId: ").append(toIndentedString(propertyAttributeId)).append("\n");
    sb.append("    stringValue: ").append(toIndentedString(stringValue)).append("\n");
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
    openapiFields.add("date_value");
    openapiFields.add("number_value");
    openapiFields.add("param_id");
    openapiFields.add("param_name");
    openapiFields.add("property_attribute_id");
    openapiFields.add("string_value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PropertyPaAndAttVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PropertyPaAndAttVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PropertyPaAndAttVO is not found in the empty JSON string", PropertyPaAndAttVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PropertyPaAndAttVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PropertyPaAndAttVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("param_name") != null && !jsonObj.get("param_name").isJsonNull()) && !jsonObj.get("param_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `param_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("param_name").toString()));
      }
      if ((jsonObj.get("string_value") != null && !jsonObj.get("string_value").isJsonNull()) && !jsonObj.get("string_value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `string_value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("string_value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PropertyPaAndAttVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PropertyPaAndAttVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PropertyPaAndAttVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PropertyPaAndAttVO.class));

       return (TypeAdapter<T>) new TypeAdapter<PropertyPaAndAttVO>() {
           @Override
           public void write(JsonWriter out, PropertyPaAndAttVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PropertyPaAndAttVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PropertyPaAndAttVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PropertyPaAndAttVO
   * @throws IOException if the JSON string is invalid with respect to PropertyPaAndAttVO
   */
  public static PropertyPaAndAttVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PropertyPaAndAttVO.class);
  }

  /**
   * Convert an instance of PropertyPaAndAttVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

