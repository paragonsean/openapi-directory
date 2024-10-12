/**
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
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
