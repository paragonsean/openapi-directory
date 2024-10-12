/*
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
 *
 * The version of the OpenAPI document: 1.0.0
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
import java.util.Arrays;
import org.openapitools.client.model.MediasPostRequestPayloadIncludedInnerOneOf;
import org.openapitools.client.model.MediasPostRequestPayloadIncludedInnerOneOf1;
import org.openapitools.client.model.MediasPostRequestPayloadIncludedInnerOneOf1Attributes;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:59:27.157946-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MediasPostRequestPayloadIncludedInner extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(MediasPostRequestPayloadIncludedInner.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!MediasPostRequestPayloadIncludedInner.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'MediasPostRequestPayloadIncludedInner' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<MediasPostRequestPayloadIncludedInnerOneOf> adapterMediasPostRequestPayloadIncludedInnerOneOf = gson.getDelegateAdapter(this, TypeToken.get(MediasPostRequestPayloadIncludedInnerOneOf.class));
            final TypeAdapter<MediasPostRequestPayloadIncludedInnerOneOf1> adapterMediasPostRequestPayloadIncludedInnerOneOf1 = gson.getDelegateAdapter(this, TypeToken.get(MediasPostRequestPayloadIncludedInnerOneOf1.class));

            return (TypeAdapter<T>) new TypeAdapter<MediasPostRequestPayloadIncludedInner>() {
                @Override
                public void write(JsonWriter out, MediasPostRequestPayloadIncludedInner value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `MediasPostRequestPayloadIncludedInnerOneOf`
                    if (value.getActualInstance() instanceof MediasPostRequestPayloadIncludedInnerOneOf) {
                        JsonElement element = adapterMediasPostRequestPayloadIncludedInnerOneOf.toJsonTree((MediasPostRequestPayloadIncludedInnerOneOf)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `MediasPostRequestPayloadIncludedInnerOneOf1`
                    if (value.getActualInstance() instanceof MediasPostRequestPayloadIncludedInnerOneOf1) {
                        JsonElement element = adapterMediasPostRequestPayloadIncludedInnerOneOf1.toJsonTree((MediasPostRequestPayloadIncludedInnerOneOf1)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: MediasPostRequestPayloadIncludedInnerOneOf, MediasPostRequestPayloadIncludedInnerOneOf1");
                }

                @Override
                public MediasPostRequestPayloadIncludedInner read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize MediasPostRequestPayloadIncludedInnerOneOf
                    try {
                        // validate the JSON object to see if any exception is thrown
                        MediasPostRequestPayloadIncludedInnerOneOf.validateJsonElement(jsonElement);
                        actualAdapter = adapterMediasPostRequestPayloadIncludedInnerOneOf;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'MediasPostRequestPayloadIncludedInnerOneOf'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for MediasPostRequestPayloadIncludedInnerOneOf failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'MediasPostRequestPayloadIncludedInnerOneOf'", e);
                    }
                    // deserialize MediasPostRequestPayloadIncludedInnerOneOf1
                    try {
                        // validate the JSON object to see if any exception is thrown
                        MediasPostRequestPayloadIncludedInnerOneOf1.validateJsonElement(jsonElement);
                        actualAdapter = adapterMediasPostRequestPayloadIncludedInnerOneOf1;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'MediasPostRequestPayloadIncludedInnerOneOf1'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for MediasPostRequestPayloadIncludedInnerOneOf1 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'MediasPostRequestPayloadIncludedInnerOneOf1'", e);
                    }

                    if (match == 1) {
                        MediasPostRequestPayloadIncludedInner ret = new MediasPostRequestPayloadIncludedInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for MediasPostRequestPayloadIncludedInner: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public MediasPostRequestPayloadIncludedInner() {
        super("oneOf", Boolean.FALSE);
    }

    public MediasPostRequestPayloadIncludedInner(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("MediasPostRequestPayloadIncludedInnerOneOf", MediasPostRequestPayloadIncludedInnerOneOf.class);
        schemas.put("MediasPostRequestPayloadIncludedInnerOneOf1", MediasPostRequestPayloadIncludedInnerOneOf1.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return MediasPostRequestPayloadIncludedInner.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * MediasPostRequestPayloadIncludedInnerOneOf, MediasPostRequestPayloadIncludedInnerOneOf1
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof MediasPostRequestPayloadIncludedInnerOneOf) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof MediasPostRequestPayloadIncludedInnerOneOf1) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be MediasPostRequestPayloadIncludedInnerOneOf, MediasPostRequestPayloadIncludedInnerOneOf1");
    }

    /**
     * Get the actual instance, which can be the following:
     * MediasPostRequestPayloadIncludedInnerOneOf, MediasPostRequestPayloadIncludedInnerOneOf1
     *
     * @return The actual instance (MediasPostRequestPayloadIncludedInnerOneOf, MediasPostRequestPayloadIncludedInnerOneOf1)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `MediasPostRequestPayloadIncludedInnerOneOf`. If the actual instance is not `MediasPostRequestPayloadIncludedInnerOneOf`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `MediasPostRequestPayloadIncludedInnerOneOf`
     * @throws ClassCastException if the instance is not `MediasPostRequestPayloadIncludedInnerOneOf`
     */
    public MediasPostRequestPayloadIncludedInnerOneOf getMediasPostRequestPayloadIncludedInnerOneOf() throws ClassCastException {
        return (MediasPostRequestPayloadIncludedInnerOneOf)super.getActualInstance();
    }
    /**
     * Get the actual instance of `MediasPostRequestPayloadIncludedInnerOneOf1`. If the actual instance is not `MediasPostRequestPayloadIncludedInnerOneOf1`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `MediasPostRequestPayloadIncludedInnerOneOf1`
     * @throws ClassCastException if the instance is not `MediasPostRequestPayloadIncludedInnerOneOf1`
     */
    public MediasPostRequestPayloadIncludedInnerOneOf1 getMediasPostRequestPayloadIncludedInnerOneOf1() throws ClassCastException {
        return (MediasPostRequestPayloadIncludedInnerOneOf1)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to MediasPostRequestPayloadIncludedInner
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with MediasPostRequestPayloadIncludedInnerOneOf
        try {
            MediasPostRequestPayloadIncludedInnerOneOf.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for MediasPostRequestPayloadIncludedInnerOneOf failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with MediasPostRequestPayloadIncludedInnerOneOf1
        try {
            MediasPostRequestPayloadIncludedInnerOneOf1.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for MediasPostRequestPayloadIncludedInnerOneOf1 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for MediasPostRequestPayloadIncludedInner with oneOf schemas: MediasPostRequestPayloadIncludedInnerOneOf, MediasPostRequestPayloadIncludedInnerOneOf1. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of MediasPostRequestPayloadIncludedInner given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of MediasPostRequestPayloadIncludedInner
     * @throws IOException if the JSON string is invalid with respect to MediasPostRequestPayloadIncludedInner
     */
    public static MediasPostRequestPayloadIncludedInner fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, MediasPostRequestPayloadIncludedInner.class);
    }

    /**
     * Convert an instance of MediasPostRequestPayloadIncludedInner to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

