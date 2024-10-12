/**
 * FRC Events
 * <html><head></head><body><h1 id=\"overview\">Overview</h1> <p><em>FIRST</em>/FMS FRC Events API is a service to return relevant information about the <em>FIRST</em> Robotics Competition (FRC). Information is made available from events operating around the world.</p> <p>For FRC, information is made available by the Field Management System (FMS) server operating at each event site. The FMS will attempt to sync all data from the event to \"the cloud\" as long as internet is available at the venue. If internet is unavailable, or \"goes down\" during the event, the FMS will automatically sync all data from the time the system was offline as soon as the connection is restored. The API will provide data as soon as it has synced, and we do not add any artificial delays. If you are receiving \"stale\" data, it may be because of connectivity problems at the venue. We recommend you try again later, and post on the FIRST FMS TeamForge site if the problem persists. <em>(Note: FMS does not sync while a match is running, so data that has to do with a particular match should become available once the score has been revealed to the audience at the event.)</em></p> <h3 id=\"migration-and-program-notes\">Migration and Program Notes:</h3> <p>Pay close attention to the addresses for calling the various endpoints- as well as the notes regarding endpoints with multiple possible responses (i.e. score details and rankings).</p> <h1 id=\"documentation-notes\">Documentation Notes</h1> <p>All times are listed in the local time to the event venue. HTTP-date values will show their timezone.</p> <p>If you specify a parameter, but no value for that parameter, it will be ignored. For example, if you request <strong>URL?teamNumber=</strong> the <strong>teamNumber</strong> parameter would be ignored.</p> <p>We will continue to support the current version of the API plus one version older. Old APIs are depricated once a version \"two times newer\" is available, at minimum 6 months. For example, version 2.0 and 1.0 are supported right now, but 1.0 will not be supported once 2.1 (or 3.0) is available. Versions may also be retired earlier with prior notice here in the documentation.</p> <p>The full host address of the API is needed in all calls. The version number is required in each call in order to ensure your requests are made (and responses are returned) in the formats you anticipate. The version number for this documentation is found on the top of the page, in the title. If you call this version number, the API responses will match the formats listed below.</p> <p>All of the APIs are capable of accepting the <strong>Accept</strong> HTTP header with either <strong>application/xml</strong> or <strong>application/json</strong> based on the desired return type. Any API call that results in an <strong>HTTP Status Code</strong> other than <strong>200 (OK)</strong> will only be shown here as an <strong>application/json</strong> response to save space, but the content is the same regardless of the request type. All response will have a <strong>Content-Length</strong> and <strong>Date</strong> response header, but those are not shown in the documentaiton.</p> <p>For all APIs that accept a query string in addition to the URI base, the order of parameters do not matter, but the name shown in the documentation must match exactly, as does the associated value format as described in details.</p> <p>For response codes that are not <strong>HTTP 200 (OK)</strong>, the documentation will show a body message that represents a possible response value. While the \"title\" of the <strong>HTTP Status Code</strong> will match those shown in the response codes documentation section exactly, the body of the response will be a more detailed explanation of why that status code is being returned and may not always be exactly as shown in the examples.</p> <p>None of the APIs will show possible return here in the documentation of <strong>HTTP 401 (Unauthorized)</strong>, but that code applies to all APIs as a possible response if the request is made without a valid token.</p> <h3 id=\"last-modified-fms-onlymodifiedsince-and-if-modified-since-headers\">Last-Modified, FMS-OnlyModifiedSince, and If-Modified-Since Headers</h3> <p>The FRC Events API utilizes the <strong>Last-Modified</strong> and <strong>If-Modified-Since</strong> Headers to communicate with consumers regarding the age of the data they are requesting. With a couple of exceptions, all calls will return a <strong>Last-Modified</strong> Header set with the time at which the data at that endpoint was last modified. The Header will always be set in the HTTP-date format, as described in the <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\">HTTP Protocol</a>. There are two exceptions: the <strong>Last-Modified</strong> Header is not set if the endpoint returns no results (such as a request for a schedule with no matches) and will also not be set if the request was an <strong>HTTP DELETE</strong>.</p> <p>Consumers should keep track of the <strong>Last-Modified</strong> Header, and return it on subsequent calls to the same endpoint as the <strong>If-Modified-Since</strong>. The server will recognize this request, and will only return a result if the data has been modified since the last request. If no changes have been made, an <strong>HTTP 304</strong> will be returned. If data has been modified, ALL data on that call will be returned (for \"only modified\" data, see below).</p> <p>The FRC Events API also allows a custom header used to filter the return data to a specific subset. This is done by specifying a <strong>FMS-OnlyModifiedSince</strong> header with each call. As with the <strong>If-Modified-Since</strong> header, consumers should keep track of the <strong>Last-Modified</strong> Header, and return it on subsequent calls to the same endpoint as the <strong>FMS-OnlyModifiedSince</strong> Header. The server will recognize this request, and will only return a result if the data has been modified since the last request, and, if returned, the data will only be those portions modified since the included date. If no changes, have been made, an <strong>HTTP 304</strong> will be returned. Using this method, the server and consumer save processing time by only receiving modified data that is in need of update on the consumer side.</p> <p>If the Headers are improperly passed (such as the wrong Day of Week for the matching date, or a date in the future), the endpoint will simply ignore the Header and return all results. If both headers are specified, the request will be denied.</p> <h1 id=\"response-codes\">Response Codes</h1> <p>The FRC Events API HTTP Status Codes correspond with the <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html\">common codes</a>, but occasionally with different \"titles\". The \"title\" used by the API is shown next to each of the below possible response HTTP Status Codes. Throughout the documentation, Apiary may automatically show the common \"title\" in example returns (like \"Not Found\" for 404) but on the production server, the \"title\" will instead match those listed below.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 200 - \"OK\" </code></pre><p>The request has succeeded. An entity corresponding to the requested resource is sent in the response. This will be returned as the HTTP Status Code for all request that succeed, even if the body is empty (such as an event that has no rankings, but with a valid season and event code were used)</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 304 - \"Not Modified\" </code></pre><p>When utilizing a Header that allows filtered data returns, such as <strong>If-Modified-Since</strong>, this response indicates that no data meets the request.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 400 - \"Invalid Season Requested\"/\"Malformed Parameter Format In Request\"/\"Missing Parameter In Request\"/\"Invalid API Version Requested\": </code></pre><p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. Specifically for this API, a 400 response indicates that the requested URI matches with a valid API, but one or more required parameter was malformed or invalid. Examples include an event code that is too short or team number that contains a letter.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 401 - \"Unauthorized\" </code></pre><p>All requests against the API require authentication via a valid user token. Failing to provide one, or providing an invalid one, will warrant a 401 response. The client MAY repeat the request with a suitable Authorization header field.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 404 - \"Invalid Event Requested\" </code></pre><p>Even though the 404 code usually indicates any not found status, a 404 will only be issued in this API when an event cannot be found for the requested season and event code. If the request didn't match a valid API or there were malformed parameters, the response would not receive a 404 but rather a 400 or 501. If this HTTP code is received, the season was a valid season and the event code matched the acceptable style of an event code, but there were no records of an event matching the combination of that season and event code. For example, HTTP 404 would be issued when the event had a different code in the requested season (the codes can change year to year based on event location).</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 500 - \"Internal Server Error\" </code></pre><p>The server encountered an unexpected condition which prevented it from fulfilling the request. This is a code sent directly by the server, and has no special alternate definition specific to this API.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 501 - \"Request Did Not Match Any Current API Pattern\" </code></pre><p>The server does not support the functionality required to fulfill the request. Specifically, the request pattern did not match any of the possible APIs, and thus processing was discontinued. This code is also issued when too many optional parameters were included in a single request and fulfilling it would make the result confusing or misleading. Each API will specify which parameters or combination of parameters can be used at the same time.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code>HTTP 503 - \"Service Unavailable\" </code></pre><p>The server is currently unable to handle the request due to a temporary overloading or maintenance of the server. The implication is that this is a temporary condition which will be alleviated after some delay. If known, the length of the delay MAY be indicated in a Retry-After header. This code will not always appear, sometimes the server may outright refuse the connection instead. This is a code sent directly by the server, and has no special alternate definition specific to this API.</p> <p>See the notes at the top of this documentation for important information about HTTP Status Codes.</p> <h1 id=\"authorization\">Authorization</h1> <p>In order to make calls against the FRC Events API, you must include an HTTP Header called <strong>Authorization</strong> with the value set as specified below. If a request is made without this header, processing stops and an <strong>HTTP 401</strong> is issued. All <strong>Authorization</strong> headers follow the same format:</p> <p>Authorization: Basic 000000000000000000000000000000000000000000000000000000000000</p> <p>Where the Zeros are replaced by your Token. The Token can be formed by taking your <strong>username</strong> and your <strong>AuthorizationKey</strong> and adding a colon. For example, if your <strong>username</strong> is sampleuser and your <strong>AuthorizationKey</strong> is 7eaa6338-a097-4221-ac04-b6120fcc4d49 you would have this string:</p> <p><strong>sampleuser:7eaa6338-a097-4221-ac04-b6120fcc4d49</strong></p> <p>This string must then be encoded using Base64 Encoded to form the Token, which will be the same length as the example above, but include letters and numbers. For our example, we would have:</p> <p>c2FtcGxldXNlcjo3ZWFhNjMzOC1hMDk3LTQyMjEtYWMwNC1iNjEyMGZjYzRkNDk=</p> <p><strong>NOTICE</strong>: Publicly distributing an application, code snippet, etc, that has your username and token in it, encoded or not, WILL result in your token being blocked from the API. Each user should apply for their own token.</p> <p>If you wish to acquire a token for your development, you may do so by requesting a token through our automated system on <a href=\"https://frc-events.firstinspires.org/services/API\">this website</a>.</p> <p><strong>AUTOMATED REMOVAL</strong>: If you do not activate your account within 72 hours of making your request for a token, or if you do not make at least one API request every twelve (12) months, your account/token will be marked as disabled for inactivity and subject to being deleted. (This policy does not apply to accounts with special operating agreements with FIRST)</p> <h3 id=\"http401-and-authorization\">HTTP401 and Authorization</h3> <p>Each Token can be individually enabled and disabled by <em>FIRST</em>. As such, a normally valid combination of <strong>username</strong> and <strong>AuthorizationToken</strong> could still be rejected. The possible return messages you may see in these instances are:</p> <p><strong>Incorrect Token</strong> (You supplied an AuthorizationToken, but it wasn't correct)</p> <p><strong>Account Disabled, Contact Support</strong> (You have been disabled for excessive traffic or abuse. Contact support)</p> <p><strong>Username Not Found</strong> (A username was found, but didn't match any on file)</p> <p><strong>Unable To Determine Authorization Token</strong> (The format of the <strong>Authorization</strong> header was incorrect)</p> </body></html>
 *
 * The version of the OpenAPI document: 1.0.0
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
