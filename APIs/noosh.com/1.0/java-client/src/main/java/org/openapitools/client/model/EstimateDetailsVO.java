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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.EstimateItemDetailsVO;
import org.openapitools.client.model.ProjectBaseVO;
import org.openapitools.client.model.PropertyPaAndAttVO;
import org.openapitools.client.model.RfeBaseVO;
import org.openapitools.client.model.WorkgroupBaseVO;

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
 * Java type: com.noosh.nooshapi.vo.EstimateDetailsVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EstimateDetailsVO {
  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_CREATE_DATE = "create_date";
  @SerializedName(SERIALIZED_NAME_CREATE_DATE)
  private LocalDate createDate;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<PropertyPaAndAttVO> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ESTIMATE_ID = "estimate_id";
  @SerializedName(SERIALIZED_NAME_ESTIMATE_ID)
  private Long estimateId;

  public static final String SERIALIZED_NAME_ESTIMATE_TITLE = "estimate_title";
  @SerializedName(SERIALIZED_NAME_ESTIMATE_TITLE)
  private String estimateTitle;

  public static final String SERIALIZED_NAME_EXPIRATION_DATE = "expiration_date";
  @SerializedName(SERIALIZED_NAME_EXPIRATION_DATE)
  private LocalDate expirationDate;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<EstimateItemDetailsVO> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROJECT = "project";
  @SerializedName(SERIALIZED_NAME_PROJECT)
  private ProjectBaseVO project;

  public static final String SERIALIZED_NAME_REFERENCE_NUMBER = "reference_number";
  @SerializedName(SERIALIZED_NAME_REFERENCE_NUMBER)
  private String referenceNumber;

  public static final String SERIALIZED_NAME_RFE = "rfe";
  @SerializedName(SERIALIZED_NAME_RFE)
  private RfeBaseVO rfe;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_SUBMIT_DATE = "submit_date";
  @SerializedName(SERIALIZED_NAME_SUBMIT_DATE)
  private LocalDate submitDate;

  public static final String SERIALIZED_NAME_SUBMITTED_BY = "submitted_by";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_BY)
  private String submittedBy;

  public static final String SERIALIZED_NAME_SUBMITTED_BY_USER_ID = "submitted_by_user_id";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_BY_USER_ID)
  private Long submittedByUserId;

  public static final String SERIALIZED_NAME_SUPPLIER_WORKGROUP = "supplier_workgroup";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_WORKGROUP)
  private WorkgroupBaseVO supplierWorkgroup;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_CURRENCY = "transactional_currency";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_CURRENCY)
  private String transactionalCurrency;

  public EstimateDetailsVO() {
  }

  public EstimateDetailsVO comments(String comments) {
    this.comments = comments;
    return this;
  }

  /**
   * 
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }

  public void setComments(String comments) {
    this.comments = comments;
  }


  public EstimateDetailsVO createDate(LocalDate createDate) {
    this.createDate = createDate;
    return this;
  }

  /**
   * 
   * @return createDate
   */
  @javax.annotation.Nullable
  public LocalDate getCreateDate() {
    return createDate;
  }

  public void setCreateDate(LocalDate createDate) {
    this.createDate = createDate;
  }


  public EstimateDetailsVO currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * 
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public EstimateDetailsVO customFields(List<PropertyPaAndAttVO> customFields) {
    this.customFields = customFields;
    return this;
  }

  public EstimateDetailsVO addCustomFieldsItem(PropertyPaAndAttVO customFieldsItem) {
    if (this.customFields == null) {
      this.customFields = new ArrayList<>();
    }
    this.customFields.add(customFieldsItem);
    return this;
  }

  /**
   * 
   * @return customFields
   */
  @javax.annotation.Nullable
  public List<PropertyPaAndAttVO> getCustomFields() {
    return customFields;
  }

  public void setCustomFields(List<PropertyPaAndAttVO> customFields) {
    this.customFields = customFields;
  }


  public EstimateDetailsVO description(String description) {
    this.description = description;
    return this;
  }

  /**
   * 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public EstimateDetailsVO estimateId(Long estimateId) {
    this.estimateId = estimateId;
    return this;
  }

  /**
   * 
   * @return estimateId
   */
  @javax.annotation.Nullable
  public Long getEstimateId() {
    return estimateId;
  }

  public void setEstimateId(Long estimateId) {
    this.estimateId = estimateId;
  }


  public EstimateDetailsVO estimateTitle(String estimateTitle) {
    this.estimateTitle = estimateTitle;
    return this;
  }

  /**
   * 
   * @return estimateTitle
   */
  @javax.annotation.Nullable
  public String getEstimateTitle() {
    return estimateTitle;
  }

  public void setEstimateTitle(String estimateTitle) {
    this.estimateTitle = estimateTitle;
  }


  public EstimateDetailsVO expirationDate(LocalDate expirationDate) {
    this.expirationDate = expirationDate;
    return this;
  }

  /**
   * 
   * @return expirationDate
   */
  @javax.annotation.Nullable
  public LocalDate getExpirationDate() {
    return expirationDate;
  }

  public void setExpirationDate(LocalDate expirationDate) {
    this.expirationDate = expirationDate;
  }


  public EstimateDetailsVO items(List<EstimateItemDetailsVO> items) {
    this.items = items;
    return this;
  }

  public EstimateDetailsVO addItemsItem(EstimateItemDetailsVO itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * 
   * @return items
   */
  @javax.annotation.Nullable
  public List<EstimateItemDetailsVO> getItems() {
    return items;
  }

  public void setItems(List<EstimateItemDetailsVO> items) {
    this.items = items;
  }


  public EstimateDetailsVO project(ProjectBaseVO project) {
    this.project = project;
    return this;
  }

  /**
   * Get project
   * @return project
   */
  @javax.annotation.Nullable
  public ProjectBaseVO getProject() {
    return project;
  }

  public void setProject(ProjectBaseVO project) {
    this.project = project;
  }


  public EstimateDetailsVO referenceNumber(String referenceNumber) {
    this.referenceNumber = referenceNumber;
    return this;
  }

  /**
   * 
   * @return referenceNumber
   */
  @javax.annotation.Nullable
  public String getReferenceNumber() {
    return referenceNumber;
  }

  public void setReferenceNumber(String referenceNumber) {
    this.referenceNumber = referenceNumber;
  }


  public EstimateDetailsVO rfe(RfeBaseVO rfe) {
    this.rfe = rfe;
    return this;
  }

  /**
   * Get rfe
   * @return rfe
   */
  @javax.annotation.Nullable
  public RfeBaseVO getRfe() {
    return rfe;
  }

  public void setRfe(RfeBaseVO rfe) {
    this.rfe = rfe;
  }


  public EstimateDetailsVO status(String status) {
    this.status = status;
    return this;
  }

  /**
   * 
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public EstimateDetailsVO submitDate(LocalDate submitDate) {
    this.submitDate = submitDate;
    return this;
  }

  /**
   * 
   * @return submitDate
   */
  @javax.annotation.Nullable
  public LocalDate getSubmitDate() {
    return submitDate;
  }

  public void setSubmitDate(LocalDate submitDate) {
    this.submitDate = submitDate;
  }


  public EstimateDetailsVO submittedBy(String submittedBy) {
    this.submittedBy = submittedBy;
    return this;
  }

  /**
   * 
   * @return submittedBy
   */
  @javax.annotation.Nullable
  public String getSubmittedBy() {
    return submittedBy;
  }

  public void setSubmittedBy(String submittedBy) {
    this.submittedBy = submittedBy;
  }


  public EstimateDetailsVO submittedByUserId(Long submittedByUserId) {
    this.submittedByUserId = submittedByUserId;
    return this;
  }

  /**
   * 
   * @return submittedByUserId
   */
  @javax.annotation.Nullable
  public Long getSubmittedByUserId() {
    return submittedByUserId;
  }

  public void setSubmittedByUserId(Long submittedByUserId) {
    this.submittedByUserId = submittedByUserId;
  }


  public EstimateDetailsVO supplierWorkgroup(WorkgroupBaseVO supplierWorkgroup) {
    this.supplierWorkgroup = supplierWorkgroup;
    return this;
  }

  /**
   * Get supplierWorkgroup
   * @return supplierWorkgroup
   */
  @javax.annotation.Nullable
  public WorkgroupBaseVO getSupplierWorkgroup() {
    return supplierWorkgroup;
  }

  public void setSupplierWorkgroup(WorkgroupBaseVO supplierWorkgroup) {
    this.supplierWorkgroup = supplierWorkgroup;
  }


  public EstimateDetailsVO transactionalCurrency(String transactionalCurrency) {
    this.transactionalCurrency = transactionalCurrency;
    return this;
  }

  /**
   * 
   * @return transactionalCurrency
   */
  @javax.annotation.Nullable
  public String getTransactionalCurrency() {
    return transactionalCurrency;
  }

  public void setTransactionalCurrency(String transactionalCurrency) {
    this.transactionalCurrency = transactionalCurrency;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EstimateDetailsVO estimateDetailsVO = (EstimateDetailsVO) o;
    return Objects.equals(this.comments, estimateDetailsVO.comments) &&
        Objects.equals(this.createDate, estimateDetailsVO.createDate) &&
        Objects.equals(this.currency, estimateDetailsVO.currency) &&
        Objects.equals(this.customFields, estimateDetailsVO.customFields) &&
        Objects.equals(this.description, estimateDetailsVO.description) &&
        Objects.equals(this.estimateId, estimateDetailsVO.estimateId) &&
        Objects.equals(this.estimateTitle, estimateDetailsVO.estimateTitle) &&
        Objects.equals(this.expirationDate, estimateDetailsVO.expirationDate) &&
        Objects.equals(this.items, estimateDetailsVO.items) &&
        Objects.equals(this.project, estimateDetailsVO.project) &&
        Objects.equals(this.referenceNumber, estimateDetailsVO.referenceNumber) &&
        Objects.equals(this.rfe, estimateDetailsVO.rfe) &&
        Objects.equals(this.status, estimateDetailsVO.status) &&
        Objects.equals(this.submitDate, estimateDetailsVO.submitDate) &&
        Objects.equals(this.submittedBy, estimateDetailsVO.submittedBy) &&
        Objects.equals(this.submittedByUserId, estimateDetailsVO.submittedByUserId) &&
        Objects.equals(this.supplierWorkgroup, estimateDetailsVO.supplierWorkgroup) &&
        Objects.equals(this.transactionalCurrency, estimateDetailsVO.transactionalCurrency);
  }

  @Override
  public int hashCode() {
    return Objects.hash(comments, createDate, currency, customFields, description, estimateId, estimateTitle, expirationDate, items, project, referenceNumber, rfe, status, submitDate, submittedBy, submittedByUserId, supplierWorkgroup, transactionalCurrency);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EstimateDetailsVO {\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    createDate: ").append(toIndentedString(createDate)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    estimateId: ").append(toIndentedString(estimateId)).append("\n");
    sb.append("    estimateTitle: ").append(toIndentedString(estimateTitle)).append("\n");
    sb.append("    expirationDate: ").append(toIndentedString(expirationDate)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
    sb.append("    referenceNumber: ").append(toIndentedString(referenceNumber)).append("\n");
    sb.append("    rfe: ").append(toIndentedString(rfe)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    submitDate: ").append(toIndentedString(submitDate)).append("\n");
    sb.append("    submittedBy: ").append(toIndentedString(submittedBy)).append("\n");
    sb.append("    submittedByUserId: ").append(toIndentedString(submittedByUserId)).append("\n");
    sb.append("    supplierWorkgroup: ").append(toIndentedString(supplierWorkgroup)).append("\n");
    sb.append("    transactionalCurrency: ").append(toIndentedString(transactionalCurrency)).append("\n");
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
    openapiFields.add("comments");
    openapiFields.add("create_date");
    openapiFields.add("currency");
    openapiFields.add("custom_fields");
    openapiFields.add("description");
    openapiFields.add("estimate_id");
    openapiFields.add("estimate_title");
    openapiFields.add("expiration_date");
    openapiFields.add("items");
    openapiFields.add("project");
    openapiFields.add("reference_number");
    openapiFields.add("rfe");
    openapiFields.add("status");
    openapiFields.add("submit_date");
    openapiFields.add("submitted_by");
    openapiFields.add("submitted_by_user_id");
    openapiFields.add("supplier_workgroup");
    openapiFields.add("transactional_currency");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EstimateDetailsVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EstimateDetailsVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EstimateDetailsVO is not found in the empty JSON string", EstimateDetailsVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EstimateDetailsVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EstimateDetailsVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (jsonObj.get("custom_fields") != null && !jsonObj.get("custom_fields").isJsonNull()) {
        JsonArray jsonArraycustomFields = jsonObj.getAsJsonArray("custom_fields");
        if (jsonArraycustomFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_fields` to be an array in the JSON string but got `%s`", jsonObj.get("custom_fields").toString()));
          }

          // validate the optional field `custom_fields` (array)
          for (int i = 0; i < jsonArraycustomFields.size(); i++) {
            PropertyPaAndAttVO.validateJsonElement(jsonArraycustomFields.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("estimate_title") != null && !jsonObj.get("estimate_title").isJsonNull()) && !jsonObj.get("estimate_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `estimate_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("estimate_title").toString()));
      }
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            EstimateItemDetailsVO.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      // validate the optional field `project`
      if (jsonObj.get("project") != null && !jsonObj.get("project").isJsonNull()) {
        ProjectBaseVO.validateJsonElement(jsonObj.get("project"));
      }
      if ((jsonObj.get("reference_number") != null && !jsonObj.get("reference_number").isJsonNull()) && !jsonObj.get("reference_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference_number").toString()));
      }
      // validate the optional field `rfe`
      if (jsonObj.get("rfe") != null && !jsonObj.get("rfe").isJsonNull()) {
        RfeBaseVO.validateJsonElement(jsonObj.get("rfe"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("submitted_by") != null && !jsonObj.get("submitted_by").isJsonNull()) && !jsonObj.get("submitted_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submitted_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submitted_by").toString()));
      }
      // validate the optional field `supplier_workgroup`
      if (jsonObj.get("supplier_workgroup") != null && !jsonObj.get("supplier_workgroup").isJsonNull()) {
        WorkgroupBaseVO.validateJsonElement(jsonObj.get("supplier_workgroup"));
      }
      if ((jsonObj.get("transactional_currency") != null && !jsonObj.get("transactional_currency").isJsonNull()) && !jsonObj.get("transactional_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactional_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactional_currency").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EstimateDetailsVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EstimateDetailsVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EstimateDetailsVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EstimateDetailsVO.class));

       return (TypeAdapter<T>) new TypeAdapter<EstimateDetailsVO>() {
           @Override
           public void write(JsonWriter out, EstimateDetailsVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EstimateDetailsVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EstimateDetailsVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EstimateDetailsVO
   * @throws IOException if the JSON string is invalid with respect to EstimateDetailsVO
   */
  public static EstimateDetailsVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EstimateDetailsVO.class);
  }

  /**
   * Convert an instance of EstimateDetailsVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

