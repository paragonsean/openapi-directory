/**
 * Developer documentation
 * # Welcome  Implementing a new tool can be daunting, but it doesn't have to. You can implement journy.io in a few different ways to ensure it fits with the rest of your tech stack seamlessly.  We welcome your feedback, ideas and suggestions. We really want to make your life easier, so if we’re falling short or should be doing something different, we want to hear about it. Send us an email at [hi@journy.io](mailto:hi@journy.io) or reach out via the chat on our website or on our platform.  There are multiple ways you can send us data about users and accounts. We have both frontend and backend APIs, which can be used together at the same time.  If you already use [Segment](https://segment.com/), you can [get up and running with journy.io in seconds](https://help.journy.io/en/articles/6488307-the-segment-connector).  # Concepts  ## Users  The most basic entity is a user, a specific individual that completed an interaction with your product.  We support multiple types of users, often differentiated by it's external ID prefix. E.g. In the case you are building an ordering app, there could easily be an administrator (who updates products and checks for orders) and the end-customers who place orders. One could have a typical ADM-XXXXXXXX ID, while the other would be referenced by USR-XXXXXXXXX.  ## Accounts  In B2B SaaS, users can be part of multiple accounts. E.g. Imagine you're building a content scheduling app where an agency can manage the social media posts of their clients. Each client of the agency has its own account in the product.  If your app doesn't have the concept of a team or group of users, you can ignore accounts.  ## Events  An event is a data point that represents an interaction between a user and/or an account; and your product. Events can represents any range of interactions. E.g. Every time a customer creates an invoice in an invoicing app. Actions like creating an invoice can be tracked as an event in journy.io.  It's critical to track events properly. You'll need to provide either an account ID, or a user ID, or both; when tracking an event. E.g. If a user updates his personal settings, you can omit the account ID as the event would not be related to any account. In a same logic, an account could get a 'suspend account' event (with account ID) from an internal process, whereas no user would be associated. In most cases, events will be associated to both 1 user and 1 account.  You can optionally pass extra details as metadata (e.g. amount of the invoice). This gets particarly powerfull when creating computed properties on those event metadata. E.g. Our above ordering app could send journy.io 'Place Order' events with metadata 'price', on which journy.io very easily would compute a total order value (for each account) for the last 30 days.  💡 Metadata does not update the properties of a user or account.  # Frontend vs backend  The best implementations we see employ a hybrid approach to maximize data quality while maintaining the flexibility to easily collect the data they need.  We recommend using our JavaScript snippet to track screen views and our backend API to sync users, sync accounts and track events.  When evaluating how to track a particular event, we suggest starting with server-side and only use frontend if it's not possible to collect purely server-side. This can be the case if you need to track interactions with your product that don't result in any natural server requests (such as a button click that opens a modal).  # Frontend  ## Setup  💡 You can find the JavaScript snippet in the website settings in the connections view.  Copy the JavaScript snippet and place it in the head or body of your application.  The snippet automatically calls `journy(\"init\", { ... })` and `journy(\"pageview\")`.  ## Identify user  💡 A user ID should be a robust, static, unique identifier that you recognize a user by in your own systems. Because these IDs are consistent across a customer’s lifetime, you should include a user ID in identify calls as often as you can. Ideally, the user ID should be a database ID.  💡 journy.io does not recommend using simple email addresses or usernames as user ID, as these can change over time. journy.io recommends that you use static IDs instead, so the IDs never change. When you use a static ID, you can still recognize the user in your analytics tools, even if the user changes their email address.  💡 The properties `full_name`, `first_name`, `last_name`, `phone` and `registered_at` will be used for creating contacts in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"identify\")` allows you to identify the user that is currently using your product.  ```ts journy(\"identify\", {   // Email or user ID is required   email: \"john.doe@acme.com\",   // Unique identifier for the user in your database   userId: \"20\",    // Optional   // Hash of the user ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     full_name: \"John Doe\",     // or     first_name: \"John\",     last_name: \"Doe\",      phone: \"123\",     registered_at: new Date(/_* ... *_/),     is_admin: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Identify account  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  💡 The properties `name`, `mrr`, `plan` and `registered_at` will be used to create companies in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"account\")` allows you to identify the business account (i.e. organization) using your product.  ```ts journy(\"account\", {   // Required   // Unique identifier for the account in your database   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     name: \"ACME, Inc\",     mrr: 399,     plan: \"Pro\",     registered_at: new Date(/_* ... *_/),     is_paying: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Send page view  💡 In applications, we advise you to use screen views instead of page views.  The JavaScript snippet in the site settings includes a `pageview` by default.  ```ts journy(\"pageview\"); ```  If you have a B2B application, we recommend to set account ID for every page view that happens within the context of an account.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"pageview\", {   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Send screen view  In applications, we strongly advise you to use screen views instead of page views.  Page URLs in applications often include the account ID (e.g. https://app.acme.com/accountId/settings).  This makes it difficult to create signals, segments, ... based on those URLs.  That's what screen views solve. It allows you to set a name for the screen being viewed (e.g. Account settings).  ```ts journy(\"screen\", { name: \"Personal settings\" }); ```  If you have a B2B application, we recommend to set account ID for every screen view that happens within the context of an account.  Example: \"Personal settings\" would be without account ID, \"Team settings\" would be with account ID.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"screen\", {   name: \"Account settings\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Trigger an event  💡 Use past tense for event names.  User events:  ```js journy(\"event\", {   // required   name: \"signed_in\",    // optional   metadata: {     key: \"value\",   }, }); ```  Account events:  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```js journy(\"event\", {   // required   name: \"created_invoice\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // optional   metadata: {     key: \"value\",     amount: 100,     allow_wire_transfer: true,   }, }); ```  ## Identity verification  Identity verification ensures that one person can't impersonate another.  Identity verification requires you to add an hash (HMAC) (that you generate on your server using SHA256) to your installation snippet alongside your user ID and account ID.  journy.io won't accept requests for a logged-in user without a valid hash. The hash is calculated using a secret key, which you should never share. Without this secret key, no third party can send journy.io a valid hash for one of your users, so they can't impersonate your users.  This is optional but highly recommended.  You can enable identify verification in the website settings in the connections view.  ```js journy(\"identify\", {   userId: \"userId\",   verification: \"USER_ID_HMAC_VALUE_HERE\" })  journy(\"account\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" })  journy(\"event\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" }) ```  ### PHP  ```php <?php  hash_hmac(   'sha256', // hash function   id, // user or account ID   'secret' // secret key (keep safe!) ); ```  ### Node.js  ```js import { createHmac } from \"crypto\"  createHmac(   \"sha256\", // hash function   'secret' // secret key (keep safe!) ).update(id).digest(\"hex\") // user or account ID ```  ### Ruby  ```ruby OpenSSL::HMAC.hexdigest(   'sha256', # hash function   'secret', # secret key (keep safe!)   id.to_s # user or account ID ) ```  ### Python  ``` import hmac import hashlib  hmac.new(   b'secret', # secret key (keep safe!)   bytes(id, encoding='utf-8'), # user or account ID   digestmod=hashlib.sha256 # hash function ).hexdigest() ```  ## Single page application  You can use our JavaScript snippet inside single page applications.  You should call `journy(\"screen\")` (or `journy(\"pageview\")`) whenever a user in your application transitions to another page. You can do this by listening to router change events. The current page URL will always be resolved using `window.location.href`.  You can trigger events using `journy(\"event\")` whenever you need to.  ### Next.js  We built a demo app with Next.js. You can find the code [here](https://github.com/journy-io/js-sdk-demo-app).  This [component](https://github.com/journy-io/js-sdk-demo-app/blob/main/components/Journy.js) should be a great start.  You can use the `Script` component from Next.js to load the web snippet and call `init`.  Don't forget to listen on route changes. You can use the `useRouter` hook for that.  ### React Router v6  You can use the [`useLocation`](https://reactrouter.com/docs/en/v6/api#uselocation) hook to listen for route changes:  ```js import React, { useEffect } from \"react\"; import { useLocation } from 'react-router-dom';  function App() {   const location = useLocation();    useEffect(() => {     journy(\"screen\", { name: \"name\" });     // or     journy(\"pageview\");   }, [location]);    return (       // ...   ); } ```  ### Vue Router  You can use [`router.afterEach`](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-after-hooks) to listen for route changes:  ```js const router = new VueRouter({ ... });  router.afterEach((to, from) => {   journy(\"screen\", { name: \"name\" });   // or   journy(\"pageview\"); }); ```  Note: We don't accept a page URL argument for `journy(\"pageview\")`. The current page URL will always be resolved using `window.location.href`.  ## TypeScript  We published an [npm package](https://www.npmjs.com/package/@journyio/web-types) with type definitions to enable type-safe usage of our JavaScript snippet. The code and documentation is available on [GitHub](https://github.com/journy-io/web-types).  ## Localhost  By default a site doesn't allow page views from other domains than the registered domain. This makes it difficult to test your tracking implementation locally.  You can enable \"Allow any domain\" in the site settings to disable the domain check.  This will allow you to test the JavaScript snippet with localhost as hostname.  # Backend  The journy.io API is organized around REST. Our API has predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The API is hosted on api.journy.io.  ## Official SDKs  Our SDKs are designed to help you interact with our APIs with less friction. They are written in several different languages and help bridge the gap between your application and journy.io APIs. They take away the need to know the exact URL and HTTP method to use for each API call among other things leaving you more time to focus on making your application.  | Language   | Package                                                                        | Source code                                                                | |------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------| | 💚 Node.js | [npm install @journyio/sdk ](https://www.npmjs.com/package/@journyio/sdk)      | [github.com/journy-io/js-sdk](https://github.com/journy-io/js-sdk)         | | 🐘 PHP     | [composer require journy-io/sdk](https://packagist.org/packages/journy-io/sdk) | [github.com/journy-io/php-sdk](https://github.com/journy-io/php-sdk)       | | 🐍 Python  | [pip install journyio-sdk](https://pypi.org/project/journyio-sdk/)             | [github.com/journy-io/python-sdk](https://github.com/journy-io/python-sdk) | | 💎 Ruby    | Coming soon                                                                    | Coming soon                                                                |  Your favourite programming language not included? [Let us know!](mailto:hi@journy.io)  In the meanwhile, you can use [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) to generate a client for your programming language.  ## Authentication  The journy.io API uses API keys to authenticate requests. You can view and manage your API keys in the [connections screen](https://system.journy.io).  Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  For every request send to the API we expect a header `X-Api-Key` to be set with the API Key.  ## Permissions  When creating an API Key in [the application](https://system.journy.io) you will have the choice to give permissions to an API Key (which you can change later on). These permissions restrict the API Key from different actions. When an API Key tries to perform a certain action it doesn't have the permissions for, you will receive a `401: Unauthorized` response.  ## Rate limiting  To prevent abuse of the API there is a maximum throughput of 1800 requests per minute. If you need a higher throughput, please contact us.  To keep our platform healthy and stable, we'll block API keys that consistently hit our rate limits. Therefore, please consider taking this throughput into account.  In every response the headers `X-RateLimit-Limit` and `X-RateLimit-Remaining` will be set. The `X-RateLimit-Limit`-header will always contain the current limit of requests per minute. The `X-RateLimit-Remaining`-header will always contain the amount of requests you have left in the current sliding window.  💡 The client-side tracking uses different rate limits.  ## Errors  journy.io uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter was omitted). Codes in the 5xx range indicate an error with journy.io's servers (these are rare).  When performing a `POST`- or `PUT`-request with a requestBody, or when including parameters, these parameters and fields will automatically be checked and validated against the API Spec. When any error occurs, you will get a response with an `errors`-field, structured as follows:  ```json {   \"errors\": {     \"parameters\": {       \"header\": {         \"headerParameterName\": \"Describe what's wrong with the header parameter.\",         ...       },       \"query\": {         \"queryParameterName\": \"Describe what's wrong with the query parameter.\",         ...       },       \"path\": {         \"pathParameterName\": \"Describe what's wrong with the path parameter.\",         ...       },     },     \"fields\": {       \"fieldName\": \"Describe what's wrong with the fieldName.\",       \"object.fieldName\": \"Describe what's wrong with the fieldName of the included object.\",        ...     }   } } ```  ## Best practices  ### Track accounts & users immediately on creation  When you create an account in your database, immediately sending data about that account to journy.io helps your team stay in sync. The same goes for users. Call [Upsert account](#operation/upsertAccount) as soon as possible, right after the account is first created in your database.  ### Update account data daily  Not every account is active every day. But, you may have properties on the account that change through background processing. That's why we recommend updating every one of your accounts' data in a recurring daily process. This way, you know that your accounts are updated every day in journy.io.  ## Changelog  ### December 2021  [POST /events](#operation/trackJourneyEvent) will be moved to [POST /track](#operation/trackEvent). [POST /events](#operation/trackJourneyEvent) is deprecated and will be removed in the future.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hi@journy.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_HELPERS_H
#define OAI_HELPERS_H

#include <QByteArray>
#include <QDate>
#include <QDateTime>
#include <QJsonArray>
#include <QJsonObject>
#include <QJsonValue>
#include <QList>
#include <QMap>
#include <QSet>
#include <QVariant>

#include "OAIEnum.h"
#include "OAIHttpFileElement.h"
#include "OAIObject.h"

namespace OpenAPI {

bool setDateTimeFormat(const QString &format);
bool setDateTimeFormat(const Qt::DateFormat &format);

template <typename T>
QString toStringValue(const QList<T> &val);

template <typename T>
QString toStringValue(const QSet<T> &val);

template <typename T>
bool fromStringValue(const QList<QString> &inStr, QList<T> &val);

template <typename T>
bool fromStringValue(const QSet<QString> &inStr, QList<T> &val);

template <typename T>
bool fromStringValue(const QMap<QString, QString> &inStr, QMap<QString, T> &val);

template <typename T>
QJsonValue toJsonValue(const QList<T> &val);

template <typename T>
QJsonValue toJsonValue(const QSet<T> &val);

template <typename T>
QJsonValue toJsonValue(const QMap<QString, T> &val);

template <typename T>
bool fromJsonValue(QList<T> &val, const QJsonValue &jval);

template <typename T>
bool fromJsonValue(QSet<T> &val, const QJsonValue &jval);

template <typename T>
bool fromJsonValue(QMap<QString, T> &val, const QJsonValue &jval);

QString toStringValue(const QString &value);
QString toStringValue(const QDateTime &value);
QString toStringValue(const QByteArray &value);
QString toStringValue(const QDate &value);
QString toStringValue(const qint32 &value);
QString toStringValue(const qint64 &value);
QString toStringValue(const bool &value);
QString toStringValue(const float &value);
QString toStringValue(const double &value);
QString toStringValue(const OAIObject &value);
QString toStringValue(const OAIEnum &value);
QString toStringValue(const OAIHttpFileElement &value);

template <typename T>
QString toStringValue(const QList<T> &val) {
    QString strArray;
    for (const auto &item : val) {
        strArray.append(toStringValue(item) + ",");
    }
    if (val.count() > 0) {
        strArray.chop(1);
    }
    return strArray;
}

template <typename T>
QString toStringValue(const QSet<T> &val) {
    QString strArray;
    for (const auto &item : val) {
        strArray.append(toStringValue(item) + ",");
    }
    if (val.count() > 0) {
        strArray.chop(1);
    }
    return strArray;
}

QJsonValue toJsonValue(const QString &value);
QJsonValue toJsonValue(const QDateTime &value);
QJsonValue toJsonValue(const QByteArray &value);
QJsonValue toJsonValue(const QDate &value);
QJsonValue toJsonValue(const qint32 &value);
QJsonValue toJsonValue(const qint64 &value);
QJsonValue toJsonValue(const bool &value);
QJsonValue toJsonValue(const float &value);
QJsonValue toJsonValue(const double &value);
QJsonValue toJsonValue(const OAIObject &value);
QJsonValue toJsonValue(const OAIEnum &value);
QJsonValue toJsonValue(const OAIHttpFileElement &value);
QJsonValue toJsonValue(const QJsonValue &value);

template <typename T>
QJsonValue toJsonValue(const QList<T> &val) {
    QJsonArray jArray;
    for (const auto &item : val) {
        jArray.append(toJsonValue(item));
    }
    return jArray;
}

template <typename T>
QJsonValue toJsonValue(const QSet<T> &val) {
    QJsonArray jArray;
    for (const auto &item : val) {
        jArray.append(toJsonValue(item));
    }
    return jArray;
}

template <typename T>
QJsonValue toJsonValue(const QMap<QString, T> &val) {
    QJsonObject jObject;
    for (const auto &itemkey : val.keys()) {
        jObject.insert(itemkey, toJsonValue(val.value(itemkey)));
    }
    return jObject;
}

bool fromStringValue(const QString &inStr, QString &value);
bool fromStringValue(const QString &inStr, QDateTime &value);
bool fromStringValue(const QString &inStr, QByteArray &value);
bool fromStringValue(const QString &inStr, QDate &value);
bool fromStringValue(const QString &inStr, qint32 &value);
bool fromStringValue(const QString &inStr, qint64 &value);
bool fromStringValue(const QString &inStr, bool &value);
bool fromStringValue(const QString &inStr, float &value);
bool fromStringValue(const QString &inStr, double &value);
bool fromStringValue(const QString &inStr, OAIObject &value);
bool fromStringValue(const QString &inStr, OAIEnum &value);
bool fromStringValue(const QString &inStr, OAIHttpFileElement &value);

template <typename T>
bool fromStringValue(const QList<QString> &inStr, QList<T> &val) {
    bool ok = (inStr.count() > 0);
    for (const auto &item : inStr) {
        T itemVal;
        ok &= fromStringValue(item, itemVal);
        val.push_back(itemVal);
    }
    return ok;
}

template <typename T>
bool fromStringValue(const QSet<QString> &inStr, QList<T> &val) {
    bool ok = (inStr.count() > 0);
    for (const auto &item : inStr) {
        T itemVal;
        ok &= fromStringValue(item, itemVal);
        val.push_back(itemVal);
    }
    return ok;
}

template <typename T>
bool fromStringValue(const QMap<QString, QString> &inStr, QMap<QString, T> &val) {
    bool ok = (inStr.count() > 0);
    for (const auto &itemkey : inStr.keys()) {
        T itemVal;
        ok &= fromStringValue(inStr.value(itemkey), itemVal);
        val.insert(itemkey, itemVal);
    }
    return ok;
}

bool fromJsonValue(QString &value, const QJsonValue &jval);
bool fromJsonValue(QDateTime &value, const QJsonValue &jval);
bool fromJsonValue(QByteArray &value, const QJsonValue &jval);
bool fromJsonValue(QDate &value, const QJsonValue &jval);
bool fromJsonValue(qint32 &value, const QJsonValue &jval);
bool fromJsonValue(qint64 &value, const QJsonValue &jval);
bool fromJsonValue(bool &value, const QJsonValue &jval);
bool fromJsonValue(float &value, const QJsonValue &jval);
bool fromJsonValue(double &value, const QJsonValue &jval);
bool fromJsonValue(OAIObject &value, const QJsonValue &jval);
bool fromJsonValue(OAIEnum &value, const QJsonValue &jval);
bool fromJsonValue(OAIHttpFileElement &value, const QJsonValue &jval);
bool fromJsonValue(QJsonValue &value, const QJsonValue &jval);

template <typename T>
bool fromJsonValue(QList<T> &val, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isArray()) {
        for (const auto jitem : jval.toArray()) {
            T item;
            ok &= fromJsonValue(item, jitem);
            val.push_back(item);
        }
    } else {
        ok = false;
    }
    return ok;
}

template <typename T>
bool fromJsonValue(QSet<T> &val, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isArray()) {
        for (const auto jitem : jval.toArray()) {
            T item;
            ok &= fromJsonValue(item, jitem);
            val.insert(item);
        }
    } else {
        ok = false;
    }
    return ok;
}

template <typename T>
bool fromJsonValue(QMap<QString, T> &val, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isObject()) {
        auto varmap = jval.toObject().toVariantMap();
        if (varmap.count() > 0) {
            for (const auto &itemkey : varmap.keys()) {
                T itemVal;
                ok &= fromJsonValue(itemVal, QJsonValue::fromVariant(varmap.value(itemkey)));
                val.insert(itemkey, itemVal);
            }
        }
    } else {
        ok = false;
    }
    return ok;
}

template <typename T>
class OptionalParam {
public:
    T m_Value;
    bool m_isNull = false;
    bool m_hasValue;
public:
    OptionalParam(){
        m_hasValue = false;
    }
    OptionalParam(const T &val, bool isNull = false){
        m_hasValue = true;
        m_Value = val;
        m_isNull = isNull;
    }
    bool hasValue() const {
        return m_hasValue;
    }
    T value() const{
        return m_Value;
    }

    QString stringValue() const {
        if (m_isNull) {
            return QStringLiteral("");
        } else {
            return toStringValue(value());
        }
    }
};

} // namespace OpenAPI

#endif // OAI_HELPERS_H
