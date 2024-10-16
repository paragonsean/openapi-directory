/*
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ObjectLink;

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
 * CriticalIllnessInsurancePolicyWithIdModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CriticalIllnessInsurancePolicyWithIdModel {
  public static final String SERIALIZED_NAME_BENEFIT = "benefit";
  @SerializedName(SERIALIZED_NAME_BENEFIT)
  private Double benefit;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private Integer frequency;

  public static final String SERIALIZED_NAME_INSURANCE_POLICY_ID = "insurancePolicyId";
  @SerializedName(SERIALIZED_NAME_INSURANCE_POLICY_ID)
  private Integer insurancePolicyId;

  /**
   * Gets or Sets insured
   */
  @JsonAdapter(InsuredEnum.Adapter.class)
  public enum InsuredEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient");

    private String value;

    InsuredEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static InsuredEnum fromValue(String value) {
      for (InsuredEnum b : InsuredEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<InsuredEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final InsuredEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public InsuredEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return InsuredEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      InsuredEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_INSURED = "insured";
  @SerializedName(SERIALIZED_NAME_INSURED)
  private InsuredEnum insured;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<ObjectLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_POLICY_TYPE = "policyType";
  @SerializedName(SERIALIZED_NAME_POLICY_TYPE)
  private Integer policyType;

  public static final String SERIALIZED_NAME_PREMIUM = "premium";
  @SerializedName(SERIALIZED_NAME_PREMIUM)
  private Double premium;

  public CriticalIllnessInsurancePolicyWithIdModel() {
  }

  public CriticalIllnessInsurancePolicyWithIdModel benefit(Double benefit) {
    this.benefit = benefit;
    return this;
  }

  /**
   * Get benefit
   * @return benefit
   */
  @javax.annotation.Nullable
  public Double getBenefit() {
    return benefit;
  }

  public void setBenefit(Double benefit) {
    this.benefit = benefit;
  }


  public CriticalIllnessInsurancePolicyWithIdModel description(String description) {
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


  public CriticalIllnessInsurancePolicyWithIdModel externalDestinationId(String externalDestinationId) {
    this.externalDestinationId = externalDestinationId;
    return this;
  }

  /**
   * Get externalDestinationId
   * @return externalDestinationId
   */
  @javax.annotation.Nullable
  public String getExternalDestinationId() {
    return externalDestinationId;
  }

  public void setExternalDestinationId(String externalDestinationId) {
    this.externalDestinationId = externalDestinationId;
  }


  public CriticalIllnessInsurancePolicyWithIdModel factFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
    return this;
  }

  /**
   * Get factFinderId
   * @return factFinderId
   */
  @javax.annotation.Nullable
  public Integer getFactFinderId() {
    return factFinderId;
  }

  public void setFactFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
  }


  public CriticalIllnessInsurancePolicyWithIdModel frequency(Integer frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Get frequency
   * @return frequency
   */
  @javax.annotation.Nullable
  public Integer getFrequency() {
    return frequency;
  }

  public void setFrequency(Integer frequency) {
    this.frequency = frequency;
  }


  public CriticalIllnessInsurancePolicyWithIdModel insurancePolicyId(Integer insurancePolicyId) {
    this.insurancePolicyId = insurancePolicyId;
    return this;
  }

  /**
   * Get insurancePolicyId
   * @return insurancePolicyId
   */
  @javax.annotation.Nullable
  public Integer getInsurancePolicyId() {
    return insurancePolicyId;
  }

  public void setInsurancePolicyId(Integer insurancePolicyId) {
    this.insurancePolicyId = insurancePolicyId;
  }


  public CriticalIllnessInsurancePolicyWithIdModel insured(InsuredEnum insured) {
    this.insured = insured;
    return this;
  }

  /**
   * Get insured
   * @return insured
   */
  @javax.annotation.Nullable
  public InsuredEnum getInsured() {
    return insured;
  }

  public void setInsured(InsuredEnum insured) {
    this.insured = insured;
  }


  public CriticalIllnessInsurancePolicyWithIdModel links(List<ObjectLink> links) {
    this.links = links;
    return this;
  }

  public CriticalIllnessInsurancePolicyWithIdModel addLinksItem(ObjectLink linksItem) {
    if (this.links == null) {
      this.links = new ArrayList<>();
    }
    this.links.add(linksItem);
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nullable
  public List<ObjectLink> getLinks() {
    return links;
  }

  public void setLinks(List<ObjectLink> links) {
    this.links = links;
  }


  public CriticalIllnessInsurancePolicyWithIdModel policyType(Integer policyType) {
    this.policyType = policyType;
    return this;
  }

  /**
   * Get policyType
   * @return policyType
   */
  @javax.annotation.Nullable
  public Integer getPolicyType() {
    return policyType;
  }

  public void setPolicyType(Integer policyType) {
    this.policyType = policyType;
  }


  public CriticalIllnessInsurancePolicyWithIdModel premium(Double premium) {
    this.premium = premium;
    return this;
  }

  /**
   * Get premium
   * @return premium
   */
  @javax.annotation.Nullable
  public Double getPremium() {
    return premium;
  }

  public void setPremium(Double premium) {
    this.premium = premium;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CriticalIllnessInsurancePolicyWithIdModel criticalIllnessInsurancePolicyWithIdModel = (CriticalIllnessInsurancePolicyWithIdModel) o;
    return Objects.equals(this.benefit, criticalIllnessInsurancePolicyWithIdModel.benefit) &&
        Objects.equals(this.description, criticalIllnessInsurancePolicyWithIdModel.description) &&
        Objects.equals(this.externalDestinationId, criticalIllnessInsurancePolicyWithIdModel.externalDestinationId) &&
        Objects.equals(this.factFinderId, criticalIllnessInsurancePolicyWithIdModel.factFinderId) &&
        Objects.equals(this.frequency, criticalIllnessInsurancePolicyWithIdModel.frequency) &&
        Objects.equals(this.insurancePolicyId, criticalIllnessInsurancePolicyWithIdModel.insurancePolicyId) &&
        Objects.equals(this.insured, criticalIllnessInsurancePolicyWithIdModel.insured) &&
        Objects.equals(this.links, criticalIllnessInsurancePolicyWithIdModel.links) &&
        Objects.equals(this.policyType, criticalIllnessInsurancePolicyWithIdModel.policyType) &&
        Objects.equals(this.premium, criticalIllnessInsurancePolicyWithIdModel.premium);
  }

  @Override
  public int hashCode() {
    return Objects.hash(benefit, description, externalDestinationId, factFinderId, frequency, insurancePolicyId, insured, links, policyType, premium);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CriticalIllnessInsurancePolicyWithIdModel {\n");
    sb.append("    benefit: ").append(toIndentedString(benefit)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    insurancePolicyId: ").append(toIndentedString(insurancePolicyId)).append("\n");
    sb.append("    insured: ").append(toIndentedString(insured)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    policyType: ").append(toIndentedString(policyType)).append("\n");
    sb.append("    premium: ").append(toIndentedString(premium)).append("\n");
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
    openapiFields.add("benefit");
    openapiFields.add("description");
    openapiFields.add("externalDestinationId");
    openapiFields.add("factFinderId");
    openapiFields.add("frequency");
    openapiFields.add("insurancePolicyId");
    openapiFields.add("insured");
    openapiFields.add("links");
    openapiFields.add("policyType");
    openapiFields.add("premium");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CriticalIllnessInsurancePolicyWithIdModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CriticalIllnessInsurancePolicyWithIdModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CriticalIllnessInsurancePolicyWithIdModel is not found in the empty JSON string", CriticalIllnessInsurancePolicyWithIdModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CriticalIllnessInsurancePolicyWithIdModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CriticalIllnessInsurancePolicyWithIdModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("externalDestinationId") != null && !jsonObj.get("externalDestinationId").isJsonNull()) && !jsonObj.get("externalDestinationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalDestinationId").toString()));
      }
      if ((jsonObj.get("insured") != null && !jsonObj.get("insured").isJsonNull()) && !jsonObj.get("insured").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insured` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insured").toString()));
      }
      // validate the optional field `insured`
      if (jsonObj.get("insured") != null && !jsonObj.get("insured").isJsonNull()) {
        InsuredEnum.validateJsonElement(jsonObj.get("insured"));
      }
      if (jsonObj.get("links") != null && !jsonObj.get("links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `links` to be an array in the JSON string but got `%s`", jsonObj.get("links").toString()));
          }

          // validate the optional field `links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            ObjectLink.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CriticalIllnessInsurancePolicyWithIdModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CriticalIllnessInsurancePolicyWithIdModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CriticalIllnessInsurancePolicyWithIdModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CriticalIllnessInsurancePolicyWithIdModel.class));

       return (TypeAdapter<T>) new TypeAdapter<CriticalIllnessInsurancePolicyWithIdModel>() {
           @Override
           public void write(JsonWriter out, CriticalIllnessInsurancePolicyWithIdModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CriticalIllnessInsurancePolicyWithIdModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CriticalIllnessInsurancePolicyWithIdModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CriticalIllnessInsurancePolicyWithIdModel
   * @throws IOException if the JSON string is invalid with respect to CriticalIllnessInsurancePolicyWithIdModel
   */
  public static CriticalIllnessInsurancePolicyWithIdModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CriticalIllnessInsurancePolicyWithIdModel.class);
  }

  /**
   * Convert an instance of CriticalIllnessInsurancePolicyWithIdModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

