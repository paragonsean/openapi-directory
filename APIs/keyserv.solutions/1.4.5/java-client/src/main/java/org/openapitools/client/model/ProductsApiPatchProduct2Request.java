/*
 * KeyServ
 * KeyServ API
 *
 * The version of the OpenAPI document: 1.4.5
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
import org.openapitools.client.model.ProductCreateModify;
import org.openapitools.jackson.nullable.JsonNullable;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:23.294884-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductsApiPatchProduct2Request extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(ProductsApiPatchProduct2Request.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!ProductsApiPatchProduct2Request.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'ProductsApiPatchProduct2Request' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<ProductCreateModify> adapterProductCreateModify = gson.getDelegateAdapter(this, TypeToken.get(ProductCreateModify.class));

            return (TypeAdapter<T>) new TypeAdapter<ProductsApiPatchProduct2Request>() {
                @Override
                public void write(JsonWriter out, ProductsApiPatchProduct2Request value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `ProductCreateModify`
                    if (value.getActualInstance() instanceof ProductCreateModify) {
                        JsonElement element = adapterProductCreateModify.toJsonTree((ProductCreateModify)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: ProductCreateModify");
                }

                @Override
                public ProductsApiPatchProduct2Request read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize ProductCreateModify
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ProductCreateModify.validateJsonElement(jsonElement);
                        actualAdapter = adapterProductCreateModify;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'ProductCreateModify'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ProductCreateModify failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ProductCreateModify'", e);
                    }

                    if (match == 1) {
                        ProductsApiPatchProduct2Request ret = new ProductsApiPatchProduct2Request();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for ProductsApiPatchProduct2Request: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public ProductsApiPatchProduct2Request() {
        super("oneOf", Boolean.TRUE);
    }

    public ProductsApiPatchProduct2Request(Object o) {
        super("oneOf", Boolean.TRUE);
        setActualInstance(o);
    }

    static {
        schemas.put("ProductCreateModify", ProductCreateModify.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return ProductsApiPatchProduct2Request.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * ProductCreateModify
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance == null) {
           super.setActualInstance(instance);
           return;
        }

        if (instance instanceof ProductCreateModify) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be ProductCreateModify");
    }

    /**
     * Get the actual instance, which can be the following:
     * ProductCreateModify
     *
     * @return The actual instance (ProductCreateModify)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `ProductCreateModify`. If the actual instance is not `ProductCreateModify`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ProductCreateModify`
     * @throws ClassCastException if the instance is not `ProductCreateModify`
     */
    public ProductCreateModify getProductCreateModify() throws ClassCastException {
        return (ProductCreateModify)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to ProductsApiPatchProduct2Request
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with ProductCreateModify
        try {
            ProductCreateModify.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ProductCreateModify failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for ProductsApiPatchProduct2Request with oneOf schemas: ProductCreateModify. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of ProductsApiPatchProduct2Request given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of ProductsApiPatchProduct2Request
     * @throws IOException if the JSON string is invalid with respect to ProductsApiPatchProduct2Request
     */
    public static ProductsApiPatchProduct2Request fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, ProductsApiPatchProduct2Request.class);
    }

    /**
     * Convert an instance of ProductsApiPatchProduct2Request to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

