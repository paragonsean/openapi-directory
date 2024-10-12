/**
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
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
