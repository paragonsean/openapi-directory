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
import org.openapitools.client.model.FileDownloadLink;
import org.openapitools.client.model.PermalinkLink;
import org.openapitools.client.model.SelfLink;
import org.openapitools.client.model.SignedLinkLink;



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
public class FileLinksInner extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(FileLinksInner.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!FileLinksInner.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'FileLinksInner' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<SelfLink> adapterSelfLink = gson.getDelegateAdapter(this, TypeToken.get(SelfLink.class));
            final TypeAdapter<FileDownloadLink> adapterFileDownloadLink = gson.getDelegateAdapter(this, TypeToken.get(FileDownloadLink.class));
            final TypeAdapter<SignedLinkLink> adapterSignedLinkLink = gson.getDelegateAdapter(this, TypeToken.get(SignedLinkLink.class));
            final TypeAdapter<PermalinkLink> adapterPermalinkLink = gson.getDelegateAdapter(this, TypeToken.get(PermalinkLink.class));

            return (TypeAdapter<T>) new TypeAdapter<FileLinksInner>() {
                @Override
                public void write(JsonWriter out, FileLinksInner value) throws IOException {
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
                    // check if the actual instance is of the type `FileDownloadLink`
                    if (value.getActualInstance() instanceof FileDownloadLink) {
                        JsonElement element = adapterFileDownloadLink.toJsonTree((FileDownloadLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `SignedLinkLink`
                    if (value.getActualInstance() instanceof SignedLinkLink) {
                        JsonElement element = adapterSignedLinkLink.toJsonTree((SignedLinkLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `PermalinkLink`
                    if (value.getActualInstance() instanceof PermalinkLink) {
                        JsonElement element = adapterPermalinkLink.toJsonTree((PermalinkLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: FileDownloadLink, PermalinkLink, SelfLink, SignedLinkLink");
                }

                @Override
                public FileLinksInner read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize SelfLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        SelfLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterSelfLink;
                        FileLinksInner ret = new FileLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for SelfLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'SelfLink'", e);
                    }
                    // deserialize FileDownloadLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        FileDownloadLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterFileDownloadLink;
                        FileLinksInner ret = new FileLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for FileDownloadLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'FileDownloadLink'", e);
                    }
                    // deserialize SignedLinkLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        SignedLinkLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterSignedLinkLink;
                        FileLinksInner ret = new FileLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for SignedLinkLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'SignedLinkLink'", e);
                    }
                    // deserialize PermalinkLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        PermalinkLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterPermalinkLink;
                        FileLinksInner ret = new FileLinksInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for PermalinkLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'PermalinkLink'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for FileLinksInner: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public FileLinksInner() {
        super("anyOf", Boolean.FALSE);
    }

    public FileLinksInner(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("SelfLink", SelfLink.class);
        schemas.put("FileDownloadLink", FileDownloadLink.class);
        schemas.put("SignedLinkLink", SignedLinkLink.class);
        schemas.put("PermalinkLink", PermalinkLink.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return FileLinksInner.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * FileDownloadLink, PermalinkLink, SelfLink, SignedLinkLink
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof SelfLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof FileDownloadLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof SignedLinkLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof PermalinkLink) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be FileDownloadLink, PermalinkLink, SelfLink, SignedLinkLink");
    }

    /**
     * Get the actual instance, which can be the following:
     * FileDownloadLink, PermalinkLink, SelfLink, SignedLinkLink
     *
     * @return The actual instance (FileDownloadLink, PermalinkLink, SelfLink, SignedLinkLink)
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
     * Get the actual instance of `FileDownloadLink`. If the actual instance is not `FileDownloadLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `FileDownloadLink`
     * @throws ClassCastException if the instance is not `FileDownloadLink`
     */
    public FileDownloadLink getFileDownloadLink() throws ClassCastException {
        return (FileDownloadLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `SignedLinkLink`. If the actual instance is not `SignedLinkLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `SignedLinkLink`
     * @throws ClassCastException if the instance is not `SignedLinkLink`
     */
    public SignedLinkLink getSignedLinkLink() throws ClassCastException {
        return (SignedLinkLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `PermalinkLink`. If the actual instance is not `PermalinkLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `PermalinkLink`
     * @throws ClassCastException if the instance is not `PermalinkLink`
     */
    public PermalinkLink getPermalinkLink() throws ClassCastException {
        return (PermalinkLink)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to FileLinksInner
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
        // validate the json string with FileDownloadLink
        try {
            FileDownloadLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for FileDownloadLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with SignedLinkLink
        try {
            SignedLinkLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for SignedLinkLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with PermalinkLink
        try {
            PermalinkLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for PermalinkLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for FileLinksInner with anyOf schemas: FileDownloadLink, PermalinkLink, SelfLink, SignedLinkLink. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of FileLinksInner given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of FileLinksInner
     * @throws IOException if the JSON string is invalid with respect to FileLinksInner
     */
    public static FileLinksInner fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, FileLinksInner.class);
    }

    /**
     * Convert an instance of FileLinksInner to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

