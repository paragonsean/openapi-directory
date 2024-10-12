/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import java.util.Arrays;
import org.openapitools.client.model.Blobstore2Info;
import org.openapitools.client.model.ObjectId;

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
 * A sequence of media data references representing composite data. Introduced to support Bigstore composite objects. For details, visit http://go/bigstore-composites.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompositeMedia {
  public static final String SERIALIZED_NAME_BLOB_REF = "blobRef";
  @SerializedName(SERIALIZED_NAME_BLOB_REF)
  private byte[] blobRef;

  public static final String SERIALIZED_NAME_BLOBSTORE2_INFO = "blobstore2Info";
  @SerializedName(SERIALIZED_NAME_BLOBSTORE2_INFO)
  private Blobstore2Info blobstore2Info;

  public static final String SERIALIZED_NAME_COSMO_BINARY_REFERENCE = "cosmoBinaryReference";
  @SerializedName(SERIALIZED_NAME_COSMO_BINARY_REFERENCE)
  private byte[] cosmoBinaryReference;

  public static final String SERIALIZED_NAME_CRC32C_HASH = "crc32cHash";
  @SerializedName(SERIALIZED_NAME_CRC32C_HASH)
  private Integer crc32cHash;

  public static final String SERIALIZED_NAME_INLINE = "inline";
  @SerializedName(SERIALIZED_NAME_INLINE)
  private byte[] inline;

  public static final String SERIALIZED_NAME_LENGTH = "length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private String length;

  public static final String SERIALIZED_NAME_MD5_HASH = "md5Hash";
  @SerializedName(SERIALIZED_NAME_MD5_HASH)
  private byte[] md5Hash;

  public static final String SERIALIZED_NAME_OBJECT_ID = "objectId";
  @SerializedName(SERIALIZED_NAME_OBJECT_ID)
  private ObjectId objectId;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  /**
   * Describes what the field reference contains.
   */
  @JsonAdapter(ReferenceTypeEnum.Adapter.class)
  public enum ReferenceTypeEnum {
    PATH("PATH"),
    
    BLOB_REF("BLOB_REF"),
    
    INLINE("INLINE"),
    
    BIGSTORE_REF("BIGSTORE_REF"),
    
    COSMO_BINARY_REFERENCE("COSMO_BINARY_REFERENCE");

    private String value;

    ReferenceTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ReferenceTypeEnum fromValue(String value) {
      for (ReferenceTypeEnum b : ReferenceTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ReferenceTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ReferenceTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ReferenceTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ReferenceTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ReferenceTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REFERENCE_TYPE = "referenceType";
  @SerializedName(SERIALIZED_NAME_REFERENCE_TYPE)
  private ReferenceTypeEnum referenceType;

  public static final String SERIALIZED_NAME_SHA1_HASH = "sha1Hash";
  @SerializedName(SERIALIZED_NAME_SHA1_HASH)
  private byte[] sha1Hash;

  public CompositeMedia() {
  }

  public CompositeMedia blobRef(byte[] blobRef) {
    this.blobRef = blobRef;
    return this;
  }

  /**
   * Blobstore v1 reference, set if reference_type is BLOBSTORE_REF This should be the byte representation of a blobstore.BlobRef. Since Blobstore is deprecating v1, use blobstore2_info instead. For now, any v2 blob will also be represented in this field as v1 BlobRef.
   * @return blobRef
   */
  @javax.annotation.Nullable
  public byte[] getBlobRef() {
    return blobRef;
  }

  public void setBlobRef(byte[] blobRef) {
    this.blobRef = blobRef;
  }


  public CompositeMedia blobstore2Info(Blobstore2Info blobstore2Info) {
    this.blobstore2Info = blobstore2Info;
    return this;
  }

  /**
   * Get blobstore2Info
   * @return blobstore2Info
   */
  @javax.annotation.Nullable
  public Blobstore2Info getBlobstore2Info() {
    return blobstore2Info;
  }

  public void setBlobstore2Info(Blobstore2Info blobstore2Info) {
    this.blobstore2Info = blobstore2Info;
  }


  public CompositeMedia cosmoBinaryReference(byte[] cosmoBinaryReference) {
    this.cosmoBinaryReference = cosmoBinaryReference;
    return this;
  }

  /**
   * A binary data reference for a media download. Serves as a technology-agnostic binary reference in some Google infrastructure. This value is a serialized storage_cosmo.BinaryReference proto. Storing it as bytes is a hack to get around the fact that the cosmo proto (as well as others it includes) doesn&#39;t support JavaScript. This prevents us from including the actual type of this field.
   * @return cosmoBinaryReference
   */
  @javax.annotation.Nullable
  public byte[] getCosmoBinaryReference() {
    return cosmoBinaryReference;
  }

  public void setCosmoBinaryReference(byte[] cosmoBinaryReference) {
    this.cosmoBinaryReference = cosmoBinaryReference;
  }


  public CompositeMedia crc32cHash(Integer crc32cHash) {
    this.crc32cHash = crc32cHash;
    return this;
  }

  /**
   * crc32.c hash for the payload.
   * @return crc32cHash
   */
  @javax.annotation.Nullable
  public Integer getCrc32cHash() {
    return crc32cHash;
  }

  public void setCrc32cHash(Integer crc32cHash) {
    this.crc32cHash = crc32cHash;
  }


  public CompositeMedia inline(byte[] inline) {
    this.inline = inline;
    return this;
  }

  /**
   * Media data, set if reference_type is INLINE
   * @return inline
   */
  @javax.annotation.Nullable
  public byte[] getInline() {
    return inline;
  }

  public void setInline(byte[] inline) {
    this.inline = inline;
  }


  public CompositeMedia length(String length) {
    this.length = length;
    return this;
  }

  /**
   * Size of the data, in bytes
   * @return length
   */
  @javax.annotation.Nullable
  public String getLength() {
    return length;
  }

  public void setLength(String length) {
    this.length = length;
  }


  public CompositeMedia md5Hash(byte[] md5Hash) {
    this.md5Hash = md5Hash;
    return this;
  }

  /**
   * MD5 hash for the payload.
   * @return md5Hash
   */
  @javax.annotation.Nullable
  public byte[] getMd5Hash() {
    return md5Hash;
  }

  public void setMd5Hash(byte[] md5Hash) {
    this.md5Hash = md5Hash;
  }


  public CompositeMedia objectId(ObjectId objectId) {
    this.objectId = objectId;
    return this;
  }

  /**
   * Get objectId
   * @return objectId
   */
  @javax.annotation.Nullable
  public ObjectId getObjectId() {
    return objectId;
  }

  public void setObjectId(ObjectId objectId) {
    this.objectId = objectId;
  }


  public CompositeMedia path(String path) {
    this.path = path;
    return this;
  }

  /**
   * Path to the data, set if reference_type is PATH
   * @return path
   */
  @javax.annotation.Nullable
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public CompositeMedia referenceType(ReferenceTypeEnum referenceType) {
    this.referenceType = referenceType;
    return this;
  }

  /**
   * Describes what the field reference contains.
   * @return referenceType
   */
  @javax.annotation.Nullable
  public ReferenceTypeEnum getReferenceType() {
    return referenceType;
  }

  public void setReferenceType(ReferenceTypeEnum referenceType) {
    this.referenceType = referenceType;
  }


  public CompositeMedia sha1Hash(byte[] sha1Hash) {
    this.sha1Hash = sha1Hash;
    return this;
  }

  /**
   * SHA-1 hash for the payload.
   * @return sha1Hash
   */
  @javax.annotation.Nullable
  public byte[] getSha1Hash() {
    return sha1Hash;
  }

  public void setSha1Hash(byte[] sha1Hash) {
    this.sha1Hash = sha1Hash;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompositeMedia compositeMedia = (CompositeMedia) o;
    return Arrays.equals(this.blobRef, compositeMedia.blobRef) &&
        Objects.equals(this.blobstore2Info, compositeMedia.blobstore2Info) &&
        Arrays.equals(this.cosmoBinaryReference, compositeMedia.cosmoBinaryReference) &&
        Objects.equals(this.crc32cHash, compositeMedia.crc32cHash) &&
        Arrays.equals(this.inline, compositeMedia.inline) &&
        Objects.equals(this.length, compositeMedia.length) &&
        Arrays.equals(this.md5Hash, compositeMedia.md5Hash) &&
        Objects.equals(this.objectId, compositeMedia.objectId) &&
        Objects.equals(this.path, compositeMedia.path) &&
        Objects.equals(this.referenceType, compositeMedia.referenceType) &&
        Arrays.equals(this.sha1Hash, compositeMedia.sha1Hash);
  }

  @Override
  public int hashCode() {
    return Objects.hash(Arrays.hashCode(blobRef), blobstore2Info, Arrays.hashCode(cosmoBinaryReference), crc32cHash, Arrays.hashCode(inline), length, Arrays.hashCode(md5Hash), objectId, path, referenceType, Arrays.hashCode(sha1Hash));
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompositeMedia {\n");
    sb.append("    blobRef: ").append(toIndentedString(blobRef)).append("\n");
    sb.append("    blobstore2Info: ").append(toIndentedString(blobstore2Info)).append("\n");
    sb.append("    cosmoBinaryReference: ").append(toIndentedString(cosmoBinaryReference)).append("\n");
    sb.append("    crc32cHash: ").append(toIndentedString(crc32cHash)).append("\n");
    sb.append("    inline: ").append(toIndentedString(inline)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    md5Hash: ").append(toIndentedString(md5Hash)).append("\n");
    sb.append("    objectId: ").append(toIndentedString(objectId)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    referenceType: ").append(toIndentedString(referenceType)).append("\n");
    sb.append("    sha1Hash: ").append(toIndentedString(sha1Hash)).append("\n");
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
    openapiFields.add("blobRef");
    openapiFields.add("blobstore2Info");
    openapiFields.add("cosmoBinaryReference");
    openapiFields.add("crc32cHash");
    openapiFields.add("inline");
    openapiFields.add("length");
    openapiFields.add("md5Hash");
    openapiFields.add("objectId");
    openapiFields.add("path");
    openapiFields.add("referenceType");
    openapiFields.add("sha1Hash");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompositeMedia
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompositeMedia.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompositeMedia is not found in the empty JSON string", CompositeMedia.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompositeMedia.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompositeMedia` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `blobstore2Info`
      if (jsonObj.get("blobstore2Info") != null && !jsonObj.get("blobstore2Info").isJsonNull()) {
        Blobstore2Info.validateJsonElement(jsonObj.get("blobstore2Info"));
      }
      if ((jsonObj.get("length") != null && !jsonObj.get("length").isJsonNull()) && !jsonObj.get("length").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `length` to be a primitive type in the JSON string but got `%s`", jsonObj.get("length").toString()));
      }
      // validate the optional field `objectId`
      if (jsonObj.get("objectId") != null && !jsonObj.get("objectId").isJsonNull()) {
        ObjectId.validateJsonElement(jsonObj.get("objectId"));
      }
      if ((jsonObj.get("path") != null && !jsonObj.get("path").isJsonNull()) && !jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      if ((jsonObj.get("referenceType") != null && !jsonObj.get("referenceType").isJsonNull()) && !jsonObj.get("referenceType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referenceType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referenceType").toString()));
      }
      // validate the optional field `referenceType`
      if (jsonObj.get("referenceType") != null && !jsonObj.get("referenceType").isJsonNull()) {
        ReferenceTypeEnum.validateJsonElement(jsonObj.get("referenceType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompositeMedia.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompositeMedia' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompositeMedia> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompositeMedia.class));

       return (TypeAdapter<T>) new TypeAdapter<CompositeMedia>() {
           @Override
           public void write(JsonWriter out, CompositeMedia value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompositeMedia read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompositeMedia given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompositeMedia
   * @throws IOException if the JSON string is invalid with respect to CompositeMedia
   */
  public static CompositeMedia fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompositeMedia.class);
  }

  /**
   * Convert an instance of CompositeMedia to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

