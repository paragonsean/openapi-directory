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
 * Discount
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Discount {
  public static final String SERIALIZED_NAME_ADDITIONAL_FIELDS = "additional_fields";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_FIELDS)
  private Object additionalFields;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields;

  public static final String SERIALIZED_NAME_CUSTOMER_GROUP_IDS = "customer_group_ids";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_GROUP_IDS)
  private String customerGroupIds;

  public static final String SERIALIZED_NAME_FROM_TIME = "from_time";
  @SerializedName(SERIALIZED_NAME_FROM_TIME)
  private String fromTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MODIFIER_TYPE = "modifier_type";
  @SerializedName(SERIALIZED_NAME_MODIFIER_TYPE)
  private String modifierType;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SORT_ORDER = "sort_order";
  @SerializedName(SERIALIZED_NAME_SORT_ORDER)
  private Integer sortOrder;

  public static final String SERIALIZED_NAME_TO_TIME = "to_time";
  @SerializedName(SERIALIZED_NAME_TO_TIME)
  private String toTime;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private BigDecimal value;

  public Discount() {
  }

  public Discount additionalFields(Object additionalFields) {
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


  public Discount customFields(Object customFields) {
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


  public Discount customerGroupIds(String customerGroupIds) {
    this.customerGroupIds = customerGroupIds;
    return this;
  }

  /**
   * Get customerGroupIds
   * @return customerGroupIds
   */
  @javax.annotation.Nullable
  public String getCustomerGroupIds() {
    return customerGroupIds;
  }

  public void setCustomerGroupIds(String customerGroupIds) {
    this.customerGroupIds = customerGroupIds;
  }


  public Discount fromTime(String fromTime) {
    this.fromTime = fromTime;
    return this;
  }

  /**
   * Get fromTime
   * @return fromTime
   */
  @javax.annotation.Nullable
  public String getFromTime() {
    return fromTime;
  }

  public void setFromTime(String fromTime) {
    this.fromTime = fromTime;
  }


  public Discount id(String id) {
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


  public Discount modifierType(String modifierType) {
    this.modifierType = modifierType;
    return this;
  }

  /**
   * Get modifierType
   * @return modifierType
   */
  @javax.annotation.Nullable
  public String getModifierType() {
    return modifierType;
  }

  public void setModifierType(String modifierType) {
    this.modifierType = modifierType;
  }


  public Discount name(String name) {
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


  public Discount sortOrder(Integer sortOrder) {
    this.sortOrder = sortOrder;
    return this;
  }

  /**
   * Get sortOrder
   * @return sortOrder
   */
  @javax.annotation.Nullable
  public Integer getSortOrder() {
    return sortOrder;
  }

  public void setSortOrder(Integer sortOrder) {
    this.sortOrder = sortOrder;
  }


  public Discount toTime(String toTime) {
    this.toTime = toTime;
    return this;
  }

  /**
   * Get toTime
   * @return toTime
   */
  @javax.annotation.Nullable
  public String getToTime() {
    return toTime;
  }

  public void setToTime(String toTime) {
    this.toTime = toTime;
  }


  public Discount value(BigDecimal value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
   */
  @javax.annotation.Nullable
  public BigDecimal getValue() {
    return value;
  }

  public void setValue(BigDecimal value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Discount discount = (Discount) o;
    return Objects.equals(this.additionalFields, discount.additionalFields) &&
        Objects.equals(this.customFields, discount.customFields) &&
        Objects.equals(this.customerGroupIds, discount.customerGroupIds) &&
        Objects.equals(this.fromTime, discount.fromTime) &&
        Objects.equals(this.id, discount.id) &&
        Objects.equals(this.modifierType, discount.modifierType) &&
        Objects.equals(this.name, discount.name) &&
        Objects.equals(this.sortOrder, discount.sortOrder) &&
        Objects.equals(this.toTime, discount.toTime) &&
        Objects.equals(this.value, discount.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalFields, customFields, customerGroupIds, fromTime, id, modifierType, name, sortOrder, toTime, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Discount {\n");
    sb.append("    additionalFields: ").append(toIndentedString(additionalFields)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customerGroupIds: ").append(toIndentedString(customerGroupIds)).append("\n");
    sb.append("    fromTime: ").append(toIndentedString(fromTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    modifierType: ").append(toIndentedString(modifierType)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    sortOrder: ").append(toIndentedString(sortOrder)).append("\n");
    sb.append("    toTime: ").append(toIndentedString(toTime)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("customer_group_ids");
    openapiFields.add("from_time");
    openapiFields.add("id");
    openapiFields.add("modifier_type");
    openapiFields.add("name");
    openapiFields.add("sort_order");
    openapiFields.add("to_time");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Discount
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Discount.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Discount is not found in the empty JSON string", Discount.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Discount.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Discount` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("customer_group_ids") != null && !jsonObj.get("customer_group_ids").isJsonNull()) && !jsonObj.get("customer_group_ids").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customer_group_ids` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customer_group_ids").toString()));
      }
      if ((jsonObj.get("from_time") != null && !jsonObj.get("from_time").isJsonNull()) && !jsonObj.get("from_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `from_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("from_time").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("modifier_type") != null && !jsonObj.get("modifier_type").isJsonNull()) && !jsonObj.get("modifier_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modifier_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modifier_type").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("to_time") != null && !jsonObj.get("to_time").isJsonNull()) && !jsonObj.get("to_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `to_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("to_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Discount.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Discount' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Discount> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Discount.class));

       return (TypeAdapter<T>) new TypeAdapter<Discount>() {
           @Override
           public void write(JsonWriter out, Discount value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Discount read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Discount given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Discount
   * @throws IOException if the JSON string is invalid with respect to Discount
   */
  public static Discount fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Discount.class);
  }

  /**
   * Convert an instance of Discount to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

