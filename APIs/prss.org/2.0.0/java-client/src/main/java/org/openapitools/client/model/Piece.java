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
 * The metadata about a \&quot;piece\&quot; which may be a story, song, report, etc.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:41.535782-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Piece {
  public static final String SERIALIZED_NAME_CONTRIBUTOR = "contributor";
  @SerializedName(SERIALIZED_NAME_CONTRIBUTOR)
  private String contributor;

  public static final String SERIALIZED_NAME_CREATED_DATE = "createdDate";
  @SerializedName(SERIALIZED_NAME_CREATED_DATE)
  private OffsetDateTime createdDate;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EPISODE_ID = "episodeId";
  @SerializedName(SERIALIZED_NAME_EPISODE_ID)
  private Long episodeId;

  public static final String SERIALIZED_NAME_FULL_DESCRIPTION = "fullDescription";
  @SerializedName(SERIALIZED_NAME_FULL_DESCRIPTION)
  private String fullDescription;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_IMAGE_CD_DRIVE_URI = "imageCdDriveUri";
  @SerializedName(SERIALIZED_NAME_IMAGE_CD_DRIVE_URI)
  private String imageCdDriveUri;

  public static final String SERIALIZED_NAME_IMAGE_FILE_NAME = "imageFileName";
  @SerializedName(SERIALIZED_NAME_IMAGE_FILE_NAME)
  private String imageFileName;

  public static final String SERIALIZED_NAME_IMAGE_FILE_SIZE = "imageFileSize";
  @SerializedName(SERIALIZED_NAME_IMAGE_FILE_SIZE)
  private Long imageFileSize;

  public static final String SERIALIZED_NAME_IMAGE_ORIGINAL_FILE_NAME = "imageOriginalFileName";
  @SerializedName(SERIALIZED_NAME_IMAGE_ORIGINAL_FILE_NAME)
  private String imageOriginalFileName;

  public static final String SERIALIZED_NAME_LAST_MODIFIED_DATE = "lastModifiedDate";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED_DATE)
  private OffsetDateTime lastModifiedDate;

  public static final String SERIALIZED_NAME_RELATIVE_END_TIME = "relativeEndTime";
  @SerializedName(SERIALIZED_NAME_RELATIVE_END_TIME)
  private Integer relativeEndTime;

  public static final String SERIALIZED_NAME_RELATIVE_START_TIME = "relativeStartTime";
  @SerializedName(SERIALIZED_NAME_RELATIVE_START_TIME)
  private Integer relativeStartTime;

  public static final String SERIALIZED_NAME_SEGMENT_NUMBER = "segmentNumber";
  @SerializedName(SERIALIZED_NAME_SEGMENT_NUMBER)
  private Integer segmentNumber;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public Piece() {
  }

  public Piece(
     OffsetDateTime createdDate, 
     Long id, 
     OffsetDateTime lastModifiedDate
  ) {
    this();
    this.createdDate = createdDate;
    this.id = id;
    this.lastModifiedDate = lastModifiedDate;
  }

  public Piece contributor(String contributor) {
    this.contributor = contributor;
    return this;
  }

  /**
   * The artist or contributor name.
   * @return contributor
   */
  @javax.annotation.Nullable
  public String getContributor() {
    return contributor;
  }

  public void setContributor(String contributor) {
    this.contributor = contributor;
  }


  /**
   * The date the piece was created. Generated at creation.
   * @return createdDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedDate() {
    return createdDate;
  }



  public Piece description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The short description of the piece.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Piece episodeId(Long episodeId) {
    this.episodeId = episodeId;
    return this;
  }

  /**
   * The ID of the episode that owns the piece.
   * minimum: 0
   * @return episodeId
   */
  @javax.annotation.Nonnull
  public Long getEpisodeId() {
    return episodeId;
  }

  public void setEpisodeId(Long episodeId) {
    this.episodeId = episodeId;
  }


  public Piece fullDescription(String fullDescription) {
    this.fullDescription = fullDescription;
    return this;
  }

  /**
   * The long description of the piece.
   * @return fullDescription
   */
  @javax.annotation.Nullable
  public String getFullDescription() {
    return fullDescription;
  }

  public void setFullDescription(String fullDescription) {
    this.fullDescription = fullDescription;
  }


  /**
   * The unique ID of the piece. Generated at creation.
   * minimum: 0
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }



  public Piece imageCdDriveUri(String imageCdDriveUri) {
    this.imageCdDriveUri = imageCdDriveUri;
    return this;
  }

  /**
   * The URI to the piece image content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;. This property is only used on modification and is not returned.
   * @return imageCdDriveUri
   */
  @javax.annotation.Nullable
  public String getImageCdDriveUri() {
    return imageCdDriveUri;
  }

  public void setImageCdDriveUri(String imageCdDriveUri) {
    this.imageCdDriveUri = imageCdDriveUri;
  }


  public Piece imageFileName(String imageFileName) {
    this.imageFileName = imageFileName;
    return this;
  }

  /**
   * The name of the piece image file. Generated at creation.
   * @return imageFileName
   */
  @javax.annotation.Nullable
  public String getImageFileName() {
    return imageFileName;
  }

  public void setImageFileName(String imageFileName) {
    this.imageFileName = imageFileName;
  }


  public Piece imageFileSize(Long imageFileSize) {
    this.imageFileSize = imageFileSize;
    return this;
  }

  /**
   * The size of the piece image file in bytes. Generated at creation.
   * @return imageFileSize
   */
  @javax.annotation.Nullable
  public Long getImageFileSize() {
    return imageFileSize;
  }

  public void setImageFileSize(Long imageFileSize) {
    this.imageFileSize = imageFileSize;
  }


  public Piece imageOriginalFileName(String imageOriginalFileName) {
    this.imageOriginalFileName = imageOriginalFileName;
    return this;
  }

  /**
   * The user&#39;s original name of the piece image file.
   * @return imageOriginalFileName
   */
  @javax.annotation.Nullable
  public String getImageOriginalFileName() {
    return imageOriginalFileName;
  }

  public void setImageOriginalFileName(String imageOriginalFileName) {
    this.imageOriginalFileName = imageOriginalFileName;
  }


  /**
   * The date the piece was last modified/updated. Automatically updated on any write operation.
   * @return lastModifiedDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastModifiedDate() {
    return lastModifiedDate;
  }



  public Piece relativeEndTime(Integer relativeEndTime) {
    this.relativeEndTime = relativeEndTime;
    return this;
  }

  /**
   * Seconds relative to the start of the episode.
   * @return relativeEndTime
   */
  @javax.annotation.Nonnull
  public Integer getRelativeEndTime() {
    return relativeEndTime;
  }

  public void setRelativeEndTime(Integer relativeEndTime) {
    this.relativeEndTime = relativeEndTime;
  }


  public Piece relativeStartTime(Integer relativeStartTime) {
    this.relativeStartTime = relativeStartTime;
    return this;
  }

  /**
   * Seconds relative to the start of the episode.
   * @return relativeStartTime
   */
  @javax.annotation.Nonnull
  public Integer getRelativeStartTime() {
    return relativeStartTime;
  }

  public void setRelativeStartTime(Integer relativeStartTime) {
    this.relativeStartTime = relativeStartTime;
  }


  public Piece segmentNumber(Integer segmentNumber) {
    this.segmentNumber = segmentNumber;
    return this;
  }

  /**
   * The number of the segment that this piece is in, starting with 1. This is an optional field but it can be used to provide more detail by linking the piece to a specific audio segment.
   * minimum: 1
   * @return segmentNumber
   */
  @javax.annotation.Nullable
  public Integer getSegmentNumber() {
    return segmentNumber;
  }

  public void setSegmentNumber(Integer segmentNumber) {
    this.segmentNumber = segmentNumber;
  }


  public Piece title(String title) {
    this.title = title;
    return this;
  }

  /**
   * The human readable title of the piece that is normally displayed on an end user&#39;s device.
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Piece piece = (Piece) o;
    return Objects.equals(this.contributor, piece.contributor) &&
        Objects.equals(this.createdDate, piece.createdDate) &&
        Objects.equals(this.description, piece.description) &&
        Objects.equals(this.episodeId, piece.episodeId) &&
        Objects.equals(this.fullDescription, piece.fullDescription) &&
        Objects.equals(this.id, piece.id) &&
        Objects.equals(this.imageCdDriveUri, piece.imageCdDriveUri) &&
        Objects.equals(this.imageFileName, piece.imageFileName) &&
        Objects.equals(this.imageFileSize, piece.imageFileSize) &&
        Objects.equals(this.imageOriginalFileName, piece.imageOriginalFileName) &&
        Objects.equals(this.lastModifiedDate, piece.lastModifiedDate) &&
        Objects.equals(this.relativeEndTime, piece.relativeEndTime) &&
        Objects.equals(this.relativeStartTime, piece.relativeStartTime) &&
        Objects.equals(this.segmentNumber, piece.segmentNumber) &&
        Objects.equals(this.title, piece.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contributor, createdDate, description, episodeId, fullDescription, id, imageCdDriveUri, imageFileName, imageFileSize, imageOriginalFileName, lastModifiedDate, relativeEndTime, relativeStartTime, segmentNumber, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Piece {\n");
    sb.append("    contributor: ").append(toIndentedString(contributor)).append("\n");
    sb.append("    createdDate: ").append(toIndentedString(createdDate)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    episodeId: ").append(toIndentedString(episodeId)).append("\n");
    sb.append("    fullDescription: ").append(toIndentedString(fullDescription)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    imageCdDriveUri: ").append(toIndentedString(imageCdDriveUri)).append("\n");
    sb.append("    imageFileName: ").append(toIndentedString(imageFileName)).append("\n");
    sb.append("    imageFileSize: ").append(toIndentedString(imageFileSize)).append("\n");
    sb.append("    imageOriginalFileName: ").append(toIndentedString(imageOriginalFileName)).append("\n");
    sb.append("    lastModifiedDate: ").append(toIndentedString(lastModifiedDate)).append("\n");
    sb.append("    relativeEndTime: ").append(toIndentedString(relativeEndTime)).append("\n");
    sb.append("    relativeStartTime: ").append(toIndentedString(relativeStartTime)).append("\n");
    sb.append("    segmentNumber: ").append(toIndentedString(segmentNumber)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("contributor");
    openapiFields.add("createdDate");
    openapiFields.add("description");
    openapiFields.add("episodeId");
    openapiFields.add("fullDescription");
    openapiFields.add("id");
    openapiFields.add("imageCdDriveUri");
    openapiFields.add("imageFileName");
    openapiFields.add("imageFileSize");
    openapiFields.add("imageOriginalFileName");
    openapiFields.add("lastModifiedDate");
    openapiFields.add("relativeEndTime");
    openapiFields.add("relativeStartTime");
    openapiFields.add("segmentNumber");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("episodeId");
    openapiRequiredFields.add("relativeEndTime");
    openapiRequiredFields.add("relativeStartTime");
    openapiRequiredFields.add("title");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Piece
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Piece.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Piece is not found in the empty JSON string", Piece.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Piece.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Piece` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Piece.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("contributor") != null && !jsonObj.get("contributor").isJsonNull()) && !jsonObj.get("contributor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contributor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contributor").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("fullDescription") != null && !jsonObj.get("fullDescription").isJsonNull()) && !jsonObj.get("fullDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fullDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fullDescription").toString()));
      }
      if ((jsonObj.get("imageCdDriveUri") != null && !jsonObj.get("imageCdDriveUri").isJsonNull()) && !jsonObj.get("imageCdDriveUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageCdDriveUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageCdDriveUri").toString()));
      }
      if ((jsonObj.get("imageFileName") != null && !jsonObj.get("imageFileName").isJsonNull()) && !jsonObj.get("imageFileName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageFileName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageFileName").toString()));
      }
      if ((jsonObj.get("imageOriginalFileName") != null && !jsonObj.get("imageOriginalFileName").isJsonNull()) && !jsonObj.get("imageOriginalFileName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageOriginalFileName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageOriginalFileName").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Piece.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Piece' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Piece> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Piece.class));

       return (TypeAdapter<T>) new TypeAdapter<Piece>() {
           @Override
           public void write(JsonWriter out, Piece value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Piece read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Piece given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Piece
   * @throws IOException if the JSON string is invalid with respect to Piece
   */
  public static Piece fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Piece.class);
  }

  /**
   * Convert an instance of Piece to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

