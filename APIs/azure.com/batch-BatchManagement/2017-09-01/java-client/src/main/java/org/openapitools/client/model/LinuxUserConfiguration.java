/*
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
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
 * LinuxUserConfiguration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LinuxUserConfiguration {
  public static final String SERIALIZED_NAME_GID = "gid";
  @SerializedName(SERIALIZED_NAME_GID)
  private Integer gid;

  public static final String SERIALIZED_NAME_SSH_PRIVATE_KEY = "sshPrivateKey";
  @SerializedName(SERIALIZED_NAME_SSH_PRIVATE_KEY)
  private String sshPrivateKey;

  public static final String SERIALIZED_NAME_UID = "uid";
  @SerializedName(SERIALIZED_NAME_UID)
  private Integer uid;

  public LinuxUserConfiguration() {
  }

  public LinuxUserConfiguration gid(Integer gid) {
    this.gid = gid;
    return this;
  }

  /**
   * The uid and gid properties must be specified together or not at all. If not specified the underlying operating system picks the gid.
   * @return gid
   */
  @javax.annotation.Nullable
  public Integer getGid() {
    return gid;
  }

  public void setGid(Integer gid) {
    this.gid = gid;
  }


  public LinuxUserConfiguration sshPrivateKey(String sshPrivateKey) {
    this.sshPrivateKey = sshPrivateKey;
    return this;
  }

  /**
   * The private key must not be password protected. The private key is used to automatically configure asymmetric-key based authentication for SSH between nodes in a Linux pool when the pool&#39;s enableInterNodeCommunication property is true (it is ignored if enableInterNodeCommunication is false). It does this by placing the key pair into the user&#39;s .ssh directory. If not specified, password-less SSH is not configured between nodes (no modification of the user&#39;s .ssh directory is done).
   * @return sshPrivateKey
   */
  @javax.annotation.Nullable
  public String getSshPrivateKey() {
    return sshPrivateKey;
  }

  public void setSshPrivateKey(String sshPrivateKey) {
    this.sshPrivateKey = sshPrivateKey;
  }


  public LinuxUserConfiguration uid(Integer uid) {
    this.uid = uid;
    return this;
  }

  /**
   * The uid and gid properties must be specified together or not at all. If not specified the underlying operating system picks the uid.
   * @return uid
   */
  @javax.annotation.Nullable
  public Integer getUid() {
    return uid;
  }

  public void setUid(Integer uid) {
    this.uid = uid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LinuxUserConfiguration linuxUserConfiguration = (LinuxUserConfiguration) o;
    return Objects.equals(this.gid, linuxUserConfiguration.gid) &&
        Objects.equals(this.sshPrivateKey, linuxUserConfiguration.sshPrivateKey) &&
        Objects.equals(this.uid, linuxUserConfiguration.uid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(gid, sshPrivateKey, uid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LinuxUserConfiguration {\n");
    sb.append("    gid: ").append(toIndentedString(gid)).append("\n");
    sb.append("    sshPrivateKey: ").append(toIndentedString(sshPrivateKey)).append("\n");
    sb.append("    uid: ").append(toIndentedString(uid)).append("\n");
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
    openapiFields.add("gid");
    openapiFields.add("sshPrivateKey");
    openapiFields.add("uid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LinuxUserConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LinuxUserConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LinuxUserConfiguration is not found in the empty JSON string", LinuxUserConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LinuxUserConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LinuxUserConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("sshPrivateKey") != null && !jsonObj.get("sshPrivateKey").isJsonNull()) && !jsonObj.get("sshPrivateKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sshPrivateKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sshPrivateKey").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LinuxUserConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LinuxUserConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LinuxUserConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LinuxUserConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<LinuxUserConfiguration>() {
           @Override
           public void write(JsonWriter out, LinuxUserConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LinuxUserConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LinuxUserConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LinuxUserConfiguration
   * @throws IOException if the JSON string is invalid with respect to LinuxUserConfiguration
   */
  public static LinuxUserConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LinuxUserConfiguration.class);
  }

  /**
   * Convert an instance of LinuxUserConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

