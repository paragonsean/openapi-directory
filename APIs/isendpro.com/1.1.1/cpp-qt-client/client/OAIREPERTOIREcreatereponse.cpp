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

#include "OAIREPERTOIREcreatereponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIREPERTOIREcreatereponse::OAIREPERTOIREcreatereponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIREPERTOIREcreatereponse::OAIREPERTOIREcreatereponse() {
    this->initializeModel();
}

OAIREPERTOIREcreatereponse::~OAIREPERTOIREcreatereponse() {}

void OAIREPERTOIREcreatereponse::initializeModel() {

    m_etat_isSet = false;
    m_etat_isValid = false;
}

void OAIREPERTOIREcreatereponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIREPERTOIREcreatereponse::fromJsonObject(QJsonObject json) {

    m_etat_isValid = ::OpenAPI::fromJsonValue(m_etat, json[QString("etat")]);
    m_etat_isSet = !json[QString("etat")].isNull() && m_etat_isValid;
}

QString OAIREPERTOIREcreatereponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIREPERTOIREcreatereponse::asJsonObject() const {
    QJsonObject obj;
    if (m_etat.isSet()) {
        obj.insert(QString("etat"), ::OpenAPI::toJsonValue(m_etat));
    }
    return obj;
}

OAIREPERTOIREcreatereponse_etat OAIREPERTOIREcreatereponse::getEtat() const {
    return m_etat;
}
void OAIREPERTOIREcreatereponse::setEtat(const OAIREPERTOIREcreatereponse_etat &etat) {
    m_etat = etat;
    m_etat_isSet = true;
}

bool OAIREPERTOIREcreatereponse::is_etat_Set() const{
    return m_etat_isSet;
}

bool OAIREPERTOIREcreatereponse::is_etat_Valid() const{
    return m_etat_isValid;
}

bool OAIREPERTOIREcreatereponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_etat.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIREPERTOIREcreatereponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
