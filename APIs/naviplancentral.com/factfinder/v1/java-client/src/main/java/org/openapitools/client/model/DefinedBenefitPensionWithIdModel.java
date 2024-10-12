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
import java.time.OffsetDateTime;
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
 * DefinedBenefitPensionWithIdModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DefinedBenefitPensionWithIdModel {
  public static final String SERIALIZED_NAME_DEFINED_BENEFIT_PENSION_ID = "definedBenefitPensionId";
  @SerializedName(SERIALIZED_NAME_DEFINED_BENEFIT_PENSION_ID)
  private Integer definedBenefitPensionId;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ESTIMATED_AMOUNT = "estimatedAmount";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_AMOUNT)
  private Double estimatedAmount;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<ObjectLink> links = new ArrayList<>();

  /**
   * Gets or Sets member
   */
  @JsonAdapter(MemberEnum.Adapter.class)
  public enum MemberEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient");

    private String value;

    MemberEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MemberEnum fromValue(String value) {
      for (MemberEnum b : MemberEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MemberEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MemberEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MemberEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MemberEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MemberEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MEMBER = "member";
  @SerializedName(SERIALIZED_NAME_MEMBER)
  private MemberEnum member;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public DefinedBenefitPensionWithIdModel() {
  }

  public DefinedBenefitPensionWithIdModel definedBenefitPensionId(Integer definedBenefitPensionId) {
    this.definedBenefitPensionId = definedBenefitPensionId;
    return this;
  }

  /**
   * Get definedBenefitPensionId
   * @return definedBenefitPensionId
   */
  @javax.annotation.Nullable
  public Integer getDefinedBenefitPensionId() {
    return definedBenefitPensionId;
  }

  public void setDefinedBenefitPensionId(Integer definedBenefitPensionId) {
    this.definedBenefitPensionId = definedBenefitPensionId;
  }


  public DefinedBenefitPensionWithIdModel description(String description) {
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


  public DefinedBenefitPensionWithIdModel estimatedAmount(Double estimatedAmount) {
    this.estimatedAmount = estimatedAmount;
    return this;
  }

  /**
   * Get estimatedAmount
   * @return estimatedAmount
   */
  @javax.annotation.Nullable
  public Double getEstimatedAmount() {
    return estimatedAmount;
  }

  public void setEstimatedAmount(Double estimatedAmount) {
    this.estimatedAmount = estimatedAmount;
  }


  public DefinedBenefitPensionWithIdModel externalDestinationId(String externalDestinationId) {
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


  public DefinedBenefitPensionWithIdModel factFinderId(Integer factFinderId) {
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


  public DefinedBenefitPensionWithIdModel links(List<ObjectLink> links) {
    this.links = links;
    return this;
  }

  public DefinedBenefitPensionWithIdModel addLinksItem(ObjectLink linksItem) {
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


  public DefinedBenefitPensionWithIdModel member(MemberEnum member) {
    this.member = member;
    return this;
  }

  /**
   * Get member
   * @return member
   */
  @javax.annotation.Nullable
  public MemberEnum getMember() {
    return member;
  }

  public void setMember(MemberEnum member) {
    this.member = member;
  }


  public DefinedBenefitPensionWithIdModel startDate(OffsetDateTime startDate) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DefinedBenefitPensionWithIdModel definedBenefitPensionWithIdModel = (DefinedBenefitPensionWithIdModel) o;
    return Objects.equals(this.definedBenefitPensionId, definedBenefitPensionWithIdModel.definedBenefitPensionId) &&
        Objects.equals(this.description, definedBenefitPensionWithIdModel.description) &&
        Objects.equals(this.estimatedAmount, definedBenefitPensionWithIdModel.estimatedAmount) &&
        Objects.equals(this.externalDestinationId, definedBenefitPensionWithIdModel.externalDestinationId) &&
        Objects.equals(this.factFinderId, definedBenefitPensionWithIdModel.factFinderId) &&
        Objects.equals(this.links, definedBenefitPensionWithIdModel.links) &&
        Objects.equals(this.member, definedBenefitPensionWithIdModel.member) &&
        Objects.equals(this.startDate, definedBenefitPensionWithIdModel.startDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(definedBenefitPensionId, description, estimatedAmount, externalDestinationId, factFinderId, links, member, startDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DefinedBenefitPensionWithIdModel {\n");
    sb.append("    definedBenefitPensionId: ").append(toIndentedString(definedBenefitPensionId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    estimatedAmount: ").append(toIndentedString(estimatedAmount)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    member: ").append(toIndentedString(member)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
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
    openapiFields.add("definedBenefitPensionId");
    openapiFields.add("description");
    openapiFields.add("estimatedAmount");
    openapiFields.add("externalDestinationId");
    openapiFields.add("factFinderId");
    openapiFields.add("links");
    openapiFields.add("member");
    openapiFields.add("startDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DefinedBenefitPensionWithIdModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DefinedBenefitPensionWithIdModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DefinedBenefitPensionWithIdModel is not found in the empty JSON string", DefinedBenefitPensionWithIdModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DefinedBenefitPensionWithIdModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DefinedBenefitPensionWithIdModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("externalDestinationId") != null && !jsonObj.get("externalDestinationId").isJsonNull()) && !jsonObj.get("externalDestinationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalDestinationId").toString()));
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
      if ((jsonObj.get("member") != null && !jsonObj.get("member").isJsonNull()) && !jsonObj.get("member").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `member` to be a primitive type in the JSON string but got `%s`", jsonObj.get("member").toString()));
      }
      // validate the optional field `member`
      if (jsonObj.get("member") != null && !jsonObj.get("member").isJsonNull()) {
        MemberEnum.validateJsonElement(jsonObj.get("member"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DefinedBenefitPensionWithIdModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DefinedBenefitPensionWithIdModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DefinedBenefitPensionWithIdModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DefinedBenefitPensionWithIdModel.class));

       return (TypeAdapter<T>) new TypeAdapter<DefinedBenefitPensionWithIdModel>() {
           @Override
           public void write(JsonWriter out, DefinedBenefitPensionWithIdModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DefinedBenefitPensionWithIdModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DefinedBenefitPensionWithIdModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DefinedBenefitPensionWithIdModel
   * @throws IOException if the JSON string is invalid with respect to DefinedBenefitPensionWithIdModel
   */
  public static DefinedBenefitPensionWithIdModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DefinedBenefitPensionWithIdModel.class);
  }

  /**
   * Convert an instance of DefinedBenefitPensionWithIdModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

