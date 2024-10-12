/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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
