/*
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
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
import org.openapitools.client.model.ApiCoreDtoDatapointsTrackingLinkSpecifics;
import org.openapitools.client.model.ApiCoreDtoDatapointsTrackingPixelSpecifics;
import org.openapitools.client.model.ApiCoreDtoTagsTag;

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
 * ApiCoreDtoDatapointsDatapoint
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:30.746224-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiCoreDtoDatapointsDatapoint {
  public static final String SERIALIZED_NAME_CREATION_DATE = "creationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private String creationDate;

  public static final String SERIALIZED_NAME_ENCODE_IP = "encodeIp";
  @SerializedName(SERIALIZED_NAME_ENCODE_IP)
  private Boolean encodeIp;

  public static final String SERIALIZED_NAME_FIFTH_CONVERSION_ID = "fifthConversionId";
  @SerializedName(SERIALIZED_NAME_FIFTH_CONVERSION_ID)
  private Long fifthConversionId;

  public static final String SERIALIZED_NAME_FIFTH_CONVERSION_NAME = "fifthConversionName";
  @SerializedName(SERIALIZED_NAME_FIFTH_CONVERSION_NAME)
  private String fifthConversionName;

  public static final String SERIALIZED_NAME_FIRST_CONVERSION_ID = "firstConversionId";
  @SerializedName(SERIALIZED_NAME_FIRST_CONVERSION_ID)
  private Long firstConversionId;

  public static final String SERIALIZED_NAME_FIRST_CONVERSION_NAME = "firstConversionName";
  @SerializedName(SERIALIZED_NAME_FIRST_CONVERSION_NAME)
  private String firstConversionName;

  public static final String SERIALIZED_NAME_FOURTH_CONVERSION_ID = "fourthConversionId";
  @SerializedName(SERIALIZED_NAME_FOURTH_CONVERSION_ID)
  private Long fourthConversionId;

  public static final String SERIALIZED_NAME_FOURTH_CONVERSION_NAME = "fourthConversionName";
  @SerializedName(SERIALIZED_NAME_FOURTH_CONVERSION_NAME)
  private String fourthConversionName;

  public static final String SERIALIZED_NAME_GROUP_ID = "groupId";
  @SerializedName(SERIALIZED_NAME_GROUP_ID)
  private Long groupId;

  public static final String SERIALIZED_NAME_GROUP_NAME = "groupName";
  @SerializedName(SERIALIZED_NAME_GROUP_NAME)
  private String groupName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_IS_PUBLIC = "isPublic";
  @SerializedName(SERIALIZED_NAME_IS_PUBLIC)
  private Boolean isPublic;

  public static final String SERIALIZED_NAME_IS_SECURED = "isSecured";
  @SerializedName(SERIALIZED_NAME_IS_SECURED)
  private Boolean isSecured;

  public static final String SERIALIZED_NAME_LIGHT_TRACKING = "lightTracking";
  @SerializedName(SERIALIZED_NAME_LIGHT_TRACKING)
  private Boolean lightTracking;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PREFERRED = "preferred";
  @SerializedName(SERIALIZED_NAME_PREFERRED)
  private Boolean preferred;

  public static final String SERIALIZED_NAME_REDIRECT_ONLY = "redirectOnly";
  @SerializedName(SERIALIZED_NAME_REDIRECT_ONLY)
  private Boolean redirectOnly;

  public static final String SERIALIZED_NAME_SECOND_CONVERSION_ID = "secondConversionId";
  @SerializedName(SERIALIZED_NAME_SECOND_CONVERSION_ID)
  private Long secondConversionId;

  public static final String SERIALIZED_NAME_SECOND_CONVERSION_NAME = "secondConversionName";
  @SerializedName(SERIALIZED_NAME_SECOND_CONVERSION_NAME)
  private String secondConversionName;

  /**
   * Gets or Sets status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    ACTIVE("Active"),
    
    PAUSED("Paused"),
    
    ABUSE("Abuse"),
    
    DELETED("Deleted");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<ApiCoreDtoTagsTag> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_THIRD_CONVERSION_ID = "thirdConversionId";
  @SerializedName(SERIALIZED_NAME_THIRD_CONVERSION_ID)
  private Long thirdConversionId;

  public static final String SERIALIZED_NAME_THIRD_CONVERSION_NAME = "thirdConversionName";
  @SerializedName(SERIALIZED_NAME_THIRD_CONVERSION_NAME)
  private String thirdConversionName;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TRACKING_CODE = "trackingCode";
  @SerializedName(SERIALIZED_NAME_TRACKING_CODE)
  private String trackingCode;

  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    TRACKING_LINK("TrackingLink"),
    
    TRACKING_PIXEL("TrackingPixel");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_TYPE_T_L = "typeTL";
  @SerializedName(SERIALIZED_NAME_TYPE_T_L)
  private ApiCoreDtoDatapointsTrackingLinkSpecifics typeTL;

  public static final String SERIALIZED_NAME_TYPE_T_P = "typeTP";
  @SerializedName(SERIALIZED_NAME_TYPE_T_P)
  private ApiCoreDtoDatapointsTrackingPixelSpecifics typeTP;

  public static final String SERIALIZED_NAME_WRITE_PERMITED = "writePermited";
  @SerializedName(SERIALIZED_NAME_WRITE_PERMITED)
  private Boolean writePermited;

  public ApiCoreDtoDatapointsDatapoint() {
  }

  public ApiCoreDtoDatapointsDatapoint creationDate(String creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   *  (A date in \&quot;YmdHis\&quot; format)
   * @return creationDate
   */
  @javax.annotation.Nullable
  public String getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(String creationDate) {
    this.creationDate = creationDate;
  }


  public ApiCoreDtoDatapointsDatapoint encodeIp(Boolean encodeIp) {
    this.encodeIp = encodeIp;
    return this;
  }

  /**
   * Get encodeIp
   * @return encodeIp
   */
  @javax.annotation.Nullable
  public Boolean getEncodeIp() {
    return encodeIp;
  }

  public void setEncodeIp(Boolean encodeIp) {
    this.encodeIp = encodeIp;
  }


  public ApiCoreDtoDatapointsDatapoint fifthConversionId(Long fifthConversionId) {
    this.fifthConversionId = fifthConversionId;
    return this;
  }

  /**
   * Get fifthConversionId
   * @return fifthConversionId
   */
  @javax.annotation.Nullable
  public Long getFifthConversionId() {
    return fifthConversionId;
  }

  public void setFifthConversionId(Long fifthConversionId) {
    this.fifthConversionId = fifthConversionId;
  }


  public ApiCoreDtoDatapointsDatapoint fifthConversionName(String fifthConversionName) {
    this.fifthConversionName = fifthConversionName;
    return this;
  }

  /**
   * Get fifthConversionName
   * @return fifthConversionName
   */
  @javax.annotation.Nullable
  public String getFifthConversionName() {
    return fifthConversionName;
  }

  public void setFifthConversionName(String fifthConversionName) {
    this.fifthConversionName = fifthConversionName;
  }


  public ApiCoreDtoDatapointsDatapoint firstConversionId(Long firstConversionId) {
    this.firstConversionId = firstConversionId;
    return this;
  }

  /**
   * Get firstConversionId
   * @return firstConversionId
   */
  @javax.annotation.Nullable
  public Long getFirstConversionId() {
    return firstConversionId;
  }

  public void setFirstConversionId(Long firstConversionId) {
    this.firstConversionId = firstConversionId;
  }


  public ApiCoreDtoDatapointsDatapoint firstConversionName(String firstConversionName) {
    this.firstConversionName = firstConversionName;
    return this;
  }

  /**
   * Get firstConversionName
   * @return firstConversionName
   */
  @javax.annotation.Nullable
  public String getFirstConversionName() {
    return firstConversionName;
  }

  public void setFirstConversionName(String firstConversionName) {
    this.firstConversionName = firstConversionName;
  }


  public ApiCoreDtoDatapointsDatapoint fourthConversionId(Long fourthConversionId) {
    this.fourthConversionId = fourthConversionId;
    return this;
  }

  /**
   * Get fourthConversionId
   * @return fourthConversionId
   */
  @javax.annotation.Nullable
  public Long getFourthConversionId() {
    return fourthConversionId;
  }

  public void setFourthConversionId(Long fourthConversionId) {
    this.fourthConversionId = fourthConversionId;
  }


  public ApiCoreDtoDatapointsDatapoint fourthConversionName(String fourthConversionName) {
    this.fourthConversionName = fourthConversionName;
    return this;
  }

  /**
   * Get fourthConversionName
   * @return fourthConversionName
   */
  @javax.annotation.Nullable
  public String getFourthConversionName() {
    return fourthConversionName;
  }

  public void setFourthConversionName(String fourthConversionName) {
    this.fourthConversionName = fourthConversionName;
  }


  public ApiCoreDtoDatapointsDatapoint groupId(Long groupId) {
    this.groupId = groupId;
    return this;
  }

  /**
   * Get groupId
   * @return groupId
   */
  @javax.annotation.Nullable
  public Long getGroupId() {
    return groupId;
  }

  public void setGroupId(Long groupId) {
    this.groupId = groupId;
  }


  public ApiCoreDtoDatapointsDatapoint groupName(String groupName) {
    this.groupName = groupName;
    return this;
  }

  /**
   * Get groupName
   * @return groupName
   */
  @javax.annotation.Nullable
  public String getGroupName() {
    return groupName;
  }

  public void setGroupName(String groupName) {
    this.groupName = groupName;
  }


  public ApiCoreDtoDatapointsDatapoint id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public ApiCoreDtoDatapointsDatapoint isPublic(Boolean isPublic) {
    this.isPublic = isPublic;
    return this;
  }

  /**
   * Get isPublic
   * @return isPublic
   */
  @javax.annotation.Nullable
  public Boolean getIsPublic() {
    return isPublic;
  }

  public void setIsPublic(Boolean isPublic) {
    this.isPublic = isPublic;
  }


  public ApiCoreDtoDatapointsDatapoint isSecured(Boolean isSecured) {
    this.isSecured = isSecured;
    return this;
  }

  /**
   * Get isSecured
   * @return isSecured
   */
  @javax.annotation.Nullable
  public Boolean getIsSecured() {
    return isSecured;
  }

  public void setIsSecured(Boolean isSecured) {
    this.isSecured = isSecured;
  }


  public ApiCoreDtoDatapointsDatapoint lightTracking(Boolean lightTracking) {
    this.lightTracking = lightTracking;
    return this;
  }

  /**
   * Get lightTracking
   * @return lightTracking
   */
  @javax.annotation.Nullable
  public Boolean getLightTracking() {
    return lightTracking;
  }

  public void setLightTracking(Boolean lightTracking) {
    this.lightTracking = lightTracking;
  }


  public ApiCoreDtoDatapointsDatapoint name(String name) {
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


  public ApiCoreDtoDatapointsDatapoint notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Get notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public ApiCoreDtoDatapointsDatapoint preferred(Boolean preferred) {
    this.preferred = preferred;
    return this;
  }

  /**
   * Get preferred
   * @return preferred
   */
  @javax.annotation.Nullable
  public Boolean getPreferred() {
    return preferred;
  }

  public void setPreferred(Boolean preferred) {
    this.preferred = preferred;
  }


  public ApiCoreDtoDatapointsDatapoint redirectOnly(Boolean redirectOnly) {
    this.redirectOnly = redirectOnly;
    return this;
  }

  /**
   * Get redirectOnly
   * @return redirectOnly
   */
  @javax.annotation.Nullable
  public Boolean getRedirectOnly() {
    return redirectOnly;
  }

  public void setRedirectOnly(Boolean redirectOnly) {
    this.redirectOnly = redirectOnly;
  }


  public ApiCoreDtoDatapointsDatapoint secondConversionId(Long secondConversionId) {
    this.secondConversionId = secondConversionId;
    return this;
  }

  /**
   * Get secondConversionId
   * @return secondConversionId
   */
  @javax.annotation.Nullable
  public Long getSecondConversionId() {
    return secondConversionId;
  }

  public void setSecondConversionId(Long secondConversionId) {
    this.secondConversionId = secondConversionId;
  }


  public ApiCoreDtoDatapointsDatapoint secondConversionName(String secondConversionName) {
    this.secondConversionName = secondConversionName;
    return this;
  }

  /**
   * Get secondConversionName
   * @return secondConversionName
   */
  @javax.annotation.Nullable
  public String getSecondConversionName() {
    return secondConversionName;
  }

  public void setSecondConversionName(String secondConversionName) {
    this.secondConversionName = secondConversionName;
  }


  public ApiCoreDtoDatapointsDatapoint status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public ApiCoreDtoDatapointsDatapoint tags(List<ApiCoreDtoTagsTag> tags) {
    this.tags = tags;
    return this;
  }

  public ApiCoreDtoDatapointsDatapoint addTagsItem(ApiCoreDtoTagsTag tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * Get tags
   * @return tags
   */
  @javax.annotation.Nullable
  public List<ApiCoreDtoTagsTag> getTags() {
    return tags;
  }

  public void setTags(List<ApiCoreDtoTagsTag> tags) {
    this.tags = tags;
  }


  public ApiCoreDtoDatapointsDatapoint thirdConversionId(Long thirdConversionId) {
    this.thirdConversionId = thirdConversionId;
    return this;
  }

  /**
   * Get thirdConversionId
   * @return thirdConversionId
   */
  @javax.annotation.Nullable
  public Long getThirdConversionId() {
    return thirdConversionId;
  }

  public void setThirdConversionId(Long thirdConversionId) {
    this.thirdConversionId = thirdConversionId;
  }


  public ApiCoreDtoDatapointsDatapoint thirdConversionName(String thirdConversionName) {
    this.thirdConversionName = thirdConversionName;
    return this;
  }

  /**
   * Get thirdConversionName
   * @return thirdConversionName
   */
  @javax.annotation.Nullable
  public String getThirdConversionName() {
    return thirdConversionName;
  }

  public void setThirdConversionName(String thirdConversionName) {
    this.thirdConversionName = thirdConversionName;
  }


  public ApiCoreDtoDatapointsDatapoint title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public ApiCoreDtoDatapointsDatapoint trackingCode(String trackingCode) {
    this.trackingCode = trackingCode;
    return this;
  }

  /**
   * Get trackingCode
   * @return trackingCode
   */
  @javax.annotation.Nullable
  public String getTrackingCode() {
    return trackingCode;
  }

  public void setTrackingCode(String trackingCode) {
    this.trackingCode = trackingCode;
  }


  public ApiCoreDtoDatapointsDatapoint type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public ApiCoreDtoDatapointsDatapoint typeTL(ApiCoreDtoDatapointsTrackingLinkSpecifics typeTL) {
    this.typeTL = typeTL;
    return this;
  }

  /**
   * Get typeTL
   * @return typeTL
   */
  @javax.annotation.Nullable
  public ApiCoreDtoDatapointsTrackingLinkSpecifics getTypeTL() {
    return typeTL;
  }

  public void setTypeTL(ApiCoreDtoDatapointsTrackingLinkSpecifics typeTL) {
    this.typeTL = typeTL;
  }


  public ApiCoreDtoDatapointsDatapoint typeTP(ApiCoreDtoDatapointsTrackingPixelSpecifics typeTP) {
    this.typeTP = typeTP;
    return this;
  }

  /**
   * Get typeTP
   * @return typeTP
   */
  @javax.annotation.Nullable
  public ApiCoreDtoDatapointsTrackingPixelSpecifics getTypeTP() {
    return typeTP;
  }

  public void setTypeTP(ApiCoreDtoDatapointsTrackingPixelSpecifics typeTP) {
    this.typeTP = typeTP;
  }


  public ApiCoreDtoDatapointsDatapoint writePermited(Boolean writePermited) {
    this.writePermited = writePermited;
    return this;
  }

  /**
   * Get writePermited
   * @return writePermited
   */
  @javax.annotation.Nullable
  public Boolean getWritePermited() {
    return writePermited;
  }

  public void setWritePermited(Boolean writePermited) {
    this.writePermited = writePermited;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiCoreDtoDatapointsDatapoint apiCoreDtoDatapointsDatapoint = (ApiCoreDtoDatapointsDatapoint) o;
    return Objects.equals(this.creationDate, apiCoreDtoDatapointsDatapoint.creationDate) &&
        Objects.equals(this.encodeIp, apiCoreDtoDatapointsDatapoint.encodeIp) &&
        Objects.equals(this.fifthConversionId, apiCoreDtoDatapointsDatapoint.fifthConversionId) &&
        Objects.equals(this.fifthConversionName, apiCoreDtoDatapointsDatapoint.fifthConversionName) &&
        Objects.equals(this.firstConversionId, apiCoreDtoDatapointsDatapoint.firstConversionId) &&
        Objects.equals(this.firstConversionName, apiCoreDtoDatapointsDatapoint.firstConversionName) &&
        Objects.equals(this.fourthConversionId, apiCoreDtoDatapointsDatapoint.fourthConversionId) &&
        Objects.equals(this.fourthConversionName, apiCoreDtoDatapointsDatapoint.fourthConversionName) &&
        Objects.equals(this.groupId, apiCoreDtoDatapointsDatapoint.groupId) &&
        Objects.equals(this.groupName, apiCoreDtoDatapointsDatapoint.groupName) &&
        Objects.equals(this.id, apiCoreDtoDatapointsDatapoint.id) &&
        Objects.equals(this.isPublic, apiCoreDtoDatapointsDatapoint.isPublic) &&
        Objects.equals(this.isSecured, apiCoreDtoDatapointsDatapoint.isSecured) &&
        Objects.equals(this.lightTracking, apiCoreDtoDatapointsDatapoint.lightTracking) &&
        Objects.equals(this.name, apiCoreDtoDatapointsDatapoint.name) &&
        Objects.equals(this.notes, apiCoreDtoDatapointsDatapoint.notes) &&
        Objects.equals(this.preferred, apiCoreDtoDatapointsDatapoint.preferred) &&
        Objects.equals(this.redirectOnly, apiCoreDtoDatapointsDatapoint.redirectOnly) &&
        Objects.equals(this.secondConversionId, apiCoreDtoDatapointsDatapoint.secondConversionId) &&
        Objects.equals(this.secondConversionName, apiCoreDtoDatapointsDatapoint.secondConversionName) &&
        Objects.equals(this.status, apiCoreDtoDatapointsDatapoint.status) &&
        Objects.equals(this.tags, apiCoreDtoDatapointsDatapoint.tags) &&
        Objects.equals(this.thirdConversionId, apiCoreDtoDatapointsDatapoint.thirdConversionId) &&
        Objects.equals(this.thirdConversionName, apiCoreDtoDatapointsDatapoint.thirdConversionName) &&
        Objects.equals(this.title, apiCoreDtoDatapointsDatapoint.title) &&
        Objects.equals(this.trackingCode, apiCoreDtoDatapointsDatapoint.trackingCode) &&
        Objects.equals(this.type, apiCoreDtoDatapointsDatapoint.type) &&
        Objects.equals(this.typeTL, apiCoreDtoDatapointsDatapoint.typeTL) &&
        Objects.equals(this.typeTP, apiCoreDtoDatapointsDatapoint.typeTP) &&
        Objects.equals(this.writePermited, apiCoreDtoDatapointsDatapoint.writePermited);
  }

  @Override
  public int hashCode() {
    return Objects.hash(creationDate, encodeIp, fifthConversionId, fifthConversionName, firstConversionId, firstConversionName, fourthConversionId, fourthConversionName, groupId, groupName, id, isPublic, isSecured, lightTracking, name, notes, preferred, redirectOnly, secondConversionId, secondConversionName, status, tags, thirdConversionId, thirdConversionName, title, trackingCode, type, typeTL, typeTP, writePermited);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiCoreDtoDatapointsDatapoint {\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    encodeIp: ").append(toIndentedString(encodeIp)).append("\n");
    sb.append("    fifthConversionId: ").append(toIndentedString(fifthConversionId)).append("\n");
    sb.append("    fifthConversionName: ").append(toIndentedString(fifthConversionName)).append("\n");
    sb.append("    firstConversionId: ").append(toIndentedString(firstConversionId)).append("\n");
    sb.append("    firstConversionName: ").append(toIndentedString(firstConversionName)).append("\n");
    sb.append("    fourthConversionId: ").append(toIndentedString(fourthConversionId)).append("\n");
    sb.append("    fourthConversionName: ").append(toIndentedString(fourthConversionName)).append("\n");
    sb.append("    groupId: ").append(toIndentedString(groupId)).append("\n");
    sb.append("    groupName: ").append(toIndentedString(groupName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isPublic: ").append(toIndentedString(isPublic)).append("\n");
    sb.append("    isSecured: ").append(toIndentedString(isSecured)).append("\n");
    sb.append("    lightTracking: ").append(toIndentedString(lightTracking)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    preferred: ").append(toIndentedString(preferred)).append("\n");
    sb.append("    redirectOnly: ").append(toIndentedString(redirectOnly)).append("\n");
    sb.append("    secondConversionId: ").append(toIndentedString(secondConversionId)).append("\n");
    sb.append("    secondConversionName: ").append(toIndentedString(secondConversionName)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    thirdConversionId: ").append(toIndentedString(thirdConversionId)).append("\n");
    sb.append("    thirdConversionName: ").append(toIndentedString(thirdConversionName)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    trackingCode: ").append(toIndentedString(trackingCode)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    typeTL: ").append(toIndentedString(typeTL)).append("\n");
    sb.append("    typeTP: ").append(toIndentedString(typeTP)).append("\n");
    sb.append("    writePermited: ").append(toIndentedString(writePermited)).append("\n");
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
    openapiFields.add("creationDate");
    openapiFields.add("encodeIp");
    openapiFields.add("fifthConversionId");
    openapiFields.add("fifthConversionName");
    openapiFields.add("firstConversionId");
    openapiFields.add("firstConversionName");
    openapiFields.add("fourthConversionId");
    openapiFields.add("fourthConversionName");
    openapiFields.add("groupId");
    openapiFields.add("groupName");
    openapiFields.add("id");
    openapiFields.add("isPublic");
    openapiFields.add("isSecured");
    openapiFields.add("lightTracking");
    openapiFields.add("name");
    openapiFields.add("notes");
    openapiFields.add("preferred");
    openapiFields.add("redirectOnly");
    openapiFields.add("secondConversionId");
    openapiFields.add("secondConversionName");
    openapiFields.add("status");
    openapiFields.add("tags");
    openapiFields.add("thirdConversionId");
    openapiFields.add("thirdConversionName");
    openapiFields.add("title");
    openapiFields.add("trackingCode");
    openapiFields.add("type");
    openapiFields.add("typeTL");
    openapiFields.add("typeTP");
    openapiFields.add("writePermited");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiCoreDtoDatapointsDatapoint
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiCoreDtoDatapointsDatapoint.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiCoreDtoDatapointsDatapoint is not found in the empty JSON string", ApiCoreDtoDatapointsDatapoint.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiCoreDtoDatapointsDatapoint.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiCoreDtoDatapointsDatapoint` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("creationDate") != null && !jsonObj.get("creationDate").isJsonNull()) && !jsonObj.get("creationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creationDate").toString()));
      }
      if ((jsonObj.get("fifthConversionName") != null && !jsonObj.get("fifthConversionName").isJsonNull()) && !jsonObj.get("fifthConversionName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fifthConversionName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fifthConversionName").toString()));
      }
      if ((jsonObj.get("firstConversionName") != null && !jsonObj.get("firstConversionName").isJsonNull()) && !jsonObj.get("firstConversionName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstConversionName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstConversionName").toString()));
      }
      if ((jsonObj.get("fourthConversionName") != null && !jsonObj.get("fourthConversionName").isJsonNull()) && !jsonObj.get("fourthConversionName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fourthConversionName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fourthConversionName").toString()));
      }
      if ((jsonObj.get("groupName") != null && !jsonObj.get("groupName").isJsonNull()) && !jsonObj.get("groupName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupName").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("secondConversionName") != null && !jsonObj.get("secondConversionName").isJsonNull()) && !jsonObj.get("secondConversionName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secondConversionName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secondConversionName").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        JsonArray jsonArraytags = jsonObj.getAsJsonArray("tags");
        if (jsonArraytags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
          }

          // validate the optional field `tags` (array)
          for (int i = 0; i < jsonArraytags.size(); i++) {
            ApiCoreDtoTagsTag.validateJsonElement(jsonArraytags.get(i));
          };
        }
      }
      if ((jsonObj.get("thirdConversionName") != null && !jsonObj.get("thirdConversionName").isJsonNull()) && !jsonObj.get("thirdConversionName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `thirdConversionName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("thirdConversionName").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("trackingCode") != null && !jsonObj.get("trackingCode").isJsonNull()) && !jsonObj.get("trackingCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `trackingCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("trackingCode").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      // validate the optional field `typeTL`
      if (jsonObj.get("typeTL") != null && !jsonObj.get("typeTL").isJsonNull()) {
        ApiCoreDtoDatapointsTrackingLinkSpecifics.validateJsonElement(jsonObj.get("typeTL"));
      }
      // validate the optional field `typeTP`
      if (jsonObj.get("typeTP") != null && !jsonObj.get("typeTP").isJsonNull()) {
        ApiCoreDtoDatapointsTrackingPixelSpecifics.validateJsonElement(jsonObj.get("typeTP"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiCoreDtoDatapointsDatapoint.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiCoreDtoDatapointsDatapoint' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiCoreDtoDatapointsDatapoint> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiCoreDtoDatapointsDatapoint.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiCoreDtoDatapointsDatapoint>() {
           @Override
           public void write(JsonWriter out, ApiCoreDtoDatapointsDatapoint value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiCoreDtoDatapointsDatapoint read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiCoreDtoDatapointsDatapoint given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiCoreDtoDatapointsDatapoint
   * @throws IOException if the JSON string is invalid with respect to ApiCoreDtoDatapointsDatapoint
   */
  public static ApiCoreDtoDatapointsDatapoint fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiCoreDtoDatapointsDatapoint.class);
  }

  /**
   * Convert an instance of ApiCoreDtoDatapointsDatapoint to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

