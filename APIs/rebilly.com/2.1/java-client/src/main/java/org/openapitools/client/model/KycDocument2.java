/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CommonKycDocumentLinksInner;
import org.openapitools.client.model.KycDocumentRejection;
import org.openapitools.client.model.KycDocumentSubtypes;
import org.openapitools.client.model.KycDocumentTypes;
import org.openapitools.client.model.ProofOfAddress;
import org.openapitools.client.model.ProofOfAddressAllOfDocumentMatches;
import org.openapitools.client.model.ProofOfFunds;
import org.openapitools.client.model.ProofOfIdentity;
import org.openapitools.client.model.ProofOfPurchase;
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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class KycDocument2 extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(KycDocument2.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!KycDocument2.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'KycDocument2' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<ProofOfIdentity> adapterProofOfIdentity = gson.getDelegateAdapter(this, TypeToken.get(ProofOfIdentity.class));
            final TypeAdapter<ProofOfAddress> adapterProofOfAddress = gson.getDelegateAdapter(this, TypeToken.get(ProofOfAddress.class));
            final TypeAdapter<ProofOfFunds> adapterProofOfFunds = gson.getDelegateAdapter(this, TypeToken.get(ProofOfFunds.class));
            final TypeAdapter<ProofOfPurchase> adapterProofOfPurchase = gson.getDelegateAdapter(this, TypeToken.get(ProofOfPurchase.class));

            return (TypeAdapter<T>) new TypeAdapter<KycDocument2>() {
                @Override
                public void write(JsonWriter out, KycDocument2 value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `ProofOfIdentity`
                    if (value.getActualInstance() instanceof ProofOfIdentity) {
                        JsonElement element = adapterProofOfIdentity.toJsonTree((ProofOfIdentity)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ProofOfAddress`
                    if (value.getActualInstance() instanceof ProofOfAddress) {
                        JsonElement element = adapterProofOfAddress.toJsonTree((ProofOfAddress)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ProofOfFunds`
                    if (value.getActualInstance() instanceof ProofOfFunds) {
                        JsonElement element = adapterProofOfFunds.toJsonTree((ProofOfFunds)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ProofOfPurchase`
                    if (value.getActualInstance() instanceof ProofOfPurchase) {
                        JsonElement element = adapterProofOfPurchase.toJsonTree((ProofOfPurchase)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: ProofOfAddress, ProofOfFunds, ProofOfIdentity, ProofOfPurchase");
                }

                @Override
                public KycDocument2 read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize ProofOfIdentity
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ProofOfIdentity.validateJsonElement(jsonElement);
                        actualAdapter = adapterProofOfIdentity;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'ProofOfIdentity'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ProofOfIdentity failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ProofOfIdentity'", e);
                    }
                    // deserialize ProofOfAddress
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ProofOfAddress.validateJsonElement(jsonElement);
                        actualAdapter = adapterProofOfAddress;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'ProofOfAddress'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ProofOfAddress failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ProofOfAddress'", e);
                    }
                    // deserialize ProofOfFunds
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ProofOfFunds.validateJsonElement(jsonElement);
                        actualAdapter = adapterProofOfFunds;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'ProofOfFunds'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ProofOfFunds failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ProofOfFunds'", e);
                    }
                    // deserialize ProofOfPurchase
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ProofOfPurchase.validateJsonElement(jsonElement);
                        actualAdapter = adapterProofOfPurchase;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'ProofOfPurchase'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ProofOfPurchase failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ProofOfPurchase'", e);
                    }

                    if (match == 1) {
                        KycDocument2 ret = new KycDocument2();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for KycDocument2: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public KycDocument2() {
        super("oneOf", Boolean.FALSE);
    }

    public KycDocument2(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("ProofOfIdentity", ProofOfIdentity.class);
        schemas.put("ProofOfAddress", ProofOfAddress.class);
        schemas.put("ProofOfFunds", ProofOfFunds.class);
        schemas.put("ProofOfPurchase", ProofOfPurchase.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return KycDocument2.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * ProofOfAddress, ProofOfFunds, ProofOfIdentity, ProofOfPurchase
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof ProofOfIdentity) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ProofOfAddress) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ProofOfFunds) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ProofOfPurchase) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be ProofOfAddress, ProofOfFunds, ProofOfIdentity, ProofOfPurchase");
    }

    /**
     * Get the actual instance, which can be the following:
     * ProofOfAddress, ProofOfFunds, ProofOfIdentity, ProofOfPurchase
     *
     * @return The actual instance (ProofOfAddress, ProofOfFunds, ProofOfIdentity, ProofOfPurchase)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `ProofOfIdentity`. If the actual instance is not `ProofOfIdentity`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ProofOfIdentity`
     * @throws ClassCastException if the instance is not `ProofOfIdentity`
     */
    public ProofOfIdentity getProofOfIdentity() throws ClassCastException {
        return (ProofOfIdentity)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ProofOfAddress`. If the actual instance is not `ProofOfAddress`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ProofOfAddress`
     * @throws ClassCastException if the instance is not `ProofOfAddress`
     */
    public ProofOfAddress getProofOfAddress() throws ClassCastException {
        return (ProofOfAddress)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ProofOfFunds`. If the actual instance is not `ProofOfFunds`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ProofOfFunds`
     * @throws ClassCastException if the instance is not `ProofOfFunds`
     */
    public ProofOfFunds getProofOfFunds() throws ClassCastException {
        return (ProofOfFunds)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ProofOfPurchase`. If the actual instance is not `ProofOfPurchase`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ProofOfPurchase`
     * @throws ClassCastException if the instance is not `ProofOfPurchase`
     */
    public ProofOfPurchase getProofOfPurchase() throws ClassCastException {
        return (ProofOfPurchase)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to KycDocument2
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with ProofOfIdentity
        try {
            ProofOfIdentity.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ProofOfIdentity failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ProofOfAddress
        try {
            ProofOfAddress.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ProofOfAddress failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ProofOfFunds
        try {
            ProofOfFunds.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ProofOfFunds failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ProofOfPurchase
        try {
            ProofOfPurchase.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ProofOfPurchase failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for KycDocument2 with oneOf schemas: ProofOfAddress, ProofOfFunds, ProofOfIdentity, ProofOfPurchase. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of KycDocument2 given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of KycDocument2
     * @throws IOException if the JSON string is invalid with respect to KycDocument2
     */
    public static KycDocument2 fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, KycDocument2.class);
    }

    /**
     * Convert an instance of KycDocument2 to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

