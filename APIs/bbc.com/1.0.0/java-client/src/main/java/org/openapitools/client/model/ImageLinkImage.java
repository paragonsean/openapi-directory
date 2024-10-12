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
import java.util.Arrays;
import org.openapitools.client.model.DeprecationAttributes;
import org.openapitools.client.model.ImageLinkImageAnyOf;
import org.openapitools.client.model.ImageLinkImageAnyOfImage;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageLinkImage extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(ImageLinkImage.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!ImageLinkImage.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'ImageLinkImage' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<DeprecationAttributes> adapterDeprecationAttributes = gson.getDelegateAdapter(this, TypeToken.get(DeprecationAttributes.class));
            final TypeAdapter<ImageLinkImageAnyOf> adapterImageLinkImageAnyOf = gson.getDelegateAdapter(this, TypeToken.get(ImageLinkImageAnyOf.class));

            return (TypeAdapter<T>) new TypeAdapter<ImageLinkImage>() {
                @Override
                public void write(JsonWriter out, ImageLinkImage value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `DeprecationAttributes`
                    if (value.getActualInstance() instanceof DeprecationAttributes) {
                        JsonElement element = adapterDeprecationAttributes.toJsonTree((DeprecationAttributes)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImageLinkImageAnyOf`
                    if (value.getActualInstance() instanceof ImageLinkImageAnyOf) {
                        JsonElement element = adapterImageLinkImageAnyOf.toJsonTree((ImageLinkImageAnyOf)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: DeprecationAttributes, ImageLinkImageAnyOf");
                }

                @Override
                public ImageLinkImage read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize DeprecationAttributes
                    try {
                        // validate the JSON object to see if any exception is thrown
                        DeprecationAttributes.validateJsonElement(jsonElement);
                        actualAdapter = adapterDeprecationAttributes;
                        ImageLinkImage ret = new ImageLinkImage();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for DeprecationAttributes failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'DeprecationAttributes'", e);
                    }
                    // deserialize ImageLinkImageAnyOf
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImageLinkImageAnyOf.validateJsonElement(jsonElement);
                        actualAdapter = adapterImageLinkImageAnyOf;
                        ImageLinkImage ret = new ImageLinkImage();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImageLinkImageAnyOf failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImageLinkImageAnyOf'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for ImageLinkImage: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public ImageLinkImage() {
        super("anyOf", Boolean.FALSE);
    }

    public ImageLinkImage(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("DeprecationAttributes", DeprecationAttributes.class);
        schemas.put("ImageLinkImageAnyOf", ImageLinkImageAnyOf.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return ImageLinkImage.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * DeprecationAttributes, ImageLinkImageAnyOf
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof DeprecationAttributes) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImageLinkImageAnyOf) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be DeprecationAttributes, ImageLinkImageAnyOf");
    }

    /**
     * Get the actual instance, which can be the following:
     * DeprecationAttributes, ImageLinkImageAnyOf
     *
     * @return The actual instance (DeprecationAttributes, ImageLinkImageAnyOf)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `DeprecationAttributes`. If the actual instance is not `DeprecationAttributes`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `DeprecationAttributes`
     * @throws ClassCastException if the instance is not `DeprecationAttributes`
     */
    public DeprecationAttributes getDeprecationAttributes() throws ClassCastException {
        return (DeprecationAttributes)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImageLinkImageAnyOf`. If the actual instance is not `ImageLinkImageAnyOf`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImageLinkImageAnyOf`
     * @throws ClassCastException if the instance is not `ImageLinkImageAnyOf`
     */
    public ImageLinkImageAnyOf getImageLinkImageAnyOf() throws ClassCastException {
        return (ImageLinkImageAnyOf)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to ImageLinkImage
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate anyOf schemas one by one
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with DeprecationAttributes
        try {
            DeprecationAttributes.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for DeprecationAttributes failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImageLinkImageAnyOf
        try {
            ImageLinkImageAnyOf.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImageLinkImageAnyOf failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for ImageLinkImage with anyOf schemas: DeprecationAttributes, ImageLinkImageAnyOf. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of ImageLinkImage given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of ImageLinkImage
     * @throws IOException if the JSON string is invalid with respect to ImageLinkImage
     */
    public static ImageLinkImage fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, ImageLinkImage.class);
    }

    /**
     * Convert an instance of ImageLinkImage to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

