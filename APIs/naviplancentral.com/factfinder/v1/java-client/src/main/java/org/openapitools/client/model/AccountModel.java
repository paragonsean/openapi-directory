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
 * AccountModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccountModel {
  public static final String SERIALIZED_NAME_ACCOUNT_TYPE = "accountType";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_TYPE)
  private Integer accountType;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_EXTERNAL_SOURCE_ID = "externalSourceId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_SOURCE_ID)
  private String externalSourceId;

  public static final String SERIALIZED_NAME_EXTERNAL_SOURCE_NAME = "externalSourceName";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_SOURCE_NAME)
  private String externalSourceName;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_LAST_UPDATED = "lastUpdated";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED)
  private OffsetDateTime lastUpdated;

  public static final String SERIALIZED_NAME_MARKET_VALUE = "marketValue";
  @SerializedName(SERIALIZED_NAME_MARKET_VALUE)
  private Double marketValue;

  /**
   * Gets or Sets owner
   */
  @JsonAdapter(OwnerEnum.Adapter.class)
  public enum OwnerEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient"),
    
    JOINT("Joint"),
    
    DEPENDENT("Dependent"),
    
    OTHER("Other");

    private String value;

    OwnerEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OwnerEnum fromValue(String value) {
      for (OwnerEnum b : OwnerEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OwnerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OwnerEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OwnerEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OwnerEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OwnerEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private OwnerEnum owner;

  public static final String SERIALIZED_NAME_OWNER_DEPENDENT_ID = "ownerDependentId";
  @SerializedName(SERIALIZED_NAME_OWNER_DEPENDENT_ID)
  private Integer ownerDependentId;

  public AccountModel() {
  }

  public AccountModel accountType(Integer accountType) {
    this.accountType = accountType;
    return this;
  }

  /**
   * Get accountType
   * @return accountType
   */
  @javax.annotation.Nullable
  public Integer getAccountType() {
    return accountType;
  }

  public void setAccountType(Integer accountType) {
    this.accountType = accountType;
  }


  public AccountModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AccountModel externalDestinationId(String externalDestinationId) {
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


  public AccountModel externalSourceId(String externalSourceId) {
    this.externalSourceId = externalSourceId;
    return this;
  }

  /**
   * Get externalSourceId
   * @return externalSourceId
   */
  @javax.annotation.Nullable
  public String getExternalSourceId() {
    return externalSourceId;
  }

  public void setExternalSourceId(String externalSourceId) {
    this.externalSourceId = externalSourceId;
  }


  public AccountModel externalSourceName(String externalSourceName) {
    this.externalSourceName = externalSourceName;
    return this;
  }

  /**
   * Get externalSourceName
   * @return externalSourceName
   */
  @javax.annotation.Nullable
  public String getExternalSourceName() {
    return externalSourceName;
  }

  public void setExternalSourceName(String externalSourceName) {
    this.externalSourceName = externalSourceName;
  }


  public AccountModel factFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
    return this;
  }

  /**
   * Get factFinderId
   * @return factFinderId
   */
  @javax.annotation.Nonnull
  public Integer getFactFinderId() {
    return factFinderId;
  }

  public void setFactFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
  }


  public AccountModel lastUpdated(OffsetDateTime lastUpdated) {
    this.lastUpdated = lastUpdated;
    return this;
  }

  /**
   * Get lastUpdated
   * @return lastUpdated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastUpdated() {
    return lastUpdated;
  }

  public void setLastUpdated(OffsetDateTime lastUpdated) {
    this.lastUpdated = lastUpdated;
  }


  public AccountModel marketValue(Double marketValue) {
    this.marketValue = marketValue;
    return this;
  }

  /**
   * Get marketValue
   * @return marketValue
   */
  @javax.annotation.Nullable
  public Double getMarketValue() {
    return marketValue;
  }

  public void setMarketValue(Double marketValue) {
    this.marketValue = marketValue;
  }


  public AccountModel owner(OwnerEnum owner) {
    this.owner = owner;
    return this;
  }

  /**
   * Get owner
   * @return owner
   */
  @javax.annotation.Nullable
  public OwnerEnum getOwner() {
    return owner;
  }

  public void setOwner(OwnerEnum owner) {
    this.owner = owner;
  }


  public AccountModel ownerDependentId(Integer ownerDependentId) {
    this.ownerDependentId = ownerDependentId;
    return this;
  }

  /**
   * Get ownerDependentId
   * @return ownerDependentId
   */
  @javax.annotation.Nullable
  public Integer getOwnerDependentId() {
    return ownerDependentId;
  }

  public void setOwnerDependentId(Integer ownerDependentId) {
    this.ownerDependentId = ownerDependentId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccountModel accountModel = (AccountModel) o;
    return Objects.equals(this.accountType, accountModel.accountType) &&
        Objects.equals(this.description, accountModel.description) &&
        Objects.equals(this.externalDestinationId, accountModel.externalDestinationId) &&
        Objects.equals(this.externalSourceId, accountModel.externalSourceId) &&
        Objects.equals(this.externalSourceName, accountModel.externalSourceName) &&
        Objects.equals(this.factFinderId, accountModel.factFinderId) &&
        Objects.equals(this.lastUpdated, accountModel.lastUpdated) &&
        Objects.equals(this.marketValue, accountModel.marketValue) &&
        Objects.equals(this.owner, accountModel.owner) &&
        Objects.equals(this.ownerDependentId, accountModel.ownerDependentId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountType, description, externalDestinationId, externalSourceId, externalSourceName, factFinderId, lastUpdated, marketValue, owner, ownerDependentId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccountModel {\n");
    sb.append("    accountType: ").append(toIndentedString(accountType)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    externalSourceId: ").append(toIndentedString(externalSourceId)).append("\n");
    sb.append("    externalSourceName: ").append(toIndentedString(externalSourceName)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    lastUpdated: ").append(toIndentedString(lastUpdated)).append("\n");
    sb.append("    marketValue: ").append(toIndentedString(marketValue)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    ownerDependentId: ").append(toIndentedString(ownerDependentId)).append("\n");
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
    openapiFields.add("accountType");
    openapiFields.add("description");
    openapiFields.add("externalDestinationId");
    openapiFields.add("externalSourceId");
    openapiFields.add("externalSourceName");
    openapiFields.add("factFinderId");
    openapiFields.add("lastUpdated");
    openapiFields.add("marketValue");
    openapiFields.add("owner");
    openapiFields.add("ownerDependentId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("factFinderId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccountModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccountModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccountModel is not found in the empty JSON string", AccountModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccountModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccountModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AccountModel.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("externalDestinationId") != null && !jsonObj.get("externalDestinationId").isJsonNull()) && !jsonObj.get("externalDestinationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalDestinationId").toString()));
      }
      if ((jsonObj.get("externalSourceId") != null && !jsonObj.get("externalSourceId").isJsonNull()) && !jsonObj.get("externalSourceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalSourceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalSourceId").toString()));
      }
      if ((jsonObj.get("externalSourceName") != null && !jsonObj.get("externalSourceName").isJsonNull()) && !jsonObj.get("externalSourceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalSourceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalSourceName").toString()));
      }
      if ((jsonObj.get("owner") != null && !jsonObj.get("owner").isJsonNull()) && !jsonObj.get("owner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner").toString()));
      }
      // validate the optional field `owner`
      if (jsonObj.get("owner") != null && !jsonObj.get("owner").isJsonNull()) {
        OwnerEnum.validateJsonElement(jsonObj.get("owner"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccountModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccountModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccountModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccountModel.class));

       return (TypeAdapter<T>) new TypeAdapter<AccountModel>() {
           @Override
           public void write(JsonWriter out, AccountModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccountModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccountModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccountModel
   * @throws IOException if the JSON string is invalid with respect to AccountModel
   */
  public static AccountModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccountModel.class);
  }

  /**
   * Convert an instance of AccountModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

