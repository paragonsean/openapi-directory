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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.IncidentChangeType;
import org.openapitools.client.model.IncidentID;
import org.openapitools.client.model.IncidentOfTypeLeague;
import org.openapitools.client.model.IncidentOfTypeMatch;
import org.openapitools.client.model.IncidentOfTypePlayer;
import org.openapitools.client.model.IncidentOfTypeSerie;
import org.openapitools.client.model.IncidentOfTypeTeam;
import org.openapitools.client.model.IncidentOfTypeTournament;
import org.openapitools.client.model.Tournament;



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
public class NonDeletionIncident extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(NonDeletionIncident.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!NonDeletionIncident.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'NonDeletionIncident' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<IncidentOfTypeLeague> adapterIncidentOfTypeLeague = gson.getDelegateAdapter(this, TypeToken.get(IncidentOfTypeLeague.class));
            final TypeAdapter<IncidentOfTypeMatch> adapterIncidentOfTypeMatch = gson.getDelegateAdapter(this, TypeToken.get(IncidentOfTypeMatch.class));
            final TypeAdapter<IncidentOfTypePlayer> adapterIncidentOfTypePlayer = gson.getDelegateAdapter(this, TypeToken.get(IncidentOfTypePlayer.class));
            final TypeAdapter<IncidentOfTypeSerie> adapterIncidentOfTypeSerie = gson.getDelegateAdapter(this, TypeToken.get(IncidentOfTypeSerie.class));
            final TypeAdapter<IncidentOfTypeTeam> adapterIncidentOfTypeTeam = gson.getDelegateAdapter(this, TypeToken.get(IncidentOfTypeTeam.class));
            final TypeAdapter<IncidentOfTypeTournament> adapterIncidentOfTypeTournament = gson.getDelegateAdapter(this, TypeToken.get(IncidentOfTypeTournament.class));

            return (TypeAdapter<T>) new TypeAdapter<NonDeletionIncident>() {
                @Override
                public void write(JsonWriter out, NonDeletionIncident value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `IncidentOfTypeLeague`
                    if (value.getActualInstance() instanceof IncidentOfTypeLeague) {
                        JsonElement element = adapterIncidentOfTypeLeague.toJsonTree((IncidentOfTypeLeague)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `IncidentOfTypeMatch`
                    if (value.getActualInstance() instanceof IncidentOfTypeMatch) {
                        JsonElement element = adapterIncidentOfTypeMatch.toJsonTree((IncidentOfTypeMatch)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `IncidentOfTypePlayer`
                    if (value.getActualInstance() instanceof IncidentOfTypePlayer) {
                        JsonElement element = adapterIncidentOfTypePlayer.toJsonTree((IncidentOfTypePlayer)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `IncidentOfTypeSerie`
                    if (value.getActualInstance() instanceof IncidentOfTypeSerie) {
                        JsonElement element = adapterIncidentOfTypeSerie.toJsonTree((IncidentOfTypeSerie)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `IncidentOfTypeTeam`
                    if (value.getActualInstance() instanceof IncidentOfTypeTeam) {
                        JsonElement element = adapterIncidentOfTypeTeam.toJsonTree((IncidentOfTypeTeam)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `IncidentOfTypeTournament`
                    if (value.getActualInstance() instanceof IncidentOfTypeTournament) {
                        JsonElement element = adapterIncidentOfTypeTournament.toJsonTree((IncidentOfTypeTournament)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament");
                }

                @Override
                public NonDeletionIncident read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize IncidentOfTypeLeague
                    try {
                        // validate the JSON object to see if any exception is thrown
                        IncidentOfTypeLeague.validateJsonElement(jsonElement);
                        actualAdapter = adapterIncidentOfTypeLeague;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'IncidentOfTypeLeague'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for IncidentOfTypeLeague failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'IncidentOfTypeLeague'", e);
                    }
                    // deserialize IncidentOfTypeMatch
                    try {
                        // validate the JSON object to see if any exception is thrown
                        IncidentOfTypeMatch.validateJsonElement(jsonElement);
                        actualAdapter = adapterIncidentOfTypeMatch;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'IncidentOfTypeMatch'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for IncidentOfTypeMatch failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'IncidentOfTypeMatch'", e);
                    }
                    // deserialize IncidentOfTypePlayer
                    try {
                        // validate the JSON object to see if any exception is thrown
                        IncidentOfTypePlayer.validateJsonElement(jsonElement);
                        actualAdapter = adapterIncidentOfTypePlayer;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'IncidentOfTypePlayer'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for IncidentOfTypePlayer failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'IncidentOfTypePlayer'", e);
                    }
                    // deserialize IncidentOfTypeSerie
                    try {
                        // validate the JSON object to see if any exception is thrown
                        IncidentOfTypeSerie.validateJsonElement(jsonElement);
                        actualAdapter = adapterIncidentOfTypeSerie;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'IncidentOfTypeSerie'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for IncidentOfTypeSerie failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'IncidentOfTypeSerie'", e);
                    }
                    // deserialize IncidentOfTypeTeam
                    try {
                        // validate the JSON object to see if any exception is thrown
                        IncidentOfTypeTeam.validateJsonElement(jsonElement);
                        actualAdapter = adapterIncidentOfTypeTeam;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'IncidentOfTypeTeam'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for IncidentOfTypeTeam failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'IncidentOfTypeTeam'", e);
                    }
                    // deserialize IncidentOfTypeTournament
                    try {
                        // validate the JSON object to see if any exception is thrown
                        IncidentOfTypeTournament.validateJsonElement(jsonElement);
                        actualAdapter = adapterIncidentOfTypeTournament;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'IncidentOfTypeTournament'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for IncidentOfTypeTournament failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'IncidentOfTypeTournament'", e);
                    }

                    if (match == 1) {
                        NonDeletionIncident ret = new NonDeletionIncident();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for NonDeletionIncident: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public NonDeletionIncident() {
        super("oneOf", Boolean.FALSE);
    }

    public NonDeletionIncident(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("IncidentOfTypeLeague", IncidentOfTypeLeague.class);
        schemas.put("IncidentOfTypeMatch", IncidentOfTypeMatch.class);
        schemas.put("IncidentOfTypePlayer", IncidentOfTypePlayer.class);
        schemas.put("IncidentOfTypeSerie", IncidentOfTypeSerie.class);
        schemas.put("IncidentOfTypeTeam", IncidentOfTypeTeam.class);
        schemas.put("IncidentOfTypeTournament", IncidentOfTypeTournament.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return NonDeletionIncident.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof IncidentOfTypeLeague) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof IncidentOfTypeMatch) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof IncidentOfTypePlayer) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof IncidentOfTypeSerie) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof IncidentOfTypeTeam) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof IncidentOfTypeTournament) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament");
    }

    /**
     * Get the actual instance, which can be the following:
     * IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament
     *
     * @return The actual instance (IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `IncidentOfTypeLeague`. If the actual instance is not `IncidentOfTypeLeague`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `IncidentOfTypeLeague`
     * @throws ClassCastException if the instance is not `IncidentOfTypeLeague`
     */
    public IncidentOfTypeLeague getIncidentOfTypeLeague() throws ClassCastException {
        return (IncidentOfTypeLeague)super.getActualInstance();
    }
    /**
     * Get the actual instance of `IncidentOfTypeMatch`. If the actual instance is not `IncidentOfTypeMatch`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `IncidentOfTypeMatch`
     * @throws ClassCastException if the instance is not `IncidentOfTypeMatch`
     */
    public IncidentOfTypeMatch getIncidentOfTypeMatch() throws ClassCastException {
        return (IncidentOfTypeMatch)super.getActualInstance();
    }
    /**
     * Get the actual instance of `IncidentOfTypePlayer`. If the actual instance is not `IncidentOfTypePlayer`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `IncidentOfTypePlayer`
     * @throws ClassCastException if the instance is not `IncidentOfTypePlayer`
     */
    public IncidentOfTypePlayer getIncidentOfTypePlayer() throws ClassCastException {
        return (IncidentOfTypePlayer)super.getActualInstance();
    }
    /**
     * Get the actual instance of `IncidentOfTypeSerie`. If the actual instance is not `IncidentOfTypeSerie`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `IncidentOfTypeSerie`
     * @throws ClassCastException if the instance is not `IncidentOfTypeSerie`
     */
    public IncidentOfTypeSerie getIncidentOfTypeSerie() throws ClassCastException {
        return (IncidentOfTypeSerie)super.getActualInstance();
    }
    /**
     * Get the actual instance of `IncidentOfTypeTeam`. If the actual instance is not `IncidentOfTypeTeam`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `IncidentOfTypeTeam`
     * @throws ClassCastException if the instance is not `IncidentOfTypeTeam`
     */
    public IncidentOfTypeTeam getIncidentOfTypeTeam() throws ClassCastException {
        return (IncidentOfTypeTeam)super.getActualInstance();
    }
    /**
     * Get the actual instance of `IncidentOfTypeTournament`. If the actual instance is not `IncidentOfTypeTournament`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `IncidentOfTypeTournament`
     * @throws ClassCastException if the instance is not `IncidentOfTypeTournament`
     */
    public IncidentOfTypeTournament getIncidentOfTypeTournament() throws ClassCastException {
        return (IncidentOfTypeTournament)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to NonDeletionIncident
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with IncidentOfTypeLeague
        try {
            IncidentOfTypeLeague.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for IncidentOfTypeLeague failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with IncidentOfTypeMatch
        try {
            IncidentOfTypeMatch.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for IncidentOfTypeMatch failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with IncidentOfTypePlayer
        try {
            IncidentOfTypePlayer.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for IncidentOfTypePlayer failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with IncidentOfTypeSerie
        try {
            IncidentOfTypeSerie.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for IncidentOfTypeSerie failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with IncidentOfTypeTeam
        try {
            IncidentOfTypeTeam.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for IncidentOfTypeTeam failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with IncidentOfTypeTournament
        try {
            IncidentOfTypeTournament.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for IncidentOfTypeTournament failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for NonDeletionIncident with oneOf schemas: IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of NonDeletionIncident given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of NonDeletionIncident
     * @throws IOException if the JSON string is invalid with respect to NonDeletionIncident
     */
    public static NonDeletionIncident fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, NonDeletionIncident.class);
    }

    /**
     * Convert an instance of NonDeletionIncident to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

