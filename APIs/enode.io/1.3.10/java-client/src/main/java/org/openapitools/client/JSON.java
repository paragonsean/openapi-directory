/*
 * Enode API
 * Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.  > The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your `client_id` - Your `client_secret` - Authorization URL: `https://link.test.enode.io/oauth2/auth` - Token URL: `https://link.test.enode.io/oauth2/token`  ```javascript // Node.js + openid-client example const enodeIssuer = await Issuer.discover('https://link.test.enode.io'); const client = new enodeIssuer.Client({   client_id: 'xyz',   client_secret: 'shhhhh',   redirect_uris: ['http://localhost:5000/callback'],   response_types: ['code'], }); ```   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.  ```javascript // Node.js + openid-client example const clientAccessToken = await client.grant({grant_type: \"client_credentials\"}); ```  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: ``` POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \"forceLanguage\": \"nb-NO\",   \"vendor\": \"Tesla\", } ```  Example Response: ``` {     \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\", } ```  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of `linkState` from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.  ```javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl = client.authorizationUrl({   scope: \"offline_access all\",   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); ```   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  ```javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState = get(req, 'session.linkState');  // Parse relevant parameters from request URL const params = client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState}) ```  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: ``` https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request. ```   ## Errors when accessing a User's resources  When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: ``` HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \"type\": \"https://docs.enode.io/problems/payload-validation-error\",   \"title\": \"Payload validation failed\",   \"detail\": \"\\\"authorizationRequest.scope\\\" is required\", } ```  
 *
 * The version of the OpenAPI document: 1.3.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.internal.bind.util.ISO8601Utils;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonElement;
import io.gsonfire.GsonFireBuilder;
import io.gsonfire.TypeSelector;

import okio.ByteString;

import java.io.IOException;
import java.io.StringReader;
import java.lang.reflect.Type;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.ParsePosition;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.util.Map;
import java.util.HashMap;

/*
 * A JSON utility class
 *
 * NOTE: in the future, this class may be converted to static, which may break
 *       backward-compatibility
 */
public class JSON {
    private static Gson gson;
    private static boolean isLenientOnJson = false;
    private static DateTypeAdapter dateTypeAdapter = new DateTypeAdapter();
    private static SqlDateTypeAdapter sqlDateTypeAdapter = new SqlDateTypeAdapter();
    private static OffsetDateTimeTypeAdapter offsetDateTimeTypeAdapter = new OffsetDateTimeTypeAdapter();
    private static LocalDateTypeAdapter localDateTypeAdapter = new LocalDateTypeAdapter();
    private static ByteArrayAdapter byteArrayAdapter = new ByteArrayAdapter();

    @SuppressWarnings("unchecked")
    public static GsonBuilder createGson() {
        GsonFireBuilder fireBuilder = new GsonFireBuilder()
        ;
        GsonBuilder builder = fireBuilder.createGsonBuilder();
        return builder;
    }

    private static String getDiscriminatorValue(JsonElement readElement, String discriminatorField) {
        JsonElement element = readElement.getAsJsonObject().get(discriminatorField);
        if (null == element) {
            throw new IllegalArgumentException("missing discriminator field: <" + discriminatorField + ">");
        }
        return element.getAsString();
    }

    /**
     * Returns the Java class that implements the OpenAPI schema for the specified discriminator value.
     *
     * @param classByDiscriminatorValue The map of discriminator values to Java classes.
     * @param discriminatorValue The value of the OpenAPI discriminator in the input data.
     * @return The Java class that implements the OpenAPI schema
     */
    private static Class getClassByDiscriminator(Map classByDiscriminatorValue, String discriminatorValue) {
        Class clazz = (Class) classByDiscriminatorValue.get(discriminatorValue);
        if (null == clazz) {
            throw new IllegalArgumentException("cannot determine model class of name: <" + discriminatorValue + ">");
        }
        return clazz;
    }

    static {
        GsonBuilder gsonBuilder = createGson();
        gsonBuilder.registerTypeAdapter(Date.class, dateTypeAdapter);
        gsonBuilder.registerTypeAdapter(java.sql.Date.class, sqlDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(OffsetDateTime.class, offsetDateTimeTypeAdapter);
        gsonBuilder.registerTypeAdapter(LocalDate.class, localDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(byte[].class, byteArrayAdapter);
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ControlChargerChargingRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetCharger200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetCharger200ResponseChargeState.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetCharger200ResponseInformation.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetHealthVendors200ResponseInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetMe200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetMe200ResponseLinkedVendorsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetStatisticsCharging200ResponseInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetStatisticsCharging200ResponseInnerKw.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetStatisticsCharging200ResponseInnerPrice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetVehicleChargestate200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetVehiclesVehicleid200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetVehiclesVehicleidInformation200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetVehiclesVehicleidLocation200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetVehiclesVehicleidOdometer200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostCharginglocationsRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostUsersUseridLink200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostUsersUseridLinkRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostVehiclesVehicleidWatchRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutVehiclesVehicleidSmartchargingpolicyRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutWebhooksFirehoseRequest.CustomTypeAdapterFactory());
        gson = gsonBuilder.create();
    }

    /**
     * Get Gson.
     *
     * @return Gson
     */
    public static Gson getGson() {
        return gson;
    }

    /**
     * Set Gson.
     *
     * @param gson Gson
     */
    public static void setGson(Gson gson) {
        JSON.gson = gson;
    }

    public static void setLenientOnJson(boolean lenientOnJson) {
        isLenientOnJson = lenientOnJson;
    }

    /**
     * Serialize the given Java object into JSON string.
     *
     * @param obj Object
     * @return String representation of the JSON
     */
    public static String serialize(Object obj) {
        return gson.toJson(obj);
    }

    /**
     * Deserialize the given JSON string to Java object.
     *
     * @param <T>        Type
     * @param body       The JSON string
     * @param returnType The type to deserialize into
     * @return The deserialized Java object
     */
    @SuppressWarnings("unchecked")
    public static <T> T deserialize(String body, Type returnType) {
        try {
            if (isLenientOnJson) {
                JsonReader jsonReader = new JsonReader(new StringReader(body));
                // see https://google-gson.googlecode.com/svn/trunk/gson/docs/javadocs/com/google/gson/stream/JsonReader.html#setLenient(boolean)
                jsonReader.setLenient(true);
                return gson.fromJson(jsonReader, returnType);
            } else {
                return gson.fromJson(body, returnType);
            }
        } catch (JsonParseException e) {
            // Fallback processing when failed to parse JSON form response body:
            // return the response body string directly for the String return type;
            if (returnType.equals(String.class)) {
                return (T) body;
            } else {
                throw (e);
            }
        }
    }

    /**
     * Gson TypeAdapter for Byte Array type
     */
    public static class ByteArrayAdapter extends TypeAdapter<byte[]> {

        @Override
        public void write(JsonWriter out, byte[] value) throws IOException {
            if (value == null) {
                out.nullValue();
            } else {
                out.value(ByteString.of(value).base64());
            }
        }

        @Override
        public byte[] read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String bytesAsBase64 = in.nextString();
                    ByteString byteString = ByteString.decodeBase64(bytesAsBase64);
                    return byteString.toByteArray();
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 OffsetDateTime type
     */
    public static class OffsetDateTimeTypeAdapter extends TypeAdapter<OffsetDateTime> {

        private DateTimeFormatter formatter;

        public OffsetDateTimeTypeAdapter() {
            this(DateTimeFormatter.ISO_OFFSET_DATE_TIME);
        }

        public OffsetDateTimeTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, OffsetDateTime date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public OffsetDateTime read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    if (date.endsWith("+0000")) {
                        date = date.substring(0, date.length()-5) + "Z";
                    }
                    return OffsetDateTime.parse(date, formatter);
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 LocalDate type
     */
    public static class LocalDateTypeAdapter extends TypeAdapter<LocalDate> {

        private DateTimeFormatter formatter;

        public LocalDateTypeAdapter() {
            this(DateTimeFormatter.ISO_LOCAL_DATE);
        }

        public LocalDateTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, LocalDate date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public LocalDate read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    return LocalDate.parse(date, formatter);
            }
        }
    }

    public static void setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        offsetDateTimeTypeAdapter.setFormat(dateFormat);
    }

    public static void setLocalDateFormat(DateTimeFormatter dateFormat) {
        localDateTypeAdapter.setFormat(dateFormat);
    }

    /**
     * Gson TypeAdapter for java.sql.Date type
     * If the dateFormat is null, a simple "yyyy-MM-dd" format will be used
     * (more efficient than SimpleDateFormat).
     */
    public static class SqlDateTypeAdapter extends TypeAdapter<java.sql.Date> {

        private DateFormat dateFormat;

        public SqlDateTypeAdapter() {}

        public SqlDateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, java.sql.Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = date.toString();
                }
                out.value(value);
            }
        }

        @Override
        public java.sql.Date read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    try {
                        if (dateFormat != null) {
                            return new java.sql.Date(dateFormat.parse(date).getTime());
                        }
                        return new java.sql.Date(ISO8601Utils.parse(date, new ParsePosition(0)).getTime());
                    } catch (ParseException e) {
                        throw new JsonParseException(e);
                    }
            }
        }
    }

    /**
     * Gson TypeAdapter for java.util.Date type
     * If the dateFormat is null, ISO8601Utils will be used.
     */
    public static class DateTypeAdapter extends TypeAdapter<Date> {

        private DateFormat dateFormat;

        public DateTypeAdapter() {}

        public DateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = ISO8601Utils.format(date, true);
                }
                out.value(value);
            }
        }

        @Override
        public Date read(JsonReader in) throws IOException {
            try {
                switch (in.peek()) {
                    case NULL:
                        in.nextNull();
                        return null;
                    default:
                        String date = in.nextString();
                        try {
                            if (dateFormat != null) {
                                return dateFormat.parse(date);
                            }
                            return ISO8601Utils.parse(date, new ParsePosition(0));
                        } catch (ParseException e) {
                            throw new JsonParseException(e);
                        }
                }
            } catch (IllegalArgumentException e) {
                throw new JsonParseException(e);
            }
        }
    }

    public static void setDateFormat(DateFormat dateFormat) {
        dateTypeAdapter.setFormat(dateFormat);
    }

    public static void setSqlDateFormat(DateFormat dateFormat) {
        sqlDateTypeAdapter.setFormat(dateFormat);
    }
}
