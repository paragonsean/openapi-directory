/*
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CommentForApiContract;
import org.openapitools.client.model.UserForApiContract;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * DiscussionTopicContract
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:40.974326-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DiscussionTopicContract {
  public static final String SERIALIZED_NAME_AUTHOR = "author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private UserForApiContract author;

  public static final String SERIALIZED_NAME_COMMENT_COUNT = "commentCount";
  @SerializedName(SERIALIZED_NAME_COMMENT_COUNT)
  private Integer commentCount;

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private List<CommentForApiContract> comments;

  public static final String SERIALIZED_NAME_CONTENT = "content";
  @SerializedName(SERIALIZED_NAME_CONTENT)
  private String content;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_FOLDER_ID = "folderId";
  @SerializedName(SERIALIZED_NAME_FOLDER_ID)
  private Integer folderId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LAST_COMMENT = "lastComment";
  @SerializedName(SERIALIZED_NAME_LAST_COMMENT)
  private CommentForApiContract lastComment;

  public static final String SERIALIZED_NAME_LOCKED = "locked";
  @SerializedName(SERIALIZED_NAME_LOCKED)
  private Boolean locked;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public DiscussionTopicContract() {
  }

  public DiscussionTopicContract author(UserForApiContract author) {
    this.author = author;
    return this;
  }

  /**
   * Get author
   * @return author
   */
  @javax.annotation.Nullable
  public UserForApiContract getAuthor() {
    return author;
  }

  public void setAuthor(UserForApiContract author) {
    this.author = author;
  }


  public DiscussionTopicContract commentCount(Integer commentCount) {
    this.commentCount = commentCount;
    return this;
  }

  /**
   * Get commentCount
   * @return commentCount
   */
  @javax.annotation.Nullable
  public Integer getCommentCount() {
    return commentCount;
  }

  public void setCommentCount(Integer commentCount) {
    this.commentCount = commentCount;
  }


  public DiscussionTopicContract comments(List<CommentForApiContract> comments) {
    this.comments = comments;
    return this;
  }

  public DiscussionTopicContract addCommentsItem(CommentForApiContract commentsItem) {
    if (this.comments == null) {
      this.comments = new ArrayList<>();
    }
    this.comments.add(commentsItem);
    return this;
  }

  /**
   * Get comments
   * @return comments
   */
  @javax.annotation.Nullable
  public List<CommentForApiContract> getComments() {
    return comments;
  }

  public void setComments(List<CommentForApiContract> comments) {
    this.comments = comments;
  }


  public DiscussionTopicContract content(String content) {
    this.content = content;
    return this;
  }

  /**
   * Get content
   * @return content
   */
  @javax.annotation.Nullable
  public String getContent() {
    return content;
  }

  public void setContent(String content) {
    this.content = content;
  }


  public DiscussionTopicContract created(OffsetDateTime created) {
    this.created = created;
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }

  public void setCreated(OffsetDateTime created) {
    this.created = created;
  }


  public DiscussionTopicContract folderId(Integer folderId) {
    this.folderId = folderId;
    return this;
  }

  /**
   * Get folderId
   * @return folderId
   */
  @javax.annotation.Nullable
  public Integer getFolderId() {
    return folderId;
  }

  public void setFolderId(Integer folderId) {
    this.folderId = folderId;
  }


  public DiscussionTopicContract id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public DiscussionTopicContract lastComment(CommentForApiContract lastComment) {
    this.lastComment = lastComment;
    return this;
  }

  /**
   * Get lastComment
   * @return lastComment
   */
  @javax.annotation.Nullable
  public CommentForApiContract getLastComment() {
    return lastComment;
  }

  public void setLastComment(CommentForApiContract lastComment) {
    this.lastComment = lastComment;
  }


  public DiscussionTopicContract locked(Boolean locked) {
    this.locked = locked;
    return this;
  }

  /**
   * Get locked
   * @return locked
   */
  @javax.annotation.Nullable
  public Boolean getLocked() {
    return locked;
  }

  public void setLocked(Boolean locked) {
    this.locked = locked;
  }


  public DiscussionTopicContract name(String name) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DiscussionTopicContract discussionTopicContract = (DiscussionTopicContract) o;
    return Objects.equals(this.author, discussionTopicContract.author) &&
        Objects.equals(this.commentCount, discussionTopicContract.commentCount) &&
        Objects.equals(this.comments, discussionTopicContract.comments) &&
        Objects.equals(this.content, discussionTopicContract.content) &&
        Objects.equals(this.created, discussionTopicContract.created) &&
        Objects.equals(this.folderId, discussionTopicContract.folderId) &&
        Objects.equals(this.id, discussionTopicContract.id) &&
        Objects.equals(this.lastComment, discussionTopicContract.lastComment) &&
        Objects.equals(this.locked, discussionTopicContract.locked) &&
        Objects.equals(this.name, discussionTopicContract.name);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, commentCount, comments, content, created, folderId, id, lastComment, locked, name);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DiscussionTopicContract {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    commentCount: ").append(toIndentedString(commentCount)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    folderId: ").append(toIndentedString(folderId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastComment: ").append(toIndentedString(lastComment)).append("\n");
    sb.append("    locked: ").append(toIndentedString(locked)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("commentCount");
    openapiFields.add("comments");
    openapiFields.add("content");
    openapiFields.add("created");
    openapiFields.add("folderId");
    openapiFields.add("id");
    openapiFields.add("lastComment");
    openapiFields.add("locked");
    openapiFields.add("name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DiscussionTopicContract
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DiscussionTopicContract.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DiscussionTopicContract is not found in the empty JSON string", DiscussionTopicContract.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DiscussionTopicContract.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DiscussionTopicContract` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `author`
      if (jsonObj.get("author") != null && !jsonObj.get("author").isJsonNull()) {
        UserForApiContract.validateJsonElement(jsonObj.get("author"));
      }
      if (jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) {
        JsonArray jsonArraycomments = jsonObj.getAsJsonArray("comments");
        if (jsonArraycomments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("comments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `comments` to be an array in the JSON string but got `%s`", jsonObj.get("comments").toString()));
          }

          // validate the optional field `comments` (array)
          for (int i = 0; i < jsonArraycomments.size(); i++) {
            CommentForApiContract.validateJsonElement(jsonArraycomments.get(i));
          };
        }
      }
      if ((jsonObj.get("content") != null && !jsonObj.get("content").isJsonNull()) && !jsonObj.get("content").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content").toString()));
      }
      // validate the optional field `lastComment`
      if (jsonObj.get("lastComment") != null && !jsonObj.get("lastComment").isJsonNull()) {
        CommentForApiContract.validateJsonElement(jsonObj.get("lastComment"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DiscussionTopicContract.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DiscussionTopicContract' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DiscussionTopicContract> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DiscussionTopicContract.class));

       return (TypeAdapter<T>) new TypeAdapter<DiscussionTopicContract>() {
           @Override
           public void write(JsonWriter out, DiscussionTopicContract value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DiscussionTopicContract read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DiscussionTopicContract given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DiscussionTopicContract
   * @throws IOException if the JSON string is invalid with respect to DiscussionTopicContract
   */
  public static DiscussionTopicContract fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DiscussionTopicContract.class);
  }

  /**
   * Convert an instance of DiscussionTopicContract to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

