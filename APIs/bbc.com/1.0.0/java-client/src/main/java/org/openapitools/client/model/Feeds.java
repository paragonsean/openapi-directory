/*
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
import org.openapitools.client.model.Deprecations;
import org.openapitools.client.model.Feed;

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
 * Feeds
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Feeds {
  public static final String SERIALIZED_NAME_DEPLOYMENT_ROOT = "deployment_root";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT_ROOT)
  private String deploymentRoot;

  public static final String SERIALIZED_NAME_DEPRECATIONS = "deprecations";
  @SerializedName(SERIALIZED_NAME_DEPRECATIONS)
  private Deprecations deprecations;

  public static final String SERIALIZED_NAME_FEED = "feed";
  @SerializedName(SERIALIZED_NAME_FEED)
  private List<Feed> feed = new ArrayList<>();

  public Feeds() {
  }

  public Feeds deploymentRoot(String deploymentRoot) {
    this.deploymentRoot = deploymentRoot;
    return this;
  }

  /**
   * Get deploymentRoot
   * @return deploymentRoot
   */
  @javax.annotation.Nullable
  public String getDeploymentRoot() {
    return deploymentRoot;
  }

  public void setDeploymentRoot(String deploymentRoot) {
    this.deploymentRoot = deploymentRoot;
  }


  public Feeds deprecations(Deprecations deprecations) {
    this.deprecations = deprecations;
    return this;
  }

  /**
   * Get deprecations
   * @return deprecations
   */
  @javax.annotation.Nullable
  public Deprecations getDeprecations() {
    return deprecations;
  }

  public void setDeprecations(Deprecations deprecations) {
    this.deprecations = deprecations;
  }


  public Feeds feed(List<Feed> feed) {
    this.feed = feed;
    return this;
  }

  public Feeds addFeedItem(Feed feedItem) {
    if (this.feed == null) {
      this.feed = new ArrayList<>();
    }
    this.feed.add(feedItem);
    return this;
  }

  /**
   * Get feed
   * @return feed
   */
  @javax.annotation.Nullable
  public List<Feed> getFeed() {
    return feed;
  }

  public void setFeed(List<Feed> feed) {
    this.feed = feed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Feeds feeds = (Feeds) o;
    return Objects.equals(this.deploymentRoot, feeds.deploymentRoot) &&
        Objects.equals(this.deprecations, feeds.deprecations) &&
        Objects.equals(this.feed, feeds.feed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(deploymentRoot, deprecations, feed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Feeds {\n");
    sb.append("    deploymentRoot: ").append(toIndentedString(deploymentRoot)).append("\n");
    sb.append("    deprecations: ").append(toIndentedString(deprecations)).append("\n");
    sb.append("    feed: ").append(toIndentedString(feed)).append("\n");
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
    openapiFields.add("deployment_root");
    openapiFields.add("deprecations");
    openapiFields.add("feed");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Feeds
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Feeds.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Feeds is not found in the empty JSON string", Feeds.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Feeds.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Feeds` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("deployment_root") != null && !jsonObj.get("deployment_root").isJsonNull()) && !jsonObj.get("deployment_root").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deployment_root` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deployment_root").toString()));
      }
      // validate the optional field `deprecations`
      if (jsonObj.get("deprecations") != null && !jsonObj.get("deprecations").isJsonNull()) {
        Deprecations.validateJsonElement(jsonObj.get("deprecations"));
      }
      if (jsonObj.get("feed") != null && !jsonObj.get("feed").isJsonNull()) {
        JsonArray jsonArrayfeed = jsonObj.getAsJsonArray("feed");
        if (jsonArrayfeed != null) {
          // ensure the json data is an array
          if (!jsonObj.get("feed").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `feed` to be an array in the JSON string but got `%s`", jsonObj.get("feed").toString()));
          }

          // validate the optional field `feed` (array)
          for (int i = 0; i < jsonArrayfeed.size(); i++) {
            Feed.validateJsonElement(jsonArrayfeed.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Feeds.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Feeds' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Feeds> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Feeds.class));

       return (TypeAdapter<T>) new TypeAdapter<Feeds>() {
           @Override
           public void write(JsonWriter out, Feeds value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Feeds read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Feeds given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Feeds
   * @throws IOException if the JSON string is invalid with respect to Feeds
   */
  public static Feeds fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Feeds.class);
  }

  /**
   * Convert an instance of Feeds to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

