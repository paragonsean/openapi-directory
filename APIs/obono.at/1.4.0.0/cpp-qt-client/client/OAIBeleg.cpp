/**
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBeleg.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBeleg::OAIBeleg(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBeleg::OAIBeleg() {
    this->initializeModel();
}

OAIBeleg::~OAIBeleg() {}

void OAIBeleg::initializeModel() {

    m_beleg_codes_isSet = false;
    m_beleg_codes_isValid = false;

    m_beleg_typen_isSet = false;
    m_beleg_typen_isValid = false;

    m_belegdaten_isSet = false;
    m_belegdaten_isValid = false;

    m_jws_isSet = false;
    m_jws_isValid = false;

    m_qr_isSet = false;
    m_qr_isValid = false;

    m_qr_link_isSet = false;
    m_qr_link_isValid = false;

    m_registrierkasse_uuid_isSet = false;
    m_registrierkasse_uuid_isValid = false;

    m_signaturerstellungseinheit_uuid_isSet = false;
    m_signaturerstellungseinheit_uuid_isValid = false;

    m__href_isSet = false;
    m__href_isValid = false;

    m__uuid_isSet = false;
    m__uuid_isValid = false;
}

void OAIBeleg::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBeleg::fromJsonObject(QJsonObject json) {

    m_beleg_codes_isValid = ::OpenAPI::fromJsonValue(m_beleg_codes, json[QString("Beleg-Codes")]);
    m_beleg_codes_isSet = !json[QString("Beleg-Codes")].isNull() && m_beleg_codes_isValid;

    m_beleg_typen_isValid = ::OpenAPI::fromJsonValue(m_beleg_typen, json[QString("Beleg-Typen")]);
    m_beleg_typen_isSet = !json[QString("Beleg-Typen")].isNull() && m_beleg_typen_isValid;

    m_belegdaten_isValid = ::OpenAPI::fromJsonValue(m_belegdaten, json[QString("Belegdaten")]);
    m_belegdaten_isSet = !json[QString("Belegdaten")].isNull() && m_belegdaten_isValid;

    m_jws_isValid = ::OpenAPI::fromJsonValue(m_jws, json[QString("JWS")]);
    m_jws_isSet = !json[QString("JWS")].isNull() && m_jws_isValid;

    m_qr_isValid = ::OpenAPI::fromJsonValue(m_qr, json[QString("QR")]);
    m_qr_isSet = !json[QString("QR")].isNull() && m_qr_isValid;

    m_qr_link_isValid = ::OpenAPI::fromJsonValue(m_qr_link, json[QString("QR-Link")]);
    m_qr_link_isSet = !json[QString("QR-Link")].isNull() && m_qr_link_isValid;

    m_registrierkasse_uuid_isValid = ::OpenAPI::fromJsonValue(m_registrierkasse_uuid, json[QString("Registrierkasse-UUID")]);
    m_registrierkasse_uuid_isSet = !json[QString("Registrierkasse-UUID")].isNull() && m_registrierkasse_uuid_isValid;

    m_signaturerstellungseinheit_uuid_isValid = ::OpenAPI::fromJsonValue(m_signaturerstellungseinheit_uuid, json[QString("Signaturerstellungseinheit-UUID")]);
    m_signaturerstellungseinheit_uuid_isSet = !json[QString("Signaturerstellungseinheit-UUID")].isNull() && m_signaturerstellungseinheit_uuid_isValid;

    m__href_isValid = ::OpenAPI::fromJsonValue(m__href, json[QString("_href")]);
    m__href_isSet = !json[QString("_href")].isNull() && m__href_isValid;

    m__uuid_isValid = ::OpenAPI::fromJsonValue(m__uuid, json[QString("_uuid")]);
    m__uuid_isSet = !json[QString("_uuid")].isNull() && m__uuid_isValid;
}

QString OAIBeleg::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBeleg::asJsonObject() const {
    QJsonObject obj;
    if (m_beleg_codes.size() > 0) {
        obj.insert(QString("Beleg-Codes"), ::OpenAPI::toJsonValue(m_beleg_codes));
    }
    if (m_beleg_typen.size() > 0) {
        obj.insert(QString("Beleg-Typen"), ::OpenAPI::toJsonValue(m_beleg_typen));
    }
    if (m_belegdaten.isSet()) {
        obj.insert(QString("Belegdaten"), ::OpenAPI::toJsonValue(m_belegdaten));
    }
    if (m_jws_isSet) {
        obj.insert(QString("JWS"), ::OpenAPI::toJsonValue(m_jws));
    }
    if (m_qr_isSet) {
        obj.insert(QString("QR"), ::OpenAPI::toJsonValue(m_qr));
    }
    if (m_qr_link_isSet) {
        obj.insert(QString("QR-Link"), ::OpenAPI::toJsonValue(m_qr_link));
    }
    if (m_registrierkasse_uuid_isSet) {
        obj.insert(QString("Registrierkasse-UUID"), ::OpenAPI::toJsonValue(m_registrierkasse_uuid));
    }
    if (m_signaturerstellungseinheit_uuid_isSet) {
        obj.insert(QString("Signaturerstellungseinheit-UUID"), ::OpenAPI::toJsonValue(m_signaturerstellungseinheit_uuid));
    }
    if (m__href_isSet) {
        obj.insert(QString("_href"), ::OpenAPI::toJsonValue(m__href));
    }
    if (m__uuid_isSet) {
        obj.insert(QString("_uuid"), ::OpenAPI::toJsonValue(m__uuid));
    }
    return obj;
}

QList<QString> OAIBeleg::getBelegCodes() const {
    return m_beleg_codes;
}
void OAIBeleg::setBelegCodes(const QList<QString> &beleg_codes) {
    m_beleg_codes = beleg_codes;
    m_beleg_codes_isSet = true;
}

bool OAIBeleg::is_beleg_codes_Set() const{
    return m_beleg_codes_isSet;
}

bool OAIBeleg::is_beleg_codes_Valid() const{
    return m_beleg_codes_isValid;
}

QList<QString> OAIBeleg::getBelegTypen() const {
    return m_beleg_typen;
}
void OAIBeleg::setBelegTypen(const QList<QString> &beleg_typen) {
    m_beleg_typen = beleg_typen;
    m_beleg_typen_isSet = true;
}

bool OAIBeleg::is_beleg_typen_Set() const{
    return m_beleg_typen_isSet;
}

bool OAIBeleg::is_beleg_typen_Valid() const{
    return m_beleg_typen_isValid;
}

OAISignierteBelegdaten OAIBeleg::getBelegdaten() const {
    return m_belegdaten;
}
void OAIBeleg::setBelegdaten(const OAISignierteBelegdaten &belegdaten) {
    m_belegdaten = belegdaten;
    m_belegdaten_isSet = true;
}

bool OAIBeleg::is_belegdaten_Set() const{
    return m_belegdaten_isSet;
}

bool OAIBeleg::is_belegdaten_Valid() const{
    return m_belegdaten_isValid;
}

QString OAIBeleg::getJws() const {
    return m_jws;
}
void OAIBeleg::setJws(const QString &jws) {
    m_jws = jws;
    m_jws_isSet = true;
}

bool OAIBeleg::is_jws_Set() const{
    return m_jws_isSet;
}

bool OAIBeleg::is_jws_Valid() const{
    return m_jws_isValid;
}

QString OAIBeleg::getQr() const {
    return m_qr;
}
void OAIBeleg::setQr(const QString &qr) {
    m_qr = qr;
    m_qr_isSet = true;
}

bool OAIBeleg::is_qr_Set() const{
    return m_qr_isSet;
}

bool OAIBeleg::is_qr_Valid() const{
    return m_qr_isValid;
}

QString OAIBeleg::getQrLink() const {
    return m_qr_link;
}
void OAIBeleg::setQrLink(const QString &qr_link) {
    m_qr_link = qr_link;
    m_qr_link_isSet = true;
}

bool OAIBeleg::is_qr_link_Set() const{
    return m_qr_link_isSet;
}

bool OAIBeleg::is_qr_link_Valid() const{
    return m_qr_link_isValid;
}

QString OAIBeleg::getRegistrierkasseUuid() const {
    return m_registrierkasse_uuid;
}
void OAIBeleg::setRegistrierkasseUuid(const QString &registrierkasse_uuid) {
    m_registrierkasse_uuid = registrierkasse_uuid;
    m_registrierkasse_uuid_isSet = true;
}

bool OAIBeleg::is_registrierkasse_uuid_Set() const{
    return m_registrierkasse_uuid_isSet;
}

bool OAIBeleg::is_registrierkasse_uuid_Valid() const{
    return m_registrierkasse_uuid_isValid;
}

QString OAIBeleg::getSignaturerstellungseinheitUuid() const {
    return m_signaturerstellungseinheit_uuid;
}
void OAIBeleg::setSignaturerstellungseinheitUuid(const QString &signaturerstellungseinheit_uuid) {
    m_signaturerstellungseinheit_uuid = signaturerstellungseinheit_uuid;
    m_signaturerstellungseinheit_uuid_isSet = true;
}

bool OAIBeleg::is_signaturerstellungseinheit_uuid_Set() const{
    return m_signaturerstellungseinheit_uuid_isSet;
}

bool OAIBeleg::is_signaturerstellungseinheit_uuid_Valid() const{
    return m_signaturerstellungseinheit_uuid_isValid;
}

QString OAIBeleg::getHref() const {
    return m__href;
}
void OAIBeleg::setHref(const QString &_href) {
    m__href = _href;
    m__href_isSet = true;
}

bool OAIBeleg::is__href_Set() const{
    return m__href_isSet;
}

bool OAIBeleg::is__href_Valid() const{
    return m__href_isValid;
}

QString OAIBeleg::getUuid() const {
    return m__uuid;
}
void OAIBeleg::setUuid(const QString &_uuid) {
    m__uuid = _uuid;
    m__uuid_isSet = true;
}

bool OAIBeleg::is__uuid_Set() const{
    return m__uuid_isSet;
}

bool OAIBeleg::is__uuid_Valid() const{
    return m__uuid_isValid;
}

bool OAIBeleg::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_beleg_codes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_beleg_typen.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_belegdaten.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_jws_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qr_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_registrierkasse_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_signaturerstellungseinheit_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__uuid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBeleg::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
