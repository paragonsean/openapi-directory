/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPriceJO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPriceJO::OAIPriceJO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPriceJO::OAIPriceJO() {
    this->initializeModel();
}

OAIPriceJO::~OAIPriceJO() {}

void OAIPriceJO::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_expand_isSet = false;
    m_expand_isValid = false;

    m_grossamount_isSet = false;
    m_grossamount_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_interval_isSet = false;
    m_interval_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_preferredprice_isSet = false;
    m_preferredprice_isValid = false;

    m_taxrate_isSet = false;
    m_taxrate_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_uid_isSet = false;
    m_uid_isValid = false;
}

void OAIPriceJO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPriceJO::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_expand_isValid = ::OpenAPI::fromJsonValue(m_expand, json[QString("expand")]);
    m_expand_isSet = !json[QString("expand")].isNull() && m_expand_isValid;

    m_grossamount_isValid = ::OpenAPI::fromJsonValue(m_grossamount, json[QString("grossamount")]);
    m_grossamount_isSet = !json[QString("grossamount")].isNull() && m_grossamount_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_interval_isValid = ::OpenAPI::fromJsonValue(m_interval, json[QString("interval")]);
    m_interval_isSet = !json[QString("interval")].isNull() && m_interval_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_preferredprice_isValid = ::OpenAPI::fromJsonValue(m_preferredprice, json[QString("preferredprice")]);
    m_preferredprice_isSet = !json[QString("preferredprice")].isNull() && m_preferredprice_isValid;

    m_taxrate_isValid = ::OpenAPI::fromJsonValue(m_taxrate, json[QString("taxrate")]);
    m_taxrate_isSet = !json[QString("taxrate")].isNull() && m_taxrate_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_uid_isValid = ::OpenAPI::fromJsonValue(m_uid, json[QString("uid")]);
    m_uid_isSet = !json[QString("uid")].isNull() && m_uid_isValid;
}

QString OAIPriceJO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPriceJO::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_attributes.size() > 0) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_expand_isSet) {
        obj.insert(QString("expand"), ::OpenAPI::toJsonValue(m_expand));
    }
    if (m_grossamount_isSet) {
        obj.insert(QString("grossamount"), ::OpenAPI::toJsonValue(m_grossamount));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_interval_isSet) {
        obj.insert(QString("interval"), ::OpenAPI::toJsonValue(m_interval));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_preferredprice_isSet) {
        obj.insert(QString("preferredprice"), ::OpenAPI::toJsonValue(m_preferredprice));
    }
    if (m_taxrate_isSet) {
        obj.insert(QString("taxrate"), ::OpenAPI::toJsonValue(m_taxrate));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_uid_isSet) {
        obj.insert(QString("uid"), ::OpenAPI::toJsonValue(m_uid));
    }
    return obj;
}

QList<OAILinkJO> OAIPriceJO::getLinks() const {
    return m__links;
}
void OAIPriceJO::setLinks(const QList<OAILinkJO> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIPriceJO::is__links_Set() const{
    return m__links_isSet;
}

bool OAIPriceJO::is__links_Valid() const{
    return m__links_isValid;
}

QMap<QString, OAIObject> OAIPriceJO::getAttributes() const {
    return m_attributes;
}
void OAIPriceJO::setAttributes(const QMap<QString, OAIObject> &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAIPriceJO::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAIPriceJO::is_attributes_Valid() const{
    return m_attributes_isValid;
}

QString OAIPriceJO::getCurrency() const {
    return m_currency;
}
void OAIPriceJO::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIPriceJO::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIPriceJO::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIPriceJO::getDescription() const {
    return m_description;
}
void OAIPriceJO::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPriceJO::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPriceJO::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIPriceJO::getExpand() const {
    return m_expand;
}
void OAIPriceJO::setExpand(const QString &expand) {
    m_expand = expand;
    m_expand_isSet = true;
}

bool OAIPriceJO::is_expand_Set() const{
    return m_expand_isSet;
}

bool OAIPriceJO::is_expand_Valid() const{
    return m_expand_isValid;
}

double OAIPriceJO::getGrossamount() const {
    return m_grossamount;
}
void OAIPriceJO::setGrossamount(const double &grossamount) {
    m_grossamount = grossamount;
    m_grossamount_isSet = true;
}

bool OAIPriceJO::is_grossamount_Set() const{
    return m_grossamount_isSet;
}

bool OAIPriceJO::is_grossamount_Valid() const{
    return m_grossamount_isValid;
}

QString OAIPriceJO::getHref() const {
    return m_href;
}
void OAIPriceJO::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIPriceJO::is_href_Set() const{
    return m_href_isSet;
}

bool OAIPriceJO::is_href_Valid() const{
    return m_href_isValid;
}

qint32 OAIPriceJO::getInterval() const {
    return m_interval;
}
void OAIPriceJO::setInterval(const qint32 &interval) {
    m_interval = interval;
    m_interval_isSet = true;
}

bool OAIPriceJO::is_interval_Set() const{
    return m_interval_isSet;
}

bool OAIPriceJO::is_interval_Valid() const{
    return m_interval_isValid;
}

QString OAIPriceJO::getName() const {
    return m_name;
}
void OAIPriceJO::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPriceJO::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPriceJO::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIPriceJO::isPreferredprice() const {
    return m_preferredprice;
}
void OAIPriceJO::setPreferredprice(const bool &preferredprice) {
    m_preferredprice = preferredprice;
    m_preferredprice_isSet = true;
}

bool OAIPriceJO::is_preferredprice_Set() const{
    return m_preferredprice_isSet;
}

bool OAIPriceJO::is_preferredprice_Valid() const{
    return m_preferredprice_isValid;
}

double OAIPriceJO::getTaxrate() const {
    return m_taxrate;
}
void OAIPriceJO::setTaxrate(const double &taxrate) {
    m_taxrate = taxrate;
    m_taxrate_isSet = true;
}

bool OAIPriceJO::is_taxrate_Set() const{
    return m_taxrate_isSet;
}

bool OAIPriceJO::is_taxrate_Valid() const{
    return m_taxrate_isValid;
}

QString OAIPriceJO::getType() const {
    return m_type;
}
void OAIPriceJO::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPriceJO::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPriceJO::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIPriceJO::getUid() const {
    return m_uid;
}
void OAIPriceJO::setUid(const QString &uid) {
    m_uid = uid;
    m_uid_isSet = true;
}

bool OAIPriceJO::is_uid_Set() const{
    return m_uid_isSet;
}

bool OAIPriceJO::is_uid_Valid() const{
    return m_uid_isValid;
}

bool OAIPriceJO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_attributes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expand_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_grossamount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preferredprice_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxrate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPriceJO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
