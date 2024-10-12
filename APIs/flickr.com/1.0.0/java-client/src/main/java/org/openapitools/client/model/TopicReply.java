/*
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.GetFavoritesContextByID200ResponseCount;

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
 * TopicReply
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:49.490227-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TopicReply {
  public static final String SERIALIZED_NAME_AUTHOR = "author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private String author;

  public static final String SERIALIZED_NAME_AUTHOR_IS_DELETED = "author_is_deleted";
  @SerializedName(SERIALIZED_NAME_AUTHOR_IS_DELETED)
  private Boolean authorIsDeleted;

  public static final String SERIALIZED_NAME_AUTHOR_PATH_ALIAS = "author_path_alias";
  @SerializedName(SERIALIZED_NAME_AUTHOR_PATH_ALIAS)
  private String authorPathAlias;

  public static final String SERIALIZED_NAME_AUTHORNAME = "authorname";
  @SerializedName(SERIALIZED_NAME_AUTHORNAME)
  private String authorname;

  public static final String SERIALIZED_NAME_CAN_DELETE = "can_delete";
  @SerializedName(SERIALIZED_NAME_CAN_DELETE)
  private Boolean canDelete;

  public static final String SERIALIZED_NAME_CAN_EDIT = "can_edit";
  @SerializedName(SERIALIZED_NAME_CAN_EDIT)
  private Boolean canEdit;

  public static final String SERIALIZED_NAME_DATECREATE = "datecreate";
  @SerializedName(SERIALIZED_NAME_DATECREATE)
  private String datecreate;

  public static final String SERIALIZED_NAME_ICONFARM = "iconfarm";
  @SerializedName(SERIALIZED_NAME_ICONFARM)
  private String iconfarm;

  public static final String SERIALIZED_NAME_ICONSERVER = "iconserver";
  @SerializedName(SERIALIZED_NAME_ICONSERVER)
  private String iconserver;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_PRO = "is_pro";
  @SerializedName(SERIALIZED_NAME_IS_PRO)
  private Boolean isPro;

  public static final String SERIALIZED_NAME_LASTEDIT = "lastedit";
  @SerializedName(SERIALIZED_NAME_LASTEDIT)
  private String lastedit;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private GetFavoritesContextByID200ResponseCount message;

  public TopicReply() {
  }

  public TopicReply author(String author) {
    this.author = author;
    return this;
  }

  /**
   * Get author
   * @return author
   */
  @javax.annotation.Nullable
  public String getAuthor() {
    return author;
  }

  public void setAuthor(String author) {
    this.author = author;
  }


  public TopicReply authorIsDeleted(Boolean authorIsDeleted) {
    this.authorIsDeleted = authorIsDeleted;
    return this;
  }

  /**
   * Get authorIsDeleted
   * @return authorIsDeleted
   */
  @javax.annotation.Nullable
  public Boolean getAuthorIsDeleted() {
    return authorIsDeleted;
  }

  public void setAuthorIsDeleted(Boolean authorIsDeleted) {
    this.authorIsDeleted = authorIsDeleted;
  }


  public TopicReply authorPathAlias(String authorPathAlias) {
    this.authorPathAlias = authorPathAlias;
    return this;
  }

  /**
   * Get authorPathAlias
   * @return authorPathAlias
   */
  @javax.annotation.Nullable
  public String getAuthorPathAlias() {
    return authorPathAlias;
  }

  public void setAuthorPathAlias(String authorPathAlias) {
    this.authorPathAlias = authorPathAlias;
  }


  public TopicReply authorname(String authorname) {
    this.authorname = authorname;
    return this;
  }

  /**
   * Get authorname
   * @return authorname
   */
  @javax.annotation.Nullable
  public String getAuthorname() {
    return authorname;
  }

  public void setAuthorname(String authorname) {
    this.authorname = authorname;
  }


  public TopicReply canDelete(Boolean canDelete) {
    this.canDelete = canDelete;
    return this;
  }

  /**
   * Get canDelete
   * @return canDelete
   */
  @javax.annotation.Nullable
  public Boolean getCanDelete() {
    return canDelete;
  }

  public void setCanDelete(Boolean canDelete) {
    this.canDelete = canDelete;
  }


  public TopicReply canEdit(Boolean canEdit) {
    this.canEdit = canEdit;
    return this;
  }

  /**
   * Get canEdit
   * @return canEdit
   */
  @javax.annotation.Nullable
  public Boolean getCanEdit() {
    return canEdit;
  }

  public void setCanEdit(Boolean canEdit) {
    this.canEdit = canEdit;
  }


  public TopicReply datecreate(String datecreate) {
    this.datecreate = datecreate;
    return this;
  }

  /**
   * Get datecreate
   * @return datecreate
   */
  @javax.annotation.Nullable
  public String getDatecreate() {
    return datecreate;
  }

  public void setDatecreate(String datecreate) {
    this.datecreate = datecreate;
  }


  public TopicReply iconfarm(String iconfarm) {
    this.iconfarm = iconfarm;
    return this;
  }

  /**
   * Get iconfarm
   * @return iconfarm
   */
  @javax.annotation.Nullable
  public String getIconfarm() {
    return iconfarm;
  }

  public void setIconfarm(String iconfarm) {
    this.iconfarm = iconfarm;
  }


  public TopicReply iconserver(String iconserver) {
    this.iconserver = iconserver;
    return this;
  }

  /**
   * Get iconserver
   * @return iconserver
   */
  @javax.annotation.Nullable
  public String getIconserver() {
    return iconserver;
  }

  public void setIconserver(String iconserver) {
    this.iconserver = iconserver;
  }


  public TopicReply id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public TopicReply isPro(Boolean isPro) {
    this.isPro = isPro;
    return this;
  }

  /**
   * Get isPro
   * @return isPro
   */
  @javax.annotation.Nullable
  public Boolean getIsPro() {
    return isPro;
  }

  public void setIsPro(Boolean isPro) {
    this.isPro = isPro;
  }


  public TopicReply lastedit(String lastedit) {
    this.lastedit = lastedit;
    return this;
  }

  /**
   * Get lastedit
   * @return lastedit
   */
  @javax.annotation.Nullable
  public String getLastedit() {
    return lastedit;
  }

  public void setLastedit(String lastedit) {
    this.lastedit = lastedit;
  }


  public TopicReply message(GetFavoritesContextByID200ResponseCount message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public GetFavoritesContextByID200ResponseCount getMessage() {
    return message;
  }

  public void setMessage(GetFavoritesContextByID200ResponseCount message) {
    this.message = message;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TopicReply topicReply = (TopicReply) o;
    return Objects.equals(this.author, topicReply.author) &&
        Objects.equals(this.authorIsDeleted, topicReply.authorIsDeleted) &&
        Objects.equals(this.authorPathAlias, topicReply.authorPathAlias) &&
        Objects.equals(this.authorname, topicReply.authorname) &&
        Objects.equals(this.canDelete, topicReply.canDelete) &&
        Objects.equals(this.canEdit, topicReply.canEdit) &&
        Objects.equals(this.datecreate, topicReply.datecreate) &&
        Objects.equals(this.iconfarm, topicReply.iconfarm) &&
        Objects.equals(this.iconserver, topicReply.iconserver) &&
        Objects.equals(this.id, topicReply.id) &&
        Objects.equals(this.isPro, topicReply.isPro) &&
        Objects.equals(this.lastedit, topicReply.lastedit) &&
        Objects.equals(this.message, topicReply.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, authorIsDeleted, authorPathAlias, authorname, canDelete, canEdit, datecreate, iconfarm, iconserver, id, isPro, lastedit, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TopicReply {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    authorIsDeleted: ").append(toIndentedString(authorIsDeleted)).append("\n");
    sb.append("    authorPathAlias: ").append(toIndentedString(authorPathAlias)).append("\n");
    sb.append("    authorname: ").append(toIndentedString(authorname)).append("\n");
    sb.append("    canDelete: ").append(toIndentedString(canDelete)).append("\n");
    sb.append("    canEdit: ").append(toIndentedString(canEdit)).append("\n");
    sb.append("    datecreate: ").append(toIndentedString(datecreate)).append("\n");
    sb.append("    iconfarm: ").append(toIndentedString(iconfarm)).append("\n");
    sb.append("    iconserver: ").append(toIndentedString(iconserver)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isPro: ").append(toIndentedString(isPro)).append("\n");
    sb.append("    lastedit: ").append(toIndentedString(lastedit)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
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
    openapiFields.add("author");
    openapiFields.add("author_is_deleted");
    openapiFields.add("author_path_alias");
    openapiFields.add("authorname");
    openapiFields.add("can_delete");
    openapiFields.add("can_edit");
    openapiFields.add("datecreate");
    openapiFields.add("iconfarm");
    openapiFields.add("iconserver");
    openapiFields.add("id");
    openapiFields.add("is_pro");
    openapiFields.add("lastedit");
    openapiFields.add("message");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TopicReply
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TopicReply.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TopicReply is not found in the empty JSON string", TopicReply.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TopicReply.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TopicReply` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("author") != null && !jsonObj.get("author").isJsonNull()) && !jsonObj.get("author").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `author` to be a primitive type in the JSON string but got `%s`", jsonObj.get("author").toString()));
      }
      if ((jsonObj.get("author_path_alias") != null && !jsonObj.get("author_path_alias").isJsonNull()) && !jsonObj.get("author_path_alias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `author_path_alias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("author_path_alias").toString()));
      }
      if ((jsonObj.get("authorname") != null && !jsonObj.get("authorname").isJsonNull()) && !jsonObj.get("authorname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authorname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authorname").toString()));
      }
      if ((jsonObj.get("datecreate") != null && !jsonObj.get("datecreate").isJsonNull()) && !jsonObj.get("datecreate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `datecreate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("datecreate").toString()));
      }
      if ((jsonObj.get("iconfarm") != null && !jsonObj.get("iconfarm").isJsonNull()) && !jsonObj.get("iconfarm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iconfarm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iconfarm").toString()));
      }
      if ((jsonObj.get("iconserver") != null && !jsonObj.get("iconserver").isJsonNull()) && !jsonObj.get("iconserver").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iconserver` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iconserver").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("lastedit") != null && !jsonObj.get("lastedit").isJsonNull()) && !jsonObj.get("lastedit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastedit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastedit").toString()));
      }
      // validate the optional field `message`
      if (jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) {
        GetFavoritesContextByID200ResponseCount.validateJsonElement(jsonObj.get("message"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TopicReply.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TopicReply' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TopicReply> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TopicReply.class));

       return (TypeAdapter<T>) new TypeAdapter<TopicReply>() {
           @Override
           public void write(JsonWriter out, TopicReply value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TopicReply read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TopicReply given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TopicReply
   * @throws IOException if the JSON string is invalid with respect to TopicReply
   */
  public static TopicReply fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TopicReply.class);
  }

  /**
   * Convert an instance of TopicReply to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

