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

#include "OAISubaccountAddResponse_etat.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubaccountAddResponse_etat::OAISubaccountAddResponse_etat(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubaccountAddResponse_etat::OAISubaccountAddResponse_etat() {
    this->initializeModel();
}

OAISubaccountAddResponse_etat::~OAISubaccountAddResponse_etat() {}

void OAISubaccountAddResponse_etat::initializeModel() {

    m_etat_isSet = false;
    m_etat_isValid = false;
}

void OAISubaccountAddResponse_etat::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubaccountAddResponse_etat::fromJsonObject(QJsonObject json) {

    m_etat_isValid = ::OpenAPI::fromJsonValue(m_etat, json[QString("etat")]);
    m_etat_isSet = !json[QString("etat")].isNull() && m_etat_isValid;
}

QString OAISubaccountAddResponse_etat::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubaccountAddResponse_etat::asJsonObject() const {
    QJsonObject obj;
    if (m_etat.size() > 0) {
        obj.insert(QString("etat"), ::OpenAPI::toJsonValue(m_etat));
    }
    return obj;
}

QList<OAISubaccountAddResponse_etat_etat_inner> OAISubaccountAddResponse_etat::getEtat() const {
    return m_etat;
}
void OAISubaccountAddResponse_etat::setEtat(const QList<OAISubaccountAddResponse_etat_etat_inner> &etat) {
    m_etat = etat;
    m_etat_isSet = true;
}

bool OAISubaccountAddResponse_etat::is_etat_Set() const{
    return m_etat_isSet;
}

bool OAISubaccountAddResponse_etat::is_etat_Valid() const{
    return m_etat_isValid;
}

bool OAISubaccountAddResponse_etat::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_etat.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubaccountAddResponse_etat::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
