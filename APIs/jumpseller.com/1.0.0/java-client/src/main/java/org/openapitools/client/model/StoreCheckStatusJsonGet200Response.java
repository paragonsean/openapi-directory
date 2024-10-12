/*
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
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
import org.openapitools.client.model.NewPartnerStore;
import org.openapitools.client.model.NewPartnerStoreStore;
import org.openapitools.client.model.PartnerStoreStatus;
import org.openapitools.client.model.PartnerStoreStatusStatus;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StoreCheckStatusJsonGet200Response extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(StoreCheckStatusJsonGet200Response.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!StoreCheckStatusJsonGet200Response.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'StoreCheckStatusJsonGet200Response' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<PartnerStoreStatus> adapterPartnerStoreStatus = gson.getDelegateAdapter(this, TypeToken.get(PartnerStoreStatus.class));
            final TypeAdapter<NewPartnerStore> adapterNewPartnerStore = gson.getDelegateAdapter(this, TypeToken.get(NewPartnerStore.class));

            return (TypeAdapter<T>) new TypeAdapter<StoreCheckStatusJsonGet200Response>() {
                @Override
                public void write(JsonWriter out, StoreCheckStatusJsonGet200Response value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `PartnerStoreStatus`
                    if (value.getActualInstance() instanceof PartnerStoreStatus) {
                        JsonElement element = adapterPartnerStoreStatus.toJsonTree((PartnerStoreStatus)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `NewPartnerStore`
                    if (value.getActualInstance() instanceof NewPartnerStore) {
                        JsonElement element = adapterNewPartnerStore.toJsonTree((NewPartnerStore)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: NewPartnerStore, PartnerStoreStatus");
                }

                @Override
                public StoreCheckStatusJsonGet200Response read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize PartnerStoreStatus
                    try {
                        // validate the JSON object to see if any exception is thrown
                        PartnerStoreStatus.validateJsonElement(jsonElement);
                        actualAdapter = adapterPartnerStoreStatus;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'PartnerStoreStatus'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for PartnerStoreStatus failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'PartnerStoreStatus'", e);
                    }
                    // deserialize NewPartnerStore
                    try {
                        // validate the JSON object to see if any exception is thrown
                        NewPartnerStore.validateJsonElement(jsonElement);
                        actualAdapter = adapterNewPartnerStore;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'NewPartnerStore'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for NewPartnerStore failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'NewPartnerStore'", e);
                    }

                    if (match == 1) {
                        StoreCheckStatusJsonGet200Response ret = new StoreCheckStatusJsonGet200Response();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for StoreCheckStatusJsonGet200Response: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public StoreCheckStatusJsonGet200Response() {
        super("oneOf", Boolean.FALSE);
    }

    public StoreCheckStatusJsonGet200Response(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("PartnerStoreStatus", PartnerStoreStatus.class);
        schemas.put("NewPartnerStore", NewPartnerStore.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return StoreCheckStatusJsonGet200Response.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * NewPartnerStore, PartnerStoreStatus
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof PartnerStoreStatus) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof NewPartnerStore) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be NewPartnerStore, PartnerStoreStatus");
    }

    /**
     * Get the actual instance, which can be the following:
     * NewPartnerStore, PartnerStoreStatus
     *
     * @return The actual instance (NewPartnerStore, PartnerStoreStatus)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `PartnerStoreStatus`. If the actual instance is not `PartnerStoreStatus`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `PartnerStoreStatus`
     * @throws ClassCastException if the instance is not `PartnerStoreStatus`
     */
    public PartnerStoreStatus getPartnerStoreStatus() throws ClassCastException {
        return (PartnerStoreStatus)super.getActualInstance();
    }
    /**
     * Get the actual instance of `NewPartnerStore`. If the actual instance is not `NewPartnerStore`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `NewPartnerStore`
     * @throws ClassCastException if the instance is not `NewPartnerStore`
     */
    public NewPartnerStore getNewPartnerStore() throws ClassCastException {
        return (NewPartnerStore)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to StoreCheckStatusJsonGet200Response
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with PartnerStoreStatus
        try {
            PartnerStoreStatus.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for PartnerStoreStatus failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with NewPartnerStore
        try {
            NewPartnerStore.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for NewPartnerStore failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for StoreCheckStatusJsonGet200Response with oneOf schemas: NewPartnerStore, PartnerStoreStatus. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of StoreCheckStatusJsonGet200Response given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of StoreCheckStatusJsonGet200Response
     * @throws IOException if the JSON string is invalid with respect to StoreCheckStatusJsonGet200Response
     */
    public static StoreCheckStatusJsonGet200Response fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, StoreCheckStatusJsonGet200Response.class);
    }

    /**
     * Convert an instance of StoreCheckStatusJsonGet200Response to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

