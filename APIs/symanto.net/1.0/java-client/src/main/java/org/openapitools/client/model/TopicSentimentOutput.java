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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Sentiment;
import org.openapitools.client.model.Topic;
import org.openapitools.client.model.TopicSentiment;

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
 * TopicSentimentOutput
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:14.714889-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TopicSentimentOutput {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_SENTIMENTS = "sentiments";
  @SerializedName(SERIALIZED_NAME_SENTIMENTS)
  private List<Sentiment> sentiments = new ArrayList<>();

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public static final String SERIALIZED_NAME_TOPIC_SENTIMENTS = "topicSentiments";
  @SerializedName(SERIALIZED_NAME_TOPIC_SENTIMENTS)
  private List<TopicSentiment> topicSentiments = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOPICS = "topics";
  @SerializedName(SERIALIZED_NAME_TOPICS)
  private List<Topic> topics = new ArrayList<>();

  public TopicSentimentOutput() {
  }

  public TopicSentimentOutput id(String id) {
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


  public TopicSentimentOutput language(String language) {
    this.language = language;
    return this;
  }

  /**
   * Get language
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public TopicSentimentOutput sentiments(List<Sentiment> sentiments) {
    this.sentiments = sentiments;
    return this;
  }

  public TopicSentimentOutput addSentimentsItem(Sentiment sentimentsItem) {
    if (this.sentiments == null) {
      this.sentiments = new ArrayList<>();
    }
    this.sentiments.add(sentimentsItem);
    return this;
  }

  /**
   * Get sentiments
   * @return sentiments
   */
  @javax.annotation.Nullable
  public List<Sentiment> getSentiments() {
    return sentiments;
  }

  public void setSentiments(List<Sentiment> sentiments) {
    this.sentiments = sentiments;
  }


  public TopicSentimentOutput text(String text) {
    this.text = text;
    return this;
  }

  /**
   * Get text
   * @return text
   */
  @javax.annotation.Nullable
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }


  public TopicSentimentOutput topicSentiments(List<TopicSentiment> topicSentiments) {
    this.topicSentiments = topicSentiments;
    return this;
  }

  public TopicSentimentOutput addTopicSentimentsItem(TopicSentiment topicSentimentsItem) {
    if (this.topicSentiments == null) {
      this.topicSentiments = new ArrayList<>();
    }
    this.topicSentiments.add(topicSentimentsItem);
    return this;
  }

  /**
   * Get topicSentiments
   * @return topicSentiments
   */
  @javax.annotation.Nullable
  public List<TopicSentiment> getTopicSentiments() {
    return topicSentiments;
  }

  public void setTopicSentiments(List<TopicSentiment> topicSentiments) {
    this.topicSentiments = topicSentiments;
  }


  public TopicSentimentOutput topics(List<Topic> topics) {
    this.topics = topics;
    return this;
  }

  public TopicSentimentOutput addTopicsItem(Topic topicsItem) {
    if (this.topics == null) {
      this.topics = new ArrayList<>();
    }
    this.topics.add(topicsItem);
    return this;
  }

  /**
   * Get topics
   * @return topics
   */
  @javax.annotation.Nullable
  public List<Topic> getTopics() {
    return topics;
  }

  public void setTopics(List<Topic> topics) {
    this.topics = topics;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TopicSentimentOutput topicSentimentOutput = (TopicSentimentOutput) o;
    return Objects.equals(this.id, topicSentimentOutput.id) &&
        Objects.equals(this.language, topicSentimentOutput.language) &&
        Objects.equals(this.sentiments, topicSentimentOutput.sentiments) &&
        Objects.equals(this.text, topicSentimentOutput.text) &&
        Objects.equals(this.topicSentiments, topicSentimentOutput.topicSentiments) &&
        Objects.equals(this.topics, topicSentimentOutput.topics);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, language, sentiments, text, topicSentiments, topics);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TopicSentimentOutput {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    sentiments: ").append(toIndentedString(sentiments)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
    sb.append("    topicSentiments: ").append(toIndentedString(topicSentiments)).append("\n");
    sb.append("    topics: ").append(toIndentedString(topics)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("language");
    openapiFields.add("sentiments");
    openapiFields.add("text");
    openapiFields.add("topicSentiments");
    openapiFields.add("topics");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TopicSentimentOutput
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TopicSentimentOutput.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TopicSentimentOutput is not found in the empty JSON string", TopicSentimentOutput.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TopicSentimentOutput.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TopicSentimentOutput` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if (jsonObj.get("sentiments") != null && !jsonObj.get("sentiments").isJsonNull()) {
        JsonArray jsonArraysentiments = jsonObj.getAsJsonArray("sentiments");
        if (jsonArraysentiments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sentiments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sentiments` to be an array in the JSON string but got `%s`", jsonObj.get("sentiments").toString()));
          }

          // validate the optional field `sentiments` (array)
          for (int i = 0; i < jsonArraysentiments.size(); i++) {
            Sentiment.validateJsonElement(jsonArraysentiments.get(i));
          };
        }
      }
      if ((jsonObj.get("text") != null && !jsonObj.get("text").isJsonNull()) && !jsonObj.get("text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text").toString()));
      }
      if (jsonObj.get("topicSentiments") != null && !jsonObj.get("topicSentiments").isJsonNull()) {
        JsonArray jsonArraytopicSentiments = jsonObj.getAsJsonArray("topicSentiments");
        if (jsonArraytopicSentiments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("topicSentiments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `topicSentiments` to be an array in the JSON string but got `%s`", jsonObj.get("topicSentiments").toString()));
          }

          // validate the optional field `topicSentiments` (array)
          for (int i = 0; i < jsonArraytopicSentiments.size(); i++) {
            TopicSentiment.validateJsonElement(jsonArraytopicSentiments.get(i));
          };
        }
      }
      if (jsonObj.get("topics") != null && !jsonObj.get("topics").isJsonNull()) {
        JsonArray jsonArraytopics = jsonObj.getAsJsonArray("topics");
        if (jsonArraytopics != null) {
          // ensure the json data is an array
          if (!jsonObj.get("topics").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `topics` to be an array in the JSON string but got `%s`", jsonObj.get("topics").toString()));
          }

          // validate the optional field `topics` (array)
          for (int i = 0; i < jsonArraytopics.size(); i++) {
            Topic.validateJsonElement(jsonArraytopics.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TopicSentimentOutput.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TopicSentimentOutput' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TopicSentimentOutput> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TopicSentimentOutput.class));

       return (TypeAdapter<T>) new TypeAdapter<TopicSentimentOutput>() {
           @Override
           public void write(JsonWriter out, TopicSentimentOutput value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TopicSentimentOutput read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TopicSentimentOutput given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TopicSentimentOutput
   * @throws IOException if the JSON string is invalid with respect to TopicSentimentOutput
   */
  public static TopicSentimentOutput fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TopicSentimentOutput.class);
  }

  /**
   * Convert an instance of TopicSentimentOutput to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

