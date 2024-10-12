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
import java.util.Arrays;
import org.openapitools.client.model.DynamicIpnLink;
import org.openapitools.client.model.OnBoardingUrlLink;
import org.openapitools.client.model.SelfLink;
import org.openapitools.client.model.StaticIpnLink;



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
public class GatewayAccountLinksInner extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(GatewayAccountLinksInner.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!GatewayAccountLinksInner.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'GatewayAccountLinksInner' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<SelfLink> adapterSelfLink = gson.getDelegateAdapter(this, TypeToken.get(SelfLink.class));
            final TypeAdapter<OnBoardingUrlLink> adapterOnBoardingUrlLink = gson.getDelegateAdapter(this, TypeToken.get(OnBoardingUrlLink.class));
            final TypeAdapter<DynamicIpnLink> adapterDynamicIpnLink = gson.getDelegateAdapter(this, TypeToken.get(DynamicIpnLink.class));
            final TypeAdapter<StaticIpnLink> adapterStaticIpnLink = gson.getDelegateAdapter(this, TypeToken.get(StaticIpnLink.class));

            return (TypeAdapter<T>) new TypeAdapter<GatewayAccountLinksInner>() {
                @Override
                public void write(JsonWriter out, GatewayAccountLinksInner value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `SelfLink`
                    if (value.getActualInstance() instanceof SelfLink) {
                        JsonElement element = adapterSelfLink.toJsonTree((SelfLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `OnBoardingUrlLink`
                    if (value.getActualInstance() instanceof OnBoardingUrlLink) {
                        JsonElement element = adapterOnBoardingUrlLink.toJsonTree((OnBoardingUrlLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `DynamicIpnLink`
                    if (value.getActualInstance() instanceof DynamicIpnLink) {
                        JsonElement element = adapterDynamicIpnLink.toJsonTree((DynamicIpnLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `StaticIpnLink`
                    if (value.getActualInstance() instanceof StaticIpnLink) {
                        JsonElement element = adapterStaticIpnLink.toJsonTree((StaticIpnLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: DynamicIpnLink, OnBoardingUrlLink, SelfLink, StaticIpnLink");
                }

                @Override
                public GatewayAccountLinksInner read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize SelfLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        SelfLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterSelfLink;
                        GatewayAccountLinksInner ret = new GatewayAccountLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for SelfLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'SelfLink'", e);
                    }
                    // deserialize OnBoardingUrlLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        OnBoardingUrlLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterOnBoardingUrlLink;
                        GatewayAccountLinksInner ret = new GatewayAccountLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for OnBoardingUrlLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'OnBoardingUrlLink'", e);
                    }
                    // deserialize DynamicIpnLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        DynamicIpnLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterDynamicIpnLink;
                        GatewayAccountLinksInner ret = new GatewayAccountLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for DynamicIpnLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'DynamicIpnLink'", e);
                    }
                    // deserialize StaticIpnLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        StaticIpnLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterStaticIpnLink;
                        GatewayAccountLinksInner ret = new GatewayAccountLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for StaticIpnLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'StaticIpnLink'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for GatewayAccountLinksInner: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public GatewayAccountLinksInner() {
        super("anyOf", Boolean.FALSE);
    }

    public GatewayAccountLinksInner(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("SelfLink", SelfLink.class);
        schemas.put("OnBoardingUrlLink", OnBoardingUrlLink.class);
        schemas.put("DynamicIpnLink", DynamicIpnLink.class);
        schemas.put("StaticIpnLink", StaticIpnLink.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return GatewayAccountLinksInner.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * DynamicIpnLink, OnBoardingUrlLink, SelfLink, StaticIpnLink
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof SelfLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof OnBoardingUrlLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof DynamicIpnLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof StaticIpnLink) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be DynamicIpnLink, OnBoardingUrlLink, SelfLink, StaticIpnLink");
    }

    /**
     * Get the actual instance, which can be the following:
     * DynamicIpnLink, OnBoardingUrlLink, SelfLink, StaticIpnLink
     *
     * @return The actual instance (DynamicIpnLink, OnBoardingUrlLink, SelfLink, StaticIpnLink)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `SelfLink`. If the actual instance is not `SelfLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `SelfLink`
     * @throws ClassCastException if the instance is not `SelfLink`
     */
    public SelfLink getSelfLink() throws ClassCastException {
        return (SelfLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `OnBoardingUrlLink`. If the actual instance is not `OnBoardingUrlLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `OnBoardingUrlLink`
     * @throws ClassCastException if the instance is not `OnBoardingUrlLink`
     */
    public OnBoardingUrlLink getOnBoardingUrlLink() throws ClassCastException {
        return (OnBoardingUrlLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `DynamicIpnLink`. If the actual instance is not `DynamicIpnLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `DynamicIpnLink`
     * @throws ClassCastException if the instance is not `DynamicIpnLink`
     */
    public DynamicIpnLink getDynamicIpnLink() throws ClassCastException {
        return (DynamicIpnLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `StaticIpnLink`. If the actual instance is not `StaticIpnLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `StaticIpnLink`
     * @throws ClassCastException if the instance is not `StaticIpnLink`
     */
    public StaticIpnLink getStaticIpnLink() throws ClassCastException {
        return (StaticIpnLink)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to GatewayAccountLinksInner
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate anyOf schemas one by one
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with SelfLink
        try {
            SelfLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for SelfLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with OnBoardingUrlLink
        try {
            OnBoardingUrlLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for OnBoardingUrlLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with DynamicIpnLink
        try {
            DynamicIpnLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for DynamicIpnLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with StaticIpnLink
        try {
            StaticIpnLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for StaticIpnLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for GatewayAccountLinksInner with anyOf schemas: DynamicIpnLink, OnBoardingUrlLink, SelfLink, StaticIpnLink. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of GatewayAccountLinksInner given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of GatewayAccountLinksInner
     * @throws IOException if the JSON string is invalid with respect to GatewayAccountLinksInner
     */
    public static GatewayAccountLinksInner fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, GatewayAccountLinksInner.class);
    }

    /**
     * Convert an instance of GatewayAccountLinksInner to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

