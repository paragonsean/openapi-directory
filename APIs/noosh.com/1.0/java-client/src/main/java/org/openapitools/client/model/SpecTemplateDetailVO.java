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
import org.openapitools.client.model.PersonVO;
import org.openapitools.client.model.ProductTypeVO;
import org.openapitools.client.model.SpecTypeVO;

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
 * Java type: com.noosh.nooshapi.vo.SpecTemplateDetailVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SpecTemplateDetailVO {
  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private PersonVO createdBy;

  public static final String SERIALIZED_NAME_CREATED_DATE = "created_date";
  @SerializedName(SERIALIZED_NAME_CREATED_DATE)
  private LocalDate createdDate;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_EXTERNALLY_PUBLISHED = "is_externally_published";
  @SerializedName(SERIALIZED_NAME_IS_EXTERNALLY_PUBLISHED)
  private Boolean isExternallyPublished;

  public static final String SERIALIZED_NAME_IS_LOCKED = "is_locked";
  @SerializedName(SERIALIZED_NAME_IS_LOCKED)
  private Boolean isLocked;

  public static final String SERIALIZED_NAME_LAST_UPDATED_DATE = "last_updated_date";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED_DATE)
  private LocalDate lastUpdatedDate;

  public static final String SERIALIZED_NAME_PRODUCT_TYPE = "product_type";
  @SerializedName(SERIALIZED_NAME_PRODUCT_TYPE)
  private String productType;

  public static final String SERIALIZED_NAME_PRODUCT_TYPE_INFO = "product_type_info";
  @SerializedName(SERIALIZED_NAME_PRODUCT_TYPE_INFO)
  private ProductTypeVO productTypeInfo;

  public static final String SERIALIZED_NAME_SPEC_TEMPLATE_ID = "spec_template_id";
  @SerializedName(SERIALIZED_NAME_SPEC_TEMPLATE_ID)
  private Long specTemplateId;

  public static final String SERIALIZED_NAME_SPEC_TEMPLATE_NAME = "spec_template_name";
  @SerializedName(SERIALIZED_NAME_SPEC_TEMPLATE_NAME)
  private String specTemplateName;

  public static final String SERIALIZED_NAME_SPEC_TYPE = "spec_type";
  @SerializedName(SERIALIZED_NAME_SPEC_TYPE)
  private SpecTypeVO specType;

  public SpecTemplateDetailVO() {
  }

  public SpecTemplateDetailVO createdBy(PersonVO createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * Get createdBy
   * @return createdBy
   */
  @javax.annotation.Nullable
  public PersonVO getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(PersonVO createdBy) {
    this.createdBy = createdBy;
  }


  public SpecTemplateDetailVO createdDate(LocalDate createdDate) {
    this.createdDate = createdDate;
    return this;
  }

  /**
   * 
   * @return createdDate
   */
  @javax.annotation.Nullable
  public LocalDate getCreatedDate() {
    return createdDate;
  }

  public void setCreatedDate(LocalDate createdDate) {
    this.createdDate = createdDate;
  }


  public SpecTemplateDetailVO isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * 
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public SpecTemplateDetailVO isExternallyPublished(Boolean isExternallyPublished) {
    this.isExternallyPublished = isExternallyPublished;
    return this;
  }

  /**
   * 
   * @return isExternallyPublished
   */
  @javax.annotation.Nullable
  public Boolean getIsExternallyPublished() {
    return isExternallyPublished;
  }

  public void setIsExternallyPublished(Boolean isExternallyPublished) {
    this.isExternallyPublished = isExternallyPublished;
  }


  public SpecTemplateDetailVO isLocked(Boolean isLocked) {
    this.isLocked = isLocked;
    return this;
  }

  /**
   * 
   * @return isLocked
   */
  @javax.annotation.Nullable
  public Boolean getIsLocked() {
    return isLocked;
  }

  public void setIsLocked(Boolean isLocked) {
    this.isLocked = isLocked;
  }


  public SpecTemplateDetailVO lastUpdatedDate(LocalDate lastUpdatedDate) {
    this.lastUpdatedDate = lastUpdatedDate;
    return this;
  }

  /**
   * 
   * @return lastUpdatedDate
   */
  @javax.annotation.Nullable
  public LocalDate getLastUpdatedDate() {
    return lastUpdatedDate;
  }

  public void setLastUpdatedDate(LocalDate lastUpdatedDate) {
    this.lastUpdatedDate = lastUpdatedDate;
  }


  public SpecTemplateDetailVO productType(String productType) {
    this.productType = productType;
    return this;
  }

  /**
   * 
   * @return productType
   */
  @javax.annotation.Nullable
  public String getProductType() {
    return productType;
  }

  public void setProductType(String productType) {
    this.productType = productType;
  }


  public SpecTemplateDetailVO productTypeInfo(ProductTypeVO productTypeInfo) {
    this.productTypeInfo = productTypeInfo;
    return this;
  }

  /**
   * Get productTypeInfo
   * @return productTypeInfo
   */
  @javax.annotation.Nullable
  public ProductTypeVO getProductTypeInfo() {
    return productTypeInfo;
  }

  public void setProductTypeInfo(ProductTypeVO productTypeInfo) {
    this.productTypeInfo = productTypeInfo;
  }


  public SpecTemplateDetailVO specTemplateId(Long specTemplateId) {
    this.specTemplateId = specTemplateId;
    return this;
  }

  /**
   * 
   * @return specTemplateId
   */
  @javax.annotation.Nullable
  public Long getSpecTemplateId() {
    return specTemplateId;
  }

  public void setSpecTemplateId(Long specTemplateId) {
    this.specTemplateId = specTemplateId;
  }


  public SpecTemplateDetailVO specTemplateName(String specTemplateName) {
    this.specTemplateName = specTemplateName;
    return this;
  }

  /**
   * 
   * @return specTemplateName
   */
  @javax.annotation.Nullable
  public String getSpecTemplateName() {
    return specTemplateName;
  }

  public void setSpecTemplateName(String specTemplateName) {
    this.specTemplateName = specTemplateName;
  }


  public SpecTemplateDetailVO specType(SpecTypeVO specType) {
    this.specType = specType;
    return this;
  }

  /**
   * Get specType
   * @return specType
   */
  @javax.annotation.Nullable
  public SpecTypeVO getSpecType() {
    return specType;
  }

  public void setSpecType(SpecTypeVO specType) {
    this.specType = specType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SpecTemplateDetailVO specTemplateDetailVO = (SpecTemplateDetailVO) o;
    return Objects.equals(this.createdBy, specTemplateDetailVO.createdBy) &&
        Objects.equals(this.createdDate, specTemplateDetailVO.createdDate) &&
        Objects.equals(this.isActive, specTemplateDetailVO.isActive) &&
        Objects.equals(this.isExternallyPublished, specTemplateDetailVO.isExternallyPublished) &&
        Objects.equals(this.isLocked, specTemplateDetailVO.isLocked) &&
        Objects.equals(this.lastUpdatedDate, specTemplateDetailVO.lastUpdatedDate) &&
        Objects.equals(this.productType, specTemplateDetailVO.productType) &&
        Objects.equals(this.productTypeInfo, specTemplateDetailVO.productTypeInfo) &&
        Objects.equals(this.specTemplateId, specTemplateDetailVO.specTemplateId) &&
        Objects.equals(this.specTemplateName, specTemplateDetailVO.specTemplateName) &&
        Objects.equals(this.specType, specTemplateDetailVO.specType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdBy, createdDate, isActive, isExternallyPublished, isLocked, lastUpdatedDate, productType, productTypeInfo, specTemplateId, specTemplateName, specType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SpecTemplateDetailVO {\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    createdDate: ").append(toIndentedString(createdDate)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isExternallyPublished: ").append(toIndentedString(isExternallyPublished)).append("\n");
    sb.append("    isLocked: ").append(toIndentedString(isLocked)).append("\n");
    sb.append("    lastUpdatedDate: ").append(toIndentedString(lastUpdatedDate)).append("\n");
    sb.append("    productType: ").append(toIndentedString(productType)).append("\n");
    sb.append("    productTypeInfo: ").append(toIndentedString(productTypeInfo)).append("\n");
    sb.append("    specTemplateId: ").append(toIndentedString(specTemplateId)).append("\n");
    sb.append("    specTemplateName: ").append(toIndentedString(specTemplateName)).append("\n");
    sb.append("    specType: ").append(toIndentedString(specType)).append("\n");
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
    openapiFields.add("created_by");
    openapiFields.add("created_date");
    openapiFields.add("is_active");
    openapiFields.add("is_externally_published");
    openapiFields.add("is_locked");
    openapiFields.add("last_updated_date");
    openapiFields.add("product_type");
    openapiFields.add("product_type_info");
    openapiFields.add("spec_template_id");
    openapiFields.add("spec_template_name");
    openapiFields.add("spec_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SpecTemplateDetailVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SpecTemplateDetailVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SpecTemplateDetailVO is not found in the empty JSON string", SpecTemplateDetailVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SpecTemplateDetailVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SpecTemplateDetailVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `created_by`
      if (jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) {
        PersonVO.validateJsonElement(jsonObj.get("created_by"));
      }
      if ((jsonObj.get("product_type") != null && !jsonObj.get("product_type").isJsonNull()) && !jsonObj.get("product_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `product_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("product_type").toString()));
      }
      // validate the optional field `product_type_info`
      if (jsonObj.get("product_type_info") != null && !jsonObj.get("product_type_info").isJsonNull()) {
        ProductTypeVO.validateJsonElement(jsonObj.get("product_type_info"));
      }
      if ((jsonObj.get("spec_template_name") != null && !jsonObj.get("spec_template_name").isJsonNull()) && !jsonObj.get("spec_template_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `spec_template_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("spec_template_name").toString()));
      }
      // validate the optional field `spec_type`
      if (jsonObj.get("spec_type") != null && !jsonObj.get("spec_type").isJsonNull()) {
        SpecTypeVO.validateJsonElement(jsonObj.get("spec_type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SpecTemplateDetailVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SpecTemplateDetailVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SpecTemplateDetailVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SpecTemplateDetailVO.class));

       return (TypeAdapter<T>) new TypeAdapter<SpecTemplateDetailVO>() {
           @Override
           public void write(JsonWriter out, SpecTemplateDetailVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SpecTemplateDetailVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SpecTemplateDetailVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SpecTemplateDetailVO
   * @throws IOException if the JSON string is invalid with respect to SpecTemplateDetailVO
   */
  public static SpecTemplateDetailVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SpecTemplateDetailVO.class);
  }

  /**
   * Convert an instance of SpecTemplateDetailVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

