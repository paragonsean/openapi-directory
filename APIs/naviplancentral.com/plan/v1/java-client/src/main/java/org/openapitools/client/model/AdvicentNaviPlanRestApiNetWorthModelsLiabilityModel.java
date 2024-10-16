/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.AdvicentNaviPlanRestApiModelsOwnerModel;

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
 * AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private OffsetDateTime endDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LEGACY_ID = "legacyId";
  @SerializedName(SERIALIZED_NAME_LEGACY_ID)
  private String legacyId;

  public static final String SERIALIZED_NAME_OUTSTANDING_PRINCIPAL = "outstandingPrincipal";
  @SerializedName(SERIALIZED_NAME_OUTSTANDING_PRINCIPAL)
  private Double outstandingPrincipal;

  public static final String SERIALIZED_NAME_OUTSTANDING_PRINCIPAL_AS_OF_DATE = "outstandingPrincipalAsOfDate";
  @SerializedName(SERIALIZED_NAME_OUTSTANDING_PRINCIPAL_AS_OF_DATE)
  private OffsetDateTime outstandingPrincipalAsOfDate;

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private AdvicentNaviPlanRestApiModelsOwnerModel owner;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private Integer type;

  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel() {
  }

  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel endDate(OffsetDateTime endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndDate() {
    return endDate;
  }

  public void setEndDate(OffsetDateTime endDate) {
    this.endDate = endDate;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel legacyId(String legacyId) {
    this.legacyId = legacyId;
    return this;
  }

  /**
   * Get legacyId
   * @return legacyId
   */
  @javax.annotation.Nullable
  public String getLegacyId() {
    return legacyId;
  }

  public void setLegacyId(String legacyId) {
    this.legacyId = legacyId;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel outstandingPrincipal(Double outstandingPrincipal) {
    this.outstandingPrincipal = outstandingPrincipal;
    return this;
  }

  /**
   * Get outstandingPrincipal
   * @return outstandingPrincipal
   */
  @javax.annotation.Nullable
  public Double getOutstandingPrincipal() {
    return outstandingPrincipal;
  }

  public void setOutstandingPrincipal(Double outstandingPrincipal) {
    this.outstandingPrincipal = outstandingPrincipal;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel outstandingPrincipalAsOfDate(OffsetDateTime outstandingPrincipalAsOfDate) {
    this.outstandingPrincipalAsOfDate = outstandingPrincipalAsOfDate;
    return this;
  }

  /**
   * Get outstandingPrincipalAsOfDate
   * @return outstandingPrincipalAsOfDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getOutstandingPrincipalAsOfDate() {
    return outstandingPrincipalAsOfDate;
  }

  public void setOutstandingPrincipalAsOfDate(OffsetDateTime outstandingPrincipalAsOfDate) {
    this.outstandingPrincipalAsOfDate = outstandingPrincipalAsOfDate;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel owner(AdvicentNaviPlanRestApiModelsOwnerModel owner) {
    this.owner = owner;
    return this;
  }

  /**
   * Get owner
   * @return owner
   */
  @javax.annotation.Nullable
  public AdvicentNaviPlanRestApiModelsOwnerModel getOwner() {
    return owner;
  }

  public void setOwner(AdvicentNaviPlanRestApiModelsOwnerModel owner) {
    this.owner = owner;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel startDate(OffsetDateTime startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartDate() {
    return startDate;
  }

  public void setStartDate(OffsetDateTime startDate) {
    this.startDate = startDate;
  }


  public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel type(Integer type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public Integer getType() {
    return type;
  }

  public void setType(Integer type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel advicentNaviPlanRestApiNetWorthModelsLiabilityModel = (AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel) o;
    return Objects.equals(this.description, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.description) &&
        Objects.equals(this.endDate, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.endDate) &&
        Objects.equals(this.id, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.id) &&
        Objects.equals(this.legacyId, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.legacyId) &&
        Objects.equals(this.outstandingPrincipal, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.outstandingPrincipal) &&
        Objects.equals(this.outstandingPrincipalAsOfDate, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.outstandingPrincipalAsOfDate) &&
        Objects.equals(this.owner, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.owner) &&
        Objects.equals(this.startDate, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.startDate) &&
        Objects.equals(this.type, advicentNaviPlanRestApiNetWorthModelsLiabilityModel.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, endDate, id, legacyId, outstandingPrincipal, outstandingPrincipalAsOfDate, owner, startDate, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    legacyId: ").append(toIndentedString(legacyId)).append("\n");
    sb.append("    outstandingPrincipal: ").append(toIndentedString(outstandingPrincipal)).append("\n");
    sb.append("    outstandingPrincipalAsOfDate: ").append(toIndentedString(outstandingPrincipalAsOfDate)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("endDate");
    openapiFields.add("id");
    openapiFields.add("legacyId");
    openapiFields.add("outstandingPrincipal");
    openapiFields.add("outstandingPrincipalAsOfDate");
    openapiFields.add("owner");
    openapiFields.add("startDate");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel is not found in the empty JSON string", AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("legacyId") != null && !jsonObj.get("legacyId").isJsonNull()) && !jsonObj.get("legacyId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `legacyId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("legacyId").toString()));
      }
      // validate the optional field `owner`
      if (jsonObj.get("owner") != null && !jsonObj.get("owner").isJsonNull()) {
        AdvicentNaviPlanRestApiModelsOwnerModel.validateJsonElement(jsonObj.get("owner"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.class));

       return (TypeAdapter<T>) new TypeAdapter<AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel>() {
           @Override
           public void write(JsonWriter out, AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel
   * @throws IOException if the JSON string is invalid with respect to AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel
   */
  public static AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.class);
  }

  /**
   * Convert an instance of AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

