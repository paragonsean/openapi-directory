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
import org.openapitools.client.model.CustomAudio;
import org.openapitools.client.model.DeletedItem;
import org.openapitools.client.model.EpisodeSimple;
import org.openapitools.client.model.PodcastExtraField;
import org.openapitools.client.model.PodcastLookingForField;
import org.openapitools.client.model.PodcastMinimum;
import org.openapitools.client.model.PodcastSimple;
import org.openapitools.client.model.PodcastTypeField;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:39.439950-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaylistItemData extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(PlaylistItemData.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!PlaylistItemData.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'PlaylistItemData' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<EpisodeSimple> adapterEpisodeSimple = gson.getDelegateAdapter(this, TypeToken.get(EpisodeSimple.class));
            final TypeAdapter<PodcastSimple> adapterPodcastSimple = gson.getDelegateAdapter(this, TypeToken.get(PodcastSimple.class));
            final TypeAdapter<CustomAudio> adapterCustomAudio = gson.getDelegateAdapter(this, TypeToken.get(CustomAudio.class));
            final TypeAdapter<DeletedItem> adapterDeletedItem = gson.getDelegateAdapter(this, TypeToken.get(DeletedItem.class));

            return (TypeAdapter<T>) new TypeAdapter<PlaylistItemData>() {
                @Override
                public void write(JsonWriter out, PlaylistItemData value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `EpisodeSimple`
                    if (value.getActualInstance() instanceof EpisodeSimple) {
                        JsonElement element = adapterEpisodeSimple.toJsonTree((EpisodeSimple)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `PodcastSimple`
                    if (value.getActualInstance() instanceof PodcastSimple) {
                        JsonElement element = adapterPodcastSimple.toJsonTree((PodcastSimple)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `CustomAudio`
                    if (value.getActualInstance() instanceof CustomAudio) {
                        JsonElement element = adapterCustomAudio.toJsonTree((CustomAudio)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `DeletedItem`
                    if (value.getActualInstance() instanceof DeletedItem) {
                        JsonElement element = adapterDeletedItem.toJsonTree((DeletedItem)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: CustomAudio, DeletedItem, EpisodeSimple, PodcastSimple");
                }

                @Override
                public PlaylistItemData read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize EpisodeSimple
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EpisodeSimple.validateJsonElement(jsonElement);
                        actualAdapter = adapterEpisodeSimple;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EpisodeSimple'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EpisodeSimple failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EpisodeSimple'", e);
                    }
                    // deserialize PodcastSimple
                    try {
                        // validate the JSON object to see if any exception is thrown
                        PodcastSimple.validateJsonElement(jsonElement);
                        actualAdapter = adapterPodcastSimple;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'PodcastSimple'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for PodcastSimple failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'PodcastSimple'", e);
                    }
                    // deserialize CustomAudio
                    try {
                        // validate the JSON object to see if any exception is thrown
                        CustomAudio.validateJsonElement(jsonElement);
                        actualAdapter = adapterCustomAudio;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'CustomAudio'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for CustomAudio failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'CustomAudio'", e);
                    }
                    // deserialize DeletedItem
                    try {
                        // validate the JSON object to see if any exception is thrown
                        DeletedItem.validateJsonElement(jsonElement);
                        actualAdapter = adapterDeletedItem;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'DeletedItem'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for DeletedItem failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'DeletedItem'", e);
                    }

                    if (match == 1) {
                        PlaylistItemData ret = new PlaylistItemData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for PlaylistItemData: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public PlaylistItemData() {
        super("oneOf", Boolean.FALSE);
    }

    public PlaylistItemData(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("EpisodeSimple", EpisodeSimple.class);
        schemas.put("PodcastSimple", PodcastSimple.class);
        schemas.put("CustomAudio", CustomAudio.class);
        schemas.put("DeletedItem", DeletedItem.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return PlaylistItemData.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * CustomAudio, DeletedItem, EpisodeSimple, PodcastSimple
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof EpisodeSimple) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof PodcastSimple) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof CustomAudio) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof DeletedItem) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be CustomAudio, DeletedItem, EpisodeSimple, PodcastSimple");
    }

    /**
     * Get the actual instance, which can be the following:
     * CustomAudio, DeletedItem, EpisodeSimple, PodcastSimple
     *
     * @return The actual instance (CustomAudio, DeletedItem, EpisodeSimple, PodcastSimple)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `EpisodeSimple`. If the actual instance is not `EpisodeSimple`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EpisodeSimple`
     * @throws ClassCastException if the instance is not `EpisodeSimple`
     */
    public EpisodeSimple getEpisodeSimple() throws ClassCastException {
        return (EpisodeSimple)super.getActualInstance();
    }
    /**
     * Get the actual instance of `PodcastSimple`. If the actual instance is not `PodcastSimple`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `PodcastSimple`
     * @throws ClassCastException if the instance is not `PodcastSimple`
     */
    public PodcastSimple getPodcastSimple() throws ClassCastException {
        return (PodcastSimple)super.getActualInstance();
    }
    /**
     * Get the actual instance of `CustomAudio`. If the actual instance is not `CustomAudio`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `CustomAudio`
     * @throws ClassCastException if the instance is not `CustomAudio`
     */
    public CustomAudio getCustomAudio() throws ClassCastException {
        return (CustomAudio)super.getActualInstance();
    }
    /**
     * Get the actual instance of `DeletedItem`. If the actual instance is not `DeletedItem`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `DeletedItem`
     * @throws ClassCastException if the instance is not `DeletedItem`
     */
    public DeletedItem getDeletedItem() throws ClassCastException {
        return (DeletedItem)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to PlaylistItemData
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with EpisodeSimple
        try {
            EpisodeSimple.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EpisodeSimple failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with PodcastSimple
        try {
            PodcastSimple.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for PodcastSimple failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with CustomAudio
        try {
            CustomAudio.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for CustomAudio failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with DeletedItem
        try {
            DeletedItem.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for DeletedItem failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for PlaylistItemData with oneOf schemas: CustomAudio, DeletedItem, EpisodeSimple, PodcastSimple. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of PlaylistItemData given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of PlaylistItemData
     * @throws IOException if the JSON string is invalid with respect to PlaylistItemData
     */
    public static PlaylistItemData fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, PlaylistItemData.class);
    }

    /**
     * Convert an instance of PlaylistItemData to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

