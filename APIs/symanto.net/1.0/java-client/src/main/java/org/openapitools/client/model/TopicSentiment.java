/*
 * Psycholinguistic Text Analytics
 * We aim to provide the deepest understanding of people through psychology & AI
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@symanto.net
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
import org.openapitools.client.model.Sentiment;
import org.openapitools.client.model.Topic;

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
 * TopicSentiment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:14.714889-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TopicSentiment {
  public static final String SERIALIZED_NAME_SENTENCE = "sentence";
  @SerializedName(SERIALIZED_NAME_SENTENCE)
  private String sentence;

  public static final String SERIALIZED_NAME_SENTIMENT = "sentiment";
  @SerializedName(SERIALIZED_NAME_SENTIMENT)
  private Sentiment sentiment;

  public static final String SERIALIZED_NAME_TOPIC = "topic";
  @SerializedName(SERIALIZED_NAME_TOPIC)
  private Topic topic;

  public TopicSentiment() {
  }

  public TopicSentiment sentence(String sentence) {
    this.sentence = sentence;
    return this;
  }

  /**
   * Get sentence
   * @return sentence
   */
  @javax.annotation.Nullable
  public String getSentence() {
    return sentence;
  }

  public void setSentence(String sentence) {
    this.sentence = sentence;
  }


  public TopicSentiment sentiment(Sentiment sentiment) {
    this.sentiment = sentiment;
    return this;
  }

  /**
   * Get sentiment
   * @return sentiment
   */
  @javax.annotation.Nullable
  public Sentiment getSentiment() {
    return sentiment;
  }

  public void setSentiment(Sentiment sentiment) {
    this.sentiment = sentiment;
  }


  public TopicSentiment topic(Topic topic) {
    this.topic = topic;
    return this;
  }

  /**
   * Get topic
   * @return topic
   */
  @javax.annotation.Nullable
  public Topic getTopic() {
    return topic;
  }

  public void setTopic(Topic topic) {
    this.topic = topic;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TopicSentiment topicSentiment = (TopicSentiment) o;
    return Objects.equals(this.sentence, topicSentiment.sentence) &&
        Objects.equals(this.sentiment, topicSentiment.sentiment) &&
        Objects.equals(this.topic, topicSentiment.topic);
  }

  @Override
  public int hashCode() {
    return Objects.hash(sentence, sentiment, topic);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TopicSentiment {\n");
    sb.append("    sentence: ").append(toIndentedString(sentence)).append("\n");
    sb.append("    sentiment: ").append(toIndentedString(sentiment)).append("\n");
    sb.append("    topic: ").append(toIndentedString(topic)).append("\n");
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
    openapiFields.add("sentence");
    openapiFields.add("sentiment");
    openapiFields.add("topic");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TopicSentiment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TopicSentiment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TopicSentiment is not found in the empty JSON string", TopicSentiment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TopicSentiment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TopicSentiment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("sentence") != null && !jsonObj.get("sentence").isJsonNull()) && !jsonObj.get("sentence").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sentence` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sentence").toString()));
      }
      // validate the optional field `sentiment`
      if (jsonObj.get("sentiment") != null && !jsonObj.get("sentiment").isJsonNull()) {
        Sentiment.validateJsonElement(jsonObj.get("sentiment"));
      }
      // validate the optional field `topic`
      if (jsonObj.get("topic") != null && !jsonObj.get("topic").isJsonNull()) {
        Topic.validateJsonElement(jsonObj.get("topic"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TopicSentiment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TopicSentiment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TopicSentiment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TopicSentiment.class));

       return (TypeAdapter<T>) new TypeAdapter<TopicSentiment>() {
           @Override
           public void write(JsonWriter out, TopicSentiment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TopicSentiment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TopicSentiment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TopicSentiment
   * @throws IOException if the JSON string is invalid with respect to TopicSentiment
   */
  public static TopicSentiment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TopicSentiment.class);
  }

  /**
   * Convert an instance of TopicSentiment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

