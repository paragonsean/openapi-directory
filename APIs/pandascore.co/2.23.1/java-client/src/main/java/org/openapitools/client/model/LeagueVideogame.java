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
import java.util.Arrays;
import org.openapitools.client.model.LeagueVideogameCSGO;
import org.openapitools.client.model.LeagueVideogameCodmw;
import org.openapitools.client.model.LeagueVideogameDota2;
import org.openapitools.client.model.LeagueVideogameFifa;
import org.openapitools.client.model.LeagueVideogameLoL;
import org.openapitools.client.model.LeagueVideogameOverwatch;
import org.openapitools.client.model.LeagueVideogamePUBG;
import org.openapitools.client.model.LeagueVideogameR6siege;
import org.openapitools.client.model.LeagueVideogameRocketLeague;
import org.openapitools.client.model.LeagueVideogameValorant;



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
public class LeagueVideogame extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(LeagueVideogame.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!LeagueVideogame.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'LeagueVideogame' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<LeagueVideogameLoL> adapterLeagueVideogameLoL = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameLoL.class));
            final TypeAdapter<LeagueVideogameCSGO> adapterLeagueVideogameCSGO = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameCSGO.class));
            final TypeAdapter<LeagueVideogameDota2> adapterLeagueVideogameDota2 = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameDota2.class));
            final TypeAdapter<LeagueVideogameOverwatch> adapterLeagueVideogameOverwatch = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameOverwatch.class));
            final TypeAdapter<LeagueVideogamePUBG> adapterLeagueVideogamePUBG = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogamePUBG.class));
            final TypeAdapter<LeagueVideogameRocketLeague> adapterLeagueVideogameRocketLeague = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameRocketLeague.class));
            final TypeAdapter<LeagueVideogameCodmw> adapterLeagueVideogameCodmw = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameCodmw.class));
            final TypeAdapter<LeagueVideogameR6siege> adapterLeagueVideogameR6siege = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameR6siege.class));
            final TypeAdapter<LeagueVideogameFifa> adapterLeagueVideogameFifa = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameFifa.class));
            final TypeAdapter<LeagueVideogameValorant> adapterLeagueVideogameValorant = gson.getDelegateAdapter(this, TypeToken.get(LeagueVideogameValorant.class));

            return (TypeAdapter<T>) new TypeAdapter<LeagueVideogame>() {
                @Override
                public void write(JsonWriter out, LeagueVideogame value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `LeagueVideogameLoL`
                    if (value.getActualInstance() instanceof LeagueVideogameLoL) {
                        JsonElement element = adapterLeagueVideogameLoL.toJsonTree((LeagueVideogameLoL)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameCSGO`
                    if (value.getActualInstance() instanceof LeagueVideogameCSGO) {
                        JsonElement element = adapterLeagueVideogameCSGO.toJsonTree((LeagueVideogameCSGO)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameDota2`
                    if (value.getActualInstance() instanceof LeagueVideogameDota2) {
                        JsonElement element = adapterLeagueVideogameDota2.toJsonTree((LeagueVideogameDota2)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameOverwatch`
                    if (value.getActualInstance() instanceof LeagueVideogameOverwatch) {
                        JsonElement element = adapterLeagueVideogameOverwatch.toJsonTree((LeagueVideogameOverwatch)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogamePUBG`
                    if (value.getActualInstance() instanceof LeagueVideogamePUBG) {
                        JsonElement element = adapterLeagueVideogamePUBG.toJsonTree((LeagueVideogamePUBG)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameRocketLeague`
                    if (value.getActualInstance() instanceof LeagueVideogameRocketLeague) {
                        JsonElement element = adapterLeagueVideogameRocketLeague.toJsonTree((LeagueVideogameRocketLeague)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameCodmw`
                    if (value.getActualInstance() instanceof LeagueVideogameCodmw) {
                        JsonElement element = adapterLeagueVideogameCodmw.toJsonTree((LeagueVideogameCodmw)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameR6siege`
                    if (value.getActualInstance() instanceof LeagueVideogameR6siege) {
                        JsonElement element = adapterLeagueVideogameR6siege.toJsonTree((LeagueVideogameR6siege)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameFifa`
                    if (value.getActualInstance() instanceof LeagueVideogameFifa) {
                        JsonElement element = adapterLeagueVideogameFifa.toJsonTree((LeagueVideogameFifa)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeagueVideogameValorant`
                    if (value.getActualInstance() instanceof LeagueVideogameValorant) {
                        JsonElement element = adapterLeagueVideogameValorant.toJsonTree((LeagueVideogameValorant)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: LeagueVideogameCSGO, LeagueVideogameCodmw, LeagueVideogameDota2, LeagueVideogameFifa, LeagueVideogameLoL, LeagueVideogameOverwatch, LeagueVideogamePUBG, LeagueVideogameR6siege, LeagueVideogameRocketLeague, LeagueVideogameValorant");
                }

                @Override
                public LeagueVideogame read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize LeagueVideogameLoL
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameLoL.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameLoL;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameLoL'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameLoL failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameLoL'", e);
                    }
                    // deserialize LeagueVideogameCSGO
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameCSGO.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameCSGO;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameCSGO'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameCSGO failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameCSGO'", e);
                    }
                    // deserialize LeagueVideogameDota2
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameDota2.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameDota2;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameDota2'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameDota2 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameDota2'", e);
                    }
                    // deserialize LeagueVideogameOverwatch
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameOverwatch.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameOverwatch;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameOverwatch'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameOverwatch failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameOverwatch'", e);
                    }
                    // deserialize LeagueVideogamePUBG
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogamePUBG.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogamePUBG;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogamePUBG'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogamePUBG failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogamePUBG'", e);
                    }
                    // deserialize LeagueVideogameRocketLeague
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameRocketLeague.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameRocketLeague;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameRocketLeague'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameRocketLeague failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameRocketLeague'", e);
                    }
                    // deserialize LeagueVideogameCodmw
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameCodmw.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameCodmw;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameCodmw'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameCodmw failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameCodmw'", e);
                    }
                    // deserialize LeagueVideogameR6siege
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameR6siege.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameR6siege;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameR6siege'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameR6siege failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameR6siege'", e);
                    }
                    // deserialize LeagueVideogameFifa
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameFifa.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameFifa;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameFifa'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameFifa failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameFifa'", e);
                    }
                    // deserialize LeagueVideogameValorant
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeagueVideogameValorant.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeagueVideogameValorant;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'LeagueVideogameValorant'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeagueVideogameValorant failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeagueVideogameValorant'", e);
                    }

                    if (match == 1) {
                        LeagueVideogame ret = new LeagueVideogame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for LeagueVideogame: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public LeagueVideogame() {
        super("oneOf", Boolean.FALSE);
    }

    public LeagueVideogame(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("LeagueVideogameLoL", LeagueVideogameLoL.class);
        schemas.put("LeagueVideogameCSGO", LeagueVideogameCSGO.class);
        schemas.put("LeagueVideogameDota2", LeagueVideogameDota2.class);
        schemas.put("LeagueVideogameOverwatch", LeagueVideogameOverwatch.class);
        schemas.put("LeagueVideogamePUBG", LeagueVideogamePUBG.class);
        schemas.put("LeagueVideogameRocketLeague", LeagueVideogameRocketLeague.class);
        schemas.put("LeagueVideogameCodmw", LeagueVideogameCodmw.class);
        schemas.put("LeagueVideogameR6siege", LeagueVideogameR6siege.class);
        schemas.put("LeagueVideogameFifa", LeagueVideogameFifa.class);
        schemas.put("LeagueVideogameValorant", LeagueVideogameValorant.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return LeagueVideogame.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * LeagueVideogameCSGO, LeagueVideogameCodmw, LeagueVideogameDota2, LeagueVideogameFifa, LeagueVideogameLoL, LeagueVideogameOverwatch, LeagueVideogamePUBG, LeagueVideogameR6siege, LeagueVideogameRocketLeague, LeagueVideogameValorant
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof LeagueVideogameLoL) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameCSGO) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameDota2) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameOverwatch) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogamePUBG) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameRocketLeague) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameCodmw) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameR6siege) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameFifa) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeagueVideogameValorant) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be LeagueVideogameCSGO, LeagueVideogameCodmw, LeagueVideogameDota2, LeagueVideogameFifa, LeagueVideogameLoL, LeagueVideogameOverwatch, LeagueVideogamePUBG, LeagueVideogameR6siege, LeagueVideogameRocketLeague, LeagueVideogameValorant");
    }

    /**
     * Get the actual instance, which can be the following:
     * LeagueVideogameCSGO, LeagueVideogameCodmw, LeagueVideogameDota2, LeagueVideogameFifa, LeagueVideogameLoL, LeagueVideogameOverwatch, LeagueVideogamePUBG, LeagueVideogameR6siege, LeagueVideogameRocketLeague, LeagueVideogameValorant
     *
     * @return The actual instance (LeagueVideogameCSGO, LeagueVideogameCodmw, LeagueVideogameDota2, LeagueVideogameFifa, LeagueVideogameLoL, LeagueVideogameOverwatch, LeagueVideogamePUBG, LeagueVideogameR6siege, LeagueVideogameRocketLeague, LeagueVideogameValorant)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `LeagueVideogameLoL`. If the actual instance is not `LeagueVideogameLoL`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameLoL`
     * @throws ClassCastException if the instance is not `LeagueVideogameLoL`
     */
    public LeagueVideogameLoL getLeagueVideogameLoL() throws ClassCastException {
        return (LeagueVideogameLoL)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameCSGO`. If the actual instance is not `LeagueVideogameCSGO`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameCSGO`
     * @throws ClassCastException if the instance is not `LeagueVideogameCSGO`
     */
    public LeagueVideogameCSGO getLeagueVideogameCSGO() throws ClassCastException {
        return (LeagueVideogameCSGO)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameDota2`. If the actual instance is not `LeagueVideogameDota2`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameDota2`
     * @throws ClassCastException if the instance is not `LeagueVideogameDota2`
     */
    public LeagueVideogameDota2 getLeagueVideogameDota2() throws ClassCastException {
        return (LeagueVideogameDota2)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameOverwatch`. If the actual instance is not `LeagueVideogameOverwatch`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameOverwatch`
     * @throws ClassCastException if the instance is not `LeagueVideogameOverwatch`
     */
    public LeagueVideogameOverwatch getLeagueVideogameOverwatch() throws ClassCastException {
        return (LeagueVideogameOverwatch)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogamePUBG`. If the actual instance is not `LeagueVideogamePUBG`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogamePUBG`
     * @throws ClassCastException if the instance is not `LeagueVideogamePUBG`
     */
    public LeagueVideogamePUBG getLeagueVideogamePUBG() throws ClassCastException {
        return (LeagueVideogamePUBG)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameRocketLeague`. If the actual instance is not `LeagueVideogameRocketLeague`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameRocketLeague`
     * @throws ClassCastException if the instance is not `LeagueVideogameRocketLeague`
     */
    public LeagueVideogameRocketLeague getLeagueVideogameRocketLeague() throws ClassCastException {
        return (LeagueVideogameRocketLeague)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameCodmw`. If the actual instance is not `LeagueVideogameCodmw`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameCodmw`
     * @throws ClassCastException if the instance is not `LeagueVideogameCodmw`
     */
    public LeagueVideogameCodmw getLeagueVideogameCodmw() throws ClassCastException {
        return (LeagueVideogameCodmw)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameR6siege`. If the actual instance is not `LeagueVideogameR6siege`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameR6siege`
     * @throws ClassCastException if the instance is not `LeagueVideogameR6siege`
     */
    public LeagueVideogameR6siege getLeagueVideogameR6siege() throws ClassCastException {
        return (LeagueVideogameR6siege)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameFifa`. If the actual instance is not `LeagueVideogameFifa`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameFifa`
     * @throws ClassCastException if the instance is not `LeagueVideogameFifa`
     */
    public LeagueVideogameFifa getLeagueVideogameFifa() throws ClassCastException {
        return (LeagueVideogameFifa)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeagueVideogameValorant`. If the actual instance is not `LeagueVideogameValorant`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeagueVideogameValorant`
     * @throws ClassCastException if the instance is not `LeagueVideogameValorant`
     */
    public LeagueVideogameValorant getLeagueVideogameValorant() throws ClassCastException {
        return (LeagueVideogameValorant)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to LeagueVideogame
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with LeagueVideogameLoL
        try {
            LeagueVideogameLoL.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameLoL failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameCSGO
        try {
            LeagueVideogameCSGO.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameCSGO failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameDota2
        try {
            LeagueVideogameDota2.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameDota2 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameOverwatch
        try {
            LeagueVideogameOverwatch.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameOverwatch failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogamePUBG
        try {
            LeagueVideogamePUBG.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogamePUBG failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameRocketLeague
        try {
            LeagueVideogameRocketLeague.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameRocketLeague failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameCodmw
        try {
            LeagueVideogameCodmw.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameCodmw failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameR6siege
        try {
            LeagueVideogameR6siege.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameR6siege failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameFifa
        try {
            LeagueVideogameFifa.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameFifa failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeagueVideogameValorant
        try {
            LeagueVideogameValorant.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeagueVideogameValorant failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for LeagueVideogame with oneOf schemas: LeagueVideogameCSGO, LeagueVideogameCodmw, LeagueVideogameDota2, LeagueVideogameFifa, LeagueVideogameLoL, LeagueVideogameOverwatch, LeagueVideogamePUBG, LeagueVideogameR6siege, LeagueVideogameRocketLeague, LeagueVideogameValorant. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of LeagueVideogame given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of LeagueVideogame
     * @throws IOException if the JSON string is invalid with respect to LeagueVideogame
     */
    public static LeagueVideogame fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, LeagueVideogame.class);
    }

    /**
     * Convert an instance of LeagueVideogame to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

