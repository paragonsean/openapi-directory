/*
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.Address;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:01.468742-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetAllAddressesResponseListInner extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(GetAllAddressesResponseListInner.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!GetAllAddressesResponseListInner.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'GetAllAddressesResponseListInner' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<Address> adapterAddress = gson.getDelegateAdapter(this, TypeToken.get(Address.class));

            return (TypeAdapter<T>) new TypeAdapter<GetAllAddressesResponseListInner>() {
                @Override
                public void write(JsonWriter out, GetAllAddressesResponseListInner value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `Address`
                    if (value.getActualInstance() instanceof Address) {
                        JsonElement element = adapterAddress.toJsonTree((Address)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: Address");
                }

                @Override
                public GetAllAddressesResponseListInner read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize Address
                    try {
                        // validate the JSON object to see if any exception is thrown
                        Address.validateJsonElement(jsonElement);
                        actualAdapter = adapterAddress;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'Address'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for Address failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'Address'", e);
                    }

                    if (match == 1) {
                        GetAllAddressesResponseListInner ret = new GetAllAddressesResponseListInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for GetAllAddressesResponseListInner: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public GetAllAddressesResponseListInner() {
        super("oneOf", Boolean.FALSE);
    }

    public GetAllAddressesResponseListInner(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("Address", Address.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return GetAllAddressesResponseListInner.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * Address
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof Address) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be Address");
    }

    /**
     * Get the actual instance, which can be the following:
     * Address
     *
     * @return The actual instance (Address)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `Address`. If the actual instance is not `Address`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `Address`
     * @throws ClassCastException if the instance is not `Address`
     */
    public Address getAddress() throws ClassCastException {
        return (Address)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to GetAllAddressesResponseListInner
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with Address
        try {
            Address.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for Address failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for GetAllAddressesResponseListInner with oneOf schemas: Address. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of GetAllAddressesResponseListInner given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of GetAllAddressesResponseListInner
     * @throws IOException if the JSON string is invalid with respect to GetAllAddressesResponseListInner
     */
    public static GetAllAddressesResponseListInner fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, GetAllAddressesResponseListInner.class);
    }

    /**
     * Convert an instance of GetAllAddressesResponseListInner to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

