/**
 * GlobalWineScore API Documentation
 *   The GlobalWineScore API is designed as a RESTful API, providing several resources and methods depending on your usage plan.  For further information please refer to <a href=\"https://www.globalwinescore.com/plans\" target=\"_blank\">our plans</a>.  # Authentication The API uses token-based authentication. In order to authenticate your requests, you need to include a specific header in each of your requests:  ``` Authorization: Token {YOUR-API-TOKEN} ``` The word <b>Token</b> must be written. Your requests must also use the <b>HTTPS</b> protocol.  If you don't have a token yet, you need to apply for one [here](https://www.globalwinescore.com/api/).  Your personal token can be found under the <a href=\"https://www.globalwinescore.com/account/api/\" target=\"_blank\">My account > API</a> section of the GlobalWineScore website  # Format The API provides several rendering formats which you can control using the `Accept` header or `format` query parameter.  - JSON (default): no header or `Accept: application/json` - XML: `Accept: application/xml` # Rate limiting For API requests, the rate limit allows for up to 10 requests per minute.  # Error handling  Whether a request succeeded is indicated by the HTTP status code. A 2xx status code indicates success, whereas a 4xx status code indicates failure.  When a request fails, the response body is still JSON, but always contains a `detail` field with a description of the error, which you can inspect for debugging.  For example, trying to access the API without proper authentication will return code 403 along with the message:  `{\"detail\": \"Authentication credentials were not provided.\"}`  Found a bug ? send us an email at <a href=\"mailto:api@globalwinescore.com\">api@globalwinescore.com</a>  # Ordering  At the moment, GlobalWineScores may be sorted by `date` and `score`. Use \"-\" to sort in descending order.  # Continuous synchronization  If you need to synchronize your database with our API, you can query our API using `?ordering=-date` to get the newest scores first, which means you won't have to crawl the whole catalog every time :-)  # Quick search interface If you need to search our catalog (e.g. to align it with yours), we're providing you with a handy interface accessible here: <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">https://api.globalwinescore.com/search/</a>  You need to be logged in (email/password) to access this page, but other than that you can share it with anyone in your team and start searching right away !  # Resources  The details about available endpoints can be found below. You can click on each endpoint to find information about their parameters. 
 *
 * The version of the OpenAPI document: 8234aab51481d37a30757d925b7f4221a659427e
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
