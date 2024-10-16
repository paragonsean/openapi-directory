/*
 * LetMC Api V3, reporting
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-reporting
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
 * Helper Model - Litigation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:11.827585-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReportingReceivershipLitigationModel {
  public static final String SERIALIZED_NAME_CLOSED_LITIGATION_DATE = "ClosedLitigationDate";
  @SerializedName(SERIALIZED_NAME_CLOSED_LITIGATION_DATE)
  private OffsetDateTime closedLitigationDate;

  /**
   * Closed Litigation Reason
   */
  @JsonAdapter(ClosedLitigationReasonEnum.Adapter.class)
  public enum ClosedLitigationReasonEnum {
    POSSESSION_OBTAINED("PossessionObtained"),
    
    TENANT_VACATED("TenantVacated"),
    
    LITIGATION_CANCELLED("LitigationCancelled"),
    
    OTHER("Other");

    private String value;

    ClosedLitigationReasonEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ClosedLitigationReasonEnum fromValue(String value) {
      for (ClosedLitigationReasonEnum b : ClosedLitigationReasonEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ClosedLitigationReasonEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ClosedLitigationReasonEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ClosedLitigationReasonEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ClosedLitigationReasonEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ClosedLitigationReasonEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CLOSED_LITIGATION_REASON = "ClosedLitigationReason";
  @SerializedName(SERIALIZED_NAME_CLOSED_LITIGATION_REASON)
  private ClosedLitigationReasonEnum closedLitigationReason;

  public static final String SERIALIZED_NAME_COMPILED_BY_SOLICITOR_I_D = "CompiledBySolicitorID";
  @SerializedName(SERIALIZED_NAME_COMPILED_BY_SOLICITOR_I_D)
  private String compiledBySolicitorID;

  public static final String SERIALIZED_NAME_DISPLAY_COMPILED_BY_SOLICITOR = "DisplayCompiledBySolicitor";
  @SerializedName(SERIALIZED_NAME_DISPLAY_COMPILED_BY_SOLICITOR)
  private String displayCompiledBySolicitor;

  public static final String SERIALIZED_NAME_EVICTION_DATE = "EvictionDate";
  @SerializedName(SERIALIZED_NAME_EVICTION_DATE)
  private OffsetDateTime evictionDate;

  /**
   * Eviction Outcome
   */
  @JsonAdapter(EvictionOutcomeEnum.Adapter.class)
  public enum EvictionOutcomeEnum {
    EVICTION_COMPLETE("EvictionComplete"),
    
    EVICTION_CANCELLED("EvictionCancelled"),
    
    OTHER("Other");

    private String value;

    EvictionOutcomeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EvictionOutcomeEnum fromValue(String value) {
      for (EvictionOutcomeEnum b : EvictionOutcomeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EvictionOutcomeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EvictionOutcomeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EvictionOutcomeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EvictionOutcomeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EvictionOutcomeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EVICTION_OUTCOME = "EvictionOutcome";
  @SerializedName(SERIALIZED_NAME_EVICTION_OUTCOME)
  private EvictionOutcomeEnum evictionOutcome;

  public static final String SERIALIZED_NAME_EXTRA_NOTES = "ExtraNotes";
  @SerializedName(SERIALIZED_NAME_EXTRA_NOTES)
  private String extraNotes;

  public static final String SERIALIZED_NAME_HEARING_DATE = "HearingDate";
  @SerializedName(SERIALIZED_NAME_HEARING_DATE)
  private OffsetDateTime hearingDate;

  public static final String SERIALIZED_NAME_HEARING_OUTCOME = "HearingOutcome";
  @SerializedName(SERIALIZED_NAME_HEARING_OUTCOME)
  private String hearingOutcome;

  public static final String SERIALIZED_NAME_LITIGATION_TYPE = "LitigationType";
  @SerializedName(SERIALIZED_NAME_LITIGATION_TYPE)
  private String litigationType;

  public static final String SERIALIZED_NAME_NOTICE_EXPIRY_DATE = "NoticeExpiryDate";
  @SerializedName(SERIALIZED_NAME_NOTICE_EXPIRY_DATE)
  private OffsetDateTime noticeExpiryDate;

  public static final String SERIALIZED_NAME_NOTICE_SERVED_DATE = "NoticeServedDate";
  @SerializedName(SERIALIZED_NAME_NOTICE_SERVED_DATE)
  private OffsetDateTime noticeServedDate;

  public static final String SERIALIZED_NAME_PROCEEDINGS_ISSUED_DATE = "ProceedingsIssuedDate";
  @SerializedName(SERIALIZED_NAME_PROCEEDINGS_ISSUED_DATE)
  private OffsetDateTime proceedingsIssuedDate;

  public ReportingReceivershipLitigationModel() {
  }

  public ReportingReceivershipLitigationModel closedLitigationDate(OffsetDateTime closedLitigationDate) {
    this.closedLitigationDate = closedLitigationDate;
    return this;
  }

  /**
   * Closed Litigation Date
   * @return closedLitigationDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getClosedLitigationDate() {
    return closedLitigationDate;
  }

  public void setClosedLitigationDate(OffsetDateTime closedLitigationDate) {
    this.closedLitigationDate = closedLitigationDate;
  }


  public ReportingReceivershipLitigationModel closedLitigationReason(ClosedLitigationReasonEnum closedLitigationReason) {
    this.closedLitigationReason = closedLitigationReason;
    return this;
  }

  /**
   * Closed Litigation Reason
   * @return closedLitigationReason
   */
  @javax.annotation.Nullable
  public ClosedLitigationReasonEnum getClosedLitigationReason() {
    return closedLitigationReason;
  }

  public void setClosedLitigationReason(ClosedLitigationReasonEnum closedLitigationReason) {
    this.closedLitigationReason = closedLitigationReason;
  }


  public ReportingReceivershipLitigationModel compiledBySolicitorID(String compiledBySolicitorID) {
    this.compiledBySolicitorID = compiledBySolicitorID;
    return this;
  }

  /**
   * Compiled By Solicitor ID (SalesSolicitor)
   * @return compiledBySolicitorID
   */
  @javax.annotation.Nullable
  public String getCompiledBySolicitorID() {
    return compiledBySolicitorID;
  }

  public void setCompiledBySolicitorID(String compiledBySolicitorID) {
    this.compiledBySolicitorID = compiledBySolicitorID;
  }


  public ReportingReceivershipLitigationModel displayCompiledBySolicitor(String displayCompiledBySolicitor) {
    this.displayCompiledBySolicitor = displayCompiledBySolicitor;
    return this;
  }

  /**
   * Display Compiled By Solicitor
   * @return displayCompiledBySolicitor
   */
  @javax.annotation.Nullable
  public String getDisplayCompiledBySolicitor() {
    return displayCompiledBySolicitor;
  }

  public void setDisplayCompiledBySolicitor(String displayCompiledBySolicitor) {
    this.displayCompiledBySolicitor = displayCompiledBySolicitor;
  }


  public ReportingReceivershipLitigationModel evictionDate(OffsetDateTime evictionDate) {
    this.evictionDate = evictionDate;
    return this;
  }

  /**
   * Eviction Date
   * @return evictionDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEvictionDate() {
    return evictionDate;
  }

  public void setEvictionDate(OffsetDateTime evictionDate) {
    this.evictionDate = evictionDate;
  }


  public ReportingReceivershipLitigationModel evictionOutcome(EvictionOutcomeEnum evictionOutcome) {
    this.evictionOutcome = evictionOutcome;
    return this;
  }

  /**
   * Eviction Outcome
   * @return evictionOutcome
   */
  @javax.annotation.Nullable
  public EvictionOutcomeEnum getEvictionOutcome() {
    return evictionOutcome;
  }

  public void setEvictionOutcome(EvictionOutcomeEnum evictionOutcome) {
    this.evictionOutcome = evictionOutcome;
  }


  public ReportingReceivershipLitigationModel extraNotes(String extraNotes) {
    this.extraNotes = extraNotes;
    return this;
  }

  /**
   * Extra Notes
   * @return extraNotes
   */
  @javax.annotation.Nullable
  public String getExtraNotes() {
    return extraNotes;
  }

  public void setExtraNotes(String extraNotes) {
    this.extraNotes = extraNotes;
  }


  public ReportingReceivershipLitigationModel hearingDate(OffsetDateTime hearingDate) {
    this.hearingDate = hearingDate;
    return this;
  }

  /**
   * Hearing Date
   * @return hearingDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getHearingDate() {
    return hearingDate;
  }

  public void setHearingDate(OffsetDateTime hearingDate) {
    this.hearingDate = hearingDate;
  }


  public ReportingReceivershipLitigationModel hearingOutcome(String hearingOutcome) {
    this.hearingOutcome = hearingOutcome;
    return this;
  }

  /**
   * Hearing Outcome
   * @return hearingOutcome
   */
  @javax.annotation.Nullable
  public String getHearingOutcome() {
    return hearingOutcome;
  }

  public void setHearingOutcome(String hearingOutcome) {
    this.hearingOutcome = hearingOutcome;
  }


  public ReportingReceivershipLitigationModel litigationType(String litigationType) {
    this.litigationType = litigationType;
    return this;
  }

  /**
   * Litigation Type
   * @return litigationType
   */
  @javax.annotation.Nullable
  public String getLitigationType() {
    return litigationType;
  }

  public void setLitigationType(String litigationType) {
    this.litigationType = litigationType;
  }


  public ReportingReceivershipLitigationModel noticeExpiryDate(OffsetDateTime noticeExpiryDate) {
    this.noticeExpiryDate = noticeExpiryDate;
    return this;
  }

  /**
   * Notice Expiry Date
   * @return noticeExpiryDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNoticeExpiryDate() {
    return noticeExpiryDate;
  }

  public void setNoticeExpiryDate(OffsetDateTime noticeExpiryDate) {
    this.noticeExpiryDate = noticeExpiryDate;
  }


  public ReportingReceivershipLitigationModel noticeServedDate(OffsetDateTime noticeServedDate) {
    this.noticeServedDate = noticeServedDate;
    return this;
  }

  /**
   * Notice Served Date
   * @return noticeServedDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNoticeServedDate() {
    return noticeServedDate;
  }

  public void setNoticeServedDate(OffsetDateTime noticeServedDate) {
    this.noticeServedDate = noticeServedDate;
  }


  public ReportingReceivershipLitigationModel proceedingsIssuedDate(OffsetDateTime proceedingsIssuedDate) {
    this.proceedingsIssuedDate = proceedingsIssuedDate;
    return this;
  }

  /**
   * Proceedings Issued Date
   * @return proceedingsIssuedDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getProceedingsIssuedDate() {
    return proceedingsIssuedDate;
  }

  public void setProceedingsIssuedDate(OffsetDateTime proceedingsIssuedDate) {
    this.proceedingsIssuedDate = proceedingsIssuedDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReportingReceivershipLitigationModel reportingReceivershipLitigationModel = (ReportingReceivershipLitigationModel) o;
    return Objects.equals(this.closedLitigationDate, reportingReceivershipLitigationModel.closedLitigationDate) &&
        Objects.equals(this.closedLitigationReason, reportingReceivershipLitigationModel.closedLitigationReason) &&
        Objects.equals(this.compiledBySolicitorID, reportingReceivershipLitigationModel.compiledBySolicitorID) &&
        Objects.equals(this.displayCompiledBySolicitor, reportingReceivershipLitigationModel.displayCompiledBySolicitor) &&
        Objects.equals(this.evictionDate, reportingReceivershipLitigationModel.evictionDate) &&
        Objects.equals(this.evictionOutcome, reportingReceivershipLitigationModel.evictionOutcome) &&
        Objects.equals(this.extraNotes, reportingReceivershipLitigationModel.extraNotes) &&
        Objects.equals(this.hearingDate, reportingReceivershipLitigationModel.hearingDate) &&
        Objects.equals(this.hearingOutcome, reportingReceivershipLitigationModel.hearingOutcome) &&
        Objects.equals(this.litigationType, reportingReceivershipLitigationModel.litigationType) &&
        Objects.equals(this.noticeExpiryDate, reportingReceivershipLitigationModel.noticeExpiryDate) &&
        Objects.equals(this.noticeServedDate, reportingReceivershipLitigationModel.noticeServedDate) &&
        Objects.equals(this.proceedingsIssuedDate, reportingReceivershipLitigationModel.proceedingsIssuedDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(closedLitigationDate, closedLitigationReason, compiledBySolicitorID, displayCompiledBySolicitor, evictionDate, evictionOutcome, extraNotes, hearingDate, hearingOutcome, litigationType, noticeExpiryDate, noticeServedDate, proceedingsIssuedDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReportingReceivershipLitigationModel {\n");
    sb.append("    closedLitigationDate: ").append(toIndentedString(closedLitigationDate)).append("\n");
    sb.append("    closedLitigationReason: ").append(toIndentedString(closedLitigationReason)).append("\n");
    sb.append("    compiledBySolicitorID: ").append(toIndentedString(compiledBySolicitorID)).append("\n");
    sb.append("    displayCompiledBySolicitor: ").append(toIndentedString(displayCompiledBySolicitor)).append("\n");
    sb.append("    evictionDate: ").append(toIndentedString(evictionDate)).append("\n");
    sb.append("    evictionOutcome: ").append(toIndentedString(evictionOutcome)).append("\n");
    sb.append("    extraNotes: ").append(toIndentedString(extraNotes)).append("\n");
    sb.append("    hearingDate: ").append(toIndentedString(hearingDate)).append("\n");
    sb.append("    hearingOutcome: ").append(toIndentedString(hearingOutcome)).append("\n");
    sb.append("    litigationType: ").append(toIndentedString(litigationType)).append("\n");
    sb.append("    noticeExpiryDate: ").append(toIndentedString(noticeExpiryDate)).append("\n");
    sb.append("    noticeServedDate: ").append(toIndentedString(noticeServedDate)).append("\n");
    sb.append("    proceedingsIssuedDate: ").append(toIndentedString(proceedingsIssuedDate)).append("\n");
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
    openapiFields.add("ClosedLitigationDate");
    openapiFields.add("ClosedLitigationReason");
    openapiFields.add("CompiledBySolicitorID");
    openapiFields.add("DisplayCompiledBySolicitor");
    openapiFields.add("EvictionDate");
    openapiFields.add("EvictionOutcome");
    openapiFields.add("ExtraNotes");
    openapiFields.add("HearingDate");
    openapiFields.add("HearingOutcome");
    openapiFields.add("LitigationType");
    openapiFields.add("NoticeExpiryDate");
    openapiFields.add("NoticeServedDate");
    openapiFields.add("ProceedingsIssuedDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReportingReceivershipLitigationModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReportingReceivershipLitigationModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReportingReceivershipLitigationModel is not found in the empty JSON string", ReportingReceivershipLitigationModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReportingReceivershipLitigationModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReportingReceivershipLitigationModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ClosedLitigationReason") != null && !jsonObj.get("ClosedLitigationReason").isJsonNull()) && !jsonObj.get("ClosedLitigationReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ClosedLitigationReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ClosedLitigationReason").toString()));
      }
      // validate the optional field `ClosedLitigationReason`
      if (jsonObj.get("ClosedLitigationReason") != null && !jsonObj.get("ClosedLitigationReason").isJsonNull()) {
        ClosedLitigationReasonEnum.validateJsonElement(jsonObj.get("ClosedLitigationReason"));
      }
      if ((jsonObj.get("CompiledBySolicitorID") != null && !jsonObj.get("CompiledBySolicitorID").isJsonNull()) && !jsonObj.get("CompiledBySolicitorID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompiledBySolicitorID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompiledBySolicitorID").toString()));
      }
      if ((jsonObj.get("DisplayCompiledBySolicitor") != null && !jsonObj.get("DisplayCompiledBySolicitor").isJsonNull()) && !jsonObj.get("DisplayCompiledBySolicitor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DisplayCompiledBySolicitor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DisplayCompiledBySolicitor").toString()));
      }
      if ((jsonObj.get("EvictionOutcome") != null && !jsonObj.get("EvictionOutcome").isJsonNull()) && !jsonObj.get("EvictionOutcome").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `EvictionOutcome` to be a primitive type in the JSON string but got `%s`", jsonObj.get("EvictionOutcome").toString()));
      }
      // validate the optional field `EvictionOutcome`
      if (jsonObj.get("EvictionOutcome") != null && !jsonObj.get("EvictionOutcome").isJsonNull()) {
        EvictionOutcomeEnum.validateJsonElement(jsonObj.get("EvictionOutcome"));
      }
      if ((jsonObj.get("ExtraNotes") != null && !jsonObj.get("ExtraNotes").isJsonNull()) && !jsonObj.get("ExtraNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ExtraNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ExtraNotes").toString()));
      }
      if ((jsonObj.get("HearingOutcome") != null && !jsonObj.get("HearingOutcome").isJsonNull()) && !jsonObj.get("HearingOutcome").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `HearingOutcome` to be a primitive type in the JSON string but got `%s`", jsonObj.get("HearingOutcome").toString()));
      }
      if ((jsonObj.get("LitigationType") != null && !jsonObj.get("LitigationType").isJsonNull()) && !jsonObj.get("LitigationType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LitigationType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LitigationType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReportingReceivershipLitigationModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReportingReceivershipLitigationModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReportingReceivershipLitigationModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReportingReceivershipLitigationModel.class));

       return (TypeAdapter<T>) new TypeAdapter<ReportingReceivershipLitigationModel>() {
           @Override
           public void write(JsonWriter out, ReportingReceivershipLitigationModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReportingReceivershipLitigationModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReportingReceivershipLitigationModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReportingReceivershipLitigationModel
   * @throws IOException if the JSON string is invalid with respect to ReportingReceivershipLitigationModel
   */
  public static ReportingReceivershipLitigationModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReportingReceivershipLitigationModel.class);
  }

  /**
   * Convert an instance of ReportingReceivershipLitigationModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

