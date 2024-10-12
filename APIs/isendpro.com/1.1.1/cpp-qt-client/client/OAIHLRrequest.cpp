/**
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHLRrequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHLRrequest::OAIHLRrequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHLRrequest::OAIHLRrequest() {
    this->initializeModel();
}

OAIHLRrequest::~OAIHLRrequest() {}

void OAIHLRrequest::initializeModel() {

    m_get_hlr_isSet = false;
    m_get_hlr_isValid = false;

    m_keyid_isSet = false;
    m_keyid_isValid = false;

    m_num_isSet = false;
    m_num_isValid = false;
}

void OAIHLRrequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHLRrequest::fromJsonObject(QJsonObject json) {

    m_get_hlr_isValid = ::OpenAPI::fromJsonValue(m_get_hlr, json[QString("getHLR")]);
    m_get_hlr_isSet = !json[QString("getHLR")].isNull() && m_get_hlr_isValid;

    m_keyid_isValid = ::OpenAPI::fromJsonValue(m_keyid, json[QString("keyid")]);
    m_keyid_isSet = !json[QString("keyid")].isNull() && m_keyid_isValid;

    m_num_isValid = ::OpenAPI::fromJsonValue(m_num, json[QString("num")]);
    m_num_isSet = !json[QString("num")].isNull() && m_num_isValid;
}

QString OAIHLRrequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHLRrequest::asJsonObject() const {
    QJsonObject obj;
    if (m_get_hlr_isSet) {
        obj.insert(QString("getHLR"), ::OpenAPI::toJsonValue(m_get_hlr));
    }
    if (m_keyid_isSet) {
        obj.insert(QString("keyid"), ::OpenAPI::toJsonValue(m_keyid));
    }
    if (m_num.size() > 0) {
        obj.insert(QString("num"), ::OpenAPI::toJsonValue(m_num));
    }
    return obj;
}

QString OAIHLRrequest::getGetHlr() const {
    return m_get_hlr;
}
void OAIHLRrequest::setGetHlr(const QString &get_hlr) {
    m_get_hlr = get_hlr;
    m_get_hlr_isSet = true;
}

bool OAIHLRrequest::is_get_hlr_Set() const{
    return m_get_hlr_isSet;
}

bool OAIHLRrequest::is_get_hlr_Valid() const{
    return m_get_hlr_isValid;
}

QString OAIHLRrequest::getKeyid() const {
    return m_keyid;
}
void OAIHLRrequest::setKeyid(const QString &keyid) {
    m_keyid = keyid;
    m_keyid_isSet = true;
}

bool OAIHLRrequest::is_keyid_Set() const{
    return m_keyid_isSet;
}

bool OAIHLRrequest::is_keyid_Valid() const{
    return m_keyid_isValid;
}

QList<QString> OAIHLRrequest::getNum() const {
    return m_num;
}
void OAIHLRrequest::setNum(const QList<QString> &num) {
    m_num = num;
    m_num_isSet = true;
}

bool OAIHLRrequest::is_num_Set() const{
    return m_num_isSet;
}

bool OAIHLRrequest::is_num_Valid() const{
    return m_num_isValid;
}

bool OAIHLRrequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_get_hlr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keyid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_num.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHLRrequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_get_hlr_isValid && m_keyid_isValid && m_num_isValid && true;
}

} // namespace OpenAPI
