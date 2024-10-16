/*
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
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
import org.openapitools.client.model.ArtistObject;
import org.openapitools.client.model.EpisodeObject;
import org.openapitools.client.model.EpisodeRestrictionObject;
import org.openapitools.client.model.ExternalIdObject;
import org.openapitools.client.model.ExternalUrlObject;
import org.openapitools.client.model.ImageObject;
import org.openapitools.client.model.LinkedTrackObject;
import org.openapitools.client.model.ResumePointObject;
import org.openapitools.client.model.SimplifiedAlbumObject;
import org.openapitools.client.model.SimplifiedShowObject;
import org.openapitools.client.model.TrackObject;



import java.io.IOException;
import java.lang.reflect.Type;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.JsonPrimitive;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonParseException;

import org.openapitools.client.JSON;

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:56.088414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CurrentlyPlayingContextObjectItem extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(CurrentlyPlayingContextObjectItem.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!CurrentlyPlayingContextObjectItem.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'CurrentlyPlayingContextObjectItem' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<TrackObject> adapterTrackObject = gson.getDelegateAdapter(this, TypeToken.get(TrackObject.class));
            final TypeAdapter<EpisodeObject> adapterEpisodeObject = gson.getDelegateAdapter(this, TypeToken.get(EpisodeObject.class));

            return (TypeAdapter<T>) new TypeAdapter<CurrentlyPlayingContextObjectItem>() {
                @Override
                public void write(JsonWriter out, CurrentlyPlayingContextObjectItem value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `TrackObject`
                    if (value.getActualInstance() instanceof TrackObject) {
                        JsonElement element = adapterTrackObject.toJsonTree((TrackObject)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EpisodeObject`
                    if (value.getActualInstance() instanceof EpisodeObject) {
                        JsonElement element = adapterEpisodeObject.toJsonTree((EpisodeObject)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: EpisodeObject, TrackObject");
                }

                @Override
                public CurrentlyPlayingContextObjectItem read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize TrackObject
                    try {
                        // validate the JSON object to see if any exception is thrown
                        TrackObject.validateJsonElement(jsonElement);
                        actualAdapter = adapterTrackObject;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'TrackObject'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for TrackObject failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'TrackObject'", e);
                    }
                    // deserialize EpisodeObject
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EpisodeObject.validateJsonElement(jsonElement);
                        actualAdapter = adapterEpisodeObject;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EpisodeObject'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EpisodeObject failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EpisodeObject'", e);
                    }

                    if (match == 1) {
                        CurrentlyPlayingContextObjectItem ret = new CurrentlyPlayingContextObjectItem();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for CurrentlyPlayingContextObjectItem: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public CurrentlyPlayingContextObjectItem() {
        super("oneOf", Boolean.FALSE);
    }

    public CurrentlyPlayingContextObjectItem(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("TrackObject", TrackObject.class);
        schemas.put("EpisodeObject", EpisodeObject.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return CurrentlyPlayingContextObjectItem.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * EpisodeObject, TrackObject
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof TrackObject) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EpisodeObject) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be EpisodeObject, TrackObject");
    }

    /**
     * Get the actual instance, which can be the following:
     * EpisodeObject, TrackObject
     *
     * @return The actual instance (EpisodeObject, TrackObject)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `TrackObject`. If the actual instance is not `TrackObject`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `TrackObject`
     * @throws ClassCastException if the instance is not `TrackObject`
     */
    public TrackObject getTrackObject() throws ClassCastException {
        return (TrackObject)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EpisodeObject`. If the actual instance is not `EpisodeObject`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EpisodeObject`
     * @throws ClassCastException if the instance is not `EpisodeObject`
     */
    public EpisodeObject getEpisodeObject() throws ClassCastException {
        return (EpisodeObject)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to CurrentlyPlayingContextObjectItem
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with TrackObject
        try {
            TrackObject.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for TrackObject failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EpisodeObject
        try {
            EpisodeObject.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EpisodeObject failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for CurrentlyPlayingContextObjectItem with oneOf schemas: EpisodeObject, TrackObject. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of CurrentlyPlayingContextObjectItem given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of CurrentlyPlayingContextObjectItem
     * @throws IOException if the JSON string is invalid with respect to CurrentlyPlayingContextObjectItem
     */
    public static CurrentlyPlayingContextObjectItem fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, CurrentlyPlayingContextObjectItem.class);
    }

    /**
     * Convert an instance of CurrentlyPlayingContextObjectItem to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

