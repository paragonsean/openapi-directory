/*
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
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
import java.math.BigDecimal;
import java.net.URI;
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.client.model.Bcc;
import org.openapitools.client.model.Cc;
import org.openapitools.client.model.CellPhone;
import org.openapitools.client.model.ContactData;
import org.openapitools.client.model.CryptoPaymentData;
import org.openapitools.client.model.Cryptocurrency;
import org.openapitools.client.model.Email;
import org.openapitools.client.model.EmailData;
import org.openapitools.client.model.Fax;
import org.openapitools.client.model.GeolocationData;
import org.openapitools.client.model.GeolocationUriFormat;
import org.openapitools.client.model.HomePhone;
import org.openapitools.client.model.PhoneData;
import org.openapitools.client.model.Photo;
import org.openapitools.client.model.SMSData;
import org.openapitools.client.model.Title;
import org.openapitools.client.model.To1;
import org.openapitools.client.model.Url;
import org.openapitools.client.model.Videophone;
import org.openapitools.client.model.WiFiData;
import org.openapitools.client.model.WiFiSecurity;
import org.openapitools.client.model.WorkPhone;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:56.961414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AutoData extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(AutoData.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!AutoData.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'AutoData' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<Object> adapterObject = gson.getDelegateAdapter(this, TypeToken.get(Object.class));
            final TypeAdapter<WiFiData> adapterWiFiData = gson.getDelegateAdapter(this, TypeToken.get(WiFiData.class));
            final TypeAdapter<EmailData> adapterEmailData = gson.getDelegateAdapter(this, TypeToken.get(EmailData.class));
            final TypeAdapter<ContactData> adapterContactData = gson.getDelegateAdapter(this, TypeToken.get(ContactData.class));
            final TypeAdapter<CryptoPaymentData> adapterCryptoPaymentData = gson.getDelegateAdapter(this, TypeToken.get(CryptoPaymentData.class));
            final TypeAdapter<PhoneData> adapterPhoneData = gson.getDelegateAdapter(this, TypeToken.get(PhoneData.class));
            final TypeAdapter<SMSData> adapterSMSData = gson.getDelegateAdapter(this, TypeToken.get(SMSData.class));
            final TypeAdapter<GeolocationData> adapterGeolocationData = gson.getDelegateAdapter(this, TypeToken.get(GeolocationData.class));

            return (TypeAdapter<T>) new TypeAdapter<AutoData>() {
                @Override
                public void write(JsonWriter out, AutoData value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `Object`
                    if (value.getActualInstance() instanceof Object) {
                        JsonPrimitive primitive = adapterObject.toJsonTree((Object)value.getActualInstance()).getAsJsonPrimitive();
                        elementAdapter.write(out, primitive);
                        return;
                    }
                    // check if the actual instance is of the type `WiFiData`
                    if (value.getActualInstance() instanceof WiFiData) {
                        JsonElement element = adapterWiFiData.toJsonTree((WiFiData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EmailData`
                    if (value.getActualInstance() instanceof EmailData) {
                        JsonElement element = adapterEmailData.toJsonTree((EmailData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ContactData`
                    if (value.getActualInstance() instanceof ContactData) {
                        JsonElement element = adapterContactData.toJsonTree((ContactData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `CryptoPaymentData`
                    if (value.getActualInstance() instanceof CryptoPaymentData) {
                        JsonElement element = adapterCryptoPaymentData.toJsonTree((CryptoPaymentData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `PhoneData`
                    if (value.getActualInstance() instanceof PhoneData) {
                        JsonElement element = adapterPhoneData.toJsonTree((PhoneData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `SMSData`
                    if (value.getActualInstance() instanceof SMSData) {
                        JsonElement element = adapterSMSData.toJsonTree((SMSData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `GeolocationData`
                    if (value.getActualInstance() instanceof GeolocationData) {
                        JsonElement element = adapterGeolocationData.toJsonTree((GeolocationData)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: ContactData, CryptoPaymentData, EmailData, GeolocationData, Object, PhoneData, SMSData, WiFiData");
                }

                @Override
                public AutoData read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize Object
                    try {
                        // validate the JSON object to see if any exception is thrown
                        if (!jsonElement.getAsJsonPrimitive().isNumber()) {
                            throw new IllegalArgumentException(String.format("Expected json element to be of type Number in the JSON string but got `%s`", jsonElement.toString()));
                        }
                        actualAdapter = adapterObject;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for Object failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'Object'", e);
                    }
                    // deserialize WiFiData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        WiFiData.validateJsonElement(jsonElement);
                        actualAdapter = adapterWiFiData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for WiFiData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'WiFiData'", e);
                    }
                    // deserialize EmailData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EmailData.validateJsonElement(jsonElement);
                        actualAdapter = adapterEmailData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EmailData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EmailData'", e);
                    }
                    // deserialize ContactData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ContactData.validateJsonElement(jsonElement);
                        actualAdapter = adapterContactData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ContactData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ContactData'", e);
                    }
                    // deserialize CryptoPaymentData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        CryptoPaymentData.validateJsonElement(jsonElement);
                        actualAdapter = adapterCryptoPaymentData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for CryptoPaymentData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'CryptoPaymentData'", e);
                    }
                    // deserialize PhoneData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        PhoneData.validateJsonElement(jsonElement);
                        actualAdapter = adapterPhoneData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for PhoneData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'PhoneData'", e);
                    }
                    // deserialize SMSData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        SMSData.validateJsonElement(jsonElement);
                        actualAdapter = adapterSMSData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for SMSData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'SMSData'", e);
                    }
                    // deserialize GeolocationData
                    try {
                        // validate the JSON object to see if any exception is thrown
                        GeolocationData.validateJsonElement(jsonElement);
                        actualAdapter = adapterGeolocationData;
                        AutoData ret = new AutoData();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for GeolocationData failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'GeolocationData'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for AutoData: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public AutoData() {
        super("anyOf", Boolean.FALSE);
    }

    public AutoData(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("Object", Object.class);
        schemas.put("WiFiData", WiFiData.class);
        schemas.put("EmailData", EmailData.class);
        schemas.put("ContactData", ContactData.class);
        schemas.put("CryptoPaymentData", CryptoPaymentData.class);
        schemas.put("PhoneData", PhoneData.class);
        schemas.put("SMSData", SMSData.class);
        schemas.put("GeolocationData", GeolocationData.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return AutoData.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * ContactData, CryptoPaymentData, EmailData, GeolocationData, Object, PhoneData, SMSData, WiFiData
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof Object) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof WiFiData) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EmailData) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ContactData) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof CryptoPaymentData) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof PhoneData) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof SMSData) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof GeolocationData) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be ContactData, CryptoPaymentData, EmailData, GeolocationData, Object, PhoneData, SMSData, WiFiData");
    }

    /**
     * Get the actual instance, which can be the following:
     * ContactData, CryptoPaymentData, EmailData, GeolocationData, Object, PhoneData, SMSData, WiFiData
     *
     * @return The actual instance (ContactData, CryptoPaymentData, EmailData, GeolocationData, Object, PhoneData, SMSData, WiFiData)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `Object`. If the actual instance is not `Object`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `Object`
     * @throws ClassCastException if the instance is not `Object`
     */
    public Object getObject() throws ClassCastException {
        return (Object)super.getActualInstance();
    }
    /**
     * Get the actual instance of `WiFiData`. If the actual instance is not `WiFiData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `WiFiData`
     * @throws ClassCastException if the instance is not `WiFiData`
     */
    public WiFiData getWiFiData() throws ClassCastException {
        return (WiFiData)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EmailData`. If the actual instance is not `EmailData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EmailData`
     * @throws ClassCastException if the instance is not `EmailData`
     */
    public EmailData getEmailData() throws ClassCastException {
        return (EmailData)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ContactData`. If the actual instance is not `ContactData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ContactData`
     * @throws ClassCastException if the instance is not `ContactData`
     */
    public ContactData getContactData() throws ClassCastException {
        return (ContactData)super.getActualInstance();
    }
    /**
     * Get the actual instance of `CryptoPaymentData`. If the actual instance is not `CryptoPaymentData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `CryptoPaymentData`
     * @throws ClassCastException if the instance is not `CryptoPaymentData`
     */
    public CryptoPaymentData getCryptoPaymentData() throws ClassCastException {
        return (CryptoPaymentData)super.getActualInstance();
    }
    /**
     * Get the actual instance of `PhoneData`. If the actual instance is not `PhoneData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `PhoneData`
     * @throws ClassCastException if the instance is not `PhoneData`
     */
    public PhoneData getPhoneData() throws ClassCastException {
        return (PhoneData)super.getActualInstance();
    }
    /**
     * Get the actual instance of `SMSData`. If the actual instance is not `SMSData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `SMSData`
     * @throws ClassCastException if the instance is not `SMSData`
     */
    public SMSData getSMSData() throws ClassCastException {
        return (SMSData)super.getActualInstance();
    }
    /**
     * Get the actual instance of `GeolocationData`. If the actual instance is not `GeolocationData`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `GeolocationData`
     * @throws ClassCastException if the instance is not `GeolocationData`
     */
    public GeolocationData getGeolocationData() throws ClassCastException {
        return (GeolocationData)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to AutoData
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate anyOf schemas one by one
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with Object
        try {
            if (!jsonElement.getAsJsonPrimitive().isNumber()) {
                throw new IllegalArgumentException(String.format("Expected json element to be of type Number in the JSON string but got `%s`", jsonElement.toString()));
            }
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for Object failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with WiFiData
        try {
            WiFiData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for WiFiData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EmailData
        try {
            EmailData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EmailData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ContactData
        try {
            ContactData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ContactData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with CryptoPaymentData
        try {
            CryptoPaymentData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for CryptoPaymentData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with PhoneData
        try {
            PhoneData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for PhoneData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with SMSData
        try {
            SMSData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for SMSData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with GeolocationData
        try {
            GeolocationData.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for GeolocationData failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for AutoData with anyOf schemas: ContactData, CryptoPaymentData, EmailData, GeolocationData, Object, PhoneData, SMSData, WiFiData. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of AutoData given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of AutoData
     * @throws IOException if the JSON string is invalid with respect to AutoData
     */
    public static AutoData fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, AutoData.class);
    }

    /**
     * Convert an instance of AutoData to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

