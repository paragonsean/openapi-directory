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
import org.openapitools.client.model.BettingSerie;
import org.openapitools.client.model.EsportCSGO;
import org.openapitools.client.model.EsportCodmw;
import org.openapitools.client.model.EsportDota2;
import org.openapitools.client.model.EsportFifa;
import org.openapitools.client.model.EsportFortnite;
import org.openapitools.client.model.EsportLoL;
import org.openapitools.client.model.EsportOverwatch;
import org.openapitools.client.model.EsportPUBG;
import org.openapitools.client.model.EsportR6siege;
import org.openapitools.client.model.EsportRocketLeague;
import org.openapitools.client.model.EsportValorant;



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
public class Esport extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(Esport.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!Esport.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'Esport' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<EsportLoL> adapterEsportLoL = gson.getDelegateAdapter(this, TypeToken.get(EsportLoL.class));
            final TypeAdapter<EsportCSGO> adapterEsportCSGO = gson.getDelegateAdapter(this, TypeToken.get(EsportCSGO.class));
            final TypeAdapter<EsportDota2> adapterEsportDota2 = gson.getDelegateAdapter(this, TypeToken.get(EsportDota2.class));
            final TypeAdapter<EsportOverwatch> adapterEsportOverwatch = gson.getDelegateAdapter(this, TypeToken.get(EsportOverwatch.class));
            final TypeAdapter<EsportPUBG> adapterEsportPUBG = gson.getDelegateAdapter(this, TypeToken.get(EsportPUBG.class));
            final TypeAdapter<EsportFortnite> adapterEsportFortnite = gson.getDelegateAdapter(this, TypeToken.get(EsportFortnite.class));
            final TypeAdapter<EsportRocketLeague> adapterEsportRocketLeague = gson.getDelegateAdapter(this, TypeToken.get(EsportRocketLeague.class));
            final TypeAdapter<EsportCodmw> adapterEsportCodmw = gson.getDelegateAdapter(this, TypeToken.get(EsportCodmw.class));
            final TypeAdapter<EsportR6siege> adapterEsportR6siege = gson.getDelegateAdapter(this, TypeToken.get(EsportR6siege.class));
            final TypeAdapter<EsportFifa> adapterEsportFifa = gson.getDelegateAdapter(this, TypeToken.get(EsportFifa.class));
            final TypeAdapter<EsportValorant> adapterEsportValorant = gson.getDelegateAdapter(this, TypeToken.get(EsportValorant.class));

            return (TypeAdapter<T>) new TypeAdapter<Esport>() {
                @Override
                public void write(JsonWriter out, Esport value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `EsportLoL`
                    if (value.getActualInstance() instanceof EsportLoL) {
                        JsonElement element = adapterEsportLoL.toJsonTree((EsportLoL)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportCSGO`
                    if (value.getActualInstance() instanceof EsportCSGO) {
                        JsonElement element = adapterEsportCSGO.toJsonTree((EsportCSGO)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportDota2`
                    if (value.getActualInstance() instanceof EsportDota2) {
                        JsonElement element = adapterEsportDota2.toJsonTree((EsportDota2)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportOverwatch`
                    if (value.getActualInstance() instanceof EsportOverwatch) {
                        JsonElement element = adapterEsportOverwatch.toJsonTree((EsportOverwatch)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportPUBG`
                    if (value.getActualInstance() instanceof EsportPUBG) {
                        JsonElement element = adapterEsportPUBG.toJsonTree((EsportPUBG)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportFortnite`
                    if (value.getActualInstance() instanceof EsportFortnite) {
                        JsonElement element = adapterEsportFortnite.toJsonTree((EsportFortnite)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportRocketLeague`
                    if (value.getActualInstance() instanceof EsportRocketLeague) {
                        JsonElement element = adapterEsportRocketLeague.toJsonTree((EsportRocketLeague)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportCodmw`
                    if (value.getActualInstance() instanceof EsportCodmw) {
                        JsonElement element = adapterEsportCodmw.toJsonTree((EsportCodmw)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportR6siege`
                    if (value.getActualInstance() instanceof EsportR6siege) {
                        JsonElement element = adapterEsportR6siege.toJsonTree((EsportR6siege)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportFifa`
                    if (value.getActualInstance() instanceof EsportFifa) {
                        JsonElement element = adapterEsportFifa.toJsonTree((EsportFifa)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `EsportValorant`
                    if (value.getActualInstance() instanceof EsportValorant) {
                        JsonElement element = adapterEsportValorant.toJsonTree((EsportValorant)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match oneOf schemas: EsportCSGO, EsportCodmw, EsportDota2, EsportFifa, EsportFortnite, EsportLoL, EsportOverwatch, EsportPUBG, EsportR6siege, EsportRocketLeague, EsportValorant");
                }

                @Override
                public Esport read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    int match = 0;
                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize EsportLoL
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportLoL.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportLoL;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportLoL'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportLoL failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportLoL'", e);
                    }
                    // deserialize EsportCSGO
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportCSGO.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportCSGO;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportCSGO'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportCSGO failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportCSGO'", e);
                    }
                    // deserialize EsportDota2
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportDota2.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportDota2;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportDota2'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportDota2 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportDota2'", e);
                    }
                    // deserialize EsportOverwatch
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportOverwatch.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportOverwatch;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportOverwatch'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportOverwatch failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportOverwatch'", e);
                    }
                    // deserialize EsportPUBG
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportPUBG.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportPUBG;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportPUBG'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportPUBG failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportPUBG'", e);
                    }
                    // deserialize EsportFortnite
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportFortnite.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportFortnite;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportFortnite'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportFortnite failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportFortnite'", e);
                    }
                    // deserialize EsportRocketLeague
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportRocketLeague.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportRocketLeague;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportRocketLeague'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportRocketLeague failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportRocketLeague'", e);
                    }
                    // deserialize EsportCodmw
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportCodmw.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportCodmw;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportCodmw'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportCodmw failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportCodmw'", e);
                    }
                    // deserialize EsportR6siege
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportR6siege.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportR6siege;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportR6siege'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportR6siege failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportR6siege'", e);
                    }
                    // deserialize EsportFifa
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportFifa.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportFifa;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportFifa'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportFifa failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportFifa'", e);
                    }
                    // deserialize EsportValorant
                    try {
                        // validate the JSON object to see if any exception is thrown
                        EsportValorant.validateJsonElement(jsonElement);
                        actualAdapter = adapterEsportValorant;
                        match++;
                        log.log(Level.FINER, "Input data matches schema 'EsportValorant'");
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for EsportValorant failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'EsportValorant'", e);
                    }

                    if (match == 1) {
                        Esport ret = new Esport();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    }

                    throw new IOException(String.format("Failed deserialization for Esport: %d classes match result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", match, errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in oneOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public Esport() {
        super("oneOf", Boolean.FALSE);
    }

    public Esport(Object o) {
        super("oneOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("EsportLoL", EsportLoL.class);
        schemas.put("EsportCSGO", EsportCSGO.class);
        schemas.put("EsportDota2", EsportDota2.class);
        schemas.put("EsportOverwatch", EsportOverwatch.class);
        schemas.put("EsportPUBG", EsportPUBG.class);
        schemas.put("EsportFortnite", EsportFortnite.class);
        schemas.put("EsportRocketLeague", EsportRocketLeague.class);
        schemas.put("EsportCodmw", EsportCodmw.class);
        schemas.put("EsportR6siege", EsportR6siege.class);
        schemas.put("EsportFifa", EsportFifa.class);
        schemas.put("EsportValorant", EsportValorant.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return Esport.schemas;
    }

    /**
     * Set the instance that matches the oneOf child schema, check
     * the instance parameter is valid against the oneOf child schemas:
     * EsportCSGO, EsportCodmw, EsportDota2, EsportFifa, EsportFortnite, EsportLoL, EsportOverwatch, EsportPUBG, EsportR6siege, EsportRocketLeague, EsportValorant
     *
     * It could be an instance of the 'oneOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof EsportLoL) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportCSGO) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportDota2) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportOverwatch) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportPUBG) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportFortnite) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportRocketLeague) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportCodmw) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportR6siege) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportFifa) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof EsportValorant) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be EsportCSGO, EsportCodmw, EsportDota2, EsportFifa, EsportFortnite, EsportLoL, EsportOverwatch, EsportPUBG, EsportR6siege, EsportRocketLeague, EsportValorant");
    }

    /**
     * Get the actual instance, which can be the following:
     * EsportCSGO, EsportCodmw, EsportDota2, EsportFifa, EsportFortnite, EsportLoL, EsportOverwatch, EsportPUBG, EsportR6siege, EsportRocketLeague, EsportValorant
     *
     * @return The actual instance (EsportCSGO, EsportCodmw, EsportDota2, EsportFifa, EsportFortnite, EsportLoL, EsportOverwatch, EsportPUBG, EsportR6siege, EsportRocketLeague, EsportValorant)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `EsportLoL`. If the actual instance is not `EsportLoL`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportLoL`
     * @throws ClassCastException if the instance is not `EsportLoL`
     */
    public EsportLoL getEsportLoL() throws ClassCastException {
        return (EsportLoL)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportCSGO`. If the actual instance is not `EsportCSGO`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportCSGO`
     * @throws ClassCastException if the instance is not `EsportCSGO`
     */
    public EsportCSGO getEsportCSGO() throws ClassCastException {
        return (EsportCSGO)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportDota2`. If the actual instance is not `EsportDota2`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportDota2`
     * @throws ClassCastException if the instance is not `EsportDota2`
     */
    public EsportDota2 getEsportDota2() throws ClassCastException {
        return (EsportDota2)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportOverwatch`. If the actual instance is not `EsportOverwatch`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportOverwatch`
     * @throws ClassCastException if the instance is not `EsportOverwatch`
     */
    public EsportOverwatch getEsportOverwatch() throws ClassCastException {
        return (EsportOverwatch)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportPUBG`. If the actual instance is not `EsportPUBG`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportPUBG`
     * @throws ClassCastException if the instance is not `EsportPUBG`
     */
    public EsportPUBG getEsportPUBG() throws ClassCastException {
        return (EsportPUBG)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportFortnite`. If the actual instance is not `EsportFortnite`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportFortnite`
     * @throws ClassCastException if the instance is not `EsportFortnite`
     */
    public EsportFortnite getEsportFortnite() throws ClassCastException {
        return (EsportFortnite)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportRocketLeague`. If the actual instance is not `EsportRocketLeague`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportRocketLeague`
     * @throws ClassCastException if the instance is not `EsportRocketLeague`
     */
    public EsportRocketLeague getEsportRocketLeague() throws ClassCastException {
        return (EsportRocketLeague)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportCodmw`. If the actual instance is not `EsportCodmw`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportCodmw`
     * @throws ClassCastException if the instance is not `EsportCodmw`
     */
    public EsportCodmw getEsportCodmw() throws ClassCastException {
        return (EsportCodmw)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportR6siege`. If the actual instance is not `EsportR6siege`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportR6siege`
     * @throws ClassCastException if the instance is not `EsportR6siege`
     */
    public EsportR6siege getEsportR6siege() throws ClassCastException {
        return (EsportR6siege)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportFifa`. If the actual instance is not `EsportFifa`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportFifa`
     * @throws ClassCastException if the instance is not `EsportFifa`
     */
    public EsportFifa getEsportFifa() throws ClassCastException {
        return (EsportFifa)super.getActualInstance();
    }
    /**
     * Get the actual instance of `EsportValorant`. If the actual instance is not `EsportValorant`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `EsportValorant`
     * @throws ClassCastException if the instance is not `EsportValorant`
     */
    public EsportValorant getEsportValorant() throws ClassCastException {
        return (EsportValorant)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to Esport
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate oneOf schemas one by one
        int validCount = 0;
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with EsportLoL
        try {
            EsportLoL.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportLoL failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportCSGO
        try {
            EsportCSGO.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportCSGO failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportDota2
        try {
            EsportDota2.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportDota2 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportOverwatch
        try {
            EsportOverwatch.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportOverwatch failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportPUBG
        try {
            EsportPUBG.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportPUBG failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportFortnite
        try {
            EsportFortnite.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportFortnite failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportRocketLeague
        try {
            EsportRocketLeague.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportRocketLeague failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportCodmw
        try {
            EsportCodmw.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportCodmw failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportR6siege
        try {
            EsportR6siege.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportR6siege failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportFifa
        try {
            EsportFifa.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportFifa failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with EsportValorant
        try {
            EsportValorant.validateJsonElement(jsonElement);
            validCount++;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for EsportValorant failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        if (validCount != 1) {
            throw new IOException(String.format("The JSON string is invalid for Esport with oneOf schemas: EsportCSGO, EsportCodmw, EsportDota2, EsportFifa, EsportFortnite, EsportLoL, EsportOverwatch, EsportPUBG, EsportR6siege, EsportRocketLeague, EsportValorant. %d class(es) match the result, expected 1. Detailed failure message for oneOf schemas: %s. JSON: %s", validCount, errorMessages, jsonElement.toString()));
        }
    }

    /**
     * Create an instance of Esport given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of Esport
     * @throws IOException if the JSON string is invalid with respect to Esport
     */
    public static Esport fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, Esport.class);
    }

    /**
     * Convert an instance of Esport to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

