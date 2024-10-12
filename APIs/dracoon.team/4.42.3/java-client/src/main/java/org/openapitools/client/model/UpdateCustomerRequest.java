/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
 * Request model for updating a customer
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateCustomerRequest {
  public static final String SERIALIZED_NAME_COMPANY_NAME = "companyName";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  /**
   * Customer type
   */
  @JsonAdapter(CustomerContractTypeEnum.Adapter.class)
  public enum CustomerContractTypeEnum {
    DEMO("demo"),
    
    FREE("free"),
    
    PAY("pay");

    private String value;

    CustomerContractTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CustomerContractTypeEnum fromValue(String value) {
      for (CustomerContractTypeEnum b : CustomerContractTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CustomerContractTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CustomerContractTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CustomerContractTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CustomerContractTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CustomerContractTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CUSTOMER_CONTRACT_TYPE = "customerContractType";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_CONTRACT_TYPE)
  private CustomerContractTypeEnum customerContractType;

  public static final String SERIALIZED_NAME_IS_LOCKED = "isLocked";
  @SerializedName(SERIALIZED_NAME_IS_LOCKED)
  private Boolean isLocked = false;

  public static final String SERIALIZED_NAME_LOCK_STATUS = "lockStatus";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_LOCK_STATUS)
  private Boolean lockStatus = false;

  public static final String SERIALIZED_NAME_PROVIDER_CUSTOMER_ID = "providerCustomerId";
  @SerializedName(SERIALIZED_NAME_PROVIDER_CUSTOMER_ID)
  private String providerCustomerId;

  public static final String SERIALIZED_NAME_QUOTA_MAX = "quotaMax";
  @SerializedName(SERIALIZED_NAME_QUOTA_MAX)
  private Long quotaMax;

  public static final String SERIALIZED_NAME_USER_MAX = "userMax";
  @SerializedName(SERIALIZED_NAME_USER_MAX)
  private Integer userMax;

  public static final String SERIALIZED_NAME_WEBHOOKS_MAX = "webhooksMax";
  @SerializedName(SERIALIZED_NAME_WEBHOOKS_MAX)
  private Long webhooksMax;

  public UpdateCustomerRequest() {
  }

  public UpdateCustomerRequest companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * Company name
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  public UpdateCustomerRequest customerContractType(CustomerContractTypeEnum customerContractType) {
    this.customerContractType = customerContractType;
    return this;
  }

  /**
   * Customer type
   * @return customerContractType
   */
  @javax.annotation.Nonnull
  public CustomerContractTypeEnum getCustomerContractType() {
    return customerContractType;
  }

  public void setCustomerContractType(CustomerContractTypeEnum customerContractType) {
    this.customerContractType = customerContractType;
  }


  public UpdateCustomerRequest isLocked(Boolean isLocked) {
    this.isLocked = isLocked;
    return this;
  }

  /**
   * Customer is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    All users of this customer will be blocked and can not login anymore.
   * @return isLocked
   */
  @javax.annotation.Nullable
  public Boolean getIsLocked() {
    return isLocked;
  }

  public void setIsLocked(Boolean isLocked) {
    this.isLocked = isLocked;
  }


  @Deprecated
  public UpdateCustomerRequest lockStatus(Boolean lockStatus) {
    this.lockStatus = lockStatus;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.7.0  Customer lock status:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    Please use &#x60;isLocked&#x60; instead.  All users of this customer will be blocked and can not login anymore.
   * @return lockStatus
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getLockStatus() {
    return lockStatus;
  }

  @Deprecated
  public void setLockStatus(Boolean lockStatus) {
    this.lockStatus = lockStatus;
  }


  public UpdateCustomerRequest providerCustomerId(String providerCustomerId) {
    this.providerCustomerId = providerCustomerId;
    return this;
  }

  /**
   * Provider customer ID
   * @return providerCustomerId
   */
  @javax.annotation.Nullable
  public String getProviderCustomerId() {
    return providerCustomerId;
  }

  public void setProviderCustomerId(String providerCustomerId) {
    this.providerCustomerId = providerCustomerId;
  }


  public UpdateCustomerRequest quotaMax(Long quotaMax) {
    this.quotaMax = quotaMax;
    return this;
  }

  /**
   * Maximal disc space which can be allocated by customer in bytes. -1 for unlimited
   * @return quotaMax
   */
  @javax.annotation.Nullable
  public Long getQuotaMax() {
    return quotaMax;
  }

  public void setQuotaMax(Long quotaMax) {
    this.quotaMax = quotaMax;
  }


  public UpdateCustomerRequest userMax(Integer userMax) {
    this.userMax = userMax;
    return this;
  }

  /**
   * Maximal number of users
   * @return userMax
   */
  @javax.annotation.Nullable
  public Integer getUserMax() {
    return userMax;
  }

  public void setUserMax(Integer userMax) {
    this.userMax = userMax;
  }


  public UpdateCustomerRequest webhooksMax(Long webhooksMax) {
    this.webhooksMax = webhooksMax;
    return this;
  }

  /**
   * &amp;#128640; Since v4.19.0  Maximal number of webhooks
   * @return webhooksMax
   */
  @javax.annotation.Nullable
  public Long getWebhooksMax() {
    return webhooksMax;
  }

  public void setWebhooksMax(Long webhooksMax) {
    this.webhooksMax = webhooksMax;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateCustomerRequest updateCustomerRequest = (UpdateCustomerRequest) o;
    return Objects.equals(this.companyName, updateCustomerRequest.companyName) &&
        Objects.equals(this.customerContractType, updateCustomerRequest.customerContractType) &&
        Objects.equals(this.isLocked, updateCustomerRequest.isLocked) &&
        Objects.equals(this.lockStatus, updateCustomerRequest.lockStatus) &&
        Objects.equals(this.providerCustomerId, updateCustomerRequest.providerCustomerId) &&
        Objects.equals(this.quotaMax, updateCustomerRequest.quotaMax) &&
        Objects.equals(this.userMax, updateCustomerRequest.userMax) &&
        Objects.equals(this.webhooksMax, updateCustomerRequest.webhooksMax);
  }

  @Override
  public int hashCode() {
    return Objects.hash(companyName, customerContractType, isLocked, lockStatus, providerCustomerId, quotaMax, userMax, webhooksMax);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateCustomerRequest {\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    customerContractType: ").append(toIndentedString(customerContractType)).append("\n");
    sb.append("    isLocked: ").append(toIndentedString(isLocked)).append("\n");
    sb.append("    lockStatus: ").append(toIndentedString(lockStatus)).append("\n");
    sb.append("    providerCustomerId: ").append(toIndentedString(providerCustomerId)).append("\n");
    sb.append("    quotaMax: ").append(toIndentedString(quotaMax)).append("\n");
    sb.append("    userMax: ").append(toIndentedString(userMax)).append("\n");
    sb.append("    webhooksMax: ").append(toIndentedString(webhooksMax)).append("\n");
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
    openapiFields.add("companyName");
    openapiFields.add("customerContractType");
    openapiFields.add("isLocked");
    openapiFields.add("lockStatus");
    openapiFields.add("providerCustomerId");
    openapiFields.add("quotaMax");
    openapiFields.add("userMax");
    openapiFields.add("webhooksMax");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("customerContractType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateCustomerRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateCustomerRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateCustomerRequest is not found in the empty JSON string", UpdateCustomerRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateCustomerRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateCustomerRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateCustomerRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("companyName") != null && !jsonObj.get("companyName").isJsonNull()) && !jsonObj.get("companyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `companyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("companyName").toString()));
      }
      if (!jsonObj.get("customerContractType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerContractType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerContractType").toString()));
      }
      // validate the required field `customerContractType`
      CustomerContractTypeEnum.validateJsonElement(jsonObj.get("customerContractType"));
      if ((jsonObj.get("providerCustomerId") != null && !jsonObj.get("providerCustomerId").isJsonNull()) && !jsonObj.get("providerCustomerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `providerCustomerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("providerCustomerId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateCustomerRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateCustomerRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateCustomerRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateCustomerRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateCustomerRequest>() {
           @Override
           public void write(JsonWriter out, UpdateCustomerRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateCustomerRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateCustomerRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateCustomerRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateCustomerRequest
   */
  public static UpdateCustomerRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateCustomerRequest.class);
  }

  /**
   * Convert an instance of UpdateCustomerRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

