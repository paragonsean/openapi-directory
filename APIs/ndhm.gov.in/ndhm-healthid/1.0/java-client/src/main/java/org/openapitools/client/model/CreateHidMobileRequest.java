/*
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
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
 * CreateHidMobileRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:34.465238-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateHidMobileRequest {
  public static final String SERIALIZED_NAME_AUTO_GENERATED_BENEFIT_ID = "autoGeneratedBenefitId";
  @SerializedName(SERIALIZED_NAME_AUTO_GENERATED_BENEFIT_ID)
  private Boolean autoGeneratedBenefitId;

  /**
   * Gets or Sets benefitDocType
   */
  @JsonAdapter(BenefitDocTypeEnum.Adapter.class)
  public enum BenefitDocTypeEnum {
    VOTER_ID_CARD("VOTER_ID_CARD"),
    
    RATION_CARD("RATION_CARD"),
    
    PAN_CARD("PAN_CARD"),
    
    DRIVING_LICENSE("DRIVING_LICENSE"),
    
    PENSIONER_PHOTO_CARD("PENSIONER_PHOTO_CARD"),
    
    KISSAN_PHOTO_PASSBOOK("KISSAN_PHOTO_PASSBOOK"),
    
    FREEDOM_FIGHTER_PHOTO_CARD("FREEDOM_FIGHTER_PHOTO_CARD"),
    
    CERTIFICATE_IDENTIFY("CERTIFICATE_IDENTIFY"),
    
    DISABILITY_ID_CARD("DISABILITY_ID_CARD"),
    
    MNREGA_JOB_CARD("MNREGA_JOB_CARD"),
    
    BIRTH_CERTIFICATE("BIRTH_CERTIFICATE"),
    
    MARRIAGE_CERTIFICATE("MARRIAGE_CERTIFICATE"),
    
    OTHER_GOVERNMENT_ID("OTHER_GOVERNMENT_ID"),
    
    ADOPTION_CERTIFICATE("ADOPTION_CERTIFICATE");

    private String value;

    BenefitDocTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BenefitDocTypeEnum fromValue(String value) {
      for (BenefitDocTypeEnum b : BenefitDocTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BenefitDocTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BenefitDocTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BenefitDocTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BenefitDocTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BenefitDocTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BENEFIT_DOC_TYPE = "benefitDocType";
  @SerializedName(SERIALIZED_NAME_BENEFIT_DOC_TYPE)
  private BenefitDocTypeEnum benefitDocType;

  public static final String SERIALIZED_NAME_BENEFIT_ID = "benefitId";
  @SerializedName(SERIALIZED_NAME_BENEFIT_ID)
  private String benefitId;

  public static final String SERIALIZED_NAME_BENEFIT_NAME = "benefitName";
  @SerializedName(SERIALIZED_NAME_BENEFIT_NAME)
  private String benefitName;

  public static final String SERIALIZED_NAME_CONSENT_HEALTH_ID = "consentHealthId";
  @SerializedName(SERIALIZED_NAME_CONSENT_HEALTH_ID)
  private Boolean consentHealthId;

  public static final String SERIALIZED_NAME_DATE_OF_BIRTH = "dateOfBirth";
  @SerializedName(SERIALIZED_NAME_DATE_OF_BIRTH)
  private String dateOfBirth;

  public static final String SERIALIZED_NAME_DOC_NUMBER = "docNumber";
  @SerializedName(SERIALIZED_NAME_DOC_NUMBER)
  private String docNumber;

  public static final String SERIALIZED_NAME_FILE_TYPE = "fileType";
  @SerializedName(SERIALIZED_NAME_FILE_TYPE)
  private String fileType;

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OTP = "otp";
  @SerializedName(SERIALIZED_NAME_OTP)
  private String otp;

  public static final String SERIALIZED_NAME_TXN_ID = "txnId";
  @SerializedName(SERIALIZED_NAME_TXN_ID)
  private String txnId;

  public static final String SERIALIZED_NAME_UPLOADED_DOC = "uploadedDoc";
  @SerializedName(SERIALIZED_NAME_UPLOADED_DOC)
  private String uploadedDoc;

  public static final String SERIALIZED_NAME_VALIDITY = "validity";
  @SerializedName(SERIALIZED_NAME_VALIDITY)
  private String validity;

  public CreateHidMobileRequest() {
  }

  public CreateHidMobileRequest autoGeneratedBenefitId(Boolean autoGeneratedBenefitId) {
    this.autoGeneratedBenefitId = autoGeneratedBenefitId;
    return this;
  }

  /**
   * Get autoGeneratedBenefitId
   * @return autoGeneratedBenefitId
   */
  @javax.annotation.Nullable
  public Boolean getAutoGeneratedBenefitId() {
    return autoGeneratedBenefitId;
  }

  public void setAutoGeneratedBenefitId(Boolean autoGeneratedBenefitId) {
    this.autoGeneratedBenefitId = autoGeneratedBenefitId;
  }


  public CreateHidMobileRequest benefitDocType(BenefitDocTypeEnum benefitDocType) {
    this.benefitDocType = benefitDocType;
    return this;
  }

  /**
   * Get benefitDocType
   * @return benefitDocType
   */
  @javax.annotation.Nullable
  public BenefitDocTypeEnum getBenefitDocType() {
    return benefitDocType;
  }

  public void setBenefitDocType(BenefitDocTypeEnum benefitDocType) {
    this.benefitDocType = benefitDocType;
  }


  public CreateHidMobileRequest benefitId(String benefitId) {
    this.benefitId = benefitId;
    return this;
  }

  /**
   * Get benefitId
   * @return benefitId
   */
  @javax.annotation.Nullable
  public String getBenefitId() {
    return benefitId;
  }

  public void setBenefitId(String benefitId) {
    this.benefitId = benefitId;
  }


  public CreateHidMobileRequest benefitName(String benefitName) {
    this.benefitName = benefitName;
    return this;
  }

  /**
   * Get benefitName
   * @return benefitName
   */
  @javax.annotation.Nullable
  public String getBenefitName() {
    return benefitName;
  }

  public void setBenefitName(String benefitName) {
    this.benefitName = benefitName;
  }


  public CreateHidMobileRequest consentHealthId(Boolean consentHealthId) {
    this.consentHealthId = consentHealthId;
    return this;
  }

  /**
   * Get consentHealthId
   * @return consentHealthId
   */
  @javax.annotation.Nullable
  public Boolean getConsentHealthId() {
    return consentHealthId;
  }

  public void setConsentHealthId(Boolean consentHealthId) {
    this.consentHealthId = consentHealthId;
  }


  public CreateHidMobileRequest dateOfBirth(String dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

  /**
   * Get dateOfBirth
   * @return dateOfBirth
   */
  @javax.annotation.Nullable
  public String getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(String dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }


  public CreateHidMobileRequest docNumber(String docNumber) {
    this.docNumber = docNumber;
    return this;
  }

  /**
   * Get docNumber
   * @return docNumber
   */
  @javax.annotation.Nullable
  public String getDocNumber() {
    return docNumber;
  }

  public void setDocNumber(String docNumber) {
    this.docNumber = docNumber;
  }


  public CreateHidMobileRequest fileType(String fileType) {
    this.fileType = fileType;
    return this;
  }

  /**
   * Get fileType
   * @return fileType
   */
  @javax.annotation.Nullable
  public String getFileType() {
    return fileType;
  }

  public void setFileType(String fileType) {
    this.fileType = fileType;
  }


  public CreateHidMobileRequest gender(String gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Get gender
   * @return gender
   */
  @javax.annotation.Nullable
  public String getGender() {
    return gender;
  }

  public void setGender(String gender) {
    this.gender = gender;
  }


  public CreateHidMobileRequest name(String name) {
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


  public CreateHidMobileRequest otp(String otp) {
    this.otp = otp;
    return this;
  }

  /**
   * Get otp
   * @return otp
   */
  @javax.annotation.Nullable
  public String getOtp() {
    return otp;
  }

  public void setOtp(String otp) {
    this.otp = otp;
  }


  public CreateHidMobileRequest txnId(String txnId) {
    this.txnId = txnId;
    return this;
  }

  /**
   * Get txnId
   * @return txnId
   */
  @javax.annotation.Nullable
  public String getTxnId() {
    return txnId;
  }

  public void setTxnId(String txnId) {
    this.txnId = txnId;
  }


  public CreateHidMobileRequest uploadedDoc(String uploadedDoc) {
    this.uploadedDoc = uploadedDoc;
    return this;
  }

  /**
   * Get uploadedDoc
   * @return uploadedDoc
   */
  @javax.annotation.Nullable
  public String getUploadedDoc() {
    return uploadedDoc;
  }

  public void setUploadedDoc(String uploadedDoc) {
    this.uploadedDoc = uploadedDoc;
  }


  public CreateHidMobileRequest validity(String validity) {
    this.validity = validity;
    return this;
  }

  /**
   * Get validity
   * @return validity
   */
  @javax.annotation.Nullable
  public String getValidity() {
    return validity;
  }

  public void setValidity(String validity) {
    this.validity = validity;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateHidMobileRequest createHidMobileRequest = (CreateHidMobileRequest) o;
    return Objects.equals(this.autoGeneratedBenefitId, createHidMobileRequest.autoGeneratedBenefitId) &&
        Objects.equals(this.benefitDocType, createHidMobileRequest.benefitDocType) &&
        Objects.equals(this.benefitId, createHidMobileRequest.benefitId) &&
        Objects.equals(this.benefitName, createHidMobileRequest.benefitName) &&
        Objects.equals(this.consentHealthId, createHidMobileRequest.consentHealthId) &&
        Objects.equals(this.dateOfBirth, createHidMobileRequest.dateOfBirth) &&
        Objects.equals(this.docNumber, createHidMobileRequest.docNumber) &&
        Objects.equals(this.fileType, createHidMobileRequest.fileType) &&
        Objects.equals(this.gender, createHidMobileRequest.gender) &&
        Objects.equals(this.name, createHidMobileRequest.name) &&
        Objects.equals(this.otp, createHidMobileRequest.otp) &&
        Objects.equals(this.txnId, createHidMobileRequest.txnId) &&
        Objects.equals(this.uploadedDoc, createHidMobileRequest.uploadedDoc) &&
        Objects.equals(this.validity, createHidMobileRequest.validity);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoGeneratedBenefitId, benefitDocType, benefitId, benefitName, consentHealthId, dateOfBirth, docNumber, fileType, gender, name, otp, txnId, uploadedDoc, validity);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateHidMobileRequest {\n");
    sb.append("    autoGeneratedBenefitId: ").append(toIndentedString(autoGeneratedBenefitId)).append("\n");
    sb.append("    benefitDocType: ").append(toIndentedString(benefitDocType)).append("\n");
    sb.append("    benefitId: ").append(toIndentedString(benefitId)).append("\n");
    sb.append("    benefitName: ").append(toIndentedString(benefitName)).append("\n");
    sb.append("    consentHealthId: ").append(toIndentedString(consentHealthId)).append("\n");
    sb.append("    dateOfBirth: ").append(toIndentedString(dateOfBirth)).append("\n");
    sb.append("    docNumber: ").append(toIndentedString(docNumber)).append("\n");
    sb.append("    fileType: ").append(toIndentedString(fileType)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    otp: ").append(toIndentedString(otp)).append("\n");
    sb.append("    txnId: ").append(toIndentedString(txnId)).append("\n");
    sb.append("    uploadedDoc: ").append(toIndentedString(uploadedDoc)).append("\n");
    sb.append("    validity: ").append(toIndentedString(validity)).append("\n");
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
    openapiFields.add("autoGeneratedBenefitId");
    openapiFields.add("benefitDocType");
    openapiFields.add("benefitId");
    openapiFields.add("benefitName");
    openapiFields.add("consentHealthId");
    openapiFields.add("dateOfBirth");
    openapiFields.add("docNumber");
    openapiFields.add("fileType");
    openapiFields.add("gender");
    openapiFields.add("name");
    openapiFields.add("otp");
    openapiFields.add("txnId");
    openapiFields.add("uploadedDoc");
    openapiFields.add("validity");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateHidMobileRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateHidMobileRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateHidMobileRequest is not found in the empty JSON string", CreateHidMobileRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateHidMobileRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateHidMobileRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("benefitDocType") != null && !jsonObj.get("benefitDocType").isJsonNull()) && !jsonObj.get("benefitDocType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `benefitDocType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("benefitDocType").toString()));
      }
      // validate the optional field `benefitDocType`
      if (jsonObj.get("benefitDocType") != null && !jsonObj.get("benefitDocType").isJsonNull()) {
        BenefitDocTypeEnum.validateJsonElement(jsonObj.get("benefitDocType"));
      }
      if ((jsonObj.get("benefitId") != null && !jsonObj.get("benefitId").isJsonNull()) && !jsonObj.get("benefitId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `benefitId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("benefitId").toString()));
      }
      if ((jsonObj.get("benefitName") != null && !jsonObj.get("benefitName").isJsonNull()) && !jsonObj.get("benefitName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `benefitName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("benefitName").toString()));
      }
      if ((jsonObj.get("dateOfBirth") != null && !jsonObj.get("dateOfBirth").isJsonNull()) && !jsonObj.get("dateOfBirth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dateOfBirth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dateOfBirth").toString()));
      }
      if ((jsonObj.get("docNumber") != null && !jsonObj.get("docNumber").isJsonNull()) && !jsonObj.get("docNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `docNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("docNumber").toString()));
      }
      if ((jsonObj.get("fileType") != null && !jsonObj.get("fileType").isJsonNull()) && !jsonObj.get("fileType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileType").toString()));
      }
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("otp") != null && !jsonObj.get("otp").isJsonNull()) && !jsonObj.get("otp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `otp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("otp").toString()));
      }
      if ((jsonObj.get("txnId") != null && !jsonObj.get("txnId").isJsonNull()) && !jsonObj.get("txnId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `txnId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("txnId").toString()));
      }
      if ((jsonObj.get("uploadedDoc") != null && !jsonObj.get("uploadedDoc").isJsonNull()) && !jsonObj.get("uploadedDoc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uploadedDoc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uploadedDoc").toString()));
      }
      if ((jsonObj.get("validity") != null && !jsonObj.get("validity").isJsonNull()) && !jsonObj.get("validity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `validity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("validity").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateHidMobileRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateHidMobileRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateHidMobileRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateHidMobileRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateHidMobileRequest>() {
           @Override
           public void write(JsonWriter out, CreateHidMobileRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateHidMobileRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateHidMobileRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateHidMobileRequest
   * @throws IOException if the JSON string is invalid with respect to CreateHidMobileRequest
   */
  public static CreateHidMobileRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateHidMobileRequest.class);
  }

  /**
   * Convert an instance of CreateHidMobileRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

