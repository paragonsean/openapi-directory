/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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
import org.openapitools.client.model.MRSSGroupContent;
import org.openapitools.client.model.MRSSPeerLink;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideosForXMLInnerMediaGroupInner extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(VideosForXMLInnerMediaGroupInner.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!VideosForXMLInnerMediaGroupInner.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'VideosForXMLInnerMediaGroupInner' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<MRSSPeerLink> adapterMRSSPeerLink = gson.getDelegateAdapter(this, TypeToken.get(MRSSPeerLink.class));
            final TypeAdapter<MRSSGroupContent> adapterMRSSGroupContent = gson.getDelegateAdapter(this, TypeToken.get(MRSSGroupContent.class));

            return (TypeAdapter<T>) new TypeAdapter<VideosForXMLInnerMediaGroupInner>() {
                @Override
                public void write(JsonWriter out, VideosForXMLInnerMediaGroupInner value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `MRSSPeerLink`
                    if (value.getActualInstance() instanceof MRSSPeerLink) {
                        JsonElement element = adapterMRSSPeerLink.toJsonTree((MRSSPeerLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `MRSSGroupContent`
                    if (value.getActualInstance() instanceof MRSSGroupContent) {
                        JsonElement element = adapterMRSSGroupContent.toJsonTree((MRSSGroupContent)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: MRSSGroupContent, MRSSPeerLink");
                }

                @Override
                public VideosForXMLInnerMediaGroupInner read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize MRSSPeerLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        MRSSPeerLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterMRSSPeerLink;
                        VideosForXMLInnerMediaGroupInner ret = new VideosForXMLInnerMediaGroupInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for MRSSPeerLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'MRSSPeerLink'", e);
                    }
                    // deserialize MRSSGroupContent
                    try {
                        // validate the JSON object to see if any exception is thrown
                        MRSSGroupContent.validateJsonElement(jsonElement);
                        actualAdapter = adapterMRSSGroupContent;
                        VideosForXMLInnerMediaGroupInner ret = new VideosForXMLInnerMediaGroupInner();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for MRSSGroupContent failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'MRSSGroupContent'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for VideosForXMLInnerMediaGroupInner: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public VideosForXMLInnerMediaGroupInner() {
        super("anyOf", Boolean.FALSE);
    }

    public VideosForXMLInnerMediaGroupInner(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("MRSSPeerLink", MRSSPeerLink.class);
        schemas.put("MRSSGroupContent", MRSSGroupContent.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return VideosForXMLInnerMediaGroupInner.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * MRSSGroupContent, MRSSPeerLink
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof MRSSPeerLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof MRSSGroupContent) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be MRSSGroupContent, MRSSPeerLink");
    }

    /**
     * Get the actual instance, which can be the following:
     * MRSSGroupContent, MRSSPeerLink
     *
     * @return The actual instance (MRSSGroupContent, MRSSPeerLink)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `MRSSPeerLink`. If the actual instance is not `MRSSPeerLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `MRSSPeerLink`
     * @throws ClassCastException if the instance is not `MRSSPeerLink`
     */
    public MRSSPeerLink getMRSSPeerLink() throws ClassCastException {
        return (MRSSPeerLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `MRSSGroupContent`. If the actual instance is not `MRSSGroupContent`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `MRSSGroupContent`
     * @throws ClassCastException if the instance is not `MRSSGroupContent`
     */
    public MRSSGroupContent getMRSSGroupContent() throws ClassCastException {
        return (MRSSGroupContent)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to VideosForXMLInnerMediaGroupInner
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate anyOf schemas one by one
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with MRSSPeerLink
        try {
            MRSSPeerLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for MRSSPeerLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with MRSSGroupContent
        try {
            MRSSGroupContent.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for MRSSGroupContent failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for VideosForXMLInnerMediaGroupInner with anyOf schemas: MRSSGroupContent, MRSSPeerLink. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of VideosForXMLInnerMediaGroupInner given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of VideosForXMLInnerMediaGroupInner
     * @throws IOException if the JSON string is invalid with respect to VideosForXMLInnerMediaGroupInner
     */
    public static VideosForXMLInnerMediaGroupInner fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, VideosForXMLInnerMediaGroupInner.class);
    }

    /**
     * Convert an instance of VideosForXMLInnerMediaGroupInner to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

