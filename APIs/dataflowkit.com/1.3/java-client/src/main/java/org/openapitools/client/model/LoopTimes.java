/*
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Action;

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
 * Loop action combines a set of actions and executes it as many times as specified in the \&quot;times\&quot; parameter.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:44.962241-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LoopTimes {
  public static final String SERIALIZED_NAME_ACTIONS = "actions";
  @SerializedName(SERIALIZED_NAME_ACTIONS)
  private List<Action> actions = new ArrayList<>();

  public static final String SERIALIZED_NAME_TIMES = "times";
  @SerializedName(SERIALIZED_NAME_TIMES)
  private BigDecimal times;

  public LoopTimes() {
  }

  public LoopTimes actions(List<Action> actions) {
    this.actions = actions;
    return this;
  }

  public LoopTimes addActionsItem(Action actionsItem) {
    if (this.actions == null) {
      this.actions = new ArrayList<>();
    }
    this.actions.add(actionsItem);
    return this;
  }

  /**
   * list of actions combined in the loop are executed step-by-step
   * @return actions
   */
  @javax.annotation.Nullable
  public List<Action> getActions() {
    return actions;
  }

  public void setActions(List<Action> actions) {
    this.actions = actions;
  }


  public LoopTimes times(BigDecimal times) {
    this.times = times;
    return this;
  }

  /**
   * the number of times to execute the wrapped actions within the &#39;loop .. times&#39; construction.
   * @return times
   */
  @javax.annotation.Nullable
  public BigDecimal getTimes() {
    return times;
  }

  public void setTimes(BigDecimal times) {
    this.times = times;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LoopTimes loopTimes = (LoopTimes) o;
    return Objects.equals(this.actions, loopTimes.actions) &&
        Objects.equals(this.times, loopTimes.times);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actions, times);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LoopTimes {\n");
    sb.append("    actions: ").append(toIndentedString(actions)).append("\n");
    sb.append("    times: ").append(toIndentedString(times)).append("\n");
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
    openapiFields.add("actions");
    openapiFields.add("times");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LoopTimes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LoopTimes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LoopTimes is not found in the empty JSON string", LoopTimes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LoopTimes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LoopTimes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("actions") != null && !jsonObj.get("actions").isJsonNull()) {
        JsonArray jsonArrayactions = jsonObj.getAsJsonArray("actions");
        if (jsonArrayactions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("actions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `actions` to be an array in the JSON string but got `%s`", jsonObj.get("actions").toString()));
          }

          // validate the optional field `actions` (array)
          for (int i = 0; i < jsonArrayactions.size(); i++) {
            Action.validateJsonElement(jsonArrayactions.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LoopTimes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LoopTimes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LoopTimes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LoopTimes.class));

       return (TypeAdapter<T>) new TypeAdapter<LoopTimes>() {
           @Override
           public void write(JsonWriter out, LoopTimes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LoopTimes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LoopTimes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LoopTimes
   * @throws IOException if the JSON string is invalid with respect to LoopTimes
   */
  public static LoopTimes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LoopTimes.class);
  }

  /**
   * Convert an instance of LoopTimes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

