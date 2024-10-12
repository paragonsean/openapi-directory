/*
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
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
import java.util.UUID;
import org.openapitools.client.model.ConsentArtefactResponseConsentConsentDetailCareContextsInner;
import org.openapitools.client.model.ConsentArtefactResponseConsentConsentDetailConsentManager;
import org.openapitools.client.model.ConsentArtefactResponseConsentConsentDetailHip;
import org.openapitools.client.model.ConsentArtefactResponseConsentConsentDetailHiu;
import org.openapitools.client.model.ConsentManagerPatientID;
import org.openapitools.client.model.HITypeEnum;
import org.openapitools.client.model.Permission;
import org.openapitools.client.model.Requester;
import org.openapitools.client.model.UsePurpose;

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
 * ConsentArtefactResponseConsentConsentDetail
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:36.866529-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ConsentArtefactResponseConsentConsentDetail {
  public static final String SERIALIZED_NAME_CARE_CONTEXTS = "careContexts";
  @SerializedName(SERIALIZED_NAME_CARE_CONTEXTS)
  private List<ConsentArtefactResponseConsentConsentDetailCareContextsInner> careContexts = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONSENT_ID = "consentId";
  @SerializedName(SERIALIZED_NAME_CONSENT_ID)
  private UUID consentId;

  public static final String SERIALIZED_NAME_CONSENT_MANAGER = "consentManager";
  @SerializedName(SERIALIZED_NAME_CONSENT_MANAGER)
  private ConsentArtefactResponseConsentConsentDetailConsentManager consentManager;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_HI_TYPES = "hiTypes";
  @SerializedName(SERIALIZED_NAME_HI_TYPES)
  private List<HITypeEnum> hiTypes = new ArrayList<>();

  public static final String SERIALIZED_NAME_HIP = "hip";
  @SerializedName(SERIALIZED_NAME_HIP)
  private ConsentArtefactResponseConsentConsentDetailHip hip;

  public static final String SERIALIZED_NAME_HIU = "hiu";
  @SerializedName(SERIALIZED_NAME_HIU)
  private ConsentArtefactResponseConsentConsentDetailHiu hiu;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private ConsentManagerPatientID patient;

  public static final String SERIALIZED_NAME_PERMISSION = "permission";
  @SerializedName(SERIALIZED_NAME_PERMISSION)
  private Permission permission;

  public static final String SERIALIZED_NAME_PURPOSE = "purpose";
  @SerializedName(SERIALIZED_NAME_PURPOSE)
  private UsePurpose purpose;

  public static final String SERIALIZED_NAME_REQUESTER = "requester";
  @SerializedName(SERIALIZED_NAME_REQUESTER)
  private Requester requester;

  public static final String SERIALIZED_NAME_SCHEMA_VERSION = "schemaVersion";
  @SerializedName(SERIALIZED_NAME_SCHEMA_VERSION)
  private String schemaVersion;

  public ConsentArtefactResponseConsentConsentDetail() {
  }

  public ConsentArtefactResponseConsentConsentDetail careContexts(List<ConsentArtefactResponseConsentConsentDetailCareContextsInner> careContexts) {
    this.careContexts = careContexts;
    return this;
  }

  public ConsentArtefactResponseConsentConsentDetail addCareContextsItem(ConsentArtefactResponseConsentConsentDetailCareContextsInner careContextsItem) {
    if (this.careContexts == null) {
      this.careContexts = new ArrayList<>();
    }
    this.careContexts.add(careContextsItem);
    return this;
  }

  /**
   * Get careContexts
   * @return careContexts
   */
  @javax.annotation.Nonnull
  public List<ConsentArtefactResponseConsentConsentDetailCareContextsInner> getCareContexts() {
    return careContexts;
  }

  public void setCareContexts(List<ConsentArtefactResponseConsentConsentDetailCareContextsInner> careContexts) {
    this.careContexts = careContexts;
  }


  public ConsentArtefactResponseConsentConsentDetail consentId(UUID consentId) {
    this.consentId = consentId;
    return this;
  }

  /**
   * Get consentId
   * @return consentId
   */
  @javax.annotation.Nonnull
  public UUID getConsentId() {
    return consentId;
  }

  public void setConsentId(UUID consentId) {
    this.consentId = consentId;
  }


  public ConsentArtefactResponseConsentConsentDetail consentManager(ConsentArtefactResponseConsentConsentDetailConsentManager consentManager) {
    this.consentManager = consentManager;
    return this;
  }

  /**
   * Get consentManager
   * @return consentManager
   */
  @javax.annotation.Nonnull
  public ConsentArtefactResponseConsentConsentDetailConsentManager getConsentManager() {
    return consentManager;
  }

  public void setConsentManager(ConsentArtefactResponseConsentConsentDetailConsentManager consentManager) {
    this.consentManager = consentManager;
  }


  public ConsentArtefactResponseConsentConsentDetail createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public ConsentArtefactResponseConsentConsentDetail hiTypes(List<HITypeEnum> hiTypes) {
    this.hiTypes = hiTypes;
    return this;
  }

  public ConsentArtefactResponseConsentConsentDetail addHiTypesItem(HITypeEnum hiTypesItem) {
    if (this.hiTypes == null) {
      this.hiTypes = new ArrayList<>();
    }
    this.hiTypes.add(hiTypesItem);
    return this;
  }

  /**
   * Get hiTypes
   * @return hiTypes
   */
  @javax.annotation.Nonnull
  public List<HITypeEnum> getHiTypes() {
    return hiTypes;
  }

  public void setHiTypes(List<HITypeEnum> hiTypes) {
    this.hiTypes = hiTypes;
  }


  public ConsentArtefactResponseConsentConsentDetail hip(ConsentArtefactResponseConsentConsentDetailHip hip) {
    this.hip = hip;
    return this;
  }

  /**
   * Get hip
   * @return hip
   */
  @javax.annotation.Nonnull
  public ConsentArtefactResponseConsentConsentDetailHip getHip() {
    return hip;
  }

  public void setHip(ConsentArtefactResponseConsentConsentDetailHip hip) {
    this.hip = hip;
  }


  public ConsentArtefactResponseConsentConsentDetail hiu(ConsentArtefactResponseConsentConsentDetailHiu hiu) {
    this.hiu = hiu;
    return this;
  }

  /**
   * Get hiu
   * @return hiu
   */
  @javax.annotation.Nonnull
  public ConsentArtefactResponseConsentConsentDetailHiu getHiu() {
    return hiu;
  }

  public void setHiu(ConsentArtefactResponseConsentConsentDetailHiu hiu) {
    this.hiu = hiu;
  }


  public ConsentArtefactResponseConsentConsentDetail patient(ConsentManagerPatientID patient) {
    this.patient = patient;
    return this;
  }

  /**
   * Get patient
   * @return patient
   */
  @javax.annotation.Nonnull
  public ConsentManagerPatientID getPatient() {
    return patient;
  }

  public void setPatient(ConsentManagerPatientID patient) {
    this.patient = patient;
  }


  public ConsentArtefactResponseConsentConsentDetail permission(Permission permission) {
    this.permission = permission;
    return this;
  }

  /**
   * Get permission
   * @return permission
   */
  @javax.annotation.Nonnull
  public Permission getPermission() {
    return permission;
  }

  public void setPermission(Permission permission) {
    this.permission = permission;
  }


  public ConsentArtefactResponseConsentConsentDetail purpose(UsePurpose purpose) {
    this.purpose = purpose;
    return this;
  }

  /**
   * Get purpose
   * @return purpose
   */
  @javax.annotation.Nonnull
  public UsePurpose getPurpose() {
    return purpose;
  }

  public void setPurpose(UsePurpose purpose) {
    this.purpose = purpose;
  }


  public ConsentArtefactResponseConsentConsentDetail requester(Requester requester) {
    this.requester = requester;
    return this;
  }

  /**
   * Get requester
   * @return requester
   */
  @javax.annotation.Nonnull
  public Requester getRequester() {
    return requester;
  }

  public void setRequester(Requester requester) {
    this.requester = requester;
  }


  public ConsentArtefactResponseConsentConsentDetail schemaVersion(String schemaVersion) {
    this.schemaVersion = schemaVersion;
    return this;
  }

  /**
   * Get schemaVersion
   * @return schemaVersion
   */
  @javax.annotation.Nullable
  public String getSchemaVersion() {
    return schemaVersion;
  }

  public void setSchemaVersion(String schemaVersion) {
    this.schemaVersion = schemaVersion;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConsentArtefactResponseConsentConsentDetail consentArtefactResponseConsentConsentDetail = (ConsentArtefactResponseConsentConsentDetail) o;
    return Objects.equals(this.careContexts, consentArtefactResponseConsentConsentDetail.careContexts) &&
        Objects.equals(this.consentId, consentArtefactResponseConsentConsentDetail.consentId) &&
        Objects.equals(this.consentManager, consentArtefactResponseConsentConsentDetail.consentManager) &&
        Objects.equals(this.createdAt, consentArtefactResponseConsentConsentDetail.createdAt) &&
        Objects.equals(this.hiTypes, consentArtefactResponseConsentConsentDetail.hiTypes) &&
        Objects.equals(this.hip, consentArtefactResponseConsentConsentDetail.hip) &&
        Objects.equals(this.hiu, consentArtefactResponseConsentConsentDetail.hiu) &&
        Objects.equals(this.patient, consentArtefactResponseConsentConsentDetail.patient) &&
        Objects.equals(this.permission, consentArtefactResponseConsentConsentDetail.permission) &&
        Objects.equals(this.purpose, consentArtefactResponseConsentConsentDetail.purpose) &&
        Objects.equals(this.requester, consentArtefactResponseConsentConsentDetail.requester) &&
        Objects.equals(this.schemaVersion, consentArtefactResponseConsentConsentDetail.schemaVersion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(careContexts, consentId, consentManager, createdAt, hiTypes, hip, hiu, patient, permission, purpose, requester, schemaVersion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ConsentArtefactResponseConsentConsentDetail {\n");
    sb.append("    careContexts: ").append(toIndentedString(careContexts)).append("\n");
    sb.append("    consentId: ").append(toIndentedString(consentId)).append("\n");
    sb.append("    consentManager: ").append(toIndentedString(consentManager)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    hiTypes: ").append(toIndentedString(hiTypes)).append("\n");
    sb.append("    hip: ").append(toIndentedString(hip)).append("\n");
    sb.append("    hiu: ").append(toIndentedString(hiu)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    permission: ").append(toIndentedString(permission)).append("\n");
    sb.append("    purpose: ").append(toIndentedString(purpose)).append("\n");
    sb.append("    requester: ").append(toIndentedString(requester)).append("\n");
    sb.append("    schemaVersion: ").append(toIndentedString(schemaVersion)).append("\n");
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
    openapiFields.add("careContexts");
    openapiFields.add("consentId");
    openapiFields.add("consentManager");
    openapiFields.add("createdAt");
    openapiFields.add("hiTypes");
    openapiFields.add("hip");
    openapiFields.add("hiu");
    openapiFields.add("patient");
    openapiFields.add("permission");
    openapiFields.add("purpose");
    openapiFields.add("requester");
    openapiFields.add("schemaVersion");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("careContexts");
    openapiRequiredFields.add("consentId");
    openapiRequiredFields.add("consentManager");
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("hiTypes");
    openapiRequiredFields.add("hip");
    openapiRequiredFields.add("hiu");
    openapiRequiredFields.add("patient");
    openapiRequiredFields.add("permission");
    openapiRequiredFields.add("purpose");
    openapiRequiredFields.add("requester");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ConsentArtefactResponseConsentConsentDetail
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ConsentArtefactResponseConsentConsentDetail.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ConsentArtefactResponseConsentConsentDetail is not found in the empty JSON string", ConsentArtefactResponseConsentConsentDetail.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ConsentArtefactResponseConsentConsentDetail.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ConsentArtefactResponseConsentConsentDetail` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ConsentArtefactResponseConsentConsentDetail.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("careContexts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `careContexts` to be an array in the JSON string but got `%s`", jsonObj.get("careContexts").toString()));
      }

      JsonArray jsonArraycareContexts = jsonObj.getAsJsonArray("careContexts");
      // validate the required field `careContexts` (array)
      for (int i = 0; i < jsonArraycareContexts.size(); i++) {
        ConsentArtefactResponseConsentConsentDetailCareContextsInner.validateJsonElement(jsonArraycareContexts.get(i));
      };
      if (!jsonObj.get("consentId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consentId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consentId").toString()));
      }
      // validate the required field `consentManager`
      ConsentArtefactResponseConsentConsentDetailConsentManager.validateJsonElement(jsonObj.get("consentManager"));
      // ensure the required json array is present
      if (jsonObj.get("hiTypes") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("hiTypes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `hiTypes` to be an array in the JSON string but got `%s`", jsonObj.get("hiTypes").toString()));
      }
      // validate the required field `hip`
      ConsentArtefactResponseConsentConsentDetailHip.validateJsonElement(jsonObj.get("hip"));
      // validate the required field `hiu`
      ConsentArtefactResponseConsentConsentDetailHiu.validateJsonElement(jsonObj.get("hiu"));
      // validate the required field `patient`
      ConsentManagerPatientID.validateJsonElement(jsonObj.get("patient"));
      // validate the required field `permission`
      Permission.validateJsonElement(jsonObj.get("permission"));
      // validate the required field `purpose`
      UsePurpose.validateJsonElement(jsonObj.get("purpose"));
      // validate the required field `requester`
      Requester.validateJsonElement(jsonObj.get("requester"));
      if ((jsonObj.get("schemaVersion") != null && !jsonObj.get("schemaVersion").isJsonNull()) && !jsonObj.get("schemaVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `schemaVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("schemaVersion").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ConsentArtefactResponseConsentConsentDetail.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ConsentArtefactResponseConsentConsentDetail' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ConsentArtefactResponseConsentConsentDetail> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ConsentArtefactResponseConsentConsentDetail.class));

       return (TypeAdapter<T>) new TypeAdapter<ConsentArtefactResponseConsentConsentDetail>() {
           @Override
           public void write(JsonWriter out, ConsentArtefactResponseConsentConsentDetail value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ConsentArtefactResponseConsentConsentDetail read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ConsentArtefactResponseConsentConsentDetail given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ConsentArtefactResponseConsentConsentDetail
   * @throws IOException if the JSON string is invalid with respect to ConsentArtefactResponseConsentConsentDetail
   */
  public static ConsentArtefactResponseConsentConsentDetail fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ConsentArtefactResponseConsentConsentDetail.class);
  }

  /**
   * Convert an instance of ConsentArtefactResponseConsentConsentDetail to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

