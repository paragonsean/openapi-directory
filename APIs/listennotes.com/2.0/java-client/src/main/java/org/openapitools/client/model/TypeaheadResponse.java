/*
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
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
import org.openapitools.client.model.Genre;
import org.openapitools.client.model.PodcastTypeaheadResult;

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
 * TypeaheadResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:39.439950-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TypeaheadResponse {
  public static final String SERIALIZED_NAME_GENRES = "genres";
  @SerializedName(SERIALIZED_NAME_GENRES)
  private List<Genre> genres = new ArrayList<>();

  public static final String SERIALIZED_NAME_PODCASTS = "podcasts";
  @SerializedName(SERIALIZED_NAME_PODCASTS)
  private List<PodcastTypeaheadResult> podcasts = new ArrayList<>();

  public static final String SERIALIZED_NAME_TERMS = "terms";
  @SerializedName(SERIALIZED_NAME_TERMS)
  private List<String> terms = new ArrayList<>();

  public TypeaheadResponse() {
  }

  public TypeaheadResponse genres(List<Genre> genres) {
    this.genres = genres;
    return this;
  }

  public TypeaheadResponse addGenresItem(Genre genresItem) {
    if (this.genres == null) {
      this.genres = new ArrayList<>();
    }
    this.genres.add(genresItem);
    return this;
  }

  /**
   * Genre suggestions. It&#39;ll show up when the **show_genres** parameter is *1*.
   * @return genres
   */
  @javax.annotation.Nullable
  public List<Genre> getGenres() {
    return genres;
  }

  public void setGenres(List<Genre> genres) {
    this.genres = genres;
  }


  public TypeaheadResponse podcasts(List<PodcastTypeaheadResult> podcasts) {
    this.podcasts = podcasts;
    return this;
  }

  public TypeaheadResponse addPodcastsItem(PodcastTypeaheadResult podcastsItem) {
    if (this.podcasts == null) {
      this.podcasts = new ArrayList<>();
    }
    this.podcasts.add(podcastsItem);
    return this;
  }

  /**
   * Podcast suggestions. It&#39;ll show up when the **show_podcasts** parameter is 1.
   * @return podcasts
   */
  @javax.annotation.Nullable
  public List<PodcastTypeaheadResult> getPodcasts() {
    return podcasts;
  }

  public void setPodcasts(List<PodcastTypeaheadResult> podcasts) {
    this.podcasts = podcasts;
  }


  public TypeaheadResponse terms(List<String> terms) {
    this.terms = terms;
    return this;
  }

  public TypeaheadResponse addTermsItem(String termsItem) {
    if (this.terms == null) {
      this.terms = new ArrayList<>();
    }
    this.terms.add(termsItem);
    return this;
  }

  /**
   * Search term suggestions.
   * @return terms
   */
  @javax.annotation.Nonnull
  public List<String> getTerms() {
    return terms;
  }

  public void setTerms(List<String> terms) {
    this.terms = terms;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TypeaheadResponse typeaheadResponse = (TypeaheadResponse) o;
    return Objects.equals(this.genres, typeaheadResponse.genres) &&
        Objects.equals(this.podcasts, typeaheadResponse.podcasts) &&
        Objects.equals(this.terms, typeaheadResponse.terms);
  }

  @Override
  public int hashCode() {
    return Objects.hash(genres, podcasts, terms);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TypeaheadResponse {\n");
    sb.append("    genres: ").append(toIndentedString(genres)).append("\n");
    sb.append("    podcasts: ").append(toIndentedString(podcasts)).append("\n");
    sb.append("    terms: ").append(toIndentedString(terms)).append("\n");
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
    openapiFields.add("genres");
    openapiFields.add("podcasts");
    openapiFields.add("terms");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("terms");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TypeaheadResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TypeaheadResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TypeaheadResponse is not found in the empty JSON string", TypeaheadResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TypeaheadResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TypeaheadResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TypeaheadResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("genres") != null && !jsonObj.get("genres").isJsonNull()) {
        JsonArray jsonArraygenres = jsonObj.getAsJsonArray("genres");
        if (jsonArraygenres != null) {
          // ensure the json data is an array
          if (!jsonObj.get("genres").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `genres` to be an array in the JSON string but got `%s`", jsonObj.get("genres").toString()));
          }

          // validate the optional field `genres` (array)
          for (int i = 0; i < jsonArraygenres.size(); i++) {
            Genre.validateJsonElement(jsonArraygenres.get(i));
          };
        }
      }
      if (jsonObj.get("podcasts") != null && !jsonObj.get("podcasts").isJsonNull()) {
        JsonArray jsonArraypodcasts = jsonObj.getAsJsonArray("podcasts");
        if (jsonArraypodcasts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("podcasts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `podcasts` to be an array in the JSON string but got `%s`", jsonObj.get("podcasts").toString()));
          }

          // validate the optional field `podcasts` (array)
          for (int i = 0; i < jsonArraypodcasts.size(); i++) {
            PodcastTypeaheadResult.validateJsonElement(jsonArraypodcasts.get(i));
          };
        }
      }
      // ensure the required json array is present
      if (jsonObj.get("terms") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("terms").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `terms` to be an array in the JSON string but got `%s`", jsonObj.get("terms").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TypeaheadResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TypeaheadResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TypeaheadResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TypeaheadResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TypeaheadResponse>() {
           @Override
           public void write(JsonWriter out, TypeaheadResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TypeaheadResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TypeaheadResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TypeaheadResponse
   * @throws IOException if the JSON string is invalid with respect to TypeaheadResponse
   */
  public static TypeaheadResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TypeaheadResponse.class);
  }

  /**
   * Convert an instance of TypeaheadResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

