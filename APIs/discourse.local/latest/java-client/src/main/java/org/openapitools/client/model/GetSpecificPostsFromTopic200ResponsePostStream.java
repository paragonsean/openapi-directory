/*
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetSpecificPostsFromTopic200ResponsePostStreamPostsInner;

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
 * GetSpecificPostsFromTopic200ResponsePostStream
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:34.324076-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetSpecificPostsFromTopic200ResponsePostStream {
  public static final String SERIALIZED_NAME_POSTS = "posts";
  @SerializedName(SERIALIZED_NAME_POSTS)
  private List<GetSpecificPostsFromTopic200ResponsePostStreamPostsInner> posts = new ArrayList<>();

  public GetSpecificPostsFromTopic200ResponsePostStream() {
  }

  public GetSpecificPostsFromTopic200ResponsePostStream posts(List<GetSpecificPostsFromTopic200ResponsePostStreamPostsInner> posts) {
    this.posts = posts;
    return this;
  }

  public GetSpecificPostsFromTopic200ResponsePostStream addPostsItem(GetSpecificPostsFromTopic200ResponsePostStreamPostsInner postsItem) {
    if (this.posts == null) {
      this.posts = new ArrayList<>();
    }
    this.posts.add(postsItem);
    return this;
  }

  /**
   * Get posts
   * @return posts
   */
  @javax.annotation.Nullable
  public List<GetSpecificPostsFromTopic200ResponsePostStreamPostsInner> getPosts() {
    return posts;
  }

  public void setPosts(List<GetSpecificPostsFromTopic200ResponsePostStreamPostsInner> posts) {
    this.posts = posts;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetSpecificPostsFromTopic200ResponsePostStream getSpecificPostsFromTopic200ResponsePostStream = (GetSpecificPostsFromTopic200ResponsePostStream) o;
    return Objects.equals(this.posts, getSpecificPostsFromTopic200ResponsePostStream.posts);
  }

  @Override
  public int hashCode() {
    return Objects.hash(posts);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetSpecificPostsFromTopic200ResponsePostStream {\n");
    sb.append("    posts: ").append(toIndentedString(posts)).append("\n");
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
    openapiFields.add("posts");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetSpecificPostsFromTopic200ResponsePostStream
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetSpecificPostsFromTopic200ResponsePostStream.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetSpecificPostsFromTopic200ResponsePostStream is not found in the empty JSON string", GetSpecificPostsFromTopic200ResponsePostStream.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetSpecificPostsFromTopic200ResponsePostStream.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetSpecificPostsFromTopic200ResponsePostStream` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("posts") != null && !jsonObj.get("posts").isJsonNull()) {
        JsonArray jsonArrayposts = jsonObj.getAsJsonArray("posts");
        if (jsonArrayposts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("posts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `posts` to be an array in the JSON string but got `%s`", jsonObj.get("posts").toString()));
          }

          // validate the optional field `posts` (array)
          for (int i = 0; i < jsonArrayposts.size(); i++) {
            GetSpecificPostsFromTopic200ResponsePostStreamPostsInner.validateJsonElement(jsonArrayposts.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetSpecificPostsFromTopic200ResponsePostStream.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetSpecificPostsFromTopic200ResponsePostStream' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetSpecificPostsFromTopic200ResponsePostStream> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetSpecificPostsFromTopic200ResponsePostStream.class));

       return (TypeAdapter<T>) new TypeAdapter<GetSpecificPostsFromTopic200ResponsePostStream>() {
           @Override
           public void write(JsonWriter out, GetSpecificPostsFromTopic200ResponsePostStream value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetSpecificPostsFromTopic200ResponsePostStream read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetSpecificPostsFromTopic200ResponsePostStream given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetSpecificPostsFromTopic200ResponsePostStream
   * @throws IOException if the JSON string is invalid with respect to GetSpecificPostsFromTopic200ResponsePostStream
   */
  public static GetSpecificPostsFromTopic200ResponsePostStream fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetSpecificPostsFromTopic200ResponsePostStream.class);
  }

  /**
   * Convert an instance of GetSpecificPostsFromTopic200ResponsePostStream to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

