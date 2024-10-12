/*
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.VideogameCSGO;
import org.openapitools.client.model.VideogameCodmw;
import org.openapitools.client.model.VideogameDota2;
import org.openapitools.client.model.VideogameFifa;
import org.openapitools.client.model.VideogameLeague;
import org.openapitools.client.model.VideogameLoL;
import org.openapitools.client.model.VideogameOverwatch;
import org.openapitools.client.model.VideogamePUBG;
import org.openapitools.client.model.VideogameR6siege;
import org.openapitools.client.model.VideogameRocketLeague;
import org.openapitools.client.model.VideogameValorant;



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

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Videogame extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(Videogame.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!Videogame.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'Videogame' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<VideogameLoL> adapterVideogameLoL = gson.getDelegateAdapter(this, TypeToken.get(VideogameLoL.class));
            final TypeAdapter<VideogameCSGO> adapterVideogameCSGO = gson.getDelegateAdapter(this, TypeToken.get(VideogameCSGO.class));
            final TypeAdapter<VideogameDota2> adapterVideogameDota2 = gson.getDelegateAdapter(this, TypeToken.get(VideogameDota2.class));
            final TypeAdapter<VideogameOverwatch> adapterVideogameOverwatch = gson.getDelegateAdapter(this, TypeToken.get(VideogameOverwatch.class));
            final TypeAdapter<VideogamePUBG> adapterVideogamePUBG = gson.getDelegateAdapter(this, TypeToken.get(VideogamePUBG.class));
            final TypeAdapter<VideogameRocketLeague> adapterVideogameRocketLeague = gson.getDelegateAdapter(this, TypeToken.get(VideogameRocketLeague.class));
            final TypeAdapter<VideogameCodmw> adapterVideogameCodmw = gson.getDelegateAdapter(this, TypeToken.get(VideogameCodmw.class));
            final TypeAdapter<VideogameR6siege> adapterVideogameR6siege = gson.getDelegateAdapter(this, TypeToken.get(VideogameR6siege.class));
            final TypeAdapter<VideogameFifa> adapterVideogameFifa = gson.getDelegateAdapter(this, TypeToken.get(VideogameFifa.class));
            final TypeAdapter<VideogameValorant> adapterVideogameValorant = gson.getDelegateAdapter(this, TypeToken.get(VideogameValorant.class));

            return (TypeAdapter<T>) new TypeAdapter<Videogame>() {
                @Override
                public void write(JsonWriter out, Videogame value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `VideogameLoL`
                    if (value.getActualInstance() instanceof VideogameLoL) {
                        JsonElement element = adapterVideogameLoL.toJsonTree((VideogameLoL)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameCSGO`
                    if (value.getActualInstance() instanceof VideogameCSGO) {
                        JsonElement element = adapterVideogameCSGO.toJsonTree((VideogameCSGO)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameDota2`
                    if (value.getActualInstance() instanceof VideogameDota2) {
                        JsonElement element = adapterVideogameDota2.toJsonTree((VideogameDota2)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameOverwatch`
                    if (value.getActualInstance() instanceof VideogameOverwatch) {
                        JsonElement element = adapterVideogameOverwatch.toJsonTree((VideogameOverwatch)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogamePUBG`
                    if (value.getActualInstance() instanceof VideogamePUBG) {
                        JsonElement element = adapterVideogamePUBG.toJsonTree((VideogamePUBG)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameRocketLeague`
                    if (value.getActualInstance() instanceof VideogameRocketLeague) {
                        JsonElement element = adapterVideogameRocketLeague.toJsonTree((VideogameRocketLeague)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameCodmw`
                    if (value.getActualInstance() instanceof VideogameCodmw) {
                        JsonElement element = adapterVideogameCodmw.toJsonTree((VideogameCodmw)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameR6siege`
                    if (value.getActualInstance() instanceof VideogameR6siege) {
                        JsonElement element = adapterVideogameR6siege.toJsonTree((VideogameR6siege)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameFifa`
                    if (value.getActualInstance() instanceof VideogameFifa) {
                        JsonElement element = adapterVideogameFifa.toJsonTree((VideogameFifa)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `VideogameValorant`
                    if (value.getActualInstance() instanceof VideogameValorant) {
                        JsonElement element = adapterVideogameValorant.toJsonTree((VideogameValorant)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant");
                }

                @Override
                public Videogame read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize VideogameLoL
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameLoL.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameLoL;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameLoL'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameLoL failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameLoL'", e);
                    }
                    // deserialize VideogameCSGO
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameCSGO.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameCSGO;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameCSGO'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameCSGO failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameCSGO'", e);
                    }
                    // deserialize VideogameDota2
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameDota2.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameDota2;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameDota2'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameDota2 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameDota2'", e);
                    }
                    // deserialize VideogameOverwatch
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameOverwatch.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameOverwatch;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameOverwatch'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameOverwatch failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameOverwatch'", e);
                    }
                    // deserialize VideogamePUBG
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogamePUBG.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogamePUBG;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogamePUBG'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogamePUBG failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogamePUBG'", e);
                    }
                    // deserialize VideogameRocketLeague
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameRocketLeague.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameRocketLeague;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameRocketLeague'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameRocketLeague failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameRocketLeague'", e);
                    }
                    // deserialize VideogameCodmw
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameCodmw.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameCodmw;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameCodmw'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameCodmw failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameCodmw'", e);
                    }
                    // deserialize VideogameR6siege
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameR6siege.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameR6siege;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameR6siege'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameR6siege failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameR6siege'", e);
                    }
                    // deserialize VideogameFifa
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameFifa.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameFifa;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameFifa'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameFifa failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameFifa'", e);
                    }
                    // deserialize VideogameValorant
                    try {
                        // validate the JSON object to see if any exception is thrown
                        VideogameValorant.validateJsonElement(jsonElement);
                        actualAdapter = adapterVideogameValorant;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'VideogameValorant'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for VideogameValorant failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'VideogameValorant'", e);
                    }

                    if (match == 1) {
                        Videogame ret = new Videogame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for Videogame: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public Videogame() {
        super("oneOf", Boolean.FALSE);
    }

    public Videogame(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("VideogameLoL", VideogameLoL.class);
        schemas.put("VideogameCSGO", VideogameCSGO.class);
        schemas.put("VideogameDota2", VideogameDota2.class);
        schemas.put("VideogameOverwatch", VideogameOverwatch.class);
        schemas.put("VideogamePUBG", VideogamePUBG.class);
        schemas.put("VideogameRocketLeague", VideogameRocketLeague.class);
        schemas.put("VideogameCodmw", VideogameCodmw.class);
        schemas.put("VideogameR6siege", VideogameR6siege.class);
        schemas.put("VideogameFifa", VideogameFifa.class);
        schemas.put("VideogameValorant", VideogameValorant.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return Videogame.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof VideogameLoL) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameCSGO) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameDota2) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameOverwatch) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogamePUBG) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameRocketLeague) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameCodmw) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameR6siege) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameFifa) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof VideogameValorant) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant");
    }

    /**
     * Get the actual instance, which can be the following:
     * VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant
     *
     * @return The actual instance (VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `VideogameLoL`. If the actual instance is not `VideogameLoL`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameLoL`
     * @throws ClassCastException if the instance is not `VideogameLoL`
     */
    public VideogameLoL getVideogameLoL() throws ClassCastException {
        return (VideogameLoL)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameCSGO`. If the actual instance is not `VideogameCSGO`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameCSGO`
     * @throws ClassCastException if the instance is not `VideogameCSGO`
     */
    public VideogameCSGO getVideogameCSGO() throws ClassCastException {
        return (VideogameCSGO)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameDota2`. If the actual instance is not `VideogameDota2`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameDota2`
     * @throws ClassCastException if the instance is not `VideogameDota2`
     */
    public VideogameDota2 getVideogameDota2() throws ClassCastException {
        return (VideogameDota2)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameOverwatch`. If the actual instance is not `VideogameOverwatch`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameOverwatch`
     * @throws ClassCastException if the instance is not `VideogameOverwatch`
     */
    public VideogameOverwatch getVideogameOverwatch() throws ClassCastException {
        return (VideogameOverwatch)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogamePUBG`. If the actual instance is not `VideogamePUBG`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogamePUBG`
     * @throws ClassCastException if the instance is not `VideogamePUBG`
     */
    public VideogamePUBG getVideogamePUBG() throws ClassCastException {
        return (VideogamePUBG)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameRocketLeague`. If the actual instance is not `VideogameRocketLeague`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameRocketLeague`
     * @throws ClassCastException if the instance is not `VideogameRocketLeague`
     */
    public VideogameRocketLeague getVideogameRocketLeague() throws ClassCastException {
        return (VideogameRocketLeague)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameCodmw`. If the actual instance is not `VideogameCodmw`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameCodmw`
     * @throws ClassCastException if the instance is not `VideogameCodmw`
     */
    public VideogameCodmw getVideogameCodmw() throws ClassCastException {
        return (VideogameCodmw)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameR6siege`. If the actual instance is not `VideogameR6siege`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameR6siege`
     * @throws ClassCastException if the instance is not `VideogameR6siege`
     */
    public VideogameR6siege getVideogameR6siege() throws ClassCastException {
        return (VideogameR6siege)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameFifa`. If the actual instance is not `VideogameFifa`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameFifa`
     * @throws ClassCastException if the instance is not `VideogameFifa`
     */
    public VideogameFifa getVideogameFifa() throws ClassCastException {
        return (VideogameFifa)super.getActualInstance();
    }
    /**
     * Get the actual instance of `VideogameValorant`. If the actual instance is not `VideogameValorant`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `VideogameValorant`
     * @throws ClassCastException if the instance is not `VideogameValorant`
     */
    public VideogameValorant getVideogameValorant() throws ClassCastException {
        return (VideogameValorant)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to Videogame
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with VideogameLoL
        try {
            VideogameLoL.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameLoL failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameCSGO
        try {
            VideogameCSGO.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameCSGO failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameDota2
        try {
            VideogameDota2.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameDota2 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameOverwatch
        try {
            VideogameOverwatch.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameOverwatch failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogamePUBG
        try {
            VideogamePUBG.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogamePUBG failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameRocketLeague
        try {
            VideogameRocketLeague.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameRocketLeague failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameCodmw
        try {
            VideogameCodmw.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameCodmw failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameR6siege
        try {
            VideogameR6siege.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameR6siege failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameFifa
        try {
            VideogameFifa.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameFifa failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with VideogameValorant
        try {
            VideogameValorant.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for VideogameValorant failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for Videogame with oneOf schemas: VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of Videogame given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of Videogame
     * @throws IOException if the JSON string is invalid with respect to Videogame
     */
    public static Videogame fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, Videogame.class);
    }

    /**
     * Convert an instance of Videogame to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

