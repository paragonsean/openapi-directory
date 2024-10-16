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
 * Java type: com.noosh.nooshapi.vo.SupplierWorkgroupSimpleVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SupplierWorkgroupSimpleVO {
  public static final String SERIALIZED_NAME_BU_SUPPLIER_WORKGROUP_ID = "bu_supplier_workgroup_id";
  @SerializedName(SERIALIZED_NAME_BU_SUPPLIER_WORKGROUP_ID)
  private Long buSupplierWorkgroupId;

  public static final String SERIALIZED_NAME_BU_SUPPLIER_WORKGROUP_NAME = "bu_supplier_workgroup_name";
  @SerializedName(SERIALIZED_NAME_BU_SUPPLIER_WORKGROUP_NAME)
  private String buSupplierWorkgroupName;

  public static final String SERIALIZED_NAME_CLIENT_WORKGROUP_ID = "client_workgroup_id";
  @SerializedName(SERIALIZED_NAME_CLIENT_WORKGROUP_ID)
  private Long clientWorkgroupId;

  public static final String SERIALIZED_NAME_CLIENT_WORKGROUP_NAME = "client_workgroup_name";
  @SerializedName(SERIALIZED_NAME_CLIENT_WORKGROUP_NAME)
  private String clientWorkgroupName;

  public static final String SERIALIZED_NAME_IS_APPROVED = "is_approved";
  @SerializedName(SERIALIZED_NAME_IS_APPROVED)
  private Boolean isApproved;

  public static final String SERIALIZED_NAME_SUPPLIER_CODE = "supplier_code";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_CODE)
  private String supplierCode;

  public static final String SERIALIZED_NAME_SUPPLIER_WORKGROUP_ID = "supplier_workgroup_id";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_WORKGROUP_ID)
  private Long supplierWorkgroupId;

  public static final String SERIALIZED_NAME_SUPPLIER_WORKGROUP_NAME = "supplier_workgroup_name";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_WORKGROUP_NAME)
  private String supplierWorkgroupName;

  public SupplierWorkgroupSimpleVO() {
  }

  public SupplierWorkgroupSimpleVO buSupplierWorkgroupId(Long buSupplierWorkgroupId) {
    this.buSupplierWorkgroupId = buSupplierWorkgroupId;
    return this;
  }

  /**
   * 
   * @return buSupplierWorkgroupId
   */
  @javax.annotation.Nullable
  public Long getBuSupplierWorkgroupId() {
    return buSupplierWorkgroupId;
  }

  public void setBuSupplierWorkgroupId(Long buSupplierWorkgroupId) {
    this.buSupplierWorkgroupId = buSupplierWorkgroupId;
  }


  public SupplierWorkgroupSimpleVO buSupplierWorkgroupName(String buSupplierWorkgroupName) {
    this.buSupplierWorkgroupName = buSupplierWorkgroupName;
    return this;
  }

  /**
   * 
   * @return buSupplierWorkgroupName
   */
  @javax.annotation.Nullable
  public String getBuSupplierWorkgroupName() {
    return buSupplierWorkgroupName;
  }

  public void setBuSupplierWorkgroupName(String buSupplierWorkgroupName) {
    this.buSupplierWorkgroupName = buSupplierWorkgroupName;
  }


  public SupplierWorkgroupSimpleVO clientWorkgroupId(Long clientWorkgroupId) {
    this.clientWorkgroupId = clientWorkgroupId;
    return this;
  }

  /**
   * 
   * @return clientWorkgroupId
   */
  @javax.annotation.Nullable
  public Long getClientWorkgroupId() {
    return clientWorkgroupId;
  }

  public void setClientWorkgroupId(Long clientWorkgroupId) {
    this.clientWorkgroupId = clientWorkgroupId;
  }


  public SupplierWorkgroupSimpleVO clientWorkgroupName(String clientWorkgroupName) {
    this.clientWorkgroupName = clientWorkgroupName;
    return this;
  }

  /**
   * 
   * @return clientWorkgroupName
   */
  @javax.annotation.Nullable
  public String getClientWorkgroupName() {
    return clientWorkgroupName;
  }

  public void setClientWorkgroupName(String clientWorkgroupName) {
    this.clientWorkgroupName = clientWorkgroupName;
  }


  public SupplierWorkgroupSimpleVO isApproved(Boolean isApproved) {
    this.isApproved = isApproved;
    return this;
  }

  /**
   * 
   * @return isApproved
   */
  @javax.annotation.Nullable
  public Boolean getIsApproved() {
    return isApproved;
  }

  public void setIsApproved(Boolean isApproved) {
    this.isApproved = isApproved;
  }


  public SupplierWorkgroupSimpleVO supplierCode(String supplierCode) {
    this.supplierCode = supplierCode;
    return this;
  }

  /**
   * 
   * @return supplierCode
   */
  @javax.annotation.Nullable
  public String getSupplierCode() {
    return supplierCode;
  }

  public void setSupplierCode(String supplierCode) {
    this.supplierCode = supplierCode;
  }


  public SupplierWorkgroupSimpleVO supplierWorkgroupId(Long supplierWorkgroupId) {
    this.supplierWorkgroupId = supplierWorkgroupId;
    return this;
  }

  /**
   * 
   * @return supplierWorkgroupId
   */
  @javax.annotation.Nullable
  public Long getSupplierWorkgroupId() {
    return supplierWorkgroupId;
  }

  public void setSupplierWorkgroupId(Long supplierWorkgroupId) {
    this.supplierWorkgroupId = supplierWorkgroupId;
  }


  public SupplierWorkgroupSimpleVO supplierWorkgroupName(String supplierWorkgroupName) {
    this.supplierWorkgroupName = supplierWorkgroupName;
    return this;
  }

  /**
   * 
   * @return supplierWorkgroupName
   */
  @javax.annotation.Nullable
  public String getSupplierWorkgroupName() {
    return supplierWorkgroupName;
  }

  public void setSupplierWorkgroupName(String supplierWorkgroupName) {
    this.supplierWorkgroupName = supplierWorkgroupName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SupplierWorkgroupSimpleVO supplierWorkgroupSimpleVO = (SupplierWorkgroupSimpleVO) o;
    return Objects.equals(this.buSupplierWorkgroupId, supplierWorkgroupSimpleVO.buSupplierWorkgroupId) &&
        Objects.equals(this.buSupplierWorkgroupName, supplierWorkgroupSimpleVO.buSupplierWorkgroupName) &&
        Objects.equals(this.clientWorkgroupId, supplierWorkgroupSimpleVO.clientWorkgroupId) &&
        Objects.equals(this.clientWorkgroupName, supplierWorkgroupSimpleVO.clientWorkgroupName) &&
        Objects.equals(this.isApproved, supplierWorkgroupSimpleVO.isApproved) &&
        Objects.equals(this.supplierCode, supplierWorkgroupSimpleVO.supplierCode) &&
        Objects.equals(this.supplierWorkgroupId, supplierWorkgroupSimpleVO.supplierWorkgroupId) &&
        Objects.equals(this.supplierWorkgroupName, supplierWorkgroupSimpleVO.supplierWorkgroupName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(buSupplierWorkgroupId, buSupplierWorkgroupName, clientWorkgroupId, clientWorkgroupName, isApproved, supplierCode, supplierWorkgroupId, supplierWorkgroupName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SupplierWorkgroupSimpleVO {\n");
    sb.append("    buSupplierWorkgroupId: ").append(toIndentedString(buSupplierWorkgroupId)).append("\n");
    sb.append("    buSupplierWorkgroupName: ").append(toIndentedString(buSupplierWorkgroupName)).append("\n");
    sb.append("    clientWorkgroupId: ").append(toIndentedString(clientWorkgroupId)).append("\n");
    sb.append("    clientWorkgroupName: ").append(toIndentedString(clientWorkgroupName)).append("\n");
    sb.append("    isApproved: ").append(toIndentedString(isApproved)).append("\n");
    sb.append("    supplierCode: ").append(toIndentedString(supplierCode)).append("\n");
    sb.append("    supplierWorkgroupId: ").append(toIndentedString(supplierWorkgroupId)).append("\n");
    sb.append("    supplierWorkgroupName: ").append(toIndentedString(supplierWorkgroupName)).append("\n");
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
    openapiFields.add("bu_supplier_workgroup_id");
    openapiFields.add("bu_supplier_workgroup_name");
    openapiFields.add("client_workgroup_id");
    openapiFields.add("client_workgroup_name");
    openapiFields.add("is_approved");
    openapiFields.add("supplier_code");
    openapiFields.add("supplier_workgroup_id");
    openapiFields.add("supplier_workgroup_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SupplierWorkgroupSimpleVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SupplierWorkgroupSimpleVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SupplierWorkgroupSimpleVO is not found in the empty JSON string", SupplierWorkgroupSimpleVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SupplierWorkgroupSimpleVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SupplierWorkgroupSimpleVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("bu_supplier_workgroup_name") != null && !jsonObj.get("bu_supplier_workgroup_name").isJsonNull()) && !jsonObj.get("bu_supplier_workgroup_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bu_supplier_workgroup_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bu_supplier_workgroup_name").toString()));
      }
      if ((jsonObj.get("client_workgroup_name") != null && !jsonObj.get("client_workgroup_name").isJsonNull()) && !jsonObj.get("client_workgroup_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client_workgroup_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client_workgroup_name").toString()));
      }
      if ((jsonObj.get("supplier_code") != null && !jsonObj.get("supplier_code").isJsonNull()) && !jsonObj.get("supplier_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supplier_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supplier_code").toString()));
      }
      if ((jsonObj.get("supplier_workgroup_name") != null && !jsonObj.get("supplier_workgroup_name").isJsonNull()) && !jsonObj.get("supplier_workgroup_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supplier_workgroup_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supplier_workgroup_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SupplierWorkgroupSimpleVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SupplierWorkgroupSimpleVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SupplierWorkgroupSimpleVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SupplierWorkgroupSimpleVO.class));

       return (TypeAdapter<T>) new TypeAdapter<SupplierWorkgroupSimpleVO>() {
           @Override
           public void write(JsonWriter out, SupplierWorkgroupSimpleVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SupplierWorkgroupSimpleVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SupplierWorkgroupSimpleVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SupplierWorkgroupSimpleVO
   * @throws IOException if the JSON string is invalid with respect to SupplierWorkgroupSimpleVO
   */
  public static SupplierWorkgroupSimpleVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SupplierWorkgroupSimpleVO.class);
  }

  /**
   * Convert an instance of SupplierWorkgroupSimpleVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

