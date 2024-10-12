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
import org.openapitools.client.model.ApprovalUrlLink;
import org.openapitools.client.model.CustomerLink;
import org.openapitools.client.model.DisputeLink;
import org.openapitools.client.model.GatewayAccountLink;
import org.openapitools.client.model.InvoicesLink;
import org.openapitools.client.model.LeadSourceLink;
import org.openapitools.client.model.ParentTransactionLink;
import org.openapitools.client.model.PaymentCardLink;
import org.openapitools.client.model.QueryUrlLink;
import org.openapitools.client.model.RefundUrlLink;
import org.openapitools.client.model.RetriedTransactionLink;
import org.openapitools.client.model.SelfLink;
import org.openapitools.client.model.TransactionUpdateUrlLink;
import org.openapitools.client.model.WebsiteLink;



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
public class TransactionAllOfLinks extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(TransactionAllOfLinks.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!TransactionAllOfLinks.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'TransactionAllOfLinks' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<SelfLink> adapterSelfLink = gson.getDelegateAdapter(this, TypeToken.get(SelfLink.class));
            final TypeAdapter<WebsiteLink> adapterWebsiteLink = gson.getDelegateAdapter(this, TypeToken.get(WebsiteLink.class));
            final TypeAdapter<CustomerLink> adapterCustomerLink = gson.getDelegateAdapter(this, TypeToken.get(CustomerLink.class));
            final TypeAdapter<GatewayAccountLink> adapterGatewayAccountLink = gson.getDelegateAdapter(this, TypeToken.get(GatewayAccountLink.class));
            final TypeAdapter<PaymentCardLink> adapterPaymentCardLink = gson.getDelegateAdapter(this, TypeToken.get(PaymentCardLink.class));
            final TypeAdapter<ParentTransactionLink> adapterParentTransactionLink = gson.getDelegateAdapter(this, TypeToken.get(ParentTransactionLink.class));
            final TypeAdapter<RetriedTransactionLink> adapterRetriedTransactionLink = gson.getDelegateAdapter(this, TypeToken.get(RetriedTransactionLink.class));
            final TypeAdapter<LeadSourceLink> adapterLeadSourceLink = gson.getDelegateAdapter(this, TypeToken.get(LeadSourceLink.class));
            final TypeAdapter<ApprovalUrlLink> adapterApprovalUrlLink = gson.getDelegateAdapter(this, TypeToken.get(ApprovalUrlLink.class));
            final TypeAdapter<RefundUrlLink> adapterRefundUrlLink = gson.getDelegateAdapter(this, TypeToken.get(RefundUrlLink.class));
            final TypeAdapter<TransactionUpdateUrlLink> adapterTransactionUpdateUrlLink = gson.getDelegateAdapter(this, TypeToken.get(TransactionUpdateUrlLink.class));
            final TypeAdapter<DisputeLink> adapterDisputeLink = gson.getDelegateAdapter(this, TypeToken.get(DisputeLink.class));
            final TypeAdapter<InvoicesLink> adapterInvoicesLink = gson.getDelegateAdapter(this, TypeToken.get(InvoicesLink.class));
            final TypeAdapter<QueryUrlLink> adapterQueryUrlLink = gson.getDelegateAdapter(this, TypeToken.get(QueryUrlLink.class));

            return (TypeAdapter<T>) new TypeAdapter<TransactionAllOfLinks>() {
                @Override
                public void write(JsonWriter out, TransactionAllOfLinks value) throws IOException {
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
                    // check if the actual instance is of the type `WebsiteLink`
                    if (value.getActualInstance() instanceof WebsiteLink) {
                        JsonElement element = adapterWebsiteLink.toJsonTree((WebsiteLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `CustomerLink`
                    if (value.getActualInstance() instanceof CustomerLink) {
                        JsonElement element = adapterCustomerLink.toJsonTree((CustomerLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `GatewayAccountLink`
                    if (value.getActualInstance() instanceof GatewayAccountLink) {
                        JsonElement element = adapterGatewayAccountLink.toJsonTree((GatewayAccountLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `PaymentCardLink`
                    if (value.getActualInstance() instanceof PaymentCardLink) {
                        JsonElement element = adapterPaymentCardLink.toJsonTree((PaymentCardLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ParentTransactionLink`
                    if (value.getActualInstance() instanceof ParentTransactionLink) {
                        JsonElement element = adapterParentTransactionLink.toJsonTree((ParentTransactionLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `RetriedTransactionLink`
                    if (value.getActualInstance() instanceof RetriedTransactionLink) {
                        JsonElement element = adapterRetriedTransactionLink.toJsonTree((RetriedTransactionLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `LeadSourceLink`
                    if (value.getActualInstance() instanceof LeadSourceLink) {
                        JsonElement element = adapterLeadSourceLink.toJsonTree((LeadSourceLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ApprovalUrlLink`
                    if (value.getActualInstance() instanceof ApprovalUrlLink) {
                        JsonElement element = adapterApprovalUrlLink.toJsonTree((ApprovalUrlLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `RefundUrlLink`
                    if (value.getActualInstance() instanceof RefundUrlLink) {
                        JsonElement element = adapterRefundUrlLink.toJsonTree((RefundUrlLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `TransactionUpdateUrlLink`
                    if (value.getActualInstance() instanceof TransactionUpdateUrlLink) {
                        JsonElement element = adapterTransactionUpdateUrlLink.toJsonTree((TransactionUpdateUrlLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `DisputeLink`
                    if (value.getActualInstance() instanceof DisputeLink) {
                        JsonElement element = adapterDisputeLink.toJsonTree((DisputeLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `InvoicesLink`
                    if (value.getActualInstance() instanceof InvoicesLink) {
                        JsonElement element = adapterInvoicesLink.toJsonTree((InvoicesLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `QueryUrlLink`
                    if (value.getActualInstance() instanceof QueryUrlLink) {
                        JsonElement element = adapterQueryUrlLink.toJsonTree((QueryUrlLink)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: ApprovalUrlLink, CustomerLink, DisputeLink, GatewayAccountLink, InvoicesLink, LeadSourceLink, ParentTransactionLink, PaymentCardLink, QueryUrlLink, RefundUrlLink, RetriedTransactionLink, SelfLink, TransactionUpdateUrlLink, WebsiteLink");
                }

                @Override
                public TransactionAllOfLinks read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize SelfLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        SelfLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterSelfLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for SelfLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'SelfLink'", e);
                    }
                    // deserialize WebsiteLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        WebsiteLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterWebsiteLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for WebsiteLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'WebsiteLink'", e);
                    }
                    // deserialize CustomerLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        CustomerLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterCustomerLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for CustomerLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'CustomerLink'", e);
                    }
                    // deserialize GatewayAccountLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        GatewayAccountLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterGatewayAccountLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for GatewayAccountLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'GatewayAccountLink'", e);
                    }
                    // deserialize PaymentCardLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        PaymentCardLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterPaymentCardLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for PaymentCardLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'PaymentCardLink'", e);
                    }
                    // deserialize ParentTransactionLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ParentTransactionLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterParentTransactionLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ParentTransactionLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ParentTransactionLink'", e);
                    }
                    // deserialize RetriedTransactionLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        RetriedTransactionLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterRetriedTransactionLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for RetriedTransactionLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'RetriedTransactionLink'", e);
                    }
                    // deserialize LeadSourceLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        LeadSourceLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterLeadSourceLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for LeadSourceLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'LeadSourceLink'", e);
                    }
                    // deserialize ApprovalUrlLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ApprovalUrlLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterApprovalUrlLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ApprovalUrlLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ApprovalUrlLink'", e);
                    }
                    // deserialize RefundUrlLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        RefundUrlLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterRefundUrlLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for RefundUrlLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'RefundUrlLink'", e);
                    }
                    // deserialize TransactionUpdateUrlLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        TransactionUpdateUrlLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterTransactionUpdateUrlLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for TransactionUpdateUrlLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'TransactionUpdateUrlLink'", e);
                    }
                    // deserialize DisputeLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        DisputeLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterDisputeLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for DisputeLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'DisputeLink'", e);
                    }
                    // deserialize InvoicesLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        InvoicesLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterInvoicesLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for InvoicesLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'InvoicesLink'", e);
                    }
                    // deserialize QueryUrlLink
                    try {
                        // validate the JSON object to see if any exception is thrown
                        QueryUrlLink.validateJsonElement(jsonElement);
                        actualAdapter = adapterQueryUrlLink;
                        TransactionAllOfLinks ret = new TransactionAllOfLinks();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for QueryUrlLink failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'QueryUrlLink'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for TransactionAllOfLinks: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public TransactionAllOfLinks() {
        super("anyOf", Boolean.FALSE);
    }

    public TransactionAllOfLinks(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("SelfLink", SelfLink.class);
        schemas.put("WebsiteLink", WebsiteLink.class);
        schemas.put("CustomerLink", CustomerLink.class);
        schemas.put("GatewayAccountLink", GatewayAccountLink.class);
        schemas.put("PaymentCardLink", PaymentCardLink.class);
        schemas.put("ParentTransactionLink", ParentTransactionLink.class);
        schemas.put("RetriedTransactionLink", RetriedTransactionLink.class);
        schemas.put("LeadSourceLink", LeadSourceLink.class);
        schemas.put("ApprovalUrlLink", ApprovalUrlLink.class);
        schemas.put("RefundUrlLink", RefundUrlLink.class);
        schemas.put("TransactionUpdateUrlLink", TransactionUpdateUrlLink.class);
        schemas.put("DisputeLink", DisputeLink.class);
        schemas.put("InvoicesLink", InvoicesLink.class);
        schemas.put("QueryUrlLink", QueryUrlLink.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return TransactionAllOfLinks.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * ApprovalUrlLink, CustomerLink, DisputeLink, GatewayAccountLink, InvoicesLink, LeadSourceLink, ParentTransactionLink, PaymentCardLink, QueryUrlLink, RefundUrlLink, RetriedTransactionLink, SelfLink, TransactionUpdateUrlLink, WebsiteLink
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof SelfLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof WebsiteLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof CustomerLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof GatewayAccountLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof PaymentCardLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ParentTransactionLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof RetriedTransactionLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof LeadSourceLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ApprovalUrlLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof RefundUrlLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof TransactionUpdateUrlLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof DisputeLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof InvoicesLink) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof QueryUrlLink) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be ApprovalUrlLink, CustomerLink, DisputeLink, GatewayAccountLink, InvoicesLink, LeadSourceLink, ParentTransactionLink, PaymentCardLink, QueryUrlLink, RefundUrlLink, RetriedTransactionLink, SelfLink, TransactionUpdateUrlLink, WebsiteLink");
    }

    /**
     * Get the actual instance, which can be the following:
     * ApprovalUrlLink, CustomerLink, DisputeLink, GatewayAccountLink, InvoicesLink, LeadSourceLink, ParentTransactionLink, PaymentCardLink, QueryUrlLink, RefundUrlLink, RetriedTransactionLink, SelfLink, TransactionUpdateUrlLink, WebsiteLink
     *
     * @return The actual instance (ApprovalUrlLink, CustomerLink, DisputeLink, GatewayAccountLink, InvoicesLink, LeadSourceLink, ParentTransactionLink, PaymentCardLink, QueryUrlLink, RefundUrlLink, RetriedTransactionLink, SelfLink, TransactionUpdateUrlLink, WebsiteLink)
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
     * Get the actual instance of `WebsiteLink`. If the actual instance is not `WebsiteLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `WebsiteLink`
     * @throws ClassCastException if the instance is not `WebsiteLink`
     */
    public WebsiteLink getWebsiteLink() throws ClassCastException {
        return (WebsiteLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `CustomerLink`. If the actual instance is not `CustomerLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `CustomerLink`
     * @throws ClassCastException if the instance is not `CustomerLink`
     */
    public CustomerLink getCustomerLink() throws ClassCastException {
        return (CustomerLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `GatewayAccountLink`. If the actual instance is not `GatewayAccountLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `GatewayAccountLink`
     * @throws ClassCastException if the instance is not `GatewayAccountLink`
     */
    public GatewayAccountLink getGatewayAccountLink() throws ClassCastException {
        return (GatewayAccountLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `PaymentCardLink`. If the actual instance is not `PaymentCardLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `PaymentCardLink`
     * @throws ClassCastException if the instance is not `PaymentCardLink`
     */
    public PaymentCardLink getPaymentCardLink() throws ClassCastException {
        return (PaymentCardLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ParentTransactionLink`. If the actual instance is not `ParentTransactionLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ParentTransactionLink`
     * @throws ClassCastException if the instance is not `ParentTransactionLink`
     */
    public ParentTransactionLink getParentTransactionLink() throws ClassCastException {
        return (ParentTransactionLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `RetriedTransactionLink`. If the actual instance is not `RetriedTransactionLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `RetriedTransactionLink`
     * @throws ClassCastException if the instance is not `RetriedTransactionLink`
     */
    public RetriedTransactionLink getRetriedTransactionLink() throws ClassCastException {
        return (RetriedTransactionLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `LeadSourceLink`. If the actual instance is not `LeadSourceLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `LeadSourceLink`
     * @throws ClassCastException if the instance is not `LeadSourceLink`
     */
    public LeadSourceLink getLeadSourceLink() throws ClassCastException {
        return (LeadSourceLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ApprovalUrlLink`. If the actual instance is not `ApprovalUrlLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ApprovalUrlLink`
     * @throws ClassCastException if the instance is not `ApprovalUrlLink`
     */
    public ApprovalUrlLink getApprovalUrlLink() throws ClassCastException {
        return (ApprovalUrlLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `RefundUrlLink`. If the actual instance is not `RefundUrlLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `RefundUrlLink`
     * @throws ClassCastException if the instance is not `RefundUrlLink`
     */
    public RefundUrlLink getRefundUrlLink() throws ClassCastException {
        return (RefundUrlLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `TransactionUpdateUrlLink`. If the actual instance is not `TransactionUpdateUrlLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `TransactionUpdateUrlLink`
     * @throws ClassCastException if the instance is not `TransactionUpdateUrlLink`
     */
    public TransactionUpdateUrlLink getTransactionUpdateUrlLink() throws ClassCastException {
        return (TransactionUpdateUrlLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `DisputeLink`. If the actual instance is not `DisputeLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `DisputeLink`
     * @throws ClassCastException if the instance is not `DisputeLink`
     */
    public DisputeLink getDisputeLink() throws ClassCastException {
        return (DisputeLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `InvoicesLink`. If the actual instance is not `InvoicesLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `InvoicesLink`
     * @throws ClassCastException if the instance is not `InvoicesLink`
     */
    public InvoicesLink getInvoicesLink() throws ClassCastException {
        return (InvoicesLink)super.getActualInstance();
    }
    /**
     * Get the actual instance of `QueryUrlLink`. If the actual instance is not `QueryUrlLink`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `QueryUrlLink`
     * @throws ClassCastException if the instance is not `QueryUrlLink`
     */
    public QueryUrlLink getQueryUrlLink() throws ClassCastException {
        return (QueryUrlLink)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to TransactionAllOfLinks
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
        // validate the json string with WebsiteLink
        try {
            WebsiteLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for WebsiteLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with CustomerLink
        try {
            CustomerLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for CustomerLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with GatewayAccountLink
        try {
            GatewayAccountLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for GatewayAccountLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with PaymentCardLink
        try {
            PaymentCardLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for PaymentCardLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ParentTransactionLink
        try {
            ParentTransactionLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ParentTransactionLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with RetriedTransactionLink
        try {
            RetriedTransactionLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for RetriedTransactionLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with LeadSourceLink
        try {
            LeadSourceLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for LeadSourceLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ApprovalUrlLink
        try {
            ApprovalUrlLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ApprovalUrlLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with RefundUrlLink
        try {
            RefundUrlLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for RefundUrlLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with TransactionUpdateUrlLink
        try {
            TransactionUpdateUrlLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for TransactionUpdateUrlLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with DisputeLink
        try {
            DisputeLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for DisputeLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with InvoicesLink
        try {
            InvoicesLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for InvoicesLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with QueryUrlLink
        try {
            QueryUrlLink.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for QueryUrlLink failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for TransactionAllOfLinks with anyOf schemas: ApprovalUrlLink, CustomerLink, DisputeLink, GatewayAccountLink, InvoicesLink, LeadSourceLink, ParentTransactionLink, PaymentCardLink, QueryUrlLink, RefundUrlLink, RetriedTransactionLink, SelfLink, TransactionUpdateUrlLink, WebsiteLink. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of TransactionAllOfLinks given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of TransactionAllOfLinks
     * @throws IOException if the JSON string is invalid with respect to TransactionAllOfLinks
     */
    public static TransactionAllOfLinks fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, TransactionAllOfLinks.class);
    }

    /**
     * Convert an instance of TransactionAllOfLinks to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

