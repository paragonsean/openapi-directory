/*
 * ContentDepot
 * ContentDepot hosts a range of API’s that allow clients to manage, discover, and obtain content. The API spans many parts of the ContentDepot functionality including MetaPub (a.k.a. metadata distribution) and content management.  ## MetaPub  MetaPub collects, normalizes and distributes publicly available program, episode, and piece metadata through the public radio system. Backed by ContentDepot and its data model, MetaPub allows producers to supply metadata through various methods:  1. MetaPub Agents that collect producer metadata by \"crawling\" existing public feeds (e.g. C24, BBC) or the producer's production system (e.g. ATC, ME, TED Radio Hour). 2. Manually enter metadata in the ContentDepot Portal on each program and episode. 3. Publish/push the metadata to the MetaPub upload API and execute an ingest job.  MetaPub then distributes this data to stations through an electronic program guide (EPG model) for display on various listener devices such as smart phones, tablets, web streams, HD radios, RDBS enabled FM radios, and more. The EPG format is based on the RadioDNS specifications.  ### RadioDNS  The RadioDNS Service and Programme Information Specification ([ETSI TS 102 818 v3.4.1](https://www.etsi.org/deliver/etsi_ts/102800_102899/102818/03.04.01_60/ts_102818v030401p.pdf)) defines three primary documents: Service Information, Program Information, and Group Information. These documents, along with the core RadioDNS Hybrid Lookup for Radio Services Specification ([ETSI TS 103 270 v1.4.1](https://www.etsi.org/deliver/etsi_ts/103200_103299/103270/01.04.01_60/ts_103270v010401p.pdf)), define a system where an end listener device can dynamically discover program metadata and fetch the metadata via Internet Protocol (IP) requests. MetaPub's use of RadioDNS differs slightly in that MetaPub (a.k.a PRSS) acts as the \"service provider\" while the stations and related middleware act as the end devices. While this is not the primary use case of RadioDNS, the flexibility in the specification, service definitions, and DNS resolution allows this model to be easily represented. MetaPub provides both _National Metadata_ and _Station Metadata_.  It is strongly recommended that the related [RadioDNS specifications](https://radiodns.org/developers/documentation/) be read for implementation details, definitions, and required XML schemas.  ## ContentDepot Drive  ContentDepot Drive (CD Drive) provides a private, per customer file storage solution similar to other cloud storage solutions such as Google Drive, Box, and Dropbox. The CD Drive is used to stage content uploads such as metadata files, images, or segment audio before associating the content with specific programs or episodes.  CD Drive content can be referenced using a URI by some operations such as synchronizing metadata. There are two possible CD Drive URI formats supported: ID and hierarchical path. The ID reference takes the form ```cddrive:id:{value}``` where value is the integer ID of the file or folder being referenced. The hierarchical path reference takes the form ```cddrive://{path}``` where path is the full, UNIX style path to the file or folder starting with '/'. For example, two CD Drive URIs pointing to the same file may be ```cddrive:id:12345``` and ```cddrive:///show1/episode2/metadata.xml```. More information about URIs can be found at [Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier).  ## Authentication  The API currently uses OAuth 2.0.  All operations require ```cd:full``` access where the client access is only limited by the permissions of the ContentDepot user after authentication. Limiting access scope per client is not currently supported. 
 *
 * The version of the OpenAPI document: 2.0.0
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * A spot insertion for playing a series of spots when a cue is received during a program.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:41.535782-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SpotInsertion {
  public static final String SERIALIZED_NAME_BROADCAST_SERVICE_ID = "broadcastServiceId";
  @SerializedName(SERIALIZED_NAME_BROADCAST_SERVICE_ID)
  private Long broadcastServiceId;

  public static final String SERIALIZED_NAME_CREATED_DATE = "createdDate";
  @SerializedName(SERIALIZED_NAME_CREATED_DATE)
  private OffsetDateTime createdDate;

  public static final String SERIALIZED_NAME_CUE = "cue";
  @SerializedName(SERIALIZED_NAME_CUE)
  private String cue;

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private Long customerId;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private Integer duration;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private LocalDate endDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_PROGRAM_ID = "programId";
  @SerializedName(SERIALIZED_NAME_PROGRAM_ID)
  private Long programId;

  public static final String SERIALIZED_NAME_SPOTS = "spots";
  @SerializedName(SERIALIZED_NAME_SPOTS)
  private List<Long> spots = new ArrayList<>();

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private LocalDate startDate;

  public SpotInsertion() {
  }

  public SpotInsertion(
     OffsetDateTime createdDate, 
     Long customerId, 
     Long id
  ) {
    this();
    this.createdDate = createdDate;
    this.customerId = customerId;
    this.id = id;
  }

  public SpotInsertion broadcastServiceId(Long broadcastServiceId) {
    this.broadcastServiceId = broadcastServiceId;
    return this;
  }

  /**
   * The ID of the broadcast service for the spot insertion.
   * minimum: 0
   * @return broadcastServiceId
   */
  @javax.annotation.Nonnull
  public Long getBroadcastServiceId() {
    return broadcastServiceId;
  }

  public void setBroadcastServiceId(Long broadcastServiceId) {
    this.broadcastServiceId = broadcastServiceId;
  }


  /**
   * The date and time the spot insertion was created. Generated at creation.
   * @return createdDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedDate() {
    return createdDate;
  }



  public SpotInsertion cue(String cue) {
    this.cue = cue;
    return this;
  }

  /**
   * The cue that triggers the spot insertion.
   * @return cue
   */
  @javax.annotation.Nonnull
  public String getCue() {
    return cue;
  }

  public void setCue(String cue) {
    this.cue = cue;
  }


  /**
   * The ID of the customer who owns the spot insertion. Set to the logged-in customer at creation.
   * minimum: 0
   * @return customerId
   */
  @javax.annotation.Nullable
  public Long getCustomerId() {
    return customerId;
  }



  public SpotInsertion duration(Integer duration) {
    this.duration = duration;
    return this;
  }

  /**
   * The duration of the spot insertion.
   * @return duration
   */
  @javax.annotation.Nonnull
  public Integer getDuration() {
    return duration;
  }

  public void setDuration(Integer duration) {
    this.duration = duration;
  }


  public SpotInsertion endDate(LocalDate endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * The date the spot insertion ends. The time will be set to midnight Eastern Time.
   * @return endDate
   */
  @javax.annotation.Nonnull
  public LocalDate getEndDate() {
    return endDate;
  }

  public void setEndDate(LocalDate endDate) {
    this.endDate = endDate;
  }


  /**
   * The unique ID of the spot insertion. Generated at creation.
   * minimum: 0
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }



  public SpotInsertion programId(Long programId) {
    this.programId = programId;
    return this;
  }

  /**
   * The ID of the program for the spot insertion.
   * minimum: 0
   * @return programId
   */
  @javax.annotation.Nonnull
  public Long getProgramId() {
    return programId;
  }

  public void setProgramId(Long programId) {
    this.programId = programId;
  }


  public SpotInsertion spots(List<Long> spots) {
    this.spots = spots;
    return this;
  }

  public SpotInsertion addSpotsItem(Long spotsItem) {
    if (this.spots == null) {
      this.spots = new ArrayList<>();
    }
    this.spots.add(spotsItem);
    return this;
  }

  /**
   * The ordered list of spot IDs to play.
   * @return spots
   */
  @javax.annotation.Nonnull
  public List<Long> getSpots() {
    return spots;
  }

  public void setSpots(List<Long> spots) {
    this.spots = spots;
  }


  public SpotInsertion startDate(LocalDate startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * The date the spot insertion can start. The time will be set to midnight Eastern Time.
   * @return startDate
   */
  @javax.annotation.Nonnull
  public LocalDate getStartDate() {
    return startDate;
  }

  public void setStartDate(LocalDate startDate) {
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
    SpotInsertion spotInsertion = (SpotInsertion) o;
    return Objects.equals(this.broadcastServiceId, spotInsertion.broadcastServiceId) &&
        Objects.equals(this.createdDate, spotInsertion.createdDate) &&
        Objects.equals(this.cue, spotInsertion.cue) &&
        Objects.equals(this.customerId, spotInsertion.customerId) &&
        Objects.equals(this.duration, spotInsertion.duration) &&
        Objects.equals(this.endDate, spotInsertion.endDate) &&
        Objects.equals(this.id, spotInsertion.id) &&
        Objects.equals(this.programId, spotInsertion.programId) &&
        Objects.equals(this.spots, spotInsertion.spots) &&
        Objects.equals(this.startDate, spotInsertion.startDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(broadcastServiceId, createdDate, cue, customerId, duration, endDate, id, programId, spots, startDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SpotInsertion {\n");
    sb.append("    broadcastServiceId: ").append(toIndentedString(broadcastServiceId)).append("\n");
    sb.append("    createdDate: ").append(toIndentedString(createdDate)).append("\n");
    sb.append("    cue: ").append(toIndentedString(cue)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    programId: ").append(toIndentedString(programId)).append("\n");
    sb.append("    spots: ").append(toIndentedString(spots)).append("\n");
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
    openapiFields.add("broadcastServiceId");
    openapiFields.add("createdDate");
    openapiFields.add("cue");
    openapiFields.add("customerId");
    openapiFields.add("duration");
    openapiFields.add("endDate");
    openapiFields.add("id");
    openapiFields.add("programId");
    openapiFields.add("spots");
    openapiFields.add("startDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("broadcastServiceId");
    openapiRequiredFields.add("cue");
    openapiRequiredFields.add("duration");
    openapiRequiredFields.add("endDate");
    openapiRequiredFields.add("programId");
    openapiRequiredFields.add("spots");
    openapiRequiredFields.add("startDate");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SpotInsertion
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SpotInsertion.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SpotInsertion is not found in the empty JSON string", SpotInsertion.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SpotInsertion.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SpotInsertion` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SpotInsertion.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("cue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cue").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("spots") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("spots").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `spots` to be an array in the JSON string but got `%s`", jsonObj.get("spots").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SpotInsertion.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SpotInsertion' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SpotInsertion> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SpotInsertion.class));

       return (TypeAdapter<T>) new TypeAdapter<SpotInsertion>() {
           @Override
           public void write(JsonWriter out, SpotInsertion value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SpotInsertion read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SpotInsertion given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SpotInsertion
   * @throws IOException if the JSON string is invalid with respect to SpotInsertion
   */
  public static SpotInsertion fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SpotInsertion.class);
  }

  /**
   * Convert an instance of SpotInsertion to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

