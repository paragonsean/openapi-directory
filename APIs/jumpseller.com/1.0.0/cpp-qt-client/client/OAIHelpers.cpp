/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include <QDebug>
#include <QJsonParseError>
#include "OAIHelpers.h"

namespace OpenAPI {

class OAISerializerSettings {
public:
    struct CustomDateTimeFormat{
        bool isStringSet = false;
        QString formatString;
        bool isEnumSet = false;
        Qt::DateFormat formatEnum;
    };

    static CustomDateTimeFormat getCustomDateTimeFormat() {
        return getInstance()->customDateTimeFormat;
    }

    static void setDateTimeFormatString(const QString &dtFormat){
        getInstance()->customDateTimeFormat.isStringSet = true;
        getInstance()->customDateTimeFormat.isEnumSet = false;
        getInstance()->customDateTimeFormat.formatString = dtFormat;
    }

    static void setDateTimeFormatEnum(const Qt::DateFormat &dtFormat){
        getInstance()->customDateTimeFormat.isEnumSet = true;
        getInstance()->customDateTimeFormat.isStringSet = false;
        getInstance()->customDateTimeFormat.formatEnum = dtFormat;
    }

    static OAISerializerSettings *getInstance(){
        if(instance == nullptr){
            instance = new OAISerializerSettings();
        }
        return instance;
    }

private:
    explicit OAISerializerSettings(){
        instance = this;
        customDateTimeFormat.isStringSet = false;
        customDateTimeFormat.isEnumSet = false;
    }
    static OAISerializerSettings *instance;
    CustomDateTimeFormat customDateTimeFormat;
};

OAISerializerSettings * OAISerializerSettings::instance = nullptr;

bool setDateTimeFormat(const QString &dateTimeFormat){
    bool success = false;
    auto dt = QDateTime::fromString(QDateTime::currentDateTime().toString(dateTimeFormat), dateTimeFormat);
    if (dt.isValid()) {
        success = true;
        OAISerializerSettings::setDateTimeFormatString(dateTimeFormat);
    }
    return success;
}

bool setDateTimeFormat(const Qt::DateFormat &dateTimeFormat){
    bool success = false;
    auto dt = QDateTime::fromString(QDateTime::currentDateTime().toString(dateTimeFormat), dateTimeFormat);
    if (dt.isValid()) {
        success = true;
        OAISerializerSettings::setDateTimeFormatEnum(dateTimeFormat);
    }
    return success;
}

QString toStringValue(const QString &value) {
    return value;
}

QString toStringValue(const QDateTime &value) {
    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
        return value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
    }

    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
        return value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
    }

    // ISO 8601
    return value.toString(Qt::ISODate);
}

QString toStringValue(const QByteArray &value) {
    return QString(value);
}

QString toStringValue(const QDate &value) {
    // ISO 8601
    return value.toString(Qt::DateFormat::ISODate);
}

QString toStringValue(const qint32 &value) {
    return QString::number(value);
}

QString toStringValue(const qint64 &value) {
    return QString::number(value);
}

QString toStringValue(const bool &value) {
    return QString(value ? "true" : "false");
}

QString toStringValue(const float &value) {
    return QString::number(static_cast<double>(value));
}

QString toStringValue(const double &value) {
    return QString::number(value);
}

QString toStringValue(const OAIObject &value) {
    return value.asJson();
}

QString toStringValue(const OAIEnum &value) {
    return value.asJson();
}

QString toStringValue(const OAIHttpFileElement &value) {
    return value.asJson();
}

QJsonValue toJsonValue(const QString &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const QDateTime &value) {
    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
        return QJsonValue(value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString));
    }

    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
        return QJsonValue(value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum));
    }

    // ISO 8601
    return QJsonValue(value.toString(Qt::ISODate));
}

QJsonValue toJsonValue(const QByteArray &value) {
    return QJsonValue(QString(value.toBase64()));
}

QJsonValue toJsonValue(const QDate &value) {
    return QJsonValue(value.toString(Qt::ISODate));
}

QJsonValue toJsonValue(const qint32 &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const qint64 &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const bool &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const float &value) {
    return QJsonValue(static_cast<double>(value));
}

QJsonValue toJsonValue(const double &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const OAIObject &value) {
    return value.asJsonObject();
}

QJsonValue toJsonValue(const OAIEnum &value) {
    return value.asJsonValue();
}

QJsonValue toJsonValue(const OAIHttpFileElement &value) {
    return value.asJsonValue();
}

QJsonValue toJsonValue(const QJsonValue &value) {
    return value;
}

bool fromStringValue(const QString &inStr, QString &value) {
    value.clear();
    value.append(inStr);
    return !inStr.isEmpty();
}

bool fromStringValue(const QString &inStr, QDateTime &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
       QDateTime dateTime;
        if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
            dateTime = QDateTime::fromString(inStr, OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
        } else if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
            dateTime = QDateTime::fromString(inStr, OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
        } else {
            dateTime = QDateTime::fromString(inStr, Qt::ISODate);
        }

        if (dateTime.isValid()) {
            value.setDate(dateTime.date());
            value.setTime(dateTime.time());
        } else {
            qDebug() << "DateTime is invalid";
        }
        return dateTime.isValid();
    }
}

bool fromStringValue(const QString &inStr, QByteArray &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
        value.clear();
        value.append(inStr.toUtf8());
        return !value.isEmpty();
    }
}

bool fromStringValue(const QString &inStr, QDate &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
        auto date = QDate::fromString(inStr, Qt::DateFormat::ISODate);
        if (date.isValid()) {
            value.setDate(date.year(), date.month(), date.day());
        } else {
            qDebug() << "Date is invalid";
        }
        return date.isValid();
    }
}

bool fromStringValue(const QString &inStr, qint32 &value) {
    bool ok = false;
    value = QVariant(inStr).toInt(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, qint64 &value) {
    bool ok = false;
    value = QVariant(inStr).toLongLong(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, bool &value) {
    value = QVariant(inStr).toBool();
    return ((inStr == "true") || (inStr == "false"));
}

bool fromStringValue(const QString &inStr, float &value) {
    bool ok = false;
    value = QVariant(inStr).toFloat(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, double &value) {
    bool ok = false;
    value = QVariant(inStr).toDouble(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, OAIObject &value)
{
    QJsonParseError err;
    QJsonDocument::fromJson(inStr.toUtf8(),&err);
    if ( err.error == QJsonParseError::NoError ){
        value.fromJson(inStr);
        return true;
    }
    return false;
}

bool fromStringValue(const QString &inStr, OAIEnum &value) {
    value.fromJson(inStr);
    return true;
}

bool fromStringValue(const QString &inStr, OAIHttpFileElement &value) {
    return value.fromStringValue(inStr);
}

bool fromJsonValue(QString &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull()) {
        if (jval.isString()) {
            value = jval.toString();
        } else if (jval.isBool()) {
            value = jval.toBool() ? "true" : "false";
        } else if (jval.isDouble()) {
            value = QString::number(jval.toDouble());
        } else {
            ok = false;
        }
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QDateTime &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
            value = QDateTime::fromString(jval.toString(), OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
        } else if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
            value = QDateTime::fromString(jval.toString(), OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
        } else {
            value = QDateTime::fromString(jval.toString(), Qt::ISODate);
        }
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QByteArray &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        value = QByteArray::fromBase64(QByteArray::fromStdString(jval.toString().toStdString()));
        ok = value.size() > 0;
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QDate &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        value = QDate::fromString(jval.toString(), Qt::ISODate);
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(qint32 &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && !jval.isObject() && !jval.isArray()) {
        value = jval.toInt();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(qint64 &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && !jval.isObject() && !jval.isArray()) {
        value = jval.toVariant().toLongLong();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(bool &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isBool()) {
        value = jval.toBool();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(float &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isDouble()) {
        value = static_cast<float>(jval.toDouble());
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(double &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isDouble()) {
        value = jval.toDouble();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(OAIObject &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isObject()) {
        value.fromJsonObject(jval.toObject());
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(OAIEnum &value, const QJsonValue &jval) {
    value.fromJsonValue(jval);
    return true;
}

bool fromJsonValue(OAIHttpFileElement &value, const QJsonValue &jval) {
    return value.fromJsonValue(jval);
}

bool fromJsonValue(QJsonValue &value, const QJsonValue &jval) {
    value = jval;
    return true;
}

} // namespace OpenAPI
