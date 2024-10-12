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
import org.openapitools.client.model.CommonSubscriptionItemsInner;
import org.openapitools.client.model.CommonSubscriptionOrderAllOfLineItemSubtotal;
import org.openapitools.client.model.CommonSubscriptionOrderAllOfRecurringInterval;
import org.openapitools.client.model.CommonSubscriptionOrderAllOfTrial;
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.InvoiceTimeShift;
import org.openapitools.client.model.RiskMetadata;
import org.openapitools.client.model.SubscriptionMetadataEmbeddedInner;
import org.openapitools.client.model.SubscriptionMetadataLinksInner;
import org.openapitools.client.model.UpcomingInvoiceItem;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for SubscriptionOrder
 */
public class SubscriptionOrderTest {
    private final SubscriptionOrder model = new SubscriptionOrder();

    /**
     * Model tests for SubscriptionOrder
     */
    @Test
    public void testSubscriptionOrder() {
        // TODO: test SubscriptionOrder
    }

    /**
     * Test the property 'activationTime'
     */
    @Test
    public void activationTimeTest() {
        // TODO: test activationTime
    }

    /**
     * Test the property 'billingAddress'
     */
    @Test
    public void billingAddressTest() {
        // TODO: test billingAddress
    }

    /**
     * Test the property 'billingStatus'
     */
    @Test
    public void billingStatusTest() {
        // TODO: test billingStatus
    }

    /**
     * Test the property 'couponIds'
     */
    @Test
    public void couponIdsTest() {
        // TODO: test couponIds
    }

    /**
     * Test the property 'deliveryAddress'
     */
    @Test
    public void deliveryAddressTest() {
        // TODO: test deliveryAddress
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'initialInvoiceId'
     */
    @Test
    public void initialInvoiceIdTest() {
        // TODO: test initialInvoiceId
    }

    /**
     * Test the property 'items'
     */
    @Test
    public void itemsTest() {
        // TODO: test items
    }

    /**
     * Test the property 'orderType'
     */
    @Test
    public void orderTypeTest() {
        // TODO: test orderType
    }

    /**
     * Test the property 'poNumber'
     */
    @Test
    public void poNumberTest() {
        // TODO: test poNumber
    }

    /**
     * Test the property 'recentInvoiceId'
     */
    @Test
    public void recentInvoiceIdTest() {
        // TODO: test recentInvoiceId
    }

    /**
     * Test the property 'voidTime'
     */
    @Test
    public void voidTimeTest() {
        // TODO: test voidTime
    }

    /**
     * Test the property 'websiteId'
     */
    @Test
    public void websiteIdTest() {
        // TODO: test websiteId
    }

    /**
     * Test the property 'autopay'
     */
    @Test
    public void autopayTest() {
        // TODO: test autopay
    }

    /**
     * Test the property 'endTime'
     */
    @Test
    public void endTimeTest() {
        // TODO: test endTime
    }

    /**
     * Test the property 'inTrial'
     */
    @Test
    public void inTrialTest() {
        // TODO: test inTrial
    }

    /**
     * Test the property 'invoiceTimeShift'
     */
    @Test
    public void invoiceTimeShiftTest() {
        // TODO: test invoiceTimeShift
    }

    /**
     * Test the property 'isTrialOnly'
     */
    @Test
    public void isTrialOnlyTest() {
        // TODO: test isTrialOnly
    }

    /**
     * Test the property 'lineItemSubtotal'
     */
    @Test
    public void lineItemSubtotalTest() {
        // TODO: test lineItemSubtotal
    }

    /**
     * Test the property 'lineItems'
     */
    @Test
    public void lineItemsTest() {
        // TODO: test lineItems
    }

    /**
     * Test the property 'rebillNumber'
     */
    @Test
    public void rebillNumberTest() {
        // TODO: test rebillNumber
    }

    /**
     * Test the property 'recurringInterval'
     */
    @Test
    public void recurringIntervalTest() {
        // TODO: test recurringInterval
    }

    /**
     * Test the property 'renewalTime'
     */
    @Test
    public void renewalTimeTest() {
        // TODO: test renewalTime
    }

    /**
     * Test the property 'startTime'
     */
    @Test
    public void startTimeTest() {
        // TODO: test startTime
    }

    /**
     * Test the property 'status'
     */
    @Test
    public void statusTest() {
        // TODO: test status
    }

    /**
     * Test the property 'trial'
     */
    @Test
    public void trialTest() {
        // TODO: test trial
    }

    /**
     * Test the property 'cancelCategory'
     */
    @Test
    public void cancelCategoryTest() {
        // TODO: test cancelCategory
    }

    /**
     * Test the property 'cancelDescription'
     */
    @Test
    public void cancelDescriptionTest() {
        // TODO: test cancelDescription
    }

    /**
     * Test the property 'canceledBy'
     */
    @Test
    public void canceledByTest() {
        // TODO: test canceledBy
    }

    /**
     * Test the property 'canceledTime'
     */
    @Test
    public void canceledTimeTest() {
        // TODO: test canceledTime
    }

    /**
     * Test the property 'embedded'
     */
    @Test
    public void embeddedTest() {
        // TODO: test embedded
    }

    /**
     * Test the property 'links'
     */
    @Test
    public void linksTest() {
        // TODO: test links
    }

    /**
     * Test the property 'createdTime'
     */
    @Test
    public void createdTimeTest() {
        // TODO: test createdTime
    }

    /**
     * Test the property 'customFields'
     */
    @Test
    public void customFieldsTest() {
        // TODO: test customFields
    }

    /**
     * Test the property 'revision'
     */
    @Test
    public void revisionTest() {
        // TODO: test revision
    }

    /**
     * Test the property 'riskMetadata'
     */
    @Test
    public void riskMetadataTest() {
        // TODO: test riskMetadata
    }

    /**
     * Test the property 'updatedTime'
     */
    @Test
    public void updatedTimeTest() {
        // TODO: test updatedTime
    }

    /**
     * Test the property 'customerId'
     */
    @Test
    public void customerIdTest() {
        // TODO: test customerId
    }

    /**
     * Test the property 'renewalReminderNumber'
     */
    @Test
    public void renewalReminderNumberTest() {
        // TODO: test renewalReminderNumber
    }

    /**
     * Test the property 'renewalReminderTime'
     */
    @Test
    public void renewalReminderTimeTest() {
        // TODO: test renewalReminderTime
    }

    /**
     * Test the property 'trialReminderNumber'
     */
    @Test
    public void trialReminderNumberTest() {
        // TODO: test trialReminderNumber
    }

    /**
     * Test the property 'trialReminderTime'
     */
    @Test
    public void trialReminderTimeTest() {
        // TODO: test trialReminderTime
    }

}
