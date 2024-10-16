/*
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.FineTuningResponseModel;
import org.openapitools.client.model.SampleResponseModel;
import org.openapitools.client.model.VoiceSettingsResponseModel;

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
 * VoiceResponseModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:47.855117-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VoiceResponseModel {
  public static final String SERIALIZED_NAME_AVAILABLE_FOR_TIERS = "available_for_tiers";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_FOR_TIERS)
  private List<String> availableForTiers = new ArrayList<>();

  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private String category;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FINE_TUNING = "fine_tuning";
  @SerializedName(SERIALIZED_NAME_FINE_TUNING)
  private FineTuningResponseModel fineTuning;

  public static final String SERIALIZED_NAME_LABELS = "labels";
  @SerializedName(SERIALIZED_NAME_LABELS)
  private Map<String, String> labels = new HashMap<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PREVIEW_URL = "preview_url";
  @SerializedName(SERIALIZED_NAME_PREVIEW_URL)
  private String previewUrl;

  public static final String SERIALIZED_NAME_SAMPLES = "samples";
  @SerializedName(SERIALIZED_NAME_SAMPLES)
  private List<SampleResponseModel> samples = new ArrayList<>();

  public static final String SERIALIZED_NAME_SETTINGS = "settings";
  @SerializedName(SERIALIZED_NAME_SETTINGS)
  private VoiceSettingsResponseModel settings;

  public static final String SERIALIZED_NAME_VOICE_ID = "voice_id";
  @SerializedName(SERIALIZED_NAME_VOICE_ID)
  private String voiceId;

  public VoiceResponseModel() {
  }

  public VoiceResponseModel availableForTiers(List<String> availableForTiers) {
    this.availableForTiers = availableForTiers;
    return this;
  }

  public VoiceResponseModel addAvailableForTiersItem(String availableForTiersItem) {
    if (this.availableForTiers == null) {
      this.availableForTiers = new ArrayList<>();
    }
    this.availableForTiers.add(availableForTiersItem);
    return this;
  }

  /**
   * Get availableForTiers
   * @return availableForTiers
   */
  @javax.annotation.Nonnull
  public List<String> getAvailableForTiers() {
    return availableForTiers;
  }

  public void setAvailableForTiers(List<String> availableForTiers) {
    this.availableForTiers = availableForTiers;
  }


  public VoiceResponseModel category(String category) {
    this.category = category;
    return this;
  }

  /**
   * Get category
   * @return category
   */
  @javax.annotation.Nonnull
  public String getCategory() {
    return category;
  }

  public void setCategory(String category) {
    this.category = category;
  }


  public VoiceResponseModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public VoiceResponseModel fineTuning(FineTuningResponseModel fineTuning) {
    this.fineTuning = fineTuning;
    return this;
  }

  /**
   * Get fineTuning
   * @return fineTuning
   */
  @javax.annotation.Nonnull
  public FineTuningResponseModel getFineTuning() {
    return fineTuning;
  }

  public void setFineTuning(FineTuningResponseModel fineTuning) {
    this.fineTuning = fineTuning;
  }


  public VoiceResponseModel labels(Map<String, String> labels) {
    this.labels = labels;
    return this;
  }

  public VoiceResponseModel putLabelsItem(String key, String labelsItem) {
    if (this.labels == null) {
      this.labels = new HashMap<>();
    }
    this.labels.put(key, labelsItem);
    return this;
  }

  /**
   * Get labels
   * @return labels
   */
  @javax.annotation.Nonnull
  public Map<String, String> getLabels() {
    return labels;
  }

  public void setLabels(Map<String, String> labels) {
    this.labels = labels;
  }


  public VoiceResponseModel name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public VoiceResponseModel previewUrl(String previewUrl) {
    this.previewUrl = previewUrl;
    return this;
  }

  /**
   * Get previewUrl
   * @return previewUrl
   */
  @javax.annotation.Nonnull
  public String getPreviewUrl() {
    return previewUrl;
  }

  public void setPreviewUrl(String previewUrl) {
    this.previewUrl = previewUrl;
  }


  public VoiceResponseModel samples(List<SampleResponseModel> samples) {
    this.samples = samples;
    return this;
  }

  public VoiceResponseModel addSamplesItem(SampleResponseModel samplesItem) {
    if (this.samples == null) {
      this.samples = new ArrayList<>();
    }
    this.samples.add(samplesItem);
    return this;
  }

  /**
   * Get samples
   * @return samples
   */
  @javax.annotation.Nonnull
  public List<SampleResponseModel> getSamples() {
    return samples;
  }

  public void setSamples(List<SampleResponseModel> samples) {
    this.samples = samples;
  }


  public VoiceResponseModel settings(VoiceSettingsResponseModel settings) {
    this.settings = settings;
    return this;
  }

  /**
   * Get settings
   * @return settings
   */
  @javax.annotation.Nonnull
  public VoiceSettingsResponseModel getSettings() {
    return settings;
  }

  public void setSettings(VoiceSettingsResponseModel settings) {
    this.settings = settings;
  }


  public VoiceResponseModel voiceId(String voiceId) {
    this.voiceId = voiceId;
    return this;
  }

  /**
   * Get voiceId
   * @return voiceId
   */
  @javax.annotation.Nonnull
  public String getVoiceId() {
    return voiceId;
  }

  public void setVoiceId(String voiceId) {
    this.voiceId = voiceId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VoiceResponseModel voiceResponseModel = (VoiceResponseModel) o;
    return Objects.equals(this.availableForTiers, voiceResponseModel.availableForTiers) &&
        Objects.equals(this.category, voiceResponseModel.category) &&
        Objects.equals(this.description, voiceResponseModel.description) &&
        Objects.equals(this.fineTuning, voiceResponseModel.fineTuning) &&
        Objects.equals(this.labels, voiceResponseModel.labels) &&
        Objects.equals(this.name, voiceResponseModel.name) &&
        Objects.equals(this.previewUrl, voiceResponseModel.previewUrl) &&
        Objects.equals(this.samples, voiceResponseModel.samples) &&
        Objects.equals(this.settings, voiceResponseModel.settings) &&
        Objects.equals(this.voiceId, voiceResponseModel.voiceId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(availableForTiers, category, description, fineTuning, labels, name, previewUrl, samples, settings, voiceId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VoiceResponseModel {\n");
    sb.append("    availableForTiers: ").append(toIndentedString(availableForTiers)).append("\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    fineTuning: ").append(toIndentedString(fineTuning)).append("\n");
    sb.append("    labels: ").append(toIndentedString(labels)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    previewUrl: ").append(toIndentedString(previewUrl)).append("\n");
    sb.append("    samples: ").append(toIndentedString(samples)).append("\n");
    sb.append("    settings: ").append(toIndentedString(settings)).append("\n");
    sb.append("    voiceId: ").append(toIndentedString(voiceId)).append("\n");
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
    openapiFields.add("available_for_tiers");
    openapiFields.add("category");
    openapiFields.add("description");
    openapiFields.add("fine_tuning");
    openapiFields.add("labels");
    openapiFields.add("name");
    openapiFields.add("preview_url");
    openapiFields.add("samples");
    openapiFields.add("settings");
    openapiFields.add("voice_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("available_for_tiers");
    openapiRequiredFields.add("category");
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("fine_tuning");
    openapiRequiredFields.add("labels");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("preview_url");
    openapiRequiredFields.add("samples");
    openapiRequiredFields.add("settings");
    openapiRequiredFields.add("voice_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VoiceResponseModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VoiceResponseModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VoiceResponseModel is not found in the empty JSON string", VoiceResponseModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VoiceResponseModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VoiceResponseModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : VoiceResponseModel.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("available_for_tiers") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("available_for_tiers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `available_for_tiers` to be an array in the JSON string but got `%s`", jsonObj.get("available_for_tiers").toString()));
      }
      if (!jsonObj.get("category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("category").toString()));
      }
      if (!jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the required field `fine_tuning`
      FineTuningResponseModel.validateJsonElement(jsonObj.get("fine_tuning"));
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("preview_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preview_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preview_url").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("samples").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `samples` to be an array in the JSON string but got `%s`", jsonObj.get("samples").toString()));
      }

      JsonArray jsonArraysamples = jsonObj.getAsJsonArray("samples");
      // validate the required field `samples` (array)
      for (int i = 0; i < jsonArraysamples.size(); i++) {
        SampleResponseModel.validateJsonElement(jsonArraysamples.get(i));
      };
      // validate the required field `settings`
      VoiceSettingsResponseModel.validateJsonElement(jsonObj.get("settings"));
      if (!jsonObj.get("voice_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `voice_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("voice_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VoiceResponseModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VoiceResponseModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VoiceResponseModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VoiceResponseModel.class));

       return (TypeAdapter<T>) new TypeAdapter<VoiceResponseModel>() {
           @Override
           public void write(JsonWriter out, VoiceResponseModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VoiceResponseModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VoiceResponseModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VoiceResponseModel
   * @throws IOException if the JSON string is invalid with respect to VoiceResponseModel
   */
  public static VoiceResponseModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VoiceResponseModel.class);
  }

  /**
   * Convert an instance of VoiceResponseModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

